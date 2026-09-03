# Quantized hyperbolic cat maps: exact moment reductions and the BGS frontier

This repository is a research workspace for spectral statistics of quantized hyperbolic toral automorphisms. Its present load-bearing line is an exact finite-field reduction of a character-averaged fourth moment to a weighted pair-key distribution, followed by a still-incomplete geometric analysis of its fluctuations.

## Scientific status (3 September 2026)

**Established exactly.** For an odd prime level `N`, a multiplicative subgroup `H <= F_N^*` of order `K`, and `m=(N-1)/K`:

- the off-diagonal pair map `(x,y) -> (u,v,d)` is bijective on its stated domain and the diagonal collapses to one weighted key;
- the `k=2` constrained off-diagonal count is `(K-1)(K-2)`;
- the coupled `k=4` distribution `B(t)` has
  `sum_t B(t)=(K^2+1)N^2-(6K^2+3K)N+13K^2-3K`;
- character orthogonality gives the exact fourth-moment collapse
  `sum_{chi,psi in H^perp}|J(chi,psi;q)|^4=m^2 Sigma4(q)` with `Sigma4` the Fourier transform of `B`;
- `Var_{q!=0} Sigma4 = N Var_{t!=0} B(t)` exactly;
- `B(t)=O(t)+2(N-2)C_H(t)+(N-2)^2 1_{t=0}` exactly;
- the Cayley identity `d(u,v)=2/(c(u)-c(v))` turns the mixed term into an additive-energy problem.

For odd prime `K`, the characteristic-zero Cayley collision classification is finite and exact. For fixed `K`, finite-field exceptions are controlled by cyclotomic resultants. The fully audited exception sets currently stored here are
`E_11={23,67,89}` and `E_13={53,79,131,157,313}`. A fresh independent reconstruction also shows that `(N,K)=(461,23)` is exceptional for the forced-energy formula: `sum_t C_H(t)^2=1190`, not `902`.

**Not established.** General BGS/local eigenphase statistics are not proved. The proposed off/off elliptic-family estimate, and therefore the restricted `K=o(N^(1/4))` M1 concentration statement, remains conditional on a publication-grade verification of the algebraic family model and the exact geometric/sheaf hypotheses needed for square-root cross-correlation. Even a completed M1 theorem would still require a separate argument connecting moment concentration to a local spectral law.

## Repository structure

- `theory/` — current mathematical statements, derivations, proof obligations and open problems.
- `src/python/` — readable exact/symbolic and moderate numerical kernels.
- `src/cpp/` — expensive exhaustive finite-field kernels and independent exact verifiers.
- `experiments/verification/` — reproducible finite checks of load-bearing identities.
- `experiments/spectral/` — finite spectral-statistics experiments; never theorem evidence by themselves.
- `results/verified/` — small machine-readable exact/finite certificates.
- `results/numerical/` — explicitly numerical evidence.
- `results/reference/` — minimal retained reference inputs needed by active regression checks.
- `formal/` — Lean 4 finite certificates and formalization work.
- `literature/` — bibliography and current literature boundary.
- `paper/main.tex` — canonical manuscript source.

Historical failed routes, old Julia programs, duplicated data trees and superseded manuscripts are intentionally absent from the active tree. They remain recoverable from Git history; they do not define current mathematical truth.

## Reproducibility

Python dependencies are pinned in `requirements.txt`.

```bash
python -m compileall -q src/python experiments
python experiments/verification/verify_cayley_anchor_k23.py
python experiments/verification/verify_fourth_moment_factorization.py
python experiments/verification/verify_second_moment_reduction.py
```

C++20 components can be built with CMake:

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build -j
./build/fourth_moment_factorization
./build/cross_term_energy verify
```

Lean sources use the pinned toolchain in `formal/lean-toolchain`:

```bash
cd formal
lake build
```

The manuscript builds with `latexmk -pdf paper/main.tex` (or from inside `paper/`).

## Language policy

Python is used for transparent symbolic/exact orchestration and analysis; C++20 for hot exhaustive kernels and independent finite verification. Fortran will be introduced only when profiling identifies a dense numerical kernel where it is materially better. Julia is no longer part of the active implementation layer. Lean remains part of the project independently of whether a given runtime exposes a Lean executable.
