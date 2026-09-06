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
- prime-order additive rigidity, square collision resultants, the Fibonacci
  obstruction/witness, and the canonical difference discriminant with its
  ratio-orbit fourth-power structure;
- the fixed-product row decomposition and the **exact** maximal-real trace
  support `Lambda'_K^(3)` for row intersections of multiplicity at least three;
- the explicit scope correction that the older dehomogenized `D'/G'` row
  invariants are one-way obstructions only because leading degree may drop at
  projective infinity;
- the Bass-based characteristic-zero trace-intercept theorem: every affine
  intercept fibre has size at most two and all double fibres are explicit;
- the cyclotomic-unit matching formula `W_r(b)=V_r(a) mod q` for finite row
  intersections;
- the general scalar shift-resultant identity
  `ord_(Z=0) R_(K,r)(Z)=I_(1,r)` and three-generator order-three support
  `c_0=c_1=c_2=0`;
- the inverse-row reflection theorem
  `I_-1(q)=2 deg gcd(E,O mod q)` and its half-degree exact support `Xi_K`;
- the inverse perfect-square factorization
  `R_-(Z)=2^m F(Z/2) S(Z)^2`, giving
  `I_-1(q)=2 ord_0 S` and the two-scalar criterion
  `I_-1>=3 iff S(0)=S'(0)=0`;
- the translated half-degree identity
  `S(Z)=+-Res(E_Z,O_Z)`, which identifies the two inverse support scalars as a
  half-degree resultant and its translation derivative and avoids the
  degree-`m^2` shift resultant;
- the per-ratio deterministic support budget
  `sum_(I_r(p)>=3) log p = O(K^3)`, explicitly separated from the still-open
  polynomial largest-split-prime target;
- the pointwise quadratic Cayley-energy theorem
  `E_+(A)<=11(K-1)(K-2)` outside the exact order-three split support;
- the global `O(K^4)` split-prime collision-mass budget;
- the full Cayley/Jacobi trace identity and exact second/fourth trace moments;
- the double-averaged split excess theorem for `theta<1/3` and density-one
  **exact** split baseline for `theta<1/5`;
- Frobenius amplification over the minimal extension
  `F_(p^ord_K(p))`, the all-prime collision/discriminant extension, and the
  density-one exact minimal-extension baseline for fixed `theta<1/3`;
- the corrected off/off elliptic theorem with the reducible `2p-8` spike and
  `Var O << pE_+(A)+K^2p+K^4sqrt(p)+K^4` after spike extraction;
- the exact partition-Mobius and Poisson trace-to-local-statistics formulas,
  isolating weighted **Heisenberg-scale** joint-trace comparison as the
  band-limited microscopic spectral closure condition;
- the additional high-frequency tail obligation needed to remove the Fourier
  band-limit.

Authoritative derivations remain in `../mathematics/`, with claim status governed
by `../record/claim_ledger.md`. The research/reproducibility discipline is
recorded in `../record/research_operating_protocol.md`. The current dated
research-state audit is
[`../record/frontier_pass_20260905.md`](../record/frontier_pass_20260905.md).
The source audit for the cyclotomic trace-intercept theorem is
[`../literature/cyclotomic_row_support_sources_20260905.md`](../literature/cyclotomic_row_support_sources_20260905.md); Dvornicich--Zannier remains an unmatched lead, not a used theorem. Exact inverse pair-sum timing/support data are recorded in
[`../evidence/cayley_inverse_pair_sum_factorization_20260905.txt`](../evidence/cayley_inverse_pair_sum_factorization_20260905.txt).

Build locally with

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error arithmetic_cat_map_moments.tex
```

The scientific CI independently recompiles the source. The PDF synchronization
workflow watches the manuscript tree, uses the TeX source commit time for
reproducible metadata, and commits the binary only if `main` has not advanced
during the build. The synchronization commit carries `[skip ci]`, so rebuilding
the binary does not create a workflow loop. A committed PDF must not be treated
as synchronized until the corresponding workflow/build has actually succeeded.