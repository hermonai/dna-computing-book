# DNA Computing Chapter 23 package
**Chapter:** 23 — Errors, redundancy and molecular reliability
**Stable ID:** DNAD-23 | **Revision:** r01 | **Status:** review candidate

This chapter turns Chapter 22's abstract/physical gap into an explicit reliability
problem. It distinguishes growth mismatch, spurious nucleation, facet nucleation,
kinetic traps, missing/incorrect components and observation errors; derives simple
finite-size reliability laws; builds repetition/proofreading teaching models; and
separates theoretical scaling from measured DNA-tile results.

Commands:
```sh
python3 drafts/ch23/reference.py > drafts/ch23/results.json
python3 -m pytest -q tests/test_ch23_reference.py
python3 drafts/ch23/build.py
```
