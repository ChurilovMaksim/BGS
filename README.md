# Quantized cat maps and BGS: research workspace

This repository studies spectral statistics of quantized hyperbolic cat maps after symmetry reduction. The long-term goal is a rigorous path from exact finite-field formulas to a random-matrix local law.

**Current status: general BGS is not proved.** The strongest active line uses the exact pair-key fourth-moment distribution `B(t)`. A restricted M1 concentration proof chain for odd prime `K`, explicit nonexceptional split primes `N`, and `K=o(N^(1/4))` is assembled but still marked audit/formalization pending. Historical Mobius-fiber proof claims remain archive-only because they analyze the wrong finite object.

## Start here

1. `STATUS.md` - concise scientific status and theorem/draft/retraction boundary.
2. `research/theory.md` - current mathematical core.
3. `research/ledger.md` - active chronology of decisions and discoveries.
4. `research/problems/m1_fluctuation_energy.md` - load-bearing M1 problem statement.
5. `research/notes/k2_cayley_energy.md` and `research/notes/m1_offoff_elliptic_family.md` - detailed current derivations.
6. `research/engineering/language_migration.md` - complete audit of the historical Julia layer and supported replacements.
7. `paper/main.tex` - the single editable manuscript source.
8. `references/bibliography.md` - literature used by the active proof program.

## Language and implementation policy

- `src/python/bgs/` - reusable symbolic/exact arithmetic and research kernels.
- `src/cpp/` - expensive finite-field loops, exhaustive combinatorics, dynamic programs, and independent exact verification.
- `experiments/` - reproducible drivers, falsifiers and verification entry points; not a second library tree.
- Fortran is not introduced just to have another language. It is reserved for a future profiled dense-numerical kernel if it gives a concrete benefit.
- A second implementation of the same mathematics exists only when independent reproduction is part of the scientific certificate.

All 31 historical Julia paths (23 byte-distinct sources) are accounted for. Supported mathematics was consolidated into a small number of Python/C++ components; falsified or superseded Julia lines were not mechanically cloned. The original Julia sources remain once in `archive/legacy-workspace/` and Git history.

## Repository layout

- `results/verified/` - curated finite/exact certificates.
- `results/diagnostics/` - falsifiers and diagnostic outputs.
- `results/numerical/` - numerical evidence only.
- `formal/` - Lean sources/certificates with build status stated explicitly.
- `paper/` - exactly one current manuscript source (`main.tex`) and its built PDF; no competing `proof/final/complete` TeX trees.
- `references/` - bibliography plus literature/symbolic-check provenance.
- `archive/legacy-workspace/` - immutable pre-restructure research corpus, including failed routes and historical manuscripts.

The archive is intentionally large and provenance-oriented. The active workspace is intentionally compact and status-controlled. Historical material is promoted only after reconstruction, an appropriate independent check, and an honest rewrite of the claim.
