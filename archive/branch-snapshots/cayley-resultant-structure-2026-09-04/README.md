# Arithmetic quantum cat maps — exact reductions and the BGS frontier

[![Scientific verification](https://github.com/ChurilovMaksim/WoW/actions/workflows/ci.yml/badge.svg)](https://github.com/ChurilovMaksim/WoW/actions/workflows/ci.yml)
[![Manuscript PDF](https://img.shields.io/badge/manuscript-PDF-b31b1b.svg)](manuscript/arithmetic_cat_map_moments.pdf)
[![Lean 4](https://img.shields.io/badge/formalization-Lean%204-ffffff.svg)](formalization/)
[![Julia](https://img.shields.io/badge/tracked%20Julia-0%20sources-3fb950.svg)](record/julia_migration.md)

This repository is a curated research programme on arithmetic quantum cat maps,
exact finite-field moment reductions and the still-open microscopic
Bohigas–Giannoni–Schmit (BGS) / GOE local-statistics problem.

> **Preserve scientific provenance, but trust only what the current tree can
> derive, recompute, formalize or explicitly label as open.**

The current branch intentionally contains no duplicate archive source tree and
no Julia source files; old bytes remain recoverable from Git history and the
original research snapshot.

![Research pipeline](assets/research_pipeline.svg)

## Status at a glance — 2026-09-04

| Layer | Status | What is currently justified |
|---|---|---|
| Pair-key parametrization | **EXACT** | off-diagonal bijection, inverse formulas, diagonal multiplicity `p-2` |
| constrained `k=2` count / finite `k=4` checks | **EXACT / FINITE-CERTIFICATE** | general `(K-1)(K-2)` count plus independent finite Python/C++/Lean checks |
| Fourth-moment distribution `B(t)` | **EXACT** | corrected coupling decomposition and Fourier identities |
| Cayley mixed-term reduction | **EXACT** | additive-energy formulation and prime-order characteristic-zero collision rigidity |
| Cyclotomic collision resultants | **EXACT / FINITE-REGRESSION** | `Res(Phi_K,P)=K^3 M^2`; stronger square-root cutoff |
| Fibonacci exceptional slice | **EXACT / FINITE-CERTIFICATE** | `Res(Phi_K,X^2+3X+1)=F_K^2`; rational excess `32`; 28-digit `K=131` witness |
| fixed `K=11,13` exceptional sets | **FINITE-CERTIFICATE** | complete audited `E_11`, `E_13` resultants |
| uniform polynomial-scale mixed energy | **OPEN** | zero-collision cutoff is now known to be the wrong target; total energy must be bounded |
| Off/off elliptic organization | **DRAFT** | historical structural evidence; projective/sheaf/isogeny obligations remain |
| Finite GOE comparisons | **NUMERICAL** | regenerated full-Hermitian spacing/window diagnostics only |
| Microscopic BGS/GOE local law | **OPEN** | no proved comparison/local-law bridge for the structured arithmetic family |

The repository-wide status authority is
[`record/claim_ledger.md`](record/claim_ledger.md). If a historical theorem
name, `PASS`, or old note disagrees with that ledger, the ledger wins.

## Exact pair-key/Fourier chain

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

The diagonal collapses to `(1,1)` with multiplicity `p-2`. With subgroup
constraints the off-diagonal count is therefore exactly `(K-1)(K-2)`.

For the corrected fourth-moment difference distribution,

```text
B(t) = O(t) + 2(p-2) C_H(t) + (p-2)^2 1_{t=0},
```

and

```text
|V4| = (K^2+1)p^2 - (6K^2+3K)p + 13K^2 - 3K.
```

Let `S=H^perp`, `m=|S|=(p-1)/K`. Character orthogonality gives

```text
E_{q != 0} Sigma4(q) = (p Z - V)/(p-1),
Var_{q != 0} Sigma4(q) = p Var_{t != 0} B(t).
```

These are finite identities, not independence heuristics.

## Cayley transform: from fixed-K audits to a uniform structural theorem

With

```text
c(h) = (h+1)/(h-1),
d(u,v) = 2/(c(u)-c(v)),
c(h^-1) = -c(h),
```

the mixed term becomes the nonzero additive-difference energy of
`A=c(H\{1})`.

The exact matching audit still supplies useful finite structure:

```text
rank 2:  30
rank 3: 240
rank 4: 450
```

with no extra rank-drop characteristic except `2`, and

```text
E_11 = {23, 67, 89}
E_13 = {53, 79, 131, 157, 313}.
```

The 2026-09-04 route goes substantially further. For odd prime `K`, Chowla's
linear independence of

```text
cot(pi*a/K),  1 <= a <= (K-1)/2,
```

turns the characteristic-zero Cayley set into a rational cross-polytope: the
only equal-difference collisions are identity and central inversion.

For every cleared collision polynomial `P`, one moreover has

```text
P(X) = (X-1)^3 Q(X),
Q(X^-1) = X^(3-T) Q(X),
Res(Phi_K,P) = K^3 M^2,   M in Z.
```

The square comes from twisting `Q(zeta_K)` into the maximal real subfield of
the prime cyclotomic field. Since `||P||_1 <= 12`, a non-forced split prime
must obey

```text
K^3 p^2 <= 12^(K-1).
```

Thus the earlier exponential cutoff is improved by a square root.

Full derivations: [`mathematics/cayley_additive_energy.md`](mathematics/cayley_additive_energy.md)
and [`mathematics/cayley_resultant_structure.md`](mathematics/cayley_resultant_structure.md).

## The Fibonacci slice: a useful obstruction, not just a counterexample

The explicit collision

```text
c(h^2)-c(h) = c(h)-c(h^-1)
```

is equivalent to

```text
h^2 + 3h + 1 = 0.
```

For every odd prime `K`,

```text
Res(Phi_K(X), X^2+3X+1) = F_K^2,
```

so the full cleared collision norm on this slice is `K^3 F_K^2`.  Since
`F_K` grows exponentially, a polynomial bound on the *entire* resultant square
factor is impossible.

But this does **not** make the energy large.  On the quadratic slice,

```text
F_n c(h^n) = L_n c(h),
```

and the rational model is

```text
S_N = { +-L_n/F_n : 1<=n<=N }.
```

Carmichael's primitive-divisor theorem plus a kernel-checked finite residual
give the exact nonzero difference energy

```text
E*(S_N) = 2N(4N-3) + 32,     N>=3.
```

The excess over the centrally symmetric forced baseline is the constant `32`.
This changes the research target: **we need a uniform energy bound, not a
universal theorem forbidding every extra collision.**

### 28-digit exact witness

At

```text
K = 131
p = F_131 = 1066340417491710595814572169
h = 188706367382658195937453923
```

`p` is proved prime by a complete Lucas certificate, `h` has exact order `131`
and satisfies `h^2+3h+1=0 mod p`. Independent Python and C++ arbitrary-
precision implementations give

```text
energy          = 33442
forced baseline = 33410
excess          = 32
max multiplicity= 4
```

This is an exact finite certificate, not an asymptotic theorem.

The older negative control

```text
(p,K)=(461,23): energy=1190, baseline=902, excess=288
```

remains useful because it probes a different, more collision-rich finite
regime.

## What remains open

The immediate mixed-term question is now quantitative: prove a strong uniform
or averaged bound for

```text
sum_t C_H(t)^2
```

for Möbius/Cayley images of multiplicative subgroups at polynomial scale in
`K`. Generic additive-energy theorems cannot simply be cited: the required
exponent must first be propagated through the exact `B(t)` variance identity.

Separately, the off/off remainder still has only a theorem-draft elliptic
organization. The target

```text
O(K^2 p + K^4 sqrt(p) + K^4)
```

requires a current projective model, complete bad-fiber locus, twists/isogeny
classification, geometric irreducibility, conductor/ramification control and
source-exact trace-sheaf correlation hypotheses.

Even completing both moment estimates would **not** prove microscopic BGS.
The local eigenphase law needs a separate comparison/local-law mechanism for
the deterministic structured family.

See [`mathematics/open_questions.md`](mathematics/open_questions.md) and
[`literature/frontier_2026.md`](literature/frontier_2026.md).

## Independent verification stack

![Verification stack](assets/verification_stack.svg)

| Tool | Role | Load-bearing checks |
|---|---|---|
| Python / SymPy | transparent reference and symbolic layer | pair-key anchors, resultants, square-factor audits, Fibonacci primality/energy certificate, spectral diagnostics |
| C++20 | independent exact/exhaustive kernels | pair-key moments, Cayley energy, cat-map order, 28-digit `boost::multiprecision` Fibonacci witness |
| Lean 4 | kernel-checked finite propositions | pair-key counts, fixed Cayley controls, Fibonacci-ratio bounded residual, torus facts, historical falsifier |
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
python computations/verification/cayley_uniform_cutoff_regression.py
python computations/verification/cayley_resultant_fibonacci.py
python computations/verification/twisted_jacobi_regression.py
python computations/analysis/spectral_diagnostics.py verify
```

A slower full preserved `N=3571` q-curve regression is available as

```bash
python computations/verification/twisted_jacobi_regression.py --full-curves
```

and is intentionally not required on every CI run.

### C++20

The arbitrary-precision witness uses Boost.Multiprecision headers (`libboost-dev`
on Ubuntu/Debian).

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build -j

./build/fourth_moment_pair_key_verifier
./build/cat_map_order verify
./build/cayley_energy_verifier
./build/cayley_fibonacci_verifier
```

### Lean 4

```bash
cd formalization
lake build
```

Every active Lean module must be imported by `formalization/Bgs.lean`. CI
checks exact coverage; an unimported `.lean` file cannot quietly sit in the
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
[`record/reconstruction.md`](record/reconstruction.md), and original bytes
remain reachable from Git history.

## Evidence discipline

`evidence/` contains promoted evidence, not a bag of old outputs.

- `certificates/` contains exact finite certificates or finite implementation
  regressions with a maintained producer.
- `numerical/` contains descriptive floating-point diagnostics only.
- `reference/` contains the minimal preserved inputs required by a maintained
  regression.

The finite spectral records remain descriptive only. The maintained producer
diagonalizes the **full complex Hermitian** `M+M^*`; no IID-KS or stationary
number-variance claim is attached to dependent unfolded samples.

See [`evidence/README.md`](evidence/README.md) and
[`evidence/provenance.md`](evidence/provenance.md).

## Languages and migration policy

The current branch contains:

- C++20 for exact hot paths and independent exhaustive/arbitrary-precision checks;
- Python for symbolic/reference/orchestration/numerical work;
- Lean 4 for meaningful formal finite certificates;
- TeX for the article;
- **zero tracked Julia source files**.

The supplied historical snapshot had 31 Julia paths (23 byte-distinct sources).
Useful logic was replaced only where a maintained implementation served a
current scientific role; false or duplicate algorithms were not mechanically
ported merely to change language percentages. The path-complete disposition is
[`record/julia_migration.md`](record/julia_migration.md).

## Onboarding another researcher

Start in this order:

1. Read [`mathematics/results.md`](mathematics/results.md) and
   [`record/claim_ledger.md`](record/claim_ledger.md).
2. Run the exact Python gates, all four C++ executables, and `lake build`.
3. Read [`record/retractions.md`](record/retractions.md) before reviving an old proof route.
4. For the mixed term, read `cayley_additive_energy.md` and
   `cayley_resultant_structure.md`; do not return to a worst-case no-collision
   cutoff without addressing the Fibonacci obstruction.
5. For the off/off term, work from `elliptic_pencil.md` and verify every
   external theorem hypothesis against the actual family.
6. Treat microscopic BGS as a separate closure problem after the moment layer.
7. Promote a result only with a derivation, producer/certificate, explicit
   scope and corresponding ledger update.

## Current next targets

The highest-value scientific work is now:

1. derive the **minimal additive-energy exponent actually needed** for the
   mixed contribution from the exact variance identity;
2. search for and prove the strongest applicable energy/incidence theorem for
   `c(H\{1})`, exploiting multiplicative-subgroup structure rather than merely
   sparse resultant size;
3. close the projective/fiber/isogeny certificate for the off/off elliptic
   pencil and verify a source-exact trace-sheaf correlation theorem;
4. formulate and aggressively falsify a concrete moment → microscopic-local-
   statistics mechanism.

The literature notes are intentionally conservative:
[`literature/bibliography.md`](literature/bibliography.md) records what each
source is actually used for, while
[`literature/frontier_2026.md`](literature/frontier_2026.md) separates quantum
ergodicity/eigenfunction results from local eigenphase statistics.

## Provenance and retractions

The project was reconstructed from a 1,100-file research snapshot with many
duplicate files and contradictory historical statuses. The current tree is a
scientific working repository, not a byte-for-byte museum.

- [`record/reconstruction.md`](record/reconstruction.md) records the preservation boundary.
- [`record/julia_migration.md`](record/julia_migration.md) accounts for every historical Julia path.
- [`record/retractions.md`](record/retractions.md) records false/superseded routes and why they failed.
- [`record/claim_ledger.md`](record/claim_ledger.md) is the current status authority.

If a result cannot survive those files plus the executable gates, it is not
part of the current claim set.
