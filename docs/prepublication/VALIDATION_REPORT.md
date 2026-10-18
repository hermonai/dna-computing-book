# Validation report

Date: 18 October 2026. Machine: macOS (Darwin 27.0.0).

## Tools
- Python 3.13.6 (pyenv), PyTorch 2.10.0, NumPy 2.4.3, pytest 9.0.2
- XeTeX 3.141592653-2.6-0.999998 (TeX Live 2026), latexmk 4.88, BibTeX 0.99e
- Poppler pdftoppm 26.07.0, rsvg-convert 2.61.1

## Commands and results
| Command | Result |
|---|---|
| `make check PYTHON=~/.pyenv/shims/python3` | computed assets verified; **1303 passed, 2 skipped** |
| `make pdf PYTHON=…` (from a clean `build/book`) | success; **442 pages**; `warning-audit.json` empty; no BibTeX warnings |
| `make archive-check PYTHON=…` | `verified_entries: 1175`, `unavailable_local_only_pdfs: 0` |
| `make review PYTHON=…` | 442 pages rendered at 90 dpi; 111 colour and 111 greyscale contact sheets |

The original base commit `5987341` fails `make pdf` from a clean build directory
(undefined chapter-scoped figure references; see FINDINGS #1). This revision
builds from clean.

## Identities
- PDF `output/pdf/dna-computing.pdf`: SHA-256 `0775970c7aebf756b4d70e03828a79f1655b3b23804de9d2dce385f54da31987`
- Build-record source set: 637 files; digest of the sorted
  `path:sha256` list `c7d901d2f77b7f821e727165d8a6756dd2b0daba113aa0be481b73be709394e9`
- Bibliography: 123 cited works from `book/backmatter/references.bib`

## Inspection coverage (actual)
- Every new or redrawn plate (21) rendered standalone at 100–130 dpi and
  re-rendered after each fix; natural widths measured (print scale 0.90–1.15).
- Built-PDF pages viewed at 60–80 dpi: title page; contents; Preface; How to
  use (pp. 5–9 of front matter); Part I opener; Chapter 1 pp. 2–5; Chapter 5
  pp. 70, 73; Chapter 8 p. 104; Chapter 21 pp. 262–264; Chapter 22 p. 268;
  Chapter 31 pp. 378–381; Chapter 32 pp. 394–395; Epilogue pp. 396–399;
  Appendices A–C pp. 400–409; Glossary pp. 410–413; Bibliography first page.
- One greyscale contact sheet checked. All other pages were rendered but not
  individually inspected; full-resolution inspection remains an open gate.

## Not covered
- No wet-lab validation; no independent specialist or reader review.
- Retained older plates were not re-reviewed at full resolution.
