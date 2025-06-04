
.PHONY: fmt
fmt:
	ruff format
	ruff check --fix --extend-select I
	python -m jupyter nbconvert --clear-output --inplace $(shell find . -name "*.ipynb")

.PHONY: run
run: fmt
	python -m jupyter nbconvert --to notebook --execute --inplace 01_replay.ipynb


02_prototype.html: 02_prototype.ipynb
	python -m jupyter nbconvert --to html --execute 02_prototype.ipynb