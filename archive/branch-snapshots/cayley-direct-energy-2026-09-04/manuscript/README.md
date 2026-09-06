# Manuscript

`arithmetic_cat_map_moments.tex` is the single active research article.
`arithmetic_cat_map_moments.pdf` is a committed build of that source and is
synchronized by
[`../.github/workflows/build-manuscript.yml`](../.github/workflows/build-manuscript.yml).

The manuscript is deliberately a **status-accurate research article**, not a
claim that BGS has been proved. It includes:

- the corrected pair-key bijection, exact `(K-1)(K-2)` constrained count and
  weighted diagonal;
- the exact fourth-moment coupling and explicit Fourier mean/variance
  identities;
- the Cayley/additive-energy mixed term;
- the complete audited `K=11,13` resultant sets and the `K=23`
  non-uniformity witness;
- the off/off elliptic route with every remaining theorem obligation named and
  the historical symbolic layer explicitly kept at draft status;
- useful earlier finite torus/scale/twisted-Jacobi and antiunitary results at
  their actual scope;
- non-promotion of the unresolved all-orders Catalan/arcsine and higher-rank
  extrapolations;
- regenerated full-complex-Hermitian spacing/window-count diagnostics with
  corrected statistical interpretation;
- the separate microscopic BGS bridge and current literature boundary.

Build locally with

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error arithmetic_cat_map_moments.tex
```

The scientific CI independently recompiles the source. The PDF workflow uses
the TeX source commit time for reproducible metadata and commits the
synchronized binary only if `main` has not advanced during the build.
