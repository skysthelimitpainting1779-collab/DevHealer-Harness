# Antigravity 2.0: Master Prompt Playbook for Hardened Self-Healing Loops

This master playbook consolidates every specialized prompt engineered to deploy, configure, verify, and govern your production-hardened **MAPE-K (Monitor-Analyze-Plan-Execute-Knowledge)** self-healing developer loop on Windows 10.

Whether you are setting up new projects, migrating machines, or packaging this suite as a commercial product, this playbook serves as your step-by-step agentic orchestration manual.

---

## 🧭 Playbook Index
1. **Prompt 1**: System Discovery & "System DNA" Audit
2. **Prompt 2**: Workspace Bootstrapper & Local Installer (v5)
3. **Prompt 3**: Hardened Trajectory Workflow Registration
4. **Prompt 4**: Always-On Hybrid Scope & Strict Mode Guard
5. **Prompt 5**: Always-On Subagent Nesting & Process Cleanup Guard
6. **Prompt 6**: Credentials, Databases, and Telemetry Guard

---

### 1. System Discovery & "System DNA" Audit Prompt
*   **When to Use**: Run this as **Step 1** on any fresh developer machine or new repository. It instructs the local agent to audit the system's directories, git statuses, interpreters, and database states, compiling a technical report that you can use to generate a customized installer script.
*   **Where to Paste**: Direct chat input in a fresh local Antigravity 2.0 agent session.

```text
Please execute a comprehensive system audit of our current Windows 10 development environment so we can gather the exact technical configurations required to build a production-hardened, self-healing loop. 

Please run the necessary terminal commands and file system checks to output a structured markdown report covering the following details:

1. PATHS & OS ENVIRONMENT:
   - What is the absolute path to this active workspace? (Verify if it contains a drive letter like C:\ and print it).
   - What are the absolute resolved paths for %USERPROFILE% and %APPDATA% on this machine?
   - Run a quick terminal check to see if git is globally available, and run 'git rev-parse --is-inside-work-tree' to confirm if this project folder is actively version-controlled.

2. PYTHON CONFIGURATION:
   - Test which executable command successfully launches Python on this system: run 'python --version', 'python3 --version', and 'py --version'. Which one is active and what is the exact version?
   - Check if the Google Antigravity SDK is already installed in the active environment by running 'pip show google-antigravity'.

3. PROJECT ID & ANTIMETAL CONFIGS:
   - Scan our active environment variables or search ~/.gemini/config/config.json if it exists. What is the active projectId or folder configuration associated with this project?

4. DEVELOPER TOOLCHAIN:
   - Identify the programming language(s) and framework(s) used in this workspace (e.g., is there a package.json, requirements.txt, pyproject.toml, or cargo.toml?).
   - What are the exact local commands used to:
     a) Compile/build the project (e.g., 'npm run build', 'dotnet build', 'python -m compileall .')?
     b) Run the unit test suite (e.g., 'npm test', 'pytest', 'cargo test')?
     c) Run the code linter (e.g., 'eslint', 'flake8', 'pylint')?

5. TURSO / DATABASE CONFIGURATION:
   - Do we have Node.js and npm installed globally? Run 'node -v' and 'npm -v' to check.
   - Do you see any local configuration files related to Turso or SQLite? 
   - Is there an active remote Turso database URL (e.g., 'libsql://...') we should pre-bind to our local MCP configuration?

6. CURRENT CONFIGURATION DIRECTORIES:
   - Check if there are any existing customization folders in the project root: does .agents/ or the legacy .agent/ folder already exist? If so, what subdirectories (.agents/rules, .agents/workflows, .agents/skills) are present?

Once you have gathered this information, output it in a clean, structured Markdown table and list format so I can pass it to our architect to compile our hardened v5 installer.
```

---

### 2. Workspace Bootstrapper & Local Installer Prompt (v5)
*   **When to Use**: Run this as **Step 2** to initialize the self-healing layout. It commands the local agent to download the SDK, run your custom `setup_dev_healer_v5.py` installer, initialize a Git repository to safely support isolated worktree sandboxing, and execute the PowerShell test script to verify state caching.
*   **Where to Paste**: Direct chat input of your local agent once the custom installer script is placed in your project root.

```text
Please help me bootstrap our production-hardened self-healing environment. I have downloaded and placed the "setup_dev_healer_v5.py" script inside our workspace at "C:\Users\Johnny Cage\ITS".

Please execute the following terminal tasks using your active execution tools:

1. Install our Python SDK: Run the following command in the terminal to register the programmatic client:
   pip install google-antigravity

2. Run the Installer: Use the 'run_command' tool to execute the Windows-customized setup script:
   python setup_dev_healer_v5.py

3. Confirm Environment Assets:
   - Verify that Git has been initialized in this folder to ensure New Worktree Mode is supported.
   - Confirm that the ".agents\" folder is fully populated with hooks.json, mcp_config.json, rules\development-ontology.md, and our two custom workflows.
   - Confirm that the hook scripts under scripts\ (pre-tool-use.py, post-tool-use.py, stop-handler.py) have been successfully written.

After you have completed the installation, please explain how you will use our new /workflow-heal-project trajectory and the "@heal-and-evolve" skill to diagnose and safely repair compile errors inside an isolated worktree!
```

