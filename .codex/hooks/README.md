# Codex Hook Wrappers

This directory stores repository-local Codex hook wrapper scripts. Codex hook
registration is host-specific, so the tracked scripts are the shared source of
truth and local registration must point at them.

Use `.codex/hooks/remind-research-workflows.sh` for prompt-time reminders. The
commit-time enforcement remains `scripts/agent_workflow_guard.py --staged`,
which is wired through the repository pre-commit hook.
