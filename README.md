# DevHealer Harness

**A fully autonomous, proactive self-healing architecture built on the Google Antigravity ecosystem.**

Welcome to DevHealer. This repository is not meant to be manually compiled or debugged by human engineers. It is guarded by a suite of background daemons, adversarial peer-review subagents, and a continuously evolving semantic ontology.

## How It Works: The Continuous Loop

DevHealer entirely replaces the reactive "code, compile, debug" loop with a proactive, self-healing background engine. 

1. **The Proactive Background Daemon**: A global Antigravity sidecar (`proactive-healer.py`) silently monitors the `src/` directory. The moment a file changes, the daemon autonomously spins up an isolated background process to run the test suite (`run_tests_hardened.py`).
2. **Autonomous Trigger**: If the background tests pass, the daemon remains silent. If an anomaly is detected (non-zero exit code), it parses the stack trace, writes it to the strictly controlled `%ANTIGRAVITY_EXECUTABLE_DATA_DIR%\healing-state.json`, and natively commands the IDE agent to execute the `/workflow_heal_project` workflow.
3. **The Devil's Advocate (Pre-Flight Eval)**: Before writing any fix, the repair subagent is bound by strict evaluation guardrails. If a proposed fix involves *any* engineering trade-offs (e.g., bypassing linter rules or incurring tech debt), it must spawn the adversarial `devils-advocate` subagent. The Devil's Advocate red-teams the fix. If it finds negative side effects, the code is rejected and cannot be merged.
4. **Development Ontology**: Once a fix is approved and verified, the agent writes the lesson learned directly into the `.agents/rules/development-ontology.md`. Because Antigravity natively injects `.agents/rules/` into its C++ AI engine, DevHealer actually gets smarter and faster every single time it catches a bug.

## Instructions for Developers

You do not need to use slash commands. You do not need to prompt the AI. You do not need to manually test.

1. Write code in your IDE.
2. Hit Save.
3. If you wrote a bug, the background sidecar will catch it, the Devil's Advocate will ensure the fix is robust, and the repair agent will seamlessly rewrite your code until the tests pass.

*This repository conforms strictly to the Google Antigravity Documentation standards, leveraging native rules injection and isolated plugin sidecars.*
