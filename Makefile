# QFUDS repository audit targets.
#
# Status authority: docs/05_next_steps/000_roadmap.md is the single source of
# truth. These targets enforce that authority and the documentation record.

PYTHON ?= python3

.PHONY: help validate research-audit preflight-exp004 preflight

help:
	@echo "QFUDS make targets:"
	@echo "  make validate          - validate per-document frontmatter and cross-links"
	@echo "  make research-audit    - validate + enforce status-authority consistency"
	@echo "  make preflight-exp004  - exp_003 -> exp_004 readiness gate"
	@echo "  make preflight         - full pre-milestone audit (all of the above)"

validate:
	$(PYTHON) scripts/validate_docs.py

research-audit: validate
	$(PYTHON) scripts/research_consistency.py

preflight-exp004:
	$(PYTHON) scripts/preflight_exp004.py

# Run before any major experiment milestone.
preflight: validate research-audit preflight-exp004
	@echo "preflight: all repository audits passed"
