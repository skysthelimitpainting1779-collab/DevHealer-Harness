# DevHealer Customization & Architecture Schemas
**Production-Grade Specification Reference for Google Antigravity 2.0 and Windows 10 Host Environments**

This document serves as the absolute, production-ready schema blueprint and architectural specification for **DevHealer**. It details the folder topologies, exact file specifications, and I/O communication contracts that govern your self-healing loop under Strict Mode and sandboxing constraints.

---

## 📂 1. Directory Topology Schema
When promoted to a global or localized scope, the DevHealer custom configurations on Windows 10 must utilize the following directory topologies to prevent workspace pollution, respect Strict Mode constraints, and ensure proper platform discovery.

### Workspace-Local Configuration Scope (Targeted)
```text
C:\Users\Johnny Cage\ITS\
├── setup.py                        # Programmatic installer & Git bootstrapper
├── run_tests_hardened.py           # Process-tree monitor and sweep harness
├── test_harness.ps1                # Dynamic filesystem sensation simulator
├── deploy_global.ps1               # Automated plugin packaging & compiler script
├── discover_system.md              # System DNA scan onboarding query
├── playbook_prompts.md             # Consolidated system and safety prompts
└── .agents/                        # Isolated configuration directory
    ├── hooks.json                  # Flat event-keyed interceptors schema
    ├── mcp_config.json             # Workspace-specific MCP server definitions
    ├── rules/
    │   └── development-ontology.md # Core autonomic MAPE-K loop rules (Max 12,000 chars)
    ├── skills/
    │   └── heal-and-evolve/
    │       └── SKILL.md            # Target reasoning instructions for repair
    └── workflows/
        └── workflow_heal_project.md # Slash trajectory (/workflow_heal_project)
```

### Machine-Global Plugin Scope (Always-On)
```text
C:\Users\Johnny Cage\.gemini\config\plugins\dev-healer\
├── plugin.json                     # Mandatory namespace registry marker
├── hooks.json                      # Global Flat 2.0 event interceptors (Absolute Paths)
├── mcp_config.json                 # Global MCP server mappings (e.g., Turso explorer)
├── rules/
│   └── development-ontology.md     # Persistent global rules across all workspaces
├── skills/
│   └── heal-and-evolve/
│       └── SKILL.md                # Global diagnostic skill instructions
└── scripts/
    ├── pre-tool-use.py             # Active semantic firewall script
    ├── post-tool-use.py            # Anomaly sensing and state capture script
    ├── stop-handler.py             # Self-healing loop control escape script
    └── run_tests_hardened.py       # Hardened Windows process sweeper
```

---

## 🛠️ 2. Hooks Engine Configuration (`hooks.json`)
The platform expects a **flat, event-keyed schema** mapping exact lifecycle event names to arrays of hook commands.

```json
{
  "PreToolUse": [
    {
      "command": "python",
      "args": ["C:/Users/Johnny Cage/.gemini/config/plugins/dev-healer/scripts/pre-tool-use.py"],
      "timeout": 30,
      "type": "command"
    }
  ],
  "PostToolUse": [
    {
      "command": "python",
      "args": ["C:/Users/Johnny Cage/.gemini/config/plugins/dev-healer/scripts/post-tool-use.py"],
      "timeout": 30,
      "type": "command"
    }
  ],
  "Stop": [
    {
      "command": "python",
      "args": ["C:/Users/Johnny Cage/.gemini/config/plugins/dev-healer/scripts/stop-handler.py"],
      "timeout": 30,
      "type": "command"
    }
  ]
}
```

