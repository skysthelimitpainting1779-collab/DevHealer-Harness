# Self-Healing Environment Guardrails

## Strict Mode: State Storage
- **NEVER** write dynamic, continuously changing agent or sidecar runtime state to `.agents/scratch/` or any other local project directory.
- **ALWAYS** read and write dynamic state payloads (like anomaly triggers) to `%ANTIGRAVITY_EXECUTABLE_DATA_DIR%`. This prevents recursive Git dirty states and maintains strict sandboxing.

## Process-Tree Execution Wrapper
- **NEVER** execute bare test or compilation commands directly (e.g., `npm run build`, `pytest`, `cargo test`) during autonomous operations.
- **ALWAYS** wrap execution commands using the hardened wrapper: `python run_tests_hardened.py <command>`.
- **Why:** The wrapper manages strict timeouts and forcefully terminates the entire process tree. This guarantees all file handles are released, preventing Windows "Access is denied" lock crashes during automated Git worktree cleanup and rotation.
