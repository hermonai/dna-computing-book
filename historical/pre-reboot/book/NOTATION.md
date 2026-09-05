# Mathematical notation

## Sequence algebra

| Symbol | Meaning |
| --- | --- |
| \(\Sigma_{\mathrm{DNA}}=\{A,C,G,T\}\) | canonical DNA alphabet |
| \(s=s_1\ldots s_n\) | strand written from 5-prime to 3-prime unless marked otherwise |
| \(|s|\) | sequence length |
| \(c:\Sigma_{\mathrm{DNA}}\to\Sigma_{\mathrm{DNA}}\) | base complement |
| \(RC(s)=c(s_n)\ldots c(s_1)\) | reverse complement |
| \(d_H(s,t)\) | Hamming distance for equal-length strands |
| \(m(s,t)\) | explicitly defined matching score |

The text uses `5'` and `3'` in prose and mathematical primes only inside equations. A complement and a reverse complement are different operations.

## Molecular and formal computation

| Symbol | Meaning |
| --- | --- |
| \(X_i\) | molecular species, never a token position unless stated |
| \(r: \sum_i \alpha_iX_i\to\sum_i\beta_iX_i\) | reaction rule |
| \(\mathbf{n}\) | molecular-count state vector |
| \(x\Rightarrow_R y\) | one rewrite under rule set \(R\) |
| \(G=(V,E)\) | graph; vertex and edge meanings must be declared locally |
| \(q\in Q\) | automaton state |
| \(P(y\mid x)\) | probability under a declared stochastic model |

## Regulation and expression

| Symbol | Meaning |
| --- | --- |
| \(g_i\) | gene or computational module |
| \(\gamma_i(x)\) | gate state for module \(i\) in context \(x\) |
| \(E_x(G)\) | expressed subset of genome/program \(G\) for context \(x\) |
| \(\Omega\) | mechanistic execution trace |

These symbols describe a formal model unless a chapter explicitly declares a biological system.

## Machine learning

| Symbol | Meaning |
| --- | --- |
| \(x_{1:T}\) | token sequence |
| \(h_t\) or \(s_t\) | hidden/recurrent state at step \(t\) |
| \(\theta\) | trainable parameters |
| \(p_\theta(x_t\mid x_{<t})\) | autoregressive predictive distribution |
| \(\mathcal{L}(\theta)\) | training objective |
| \(d_{\mathrm{model}}\) | model/embedding width |
| \(d_{\mathrm{state}}\) | recurrent state dimension |

Never use \(G\) for both a molecular graph and a genomic program in the same section. Every asymptotic statement names its input size, cost model, and machine assumptions.

