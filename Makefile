PYTHON ?= python3
export OMP_NUM_THREADS := 1
export PATH := /Library/TeX/texbin:/opt/homebrew/bin:/usr/local/bin:$(PATH)

.DEFAULT_GOAL := pdf
.PHONY: pdf prepare check test legacy-test archive-check review help

pdf:
	$(PYTHON) scripts/build_book.py

prepare:
	$(PYTHON) scripts/build_book.py --prepare-only

check: prepare
	$(PYTHON) scripts/build_book.py --check-assets
	$(PYTHON) -m pytest -q -o addopts=''

test:
	$(PYTHON) -m pytest -q -o addopts=''

legacy-test:
	cd archive/legacy/dna-computing-book && GIT_DIR=$(CURDIR)/.git GIT_WORK_TREE=$(CURDIR)/archive/legacy/dna-computing-book $(PYTHON) -m pytest -q -o addopts=''

archive-check:
	$(PYTHON) scripts/verify_archive.py

review:
	$(PYTHON) scripts/review_pdf.py

help:
	@echo "make pdf          Build the full 32-chapter manuscript"
	@echo "make check        Verify generated assets and current numerical/source tests"
	@echo "make legacy-test  Run the unchanged historical regression suite"
	@echo "make archive-check  Verify preserved source and PDF bytes"
	@echo "make review       Render all pages and color/grayscale contact sheets"
