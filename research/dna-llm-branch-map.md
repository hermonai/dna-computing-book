# DNA-LLM branch map

## Shared layer

Both branches may share DNA tokenization, reverse-complement transforms, dataset manifests, leakage-aware splits, losses, metrics, seeds, artifact metadata, and causality tests. Sharing stops at the model interface.

## Transformer DNA line - proposed target name: DOGMA

```text
DNA tokens -> embedding -> causal Transformer blocks -> normalization -> logits
                              |
                              +--> attention state / KV cache at inference
```

Research increments, each tested separately: reverse-complement augmentation/equivariance, strand-aware attention, regulatory conditioning, biological position representations, long-context attention, retrieval, and sparse/MoE variants.

Baseline rule: begin with `torch.nn` and a plain causal Transformer. A biological label is not a mechanism result.

## Non-Transformer DNA line - proposed target name: Hermon DNA

```text
DNA tokens -> embedding -> recurrent / state-space / regulated state -> logits
                                  |
                                  +--> fixed or structured carried state
```

Baseline family: GRU, simple recurrence, and a clearly specified state-space update. Later candidates include selective scans, graph state, formal GCS expression, structural memory, and symbolic-neural hybrids.

Baseline rule: do not define “genomic computation” as whichever recurrence is currently implemented.

## Comparison matrix

| Capability | Transformer test | Non-transformer test |
| --- | --- | --- |
| exact past-content retrieval | attention and cache baselines | state-capacity sweep |
| running aggregate / streaming state | causal attention baseline | recurrent step baseline |
| motif and strand symmetry | equivariant/augmented variants | equivariant/augmented variants |
| regulatory dependency | conditional-attention control | gated-state control |
| context scaling | prefill, decode, KV memory | scan/step, carried-state memory |

No global winner is expected. Results are task-, budget-, and machine-specific.

