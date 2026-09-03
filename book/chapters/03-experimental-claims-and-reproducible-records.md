# Chapter 3 - Experimental Claims and Reproducible Records

After this chapter, you will be able to turn a scientific sentence into a bounded claim, specify the artifacts needed to test it, distinguish rerunning from replication, and preserve enough evidence for a later reader to reproduce or reject the conclusion.

## 3.1 A result is a dependency graph

An experimental result is often compressed into a sentence: model A outperformed model B; a molecular circuit produced the intended output; a symmetry improved sample efficiency. The sentence is the visible end of a larger structure. It depends on definitions, implementations, data, controls, budgets, measurements, and analysis choices.

If one dependency changes, the meaning of the result may change. A corrected causal mask can invalidate a checkpoint. A different split can expose leakage. An omitted state dimension can reverse a capacity comparison. A more selective assay can turn an apparent molecular product into noise.

This book therefore treats the complete unit of evidence as

\[
\mathcal{R}=(C, A, P, O, J),
\]

where (C) is the claim, (A) the artifact set, (P) the protocol, (O) the observations, and (J) the justified interpretation. The interpretation is not free to exceed the scope of the other four components.

## 3.2 The claim contract

Before an experiment begins, its claim should be writable in a form that could be false. A useful template is:

> Under conditions (K), intervention or mechanism (M), compared with control (B), changes observable (Y) by criterion (D), subject to exclusions (E).

Each term closes an escape route.

- (K) names the task, data population, input sizes, laboratory conditions, training budget, or hardware scope.
- (M) names the single mechanism being tested.
- (B) names a control that could plausibly explain the same result.
- (Y) names the raw observable before it becomes a narrative.
- (D) says what would count as support, failure, or ambiguity.
- (E) states what the experiment does not test.

For example, “reverse-complement equivariance helps DNA models” is too open. A testable version is: under a preregistered motif-classification dataset with group-separated sequence families, an exactly equivariant mechanism, compared with the same backbone using augmentation alone, improves held-out balanced accuracy under matched training compute across five declared seeds. This still would not establish a general advantage on genomes, causal biological fidelity, or superiority over every architecture.

## 3.3 Promotion requires gates, not enthusiasm

[D16 — Claim promotion, rejection, and correction](../diagrams/d16-claim-promotion.txt) is the governing graph for experimental claims in this book. It begins with a formal contract, then passes through implementation integrity, a frozen experiment, intervention or ablation, and replication. Every stage has a failure exit.

The failure exits matter. Without them, the process becomes a ceremonial checklist performed only after a desired result appears. A causal test that falsifies the proposed mechanism should narrow or withdraw the mechanism claim even when the headline metric remains positive. A comparison with unequal hidden state should be redesigned even when parameter counts match. A failed independent replication should reopen the conclusion.

Claim status is therefore versioned. A statement may move among `HYPOTHESIS`, `SUPPORTED UNDER PROTOCOL`, `REJECTED`, `WITHDRAWN`, and `OPEN`. “Supported” is not an irreversible promotion to truth; it points to the exact record that earned the wording.

## 3.4 The experiment manifest

Reproducibility starts before execution. A manifest freezes the identities and choices that would otherwise drift. A minimal machine-learning record should include:

```yaml
claim_id: C010
code_revision: <commit-or-content-hash>
architecture_id: <stable-mechanism-id>
data:
  source_ids: [<source-and-version>]
  content_hashes: [<hash>]
  split_strategy: <grouping-and-seed>
  exclusions: [<declared-exclusion>]
model:
  config_hash: <hash>
  parameter_count: <count>
  width: <dimensions>
  inference_state: <shape-and-growth-rule>
training:
  objective: <definition>
  optimizer: <definition>
  budget: <steps-tokens-flops-or-time>
  seeds: [<seed-list>]
evaluation:
  metrics: [<definitions>]
  interventions: [<tests>]
  stopping_rule: <predeclared-rule>
environment:
  software: <versions>
  hardware: <device-record>
```

The literal field names may evolve. The obligations do not. A manifest must identify what ran, what it consumed, what capacity it had, how long it was allowed to learn, and how success was judged.

A molecular experiment needs an analogous record: strand sequences and modifications, reagent identities and lots when relevant, concentrations, buffer, temperature schedule, timing, vessel layout, controls, assay settings, raw instrument outputs, and analysis code. The computational and molecular manifests differ because their failure modes differ.

## 3.5 Immutable artifacts and derived summaries

Raw observations should be preserved separately from derived summaries. Per-seed metric files are primary artifacts; their mean and confidence interval are derived. Instrument traces and uncropped images are primary; a selected panel is derived. Checkpoints are primary for a model result; a rounded table is derived.

An artifact bundle should link:

1. the frozen manifest;
2. source and dependency identities;
3. input data identities without redistributing restricted data;
4. raw outputs and logs;
5. checkpoints or physical sample identifiers where feasible;
6. analysis code and its outputs;
7. the final scoped conclusion;
8. corrections and superseding records.

