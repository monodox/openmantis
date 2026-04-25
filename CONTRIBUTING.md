# Contributing

Thank you for contributing to OpenMantis!

## How to Contribute

1. Open or link an issue before starting larger work.
2. Fork the repository or create a branch in the main repo.
3. Make the smallest change that solves the problem.
4. Add or update tests when behavior changes.
5. Open a pull request and describe the user-facing impact.

## Development Notes

- This is a monorepo with two packages:
  - `packages/node` — Node.js SDK
  - `packages/python` — Python SDK
- The Node.js package is organized into:
  - `src/cli` (command-line interface)
  - `src/core` (core utilities like caching, routing, tokenization)
  - `src/runtimes` (adapters for local runtimes like Ollama / Foundry Local)
  - `src/platform` (platform-specific helpers)
- The Python package mirrors the same module layout under `src/openmantis/`.
- Keep public APIs consistent and prefer small, focused changes.
- Avoid adding dependencies unless they materially reduce complexity or improve correctness.
- Prefer deterministic tests that do not require a live runtime unless explicitly marked as integration coverage.

## Testing

Run all tests before opening a PR:

```bash
npm run test:all
```

Or run them individually:

```bash
npm run test:node
npm run test:python
```

If you add an integration test that depends on a local runtime, make it opt-in and keep the default suite offline.

## Code Style

### Node.js
- Follow the existing CommonJS and single-quote style used in the repository.

### Python
- Follow PEP 8 conventions with single quotes.

Keep modules cohesive and avoid broad refactors in feature PRs. Update docs when you change behavior that users will see.

## Code of Conduct

By participating, you agree to follow the `CODE_OF_CONDUCT.md`.
