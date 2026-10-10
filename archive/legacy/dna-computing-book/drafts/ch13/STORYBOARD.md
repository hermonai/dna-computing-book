# Chapter 13: SAT and combinatorial constructions

Author storyboard approved before prose, 24 September 2026. This is an internal authoring decision, not independent scientific approval.

## 01-encoding

Question: How is an assignment physically addressable?

An oriented assignment strand with three distinct variable-value domains and a complementary capture probe; direction arrows are backbone polarity, dashed rungs are pairing. The logical assignment is fixed during capture; only location changes. Caption: representation and separation are different operations. Risk: domains are symbols, not validated sequences.

Editable TikZ source plus semantic TXT companion. Labels, geometry and line patterns remain meaningful in grayscale.

## 02-partition

Question: Why must clause branches be disjoint?

Three literal tests act on successive residual tubes. Captured copies merge once; previously captured molecules do not enter later branches. A single assignment satisfying two literals follows only its first matching branch. Caption: OR without duplicated inventory. Risk: do not imply copying when drawing a split.

Editable TikZ source plus semantic TXT companion. Labels, geometry and line patterns remain meaningful in grayscale.

## 03-cube

Question: How do clauses shrink the candidate space?

Eight labeled vertices of a three-bit cube, with survivors after each clause marked by circles versus crosses. Geometry is an abstract state space, not molecular conformation. Caption: intersection removes exactly the falsifying assignments. Risk: labels must agree with generated results.

Editable TikZ source plus semantic TXT companion. Labels, geometry and line patterns remain meaningful in grayscale.

## 04-coverage

Question: When does enormous parallelism still miss a witness?

Generated plot of probability of observing a unique satisfying assignment versus independent samples, with exact formula and declared n. Candidate count increases; success need not reach one. Caption: physical coverage is a resource. Risk: uniform independent sampling is an assumption.

Editable TikZ source plus semantic TXT companion. Labels, geometry and line patterns remain meaningful in grayscale.

## 05-certificate

Question: What does a detected molecule prove?

Assignment domains decoded to values; literal truth table compared against CNF. Separate positive witness verification from a no-signal result with two possible causes. Caption: existence is certifiable, absence requires coverage and assay guarantees. Risk: no-signal is not an UNSAT certificate.

Editable TikZ source plus semantic TXT companion. Labels, geometry and line patterns remain meaningful in grayscale.
