# Arithmetic quantum cat maps — exact reductions and the BGS frontier

[![Scientific verification](https://github.com/ChurilovMaksim/WoW/actions/workflows/ci.yml/badge.svg)](https://github.com/ChurilovMaksim/WoW/actions/workflows/ci.yml)
[![Manuscript PDF](https://img.shields.io/badge/manuscript-PDF-b31b1b.svg)](manuscript/arithmetic_cat_map_moments.pdf)
[![Lean 4](https://img.shields.io/badge/formalization-Lean%204-ffffff.svg)](formalization/)
[![Julia](https://img.shields.io/badge/tracked%20Julia-0%20sources-3fb950.svg)](record/julia_migration.md)

This repository is a curated research programme on arithmetic quantum cat maps,
exact finite-field moment reductions, and the still-open microscopic
Bohigas--Giannoni--Schmit (BGS) / GOE local-statistics problem.

> **Preserve provenance, but trust only what the current tree derives,
> recomputes, formalizes, or explicitly labels as open.**

![Research pipeline](assets/research_pipeline.svg)

## Status at a glance — 2026-09-04

| Layer | Status | Current statement |
|---|---|---|
| Pair-key geometry | **EXACT** | off-diagonal bijection; diagonal multiplicity `p-2` |
| Fourth-moment distribution | **EXACT** | corrected `B(t)` decomposition, total count, Fourier identities |
| Cayley mixed reduction | **EXACT** | mixed collisions are additive energy of `c(H\{1})` |
| Prime-order characteristic-zero collisions | **EXACT** | only identity and central inversion, by Chowla cotangent independence |
| Collision resultants | **EXACT / FINITE-REGRESSION** | `Res(Phi_K,P)=K^3 M^2`; improved exponential no-collision cutoff |
| Fibonacci slice | **EXACT / FINITE-CERTIFICATE** | `Res(Phi_K,X^2+3X+1)=F_K^2`; rational excess `32`; 28-digit witness |
| Direct polynomial-scale mixed energy | **EXACT / FINITE-REGRESSION** | `E_+(c(H\{1}))<34K^(8/3)` for `100<K<p^(3/4)/3` |
| Split-prime non-forced mass | **EXACT / FINITE-REGRESSION** | explicit `O(K^4)` weighted budget over all `p==1 mod K` for odd prime `K` |
| Sharp centered mixed energy | **OPEN** | target `E_+(A)=(K-1)^4/p+O(K^(2+o(1)))` |
| Off/off elliptic correlation | **DRAFT** | projective/sheaf/isogeny obligations remain |
| GOE finite diagnostics | **NUMERICAL** | descriptive full-Hermitian diagnostics only |
| Microscopic BGS/GOE law | **OPEN** | no local-law/comparison bridge for this arithmetic family |

The repository-wide authority for claim status is
[`record/claim_ledger.md`](record/claim_ledger.md). The concise theorem index is
[`mathematics/results.md`](mathematics/results.md).

## Exact pair-key/Fourier chain

Let `p` be odd and `H<=F_p^*` have order `K`. For
`x,y in F_p\{0,1}`, set

```text
u=x/y,
v=(x-1)/(y-1),
d=x-y.
```

Off the diagonal this is a bijection onto
`u,v in F_p^*\{1}`, `u!=v`, with

```text
y=(1-v)/(u-v),
x=u(1-v)/(u-v),
d=(u-1)(v-1)/(v-u).
```

The diagonal collapses to `(1,1,0)` with multiplicity `p-2`, and the subgroup
constraints give the exact off-diagonal count `(K-1)(K-2)`.

For the corrected fourth-moment distribution,

```text
B(t)=O(t)+2(p-2)C_H(t)+(p-2)^2 1_{t=0},
```

```text
|V4|=(K^2+1)p^2-(6K^2+3K)p+13K^2-3K.
```

With `S=H^perp`, `m=(p-1)/K`, and
`Sigma4(q)=sum_t B(t)e_p(qt)`, finite Fourier orthogonality gives

```text
E_{q!=0} Sigma4(q)=(pZ-V)/(p-1),
Var_{q!=0} Sigma4(q)=p Var_{t!=0} B(t).
```

No probabilistic independence assumption enters this reduction.

## Cayley transform and arithmetic rigidity

Put

```text
c(h)=(h+1)/(h-1).
```

Then

```text
d(u,v)=2/(c(u)-c(v)),
c(h^-1)=-c(h).
```

Hence the mixed term is the nonzero additive-difference energy of

```text
A=c(H\{1}),   |A|=K-1,   A=-A.
```

For odd prime `K`, Chowla's rational independence of

```text
cot(pi*a/K), 1<=a<K/2,
```

turns the characteristic-zero Cayley set into a rational cross-polytope. The
only equal-difference collisions are identity and central inversion.

For every cleared prime-order collision polynomial `P`, the project proves

```text
P(X)=(X-1)^3 Q(X),
Q(X^-1)=X^(3-T)Q(X),
Res(Phi_K,P)=K^3 M^2.
```

Thus a non-forced split prime must satisfy

```text
K^3 p^2 <= 12^(K-1).
```

This is exact but remains an exponential worst-case obstruction.

## Fibonacci slice: why zero-collision is the wrong target

The collision

```text
c(h^2)-c(h)=c(h)-c(h^-1)
```

is equivalent to

```text
h^2+3h+1=0.
```

For every odd prime `K`,

```text
Res(Phi_K(X),X^2+3X+1)=F_K^2.
```

So the full cleared norm is `K^3F_K^2`, genuinely exponential in `K`; a
polynomial bound on every collision resultant is impossible.

Nevertheless the corresponding rational model

```text
S_N={+-L_n/F_n:1<=n<=N}
```

has exact nonzero difference energy

```text
E*(S_N)=2N(4N-3)+32,   N>=3.
```

At the exact finite-field design

```text
K=131,
p=F_131=1066340417491710595814572169,
```

a complete Lucas primality certificate plus independent Python/C++
computations gives

```text
mixed energy    = 33442
forced baseline = 33410
excess          = 32
max multiplicity= 4
```

Large exceptional primes therefore need not cause large total collision
energy.

## Direct polynomial-scale mixed theorem

The sum fiber of the Cayley image is unexpectedly simple:

```text
c(x)+c(y)=t
```

is equivalent to

```text
P_t(x,y)=(2-t)xy+t(x+y)-(2+t)=0.
```

For a bilinear polynomial `axy+bx+cy+d`, reducibility over the algebraic closure
is equivalent to `ad-bc=0`. Here

```text
ad-bc=-4,
```

so every fiber is absolutely irreducible in odd characteristic.

A source-exact application of Vyugin--Makarychev Theorem 2 then gives, for

```text
100<K<p^(3/4)/3,
```

and `t notin {0,-2}`,

```text
r_{A+A}(t)<=32K^(2/3).
```

The exceptional fibers satisfy `r(0)=K-1` and `r(-2)<=K-1`; hence

```text
E_+(A)<34K^(8/3),
sum_t C_H(t)^2<34K^(8/3).
```

After propagating the exact mixed coefficient `2(p-2)` through the fourth-
moment variance normalization,

```text
Var_{t!=0}(2(p-2)C_H(t))<136pK^(8/3).
```

This is a genuine uniform polynomial-scale theorem. It applies to every
subgroup in the stated range, including cyclotomic/Fibonacci exceptional
reductions, and does not use the resultant cutoff.

Full proof and source audit:
[`mathematics/cayley_direct_energy.md`](mathematics/cayley_direct_energy.md).

## Centered energy: the remaining pointwise exponent gap

For every `A subset F_p`, with unnormalized additive Fourier transform,

```text
E_+(A)=|A|^4/p+(1/p)sum_{q!=0}|1_Ahat(q)|^4.
```

The density term is unavoidable, so the correct sharp target is

```text
E_+(A)=(K-1)^4/p+O(K^(2+o(1))),
```

or equivalently

```text
sum_{q!=0}|1_Ahat(q)|^4 << pK^(2+o(1)).
```

For the Cayley image, letting `S=H^perp`, `m=(p-1)/K`, and
`y=(h-1)^(-1)`, the project derives exactly

```text
1_Ahat(q)=e_p(q)/m * sum_{chi in S} T_chi(q),
T_chi(q)=sum_{y!=0,-1} chi((y+1)/y)e_p(2qy).
```

The character family has exact Gram matrix

```text
sum_q T_chi(q) conjugate(T_eta(q))
  = p(p-2),  chi=eta,
  = -p,      chi!=eta.
```

The same problem is an intersection problem with a one-parameter unipotent
PGL2 family:

```text
r_{A-A}(t)=#{h in H\{1}:u_t(h) in H\{1}},
u_t(h)=((2-t)h+t)/(2+t-th).
```

No verified theorem currently removes the remaining `K^(2/3)` pointwise loss.
See [`mathematics/cayley_centered_energy.md`](mathematics/cayley_centered_energy.md).

## Global split-prime collision-mass theorem

For odd prime subgroup order `K`, simultaneous exponent scaling partitions all
non-forced collision quadruples into exactly

```text
N_K=K^3-5K^2+6K+1
```

free Galois orbits. If

```text
Delta_K(p)=sum_{d!=0}r_{A-A}(d)^2-(K-1)(2K-5)
```

for split primes `p==1 mod K`, common-root counting inside each normalized
orbit, together with `Res(Phi_K,P)=K^3M^2` and
`|Res(Phi_K,P)|<=12^(K-1)`, gives

```text
sum_{p==1 mod K} Delta_K(p) log p
 <= (K^3-5K^2+6K+1)((K-1)log12-3logK).
```

Thus all non-forced collision mass over all split rational primes has an
explicit deterministic `O(K^4)` logarithmic budget, with immediate tail and
sparsity corollaries. This is an average/sparsity theorem, not a pointwise
replacement for the centered-energy target.

Full proof and exact `K=11,13` regression:
[`mathematics/cayley_resultant_mass_budget.md`](mathematics/cayley_resultant_mass_budget.md).

## Off/off and microscopic BGS remain separate gaps

The off/off term is organized historically by a genus-one/elliptic pencil. The
conditional target is

```text
O(K^2p+K^4sqrt(p)+K^4),
```

with intended regime `K=o(p^(1/4))`. A publication-grade proof still needs the
actual smooth projective model, complete bad-fiber locus, boundary corrections,
twists/isogenies, geometric irreducibility, conductor/ramification control, and
exact trace-sheaf correlation hypotheses.

Even closing both mixed and off/off moment estimates would **not** prove
microscopic BGS. The local eigenphase law requires a separate arithmetic or
comparison/local-law mechanism at mean-spacing scale.

## Independent verification stack

![Verification stack](assets/verification_stack.svg)

| Tool | Role |
|---|---|
| Python / SymPy | transparent exact reference, symbolic algebra, resultants, Galois-orbit/valuation regressions, finite certificates, numerical diagnostics |
| C++20 | independent exact/exhaustive hot paths, including direct Cayley-energy and 28-digit multiprecision verifiers |
| Lean 4 | kernel-checked finite pair-key/Cayley/Fibonacci residual statements and historical falsifiers |
| TeX + CI | publication-facing integration and independent manuscript build |

### Reproduce the maintained gates

```bash
python -m pip install -r requirements.txt
python computations/verification/repository_audit.py
python computations/verification/current_regression.py
python computations/verification/mixed_cayley_energy.py
python computations/verification/cayley_uniform_cutoff_regression.py
python computations/verification/cayley_resultant_fibonacci.py
python computations/verification/cayley_resultant_mass_budget.py
python computations/verification/twisted_jacobi_regression.py
python computations/analysis/spectral_diagnostics.py verify

cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build -j
./build/fourth_moment_pair_key_verifier
./build/cat_map_order verify
./build/cayley_energy_verifier
./build/cayley_fibonacci_verifier
./build/cayley_direct_energy_verifier

cd formalization && lake build
```

The slower full preserved `N=3571` q-curve regression is available via

```bash
python computations/verification/twisted_jacobi_regression.py --full-curves
```

and is intentionally not required on every CI run.

## Repository map

```text
.
├── assets/          README diagrams
├── computations/   maintained Python/C++ verification and analysis
├── evidence/       promoted certificates, numerical records, reference inputs
├── formalization/  active Lean 4 finite certificates/falsifiers
├── literature/     theorem-source map and current frontier notes
├── manuscript/     active TeX article + synchronized PDF
├── mathematics/    authoritative derivations and open obligations
└── record/         claim/retraction/research-route/reconstruction/migration provenance
```

The current tree contains zero Julia source files. Historical bytes remain in
Git history; false or duplicate algorithms were not mechanically ported merely
to change language percentages.

## Onboarding another researcher

1. Read `mathematics/results.md` and `record/claim_ledger.md`.
2. Run the Python/C++/Lean gates above.
3. Read `record/retractions.md` before reviving historical proof routes.
4. For the mixed term, read `cayley_direct_energy.md`,
   `cayley_centered_energy.md`, and `cayley_resultant_mass_budget.md`.
5. For off/off, start from `mathematics/elliptic_pencil.md` and re-check every
   external theorem hypothesis against the actual family.
6. Treat microscopic BGS as a separate closure problem after the moment layer.

## Highest-value next targets

1. improve the proved mixed bound from `K^(8/3)` toward the centered quadratic
   scale using the exact character-family or torus--unipotent structure;
2. combine the global resultant mass budget with a source-exact count of split
   primes only in ranges where the required varying-modulus uniformity is
   actually proved;
3. close the projective/fiber/isogeny/sheaf certificate for the off/off elliptic
   pencil;
4. formulate and falsify a concrete moment-to-microscopic-local-statistics
   mechanism rather than assuming moments imply BGS.

The literature map is intentionally conservative:
[`literature/bibliography.md`](literature/bibliography.md) records exactly what
sources are used for, while [`literature/frontier_2026.md`](literature/frontier_2026.md)
separates quantum ergodicity/eigenfunction results from local eigenphase
statistics.
