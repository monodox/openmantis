# @monodox/openmantis

A small Node.js SDK that acts as an optimization layer between your app and local model runtimes like Ollama and Foundry Local.

## Install

```bash
npm install @monodox/openmantis
```

## Quick Start

```js
const { createOpenMantis } = require('@monodox/openmantis')

const client = createOpenMantis()
const response = await client.chat({
  messages: [{ role: 'user', content: 'hello' }],
})

console.log(response.content)
```

## CLI

```bash
npx @monodox/openmantis run "hello world"
```

## Features

- Runtime adapters for Ollama and Foundry Local
- Disk-backed caching to skip repeated calls
- Token estimation and prompt budgeting
- Context directory indexing
- Lightweight in-memory key-value store

## Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENMANTIS_CACHE_DIR` | Cache directory | `.openmantis/cache` |
| `OPENMANTIS_RUNTIME_OLLAMA_URL` | Ollama endpoint | `http://localhost:11434` |
| `OPENMANTIS_RUNTIME_FOUNDRY_URL` | Foundry endpoint | `http://localhost:3000` |
| `OPENMANTIS_MAX_CONTEXT_TOKENS` | Max context tokens | `4096` |
| `OPENMANTIS_MAX_OUTPUT_TOKENS` | Max output tokens | `1024` |

## API

```js
const {
  createOpenMantis,
  createCache,
  createMemoryStore,
  createRouter,
  createOllamaRuntime,
  createFoundryRuntime,
  indexDirectory,
} = require('@monodox/openmantis')
```

## License

MIT
