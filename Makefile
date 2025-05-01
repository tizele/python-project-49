install: #install package
	uv sync

brain-games: #start
	uv run brain-games

build: #assembly
	uv build

package-install:
	uv tool install dist/*.whl

lint: #code check
	uv run ruff check brain_games
