# OpenMantis

OpenMantis is an open-source tool and SDK that lets developers run large AI models on low-spec devices by acting as a smart optimization layer between your app and local model runtimes like Ollama and Foundry Local.

It focuses on reducing memory and storage usage through caching, prompt tokenization, and context directory indexing.

## Packages

This is a monorepo containing two SDK packages:

| Package | Path | Registry |
|---------|------|----------|
| [@openmantis/openmantis](packages/node) | `packages/node` | GitHub Packages (npm) |
| [openmantis](packages/python) | `packages/python` | PyPI |

## Features

- Runtime adapters for local model servers (Ollama, Foundry Local)
- Caching layer to avoid recomputation across sessions
- Tokenization and prompt budgeting utilities
- Context directory indexing to reuse relevant information efficiently

## Getting Started

### Node.js

```bash
npm install
npm run test:node
node packages/node/bin/openmantis.js run "hello world"
```

### Python

```bash
cd packages/python
pip install -r requirements.txt
pip install -e ".[dev]"
pytest
```

## Configuration

Copy `.env.example` to `.env.local` and update the values.

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENMANTIS_CACHE_DIR` | Cache directory | `.openmantis/cache` |
| `OPENMANTIS_RUNTIME_OLLAMA_URL` | Ollama endpoint | `http://localhost:11434` |
| `OPENMANTIS_RUNTIME_FOUNDRY_URL` | Foundry endpoint | `http://localhost:3000` |
| `OPENMANTIS_MAX_CONTEXT_TOKENS` | Max context tokens | `4096` |
| `OPENMANTIS_MAX_OUTPUT_TOKENS` | Max output tokens | `1024` |

## Development

```bash
# Run all tests
npm run test:all

# Node.js tests only
npm run test:node

# Python tests only
npm run test:python
```

## Repository Structure

```
packages/
  node/            Node.js SDK (@openmantis/openmantis)
    bin/            CLI entrypoint
    src/cli/        Command handlers
    src/core/       Cache, router, tokenizer, memory, directory
    src/runtimes/   Ollama and Foundry adapters
    src/platform/   Path, process, and hardware helpers
    test/           Node.js tests
  python/          Python SDK (openmantis)
    src/openmantis/ Package source
    tests/          Python tests
docs/              Architecture and runtime docs
skills/            Agent runbooks
```

## Releasing

### Node.js (npm)

1. Bump the version in `packages/node/package.json`.
2. Run `npm run test:node` and make sure the suite passes.
3. Create a GitHub release or tag (e.g. `v0.1.1`).
4. The workflow `.github/workflows/npm-publish.yml` publishes to GitHub Packages.

### Python (PyPI)

1. Bump the version in `packages/python/pyproject.toml`.
2. Run `npm run test:python` and make sure the suite passes.
3. Create a GitHub release or tag.
4. The workflow `.github/workflows/pypi-publish.yml` publishes to PyPI.

## Security

See [`SECURITY.md`](SECURITY.md) for reporting vulnerabilities.

## License

MIT (see [`LICENSE`](LICENSE)).
