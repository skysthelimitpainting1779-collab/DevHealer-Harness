# 🩺 DevHealer: Autonomic Self-Healing & Rule-Evolution Harness

**DevHealer** is a production-hardened, self-healing developer harness designed to run continuously on a Windows 10 host workstation. It implements an autonomous Monitor-Analyze-Plan-Execute-Knowledge (MAPE-K) control loop fully integrated with the Google Antigravity 2.0 platform specifications [57, 58].

By combining event-driven transport hooks, out-of-band state caches, and isolated version control operations, DevHealer automatically detects compile and runtime disruptions, spins up safe execution sandboxes to apply repairs, and dynamically evolves its own ruleset to prevent future regressions [73, 74].

## 📁 Repository Filesystem Topology

Deploying this structure ensures your environment complies with Antigravity's strict validation engines and remains portable across any workstation [86, 98].

```text
ITS/ (Repository Root)
├── .gitignore                          # Excludes temporary worktrees, logs, and venv
├── README.md                           # This file (Onboarding & Quick Start guide)
├── devhealer_colab_notebook.ipynb      # Interactive installation & simulation notebook
├── master_operations_manual.md         # Single Source of Truth architectural spec
├── setup.py                            # The workspace-scaffolding installer script
├── run_tests_hardened.py               # Windows process-tree file-lock sweeper
├── test_harness.ps1                    # PowerShell background diagnostic watcher
├── deploy_global.ps1                   # Global plugin promotion deployer
└── .agents/                            # Antigravity project customization folder
    ├── hooks.json                      # Flat 2.0 event-keyed hooks registration
    ├── mcp_config.json                 # Core sparse MCP server definitions
    ├── scripts/                        # Synchronous runtime interception hooks
    │   ├── pre-tool-use.py             # Semantic firewall & command-gating rules
    │   ├── post-tool-use.py            # Anomaly categorization state writer
    │   └── stop-handler.py             # Sliding retry & sliding loop controller
    ├── rules/                          # Prompt-level workspace constraints
    │   └── development-ontology.md     # Core MAPE-K taxonomy & rule constraints
    ├── workflows/                      # Trajectory-level slash commands
    │   ├── workflow_heal_project.md    # Sequential /workflow_heal_project trajectory
    │   └── workflow_evolve_rules.md    # Automated rule-compaction workflow
    └── skills/                         # Encapsulated task reasoning modules
        └── heal-and-evolve/  
            └── SKILL.md                # Diagnostic & remediation decision trees
```

## ⚡ Quick Start

### 1. Scaffold the Workspace
Run the bootstrapper to initialize the directory layouts and compile configurations:
```bash
python setup.py
```
Alternatively, run the interactive steps in `devhealer_colab_notebook.ipynb` to walk through the system setup sequentially.

### 2. Run Tests with Hardened Wrapper
To prevent "Access is Denied" file locks on Windows during automated Git worktree cleanup and branch rotation, never run bare test or build commands natively. Instead, prepend your execution calls:
```bash
python run_tests_hardened.py <command>
```
*Example:* `python run_tests_hardened.py npm test` or `python run_tests_hardened.py pytest`

### 3. Background Watcher Sidecar
Invoke the diagnostic watcher to monitor active file changes, record compile anomalies out-of-band, and simulate proactive agent triggers:
```powershell
powershell -ExecutionPolicy Bypass -File test_harness.ps1
```

## 🛡️ Strict Mode & State Storage

Under Google Antigravity's **Strict Mode**, writing dynamic state metrics or temporary data directly inside the workspace files is strictly blocked by the permissions engine [180].

To keep the agent immune to write-denial errors, all continuously changing sidecar state and anomaly triggers are explicitly banned from being written to `.agents/scratch/` or any other repository path [38, 48]. All dynamic loop metadata (such as `healing-state.json`) is pushed to the secure, platform-allocated AppData directory exposed via the `%ANTIGRAVITY_EXECUTABLE_DATA_DIR%` environment variable [38, 48].

This maintains absolute sandboxing, ensures clean Git commits, and keeps your project completely unpolluted [38].

## 🔍 Auditing the Harness (Repomix)

To generate a precise, high-fidelity logic and security audit of your active configuration without polluting your LLM context window with large binary blobs (like notebook JSON) or verbose conceptual prose, execute a targeted Repomix pack:
```bash
npx repomix --include "setup.py,run_tests_hardened.py,test_harness.ps1,.agents/hooks.json,.agents/mcp_config.json,.agents/scripts/**/*.py,.agents/rules/**/*.md,.agents/workflows/**/*.md,.agents/skills/**/*.md"
```
The resulting `repomix-output.md` (or `.xml`) file compiles all load-bearing scripts, hooks, rules, and workflows into a single file. You can paste this output directly into an auditor LLM with our verification prompts to ensure absolute compliance with Antigravity 2.0 specs.

## 🗺️ Architectural Mapping to Antigravity 2.0 Specifications

| Local Component | Spec Section | Windows 10 / Platform Compliance Details |
| :--- | :--- | :--- |
| `hooks.json` | Hooks (§4.1) | Written in the mandatory flat, event-keyed 2.0 format. Bypasses old nested configurations and uses the native `python` interpreter command rather than `python3` to avoid Windows Store prompts [47]. |
| `pre-tool-use.py` | Permissions (§4.5) | Features Windows path normalization (stripping drive letters like `C:` and converting backslashes to forward slashes `/`) to prevent permission evaluation failures [54]. |
| `run_tests_hardened.py` | Worktrees (§4.6) | Aggressively sweeps child process trees via `psutil` before worktree exits, releasing active file locks so the system can clean up temporary folders cleanly [34, 36, 51]. |
| `stop-handler.py` | Loop Control (§4.1) | Instructs the process spawner to continue the loop (`{"decision": "continue"}`) and retry the repair if compilation is still failing and retries are under the limit [74, 87]. |
| `ToolFailure.md` | Rule Limits (§4.4) | Codifies syntax validation checks (`node --check`) using a strict rewrite-in-place compacting strategy to ensure rules remain well below the hard 12,000-character ceiling [34, 35]. |
