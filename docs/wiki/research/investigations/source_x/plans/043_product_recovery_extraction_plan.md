---
doc_id: audit_2026_06_11_product_recovery_extraction_plan
title: "2026-06-11 Product-Recovery Extraction Plan"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - audit_2026_06_10_black_hole_data_product_audit
  - audit_2026_06_11_product_recovery_candidate_selection_plan
  - audit_2026_06_11_product_recovery_execution_plan
next_gate: execute product recovery extraction without derivation
last_updated: 2026-06-11
---

# 2026-06-11 Product-Recovery Extraction Plan

Execute 043 Product Recovery Extraction.

Authorities (in order):

1. [Black-Hole Data Product Audit](../conclusions/040_black_hole_data_product_audit.md)
2. [Product-Recovery Candidate Selection Plan](041_product_recovery_candidate_selection_plan.md)
3. [Product-Recovery Execution Plan](042_product_recovery_execution_plan.md)

Follow the authority chain exactly.

If two documents conflict:

040 > 041 > 042

Do not infer new requirements.

⸻

Scope

This task is a product-recovery extraction task only.

The goal is to recover structured source-history products from the selected assets.

This is not:

* a Q^nu derivation
* a delta Q derivation
* a physical-model derivation
* a Level 2B admission attempt

⸻

Lane A

Recover only:

rho_BH(a)

or

d rho_BH / dln(a)

from the Lacy 2024 asset chain.

Use only source files explicitly approved by 042.

⸻

Lane B

Recover only:

S_BH(a)

or

dS_BH / dln(a)

from the Chen 2026 asset chain.

Use only source files explicitly approved by 042.

⸻

Required Output Locations

Lane A:

docs/wiki/research/assets/lacy_2024_smbh_accretion_coupling_constraints/digitization/

Lane B:

docs/wiki/research/assets/chen_2026_merger_entropy_budget/digitization/

⸻

Extraction Rules

Record:

* exact source file
* exact source location
* page
* figure
* table
* equation
* caption
* extraction method

For every extracted item:

record provenance.

⸻

Missing Data Policy

If any field is missing:

* units
* uncertainty
* normalization
* redshift coverage
* source location

record it as missing.

Do not estimate.

Do not infer.

Do not fill gaps.

⸻

Required Classification

For every extracted item:

quality_state:

* manual_structured_extract
    or
* numeric_digitized

qfuds_role:

* source-history candidate
* comparator
* normalization check
* rejected for QFUDS use

⸻

Forbidden

Do not:

* derive Q^nu
* derive delta Q
* derive a candidate X
* modify roadmap status
* open Physical-QFUDS Level 2B
* claim support for QFUDS
* claim physical significance beyond the source material

⸻

Required Final Report

Report:

* files created
* files modified
* Lane A outcome
* Lane B outcome
* units verified?
* uncertainty route verified?
* normalization route verified?
* redshift coverage verified?
* candidate X boundary exists?
* still data_product_blocked?
* validation results

Run:

rtk python3 scripts/validate_docs.py
rtk python3 scripts/research_consistency.py
rtk git diff –check
rtk git status –short

Roadmap status must remain unchanged.

Level 2B must remain blocked.
