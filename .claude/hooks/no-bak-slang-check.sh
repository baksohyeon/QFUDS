#!/bin/bash
# no-bak-slang-check.sh — deprecated no-op.
#
# This used to hard-deny Korean "박-" translationese during Write/Edit.
# That was too blunt for fiction work because literal prose can legitimately use
# 박다/박았다/박혀/박힌. The active rule is now the soft UserPromptSubmit
# reminder in .claude/hooks/remind-korean-style.sh.

exit 0
