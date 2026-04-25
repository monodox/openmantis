# Changelog

All notable changes to OpenMantis will be documented here.

## Unreleased

### Added
- Converted project to monorepo with `packages/node` and `packages/python`.
- Python SDK mirroring Node.js functionality (cache, router, tokenizer, runtimes, CLI).
- `requirements.txt` and `requirements-dev.txt` for Python.
- Separate CI jobs for Node.js and Python tests.
- PyPI publish workflow (`.github/workflows/pypi-publish.yml`).
- Updated repo URL to `https://github.com/monodox/openmantis`.

### Changed
- Moved Node.js source from root `src/` to `packages/node/src/`.
- Moved Node.js tests from root `test/` to `packages/node/test/`.
- Root `package.json` now uses npm workspaces.
- Updated CI and npm-publish workflows for monorepo paths.
- Updated `.gitignore` with Python and IDE entries.

### Removed
- `CONTRIBUTTING.md` typo alias file.
- Empty leftover `src/`, `test/`, `bin/` directories.

## 0.1.0

### Added
- Working CLI entrypoint and OpenMantis library entrypoint.
- Disk-backed cache, request routing, token estimation, and local runtime adapters.
- Deterministic tests for core helpers and runtime request shapes.
- Contributor-facing documentation and CI scaffolding.
