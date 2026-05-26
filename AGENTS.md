# AGENTS.md

Tooling instructions for AI assistants.
Humans may ignore this file.

## Companion Files

Keep command sections equivalent across all:

- AGENTS.md (must be in root)
- CLAUDE.md (root or .claude/)
- .github/copilot-instructions.md

## Purpose

Canonical, cross-platform workflow for this repository.
Python is managed by uv; uv downloads Python if needed.

## Requirements

- Use **uv only**
- Do **not** suggest pip or venv workflows
- Commands must be cross-platform

## Setup

```shell
uv self update
uv python pin 3.14
uv sync --extra dev --extra docs --upgrade
```

## Quality

```shell
uv run ruff format .
uv run ruff check .
uv run pyright .
uv run pytest
```

## Docs

```shell
uv run mkdocs serve
uv run mkdocs build
```

## Git

```shell
git add .
git commit -m "Describe your changes"
git push -u origin main
```
