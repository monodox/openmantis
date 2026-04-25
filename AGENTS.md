# AGENTS.md

This file provides coding-agent context for working on OpenMantis.

## Project overview

OpenMantis is a monorepo (`https://github.com/monodox/openmantis`) containing Node.js and Python SDKs that act as an optimization layer between an app and local model runtimes (Ollama, Foundry Local) using caching, context directory indexing, and prompt tokenization.

## Setup commands

- Install deps (Node): `npm install`
- Install deps (Python): `cd packages/python && pip install -e ".[dev]"`
- Run all tests: `npm run test:all`
- Run Node tests: `npm run test:node`
- Run Python tests: `npm run test:python`

## Code style

### Node.js (packages/node)
- JavaScript, CommonJS modules.
- Single quotes, no semicolons, tabs for indentation.
- Prefer small functional helpers over large imperative blocks.
- Modules: `src/cli`, `src/core`, `src/runtimes`, `src/platform`.

### Python (packages/python)
- Python 3.10+.
- Single quotes, PEP 8 conventions.
- Modules: `core`, `runtimes`, `platform`.

## Testing instructions

- Node tests: `packages/node/test/` — uses Node.js built-in test runner.
- Python tests: `packages/python/tests/` — uses pytest.
- Keep tests deterministic. Mock runtime adapters, avoid network calls.

## Security considerations

- Never execute untrusted code returned by a model.
- Treat runtime responses and user prompts as untrusted input.
- Do not log secrets (API keys, auth tokens, sensitive prompt contents).

## Repo locations (agent quick reference)

- Root package.json: monorepo orchestrator (npm workspaces, convenience scripts)
- Node CLI entrypoint: `packages/node/bin/openmantis.js`
- Node runtime adapters: `packages/node/src/runtimes/`
- Node shared core: `packages/node/src/core/`
- Node tests: `packages/node/test/`
- Python CLI entrypoint: `packages/python/src/openmantis/cli.py`
- Python runtime adapters: `packages/python/src/openmantis/runtimes/`
- Python shared core: `packages/python/src/openmantis/core/`
- Python tests: `packages/python/tests/`
- Python requirements: `packages/python/requirements.txt`
- Skills (agent runbooks): `skills/`
- Docs: `docs/`
