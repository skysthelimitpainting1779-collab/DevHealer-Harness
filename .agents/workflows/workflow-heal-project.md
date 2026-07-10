# Proactive Project Self-Healing Trajectory
This workflow executes sequentially when a background sidecar logs a tool execution fault or testing failure.

## Trajectory Sequence
1. Read the structured failure details from our git-immune state registry using the `view_file` tool on `healing-state.json` inside the system path mapped by `ANTIGRAVITY_EXECUTABLE_DATA_DIR`.
2. Activate the `@heal-and-evolve` skill to run a rigorous diagnosis of the error logs and plan an isolated remediation.
3. Spawn a dedicated helper subagent using the `invoke_subagent` tool. You must configure the subagent to run in **New Worktree Mode** to shield the active repository from broken builds.
4. Inside the isolated background branch, direct the subagent to run edits and validation scripts (`npm run build`, `npm test`, etc.).
5. **Critical Windows Process Cleanup**: Before exiting, the subagent must explicitly trace and terminate all child processes it spawned to free Windows file lock handles, avoiding 'Access is denied' exceptions on directory cleanup.
6. Commit the passing build changes, merge the clean branch, reset `healing-state.json`, and run `/workflow-evolve-rules` to write hardened guidelines.
