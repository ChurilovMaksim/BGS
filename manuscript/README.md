# Manuscript

`arithmetic_cat_map_moments.tex` is the single active research article. `arithmetic_cat_map_moments.pdf` is a committed build of that source and is synchronized by `.github/workflows/manuscript-pdf.yml`.

The manuscript is deliberately a **status-accurate research article**, not a claim that BGS has been proved. It includes:

- the corrected pair-key bijection and weighted diagonal;
- the exact fourth-moment coupling and Fourier reduction;
- the Cayley/additive-energy mixed term;
- the complete audited `K=11,13` resultant sets and the `K=23` non-uniformity witness;
- the off/off elliptic route with every remaining theorem obligation named;
- useful earlier finite torus/scale/twisted-Jacobi and antiunitary results at their actual scope;
- the non-promotion of the unresolved all-orders Catalan/arcsine package;
- corrected interpretation of the numerical spacing/window-count diagnostics;
- the remaining microscopic BGS bridge and the relevant literature boundary.

Build locally with

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error arithmetic_cat_map_moments.tex
```

The scientific CI independently recompiles the source; the PDF workflow then commits the synchronized binary if the branch head is unchanged.
