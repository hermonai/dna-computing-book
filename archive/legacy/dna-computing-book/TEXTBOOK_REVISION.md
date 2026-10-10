# LaTeX-first textbook revision

This is a new Chapters 1–3 review candidate, not a promotion of Chapter 3 into
the accepted cumulative edition. Chapters 1–2, their accepted build inputs,
and the standalone Chapter 3 review remain unchanged. Independent specialist
review and cumulative acceptance remain open; Chapter 4 onward is planned.

## What changed

The new entry point is [dna-computing-textbook.tex](tex/dna-computing-textbook.tex).
It directly includes the accepted chapter sources and a separately editable
[Chapter 3 manuscript](tex/textbook/ch03.tex). Future revisions are authored
in LaTeX; the build never converts Markdown into prose.

An original worked opening derives work and dependency depth for four
candidates and three dependent tests. Its native TikZ figure distinguishes
twelve operations from three sequential stages, then asks what doubles when
the candidate count doubles. It explicitly excludes a measured chemical
speedup claim. The chapter retains twelve reviewed vector figures, numerical
diagnostics, twelve worked exercises, and its source/evidence ledger.

The shared [textbook standard](TEXTBOOK_STANDARD.md) requires concrete
examples, derivations, executable checks, limitations, and original geometric
illustrations. The general build-from-scratch pedagogy is informed by
Sebastian Raschka's book; prose and illustrations are original.

## Reproduce and review

```sh
make -f textbook.mk textbook-check
make -f textbook.mk textbook
python3 scripts/build_textbook_plan.py --check
python3 -m pytest
python3 scripts/review-textbook-pdf.py output/pdf/dna-computing-textbook.pdf build/textbook/review
```

Use Python 3.10+, pytest, the existing numerical dependencies, XeLaTeX/latexmk,
TeX Gyre Pagella and Heros, TikZ, DejaVu fonts, librsvg and Poppler. The page
review helper additionally needs Pillow. Build output stays under build/ and
output/pdf/; generated PDFs are not new acceptance records.

The source checker verifies 184 prior recorded source hashes and the old
standalone PDF hash, checks the native/vector inputs, and independently checks
the worked opening's arithmetic. The build rejects overfull boxes, missing
glyphs and unresolved references. Every page is rendered; contact-sheet and
full-size figure inspection supplement the automated word-bound audit.

This is author-agent technical/editorial review, not independent scientific
certification. It is a partial editorial revision: accepted Chapters 1–2
are retained, and Chapter 3 combines retained reviewed material with a new
worked opening and native authoring surface.

## Planning without rewriting history

The historical build_deep_plan.py is a frozen accepted input. Its old roadmap
still calls Chapter 3 planned, while the accepted repository had moved to a
standalone review. The new build_textbook_plan.py layers the current review
status on that generator and changes only ROADMAP.md. Tests retain its old
validation behavior and ensure the overlay cannot mark Chapter 3 accepted.
book/book.json still contains only the two accepted chapters.

Next: obtain specialist review of Chapter 3, close cumulative acceptance,
then author Chapter 4 in LaTeX. Do not overwrite any frozen edition to make a
new candidate appear accepted.
