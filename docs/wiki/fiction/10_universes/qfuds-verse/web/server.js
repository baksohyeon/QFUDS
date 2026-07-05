// QFUDS Verse Codex — static server + optional Gemini archive-query proxy.
//
// Serves the static codex (index.html + assets) and exposes POST /api/query.
// The query route proxies to Google Gemini when GEMINI_API_KEY is set; with no
// key it returns 503 and the front-end shows a graceful "unavailable here"
// message. Behaves as a pure static site until you `dokku config:set … GEMINI_API_KEY=…`.
//
// Zero dependencies — Node's built-in http + fs only. Runs the same under
// Dokku, Docker, PM2, or systemd.

'use strict';

const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');

const ROOT = __dirname;
const PORT = process.env.PORT || 5000;
const KEY = process.env.GEMINI_API_KEY || '';
// Small, fast, free-tier friendly. Override via env if you like.
const MODEL = process.env.GEMINI_MODEL || 'gemini-2.0-flash';

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.woff2': 'font/woff2',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.ico': 'image/x-icon',
  '.map': 'application/json; charset=utf-8',
};

function send(res, code, body, headers) {
  res.writeHead(code, Object.assign({ 'Cache-Control': 'no-cache' }, headers));
  res.end(body);
}

// Serve a file safely (no path traversal outside ROOT).
function serveStatic(req, res) {
  let urlPath = decodeURIComponent((req.url.split('?')[0] || '/'));
  if (urlPath === '/') urlPath = '/index.html';
  const full = path.normalize(path.join(ROOT, urlPath));
  if (!full.startsWith(ROOT)) return send(res, 403, 'forbidden');
  fs.readFile(full, (err, data) => {
    if (err) {
      // SPA-ish fallback: unknown non-asset paths get the codex shell.
      if (!path.extname(full)) return serveIndex(res);
      return send(res, 404, 'not found');
    }
    const type = MIME[path.extname(full).toLowerCase()] || 'application/octet-stream';
    const cache = /\.(woff2|js|css)$/.test(full)
      ? 'public, max-age=604800'
      : 'no-cache';
    send(res, 200, data, { 'Content-Type': type, 'Cache-Control': cache });
  });
}

function serveIndex(res) {
  fs.readFile(path.join(ROOT, 'index.html'), (err, data) => {
    if (err) return send(res, 500, 'missing index.html');
    send(res, 200, data, { 'Content-Type': MIME['.html'] });
  });
}

function readBody(req, cap, cb) {
  let buf = '';
  let over = false;
  req.on('data', (c) => {
    buf += c;
    if (buf.length > cap) { over = true; req.destroy(); }
  });
  req.on('end', () => cb(over ? null : buf));
  req.on('error', () => cb(null));
}

// POST /api/query { system, messages:[{role,content}], max_tokens } -> { reply }
function handleQuery(req, res) {
  if (!KEY) {
    return send(res, 503, JSON.stringify({
      error: 'no_key',
      message: '이 서버에는 질의(Gemini) 키가 설정되지 않았어요. 관리자가 GEMINI_API_KEY를 설정하면 켜집니다.',
    }), { 'Content-Type': MIME['.json'] });
  }
  readBody(req, 200_000, async (raw) => {
    if (!raw) return send(res, 400, JSON.stringify({ error: 'bad_body' }), { 'Content-Type': MIME['.json'] });
    let body;
    try { body = JSON.parse(raw); } catch { return send(res, 400, JSON.stringify({ error: 'bad_json' }), { 'Content-Type': MIME['.json'] }); }
    const messages = Array.isArray(body.messages) ? body.messages : [];
    const maxTokens = Math.min(Number(body.max_tokens) || 1400, 8192);
    // Map to Gemini's generateContent shape.
    const contents = messages.map((m) => ({
      role: m.role === 'assistant' ? 'model' : 'user',
      parts: [{ text: String(m.content || '') }],
    }));
    const payload = {
      contents,
      generationConfig: { maxOutputTokens: maxTokens, temperature: 0.7 },
    };
    if (body.system) payload.system_instruction = { parts: [{ text: String(body.system) }] };

    const endpoint = `https://generativelanguage.googleapis.com/v1beta/models/${MODEL}:generateContent?key=${KEY}`;
    try {
      const r = await fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });
      const data = await r.json();
      if (!r.ok) {
        const msg = (data && data.error && data.error.message) || ('Gemini ' + r.status);
        return send(res, 502, JSON.stringify({ error: 'upstream', message: msg }), { 'Content-Type': MIME['.json'] });
      }
      const reply = (((data.candidates || [])[0] || {}).content || {}).parts
        ? data.candidates[0].content.parts.map((p) => p.text || '').join('')
        : '';
      send(res, 200, JSON.stringify({ reply: reply.trim() }), { 'Content-Type': MIME['.json'] });
    } catch (e) {
      send(res, 502, JSON.stringify({ error: 'fetch_failed', message: String(e && e.message || e) }), { 'Content-Type': MIME['.json'] });
    }
  });
}

const server = http.createServer((req, res) => {
  const url = (req.url || '/').split('?')[0];
  if (url === '/healthz') return send(res, 200, 'ok');
  if (url === '/api/query') {
    if (req.method !== 'POST') return send(res, 405, 'method not allowed');
    return handleQuery(req, res);
  }
  if (req.method !== 'GET' && req.method !== 'HEAD') return send(res, 405, 'method not allowed');
  serveStatic(req, res);
});

server.listen(PORT, () => {
  console.log(`[qfuds-codex] listening on :${PORT}  query=${KEY ? 'gemini:' + MODEL : 'disabled (no GEMINI_API_KEY)'}`);
});
