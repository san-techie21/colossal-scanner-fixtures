# cs-small1

Scanner fixtures for the ColossalX rule set `2026.10.17-cs-small1` (C and C++ banned functions, CWE-703 and CWE-248
exceptional conditions). **All content here is a test fixture: synthetic code that is deliberately unsafe and is never
compiled or run.** There are no credentials, keys or real hosts anywhere in this folder.

| File | Expected result of a standard scan |
|---|---|
| `src/legacy.c` | critical `c.gets` (CWE-242), high `c.unbounded-copy` (CWE-120), low `c.memcpy-size` |
| `web/app.ts` | low `js.empty-catch` (CWE-703) |
| `jobs/run.py` | medium `py.except-pass`, "Error swallowed around a security check" (CWE-703) |

Colossal scans this folder after a release that changes the rules and checks that the findings above are reported and
that the coverage ledger carries the C memory-safety sentence. AWS key validation is deliberately not fixtured here: no
key-shaped value is ever committed to a public repository.
