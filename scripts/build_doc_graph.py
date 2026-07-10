#!/usr/bin/env python3
"""Build a dependency graph of qfuds-verse fiction docs from frontmatter depends_on.

Minimal stack: Python standard library only (re, sqlite3, json, pathlib, html).
Scans every .md under the qfuds-verse subtree (in-scope + drafts + revisions +
release), resolves doc_id -> depends_on edges, and emits three artifacts under
outputs/:

  qfuds_verse_doc_graph.db    sqlite (nodes, edges) - queryable
  qfuds_verse_doc_graph.dot   GraphViz DOT - render with `dot -Tsvg`
  qfuds_verse_doc_graph.html  self-contained interactive force graph (Obsidian-like)

Usage:
    python3 scripts/build_doc_graph.py

Read-only over the docs tree. Does not modify any fiction file.
"""
from __future__ import annotations

import html
import json
import re
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# 2026-07-10 fiction-vault migration: qfuds-verse moved from
# docs/wiki/fiction/10_universes/qfuds-verse to fiction/worlds/qfuds-verse.
VERSE = ROOT / "fiction/worlds/qfuds-verse"
OUT = ROOT / "outputs"

# Layer (shelf) detection, ordered most-specific first. The SAGA production
# shelves (00_workroom, 10_story_design, 20_drafts, 30_revisions, 40_release,
# 90_archive) closed on 2026-07-10 and are Git-history-only
# (`git show bbbcb970:<path>`); they no longer exist under VERSE, so those
# rules are retired along with the paths they matched.
LAYER_RULES = [
    ("series-bible", "00_bible"),
    ("continuity", "00_continuity"),
    ("world", "10_world"),
]

# candidate doc_id fragments (registers, brainstorm, native lexicon, ideology axis)
CANDIDATE_HINTS = (
    "world_expansion_wave",
    "yi_gi_ideology_axis",
    "far_future_native_lexicon",
    "near_future_prelude_forecast",
    "sovereign_ai_open_closed_axis_brainstorm",
)


def layer_of(rel: str) -> str:
    for frag, name in LAYER_RULES:
        if rel.startswith(frag) or f"/{frag}" in rel:
            return name
    if rel.count("/") == 0:
        return "root"
    return "misc"


def classify(rel: str, layer: str, doc_id: str, status: str) -> str:
    if layer in ("20_drafts",):
        return "draft"
    if layer in ("30_revisions",):
        return "revision"
    if layer in ("00_workroom", "40_release") or rel.endswith("README.md"):
        return "provenance"
    if layer == "10_story_design":
        if any(h in doc_id for h in CANDIDATE_HINTS):
            return "candidate"
        return "design"
    if layer in ("00_continuity", "10_world", "00_bible"):
        if any(h in doc_id for h in CANDIDATE_HINTS):
            return "candidate"
        return "canon"
    return "misc"


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    fm: dict = {"depends_on": []}
    if not m:
        return fm
    cur = None
    for line in m.group(1).splitlines():
        if re.match(r"^\s*-\s", line) and cur == "depends_on":
            fm["depends_on"].append(line.strip()[2:].strip())
        else:
            mm = re.match(r"^([a-z_]+):\s*(.*)$", line)
            if mm:
                key, val = mm.group(1), mm.group(2).strip()
                cur = key
                if key == "depends_on" and val == "":
                    continue
                fm[key] = val
    return fm