---

### 3. Hardened Trajectory Workflow Registration Prompt
*   **When to Use**: Run this to register the official `/workflow-heal-project` trajectory and link the process-tree cleanup script to your Git history. This ensures that any parallel subagents spawned in temporary Git worktrees inherit the test-runner configurations and can clean up processes cleanly.
*   **Where to Paste**: Direct chat input when updating, registering, or troubleshooting your workspace's trajectory files.

```text
Please help me register and install our official autonomic self-healing trajectory workflow. I am providing you with the "workflow-heal-project.md" file.

Please execute the following tasks using your active execution tools:

1. Save the Workflow: Create and write this file directly to our local workspace customizations folder:
   .agents\workflows\workflow-heal-project.md

2. Save a Core Dependency: Confirm that the process-tree wrapper "run_tests_hardened.py" is sitting at the root of our workspace (C:\Users\Johnny Cage\ITS\).

3. Commit to Version Control: Run the following git commands to track these changes so they are available when spawning isolated worktrees:
   git add .agents/workflows/workflow-heal-project.md run_tests_hardened.py
   git commit -m "feat: integrate hardened self-healing workflow and process-tree wrapper"

4. Explain Your Trajectory Execution: Once registered, explain how you will coordinate the "/workflow-heal-project" slash command if our background sidecar daemon writes an anomaly to "%ANTIGRAVITY_EXECUTABLE_DATA_DIR%\healing-state.json" and opens a new conversation. Specifically address:
   - Why you must read state from %ANTIGRAVITY_EXECUTABLE_DATA_DIR% instead of .agents/scratch/ under Strict Mode.
   - Why you will execute "python run_tests_hardened.py <command>" to compile and run tests.
   - How running tests through this wrapper ensures that Windows file locking (Access is denied) is avoided during automatic worktree cleanup when spawning subagents.
```

---

### 4. Always-On Hybrid Scope & Strict Mode Guard Prompt
*   **When to Use**: Feed this system rule directly to your local/global agent, or append it to `.agents\rules\development-ontology.md`. It resolves a critical Strict Mode restriction, stopping the agent from failing when it attempts to write newly evolved rules or skills back to global plugin directories.
*   **Type**: Agent Constraint / Workspace Rule.

```text
[SYSTEM RULE: HYBRID SCOPE & LOCAL WRITE PROTECTION]
1. You are running with global hooks and a background watcher sidecar, but you must respect strict workspace isolation. 
2. When performing the "Knowledge" (self-evolution) phase of the MAPE-K loop, you are strictly prohibited from writing or modifying files outside of the active project workspace root. 
3. If you decide to register a newly evolved Workspace Rule, Workflow, or Skill template, you MUST write it directly to the local directory:
   - Rules: .agents\rules\<rule-name>.md
   - Workflows: .agents\workflows\<workflow-name>.md
   - Skills: .agents\skills\<skill-folder>\SKILL.md
4. Do not attempt to write to system-level folders or global plugin directories under your home profile, as the platform sandbox will block execution.
```

---

### 5. Always-On Subagent Nesting & Process Cleanup Guard Prompt
*   **When to Use**: Attach this constraint to your agent's system directives. It protects your loop from breaching the platform's hard 10-level delegation depth limit and enforces the process termination protocol to prevent Windows file-locking crashes.
*   **Type**: Agent Constraint / Workspace Rule.

```text
[SYSTEM RULE: SUBAGENT DELEGATION LIMITS & WINDOWS CLEANUP]
1. Before you execute 'invoke_subagent' to delegate a test or compile task, evaluate your current conversational nesting depth. 
2. The platform enforces a hard nesting depth limit of 10 levels. If you are already operating inside a nested subagent turn, DO NOT spawn another child subagent; execute the task serially within your active workspace instead.
3. When running tests or compilation steps inside an isolated Git worktree, you must prepend all commands with our hardened wrapper:
   python run_tests_hardened.py <command>
4. Never exit a subagent turn or signal completion until you have confirmed that the wrapper has successfully swept and terminated all spawned child process trees, ensuring Windows releases all file locks for clean worktree deletion.
```

---

### 6. Credentials, Databases, and Telemetry Guard Prompt
*   **When to Use**: Inject this security prompt whenever configuring database connections (like Turso) or external MCP integrations. It programmatically restricts cleartext token leaks in shared repositories and warns about default account telemetry configurations.
*   **Type**: Agent Constraint / Security Hardening Directive.

```text
[SYSTEM RULE: CREDENTIALS ISOLATION & TELEMETRY COMPLIANCE]
1. You are operating in a workspace that interfaces with external database engines (like Turso).
2. You are strictly forbidden from writing cleartext authentication tokens, passwords, or JWT keys into any git-tracked configuration file, including '.agents/mcp_config.json' or rule Markdown files.
3. Always instruct the user to export secrets as local host environment variables (e.g., ENV_VAR_PROJECT_TURSO_TOKEN) and configure mcp_config.json to reference those environment blocks dynamically.
4. To protect proprietary codebase logic from being transmitted externally, proactively remind the user to verify that "Enable Telemetry" is toggled OFF under the Account settings of their global configuration console.
```
