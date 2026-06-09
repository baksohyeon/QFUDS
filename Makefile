# QFUDS repository audit targets.
#
# Status authority: docs/05_next_steps/000_roadmap.md is the single source of
# truth. These targets enforce that authority and the documentation record.

PYTHON ?= python3

.PHONY: help validate research-audit preflight-exp004 preflight test install-git-hooks

help:
	@echo "QFUDS make targets:"
	@echo "  make validate          - validate per-document frontmatter and cross-links"
	@echo "  make research-audit    - validate + enforce status-authority consistency"
	@echo "  make preflight-exp004  - exp_003 -> exp_004 readiness gate"
	@echo "  make preflight         - full pre-milestone audit (all of the above)"
	@echo "  make test              - run unittest regression tests under tests/"
	@echo "  make install-git-hooks - install local git pre-commit checks"

validate:
	$(PYTHON) scripts/validate_docs.py

research-audit: validate
	$(PYTHON) scripts/research_consistency.py

preflight-exp004:
	$(PYTHON) scripts/preflight_exp004.py

test:
	$(PYTHON) -m unittest discover -s tests -p 'test_*.py'

# Run before any major experiment milestone.
preflight: validate research-audit preflight-exp004
	@echo "preflight: all repository audits passed"

install-git-hooks:
	install -m 755 scripts/git-hooks/pre-commit .git/hooks/pre-commit
	@echo "installed .git/hooks/pre-commit"
