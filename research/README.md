# Active research line

This directory describes the reasoning that survives the 2026-09-03 full audit and is the default starting point for future proof work.

## Surviving chain

1. **Twisted-Jacobi representation.**  The rank-1 Hecke-sector matrix is computed from a finite-field twisted Jacobi sum.  Canonical kernel: `code/math/twisted_jacobi.py`.
2. **Independent computational reproduction.**  The R82 q-curves are reproduced at `N=199` and `N=3571` from immutable preserved inputs.  Check: `code/verification/baseline_r82.py`.
3. **Exact `k=2` layer.**  The off-diagonal constraint set has exact cardinality `(K-1)(K-2)` at the audited designs and the associated energy identity is directly checked.  Check: `code/verification/h3_k2_exact_reduction.py`.
4. **Independent matrix-element regression.**  Direct scalar character sums agree with the production contraction at `N=461` and `N=19489` within the documented tolerance.  Check: `code/verification/theorem_ii_new_primes.py`.
5. **Spectral target.**  GOE-like spacing and matched number variance are observed numerically after desymmetrisation.  These measurements are targets/falsifiers, not limiting theorems.
6. **Current bottleneck.**  M1 must control the full ordered twist-summed fluctuation energy, including cross-twist terms, in a stated asymptotic regime.  See `M1.md`.

The historical Möbius-fiber theorem does not close Step 6.  The R86/R87 trace-fluctuation lemma also cannot bypass it as written: its Step 1 applies a scalar binomial expansion to `C_q` and `C_q^*` without a commutation theorem, and its subsequent factorisation is unproved.

Higher-moment and rank-2/Sp4 experiments remain available in the research corpus and may suggest a different route.  A downstream route becomes canonical only when it supplies an independent load-bearing estimate instead of importing either invalid promotion.
