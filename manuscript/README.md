# Manuscript

`arithmetic_cat_map_moments.tex` is the single active research article.
`arithmetic_cat_map_moments.pdf` is the committed build, synchronized by
[`../.github/workflows/build-manuscript.yml`](../.github/workflows/build-manuscript.yml).

The manuscript is deliberately **status-accurate**: it develops exact
finite-field/arithmetic reductions and a deterministic trace-to-local-statistics
bridge, but it does **not** claim microscopic BGS/GOE/COE universality.

The publication-facing theorem surface now includes:

- the exact pair-key bijection, constrained count `(K-1)(K-2)`, weighted
  diagonal and fourth-moment distribution;
- the Cayley/additive-energy reduction and the pointwise
  `E_+(A)<34K^(8/3)` theorem;
- prime-order additive rigidity, square collision resultants and the Fibonacci
  obstruction/witness;
- the canonical additive difference discriminant, ratio-orbit factorization
  and global fourth-power discriminant identity;
- characteristic-zero multiplicative Cayley rigidity and its canonical product
  discriminant;
- the fixed-product row decomposition and the **exact** maximal-real trace
  support `Lambda'_K^(3)` for row intersections of multiplicity at least three;
- the explicit scope correction that the older dehomogenized `D'/G'` row
  invariants are one-way obstructions only because leading degree may drop at
  the projective point at infinity;
- the pointwise quadratic Cayley-energy theorem
  `E_+(A)<=11(K-1)(K-2)` outside `p|Lambda'_K^(3)`;
- the global `O(K^4)` split-prime collision-mass budget;
- the full Cayley/Jacobi trace identity and exact second/fourth trace moments;
- the double-averaged split excess theorem for `theta<1/3` and the density-one
  **exact** split baseline for `theta<1/5`;
- Frobenius amplification over the minimal extension
  `F_(p^ord_K(p))`, the all-prime collision/discriminant extension, and the
  density-one exact minimal-extension baseline for fixed `theta<1/3`;
- the corrected off/off elliptic theorem: every generic class has a reducible
  `2p-8` spike, and after spike extraction
  `Var O << pE_+(A)+K^2p+K^4sqrt(p)+K^4`;
- the exact partition-Mobius and Poisson trace-to-local-statistics formulas,
  which isolate a weighted **Heisenberg-scale** joint-trace comparison as the
  remaining band-limited microscopic spectral closure condition;
- the additional high-frequency tail obligation needed to remove the Fourier
  band-limit.

Authoritative derivations remain in `../mathematics/`, with claim status governed
by `../record/claim_ledger.md`. The research/reproducibility discipline is
recorded in `../record/research_operating_protocol.md`.

Build locally with

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error arithmetic_cat_map_moments.tex
```

The scientific CI independently recompiles the source. The PDF synchronization
workflow uses the TeX source commit time for reproducible metadata and commits
the binary only if `main` has not advanced during the build. A committed PDF
must not be treated as synchronized until the corresponding workflow/build has
actually succeeded.
