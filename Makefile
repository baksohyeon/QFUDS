# QFUDS repository audit targets.
#
# Status authority: docs/05_next_steps/000_roadmap.md is the single source of
# truth. These targets enforce that authority and the documentation record.

PYTHON ?= python3

.PHONY: help validate research-audit agent-workflow-guard web-data-provenance preflight-exp004 result-figures preflight test install-git-hooks

help:
	@echo "QFUDS make targets:"
	@echo "  make validate          - validate per-document frontmatter and cross-links"
	@echo "  make research-audit    - validate + enforce status-authority consistency"
	@echo "  make agent-workflow-guard - enforce staged research workflow evidence"
	@echo "  make web-data-provenance - check fiction web data doc-number references"
	@echo "  make preflight-exp004  - exp_003 -> exp_004 readiness gate"
	@echo "  make result-figures    - regenerate docs/04_results summary figures"
	@echo "  make preflight         - full pre-milestone audit (all of the above)"
	@echo "  make test              - run unittest regression tests under tests/"
	@echo "  make install-git-hooks - install local git pre-commit checks"

validate:
	$(PYTHON) scripts/validate_docs.py

research-audit: validate
	$(PYTHON) scripts/research_consistency.py
	$(PYTHON) scripts/check_web_data_provenance.py

agent-workflow-guard:
	$(PYTHON) scripts/agent_workflow_guard.py --staged

web-data-provenance:
	$(PYTHON) scripts/check_web_data_provenance.py

preflight-exp004:
	$(PYTHON) scripts/preflight_exp004.py

result-figures:
	$(PYTHON) scripts/generate_result_figures.py

test:
	$(PYTHON) -m unittest discover -s tests -p 'test_*.py'

# Run before any major experiment milestone.
preflight: validate research-audit agent-workflow-guard preflight-exp004
	@echo "preflight: all repository audits passed"

install-git-hooks:
	install -m 755 scripts/git-hooks/pre-commit .git/hooks/pre-commit
	@echo "installed .git/hooks/pre-commit"
