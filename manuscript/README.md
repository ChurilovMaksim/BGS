# Manuscript

`arithmetic_cat_map_moments.tex` is the active research article.
`arithmetic_cat_map_moments.pdf` is the committed build, synchronized by
[`../.github/workflows/build-manuscript.yml`](../.github/workflows/build-manuscript.yml).

The manuscript is deliberately **status-accurate**: it develops exact
finite-field moment results and the current arithmetic frontier, but it does
not claim a proof of microscopic BGS/GOE universality.

The publication-facing theorem surface now includes:

- the exact pair-key bijection, constrained count `(K-1)(K-2)`, weighted
  diagonal and fourth-moment distribution;
- the Cayley/additive-energy reduction and the pointwise
  `E_+(A)<34K^(8/3)` theorem;
- prime-order additive rigidity, square collision resultants and the Fibonacci
  obstruction/witness;
- the global `O(K^4)` split-prime collision-mass budget;
- the canonical additive difference discriminant, ratio-orbit factorization
  and global fourth-power discriminant identity;
- characteristic-zero multiplicative Cayley rigidity and the canonical product
  discriminant;
- the full Cayley/Jacobi trace identity and exact second/fourth trace moments;
- the double-averaged quadratic excess theorem for `theta<1/3`;
- the density-one **exact** Cayley baseline theorem for `theta<1/5`;
- the corrected off/off elliptic theorem: every generic class has a reducible
  `2p-8` spike, and after spike extraction
  `Var O << pE_+(A)+K^2p+K^4sqrt(p)+K^4`;
- explicit separation of all moment statements from the still-open
  mean-spacing BGS/GOE local-statistics problem.

`frontier_addendum_20260904.tex` records publication-ready frontier material
that is being integrated into the main article.  The authoritative mathematical
versions are the corresponding files in `../mathematics/` and the status
ledger `../record/claim_ledger.md`.

Build locally with

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error arithmetic_cat_map_moments.tex
```

The scientific CI independently recompiles the source.  The PDF synchronization
workflow uses the TeX source commit time for reproducible metadata and commits
the binary only if `main` has not advanced during the build.
