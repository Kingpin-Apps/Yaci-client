# yaci-client development tasks. Run `just` to list them.

pythons := "3.11 3.12 3.13 3.14 3.15"

default:
    @just --list

# Install the project and all development groups
sync:
    uv sync --all-groups

# Run the tests on the default Python
test *args:
    uv run pytest {{args}}

# Run the tests on every supported Python, each in its own environment
test-all *args:
    #!/usr/bin/env bash
    set -uo pipefail
    failed=()
    for py in {{pythons}}; do
        echo "==> Python $py"
        UV_PROJECT_ENVIRONMENT=.venvs/py$py uv run --python "$py" pytest -q {{args}} || failed+=("$py")
    done
    if [ ${#failed[@]} -gt 0 ]; then echo "Failed on: ${failed[*]}"; exit 1; fi

# Run the tests against the oldest dependency versions allowed, on the oldest and newest Python
test-lowest *args:
    #!/usr/bin/env bash
    set -uo pipefail
    failed=()
    for py in 3.11 3.15; do
        echo "==> Python $py, lowest dependencies"
        UV_PROJECT_ENVIRONMENT=.venvs/lowest-py$py uv run --resolution lowest-direct --no-default-groups --group test --python "$py" pytest -q {{args}} || failed+=("$py")
    done
    if [ ${#failed[@]} -gt 0 ]; then echo "Failed on: ${failed[*]}"; exit 1; fi

# Run the tests with a coverage report
cov:
    uv run pytest --cov --cov-report=term-missing --cov-report=html

# Check linting and formatting
lint:
    uv run ruff check .
    uv run ruff format --check .

# Fix lint findings and format the code
fmt:
    uv run ruff check --fix .
    uv run ruff format .

# Type-check the package and tests
typecheck:
    uv run ty check

# Lint, type-check and test
check: lint typecheck test

# Regenerate yaci_client from the OpenAPI spec in yaci_api.json, keeping __init__.py and py.typed
regenerate:
    #!/usr/bin/env bash
    set -euo pipefail
    keep=$(mktemp -d)
    trap 'rm -rf "$keep"' EXIT
    cp yaci_client/__init__.py yaci_client/py.typed "$keep"/
    uv run --group generate openapi-python-client generate --path yaci_api.json --config generator-config.yaml --meta none --output-path yaci_client --overwrite
    cp "$keep"/__init__.py "$keep"/py.typed yaci_client/

# Check yaci_client matches what the spec generates
check-generated: regenerate
    git diff --exit-code -- yaci_client

# Build the sdist and wheel into dist/
build:
    rm -rf dist
    uv build

# Update the changelog from commits
changelog:
    uv run cz changelog

# Bump the version and changelog from commits, and tag
bump:
    uv run cz bump --yes </dev/null

# Remove build, test and cache artifacts
clean:
    rm -rf dist .venvs .pytest_cache .ruff_cache .coverage htmlcov
    find . -name __pycache__ -type d -prune -not -path "./.venv/*" -exec rm -rf {} +
