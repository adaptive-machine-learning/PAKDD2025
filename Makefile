
.PHONY: fmt
fmt:
	ruff format
	jupyter nbconvert --clear-output --inplace $(shell find . -name "*.ipynb")