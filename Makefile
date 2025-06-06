

notebooks = $(shell find notebooks -name "*.ipynb")

.PHONY: fmt
fmt:
	ruff format
	ruff check --fix --extend-select I
	python -m jupyter nbconvert --clear-output --inplace $(notebooks)

.PHONY: clear
clear:
	python -m jupyter nbconvert --clear-output --inplace $(notebooks)

# Render all notebooks
.PHONY: render
render: fmt clear
	python -m jupyter nbconvert --to notebook --execute --inplace $(notebooks)


