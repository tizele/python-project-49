install: #install package
	uv sync

brain-games: #start
	uv run brain-games

build: #assembly
	uv build

package-install:
	uv tool install dist/*.whl


