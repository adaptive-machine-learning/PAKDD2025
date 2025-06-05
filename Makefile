
.PHONY: fmt
fmt:
	ruff format
	ruff check --fix --extend-select I
	python -m jupyter nbconvert --clear-output --inplace $(shell find . -name "*.ipynb")

.PHONY: run
run: fmt
	python -m jupyter nbconvert --to notebook --execute --inplace 01_replay.ipynb


html/%.html: %.ipynb
	python -m jupyter nbconvert --to html --output-dir=html --execute $<

all: \
	html/00_evaluation.html \
	html/01_replay.html \
	html/02_regularization.html \
	html/03_prototype.html
