# DNA-01 research and review record

Question: what makes a molecular process a computation rather than a metaphor?

Outline: a small route problem; physical encoding/operations/readout; exact set filtering; executable oracle; resource and error boundaries; exercises; the next molecular prerequisites.

Source review on 2026-09-05: Adleman (1994), Science 266, 1021–1024, full article body, figure captions and relevant methodological notes inspected through a primary-paper reprint at https://computingbiology.github.io/docs/adleman1994.pdf. The scan includes neighboring articles; those are not sources for this chapter. Historical performance forecasts are not imported as current facts. The four-vertex example, its loops, counts, proof and implementation are newly constructed teaching material, not a reconstruction of Adleman's seven-vertex experiment.

Claims: DNA-CL06 exact filtering is sound and complete relative to a complete finite candidate pool; DNA-CL07 a negative experimental readout needs sensitivity/generation assumptions; DNA-CL08 illustrative candidate counts are deterministic code outputs, not molecule counts.

Math review: distinguish a walk (repeats allowed) from a Hamiltonian path; length n plus coverage of n distinct vertices implies no repetition. Completeness depends on candidate coverage and is not guaranteed by random molecular generation.

Skeptical review: a string simulator is not molecular evidence. The chapter explicitly models tokens, ideal filters and complete enumeration; it neither chooses DNA sequences nor predicts reaction kinetics. Source-derived history is brief, with detailed reconstruction deferred to chapter 6. Exercises challenge false positives, false negatives and exponential material assumptions.

Verification and publication outcome are recorded in CHAPTER_REPORT.md. This is internal review, not independent peer review.