def scan() -> tuple[list[dict], list[tuple[str, str, bool]]]:
    nodes: dict[str, dict] = {}
    raw_edges: list[tuple[str, list[str]]] = []
    for path in sorted(VERSE.rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        rel_verse = path.relative_to(VERSE).as_posix()
        fm = parse_frontmatter(path)
        doc_id = fm.get("doc_id") or rel_verse
        layer = layer_of(rel_verse)
        node = {
            "doc_id": doc_id,
            "path": rel,
            "title": fm.get("title", ""),
            "doc_type": fm.get("doc_type", ""),
            "status": fm.get("status", ""),
            "layer": layer,
            "clazz": classify(rel_verse, layer, doc_id, fm.get("status", "")),
            "in_degree": 0,
        }
        nodes[doc_id] = node
        raw_edges.append((doc_id, fm.get("depends_on", [])))

    edges: list[tuple[str, str, bool]] = []
    for src, deps in raw_edges:
        for dep in deps:
            resolved = dep in nodes
            edges.append((src, dep, resolved))
            if resolved:
                nodes[dep]["in_degree"] += 1
    return list(nodes.values()), edges


def write_sqlite(nodes, edges, dangling_ids):
    db = OUT / "qfuds_verse_doc_graph.db"
    if db.exists():
        db.unlink()
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE nodes (doc_id TEXT PRIMARY KEY, path TEXT, title TEXT, "
        "doc_type TEXT, status TEXT, layer TEXT, class TEXT, in_degree INTEGER)"
    )
    cur.execute(
        "CREATE TABLE edges (src TEXT, dst TEXT, resolved INTEGER)"
    )
    cur.execute(
        "CREATE TABLE dangling (doc_id TEXT)"  # dep targets that are not nodes
    )
    cur.executemany(
        "INSERT INTO nodes VALUES (?,?,?,?,?,?,?,?)",
        [
            (n["doc_id"], n["path"], n["title"], n["doc_type"], n["status"],
             n["layer"], n["clazz"], n["in_degree"])
            for n in nodes
        ],
    )
    cur.executemany(
        "INSERT INTO edges VALUES (?,?,?)",
        [(s, d, 1 if r else 0) for s, d, r in edges],
    )
    cur.executemany("INSERT INTO dangling VALUES (?)", [(d,) for d in sorted(dangling_ids)])
    con.commit()
    con.close()
    return db


LAYER_COLOR = {
    "00_continuity": "#e15759",
    "10_world": "#4e79a7",
    "00_bible": "#59a14f",
    "00_workroom": "#b07aa1",
    "10_story_design": "#f28e2b",
    "20_drafts": "#9c755f",
    "30_revisions": "#edc948",
    "40_release": "#76b7b2",
    "root": "#bab0ac",
    "misc": "#bab0ac",
}


def write_dot(nodes, edges):
    dot = OUT / "qfuds_verse_doc_graph.dot"
    lines = ["digraph qfuds_verse {", '  rankdir=LR;', '  node [shape=box, style=filled, fontsize=9];']
    for n in nodes:
        color = LAYER_COLOR.get(n["layer"], "#bab0ac")
        label = n["doc_id"].replace('"', "'")
        lines.append(f'  "{n["doc_id"]}" [fillcolor="{color}", label="{label}"];')
    for s, d, r in edges:
        style = "" if r else ' [style=dashed, color=red]'
        lines.append(f'  "{s}" -> "{d}"{style};')
    lines.append("}")
    dot.write_text("\n".join(lines), encoding="utf-8")
    return dot


def write_html(nodes, edges):
    id2idx = {n["doc_id"]: i for i, n in enumerate(nodes)}
    vis_nodes = []
    for n in nodes:
        deg = n["in_degree"]
        vis_nodes.append({
            "id": n["doc_id"],
            "label": n["path"].split("/")[-1].replace(".md", ""),
            "group": n["layer"],
            "value": deg + 1,
            "title": f'{n["path"]}\n{n["title"]}\nclass={n["clazz"]} status={n["status"]} in_degree={deg}',
        })
    vis_edges = []
    dangling_targets = set()
    for s, d, r in edges:
        if r:
            vis_edges.append({"from": s, "to": d})
        else:
            dangling_targets.add(d)
    # add dangling target placeholder nodes so red edges render
    for d in sorted(dangling_targets):
        if d not in id2idx:
            vis_nodes.append({
                "id": d, "label": d, "group": "dangling", "value": 1,
                "title": f"DANGLING (unresolved doc_id): {d}",
            })
    for s, d, r in edges:
        if not r:
            vis_edges.append({"from": s, "to": d, "color": {"color": "#e15759"}, "dashes": True})

    colors = dict(LAYER_COLOR)
    colors["dangling"] = "#000000"
    groups_js = ",\n".join(
        f'"{k}": {{color: {{background: "{v}", border: "#333"}}}}' for k, v in colors.items()
    )
    data = {
        "nodes": vis_nodes,
        "edges": vis_edges,
    }
    payload = html.escape(json.dumps(data), quote=False)
    legend = " ".join(
        f'<span style="background:{v};padding:2px 6px;border-radius:3px;color:#fff;font-size:11px">{k}</span>'
        for k, v in colors.items()
    )
    doc = f"""<!DOCTYPE html>
<html lang="ko"><head><meta charset="utf-8">
<title>QFUDS Verse 문서 의존성 그래프</title>
<script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
<style>
  body {{ font-family: sans-serif; margin: 0; }}
  #bar {{ padding: 8px; background: #222; color: #eee; }}
  #legend span {{ margin-right: 4px; }}
  #net {{ width: 100vw; height: calc(100vh - 84px); border-top: 1px solid #444; }}
  input {{ padding: 4px; width: 320px; }}
</style></head>
<body>
<div id="bar">
  <b>QFUDS Verse 문서 의존성 그래프</b>
  &nbsp; 노드 {len(nodes)} · 엣지 {len(edges)} &nbsp;
  <input id="q" placeholder="doc_id / 경로 검색 후 Enter">
  <div id="legend">{legend}</div>
</div>
<div id="net"></div>
<script>
const raw = JSON.parse("{payload}".replace(/&quot;/g,'"'));
const nodes = new vis.DataSet(raw.nodes);
const edges = new vis.DataSet(raw.edges);
const groups = {{ {groups_js} }};
const net = new vis.Network(document.getElementById('net'), {{nodes, edges}}, {{
  groups,
  nodes: {{ shape: 'dot', scaling: {{min: 6, max: 40}}, font: {{size: 11}} }},
  edges: {{ arrows: 'to', color: {{color: '#aaa'}}, smooth: {{type: 'continuous'}} }},
  physics: {{ barnesHut: {{gravitationalConstant: -8000, springLength: 120}}, stabilization: {{iterations: 300}} }},
  interaction: {{ hover: true, tooltipDelay: 100 }}
}});
document.getElementById('q').addEventListener('keydown', e => {{
  if (e.key !== 'Enter') return;
  const term = e.target.value.trim().toLowerCase();
  if (!term) return;
  const hit = raw.nodes.find(n => n.id.toLowerCase().includes(term) || (n.title||'').toLowerCase().includes(term));
  if (hit) {{ net.selectNodes([hit.id]); net.focus(hit.id, {{scale: 1.2, animation: true}}); }}
}});
</script>
</body></html>"""
    out = OUT / "qfuds_verse_doc_graph.html"
    out.write_text(doc, encoding="utf-8")
    return out


def main():
    OUT.mkdir(exist_ok=True)
    nodes, edges = scan()
    dangling = {d for _, d, r in edges if not r}
    db = write_sqlite(nodes, edges, dangling)
    dot = write_dot(nodes, edges)
    html_path = write_html(nodes, edges)

    resolved = sum(1 for _, _, r in edges if r)
    print(f"nodes={len(nodes)} edges={len(edges)} (resolved={resolved} dangling={len(edges)-resolved})")
    by_layer: dict[str, int] = {}
    for n in nodes:
        by_layer[n["layer"]] = by_layer.get(n["layer"], 0) + 1
    print("by layer:", ", ".join(f"{k}={v}" for k, v in sorted(by_layer.items())))
    print("\nTop hubs (in_degree):")
    for n in sorted(nodes, key=lambda x: -x["in_degree"])[:12]:
        print(f"  {n['in_degree']:3d}  {n['doc_id']}  [{n['clazz']}]")
    if dangling:
        print(f"\nDangling depends_on targets ({len(dangling)}):")
        for d in sorted(dangling):
            print(f"  - {d}")
    orphans = [n for n in nodes if n["in_degree"] == 0 and not n["path"].endswith("README.md")]
    print(f"\nOrphans (in_degree 0, non-README): {len(orphans)}")
    print(f"\nWrote: {db}\n       {dot}\n       {html_path}")


if __name__ == "__main__":
    main()