Content hashes help detect accidental replacement. They do not establish scientific validity. A perfectly hashed leaked dataset remains leaked, and a reproducible confound remains a confound.

## 3.6 Controls are alternate explanations made executable

A control is not merely a weaker model. It represents another explanation for the observed result.

If a regulation-inspired router improves accuracy, a generic router of comparable capacity tests whether the biological structure mattered or conditional computation alone was sufficient. If reverse-complement augmentation helps, an exact equivariant model should be compared with augmentation under the same data exposure. If a DNA algorithm appears fast in laboratory rounds, material volume and readout work test whether the advantage was moved into an unreported resource.

Capacity matching also has several meanings. Equal parameter count can leave width, recurrence state, attention memory, and operation count unequal. Equal width can leave parameters unequal. Equal compute can leave memory and representational structure unequal. The honest record reports multiple views instead of calling one of them “fair” without qualification.

Interventions test mechanism more directly than correlation. For a causal sequence model, change future tokens while holding the prefix fixed; earlier logits should remain unchanged within a declared tolerance. For a proposed gate, force or remove the gate while preserving the rest of the computation. For a molecular circuit, omit or replace a strand whose role is mechanistically required. The intervention should target the claimed dependency.

## 3.7 Seeds, uncertainty, and heterogeneous outcomes

An aggregate can hide structure. Suppose five training runs produce strong gains in three seeds and severe failures in two. The mean may look modestly positive while describing no typical run. Every seed must therefore be inspected before aggregation.

The record should preserve the seed-level outcome, training trajectory, stopping event, and any exclusion. Exclusions decided after seeing the result need explicit justification and a sensitivity analysis with the run included. More seeds reduce sampling uncertainty, but they do not repair leakage, a broken baseline, or a biased oracle.

Uncertainty should match the sampling process. Variation across random initialization is different from variation across datasets, biological replicates, instruments, or laboratory days. Pooling them into one error bar erases the question the interval answers.

## 3.8 Rerun, reproduction, and replication

These terms are useful when kept distinct.

- A **rerun** executes the same code and manifest again, often in the same environment.
- A **reproduction** reconstructs the reported result from the described artifacts and protocol.
- A **replication** tests the claim while varying a meaningful dependency, such as implementation, dataset, laboratory, or measurement path.

A deterministic cached rerun can verify artifact integrity but provides little independence. A clean-room implementation may expose an ambiguity in the formal definition. A second biological sample or laboratory may expose batch sensitivity. A new dataset may show whether a machine-learning effect transfers beyond the original distribution.

Replication is not required to publish every exploratory result, but the strength of the prose should track the independence of the evidence.

## 3.9 A worked claim record

Consider claim `C010`: reverse-complement equivariance may improve sample efficiency on an appropriate genomic task.

The formal artifact defines (RC) and the equivariance relation. Symbolic and tensor parity tests verify the transform. The implementation artifact contains a plain causal baseline, an augmentation control, and one equivariant variant. The data manifest uses family-aware groups so near-duplicate strands do not cross splits. The budget fixes tokens, optimizer steps, and tuning opportunities. The evaluation reports every seed, learning curves, held-out performance, parameter/width/compute/state tables, and an intervention confirming the symmetry.

Three outcomes remain scientifically useful:

1. The equivariant model consistently improves the preregistered metric: report scoped support.
2. Augmentation explains the gain: reject the stronger architectural-mechanism claim while retaining the practical data result.
3. Neither helps or the effect is unstable: preserve the negative result and revise the research priority.

None of the outcomes establishes that double-stranded molecular biology caused the behavior of the digital model.

## 3.10 Correction is part of reproducibility

A reproducible record must be correctable. When a defect is found, the old artifacts should not vanish. The correction identifies the affected claim, the failed dependency, the scope of invalidation, the repaired protocol, and the rerun or replication outcome. Descendant claims that relied on the defect are re-evaluated.

This is why [D16](../diagrams/d16-claim-promotion.txt) contains correction returns rather than a terminal success box. Public science is not a sequence of polished conclusions. It is a versioned structure in which readers can see why a sentence was once reasonable, why it changed, and what evidence now supports it.

## What this chapter established

- A result consists of a claim, artifacts, protocol, observations, and a bounded interpretation.
- A claim contract names conditions, mechanism, control, observable, decision rule, and exclusions.
- Manifests are frozen inputs to experiments, not retrospective descriptions.
- Raw and per-seed artifacts remain primary; aggregates are derived.
- Controls encode alternate explanations, while interventions target claimed dependencies.
- Rerun, reproduction, and replication provide different degrees of independence.
- Corrections must propagate through the claim dependency graph.

## What remains unverified

- The repository has not yet executed claim `C010` or another DNA-specific neural comparison.
- The final manifest schema and long-term artifact host are not selected.
- Molecular chapters will require protocol fields beyond the computational schema shown here.
- Independent review is still needed to test whether the completion gates are sufficient and usable.