### Key Operational Rules:
1. **Flat Layout Constraint**: Placing handlers inside an outer `{"hooks": [...]}` or nested event objects will cause the platform 2.0 spawner to completely ignore them.
2. **Interpreter Pointer**: Windows 10 environment spawners require `python` as the command executable. Pointers using `python3` will fail.
3. **Paths Normalization**: Backward slashes (`\`) must be normalized to forward slashes (`/`) inside all file path mappings.

---

## 📥 3. Hook Input/Output Payloads Schema (stdin / stdout)
All hooks receive input payloads via standard input (`stdin`) and return system directives via standard output (`stdout`) using **camelCase** serialization.

### PreToolUse Contract
Fires right before any tool execution (e.g., executing a command or writing a file).

#### System Input (`stdin`):
```json
{
  "conversationId": "ec33ebf9-0cba-4100-8142-c61503f6c587",
  "workspacePaths": ["C:/Users/Johnny Cage/ITS"],
  "transcriptPath": "C:/Users/Johnny Cage/.gemini/antigravity/brain/ec33ebf9-0cba-4100-8142-c61503f6c587/.system_generated/logs/transcript.jsonl",
  "artifactDirectoryPath": "C:/Users/Johnny Cage/.gemini/antigravity/brain/ec33ebf9-0cba-4100-8142-c61503f6c587",
  "toolCall": {
    "name": "run_command",
    "args": {
      "CommandLine": "npm test",
      "Cwd": "C:/Users/Johnny Cage/ITS"
    }
  },
  "stepIdx": 19
}
```

#### Expected Script Output (`stdout`):
```json
{
  "decision": "ask",
  "reason": "Requires manual verification before executing tests on active shell.",
  "permissionOverrides": ["command(npm test)"]
}
```
*Possible Decisions: `"allow"` (auto-execute), `"deny"` (hard-block), `"ask"` (interactive prompt based on history), `"force_ask"` (forces prompt regardless of permissions cache).*

---

### PostToolUse Contract
Fires immediately after a tool execution completes, capturing output or runtime failures.

#### System Input (`stdin`):
```json
{
  "conversationId": "ec33ebf9-0cba-4100-8142-c61503f6c587",
  "workspacePaths": ["C:/Users/Johnny Cage/ITS"],
  "transcriptPath": "C:/Users/Johnny Cage/.gemini/antigravity/brain/ec33ebf9-0cba-4100-8142-c61503f6c587/.system_generated/logs/transcript.jsonl",
  "artifactDirectoryPath": "C:/Users/Johnny Cage/.gemini/antigravity/brain/ec33ebf9-0cba-4100-8142-c61503f6c587",
  "stepIdx": 5,
  "error": "exit status 1: Compilation failed in index.js: SyntaxError Unexpected token"
}
```

#### Expected Script Output (`stdout`):
```json
{}
```
*(PostToolUse must return a clean, empty JSON object `{}`. All logging or state modification must happen within out-of-band files, specifically writing structured anomalies to the secure AppData registry).*

---

### Stop (Loop Controller) Contract
Fires when the primary conversation loop attempts to terminate, allowing hooks to trigger loop re-entry if errors persist.

#### System Input (`stdin`):
```json
{
  "conversationId": "ec33ebf9-0cba-4100-8142-c61503f6c587",
  "workspacePaths": ["C:/Users/Johnny Cage/ITS"],
  "transcriptPath": "C:/Users/Johnny Cage/.gemini/antigravity/brain/ec33ebf9-0cba-4100-8142-c61503f6c587/.system_generated/logs/transcript.jsonl",
  "artifactDirectoryPath": "C:/Users/Johnny Cage/.gemini/antigravity/brain/ec33ebf9-0cba-4100-8142-c61503f6c587",
  "executionNum": 1,
  "terminationReason": "model_stop",
  "error": "",
  "fullyIdle": true
}
```

#### Expected Script Output (`stdout`):
```json
{
  "decision": "continue",
  "reason": "Sensation layer reports an active ToolFailure. Initiating /workflow_heal_project trajectory."
}
```
*If `"decision": "continue"` is returned, the platform cancels termination and re-enters the model processing loop, injecting the `"reason"` text as a fresh system instruction.*

---

## 🔌 4. Model Context Protocol Schema (`mcp_config.json`)
Allows your local and global agent sessions to securely integrate databases (like Turso), development linters, and external microservices.

```json
{
  "mcpServers": {
    "turso-sqlite-explorer": {
      "command": "node",
      "args": ["C:/Users/Johnny Cage/AppData/Roaming/npm/node_modules/libsql-mcp-server/index.js"],
      "env": {
        "SQLITE_DB_PATH": "C:/Users/Johnny Cage/ITS/app.db",
        "LIBSQL_URL": "ENV_VAR_PROJECT_TURSO_URL",
        "LIBSQL_AUTH_TOKEN": "ENV_VAR_PROJECT_TURSO_TOKEN"
      },
      "cwd": "C:/Users/Johnny Cage/ITS",
      "disabled": false,
      "disabledTools": ["destructive_query_tool"]
    },
    "enterprise-remote-mcp": {
      "serverUrl": "https://api.example.com/mcp/",
      "headers": {
        "Authorization": "Bearer SECURE_API_BEARER_KEY"
      },
      "authProviderType": "google_credentials",
      "oauth": {
        "clientId": "your-oauth-client-id",
        "clientSecret": "your-oauth-client-secret"
      }
    }
  }
}
```

### Breaking Change Warning:
Legacy schema parameters like `"url"` or `"httpUrl"` are strictly **unsupported** for SSE or websocket configurations. You must explicitly define the endpoint using the `"serverUrl"` key, or the connection will throw a parsing fault.

---

## 📦 5. Plugin Manifest Schema (`plugin.json`)
The manifest registry file required at the root of every global or local plugin bundle.

```json
{
  "$schema": "https://antigravity.google/schemas/plugin.schema.json",
  "name": "dev-healer",
  "description": "Production-hardened MAPE-K loop sidecar watcher, process sweep wrapper, and self-healing trajectory."
}
```
*The `"name"` field is used as the machine-readable plugin namespace matching `^[a-zA-Z0-9-_]+$`. If omitted, it automatically defaults to the folder name.*

---

## 🧭 6. Status Line Script Payload Schema
If you route live agent metadata into custom terminal status lines or title bars using the `statusLine` settings configurations inside your host preferences (`~/.gemini/antigravity-cli/settings.json`), the TUI pipes the following JSON payload directly into your script's standard input:

```json
{
  "cwd": "C:/Users/Johnny Cage/ITS",
  "conversation_id": "ec33ebf9-0cba-4100-8142-c61503f6c587",
  "session_id": "ec33ebf9-0cba-4100-8142-c61503f6c587",
  "transcript_path": "C:/Users/Johnny Cage/.gemini/antigravity-cli/brain/ec33ebf9-0cba-4100-8142-c61503f6c587/.system_generated/logs/transcript.jsonl",
  "model": {
    "id": "gemini-3.1-pro",
    "display_name": "Gemini 3.1 Pro"
  },
  "workspace": {
    "current_dir": "C:/Users/Johnny Cage/ITS",
    "project_dir": "C:/Users/Johnny Cage/ITS"
  },
  "version": "2.0.4",
  "context_window": {
    "total_input_tokens": 14205,
    "total_output_tokens": 2341,
    "context_window_size": 2000000,
    "used_percentage": 0.827,
    "remaining_percentage": 99.173,
    "current_usage": {}
  },
  "exceeds_200k_tokens": false,
  "product": "antigravity",
  "agent_state": "thinking",
  "vcs": {
    "type": "git",
    "branch": "main",
    "client": "git",
    "dirty": true
  },
  "sandbox": {
    "enabled": true,
    "allow_network": false
  },
  "artifact_count": 7,
  "email": "johnny.cage@its.com",
  "pending_input_count": 0,
  "tool_confirmation_pending": false,
  "task_count": 0,
  "terminal_width": 120,
  "execution_mode": "planning"
}
```
