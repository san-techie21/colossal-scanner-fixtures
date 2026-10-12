# ag3-packages/

Colossal scanner fixture (inert). **Do not install anything named here.** Every package called `colossal-fixture-nonexistent-...` is meant
not to exist: it is the sample for "this package does not exist on its registry, so anyone can register it". If
one ever does exist, someone registered it after this fixture was published; do not install it.

Package reality fixtures for Colossal's repository scan (AG3). Each `<sample>/bad/` folder names a package for
installing in one of the places the scan reads (requirements, an MCP server, an instruction file, a skill, a
Dockerfile); each `<sample>/clean/` folder holds its safe twin. `private-scope/` and `unconfigured-scope/` must give
no finding: a private or scoped package the scan cannot see is reported as "could not check".

| Sample | Rule | Severity |
|---|---|---|
| `nonexistent-requirements` | `package.nonexistent` | high |
| `nonexistent-mcp-npx` | `package.nonexistent` | high |
| `nonexistent-instruction` | `package.nonexistent` | high |
| `nonexistent-skill` | `package.nonexistent` | high |
| `nonexistent-dockerfile` | `package.nonexistent` | high |
| `private-scope` | `none (could not check)` | - |
| `unconfigured-scope` | `none (could not check)` | - |
