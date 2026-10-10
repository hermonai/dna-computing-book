# Chapter 9 storyboard: amplification and copy-number evidence

Author storyboard approved for implementation, 20 September 2026.
The five plates answer distinct questions; they are not assay protocols.

1. Primer geometry: two antiparallel parental strands, coordinate interval [a,b), forward and reverse primers with marked 3-prime growing ends pointing inward. Dashed rungs mean pairing; solid colored segments mean backbone. Extension continues along available template, not automatically to the opposite primer. Risk: implying the reverse primer has the same written sequence as its top-strand site.
2. Product birth: one lineage through cycles 1, 2 and 3. First new strand has one primer-defined end; copying it creates the first exact-length strand; copying that creates an exact-length duplex. Old parental strands persist. Companion recurrence counts the whole population, not just this lineage. Risk: calling the cycle-2 heteroduplex an exact duplex.
3. Resource accounting: two oriented mature templates with primers and new residues; per extra duplex, one forward primer, one reverse primer, and 2L-lf-lr dNTPs. Existing templates are retained. Risk: confusing primer residues with free dNTP consumption.
4. Growth and bias: numerical curves from the executable finite-resource model; separate log-scale exponential growth from saturation. A small unequal-efficiency example exposes compounded ratio bias. Numbers are assigned inputs, not measured amplification efficiency.
5. Threshold and sampling: same fluorescence threshold intersected by two assigned initial populations, alongside the empty-well probability exp(-lambda). Different mechanisms, separate panels: signal crossing does not undo an empty initial draw. Risk: inferring absolute abundance without gain and efficiency calibration.

Captions must name assumptions and inferences. Every plate has editable TikZ
and a semantic TXT companion. All pages receive color/grayscale inspection.
