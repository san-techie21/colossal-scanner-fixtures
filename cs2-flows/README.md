# cs2-flows

Python and agent cases for the ColossalX standard repository scan (agent-aware data flow and the newer Python
vulnerability families). **All code is synthetic and is never run.** Hosts are `example.com` or `example.invalid`,
there are no credentials, and nothing here talks to a real service.

80 cases in four groups. Each case is a few lines in its own folder: either a vulnerable pattern or its safe twin
(the same code with the fix), so a scanner is checked for what it finds and for what it correctly leaves alone.

| Group | Cases | What it covers |
|---|---|---|
| `agent_dataflow/` | 27 | model output, tool and MCP tool arguments and retrieved text used as untrusted input (command, SQL, code, file, markup, URL), untrusted text in system instructions, remote model code |
| `web_classes/` | 20 | open redirect, XXE, NoSQL injection, mass assignment, template injection from input, reflected and template XSS, upload handling, XPath, passwords stored as typed |
| `py_injection/` | 21 | command, code, SQL, path, SSRF and template injection, deserialisation, Tornado handlers |
| `py_config/` | 12 | TLS checks, password hashing, debug mode, session cookie flags, randomness for tokens, unsafe YAML |

Expected result of a standard scan: every vulnerable case is reported and every safe twin is clean. The CSRF cases are
found by a deep scan only and are under `cs5a-authz/`.

A standard scan reads at most 400 files and `ag1-agentic/filler/` already uses them up, so scan this folder with the
file limit raised (a deep scan reads 2,000), as the proof script does.
