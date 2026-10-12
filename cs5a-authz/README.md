# cs5a-authz

Authorization fixtures for the ColossalX deep scan: missing authentication, missing authorization, object-level access
(IDOR) and CSRF. **All code is synthetic and is never run.** Hosts are `example.com`, there are no credentials.

34 cases as guarded and unguarded twins: each unguarded case has a twin with the control in place (a login or role check,
a filter by the signed-in user, a CSRF token, server-side authentication on an MCP server). Flask, FastAPI, Django,
Django REST framework, MCP servers and agent tools are covered.

Expected result of a deep scan: every unguarded case has an authorization or CSRF finding of its class and every
guarded twin has none of that class. A standard scan reports none of these (the analysis is deep only).

`web_classes/` here holds the CSRF pairs; `authorization/` the rest. A deep scan reads up to 2,000 files, which covers
this repository.
