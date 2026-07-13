---
name: workflow_heal_project
description: Workflow converted to skill: workflow_heal_project
---

# Trajectory Workflow: Build and Heal Project
# Command: /workflow-heal-project
# Size Cap Compliance: Under 12,000 characters

## Step 1: Secure State Inspection
*   Read current anomaly report from `%ANTIGRAVITY_EXECUTABLE_DATA_DIR%\healing-state.json`.
*   Verify error signature (e.g., `ToolFailure` compilation error).

## Step 2: Isolated Branching (New Worktree Mode)
*   Check if active environment is inside a Git repository.
*   If initialized, spawn an isolated subagent in New Worktree Mode:
    `invoke_subagent --workspace=worktree --role=resolver`

## Step 3: Run Diagnostic Compilation
*   Prepend compile & test runs using our Windows-safe process tree sweeper:
    `python run_tests_hardened.py <your-test-or-build-command>`

## Step 4: Resolve Anomaly
*   Let the subagent resolve database schemas, linter bugs, or compile conflicts.
*   Validate the fix using the `run_tests_hardened.py` wrapper to prevent background process locking.

## Step 5: Merge & Evolve Rules
*   Cleanly teardown the worktree.
*   Write lessons learned to `.agents/rules/development-ontology.md` following our rewrite-in-place compacting policy to stay strictly under the 12,000-character cap.
