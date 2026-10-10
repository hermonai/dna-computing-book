# Architecture lineage

## Conclusion

The corpus contains two different naming eras. They must coexist until an explicit migration is approved.

| Era / artifact | Name used | Actual architecture family | Immutable identity | Treatment in this book |
| --- | --- | --- | --- | --- |
| current local `dogma` | DOGMA | recurrent / selective-state, no self-attention | unborn local branch; file hashes required | call “historical/current DOGMA recurrent line” |
| `evo-trainer` corrected core | DOGMA / dogma-core / dogma-scan | recurrent and non-transformer | commit `610117f0c6f...`, dirty tree | evidence requires committed or hashed artifacts |
| current local `hermon` | Hermon | transformer-oriented inference/runtime, paged KV | commit `472a44cdb511...` | call “historical/current Hermon runtime” |
| Evolutor v1.4.1 | Evolutor / GCS | umbrella formal model | local TeX/PDF, March 2026 | do not collapse into either neural branch |
| intended forward taxonomy | DOGMA | Transformer DNA-LLM | proposed name only | use “target DOGMA Transformer line” |
| intended forward taxonomy | Hermon DNA | non-transformer DNA-LLM | proposed name only | use “target Hermon DNA line” |

## Historical facts

The inspected `dogma/docs/ARCHITECTURE.md` begins by defining an inference engine for recurrent-state language models and contrasts fixed recurrent state with Transformer KV cache. Its associated book-generation prompt also defines DOGMA as non-transformer.

The inspected `hermon` repository contains `hermon-paged-kv`, attention kernels, prefix-radix state, and runtime KV modules. Those are transformer-oriented implementation facts, independent of future branding.

## Target taxonomy

The supplied execution prompt proposes two target lines. [D13 — Architecture lineage and evidence firewall](../book/diagrams/d13-architecture-lineage.txt) records both historical implementations, both proposed targets, and the rule that prevents a reused name from carrying evidence across architectures.

## Migration rule

Do not rename source repositories or rewrite old documents during bootstrap. New writing uses qualified names until a migration RFC maps repositories, packages, checkpoint metadata, artifact schemas, and claims. Historical measurements remain attached to the architecture that produced them, even if the brand later moves.
