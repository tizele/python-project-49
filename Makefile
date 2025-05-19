install: #install package
	uv sync

brain-games: #start
	uv run brain-games

build: #assembly
	uv build

package-install:
	uv tool install dist/*.whl

package-force:
	uv tool install --force dist/*.whl

lint: #code check
	uv run ruff check

lint-fix: #code check fix
	uv run ruff check --fix

