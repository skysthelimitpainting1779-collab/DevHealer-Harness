---
name: development-ontology
description: development-ontology rule
---

# Workspace Guidelines & Anomaly Ontology
This rule is Always-On and enforces project integrity guidelines for all developer agents.

## Enforced Standards
* **Process Handle Hygiene**: All background compilers, watchers, or test runners spawned in isolated worktrees must be explicitly terminated prior to subagent shutdown to prevent Windows directory lockups (Access is denied errors).
* **Workspace Isolation**: Multi-step codebase refactors or experimental repairs must be performed inside isolated background branches via New Worktree Mode.
* **Pathing Normalization**: Programmatically convert all backslashes (`\`) to forward slashes (`/`) in path strings prior to testing permissions, drive letters must be stripped during evaluation.
* **Character Capacity Safeguard**: Never commit log dumps, compile warnings, or stack traces directly into rule files. Rule updates must use a rewrite-in-place compacting pattern to stay well below 12,000 characters.
* **Syntax Validation**: Prior to committing any Javascript/Node.js changes, verify syntax validity (e.g., by running `node --check <file>`) to ensure no syntax errors or unclosed parentheses are introduced.

