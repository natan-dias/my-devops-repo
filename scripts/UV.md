# uv Environment

This directory uses [uv](https://docs.astral.sh/uv/) for Python dependency management.

## Files

**`pyproject.toml`** — declares the project metadata and dependencies. Dev dependencies (pytest, coverage, etc.) live under `[project.optional-dependencies].dev` and are installed with the `--extra dev` flag.

**`uv.lock`** — auto-generated lockfile that pins the exact version of every dependency (including transitive ones). Do not edit it manually; it is updated automatically when you run `uv lock`. Commit it to version control to ensure reproducible installs across machines and CI.

## Setup

```bash
# Install dependencies (run from scripts/)
uv sync --extra dev
```

This creates a `.venv` directory and installs all dev dependencies into it.

## Running tests

```bash
# All tests with coverage
uv run python -m pytest --cov . tests/

# Single test file
uv run python -m pytest tests/test_build_and_push.py

# Single test
uv run python -m pytest tests/test_build_and_push.py::test_build_image
```

`uv run` automatically uses the managed `.venv` — no need to activate it manually.
