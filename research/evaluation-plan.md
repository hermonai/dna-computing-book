# Benchmark and evaluation plan

## Common experimental contract

Every run records dataset/version, tokenizer, split manifest, model configuration, parameter count, model width, state dimension where applicable, layers, heads/FFN width where applicable, training tokens, context length, optimizer and schedule, batch size, seeds, precision, hardware, source revision, and checkpoint hash.

## Integrity gates

1. **Shape and parity:** symbolic/tensor operations agree where an exact mapping exists.
2. **Causality:** interventions to future tokens do not alter prefix logits within a justified tolerance.
3. **Data separation:** group-aware or organism-aware splits and explicit margins prevent near-duplicate leakage.
4. **Oracle validity:** trivial and gameable baselines are measured before architecture claims.
5. **Dispersion:** per-seed results are inspected, not hidden behind a mean.

## Task families

- exact copy and associative retrieval;
- counting, parity, running aggregates, and finite-state machines;
- reverse-complement recognition and strand symmetry;
- motif and long-range regulatory dependency tasks;
- next-base modeling with organism-aware splits;
- streaming latency/state memory and Transformer prefill/decode/KV memory.

## Comparison families

Run parameter-matched, width-matched, state-capacity-matched, and compute-matched comparisons where meaningful. These answer different questions; none removes all confounds.

## Causal attribution

A statement “component X causes improvement Y” requires a baseline, one-factor ablation, transplant/control where possible, matched budgets, multiple seeds, and a recorded negative-result path. The analysis must report width, state dimension, and parameter budget for every arm.

## Initial stop conditions

- Do not optimize a custom kernel before reference semantics pass.
- Do not publish a long-context advantage from one task family.
- Do not interpret a mean until per-seed behavior and oracle validity are inspected.
- Do not call a mechanism “biological” without external biological validation.

