# Arithmetic quantum cat maps — exact reductions and the BGS frontier

[![Scientific verification](https://github.com/ChurilovMaksim/WoW/actions/workflows/ci.yml/badge.svg)](https://github.com/ChurilovMaksim/WoW/actions/workflows/ci.yml)
[![Manuscript PDF](https://img.shields.io/badge/manuscript-PDF-b31b1b.svg)](manuscript/arithmetic_cat_map_moments.pdf)
[![Lean 4](https://img.shields.io/badge/formalization-Lean%204-ffffff.svg)](formalization/)
[![Julia](https://img.shields.io/badge/tracked%20Julia-0%20sources-3fb950.svg)](record/julia_migration.md)

This repository is a curated research programme on arithmetic quantum cat maps,
exact finite-field moment reductions and the still-open microscopic
Bohigas–Giannoni–Schmit (BGS) / GOE local-statistics problem.

The central editorial rule is:

> **Preserve scientific provenance, but trust only what the current tree can
> derive, recompute, formalize or explicitly label as open.**

The historical workspace was much larger than the maintained project. The
current branch intentionally contains no duplicate archive source tree and no
Julia source files; old bytes remain recoverable from Git history and the
original research snapshot.

![Research pipeline](assets/research_pipeline.svg)

## Status at a glance — 2026-09-03

| Layer | Status | What is currently justified |
|---|---|---|
| Pair-key parametrization | **EXACT** | off-diagonal bijection, inverse formulas, diagonal multiplicity `p-2` |
| `k=2` and finite `k=4` counts | **EXACT / FINITE-CERTIFICATE** | symbolic count plus independent finite Python/C++/Lean checks |
| Fourth-moment distribution `B(t)` | **EXACT** | corrected coupling decomposition and Fourier identities |
| Cayley mixed term | **EXACT / FINITE-CERTIFICATE** | additive-energy reduction, complete audited `E_11`, `E_13`, generic/exceptional controls |
| `(p,K)=(461,23)` | **FINITE-CERTIFICATE** | energy `1190`, forced baseline `902`, excess `288` |
| Off/off elliptic organization | **DRAFT** | promising non-isotrivial elliptic pencil; sheaf/isogeny obligations remain |
| Finite GOE comparisons | **NUMERICAL** | descriptive spacing/window diagnostics only |
| Microscopic BGS/GOE local law | **OPEN** | no proved comparison/local-law bridge for the structured arithmetic family |

The repository-wide status authority is
[`record/claim_ledger.md`](record/claim_ledger.md). If a historical theorem
name, `PASS`, or old note disagrees with that ledger, the ledger wins.

## The exact chain

Let `p` be an odd prime and `H <= F_p^*` a multiplicative subgroup of order
`K`. For admissible ordered pairs `x,y in F_p \ {0,1}`, define

```text
u = x/y,
v = (x-1)/(y-1),
d = x-y.
```

Off the diagonal `x != y`, the map is bijective onto
`u,v in F_p^* \ {1}`, `u != v`, with

```text
y = (1-v)/(u-v),
x = u(1-v)/(u-v),
d = (u-1)(v-1)/(v-u).
```

The entire diagonal collapses to the key `(1,1)` with multiplicity `p-2`.
That multiplicity is load-bearing: an older proof route effectively treated
the diagonal as if it were generic and produced a false M1 claim.

For the corrected fourth-moment difference distribution,

```text
B(t) = O(t) + 2(p-2) C_H(t) + (p-2)^2 1_{t=0},
```

and the total coupled count is

```text
|V4| = (K^2+1)p^2 - (6K^2+3K)p + 13K^2 - 3K.
```

Character orthogonality turns the fourth-moment character sum into the finite
Fourier transform of `B`. If `V = sum_t B(t)` and `Z=B(0)`, then

```text
E_{q != 0} Sigma4(q) = (p Z - V)/(p-1),
Var_{q != 0} Sigma4(q) = p Var_{t != 0} B(t).
```

These are finite identities, not independence heuristics.

### Cayley transform and the fixed-K obstruction structure

With

```text
c(h) = (h+1)/(h-1),
d(u,v) = 2/(c(u)-c(v)),
c(h^-1) = -c(h),
```

the mixed term becomes a nonzero additive-difference energy of
`A=c(H\{1})`. The exact matching audit classifies all `6! = 720` integer
systems as:

```text
rank 2:  30
rank 3: 240
rank 4: 450
```

and finds no extra rank-drop characteristic except `2`.

For the two subgroup orders whose resultant enumeration is fully audited in
the maintained project,

```text
E_11 = {23, 67, 89}
E_13 = {53, 79, 131, 157, 313}.
```

This is a **fixed-K statement**. It is deliberately not extrapolated uniformly
as `K` grows.

The most useful negative control is

```text
(p,K) = (461,23)
observed mixed collision energy = 1190
forced central-symmetry baseline = 902
excess = 288.
```

That one finite example prevents a false “the generic formula is uniform in
K” narrative.

For the full derivation, read
[`mathematics/fourth_moment_reduction.md`](mathematics/fourth_moment_reduction.md)
then
[`mathematics/cayley_additive_energy.md`](mathematics/cayley_additive_energy.md).

## What is not proved

The off/off remainder has a strong elliptic-family organization, but the target

```text
O(K^2 p + K^4 sqrt(p) + K^4)
```

remains a theorem draft. A publication-grade proof still has to close the
projective/Weierstrass model, bad fibers, twists and isogeny exclusions,
geometric irreducibility/monodromy, conductor control, ramification,
deleted-point/boundary bookkeeping, and the exact hypotheses of the
trace-sheaf correlation theorem actually used.

Even completing that estimate would **not** prove microscopic BGS statistics.
The next bridge must identify and control the relevant local spectral object
(resolvent/comparison/cumulant/Dyson-flow or an arithmetic replacement) for
the deterministic structured family. Quantum ergodicity results in the
literature are important context but are not interchangeable with a local
eigenphase-spacing theorem.

See [`mathematics/elliptic_pencil.md`](mathematics/elliptic_pencil.md),
[`mathematics/open_questions.md`](mathematics/open_questions.md), and
[`literature/frontier_2026.md`](literature/frontier_2026.md).

## Independent verification stack

![Verification stack](assets/verification_stack.svg)

The same finite facts are intentionally attacked from different directions:

| Tool | Role | Load-bearing checks |
|---|---|---|
| Python | transparent reference/symbolic layer | pair-key anchors, 720 matching audit, exact resultants, twisted-Jacobi regressions |
| C++20 | independent exact/exhaustive kernels | fourth-moment pair keys, Cayley energies, cat-map order |
| Lean 4 | kernel-checked finite propositions | pair-key counts, Cayley generic/exceptional controls, torus facts, historical falsifier |
| TeX + CI | scientific integration | manuscript compiles and whole-tree provenance/structure gates stay green |

The point is independent failure modes, not language diversity for its own
sake.

## Reproduce the maintained project

### Python gates

```bash
python -m pip install -r requirements.txt

python computations/verification/repository_audit.py
python computations/verification/current_regression.py
python computations/verification/mixed_cayley_energy.py
python computations/verification/twisted_jacobi_regression.py
python computations/analysis/spectral_diagnostics.py quick
```

A much slower full preserved `N=3571` q-curve regression is available as

```bash
python computations/verification/twisted_jacobi_regression.py --full-curves
```

and is intentionally not required on every CI run.

### C++20

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build -j

./build/fourth_moment_pair_key_verifier
./build/cat_map_order verify
./build/cayley_energy_verifier
```

### Lean 4

```bash
cd formalization
lake build
```

Every active Lean module must be imported by `formalization/Bgs.lean`.
CI checks exact coverage; an unimported `.lean` file cannot quietly sit in the
active formalization tree.

### Manuscript

```bash
cd manuscript
latexmk -pdf -interaction=nonstopmode -halt-on-error arithmetic_cat_map_moments.tex
```

The TeX source and committed PDF live together. The dedicated manuscript
workflow rebuilds the PDF reproducibly and avoids pushing a stale generated PDF
if `main` advances during the job.

## Repository map

```text
.
├── assets/          README diagrams
├── computations/   maintained Python/C++ and verification/analysis entry points
├── evidence/       promoted certificates, numerical records, minimal reference inputs
├── formalization/  active Lean 4 finite certificates/falsifiers
├── literature/     curated bibliography and current frontier notes
├── manuscript/     one active article: TeX + synchronized PDF
├── mathematics/    authoritative derivations and open proof obligations
└── record/         compact claim/retraction/reconstruction/migration provenance
```

There is deliberately **no** second workspace under `record/`. The last
pre-cleanup tree containing the curated historical corpus is identified in
[`record/reconstruction.md`](record/reconstruction.md), and all original
historical bytes remain reachable from Git history.

## Evidence discipline

`evidence/` contains promoted evidence, not a bag of old outputs.

- `certificates/` contains exact finite certificates or finite implementation
  regressions with a maintained producer.
- `numerical/` contains descriptive floating-point diagnostics only.
- `reference/` contains the minimal preserved inputs required by a maintained
  regression.

The spacing diagnostic reports an empirical CDF sup-distance to the GOE Wigner
surmise. It does **not** attach textbook IID-KS significance because unfolded
and pooled gaps are dependent.

The historical “number variance” computation is retained only with its literal
meaning: forward windows are anchored at eigenvalues and edge-truncated. The
current name is **matched forward-window count variance**; it is not stationary
`Sigma^2(L)` and carries no inferential two-sigma verdict.

See [`evidence/README.md`](evidence/README.md) and
[`evidence/provenance.md`](evidence/provenance.md).

## Languages and migration policy

The current branch contains:

- C++20 for exact hot paths and independent exhaustive checks;
- Python for symbolic/reference/orchestration/numerical work;
- Lean 4 for meaningful formal finite certificates;
- TeX for the article;
- **zero tracked Julia source files**.

The supplied historical snapshot had 31 Julia paths (23 byte-distinct
sources). They were reviewed one by one. Useful logic was either replaced by a
maintained C++/Python implementation or had already served as a historical
regression/falsifier; false or duplicate algorithms were **not** mechanically
ported just to inflate C++ line count.

The path-complete disposition is
[`record/julia_migration.md`](record/julia_migration.md).

## Onboarding another researcher

Start in this order:

1. Read [`mathematics/results.md`](mathematics/results.md) and
   [`record/claim_ledger.md`](record/claim_ledger.md). These define what may be
   cited as exact, finite, numerical, draft or open.
2. Run `repository_audit.py`, the exact Python gates, CMake executables, and
   `lake build`.
3. Read [`record/retractions.md`](record/retractions.md) before reviving an old
   proof idea; several superficially attractive routes have concrete known
   failure mechanisms.
4. For M1, work from
   [`mathematics/elliptic_pencil.md`](mathematics/elliptic_pencil.md) and check
   every external theorem hypothesis against the actual family.
5. Treat the microscopic BGS step as a separate problem after M1, not as a
   corollary of moment resemblance.
6. Add a new result only with a derivation, producer/certificate, explicit
   scope and corresponding ledger update.

A new computation should have one canonical maintained producer. Keep an
independent implementation only when it genuinely tests a different failure
mode.

## Current next targets

The highest-value scientific work is:

1. close the projective/fiber/isogeny certificate for the elliptic pencil;
2. pin down a source-exact trace-sheaf correlation theorem and verify all
   geometric hypotheses for this family;
3. only then promote the off/off estimate from **DRAFT**;
4. formulate a concrete M1 → microscopic-local-statistics mechanism and try to
   falsify it on the explicit arithmetic structure before attempting a long
   proof.

The literature notes are intentionally conservative:
[`literature/bibliography.md`](literature/bibliography.md) records what each
source is actually used for, while
[`literature/frontier_2026.md`](literature/frontier_2026.md) separates quantum
ergodicity/eigenfunction results from local eigenphase statistics.

## Provenance and retractions

The project was reconstructed from a 1,100-file research snapshot with many
duplicate files and contradictory historical statuses. The current tree is a
scientific working repository, not a byte-for-byte museum.

- [`record/reconstruction.md`](record/reconstruction.md) records the source
  snapshot hash, inventory statistics and Git preservation boundary.
- [`record/julia_migration.md`](record/julia_migration.md) accounts for every
  historical Julia path.
- [`record/retractions.md`](record/retractions.md) records false/superseded
  routes and why they failed.
- [`record/claim_ledger.md`](record/claim_ledger.md) is the current status
  authority.

If a result cannot survive those four files plus the executable gates, it is
not part of the current claim set.
