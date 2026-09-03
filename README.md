# Arithmetic quantum cat maps and the BGS frontier

This repository is a research archive and working laboratory for exact
finite-field reductions, matrix-element moments and local spectral statistics
of quantized hyperbolic toral automorphisms.

The repository is intentionally organized like a mathematical research project,
not a software product.  The trust boundary is explicit: **preserve broadly,
trust narrowly**.

## Current mathematical position

The exact load-bearing object is the weighted pair-key fourth-moment
distribution `B(t)`.  The pair parametrization, `k=2` count, `k=4` total,
character-orthogonality collapse and finite Fourier mean/variance duality are
exact.  The mixed term is reduced by a Cayley transform to an additive-energy
problem.  For fixed odd prime subgroup order `K`, non-forced finite-field
collisions occur only at explicit cyclotomic reduction primes; the audited
sets currently include

`E_11={23,67,89}` and `E_13={53,79,131,157,313}`.

The exact negative control `(N,K)=(461,23)` has Cayley energy `1190`, whereas
the forced central-symmetry baseline is `902`.

The remaining off/off term has a non-isotrivial elliptic-family organization.
A restricted `K=o(N^(1/4))` M1 estimate is still a **theorem draft**, not a
finished theorem: the actual algebraic family and the exact sheaf-correlation
hypotheses must be certified at publication standard.  Even that would not
prove microscopic BGS/GOE local eigenphase statistics; the local-law bridge is
separate and open.

## Scientific layout

- `manuscript/` — the single active article source and its committed PDF.
- `mathematics/` — current derivations, proof notes and open questions.
- `computations/` — supported Python/C++ implementations and current regression
  checks.
- `evidence/` — promoted finite certificates, numerical evidence and minimal
  reference inputs.
- `formalization/` — Lean 4 finite certificates and open formalization work.
- `literature/` — current bibliography and literature-boundary notes.
- `record/` — reconstruction ledger, retractions, Julia migration map, exact ZIP
  manifest and the broader historical research corpus.

`record/corpus/` is deliberately non-authoritative.  It contains useful
experiments, negative results, review material and historical code/data restored
for scientific provenance.  A file being present there does not promote its
claim.

## Reproducibility

```bash
python -m pip install -r requirements.txt
python computations/verification/current_regression.py

cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build -j
./build/cross_term_energy verify
./build/fourth_moment_factorization
./build/catmap_order verify
./build/relation_automaton verify

cd formalization
lake build
```

The manuscript is built by

```bash
cd manuscript
latexmk -pdf -interaction=nonstopmode -halt-on-error arithmetic_cat_map_moments.tex
```

Both `arithmetic_cat_map_moments.tex` and `arithmetic_cat_map_moments.pdf` are
versioned.  CI independently recompiles the TeX source.

## Evidence labels

Use `record/claim_ledger.md` before citing a result.  In particular, finite Lean
certificates are not automatically uniform theorems, numerical GOE fits are not
a limiting law, and the historical Möbius-fiber/M4D proof is retracted from the
active argument.

## Language policy

Python is used for symbolic/exact orchestration and readable analysis.  C++20 is
used for exhaustive finite-field and combinatorial kernels and for independent
verification.  Fortran will be introduced only when profiling identifies a
dense numerical kernel for which it materially improves the implementation.

The supplied snapshot contains 31 Julia paths (23 byte-distinct sources).
Every one is accounted for in `record/julia_migration.md`; falsified Julia
algorithms are not mechanically translated and useful ones are migrated only
against preserved exact anchors.
