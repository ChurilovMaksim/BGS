# Arithmetic quantum cat maps and the BGS frontier

This repository is a curated research project for exact finite-field reductions, matrix-element moments and the unresolved local spectral-statistics problem for arithmetic quantum cat maps.

The governing rule is **preserve useful evidence, trust only what is re-verified**. Historical files are not allowed to masquerade as current theorems, and the active tree is kept deliberately small.

## Current mathematical position

The load-bearing exact object is the weighted pair-key fourth-moment distribution `B(t)`. The pair parametrization, diagonal multiplicity, `k=2` and `k=4` finite counts, character-orthogonality collapse and finite Fourier mean/variance identities are exact.

The mixed term is transformed to the additive energy of `c(H\{1})`, `c(h)=(h+1)/(h-1)`. For fixed odd prime subgroup order `K`, non-forced collisions can occur only at finitely many cyclotomic reduction primes. The active exact producer recomputes all 720 matching systems and the resultants for

`E_11={23,67,89}` and `E_13={53,79,131,157,313}`

on every CI run. The exact negative control `(p,K)=(461,23)` has collision energy `1190`, versus forced baseline `902`; this forbids a naive uniform-in-`K` extrapolation.

The remaining off/off fluctuation has a promising non-isotrivial elliptic organization, but the sheaf/isogeny/correlation step is still a **theorem draft**. Even a completed moment estimate would not prove microscopic BGS/GOE eigenphase statistics: the local-law bridge remains separate and open.

See `mathematics/results.md` for the authoritative claim list.

## Layout

- `manuscript/` — one active article, both TeX source and committed PDF.
- `mathematics/` — authoritative current derivations and open obligations.
- `computations/` — supported Python/C++ code and exact regression gates.
- `evidence/` — promoted finite certificates, descriptive numerical records and minimal reference inputs.
- `formalization/` — active Lean 4 finite certificates only.
- `literature/` — bibliography and literature-boundary notes.
- `record/` — retractions, reconstruction/provenance, migration records and historical material that remains scientifically useful.

`record/corpus/` is non-authoritative provenance. Presence there does not promote a claim.

## Reproducibility

```bash
python -m pip install -r requirements.txt
python computations/verification/current_regression.py
python computations/verification/mixed_cayley_energy.py

cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build -j
./build/fourth_moment_pair_key_verifier
./build/cat_map_order verify

cd formalization
lake build
```

CI additionally checks that every active Lean module is in the root import graph, that promoted JSON provenance resolves, and that the fixed-`K` Cayley certificate is synchronized with a fresh exact recomputation.

The manuscript is built with

```bash
cd manuscript
latexmk -pdf -interaction=nonstopmode -halt-on-error arithmetic_cat_map_moments.tex
```

Both `arithmetic_cat_map_moments.tex` and `arithmetic_cat_map_moments.pdf` are versioned; a dedicated workflow rebuilds and synchronizes the PDF.

## Evidence discipline

Use `record/claim_ledger.md` before citing a result. In particular:

- finite Lean evaluation at one prime is not a uniform theorem;
- finite numerical GOE resemblance is not a hypothesis test or limiting law;
- the historical Möbius/M4D proof route is retracted;
- historical full-group arcsine/Catalan all-orders claims are not promoted where they depend on unresolved word-trace reduction;
- theorem drafts remain drafts until every external theorem hypothesis is checked for the actual family.

## Julia migration

The supplied snapshot contains 31 Julia paths (23 byte-distinct sources). Every path is accounted for in `record/julia_migration.md`. Useful kernels are migrated only against preserved anchors; falsified Julia algorithms are kept as negative historical evidence rather than translated mechanically.
