# QFUDS Verse Codex — Dokku builds this (Dockerfile detected at the app build-dir).
# Tiny zero-dependency Node server: static codex + optional Gemini query proxy.
FROM node:20-alpine

WORKDIR /app
COPY . .

# No dependencies to install (server uses only Node built-ins).
ENV PORT=5000
EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s \
  CMD wget -qO- http://127.0.0.1:5000/healthz || exit 1

CMD ["node", "server.js"]
