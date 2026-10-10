# Chapter 32 — From molecular computation to genomic computation

Integration candidate using dna-computing-ch32-r01.zip; incoming metadata is
preserved under research/integration/ch32/incoming, not adopted as local evidence.

The closing chapter proves the fiber recoverability criterion, constructs a
sequence/concentration collision, implements strict encodings and computes a
matched factorial comparison. Twenty worked synthesis exercises and six
original vector mechanism/algorithm plates have semantic TXT companions.
This completes the planned chapter spine, not independent publication acceptance.

## Build and verify

Use Python 3.13.6 at /Users/wenyan/.pyenv/versions/3.13.6/bin/python3.

- pytest -q -o addopts='' tests/test_ch32_reference.py
- drafts/ch32/build.py --render
- drafts/ch32/build.py --check
- pytest -q -o addopts='' --junitxml=build/ch32/regression.xml
- scripts/build-convergence.py --through 32 --refresh-assets

Assigned synthetic scores are not trained-model results. Accepted opening
unchanged; cumulative editorial, scientific and reader review remain open.
