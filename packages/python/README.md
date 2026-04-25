# OpenMantis Python SDK

Python SDK for OpenMantis — a local-model orchestration layer for caching, routing, and prompt budgeting.

## Installation

```bash
pip install openmantis
```

For development:

```bash
pip install -e ".[dev]"
```

## Quick Start

```python
from openmantis import create_openmantis

client = create_openmantis()
response = client.chat(messages=[{'role': 'user', 'content': 'hello'}])
print(response['content'])
```

## Features

- Runtime adapters for local model servers (Ollama, Foundry Local)
- Disk-backed caching to avoid recomputation
- Token estimation and prompt budgeting
- Context directory indexing

## Configuration

Set environment variables to configure OpenMantis:

- `OPENMANTIS_CACHE_DIR` — cache directory (default: `.openmantis/cache`)
- `OPENMANTIS_RUNTIME_OLLAMA_URL` — Ollama endpoint (default: `http://localhost:11434`)
- `OPENMANTIS_RUNTIME_FOUNDRY_URL` — Foundry endpoint (default: `http://localhost:3000`)
- `OPENMANTIS_MAX_CONTEXT_TOKENS` — max context tokens (default: `4096`)
- `OPENMANTIS_MAX_OUTPUT_TOKENS` — max output tokens (default: `1024`)

## License

MIT
