# colossal-scanner-fixtures

Intentionally insecure test fixtures for Colossal scanner conformance. **All values are fake.**

Every file here is deliberately unsafe so that a scanner has something to find. Nothing in this repository is a real
service, credential or key: every secret-looking value (the password in `Dockerfile.prod`, the signing key in
`docker-compose.override.yml`) is invented, a random string that belongs to nothing and opens nothing, and every host
name is a placeholder. Do not copy anything from here into real infrastructure.

Colossal scans this repository after each deploy and checks that the findings it reports match what is written into
the files.

## m1-docker/

Container-file fixtures for Docker code scanning:

| File | Expected container findings |
|---|---|
| `Dockerfile.prod` | 11 |
| `docker/Containerfile` | 2 |
| `docker-compose.override.yml` | 7 |
| `Dockerfile` | 0 (the clean control) |

## ag1-agentic/

Agent-surface fixtures for the repository scan (AG1 + AG2a): 19 samples, each a `bad/` folder holding one unsafe pattern and a `clean/` twin, plus 450 filler files. Every host is `example.invalid` except the safe twin of `endpoint-override`; every command is inert. See the README inside the folder.

## ag3-packages/

Package-reality fixtures for the repository scan (AG3): 5 samples naming a package that does not exist (each with a `clean/` twin) and 2 that must give no finding (a private scope and an unconfigured scope). Every missing name is `colossal-fixture-nonexistent-...` and must never be installed. See the README inside the folder.
