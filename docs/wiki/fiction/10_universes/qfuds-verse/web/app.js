/* QFUDS Verse — 세계관 코덱스
 * Standalone vanilla-JS port of the Claude Design prototype (DCLogic/React removed).
 * Behaviour, markup classes, and three.js scene are preserved 1:1 with the design.
 *
 * Data:   window.QFUDS_LORE (nodes + qa/promo system prompts)
 *         window.QFUDS_CHRONICLE (chapters / lives / system / dict)
 * Deps:   window.THREE (vendored, offline)
 * Query:  window.claude.complete (Claude preview) → POST ./api/query (Gemini proxy) → graceful fallback
 */
(function () {
  'use strict';

  var esc = function (s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  };
  var attr = function (s) { return esc(s).replace(/"/g, '&quot;'); };

  // ── optional "tweaks" (design-tool props) via URL params, else design defaults
  var qp = new URLSearchParams(location.search);
  var numOr = function (v, d) { var n = parseInt(v, 10); return isNaN(n) ? d : n; };
  var OPTS = {
    unlockAll: qp.get('unlockAll') === '1',
    autoRotate: qp.get('autoRotate') !== '0',
    starDensity: numOr(qp.get('starDensity'), 1100),
  };

  function Codex(rootEl) {
    this.ui = rootEl;
    this.stageEl = document.getElementById('stage');
    this.state = { ready: false, sel: null, termDef: null, intro: true, toast: null, view: 'graph', dictQ: '', ask: false, asking: false, seedsOpen: false, promo: false };
    this.qaMsgs = [];
    this.seeds = [];
    this.CAT = {
      era: { color: '#e8b34b', label: 'ERA · 시대' },
      faction: { color: '#5aa7ff', label: 'FACTION · 세력' },
      char: { color: '#ff7a6b', label: 'CHARACTER · 인물' },
      ideo: { color: '#b48cff', label: 'IDEOLOGY · 이념' },
      term: { color: '#3ad6a8', label: 'TERM · 용어' },
      saga: { color: '#f26fae', label: 'SAGA · 이야기(부)' },
    };
    this.SUGS = ['Salt Fires가 뭐야?', '사엘 이야기 쉽게 요약해줘', 'Q-Day가 21세기야 먼 미래야?', '복원이랑 부활이 뭐가 달라?'];
    this.boot();
  }

  Codex.prototype.boot = function () {
    try { this.seeds = JSON.parse(localStorage.getItem('qfuds-codex-seeds') || '[]'); } catch (e) { this.seeds = []; }
    this.read = new Set();
    this.unlocked = new Set();
    this.pulse = {};
    this.loadProgress();
    if (localStorage.getItem('qfuds-codex-intro')) this.state.intro = false;
    this.bindDelegates();
    this.waitLibs();
  };

  Codex.prototype.waitLibs = function () {
    var self = this;
    if (window.THREE && window.QFUDS_LORE && window.QFUDS_CHRONICLE && this.stageEl) { this.init(); return; }
    this._wait = setTimeout(function () { self.waitLibs(); }, 120);
  };

  // ── progress persistence ──────────────────────────────────────────────
  Codex.prototype.loadProgress = function () {
    try {
      var s = JSON.parse(localStorage.getItem('qfuds-codex-progress') || 'null');
      if (s) { this.read = new Set(s.read); this.unlocked = new Set(s.unlocked); }
    } catch (e) {}
    if (!this.unlocked.size) this.unlocked.add('btc-2008');
  };
  Codex.prototype.saveProgress = function () {
    localStorage.setItem('qfuds-codex-progress', JSON.stringify({ read: Array.from(this.read), unlocked: Array.from(this.unlocked) }));
  };
  Codex.prototype.isUnlocked = function (id) { return OPTS.unlockAll || this.unlocked.has(id); };

  // ── lightweight reactivity ────────────────────────────────────────────
  Codex.prototype.setState = function (patch, cb) {
    for (var k in patch) this.state[k] = patch[k];
    this.render();
    if (cb) cb();
  };
  Codex.prototype.forceUpdate = function () { this.render(); };

  // ── three.js scene ────────────────────────────────────────────────────
  Codex.prototype.init = function () {
    var THREE = window.THREE;
    var nodes = window.QFUDS_LORE.nodes;
    this.nodes = nodes;
    this.byId = {}; var self = this;
    nodes.forEach(function (n) { self.byId[n.id] = n; });
    this.adj = {}; nodes.forEach(function (n) { self.adj[n.id] = new Set(); });
    nodes.forEach(function (n) { (n.links || []).forEach(function (l) { if (self.byId[l]) { self.adj[n.id].add(l); self.adj[l].add(n.id); } }); });

    var eras = nodes.filter(function (n) { return n.cat === 'era'; }).sort(function (a, b) { return a.idx - b.idx; });
    this.eraList = eras;
    var epos = {};
    eras.forEach(function (e) {
      var t = e.idx;
      epos[e.id] = new THREE.Vector3((t - 8) * 78, Math.sin(t * 0.75) * 34, Math.cos(t * 0.5) * 46);
    });
    var hash = function (s) { var h = 2166136261; for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); } return (h >>> 0); };
    this.pos = {};
    nodes.forEach(function (n) {
      if (n.cat === 'era') { self.pos[n.id] = epos[n.id]; return; }
      var a = epos[n.era] || new THREE.Vector3();
      var h = hash(n.id);
      var ang = (h % 628) / 100;
      var r = 38 + (h % 30);
      var lift = { faction: 42, char: -8, ideo: 26, term: -38, saga: 74 }[n.cat] || 0;
      self.pos[n.id] = new THREE.Vector3(
        a.x + Math.cos(ang) * r * 0.55,
        a.y + lift + Math.sin(h % 97) * 14,
        a.z + Math.sin(ang) * r
      );
    });

    var scene = new THREE.Scene();
    scene.fog = new THREE.Fog(0x05070d, 1100, 2600);
    this.scene = scene;
    var w = this.stageEl.clientWidth, h = this.stageEl.clientHeight;
    this.camera = new THREE.PerspectiveCamera(52, w / h, 1, 5000);
    this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false });
    this.renderer.setSize(w, h);
    this.renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
    this.renderer.setClearColor(0x05070d);
    this.stageEl.appendChild(this.renderer.domElement);

    var density = Math.round(OPTS.starDensity);
    var sp = new Float32Array(density * 3);
    for (var i = 0; i < density; i++) {
      var v = new THREE.Vector3().randomDirection().multiplyScalar(900 + Math.random() * 1400);
      sp[i * 3] = v.x; sp[i * 3 + 1] = v.y; sp[i * 3 + 2] = v.z;
    }
    var sg = new THREE.BufferGeometry();
    sg.setAttribute('position', new THREE.BufferAttribute(sp, 3));
    scene.add(new THREE.Points(sg, new THREE.PointsMaterial({ color: 0x2e3d5c, size: 1.6, sizeAttenuation: true })));

    var curve = new THREE.CatmullRomCurve3(eras.map(function (e) { return epos[e.id]; }));
    var spineGeo = new THREE.BufferGeometry().setFromPoints(curve.getPoints(240));
    scene.add(new THREE.Line(spineGeo, new THREE.LineBasicMaterial({ color: 0x18243d, transparent: true, opacity: 0.9 })));

    this.sprites = {};
    nodes.forEach(function (n) {
      var sprite = new THREE.Sprite(new THREE.SpriteMaterial({ transparent: true, depthTest: true }));
      sprite.position.copy(self.pos[n.id]);
      sprite.userData.id = n.id;
      sprite.scale.set(50, 25, 1);
      scene.add(sprite);
      self.sprites[n.id] = sprite;
    });
    this.linkGroup = new THREE.Group();
    scene.add(this.linkGroup);

    var focusId = 'btc-2008';
    this.eraList.forEach(function (e) { if (self.isUnlocked(e.id)) focusId = e.id; });
    var fp = this.pos[focusId] || new THREE.Vector3(0, 0, 0);
    this.orb = { theta: 0.55, phi: 1.15, radius: 420, target: fp.clone() };
    this.goal = { theta: 0.55, phi: 1.15, radius: 420, target: fp.clone() };
    this.bindInput();
    this.refreshAll();
    this.state.ready = true;
    this.render();
    this.lastInteract = Date.now();
    var loop = function () { self.raf = requestAnimationFrame(loop); self.animate(); };
    loop();
    this._onResize = function () {
      var w2 = self.stageEl.clientWidth, h2 = self.stageEl.clientHeight;
      self.camera.aspect = w2 / h2; self.camera.updateProjectionMatrix();
      self.renderer.setSize(w2, h2);
    };
    window.addEventListener('resize', this._onResize);
  };

  Codex.prototype.nodeState = function (id) {
    if (this.isUnlocked(id)) return 'open';
    var it = this.adj[id].values(), r;
    while (!(r = it.next()).done) if (this.isUnlocked(r.value)) return 'signal';
    return 'hidden';
  };

  Codex.prototype.makeTexture = function (n, st) {
    var THREE = window.THREE;
    var c = document.createElement('canvas'); c.width = 512; c.height = 256;
    var x = c.getContext('2d');
    var color = st === 'open' ? this.CAT[n.cat].color : '#4a5670';
    var g = x.createRadialGradient(256, 72, 2, 256, 72, 46);
    g.addColorStop(0, color); g.addColorStop(0.35, color + 'aa'); g.addColorStop(1, 'rgba(0,0,0,0)');
    x.fillStyle = g; x.fillRect(150, 0, 212, 150);
    x.beginPath(); x.arc(256, 72, st === 'open' ? 9 : 6, 0, 7); x.fillStyle = st === 'open' ? '#ffffff' : '#6b7896'; x.fill();
    if (st === 'signal') { x.beginPath(); x.arc(256, 72, 18, 0, 7); x.strokeStyle = '#4a5670'; x.setLineDash([4, 5]); x.lineWidth = 2; x.stroke(); x.setLineDash([]); }
    x.textAlign = 'center';
    if (st === 'open') {
      x.font = '600 42px "IBM Plex Sans KR", sans-serif';
      x.fillStyle = '#eef4ff'; x.shadowColor = 'rgba(0,0,0,.9)'; x.shadowBlur = 10;
      x.fillText(n.title, 256, 168);
      x.font = '400 23px "IBM Plex Mono", monospace';
      x.fillStyle = color; x.fillText((n.sub || '').split('·')[0].trim().slice(0, 26), 256, 206);
    } else {
      x.font = '500 26px "IBM Plex Mono", monospace';
      x.fillStyle = '#5a6884'; x.fillText('미확인 신호', 256, 172);
    }
    var t = new THREE.CanvasTexture(c);
    t.anisotropy = 4;
    return t;
  };

  Codex.prototype.refreshAll = function () {
    var self = this;
    this.nodes.forEach(function (n) {
      var st = self.nodeState(n.id);
      var sp = self.sprites[n.id];
      if (st === 'hidden') { sp.visible = false; return; }
      sp.visible = true;
      if (sp.userData.st !== st) {
        if (sp.material.map) sp.material.map.dispose();
        sp.material.map = self.makeTexture(n, st);
        sp.material.needsUpdate = true;
        sp.userData.st = st;
        var base = st === 'open' ? (n.cat === 'era' ? 60 : 46) : 34;
        sp.userData.base = base;
        sp.scale.set(base, base / 2, 1);
      }
    });
    while (this.linkGroup.children.length) {
      var l = this.linkGroup.children.pop();
      l.geometry.dispose(); l.material.dispose();
    }
    var solid = [], faint = [], seen = new Set();
    this.nodes.forEach(function (n) {
      self.adj[n.id].forEach(function (m) {
        var k = n.id < m ? n.id + '|' + m : m + '|' + n.id;
        if (seen.has(k)) return; seen.add(k);
        var a = self.nodeState(n.id), b = self.nodeState(m);
        if (a === 'hidden' || b === 'hidden') return;
        var arr = (a === 'open' && b === 'open') ? solid : faint;
        arr.push(self.pos[n.id], self.pos[m]);
      });
    });
    var mk = function (pts, color, op) {
      if (!pts.length) return;
      var g = new window.THREE.BufferGeometry().setFromPoints(pts);
      self.linkGroup.add(new window.THREE.LineSegments(g, new window.THREE.LineBasicMaterial({ color: color, transparent: true, opacity: op })));
    };
    mk(solid, 0x3a5f8f, 0.55);
    mk(faint, 0x22304e, 0.3);
  };

  Codex.prototype.bindInput = function () {
    var self = this, el = this.stageEl;
    var down = null, moved = false;
    var touches = new Map();
    var pinchDist = null;
    el.addEventListener('pointerdown', function (e) {
      touches.set(e.pointerId, { x: e.clientX, y: e.clientY });
      if (touches.size === 2) {
        var vs = [].slice.call(touches.values());
        pinchDist = Math.hypot(vs[0].x - vs[1].x, vs[0].y - vs[1].y);
        down = null; return;
      }
      down = { x: e.clientX, y: e.clientY, t: self.goal.theta, p: self.goal.phi };
      moved = false; el.classList.add('drag'); self.lastInteract = Date.now();
    });
    window.addEventListener('pointermove', function (e) {
      if (touches.has(e.pointerId)) touches.set(e.pointerId, { x: e.clientX, y: e.clientY });
      if (touches.size === 2 && pinchDist) {
        var vs = [].slice.call(touches.values());
        var d = Math.hypot(vs[0].x - vs[1].x, vs[0].y - vs[1].y);
        if (d > 0) self.goal.radius = Math.min(1600, Math.max(120, self.goal.radius * (pinchDist / d)));
        pinchDist = d; self.lastInteract = Date.now(); return;
      }
      if (!down) { self.hover(e); return; }
      var dx = e.clientX - down.x, dy = e.clientY - down.y;
      if (Math.abs(dx) + Math.abs(dy) > 6) moved = true;
      self.goal.theta = down.t - dx * 0.005;
      self.goal.phi = Math.min(2.6, Math.max(0.4, down.p - dy * 0.005));
      self.lastInteract = Date.now();
    });
    window.addEventListener('pointerup', function (e) {
      touches.delete(e.pointerId);
      if (touches.size < 2) pinchDist = null;
      el.classList.remove('drag');
      if (down && !moved) self.pick(e);
      down = null;
    });
    window.addEventListener('pointercancel', function (e) { touches.delete(e.pointerId); pinchDist = null; down = null; el.classList.remove('drag'); });
    el.style.touchAction = 'none';
    el.addEventListener('wheel', function (e) {
      e.preventDefault();
      self.goal.radius = Math.min(1600, Math.max(120, self.goal.radius * (1 + e.deltaY * 0.001)));
      self.lastInteract = Date.now();
    }, { passive: false });
  };

  Codex.prototype.ray = function (e) {
    var THREE = window.THREE;
    var r = this.renderer.domElement.getBoundingClientRect();
    var v = new THREE.Vector2(((e.clientX - r.left) / r.width) * 2 - 1, -((e.clientY - r.top) / r.height) * 2 + 1);
    var rc = new THREE.Raycaster();
    rc.setFromCamera(v, this.camera);
    var vis = Object.keys(this.sprites).map(function (k) { return this.sprites[k]; }, this).filter(function (s) { return s.visible; });
    var hits = rc.intersectObjects(vis);
    return hits.length ? hits[0].object.userData.id : null;
  };
  Codex.prototype.hover = function (e) {
    if (!this.renderer) return;
    var id = this.ray(e);
    this.stageEl.style.cursor = id ? 'pointer' : 'grab';
  };
  Codex.prototype.pick = function (e) {
    if (!this.renderer) return;
    var id = this.ray(e);
    if (id) this.open(id);
  };

  Codex.prototype.open = function (id) {
    this.setState({ sel: id, termDef: null });
    this.flyTo(id, 300);
  };
  Codex.prototype.flyTo = function (id, radius) {
    var p = this.pos[id];
    if (!p) return;
    this.goal.target = p.clone();
    if (radius) this.goal.radius = Math.min(this.goal.radius, radius);
    this.lastInteract = Date.now();
  };

  Codex.prototype.showToast = function (msg) {
    var self = this;
    clearTimeout(this._toastT);
    this.setState({ toast: msg });
    this._toastT = setTimeout(function () { self.setState({ toast: null }); }, 2600);
  };

  Codex.prototype.doRead = function () {
    var id = this.state.sel, self = this;
    if (!id || this.read.has(id)) return;
    this.read.add(id);
    this.unlocked.add(id);
    var fresh = 0;
    this.adj[id].forEach(function (nb) { if (!self.unlocked.has(nb)) { self.unlocked.add(nb); self.pulse[nb] = performance.now(); fresh++; } });
    this.saveProgress();
    this.refreshAll();
    this.showToast(fresh ? '⟐ 신호 ' + fresh + '건 해금' : '⟐ 판독 기록됨');
    this.forceUpdate();
  };

  Codex.prototype.doReset = function () {
    var self = this;
    if (!this._confirmReset) {
      this._confirmReset = true;
      this.showToast('다시 누르면 초기화됩니다');
      clearTimeout(this._resetT);
      this._resetT = setTimeout(function () { self._confirmReset = false; self.forceUpdate(); }, 3000);
      this.forceUpdate();
      return;
    }
    this._confirmReset = false;
    clearTimeout(this._resetT);
    this.read = new Set(); this.unlocked = new Set(['btc-2008']); this.pulse = {};
    localStorage.removeItem('qfuds-codex-progress');
    if (this.nodes) this.refreshAll();
    this.setState({ sel: null, termDef: null });
    if (this.goal) { this.goal.target = new window.THREE.Vector3(-620, 0, 0); this.goal.radius = 420; }
    this.showToast('⟲ 초기화 완료 — 비트코인부터 다시');
  };

  Codex.prototype.animate = function () {
    var o = this.orb, g = this.goal, k = 0.07;
    if (OPTS.autoRotate) { if (Date.now() - this.lastInteract > 4000) g.theta += 0.00045; }
    o.theta += (g.theta - o.theta) * k;
    o.phi += (g.phi - o.phi) * k;
    o.radius += (g.radius - o.radius) * k;
    o.target.lerp(g.target, k);
    var c = this.camera;
    c.position.set(
      o.target.x + o.radius * Math.sin(o.phi) * Math.sin(o.theta),
      o.target.y + o.radius * Math.cos(o.phi),
      o.target.z + o.radius * Math.sin(o.phi) * Math.cos(o.theta)
    );
    c.lookAt(o.target);
    var now = performance.now();
    for (var id in this.pulse) {
      var dt = (now - this.pulse[id]) / 1000;
      var sp = this.sprites[id];
      if (dt > 2.4) { delete this.pulse[id]; if (sp && sp.userData.base) sp.scale.set(sp.userData.base, sp.userData.base / 2, 1); continue; }
      if (sp && sp.userData.base) {
        var s = sp.userData.base * (1 + 0.3 * Math.sin(dt * 6) * Math.exp(-dt * 1.4));
        sp.scale.set(s, s / 2, 1);
      }
    }
    this.renderer.render(this.scene, this.camera);
  };

  // ── archive query (Claude preview → Gemini proxy → fallback) ───────────
  Codex.prototype.askArchive = function (opts) {
    if (window.claude && window.claude.complete) {
      return window.claude.complete({ model: 'claude-sonnet-4-5', max_tokens: opts.max_tokens, system: opts.system, messages: opts.messages });
    }
    return fetch('./api/query', {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ system: opts.system, messages: opts.messages, max_tokens: opts.max_tokens }),
    }).then(function (res) {
      return res.json().catch(function () { return {}; }).then(function (data) {
        if (!res.ok) { var e = new Error(data.message || ('HTTP ' + res.status)); e.code = data.error; throw e; }
        return data.reply || '';
      });
    });
  };

  Codex.prototype.sendQuery = function (q) {
    var self = this;
    var text = (q || (this.qaInput ? this.qaInput.value : '')).trim();
    if (!text || this.state.asking) return;
    if (this.qaInput) this.qaInput.value = '';
    if (!this.qaMsgs.length || !this.sessionId) {
      this.sessionId = 's' + Date.now().toString(36);
      this.sessionLabel = text.slice(0, 30);
    }
    this.qaMsgs.push({ role: 'user', content: text, sid: this.sessionId });
    var promo = !!this.state.promo;
    var sys = promo ? window.QFUDS_LORE.promoContext : window.QFUDS_LORE.qaContext;
    var cap = promo ? 4000 : 1400;
    this.setState({ asking: true }, function () { self.scrollQa(); });
    this.askArchive({
      max_tokens: cap, system: sys,
      messages: this.qaMsgs.filter(function (m) { return !m.err; }).map(function (m) { return { role: m.role, content: m.content }; }),
    }).then(function (reply) {
      self.qaMsgs.push({ role: 'assistant', content: reply, promo: promo, sid: self.sessionId });
      self.setState({ asking: false }, function () { self.scrollQa(); });
    }).catch(function (e) {
      var msg;
      if (e && e.code === 'no_key') msg = e.message;
      else if (e && /Failed to fetch|NetworkError|fetch_failed/.test(String(e && (e.message || e.code)))) msg = '이 환경에서는 질의 기능을 쓸 수 없어요. 클로드 미리보기 안에서 열거나, 홈서버에 GEMINI_API_KEY를 설정하면 동작합니다.';
      else msg = '질의에 실패했어요. 잠시 후 다시 시도해 주세요' + (e && e.message ? ' (' + e.message + ')' : '.');
      self.qaMsgs.push({ role: 'assistant', content: msg, err: true });
      self.setState({ asking: false }, function () { self.scrollQa(); });
    });
  };

  // ── doc builders (chronicle / system / lives / dict) ───────────────────
  Codex.prototype.chronStBadge = function (st) {
    var ST = { canon: ['캐논', 'st-canon'], dir: ['캐논 방향', 'st-dir'], cand: ['후보·보류', 'st-cand'], prop: ['제안', 'st-prop'], tbd: ['미정', 'st-tbd'] };
    var s = ST[st] || ST.tbd;
    return '<span class="tagb ' + s[1] + '">' + s[0] + '</span>';
  };
  Codex.prototype.nodeChips = function (ids) {
    if (!ids || !ids.length) return '';
    var by = this.byId || {};
    return '<div class="nodechips">' + ids.map(function (id) {
      var n = by[id];
      return '<button class="chip-node" data-node="' + attr(id) + '">⟐ ' + esc(n ? n.title : id) + '</button>';
    }).join('') + '</div>';
  };
  Codex.prototype.buildChron = function () {
    if (this._chronHtml) return this._chronHtml;
    var C = window.QFUDS_CHRONICLE, self = this;
    if (!C) return '<p style="color:#5f7396">연대기 데이터 로딩 중…</p>';
    var h = '';
    C.chapters.forEach(function (ch) {
      h += '<section class="chp" id="' + attr(ch.id) + '"><div class="chp-era">' + esc(ch.era) + '</div><div class="chp-time">' + esc(ch.time) + '</div><h2 class="chp-title">' + esc(ch.title) + '</h2>';
      if (ch.intro) h += '<div class="chp-intro">' + ch.intro + '</div>';
      ch.entries.forEach(function (e) {
        h += '<div class="ent ' + (e.st === 'canon' ? 'canon' : '') + '"><div class="ent-head"><span class="ent-t">' + esc(e.t) + '</span><span class="tagb tag-scope">' + esc(e.scope) + '</span>' + self.chronStBadge(e.st) + '</div><h3 class="ent-title">' + esc(e.title) + '</h3><div class="ent-body">' + e.html + '</div>' + self.nodeChips(e.nodes) + '</div>';
      });
      h += '</section>';
    });
    this._chronHtml = h;
    return h;
  };
  Codex.prototype.buildSystem = function () {
    if (this._sysHtml) return this._sysHtml;
    var C = window.QFUDS_CHRONICLE;
    if (!C || !C.system) return '<p style="color:#5f7396">체계 데이터 로딩 중…</p>';
    var S = C.system, h = '<div class="dg-title">붕괴·재구성 사슬</div>';
    S.chains.forEach(function (ch) {
      h += '<div class="sys-chain ' + ch.kind + '"><div class="sys-ct">' + esc(ch.title) + '</div>';
      ch.steps.forEach(function (st, i) {
        if (i > 0) h += '<div class="sys-arrow">↓</div>';
        h += '<div class="sys-step"><span class="sys-num">' + (i + 1) + '</span><span>' + esc(st) + '</span></div>';
      });
      h += '</div>';
    });
    h += '<div class="sys-cross">' + S.crossNote + '</div>';
    h += '<div class="dg-title">14개 도메인 — 무너진 뒤 무엇이 새 권력이 되었나</div>';
    S.domains.forEach(function (d) {
      var vc = d.v.indexOf('V') >= 0 ? 'vV' : (d.v.indexOf('G') >= 0 ? 'vG' : 'vE');
      h += '<div class="dom"><div class="dom-head"><span class="dom-n">' + esc(d.n) + '</span><span class="dom-name">' + esc(d.name) + '</span><span class="dom-v ' + vc + '">' + esc(d.v) + '</span></div>';
      h += '<div class="dom-line"><div class="dom-k">끊긴 기둥</div><div class="dom-val broke">' + esc(d.broke) + '</div></div>';
      h += '<div class="dom-line"><div class="dom-k">새 권력</div><div class="dom-val">' + esc(d.power) + '</div></div>';
      h += '<div class="dom-line"><div class="dom-k">앵커</div><div class="dom-val">' + esc(d.anchor) + '</div></div>';
      h += '<div class="dom-line"><div class="dom-k">스파이스</div><div class="dom-val">' + esc(d.spice) + '</div></div>';
      h += '</div>';
    });
    this._sysHtml = h;
    return h;
  };
  Codex.prototype.buildLives = function () {
    if (this._livesHtml) return this._livesHtml;
    var C = window.QFUDS_CHRONICLE, self = this;
    if (!C || !C.lives) return '<p style="color:#5f7396">인물 데이터 로딩 중…</p>';
    var h = '';
    C.lives.forEach(function (band) {
      h += '<div class="lband"><div class="lband-name">' + esc(band.band) + '</div><div class="lband-when">' + esc(band.when) + '</div></div>';
      band.figs.forEach(function (f) {
        h += '<div class="fig ' + (f.st === 'canon' ? 'canon' : '') + '"><div class="fig-head"><span class="fig-name">' + esc(f.name) + '</span>' + self.chronStBadge(f.st) + '<span class="fig-role">' + esc(f.role) + '</span>' + (f.node ? '<button class="fig-node" data-node="' + attr(f.node) + '">⟐ 성좌</button>' : '') + '</div>';
        h += '<div class="fig-line"><div class="fig-k">그때 상태</div><div class="fig-v">' + f.state + '</div></div>';
        h += '<div class="fig-line"><div class="fig-k">그때 성격</div><div class="fig-v">' + f.character + '</div></div>';
        h += '<div class="fig-line"><div class="fig-k">서사</div><div class="fig-v">' + f.arc + '</div></div>';
        h += '</div>';
      });
    });
    this._livesHtml = h;
    return h;
  };
  Codex.prototype.buildDict = function (q) {
    var C = window.QFUDS_CHRONICLE, self = this;
    if (!C) return '';
    var ql = (q || '').trim().toLowerCase();
    var h = '', lastG = null, any = false;
    C.dict.forEach(function (d) {
      if (ql && (d.title + ' ' + (d.sub || '') + ' ' + d.html).toLowerCase().indexOf(ql) < 0) return;
      any = true;
      if (d.g !== lastG) { h += '<div class="dg-title">' + esc(d.g) + '</div>'; lastG = d.g; }
      h += '<div class="dent"><div class="dent-head"><h3 class="dent-title">' + esc(d.title) + '</h3><span class="dent-sub">' + esc(d.sub || '') + '</span>' + self.chronStBadge(d.st) + '</div><div class="ent-body">' + d.html + '</div></div>';
    });
    if (!any) h = '<p style="color:#5f7396">「' + esc(q || '') + '」에 해당하는 항목이 없어요.</p>';
    return h;
  };

  // ── seed vault ─────────────────────────────────────────────────────────
  Codex.prototype.saveSeed = function (idx) {
    var a = this.qaMsgs[idx];
    if (!a || a.role !== 'assistant') return;
    var sid = a.sid || 's0', q = '';
    for (var i = idx - 1; i >= 0; i--) if (this.qaMsgs[i].role === 'user') { q = this.qaMsgs[i].content; break; }
    var thread = [];
    for (var j = 0; j <= idx; j++) {
      var m = this.qaMsgs[j];
      if (m.err) continue;
      if ((m.sid || 's0') === sid) thread.push({ role: m.role, content: m.content });
    }
    var label = this.sessionLabel || q.slice(0, 30);
    var existing = -1;
    for (var e = 0; e < this.seeds.length; e++) if (this.seeds[e].sid === sid) { existing = e; break; }
    var seed = { sid: sid, label: label, thread: thread, q: q, a: a.content, promo: !!a.promo, turns: thread.filter(function (m) { return m.role === 'user'; }).length, t: Date.now() };
    if (existing >= 0 && thread.length >= (this.seeds[existing].thread || []).length) {
      this.seeds[existing] = seed;
      this.showToast('🌱 세션 시드 갱신 · 맥락 ' + seed.turns + '턴');
    } else {
      this.seeds.push(seed);
      this.showToast('🌱 시드 저장 · 세션 맥락 ' + seed.turns + '턴 포함');
    }
    localStorage.setItem('qfuds-codex-seeds', JSON.stringify(this.seeds));
    this.forceUpdate();
  };
  Codex.prototype.delSeed = function (i) {
    this.seeds.splice(i, 1);
    localStorage.setItem('qfuds-codex-seeds', JSON.stringify(this.seeds));
    this.forceUpdate();
  };
  Codex.prototype.saveDoc = function (idx) {
    var m = this.qaMsgs[idx];
    if (!m) return;
    var body = m.content.trim();
    body = body.replace(/^```[a-z]*\s*\n/i, '').replace(/\n```\s*$/i, '').trim();
    var fm = body.match(/doc_id:\s*([a-z0-9_]+)/i);
    var name = (fm ? fm[1] : 'qfuds_promotion_draft') + '.md';
    this._download(name, body + '\n');
    this.showToast('⇩ ' + name + ' 저장됨');
  };
  Codex.prototype.exportSeeds = function () {
    var d = new Date();
    var pad = function (n) { return String(n).padStart(2, '0'); };
    var stamp = d.getFullYear() + pad(d.getMonth() + 1) + pad(d.getDate());
    var md = '# QFUDS Verse 세계관 시드 로그\n\n생성: ' + d.toISOString().slice(0, 10) + ' · 세션 ' + this.seeds.length + '건 (대화 맥락 단위)\n\n';
    this.seeds.forEach(function (s, i) {
      md += '## 세션 ' + (i + 1) + ' · ' + (s.label || s.q) + '\n\n';
      if (s.thread && s.thread.length) {
        s.thread.forEach(function (m) { md += (m.role === 'user' ? '**Q.** ' : '**A.** ') + m.content.trim() + '\n\n'; });
      } else {
        md += '**Q.** ' + s.q + '\n\n**A.** ' + s.a + '\n\n';
      }
      md += '---\n\n';
    });
    this._download('qfuds-seeds-' + stamp + '.md', md);
  };
  Codex.prototype._download = function (name, text) {
    var blob = new Blob([text], { type: 'text/markdown' });
    var a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = name;
    a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); }, 5000);
  };
  Codex.prototype.stripMd = function (t) {
    return String(t)
      .replace(/^#{1,4}\s*/gm, '')
      .replace(/\*\*([^*]+)\*\*/g, '$1')
      .replace(/\*([^*]+)\*/g, '$1')
      .replace(/^[-*]\s+/gm, '· ');
  };
  Codex.prototype.scrollQa = function () {
    if (this.qaBody) this.qaBody.scrollTop = this.qaBody.scrollHeight;
  };

  // ── render (imperative mirror of the DCLogic template) ─────────────────
  Codex.prototype.render = function () {
    var s = this.state, self = this;
    var total = this.nodes ? this.nodes.length : 0;
    var readCount = OPTS.unlockAll ? total : (this.read ? this.read.size : 0);
    var unlockCount = OPTS.unlockAll ? total : (this.unlocked ? this.unlocked.size : 0);
    var pct = total ? Math.round(readCount / total * 100) : 0;
    var H = [];

    // HUD
    H.push('<div class="hud"><div class="hud-title">QFUDS VERSE</div><div class="hud-sub">세계관 코덱스 · DEEP-TIME CODEX</div>' +
      '<div class="pbar"><div class="pfill" style="width:' + pct + '%"></div></div>' +
      '<div class="ptext mono">판독 ' + readCount + ' / ' + total + ' · 해금 ' + unlockCount + '</div>' +
      '<button class="reset" data-act="reset">' + (this._confirmReset ? '정말 초기화?' : '진행 초기화') + '</button></div>');

    // legend
    H.push('<div class="legend">' +
      '<div class="lrow"><span class="ldot dot-era"></span>시대</div>' +
      '<div class="lrow"><span class="ldot dot-faction"></span>세력</div>' +
      '<div class="lrow"><span class="ldot dot-char"></span>인물</div>' +
      '<div class="lrow"><span class="ldot dot-ideo"></span>이념</div>' +
      '<div class="lrow"><span class="ldot dot-term"></span>용어</div>' +
      '<div class="lrow"><span class="ldot dot-saga"></span>이야기(부)</div></div>');

    // view tabs
    var tabs = [['graph', '⟐ 성좌'], ['chron', '≡ 연대기'], ['lives', '◇ 인물'], ['system', '⊞ 체계'], ['dict', '⌘ 사전']];
    H.push('<div class="vtabs">' + tabs.map(function (t) {
      return '<button class="vtab ' + (s.view === t[0] ? 'cur' : '') + '" data-act="tab" data-arg="' + t[0] + '">' + t[1] + '</button>';
    }).join('') + '</div>');

    // doc views
    var CH = window.QFUDS_CHRONICLE || {};
    if (s.view === 'chron') {
      H.push('<div class="doc" data-doc="1"><div class="doc-inner"><h1 class="doc-h1">QFUDS VERSE 연대기</h1>' +
        '<div class="doc-lead">2026 현재 기준선 → t+0 경첩의 밤 → 수억 년 · 9기 접근 — 시간 단위에서 은하년 단위까지의 정사(正史)와 후보 기록. ⟐ 칩을 누르면 성좌의 해당 기록으로 이동합니다.</div>' +
        this.buildChron() + '</div></div>');
    } else if (s.view === 'system') {
      H.push('<div class="doc" data-doc="1"><div class="doc-inner"><h1 class="doc-h1">세계-체계 · SYSTEM MATRIX</h1>' +
        '<div class="doc-lead">' + esc((CH.system && CH.system.note) || '') + '</div>' + this.buildSystem() + '</div></div>');
    } else if (s.view === 'lives') {
      H.push('<div class="doc" data-doc="1"><div class="doc-inner"><h1 class="doc-h1">인물 연표 · DRAMATIS PERSONAE</h1>' +
        '<div class="doc-lead">' + esc(CH.livesNote || '') + ' ⟐ 노드 칩을 누르면 성좌의 해당 인물로 이동합니다.</div>' + this.buildLives() + '</div></div>');
    } else if (s.view === 'dict') {
      H.push('<div class="doc" data-doc="1"><div class="doc-inner"><h1 class="doc-h1">세계 사전 · REGISTER</h1>' +
        '<div class="doc-lead">가문·조직 / 인물 후보 / 지명 / 사건명 / 어휘 / 경제 / 의례 / 교육 / 관계망 / 기술 인프라 — 대부분 「후보(보류)」 상태의 확장 레지스터이며, 캐논과 구분해 표기합니다.</div>' +
        '<input class="dsearch" id="dsearch" placeholder="검색 — 예: 베리디온, 세 이름, Vadis…" value="' + attr(s.dictQ) + '">' +
        '<div id="dictresults">' + this.buildDict(s.dictQ) + '</div></div></div>');
    }

    // ask button
    H.push('<button class="askbtn" data-act="toggleAsk">⌬ 아카이브에 질의</button>');

    // QA panel
    if (s.ask) H.push(this.renderQa());

    // hint + rail
    H.push('<div class="hint mono">드래그 회전 · 휠 확대 · 노드 클릭 = 판독</div>');
    H.push('<div class="rail">' + this.renderRail() + '</div>');

    // toast
    if (s.toast) H.push('<div class="toast">' + esc(s.toast) + '</div>');

    // selection panel
    H.push(this.renderPanel());

    // term popup
    if (s.termDef) H.push('<div class="pop"><div class="pop-t">용어 해설</div>' + esc(s.termDef) + '</div>');

    // intro
    if (s.intro) H.push('<div class="intro"><div class="icard"><div class="itag">INCOMING SIGNAL</div><h1>QFUDS VERSE</h1>' +
      '<p>미확인 아카이브에서 신호가 수신되었습니다.<br>기록을 <b>판독</b>하면 연결된 신호가 해금됩니다.<br>2008년, 하나의 좌표에서 시작합니다.</p>' +
      '<button class="ibtn" data-act="begin">판독 시작</button></div></div>');

    this.ui.innerHTML = H.join('');
    this.postRender();
  };

  Codex.prototype.renderRail = function () {
    var self = this, s = this.state;
    if (!this.nodes) return '';
    return this.eraList.map(function (e) {
      var st = self.nodeState(e.id);
      var open = st === 'open';
      var label = open ? e.title.replace(/ ·.*/, '') : '░░░';
      var cls = (open ? '' : 'lk') + (s.sel === e.id ? ' cur' : '');
      return '<button class="echip ' + cls + '"' + (st !== 'hidden' ? ' data-act="open" data-arg="' + attr(e.id) + '"' : '') + '>' + esc(label) + '</button>';
    }).join('');
  };

  Codex.prototype.renderPanel = function () {
    var s = this.state;
    if (!this.nodes) return '';
    var n = s.sel ? this.byId[s.sel] : null;
    if (!n) return '';
    var st = this.nodeState(n.id);
    var open = st === 'open';
    var badgeCls = open ? 'bg-' + n.cat : 'bg-lock';
    var catLabel = open ? this.CAT[n.cat].label : 'LOCKED';
    var title = open ? n.title : '암호화된 기록';
    var sub = open ? n.sub : 'ENCRYPTED · SIGNAL ONLY';
    var h = '<aside class="panel"><div class="phead"><span class="badge ' + badgeCls + '">' + esc(catLabel) + '</span><button class="pclose" data-act="closePanel">✕</button></div>' +
      '<div class="pbody" data-panel="1"><h2>' + esc(title) + '</h2><div class="psub">' + esc(sub) + '</div>';
    if (!open) {
      h += '<div class="lockbox">⬡ 암호화된 기록<br>인접한 기록을 판독하면 이 신호가 해금됩니다.</div>';
    } else {
      h += '<div class="lore">' + n.body + '</div>';
      var unread = !OPTS.unlockAll && !this.read.has(n.id);
      if (unread) h += '<button class="readbtn" data-act="markRead">⟐ 판독 완료 — 연결 신호 해금</button>';
      else h += '<div class="donetag">— 판독 완료된 기록 —</div>';
      h += '<div class="relh">CONNECTED SIGNALS</div>';
      var self = this;
      [].slice.call(this.adj[n.id]).forEach(function (id) {
        var m = self.byId[id];
        var mo = self.nodeState(id) === 'open';
        h += '<button class="rel ' + (mo ? '' : 'lk') + '" data-act="open" data-arg="' + attr(id) + '"><span class="ldot ' + (mo ? 'dot-' + m.cat : '') + '"></span>' + esc(mo ? m.title : '░░░ 암호화된 신호') + '</button>';
      });
    }
    h += '</div></aside>';
    return h;
  };

  Codex.prototype.renderQa = function () {
    var s = this.state, self = this;
    var seedCount = this.seeds ? this.seeds.length : 0;
    var head = '<div class="qa-head"><span class="qa-title">아카이브 질의</span><div class="fx ac">' +
      '<button class="seedhead-btn" data-act="newSession">＋ 새 세션</button>' +
      '<button class="seedhead-btn" data-act="toggleSeeds">🌱 시드 ' + seedCount + '</button>' +
      '<button class="pclose" data-act="toggleAsk">✕</button></div></div>';
    var body;
    if (s.seedsOpen) {
      var rows = (this.seeds || []).map(function (sd, i) {
        return { i: i, label: sd.label || sd.q, turns: (sd.turns || 1) + '턴',
          a: (sd.thread && sd.thread.length ? sd.thread : [{ role: 'user', content: sd.q }, { role: 'assistant', content: sd.a }]).map(function (m) { return (m.role === 'user' ? 'Q. ' : 'A. ') + m.content; }).join('\n\n') };
      }).reverse();
      body = '<div class="qa-body"><div class="qa-note" style="padding:0 0 10px">대화 맥락(세션) 단위로 저장된 시드입니다. 같은 세션에서 다시 저장하면 갱신돼요. 내보내기 .md에는 세션별 전체 질의응답이 담겨, 다음 작업(레포 커밋·다른 대화)의 재료가 됩니다.</div>';
      if (seedCount) body += '<button class="readbtn" data-act="exportSeeds">⇩ 시드 ' + seedCount + '건 .md로 내보내기</button>';
      body += rows.map(function (sd) {
        return '<div class="seedrow"><button class="seeddel" data-act="delSeed" data-arg="' + sd.i + '">삭제</button>' +
          '<div class="seedq"><span class="seedturns">세션 · ' + esc(sd.turns) + '</span> ' + esc(sd.label) + '</div>' +
          '<div class="seeda">' + esc(sd.a) + '</div></div>';
      }).join('');
      if (!seedCount) body += '<div class="lockbox">아직 저장된 시드가 없어요.<br>답변 아래 「🌱 시드로 저장」을 누르면 여기에 쌓입니다.</div>';
      body += '</div>';
    } else {
      var msgs = (this.qaMsgs || []).map(function (m, i) {
        var text = m.promo ? m.content : self.stripMd(m.content);
        var cls = (m.err ? 'msg-e' : (m.role === 'user' ? 'msg-u' : 'msg-a')) + (m.promo ? ' promo-msg' : '');
        var canSave = m.role === 'assistant' && !m.err;
        var inner = esc(text);
        if (canSave) {
          inner += '<div class="fx wrap"><button class="seedbtn" data-act="saveSeed" data-arg="' + i + '">🌱 시드로 저장</button>';
          if (m.promo) inner += '<button class="savedoc" data-act="saveDoc" data-arg="' + i + '">⇩ 이 초안 .md로 저장</button>';
          inner += '</div>';
        }
        return '<div class="msg ' + cls + '">' + inner + '</div>';
      }).join('');
      var thinking = s.asking ? '<div class="thinking">판독 중…</div>' : '';
      var sugs = this.SUGS.map(function (q, i) { return '<button class="sug" data-act="sug" data-arg="' + i + '">' + esc(q) + '</button>'; }).join('');
      var promoCls = s.promo ? 'on' : '';
      var promoLabel = s.promo ? '승격 모드 ON' : '승격 모드';
      var promoHint = s.promo ? '레포 커밋용 .md 초안을 생성합니다' : '켜면 답변 대신 문서 초안을 만듭니다';
      var placeholder = s.promo ? '예: Salt Fires 가문을 캐논으로 승격해줘' : '예: Salt Fires가 뭐야?';
      var sendLabel = s.promo ? '초안' : '질의';
      body = '<div class="qa-note">설정 문서 기반으로 답합니다. 캐논에 없는 건 「미정」이라 정직하게 답해요. 시드는 <b>대화 맥락(세션) 단위</b>로 저장됩니다 — 이어지는 질의응답 전체가 한 시드에 담겨요. 주제를 바꿀 땐 「＋ 새 세션」.</div>' +
        '<div class="qa-body" data-qabody="1">' + msgs + thinking + '</div>' +
        '<div class="qa-sugs">' + sugs + '</div>' +
        '<div class="promo-bar"><button class="promo-tog ' + promoCls + '" data-act="togglePromo"><span class="promo-dot"></span>' + promoLabel + '</button><span class="promo-hint">' + esc(promoHint) + '</span></div>' +
        '<div class="qa-in"><input id="qainput" placeholder="' + attr(placeholder) + '"><button class="qa-send" data-act="sendAsk"' + (s.asking ? ' disabled' : '') + '>' + sendLabel + '</button></div>';
    }
    return '<aside class="qa">' + head + body + '</aside>';
  };

  // ── post-render wiring (refs + input listeners; clicks are delegated) ──
  Codex.prototype.postRender = function () {
    var self = this;
    var doc = this.ui.querySelector('[data-doc]');
    if (doc) { /* node chips handled by delegation */ }
    this.qaBody = this.ui.querySelector('[data-qabody]');
    this.qaInput = this.ui.querySelector('#qainput');
    if (this.qaInput) {
      this.qaInput.addEventListener('keydown', function (e) { if (e.key === 'Enter') self.sendQuery(); });
    }
    var ds = this.ui.querySelector('#dsearch');
    if (ds) {
      // patch only the results list so focus/caret survive typing
      ds.addEventListener('input', function (e) {
        self.state.dictQ = e.target.value;
        var box = self.ui.querySelector('#dictresults');
        if (box) box.innerHTML = self.buildDict(self.state.dictQ);
      });
      if (this._focusDict) { ds.focus(); try { ds.setSelectionRange(ds.value.length, ds.value.length); } catch (x) {} }
    }
    if (this.qaBody) this.scrollQa();
  };

  Codex.prototype.bindDelegates = function () {
    var self = this;
    this.ui.addEventListener('click', function (e) {
      // node chips inside doc views
      var chip = e.target.closest('[data-node]');
      if (chip) { self.setState({ view: 'graph' }); self.open(chip.getAttribute('data-node')); return; }
      // term glossary spans
      var term = e.target.closest('.term');
      if (term) { self.setState({ termDef: term.getAttribute('data-def') }); return; }
      var act = e.target.closest('[data-act]');
      if (!act) { if (self.state.termDef && !e.target.closest('.pop')) self.setState({ termDef: null }); return; }
      var a = act.getAttribute('data-act'), arg = act.getAttribute('data-arg');
      self.dispatch(a, arg);
    });
  };

  Codex.prototype.dispatch = function (a, arg) {
    switch (a) {
      case 'begin': localStorage.setItem('qfuds-codex-intro', '1'); this.setState({ intro: false }); this.flyTo('btc-2008', 320); break;
      case 'reset': this.doReset(); break;
      case 'tab': this._focusDict = false; this.setState({ view: arg }); break;
      case 'open': this._focusDict = false; this.open(arg); break;
      case 'closePanel': this.setState({ sel: null, termDef: null }); break;
      case 'markRead': this.doRead(); break;
      case 'toggleAsk': this.setState({ ask: !this.state.ask, seedsOpen: false }); break;
      case 'toggleSeeds': this.setState({ seedsOpen: !this.state.seedsOpen }); break;
      case 'newSession':
        this.qaMsgs = []; this.sessionId = null; this.sessionLabel = '';
        this.setState({ seedsOpen: false, asking: false });
        this.showToast('＋ 새 세션 — 이전 대화는 시드로 보존됩니다');
        break;
      case 'togglePromo': this.setState({ promo: !this.state.promo }); break;
      case 'sendAsk': this.sendQuery(); break;
      case 'sug': this.sendQuery(this.SUGS[+arg]); break;
      case 'saveSeed': this.saveSeed(+arg); break;
      case 'delSeed': this.delSeed(+arg); break;
      case 'saveDoc': this.saveDoc(+arg); break;
      case 'exportSeeds': this.exportSeeds(); break;
    }
  };

  // boot
  function start() {
    var ui = document.getElementById('ui');
    if (!ui) return;
    window.__codex = new Codex(ui);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
