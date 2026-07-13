# Google Antigravity · Complete Documentation (All 7 Pages Combined)

## Contents

1. Antigravity 2.0 (Entries 1–9)
2. Customizations & Capabilities (Entries 10–21)
3. CLI Setup & Daily Use (Entries 22–33)
4. CLI Security & Reference (Entries 34–51)
5. Antigravity SDK (Entry 52)
6. Antigravity IDE (Entries 53–70)
7. Migration, Enterprise, Plans & FAQ (Entries 71–74)

---

# 01 · Antigravity 2.0 · Entries 1–9

## 1. Antigravity 2.0 — Overview

**Source:** [https://antigravity.google/docs/overview](https://antigravity.google/docs/overview)

Antigravity 2.0 is a standalone desktop application for managing AI agents that perform complex knowledge and coding tasks. It operates independently of an IDE and provides a central command center to launch, monitor, and coordinate agents.

Agents can:

- Execute system commands
- Read and write files
- Conduct web searches
- Connect to external tools through skills and MCP servers
- Manage subagents
- Interact with Chrome
- Create artifacts and implementation plans

It is intended for workflows ranging from deep research to building applications.

## 2. Getting Started with Antigravity 2.0

**Source:** [https://antigravity.google/docs/getting-started](https://antigravity.google/docs/getting-started)

### System requirements

- **macOS:** Version 12 Monterey or newer; Intel x86 is unsupported.
- **Windows:** Windows 10, 64-bit.
- **Linux:** `glibc >= 2.28` and `glibcxx >= 3.4.25`.

### Create a project

1. Select the folder-plus icon in the left sidebar.
2. Select **New Project**.
3. Add one or more local folders or Git repositories.
4. Select **Create**.
5. Optionally configure project-specific settings and security policies.

### Start an agent

Enter an instruction, then choose:

- **Local Mode:** Works directly in the active folders.
- **New Worktree Mode:** Works inside an isolated Git worktree.

### Keyboard shortcuts

| Action | macOS | Windows/Linux |
| --- | --- | --- |
| Conversation picker | `⌘K` | `Ctrl+K` |
| File search | `⌘P` | `Ctrl+P` |
| Focus input | `⌘L` | `Ctrl+L` |
| New conversation | `⌘N` | `Ctrl+N` |
| Previous/next conversation | `⌥ ↑/↓` | `Alt+↑/↓` |

### Slash commands

- `/goal` — Continue until the task is finished without requesting intermediate input.
- `/grill-me` — Ask clarifying questions before implementation.
- `/schedule` — Run an instruction later or on a recurring schedule.
- `/browser` — Explicitly enable browser operations; requires Chrome and debugging permission.

## 3. Build with Google

**Source:** [https://antigravity.google/docs/build-with-google](https://antigravity.google/docs/build-with-google)

Antigravity provides curated integration bundles containing **skills, MCP servers, and editor extensions** for Google technology ecosystems.

### Enable integrations

- Select integrations during onboarding.
- Or open **Settings → Customizations → Build with Google Plugins**.

### Available bundles

- **Modern Web Guidance:** Accessibility, performance, security, and current web-development practices.
- **Firebase:** Write code, configure security rules, manage authentication users, deploy rules, and work with Firestore data.
- **Antigravity SDK:** Build Python agents, configure models, register tools, connect MCP servers, and implement safety policies.
- **Android CLI:** Create, deploy, test, optimize, and modernize Android applications.
- **Science:** Curated scientific skills for research workflows.
- **Chrome DevTools:** Browser automation, accessibility debugging, Core Web Vitals, visual testing, and memory-leak diagnosis.
- **Dart and Flutter:** Static analysis, package management, formatting, automated renaming, adaptive layouts, and multiplatform development.

## 4. Antigravity 2.0 Features

**Source:** [https://antigravity.google/docs/features](https://antigravity.google/docs/features)

### Projects

- Native Git worktree support for isolated agent work.
- Project-level security settings: **Default**, **Full Machine**, and **Unrestricted**.
- Persistent permission grants for trusted actions.
- Multiple folders and codebases within one project.

### Independent conversations

Quick conversations can run outside projects in isolated scratch folders. They have separate settings and permissions while inheriting global permissions.

### Scheduled tasks

- Schedule messages for agents to process while you are away.
- Create recurring, time-based triggers.
- Powered by Gemini 3.5 Flash.

### Security

- Agents request approval before running terminal commands by default.
- File access is limited to project folders unless **Full Machine** or **Unrestricted** access is enabled.

### Voice transcription

- Start and stop with the microphone button or `Ctrl+M`.
- Live transcription appears in the input field.
- Automatically removes filler words, repetitions, and self-corrections.
- Available for agent prompts and artifact comments.

### JSON hooks

Run custom local shell scripts at key execution stages:

- Before tool calls
- After model responses
- At agent-loop stopping conditions
- Globally or per project using JSON configuration

### Browser agent

- Activated with `/browser`.
- Integrates with Chrome DevTools MCP.
- Supports browser-session recordings in WebM format.

## 5. Models

**Source:** [https://antigravity.google/docs/models](https://antigravity.google/docs/models)

### Reasoning models by plan

| Model | Standard | AI Pro | AI Ultra | Enterprise |
| --- | --- | --- | --- | --- |
| Gemini 3.5 Flash | ✅ | ✅ | ✅ | ✅ |
| Gemini 3.1 Pro | ✅ | ✅ | ✅ | ✅ |
| Claude Sonnet 4.6 Thinking | — | — | ✅ | — |
| Claude Opus 4.6 Thinking | — | — | ✅ | — |
| GPT-OSS-120B | — | — | ✅ | — |
- Select the reasoning model below the conversation prompt.
- The selection remains active throughout the current user turn.
- Changing models while an agent is working takes effect after that turn finishes or is canceled.
- **Nano Banana 2** is automatically used for image generation, UI mockups, diagrams, and visual assets.

## 6. Projects

**Source:** [https://antigravity.google/docs/projects](https://antigravity.google/docs/projects)

A project defines the folders, environment, permissions, and settings available to an agent.

### Projects versus legacy workspaces

| Legacy workspace | Project |
| --- | --- |
| Tied to one repository | Can include multiple folders and repositories |
| One directory boundary | Cross-folder access |
| Machine-level settings | Isolated project settings |
| Broad global permissions | Global plus project-specific permissions |
| Workspace customizations | Reusable global skills, MCPs, and hooks |

### Folder types

- Local folders without Git
- Local Git repository checkouts

### Operating modes

- **Local Mode:** Agents edit active folders directly.
- **New Worktree Mode:** Each conversation receives an isolated Git worktree, preventing conflicts during parallel work.

### Default security

New projects initially:

- Allow reading and writing inside project folders.
- Require approval before running terminal commands.
- Inherit global permissions while supporting additional project-level permissions.

### Common workflows

- One project for a single folder
- One project spanning frontend and backend repositories
- Multiple agents sharing active folders through Local Mode
- Isolated concurrent agents through New Worktree Mode
- Combined Git checkouts and non-Git folders

## 7. Settings

**Source:** [https://antigravity.google/docs/settings](https://antigravity.google/docs/settings)

Open settings using:

- `Cmd+,`
- **Settings** at the bottom of the sidebar
- The gear beside a project

### Settings categories

1. **Global settings**
    - Account and telemetry
    - Global permissions
    - Appearance
    - Browser integration
    - Default models
    - MCP servers, skills, and Google plugins
2. **Project settings**
    - Associated folders and Git repositories
    - Local versus worktree operation
    - Terminal-execution policy
    - Access outside project folders
    - Terminal sandbox
    - Project permissions and customizations
3. **Standalone conversations**
    - Operate in a local scratch directory
    - Maintain independent terminal, file-access, and permission settings
4. **Miscellaneous**
    - Keyboard shortcuts
    - Product feedback

Telemetry can be enabled or disabled under **Settings → Account**.

## 8. Agent Settings

**Source:** [https://antigravity.google/docs/agent-settings](https://antigravity.google/docs/agent-settings)

### Terminal command execution

- **Request Review:** Never automatically execute terminal commands unless they match the allowlist.
- **Always Proceed:** Automatically execute commands unless they match the denylist.

### Files outside the project

By default, agents can access:

- Folders assigned to the active project
- Antigravity application data under `~/.gemini/antigravity/`

Access to files outside these locations should be enabled cautiously because it may expose sensitive local data.

## 9. Artifact Review

**Source:** [https://antigravity.google/docs/artifact-review](https://antigravity.google/docs/artifact-review)

### Execution modes

- **Planning Mode:** Researches the codebase, organizes tasks, and creates structured implementation-plan artifacts before making changes.
- **Fast Mode:** Executes simple, localized tasks without a dedicated planning phase.

### Review policies

- **Request Review — recommended:** The agent pauses after generating a plan or code diff. You can review it, add inline comments, and approve it before implementation.
- **Always Proceed:** The agent bypasses manual approval and immediately executes its plan for a fully autonomous workflow.

---

# 02 · Customizations & Capabilities · Entries 10–21

## 10. Model Context Protocol

**Source:** [https://antigravity.google/docs/mcp](https://antigravity.google/docs/mcp)

MCP connects Antigravity to external tools, databases, APIs, and live data.

- Manage servers under **Settings → Customizations → Installed MCP Servers**.
- IDE and CLI configurations use:
    - Global: `~/.gemini/config/mcp_config.json`
    - Project: `.agents/mcp_config.json`
- Supports local `stdio` and remote HTTP/SSE servers.
- Authentication options include Google credentials, OAuth, and custom headers.
- Permissions can cover one tool, one server, or all MCP tools.
- Available integrations include GitHub, Notion, Linear, Firebase, Figma, Stripe, Supabase, Chrome DevTools, and many others.

## 11. Agent Skills

**Source:** [https://antigravity.google/docs/skills](https://antigravity.google/docs/skills)

A skill is a reusable folder containing agent instructions in `SKILL.md`.

### Locations

- Project: `.agents/skills/<skill-name>/`
- Global: `~/.gemini/config/skills/<skill-name>/`

`SKILL.md` requires a clear `description` in YAML frontmatter. Skills can also contain scripts, examples, resources, and templates.

The agent uses skills through:

1. **Discovery:** Reads available names and descriptions.
2. **Activation:** Loads relevant instructions.
3. **Execution:** Follows the instructions during the task.

## 12. Rules and Workflows

**Source:** [https://antigravity.google/docs/rules-workflows](https://antigravity.google/docs/rules-workflows)

### Rules

Rules are Markdown constraints that guide agent behavior.

- Global: `~/.gemini/GEMINI.md`
- Project: `.agents/rules/`
- Maximum size: 12,000 characters per file
- Activation options:
    - Manual
    - Always on
    - Model decision
    - File-glob match

Rules may reference other files using `@filename`.

### Workflows

Workflows define repeatable sequences of steps and run through `/workflow-name`.

- Can be global or project-specific.
- Can invoke other workflows.
- Can be generated from a completed conversation.
- Maximum size: 12,000 characters per file.

## 13. Plugins

**Source:** [https://antigravity.google/docs/plugins](https://antigravity.google/docs/plugins)

Plugins bundle skills, rules, MCP servers, and hooks into one package.

```
plugins/<plugin-name>/
├── plugin.json
├── mcp_config.json
├── hooks.json
├── skills/
└── rules/
```

Plugin locations:

- Project: `.agents/plugins/`
- Global: `~/.gemini/config/plugins/`

Each plugin requires `plugin.json`; the `name` field is optional and otherwise defaults to the directory name.

## 14. Hooks

**Source:** [https://antigravity.google/docs/hooks](https://antigravity.google/docs/hooks)

Hooks execute shell commands at specific points in the agent loop.

### Events

- `PreToolUse`
- `PostToolUse`
- `PreInvocation`
- `PostInvocation`
- `Stop`

They are configured in `.agents/hooks.json` or `~/.gemini/config/hooks.json`.

Hooks:

- Match tools using regular expressions.
- Receive JSON through standard input.
- Return JSON through standard output.
- Can allow, deny, or require approval for tool calls.
- Can inject messages or tool calls.
- Can force the agent to continue or terminate.
- Support configurable command timeouts.

## 15. Sidecars

**Source:** [https://antigravity.google/docs/sidecars](https://antigravity.google/docs/sidecars)

Sidecars are persistent background processes managed by Antigravity. They can run scripts, respond to events, or perform scheduled work.

### Locations

- Global: `~/.gemini/config/sidecars/`
- Plugin: `~/.gemini/config/plugins/<plugin>/sidecars/`

Each sidecar uses `sidecar.json` and supports:

- A command or built-in scheduler
- Arguments and environment variables
- Restart policies: `always`, `on-failure`, or `never`
- Cron schedules
- `agentapi` for creating conversations or sending messages

Sidecars are disabled until explicitly enabled in `~/.gemini/config/config.json`.

## 16. Agent Permissions

**Source:** [https://antigravity.google/docs/permissions](https://antigravity.google/docs/permissions)

Every sensitive operation is represented as `action(target)` and evaluated using:

1. **Deny**
2. **Ask**
3. **Allow**

That precedence order means Deny overrides Ask, and Ask overrides Allow.

### Supported permissions

- `read_file`
- `write_file`
- `read_url`
- `execute_url`
- `command`
- `unsandboxed`
- `mcp`

Project-file access is generally allowed by default. Commands, MCP tools, browser interactions, and files outside the project default to **Ask**.

Additional rules:

- Write permission implies read permission.
- Denying read access also denies writing.
- Browser viewing and browser interaction use separate permissions.
- Terminal sandboxing uses approved file paths and domains as its access boundaries.

## 17. Asynchronous Subagents

**Source:** [https://antigravity.google/docs/subagents](https://antigravity.google/docs/subagents)

Subagents execute delegated tasks concurrently without filling the parent agent’s context.

### Characteristics

- Use the parent’s model but begin with an empty conversation.
- Can share the parent workspace or use an isolated Git worktree.
- Can communicate with other agents.
- Preserve their context when idle and reawakened.
- Inherit the parent’s security and permission boundaries.

### States

- **Running**
- **Idle**
- **Killed**

Built-in subagents include:

- `research`
- `browser`
- `self`

Delegation supports up to ten nested levels. `/teamwork-preview` provides advanced orchestration for Ultra-plan users.

## 18. Artifacts

**Source:** [https://antigravity.google/docs/artifacts](https://antigravity.google/docs/artifacts)

Artifacts are structured deliverables created by agents, including:

- Implementation plans
- Code diffs
- Architecture diagrams
- Images
- Browser recordings

They support asynchronous collaboration by letting you review key milestones rather than every individual tool call. You can leave inline feedback and approve plans or edits before execution.

## 19. Implementation Plans

**Source:** [https://antigravity.google/docs/implementation-plan](https://antigravity.google/docs/implementation-plan)

An implementation plan explains the technical changes an agent intends to make.

Unless **Always Proceed** is enabled, the agent normally requests approval before implementation. You can:

- Select **Proceed** to approve.
- Add inline comments.
- Reduce or change scope.
- Request a different technology.
- Submit a review and have the agent revise the plan.

## 20. Walkthroughs

**Source:** [https://antigravity.google/docs/walkthrough](https://antigravity.google/docs/walkthrough)

A walkthrough is generated after implementation and summarizes what changed. It helps you understand the resulting state without following every execution step.

Browser-task walkthroughs may include screenshots and screen recordings.

## 21. Screenshots

**Source:** [https://antigravity.google/docs/screenshots](https://antigravity.google/docs/screenshots)

The browser subagent can capture:

- Entire open pages
- Specific page elements

Screenshots are stored as image artifacts. You can comment directly on them to provide visual feedback to the agent.

---

# 03 · CLI Setup & Daily Use · Entries 22–33

## 22. Antigravity CLI Overview

**Source:** [https://antigravity.google/docs/cli/overview](https://antigravity.google/docs/cli/overview)

Antigravity CLI is a lightweight terminal interface that provides:

- Multi-step reasoning
- Multi-file editing
- Tool execution
- Conversation history
- SSH and headless operation
- Shared settings and permissions with Antigravity 2.0
- Conversation export to the desktop application

It uses the same underlying agent system as Antigravity 2.0 but is optimized for keyboard-driven terminal workflows.

## 23. CLI Getting Started

**Source:** [https://antigravity.google/docs/cli/getting-started](https://antigravity.google/docs/cli/getting-started)

### Quick installation

**macOS or Linux**

```bash
curl -fsSL https://antigravity.google/cli/install.sh | bash
```

**Windows PowerShell**

```powershell
irm https://antigravity.google/cli/install.ps1 | iex
```

**Windows Command Prompt**

```bash
curl -fsSL https://antigravity.google/cli/install.cmd -o install.cmd && install.cmd && del install.cmd
```

Launch the CLI from a project directory:

```bash
agy
```

First launch includes theme selection, rendering-mode selection, and project trust confirmation.

## 24. Installation and Authentication

**Source:** [https://antigravity.google/docs/cli/install](https://antigravity.google/docs/cli/install)

Default installation locations:

- macOS/Linux: `~/.local/bin/agy`
- Windows: `%LOCALAPPDATA%\agy\bin`

Installation flags:

- `--skip-aliases` — Preserve existing shell aliases.
- `--skip-path` — Prevent automatic shell-path changes.

Authentication uses the operating system’s secure credential store. Local sessions can open a browser automatically; SSH sessions provide a URL and authorization code.

Sign out and remove cached credentials with:

```
/logout
```

## 25. CLI Tutorial

**Source:** [https://antigravity.google/docs/cli/tutorial](https://antigravity.google/docs/cli/tutorial)

The tutorial demonstrates this workflow:

1. Create an empty project directory.
2. Run `agy`.
3. Ask the agent to create a Python web-scraping utility.
4. Press `Ctrl+R` to open artifact review.
5. Inspect `main.py`.
6. Press `y` to approve it.
7. Ask the agent to execute `python3 main.py`.
8. Approve the command.
9. Exit with `Ctrl+D` or `/exit`.

## 26. Using AGY CLI

**Source:** [https://antigravity.google/docs/cli/using](https://antigravity.google/docs/cli/using)

Configuration is stored at:

```
~/.gemini/antigravity-cli/settings.json
```

Open settings with `/config` or `/settings`.

### Useful commands

- `@` — Suggest file paths
- `!command` — Run a terminal command directly
- `?` — Display help
- `/permissions` — Manage agent permissions
- `/rewind` or `/undo` — Return to an earlier checkpoint
- `/fork` — Branch the current conversation
- `/clear` — Start a new conversation
- `/resume` — Resume an earlier session
- `/keybindings` — Customize keyboard controls

Custom keybindings are stored in:

```
~/.gemini/antigravity-cli/keybindings.json
```

## 27. CLI Features

**Source:** [https://antigravity.google/docs/cli/features](https://antigravity.google/docs/cli/features)

### Primary features

- Installable plugins
- Native terminal sandboxing
- Fine-grained permissions
- Conversation management
- MCP-server management
- Skills and custom workflows
- Interactive diff review
- Background tasks and subagents
- Custom status lines and terminal titles

### Important commands

- `/resume`
- `/rewind`
- `/permissions`
- `/model`
- `/agents`
- `/tasks`
- `/skills`
- `/mcp`
- `/diff`
- `/usage`
- `/logout`

The sandbox uses native operating-system isolation: `nsjail` on Linux, `sandbox-exec` on macOS, and AppContainer on Windows.

## 28. Migrating from Gemini CLI

**Source:** [https://antigravity.google/docs/cli/gcli-migration](https://antigravity.google/docs/cli/gcli-migration)

Antigravity detects legacy Gemini CLI configuration during first launch and can import settings, credentials, and extensions.

Convert Gemini extensions into Antigravity plugins with:

```bash
agy plugin import gemini
```

### Updated locations

| Configuration | Gemini CLI | Antigravity CLI |
| --- | --- | --- |
| Global skills | `~/.gemini/skills/` | `~/.gemini/antigravity-cli/skills/` |
| Project skills | `.gemini/skills/` | `.agents/skills/` |
| Global MCP | Inside `settings.json` | `~/.gemini/config/mcp_config.json` |
| Project MCP | Inside project settings | `.agents/mcp_config.json` |

Remote MCP configurations must use `serverUrl`, not the older `url` or `httpUrl`.

## 29. Prompting and Interaction

**Source:** [https://antigravity.google/docs/cli/prompting](https://antigravity.google/docs/cli/prompting)

- Press `Enter` to submit a prompt.
- Press `Esc` to cancel the current turn or close an overlay.
- Use `Shift+Enter` or `Ctrl+J` for a new line.
- On macOS Terminal, use `Option+Enter` when configured as the Meta key.
- End a line with `\` and press Enter for a universal newline.
- Press `Ctrl+G` to compose a long prompt in `$EDITOR`.
- Press `Ctrl+V` to attach supported images or videos.

Supported media includes PNG, JPEG, GIF, WebP, SVG, MP4, MOV, WebM, and AVI.

## 30. Reviewing CLI Artifacts

**Source:** [https://antigravity.google/docs/cli/artifacts](https://antigravity.google/docs/cli/artifacts)

Press `Ctrl+R` to open the artifact-review interface.

### Review controls

- `↑` / `↓` — Navigate
- `p` — Preview
- `y` — Approve
- `n` — Reject
- `Shift+A` — Approve everything
- `Shift+R` — Reject everything
- `Enter` — Open the detailed viewer
- `Esc` — Submit decisions and return

Inside the detailed viewer:

- `c` — Comment on a line
- `d` — Delete a comment
- `g` / `Shift+G` — Jump to top or bottom
- `m` — Cycle Mermaid rendering
- `Ctrl+=` / `Ctrl+-` — Zoom diagrams

## 31. Managing Conversations

**Source:** [https://antigravity.google/docs/cli/conversations](https://antigravity.google/docs/cli/conversations)

Conversation history is scoped to the directory from which `agy` is launched.

Resume sessions with:

- `/resume`
- `agy -c`
- `agy --continue`

Use `/fork` or `/branch` to duplicate the current conversation into an independent session. This branches the conversation history, but it does **not** create a separate Git checkout.

## 32. CLI Execution Modes

**Source:** [https://antigravity.google/docs/cli/modes](https://antigravity.google/docs/cli/modes)

| Mode | Behavior |
| --- | --- |
| `default` | Requires review before changing files |
| `accept-edits` | Automatically approves file changes |
| `plan` | Investigates and creates a plan before editing |

Press `Shift+Tab` to cycle through modes.

Launch directly in a mode:

```bash
agy --mode=accept-edits
agy --mode=plan
```

Persist the default in `settings.json`:

```json
{
  "agentMode": "accept-edits"
}
```

Tool permissions continue to apply regardless of the selected execution mode.

## 33. CLI Background Tasks and Subagents

**Source:** [https://antigravity.google/docs/cli/subagents](https://antigravity.google/docs/cli/subagents)

Subagents handle builds, research, validation, and multi-file work in parallel while the primary conversation remains usable.

- `/agents` — View and manage subagents.
- `/tasks` — Monitor non-agent background processes and terminal commands.
- Select an agent to inspect its activity and tool logs.
- `Alt+J` — Jump to the next subagent awaiting approval.
- `Ctrl+K` — Approve a pending action without leaving the primary conversation.
- Background tasks can be inspected or terminated from their respective panels.

---

# 04 · CLI Security & Reference · Entries 34–51

## 34. CLI Sandbox

**Source:** [https://antigravity.google/docs/cli/sandbox](https://antigravity.google/docs/cli/sandbox)

The terminal sandbox isolates agent-run commands using native operating-system security:

- **Linux:** `nsjail`
- **macOS:** `sandbox-exec`
- **Windows:** AppContainer

Enable it in `~/.gemini/antigravity-cli/settings.json`:

```json
{
  "enableTerminalSandbox": true
}
```

When enabled, individual commands can temporarily be approved to run outside the sandbox. When disabled, a potentially risky command can be run inside the sandbox for that execution only.

## 35. CLI Permissions

**Source:** [https://antigravity.google/docs/cli/permissions](https://antigravity.google/docs/cli/permissions)

Permissions use the format `action(target)` and three policy lists:

1. **Deny**
2. **Ask**
3. **Allow**

The precedence is **Deny → Ask → Allow**.

Supported actions include:

- `read_file`
- `write_file`
- `read_url`
- `execute_url`
- `command`
- `unsandboxed`
- `mcp`

Project files are automatically accessible by default. Commands, MCP tools, browser actions, external URLs, and files outside the project default to **Ask**.

Example:

```json
{
  "permissions": {
    "allow": [
      "command(git)",
      "command(npm run (build|lint|test))",
      "read_url(google.com)"
    ],
    "deny": [
      "command(rm -rf)",
      "command(sudo)",
      "write_file(.git/)"
    ],
    "ask": [
      "command(*)",
      "mcp(sql/execute_mutation)"
    ]
  }
}
```

## 36. CLI Settings and Rendering

**Source:** [https://antigravity.google/docs/cli/settings](https://antigravity.google/docs/cli/settings)

Open the settings editor with `/config` or `/settings`.

### Security options

- **Tool permission:** Request review, proceed in sandbox, strict, or always proceed.
- **Artifact review:** Always ask, agent decides, or always proceed.
- **Terminal sandbox:** Enable native command isolation.
- **External-file access:** Control access outside active projects.

### Rendering modes

- **Alt-screen:** Full-screen application interface with integrated scrolling.
- **Inline:** Preserves output in normal terminal history; recommended for SSH and `tmux`.
- **Adaptive:** Automatically selects the most appropriate mode.

Other settings cover themes, animation speed, verbosity, editor selection, notifications, telemetry, tips, surveys, credits, status lines, and terminal titles.

## 37. AI Credits and Quotas

**Source:** [https://antigravity.google/docs/cli/credits](https://antigravity.google/docs/cli/credits)

The CLI status line can display remaining AI credits and warn when the balance is low.

Enable credit fallback in settings:

```json
{
  "useG1Credits": true
}
```

When enabled, personal credits may be consumed after the plan’s included quota is exhausted. The setting is also available through `/config`.

## 38. CLI Plugins and Skills

**Source:** [https://antigravity.google/docs/cli/plugins](https://antigravity.google/docs/cli/plugins)

Plugins are stored under:

```
~/.gemini/antigravity-cli/plugins/<plugin-name>/
```

A plugin can contain:

- Skills
- Custom agents
- Rules
- MCP configurations
- Hooks

### Plugin commands

```bash
agy plugin list
agy plugin install /path/to/plugin
agy plugin disable <plugin-name>
agy plugin enable <plugin-name>
agy plugin uninstall <plugin-name>
```

Project skills live in `.agents/skills/`. Global skills live in `~/.gemini/antigravity-cli/skills/` and become slash commands in the TUI.

## 39. Status-Line Customization

**Source:** [https://antigravity.google/docs/cli/statusline](https://antigravity.google/docs/cli/statusline)

Configure a custom status-line script:

```json
{
  "statusLine": {
    "type": "command",
    "command": "~/.gemini/antigravity-cli/statusline.sh"
  }
}
```

Antigravity passes a JSON state payload to the script through standard input and renders the script’s standard output.

Available information includes:

- Agent state and active model
- Project directory and conversation ID
- Token usage
- Quota status
- Git branch and dirty state
- Sandbox state
- Artifact and task counts
- Subscription tier
- Execution mode

ANSI colors are supported.

## 40. Terminal-Title Customization

**Source:** [https://antigravity.google/docs/cli/title](https://antigravity.google/docs/cli/title)

Configure a dynamic terminal-title script:

```json
{
  "title": {
    "type": "command",
    "command": "~/.gemini/antigravity-cli/title.sh"
  }
}
```

The script receives the same JSON payload as the custom status line. Its output becomes the terminal window title. ANSI codes and non-printable characters are removed automatically.

## 41. `/agents` Command

**Source:** [https://antigravity.google/docs/cli/commands/agents](https://antigravity.google/docs/cli/commands/agents)

`/agents` opens the Agent Manager for:

- Selecting custom agents
- Monitoring subagents
- Inspecting completed or failed work
- Approving protected actions
- Terminating running subagents

### Custom-agent locations

- Project: `.agents/agents/<name>/agent.md`
- Global: `~/.gemini/config/agents/<name>/agent.md`

Switching agents during an active conversation creates a fork so the existing history is preserved.

### Controls

- `↑` / `↓` — Navigate
- `Enter` — Select, expand, or inspect
- `k` — Terminate a running subagent
- `a` — Approve an action
- `d` — Deny an action
- `Esc` — Apply the selection and exit

## 42. `/credits` Command

**Source:** [https://antigravity.google/docs/cli/commands/credits](https://antigravity.google/docs/cli/commands/credits)

Run:

```
/credits
```

The panel shows:

- Current AI Premium credit balance
- Usage during the current billing cycle
- Links for purchasing credits
- Subscription-upgrade links

Press `Esc` to close it.

## 43. `/diff` Command

**Source:** [https://antigravity.google/docs/cli/commands/diff](https://antigravity.google/docs/cli/commands/diff)

`/diff` opens an interactive viewer with three modes:

- **VCS:** Modified and untracked project files
- **Turn:** Changes grouped by agent conversation turn
- **Commit:** Interactive repository commit graph

It supports Git, Mercurial, and Jujutsu.

### Controls

- `Tab` — Cycle between modes
- `Enter` — Open a selected diff
- `n` / `N` — Move between diff sections
- `c` — Add a line-level comment
- `d` — Delete a comment
- `Shift+Y` — Exit and send comments to the agent
- `Shift+N` — Exit and discard comments

## 44. `/permissions` Command

**Source:** [https://antigravity.google/docs/cli/commands/permissions](https://antigravity.google/docs/cli/commands/permissions)

`/permissions` opens an interactive manager for editing agent security rules.

### Permission scopes

- **Project:** Applies only to the active project.
- **Shared:** Used across Antigravity products.
- **Global:** Applies to every CLI session.

### Controls

- `Tab` or `←` / `→` — Switch between Allow, Deny, and Ask
- `a` — Add a rule
- `e` or `Ctrl+G` — Edit a rule
- `d` or `Backspace` — Delete a rule
- `Enter` — Validate and save
- `Esc` — Return or exit

Rules must follow `action(target)` format, such as:

```
command(git)
read_file(/var/log/app)
mcp(server/tool)
```

## 45. `/resume` Command

**Source:** [https://antigravity.google/docs/cli/commands/resume](https://antigravity.google/docs/cli/commands/resume)

`/resume`, `/switch`, or `/conversation` opens the Session Picker.

You can:

- Search by title, preview, or conversation ID
- Navigate conversations by recency
- Press `F2` to rename a conversation
- Press `Ctrl+Delete` to delete one
- Press `Tab` to view and import Antigravity 2.0 conversations

### Shell shortcuts

Resume the latest conversation for the current project:

```bash
agy -c
agy --continue
```

Resume a specific conversation:

```bash
agy --conversation <conversation-id>
```

The latest conversation per project is tracked in:

```
~/.gemini/antigravity-cli/cache/last_conversations.json
```

## 46. `/statusline` Command

**Source:** [https://antigravity.google/docs/cli/commands/statusline](https://antigravity.google/docs/cli/commands/statusline)

Control the TUI status line with:

```
/statusline
/statusline on
/statusline off
/statusline enable
/statusline disable
/statusline reset
```

With no argument, `/statusline` toggles the current state. It can also be configured to run a custom command that receives live agent-state JSON and returns formatted status text.

## 47. `/title` Command

**Source:** [https://antigravity.google/docs/cli/commands/title](https://antigravity.google/docs/cli/commands/title)

Control dynamic terminal-window titles with:

```
/title
/title on
/title off
```

When enabled, the title can display the active model, project, and agent state. Running `/title` without an argument toggles the feature.

## 48. `/usage` and `/quota`

**Source:** [https://antigravity.google/docs/cli/commands/usage](https://antigravity.google/docs/cli/commands/usage)

`/usage` or `/quota` refreshes quota data and opens the Model Quotas panel.

It displays:

- Usage by model
- Remaining requests or tokens
- Updated quota information from the backend

### Controls

- `↑` / `↓` or `j` / `k` — Scroll
- `PgUp` / `PgDn` — Move by page
- `g` / `G` — Jump to top or bottom
- `Esc` or `q` — Close

## 49. CLI Best Practices

**Source:** [https://antigravity.google/docs/cli/best-practices](https://antigravity.google/docs/cli/best-practices)

### Recommended workflow

1. Provide tests, build commands, or formatting checks.
2. Ask the agent to explore the codebase first.
3. Request an implementation plan.
4. Review and approve the plan.
5. Execute the changes.
6. Run local verification.

Additional recommendations:

- Use `@` to reference exact files.
- Attach screenshots or recordings for visual issues.
- Add `GEMINI.md` or `AGENTS.md` with project conventions.
- Enable sandboxed execution for trusted automation.
- Press `Esc` to stop incorrect work early.
- Use `/rewind` to return to an earlier checkpoint.
- Use `/fork` for experimental approaches.
- Delegate large work to parallel subagents.

Run a non-interactive prompt with:

```bash
agy -p "Review this git diff and draft a conventional commit message" --cwd "$(pwd)"
```

## 50. Troubleshooting

**Source:** [https://antigravity.google/docs/cli/troubleshooting](https://antigravity.google/docs/cli/troubleshooting)

### `agy: command not found`

Add the installation directory to `PATH`:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Then reload the shell profile.

### Locked keyring

- **macOS:** Authorize `agy` through Keychain Access.
- **Linux:** Ensure the keyring and D-Bus session are active.
- **Windows:** Verify access through Credential Manager.

### Clipboard failures over SSH

Use a terminal supporting clipboard forwarding, such as iTerm2 or Ghostty. For `tmux`:

```
set -s set-clipboard on
```

### Updater lock

Remove a stale lock:

```bash
rm -f ~/.gemini/antigravity-cli/updater/update.lock
```

Disable automatic updates:

```bash
export AGY_CLI_DISABLE_AUTO_UPDATE=true
```

## 51. CLI Reference

**Source:** [https://antigravity.google/docs/cli/reference](https://antigravity.google/docs/cli/reference)

The reference collects all slash commands, keyboard shortcuts, and configuration keys.

### Core commands

| Command | Purpose |
| --- | --- |
| `/agents` | Select and monitor agents |
| `/artifact` | Review artifacts |
| `/btw` | Ask a background question |
| `/config` | Edit settings |
| `/context` | Inspect context usage |
| `/diff` | Review changes and commits |
| `/fork` | Branch the conversation |
| `/mcp` | Manage MCP servers |
| `/model` | Select a model |
| `/permissions` | Manage security rules |
| `/resume` | Resume conversations |
| `/rewind` | Restore an earlier point |
| `/skills` | View agent skills |
| `/tasks` | Monitor background tasks |
| `/usage` | View model quotas |

### Example configuration

```json
{
  "colorScheme": "tokyo night",
  "altScreenMode": "always",
  "toolPermission": "request-review",
  "notifications": true,
  "enableTerminalSandbox": true
}
```

---

# 05 · Antigravity SDK · Entry 52

## 52. Antigravity SDK

**Source:** [https://antigravity.google/docs/sdk/overview](https://antigravity.google/docs/sdk/overview)

The Antigravity SDK is a Python framework for building, testing, and running autonomous agents using the same core agent system as Antigravity CLI and 2.0.

Install it with:

```bash
pip install google-antigravity
```

Basic example:

```python
import asyncio
from google.antigravity import Agent, LocalAgentConfig

async def main():
    config = LocalAgentConfig()

    async with Agent(config) as agent:
        response = await agent.chat(
            "What files are in the current directory?"
        )
        print(await response.text())

asyncio.run(main())
```

### Capabilities

- Built-in file, code-editing, search, and shell tools
- Custom Python tools
- MCP servers
- Agent skills
- Declarative security policies
- Lifecycle hooks
- Streaming responses
- Images, PDFs, audio, and video
- Subagents
- Structured Pydantic output
- Human approval and questions
- Token-usage observability

---

# 06 · Antigravity IDE · Entries 53–70

## 53. Antigravity IDE Overview

**Source:** [https://antigravity.google/docs/ide/overview](https://antigravity.google/docs/ide/overview)

Antigravity IDE combines an editor, terminal, browser, and autonomous agents in one development environment.

> Antigravity IDE is not supported for enterprise configurations. Enterprise users should use Antigravity 2.0 or Antigravity CLI.
> 

### Main features

- AI-powered editor
- Advanced Tab completion
- Parallel local agents
- Browser automation
- Planning and implementation artifacts
- Code diffs and architecture diagrams
- Browser screenshots and recordings

## 54. IDE Getting Started

**Source:** [https://antigravity.google/docs/ide/getting-started](https://antigravity.google/docs/ide/getting-started)

Download from:

[https://antigravity.google/download](https://antigravity.google/download)

### Requirements

- **macOS:** Version 12 Monterey or newer; Intel x86 unsupported
- **Windows:** Windows 10, 64-bit
- **Linux:** `glibc >= 2.28` and `glibcxx >= 3.4.25`

The IDE displays a notification when an update becomes available.

## 55. IDE Tab and Navigation

**Source:** [https://antigravity.google/docs/ide/tab](https://antigravity.google/docs/ide/tab)

### Supercomplete

Provides code suggestions near the cursor and can update multiple areas of a file simultaneously. Press `Tab` to accept.

### Tab-to-Jump

Predicts the next logical editing location. Press `Tab` to move there.

### Tab-to-Import

Detects missing dependencies and inserts the required import at the top of the file.

### Settings

You can:

- Enable or disable each Tab feature
- Select slow, default, or fast suggestion speed
- Highlight inserted text
- Use clipboard contents as completion context
- Enable suggestions inside `.gitignore` files

## 56. IDE Browser Overview

**Source:** [https://antigravity.google/docs/ide/browser](https://antigravity.google/docs/ide/browser)

Antigravity can open, read, and interact with a local Chrome browser.

The browser subagent can:

- Test development websites
- Read documentation
- Interact with web applications
- Capture screenshots
- Save action videos as artifacts

Browser tools can be disabled under **User Settings → Browser**. Security is provided through URL allowlists, denylists, and an isolated Chrome profile.

## 57. Agent Side Panel

**Source:** [https://antigravity.google/docs/ide/agent-side-panel](https://antigravity.google/docs/ide/agent-side-panel)

The right-side Agent panel supports:

- Starting conversations
- Attaching images
- Switching agent modes
- Selecting models
- Monitoring changed files
- Monitoring terminal processes
- Reviewing artifacts

Current activity appears in the toolbar above the prompt input.

## 58. Review Changes

**Source:** [https://antigravity.google/docs/ide/review-changes-editor](https://antigravity.google/docs/ide/review-changes-editor)

After an agent edits code, select **Review Changes** in the Agent panel’s bottom toolbar.

The review pane displays all changes made by you and the agent during the conversation. You can comment directly on file diffs to request corrections or guide the agent’s next actions.

## 59. IDE Implementation Plans

**Source:** [https://antigravity.google/docs/ide/implementation-plan](https://antigravity.google/docs/ide/implementation-plan)

An implementation-plan artifact explains the technical changes an agent intends to make.

Unless **Always Proceed** is enabled, the agent normally requests review before implementation.

You can:

- Select **Proceed** to approve the plan.
- Add comments to particular sections.
- Reduce the scope.
- Request another technology.
- Correct errors or assumptions.
- Submit a review and request a revised plan.

## 60. IDE Walkthroughs

**Source:** [https://antigravity.google/docs/ide/walkthrough](https://antigravity.google/docs/ide/walkthrough)

After finishing implementation, the agent can produce a walkthrough containing:

- A concise summary of completed changes
- The resulting codebase state
- Relevant screenshots
- Browser screen recordings

Walkthroughs are useful when the agent worked asynchronously and you did not monitor every step.

## 61. IDE Screenshots

**Source:** [https://antigravity.google/docs/ide/screenshots](https://antigravity.google/docs/ide/screenshots)

The browser subagent can capture:

- Complete browser pages
- Specific elements on a page

Screenshots are saved as image artifacts. You can comment directly on them to provide visual feedback.

## 62. IDE Browser Recordings

**Source:** [https://antigravity.google/docs/ide/browser-recordings](https://antigravity.google/docs/ide/browser-recordings)

The browser subagent may record its actions whenever it interacts with a web page.

Recordings:

- Appear below the relevant browser step
- Are saved as reviewable artifacts
- Replay the sequence of browser actions
- Help verify what the agent clicked, typed, or changed

## 63. Browser Allowlist and Denylist

**Source:** [https://antigravity.google/docs/ide/allowlist-denylist](https://antigravity.google/docs/ide/allowlist-denylist)

Browser security uses two layers:

1. **Denylist:** Blocks known dangerous or malicious URLs.
2. **Allowlist:** Contains URLs explicitly trusted by the user.

The allowlist initially contains only [localhost](http://localhost). When the agent encounters another domain, Antigravity asks whether to always allow it.

The denylist takes precedence. A denylisted URL cannot be enabled through the local allowlist. If the denylist service is unavailable, access is denied by default.

## 64. Separate Chrome Profile

**Source:** [https://antigravity.google/docs/ide/separate-chrome-profile](https://antigravity.google/docs/ide/separate-chrome-profile)

The browser agent uses an isolated Chrome profile.

- It does not share cookies or login information with the default Chrome profile.
- Accounts added to the isolated profile remain available in future sessions.
- It may appear as a separate application or dock icon.
- The profile’s storage location can be changed in browser settings.

This protects normal browsing data while allowing persistent agent-specific sessions.

## 65. IDE Agent Skills

**Source:** [https://antigravity.google/docs/ide/skills](https://antigravity.google/docs/ide/skills)

Skills are reusable instruction packages centered around `SKILL.md`.

### Locations

- Project: `.agents/skills/<skill-name>/`
- Global: `~/.gemini/antigravity/skills/<skill-name>/`

Each skill requires a description in YAML frontmatter:

```markdown
---
name: code-review
description: Reviews code for bugs, security issues, and style problems.
---
```

Skills can also contain:

- Helper scripts
- Examples
- Templates
- Reference resources

The agent first sees the skill’s name and description, then loads its complete instructions when relevant.

## 66. IDE Rules

**Source:** [https://antigravity.google/docs/ide/rules](https://antigravity.google/docs/ide/rules)

Rules are Markdown files containing persistent constraints or instructions.

### Locations

- Global: `~/.gemini/GEMINI.md`
- Project: `.agents/rules/`

Activation options include:

- Manual mention
- Always on
- Model decision
- File-glob match

Each rule file is limited to 12,000 characters and can reference another file using `@filename`.

## 67. IDE Workflows

**Source:** [https://antigravity.google/docs/ide/workflows](https://antigravity.google/docs/ide/workflows)

Workflows define repeatable sequences for tasks such as deployment, testing, or responding to pull-request comments.

Run one using:

```
/workflow-name
```

Workflows:

- Can be global or project-specific
- Can invoke other workflows
- Are stored as Markdown
- Include a title, description, and ordered instructions
- Are limited to 12,000 characters
- Can be generated by the agent from conversation history

## 68. IDE Plugins

**Source:** [https://antigravity.google/docs/ide/plugins](https://antigravity.google/docs/ide/plugins)

Plugins combine skills, rules, MCP servers, and hooks.

```
plugins/<plugin-name>/
├── plugin.json
├── mcp_config.json
├── hooks.json
├── skills/
└── rules/
```

### Locations

- Project: `.agents/plugins/`
- Global: `~/.gemini/config/plugins/`

Google-provided plugins are available from the **Customizations** page.

## 69. IDE Hooks

**Source:** [https://antigravity.google/docs/ide/hooks](https://antigravity.google/docs/ide/hooks)

Hooks run custom shell commands at agent lifecycle events.

### Events

- `PreToolUse`
- `PostToolUse`
- `PreInvocation`
- `PostInvocation`
- `Stop`

Hooks are configured in:

- Project: `.agents/hooks.json`
- Global: `~/.gemini/config/hooks.json`

They can:

- Run linters and diagnostics
- Allow, deny, or request approval for tools
- Inject messages or tool calls
- Force continuation or termination
- Match specific tools using regular expressions

Hook input and output use JSON through standard input and standard output.

## 70. IDE Settings and Strict Mode

**Source:** [https://antigravity.google/docs/ide/settings](https://antigravity.google/docs/ide/settings)

### Command execution

- **Request Review:** Ask before running terminal commands.
- **Always Proceed:** Execute automatically unless denied.

### Strict mode

Strict mode enforces:

- Terminal approval for every command
- Browser-JavaScript approval
- Artifact-plan approval
- `.gitignore` restrictions
- No access outside the project
- Browser allowlist and denylist
- Automatic terminal sandboxing
- No sandbox network access

Sandboxing uses:

- macOS: `sandbox-exec`
- Linux: `nsjail`

When sandboxing is enabled, commands can write only inside authorized project and system locations. Network access is controlled separately.

---

# 07 · Migration, Enterprise, Plans & FAQ · Entries 71–74

## 71. Firebase Studio Migration

**Source:** [https://antigravity.google/docs/firebase-studio-migration](https://antigravity.google/docs/firebase-studio-migration)

### Requirements

- Antigravity IDE
- Node.js 20 or newer
- Firebase CLI 15.10.0 or newer

### Migration process

1. Export the Firebase Studio project using **Move now** or **Firebase Studio: Zip & Download**.
2. Extract the project locally.
3. Open the folder in Antigravity.
4. Let the agent transform and configure the project, or use the Firebase CLI for a manual migration.
5. Start the app through **Run and Debug**.
6. Deploy through the agent or `firebase deploy`.

The migration command is primarily optimized for Next.js, Flutter, and Angular workspaces. Other project types may require manual adjustments.

## 72. Enterprise Setup

**Source:** [https://antigravity.google/docs/enterprise](https://antigravity.google/docs/enterprise)

Enterprise integration is supported by:

- Antigravity 2.0
- Antigravity CLI

Antigravity IDE is not supported for enterprise configurations.

The Gemini Enterprise Agent Platform integration provides:

- Models hosted in the organization’s Google Cloud project
- Google Cloud Terms of Service
- Private-networking support
- Data-residency controls
- Consumption-based billing

### Setup requirements

1. Select or create a Google Cloud project.
2. Enable billing.
3. Enable `aiplatform.googleapis.com`.
4. Grant users the Agent Platform User role:

```
roles/aiplatform.user
```

Additional setup roles may include:

- Project Creator: `roles/resourcemanager.projectCreator`
- Service Usage Admin: `roles/serviceusage.serviceUsageAdmin`

Available endpoints include:

- Global
- Multi-region United States
- Multi-region European Union

Image generation is currently unavailable on the US and EU multi-region endpoints.

## 73. Plans and Quotas

**Source:** [https://antigravity.google/docs/plans](https://antigravity.google/docs/plans)

All plans receive:

- Gemini 3.1 Pro and Gemini 3.5 Flash access
- Unlimited Tab completions
- Scheduled Tasks
- Antigravity CLI
- Other core product features

### Google AI Ultra

- Highest quota
- Quota refreshes every five hours
- Highest weekly limits
- Access to supported third-party models

### Google AI Pro

- High quota
- Five-hour refreshes until the weekly limit is reached
- Higher weekly limits than the standard plan

### Standard accounts

- Weekly quota refresh
- Weekly usage limits

Task complexity affects consumption. Longer and more complicated agent work consumes more quota than short tasks.

### AI-credit overages

Pro and Ultra users may use purchased or promotional AI credits after the included quota is exhausted.

Options:

- **Never:** Wait for the included quota to refresh.
- **Always:** Use credits until the included quota refreshes.

Bring-your-own API keys and custom endpoints are not supported for increasing limits.

## 74. Frequently Asked Questions

**Source:** [https://antigravity.google/docs/faq](https://antigravity.google/docs/faq)

### Authentication

Antigravity is available to personal Google accounts in approved regions. If a Workspace account fails, Google recommends trying an `@gmail.com` account.

### Age requirement

Users must be at least 18. Eligible users can complete Google Account age verification.

### Availability

Antigravity is available across approved regions in the Americas, Europe, Africa, Asia, Oceania, and Antarctica. Eligibility is determined partly by the country associated with the Google account.

### Data collection

Data collection can be disabled through the Antigravity Settings panel.

### Third-party clients

Using Antigravity credentials through unauthorized third-party software violates the Terms of Service and may result in account suspension. Google recommends Vertex AI or AI Studio API keys for external agents.

### Worktrees

Antigravity 2.0 supports Git worktrees.

### Computer sleep

If an agent is actively running, Antigravity prevents the computer from going to sleep.