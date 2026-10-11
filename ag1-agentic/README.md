# ag1-agentic/

Colossal scanner fixture (inert). **All values are fake.** Every host is `example.invalid`, which never resolves, except the safe twin of `endpoint-override`,
which names the vendor's own public endpoint and is never contacted; every command is inert;
nothing here is a credential. Do not copy anything from here into a real repository.

Agent-surface fixtures for Colossal's repository scan (AG1 + AG2a). Each `<sample>/bad/` folder holds the files an
agent reads, runs or obeys with exactly one unsafe pattern; each `<sample>/clean/` folder holds its safe twin.
`filler/` holds 450 small files so a scan of this repository passes the 400-file limit.

Some samples hold invisible Unicode characters on purpose (`hidden-unicode/bad/CLAUDE.md`).

| Sample | Rule | Severity |
|---|---|---|
| `hidden-unicode` | `agent.hidden-unicode` | critical |
| `instruction-remote-exec` | `agent.instruction-remote-exec` | high |
| `instruction-disable-safety` | `agent.instruction-disable-safety` | high |
| `instruction-secret-read` | `agent.instruction-secret-read` | high |
| `external-import` | `agent.external-import` | medium |
| `repo-hook` | `agent.repo-hook` | critical |
| `endpoint-override` | `agent.endpoint-override` | high |
| `permission-bypass` | `agent.permission-bypass` | high |
| `mcp-auto-enable` | `agent.mcp-auto-enable` | medium |
| `marketplace-source` | `agent.marketplace-source` | medium |
| `editor-folder-open-task` | `editor.folder-open-task` | high |
| `editor-agent-auto-approve` | `editor.agent-auto-approve` | high |
| `skill-remote-prerequisite` | `skill.remote-prerequisite` | high |
| `skill-unrestricted-tools` | `skill.unrestricted-tools` | medium |
| `skill-script-network` | `skill.script-network` | medium |
| `ci-agent-untrusted-trigger` | `ci.agent-untrusted-trigger` | critical |
| `ci-agent-bypass-flags` | `ci.agent-bypass-flags` | high |
| `mcp-gemini-settings` | `MCP-UNPINNED-PACKAGE` | medium |
| `mcp-codex-config` | `MCP-UNPINNED-PACKAGE` | medium |
