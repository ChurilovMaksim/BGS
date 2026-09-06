# Active research line

This directory describes the reasoning that survives the 2026-09-03 audit and is the default starting point for proof work. Root `STATUS.md` controls theorem status; `docs/roadmap.md` controls the execution programme.

## Surviving chain

1. **Twisted-Jacobi representation.** The rank-1 Hecke-sector matrix is computed from a finite-field twisted Jacobi sum. Canonical kernel: `code/math/twisted_jacobi.py`.
2. **Independent computational reproduction.** The R82 q-curves are reproduced at `N=199` and `N=3571` from immutable preserved inputs. Check: `code/verification/baseline_r82.py`.
3. **Exact `k=2` layer.** The off-diagonal constraint set has exact cardinality `(K-1)(K-2)` at the audited designs and the associated energy identity is directly checked. Check: `code/verification/h3_k2_exact_reduction.py`.
4. **Independent matrix-element regression.** Direct scalar character sums agree with the production contraction at `N=461` and `N=19489` within the documented tolerance. Check: `code/verification/theorem_ii_new_primes.py`.
5. **M1 cycle 001 — exact structure.** The weighted key table, quotient-character projector, singular/regular decomposition, and full cross-twist energy are reconstructed by independent Python and C++17 implementations. See `M1_CROSS_TWIST_001.md`, `code/research/m1/`, and `results/research/m1/cross_twist_suite.json`.
6. **M1 cycle 002 — regular single-twist analytic lemma.** A polynomial domain mask converts the restricted rational fiber sum to a complete polynomial multiplicative-character sum. The non-`m`-th-power classification is proved for generic `d` and the `d=±1` collisions, yielding `|A_{r,s}(d)| <= 3 sqrt(N)` for all nontrivial regular twists via the standard Weil theorem. See `M1_WEIL_002.md` and `results/research/m1/regular_weil_classifier.json`.
7. **Current bottleneck.** Determine whether the exact singular term is removed by the correct spectral centering, then control the **assembled** regular cross-twist covariance/energy in the true arithmetic regime. See `M1.md`.
8. **Spectral target.** GOE-like spacing and matched number variance remain target/falsifier evidence, not limiting theorems.

The historical Möbius-fiber theorem does not close Step 7. The R86/R87 trace-fluctuation lemma also cannot bypass it as written because it applies a scalar binomial expansion to noncommuting matrices and then uses an unproved factorisation.

## Active files

- `M1.md` — canonical statement of the open analytic bottleneck and promotion rule.
- `M1_CROSS_TWIST_001.md` — exact weighted assembly, singular split, raw-energy obstruction, and arithmetic-regime correction.
- `M1_WEIL_002.md` — regular divisor/non-power classification and the `3 sqrt(N)` single-twist theorem.
- `../docs/roadmap.md` — full programme gates and immediate execution queue.

Higher-moment, shape-automaton, word, and rank-2/Sp4 corpora remain available as alternative mechanisms. They become load-bearing only after an independent proof route passes the same exact/analytic/reproducibility gates.
