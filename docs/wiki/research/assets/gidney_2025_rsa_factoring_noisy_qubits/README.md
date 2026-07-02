---
doc_id: asset_gidney_2025_rsa_factoring_noisy_qubits
title: "Gidney 2025 RSA Factoring with Under a Million Noisy Qubits Assets"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - qfuds_saga_real_world_and_physics_research_anchors_ko
next_gate: fiction verisimilitude anchor for workroom 013 A6 and 039 Q-Day spine; no QFUDS promotion
last_updated: 2026-07-02
---

# Gidney 2025 RSA Factoring with Under a Million Noisy Qubits Assets

## Workflow Boundary

This cache follows the
[Research Asset and Product Workflow](../../../../../.agent/workflows/research-asset-product-workflow.md).

These files are research assets only. They do not create QFUDS evidence, change
roadmap status, or open Level 2B.

**Fiction-side use boundary.** This paper is cached as a **fiction verisimilitude
anchor** for the QFUDS SAGA near-future timeline (workroom 013 real-world anchors,
039 Q-Day two-crisis spine). It is a real quantum-cryptanalysis resource estimate.
It is not a claim about real-world Q-Day timing, not investment or policy advice,
and not QFUDS physics evidence. In-world Q-Day dates are dramatic fiction. CRQC
timing remains contested (mainstream weight 2030s or later); this paper is a
theoretical resource estimate, not a working code-breaking machine.

## Bibliographic Metadata

- Paper: "How to factor 2048 bit RSA integers with less than a million noisy
  qubits"
- Author: Craig Gidney (Google Quantum AI)
- Year: 2025 (submitted 2025-05-21, v1)
- arXiv: [2505.15917](https://arxiv.org/abs/2505.15917)
- Subject: Quantum Physics (quant-ph)

## Asset State

| Field | Value |
| --- | --- |
| Source URL | <https://arxiv.org/abs/2505.15917> |
| Asset type | arXiv PDF, 6 pages |
| Current asset state | `asset_cached` (raw PDF + abstract text) |
| Extraction potential | `source_tex_parse_possible`; `figure_digitization_possible` |
| Text quality | abstract captured as `source_text_parse` in [source/arxiv_abstract.md](source/arxiv_abstract.md); full-body numerical digitization not performed |
| Depends on | workroom 013 A6 near-future anchor; 039 Q-Day acceleration note |
| Known blocked step | no figure/numeric digitization (not required for fiction verisimilitude use) |
| Raw bundle policy | full PDF retained under `source/`; arXiv TeX source bundle not retained |

## Key Claim (anchor)

A 2048-bit RSA integer could be factored in under a week by a quantum computer
with fewer than one million noisy qubits, an order-of-magnitude reduction from
the author's 2019 estimate (20 million qubits, 8 hours). Drivers: approximate
residue arithmetic, yoked surface codes, magic state cultivation. Runtime rose
vs 2019 but Toffoli-gate count fell 100x vs a 2024 comparison.

This resource estimate is the primary source behind the "2026 Q-Day acceleration"
context recorded in workroom 013 A6. It lowers the theoretical qubit requirement;
it does not assert a working machine exists.

## Files

- `source/2505.15917.pdf` - full arXiv paper PDF (retrieved 2026-07-02 from
  `https://arxiv.org/pdf/2505.15917`).
- [source/arxiv_abstract.md](source/arxiv_abstract.md) - abstract and bibliographic record (source text).
- `figures/.gitkeep` - reserved for rendered figure mirrors if later needed.
- `digitization/.gitkeep` - reserved for derived conversions if later needed.

## Use Restriction

Cite only as a near-future verisimilitude anchor. Do not present as a real-world
Q-Day forecast or as QFUDS support.
