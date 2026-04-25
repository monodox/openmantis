---
title: Architecture
---

# Architecture

OpenMantis is built around a small request pipeline:

1. The CLI or library entrypoint creates an OpenMantis instance.
2. The router normalizes the request and checks token budget constraints.
3. The router generates a cache key from the runtime, model, messages, and output budget.
4. If a cached response exists, it is returned immediately.
5. Otherwise, the selected runtime adapter sends the request to a local model server.
6. The response is stored in the disk-backed cache and returned to the caller.

## Monorepo Layout

- `packages/node/` — Node.js SDK (`@openmantis/openmantis`)
- `packages/python/` — Python SDK (`openmantis`)

Both packages share the same architecture and module structure.

## Core Modules (Node.js)

- [packages/node/src/index.js](../packages/node/src/index.js) wires together the cache, memory store, router, runtimes, and platform helpers.
- [packages/node/src/core/cache.js](../packages/node/src/core/cache.js) stores cached responses in JSON on disk.
- [packages/node/src/core/router.js](../packages/node/src/core/router.js) selects the runtime, enforces prompt budgets, and handles cache hits.
- [packages/node/src/core/tokenizer.js](../packages/node/src/core/tokenizer.js) estimates token usage for messages and other values.
- [packages/node/src/core/directory.js](../packages/node/src/core/directory.js) indexes files for context reuse.
- [packages/node/src/core/memory.js](../packages/node/src/core/memory.js) persists lightweight keyed memory.
- [packages/node/src/runtimes/ollama.js](../packages/node/src/runtimes/ollama.js) and [packages/node/src/runtimes/foundry.js](../packages/node/src/runtimes/foundry.js) adapt local runtime APIs into a common `chat()` contract.

## Core Modules (Python)

- [packages/python/src/openmantis/__init__.py](../packages/python/src/openmantis/__init__.py) wires together the cache, memory store, router, runtimes, and platform helpers.
- [packages/python/src/openmantis/core/cache.py](../packages/python/src/openmantis/core/cache.py) stores cached responses in JSON on disk.
- [packages/python/src/openmantis/core/router.py](../packages/python/src/openmantis/core/router.py) selects the runtime, enforces prompt budgets, and handles cache hits.
- [packages/python/src/openmantis/core/tokenizer.py](../packages/python/src/openmantis/core/tokenizer.py) estimates token usage.
- [packages/python/src/openmantis/core/directory.py](../packages/python/src/openmantis/core/directory.py) indexes files for context reuse.
- [packages/python/src/openmantis/core/memory.py](../packages/python/src/openmantis/core/memory.py) persists lightweight keyed memory.
- [packages/python/src/openmantis/runtimes/](../packages/python/src/openmantis/runtimes/) adapts local runtime APIs.

## Extension Points

- Add a new runtime by implementing the same `chat(request)` shape and exporting it from the runtimes index.
- Add new routing behavior in the router so the CLI and library entrypoints stay thin.
- Keep cache and memory storage deterministic so tests can run without network access.

## Configuration

- `OPENMANTIS_CACHE_DIR` controls the on-disk cache location.
- `OPENMANTIS_RUNTIME_OLLAMA_URL` controls the Ollama endpoint.
- `OPENMANTIS_RUNTIME_FOUNDRY_URL` controls the Foundry Local endpoint.
- `OPENMANTIS_MAX_CONTEXT_TOKENS` and `OPENMANTIS_MAX_OUTPUT_TOKENS` bound request size.
