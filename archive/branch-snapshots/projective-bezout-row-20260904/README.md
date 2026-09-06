# Arithmetic quantum cat maps — exact reductions and the BGS frontier

[![Scientific verification](https://github.com/ChurilovMaksim/WoW/actions/workflows/ci.yml/badge.svg)](https://github.com/ChurilovMaksim/WoW/actions/workflows/ci.yml)
[![Manuscript PDF](https://img.shields.io/badge/manuscript-PDF-b31b1b.svg)](manuscript/arithmetic_cat_map_moments.pdf)
[![Lean 4](https://img.shields.io/badge/formalization-Lean%204-ffffff.svg)](formalization/)

This repository is a curated research programme on arithmetic quantum cat maps,
exact finite-field moment reductions, and the still-open microscopic
Bohigas--Giannoni--Schmit (BGS) / GOE local-statistics problem.

> **Status discipline.** Historical commits can contain stronger language.
> The current authority is [`record/claim_ledger.md`](record/claim_ledger.md),
> backed by current proofs, source audits and executable regression gates.

![Research pipeline](assets/research_pipeline.svg)

## Status at a glance — 2026-09-04

| Layer | Status | Current statement |
|---|---|---|
| Pair-key geometry | **EXACT** | off-diagonal bijection; diagonal multiplicity `p-2` |
| Fourth-moment distribution | **EXACT** | exact `B(t)` decomposition, total count and Fourier mean/variance |
| Cayley mixed reduction | **EXACT** | mixed collisions are additive energy of `A=c(H\{1})` |
| Direct pointwise Cayley bound | **EXACT + EXTERNAL-THEOREM** | `E_+(A)<34K^(8/3)` for `100<K<p^(3/4)/3` |
| Characteristic-zero additive rigidity | **EXACT** | only identity and central inversion-swap for odd prime `K` |
| Difference discriminant | **EXACT** | one polynomial `S_K` classifies every non-forced split-prime additive collision |
| Ratio-orbit / fourth-power structure | **EXACT** | `Disc(S_K)` has an explicit universal `2,K` part times `J_K^4` |
| Characteristic-zero multiplicative rigidity | **EXACT** | product collisions are only swap/simultaneous inversion |
| Product discriminant | **EXACT** | one polynomial classifies multiplicative split-prime exceptions |
| Global split-prime additive mass | **EXACT** | deterministic `O(K^4)` weighted excess budget |
| Almost-all exact baseline | **EXACT + EXTERNAL-THEOREM** | for fixed `theta<1/5`, density-one split pairs have `Delta_K(p)=0` exactly |
| Full Cayley/Jacobi trace | **EXACT** | `1_Ahat(r)=K Tr M_S(2r)` and exact second/fourth trace moments |
| Double-average quadratic excess | **EXACT + EXTERNAL-THEOREM** | for `theta<1/3`, average `Delta_K(p)/K^2 << X^(3theta-1)` |
| Corrected off/off elliptic layer | **EXACT + EXTERNAL-THEOREM** | reducible spike extracted; variance is controlled by the same `E_+(A)` |
| Sharp pointwise centered energy | **OPEN** | target `(K-1)^4/p+O(K^(2+o(1)))` |
| Microscopic BGS/GOE law | **OPEN** | no mean-spacing local-law/comparison bridge yet |

The concise theorem index is [`mathematics/results.md`](mathematics/results.md).

## Exact fourth-moment reduction

Let `p` be odd and `H<=F_p^*` have order `K`.  For
`x,y in F_p\{0,1}` define

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

The diagonal collapses to `(1,1,0)` with multiplicity `p-2`.  Under the
subgroup constraints the number of admissible off-diagonal ordered pairs is
exactly `(K-1)(K-2)`.

The fourth-moment difference distribution is

```text
B(t)=O(t)+2(p-2)C_H(t)+(p-2)^2 1_{t=0},
```

with exact total

```text
|V4|=(K^2+1)p^2-(6K^2+3K)p+13K^2-3K.
```

If `Sigma4(q)=sum_t B(t)e_p(qt)`, then finite Fourier orthogonality gives

```text
E_{q!=0} Sigma4(q)=(pZ-V)/(p-1),
Var_{q!=0} Sigma4(q)=p Var_{t!=0}B(t).
```

No probabilistic independence assumption enters this reduction.

## One arithmetic bottleneck now controls both mixed and off/off layers

Put

```text
c(h)=(h+1)/(h-1),
A=c(H\{1}).
```

Then

```text
d(u,v)=2/(c(u)-c(v)),
c(h^-1)=-c(h),
```

so the mixed collision problem is the additive energy `E_+(A)`.

The corrected elliptic analysis shows that the pure off/off layer is governed
by the same quantity.  Every generic parameter class has a reducible fiber at

```text
t_lambda=2/(c(h1)-c(h2))
```

with exactly `2p-8` valid affine points.  Those coherent `O(p)` spikes produce
the term `pE_+(A)`.  After their extraction, the remaining rank-two elliptic
trace sheaves are quasi-orthogonal at square-root scale.  The exact corrected
bound is

```text
Var_{t!=0} O(t)
 << pE_+(A)+K^2p+K^4sqrt(p)+K^4.
```

Thus the historical spike-free target `O(K^2p+K^4sqrt(p)+K^4)` is superseded.
See [`mathematics/offoff_elliptic_spike_theorem.md`](mathematics/offoff_elliptic_spike_theorem.md).

The strongest current uniform pointwise Cayley theorem is

```text
E_+(A)<34K^(8/3),
```

for `100<K<p^(3/4)/3`.  Hence in `K=o(p^(1/4))` the corrected off/off variance
is `<<pK^(8/3)`.  The remaining pointwise loss is therefore the same
`K^(2/3)` in both layers.

The sharp closure target is

```text
E_+(A)=(K-1)^4/p+O(K^(2+o(1))),
```

or equivalently

```text
sum_{q!=0}|1_Ahat(q)|^4 << pK^(2+o(1)).
```

## Additive rigidity, canonical discriminant and fourth powers

For odd prime `K`, Chowla's rational independence of the prime-modulus
cotangents gives the complete characteristic-zero additive collision
classification: identity and central inversion-swap are the only relations.
The corresponding forced nonzero baseline is

```text
(K-1)(2K-5).
```

Every cleared collision polynomial satisfies

```text
Res(Phi_K,P)=K^3 M^2.
```

More strongly, the canonical squarefree nonzero-difference polynomial `S_K`
classifies every non-forced split-prime collision:

```text
Delta_K(p)>0  iff  p | Disc(S_K),
Delta_K(p) <= 4 v_p(Disc(S_K)).
```

The polynomial factors into ratio orbits and its discriminant has the exact
shape

```text
|Disc(S_K)|
 =2^((K-1)^4/4)
  K^((K-1)(K^2-7)/4)
  J_K^4.
```

This fourth-power theorem explains the observed split-prime valuation pattern,
but exact larger-`K` cross-resultants show that their total archimedean mass is
genuinely `K^4`-scale.  It is therefore a structural theorem, not a hidden
pointwise proof of the quadratic energy target.

See [`mathematics/cayley_difference_discriminant.md`](mathematics/cayley_difference_discriminant.md)
and [`mathematics/cayley_ratio_orbit_factorization.md`](mathematics/cayley_ratio_orbit_factorization.md).

## Multiplicative rigidity is independently exact

For the characteristic-zero Cayley set, product collisions satisfy only swap
and simultaneous inversion, giving

```text
E_x(A_K)=4(K-1)(K-2).
```

A companion canonical product discriminant classifies all additional split
finite-field product collisions and gives

```text
Delta_K^x(p)>0  iff  p | Disc(S_K^x),
Delta_K^x(p) <= 16 v_p(Disc(S_K^x)).
```

This is useful extra structure, but it does not by itself transfer to the
required additive energy after reduction.  See
[`mathematics/cayley_multiplicative_rigidity.md`](mathematics/cayley_multiplicative_rigidity.md)
and [`mathematics/cayley_product_discriminant.md`](mathematics/cayley_product_discriminant.md).

## Global and almost-all theorems

For odd prime `K`, with

```text
Delta_K(p)=sum_{d!=0}r_{A-A}(d)^2-(K-1)(2K-5),
```

the global resultant argument proves

```text
sum_{p==1 mod K} Delta_K(p) log p
 <=(K^3-5K^2+6K+1)((K-1)log12-3logK).
```

For the dyadic split family

```text
K~X^theta,
p~X,
p==1 mod K,
```

Bombieri--Vinogradov and PNT give two consequences.

1. For fixed `theta<1/3`,

```text
average Delta_K(p)/K^2 <<_theta X^(3theta-1) -> 0.
```

2. Because `Delta_K(p)` is a nonnegative integer, for fixed `theta<1/5` the
proportion of pairs with `Delta_K(p)>0` is

```text
O_theta(X^(5theta-1)) -> 0.
```

Hence asymptotically almost every pair in that smaller range has the exact
energy

```text
E_+(A)=3(K-1)(K-2).
```

See [`mathematics/cayley_jacobi_trace_average.md`](mathematics/cayley_jacobi_trace_average.md)
and [`mathematics/cayley_exact_baseline_density.md`](mathematics/cayley_exact_baseline_density.md).

## Full Jacobi trace identity

Let `S=H^perp` and `J_S(q)` be the full annihilator twisted-Jacobi matrix in the
maintained convention, with

```text
M_S(q)=e_p(-q/2)J_S(q)/(p-1).
```

Then exactly

```text
1_Ahat(r)=K Tr M_S(2r),
```

and therefore

```text
sum_q |Tr M_S(q)|^2 = p(K-1)/K^2,
sum_q |Tr M_S(q)|^4 = pE_+(A)/K^4.
```

The resulting double-average fourth-moment ratio tends to the real-Gaussian
value `3`, but this is **not** a CLT and not a microscopic local-statistics
statement.

## Finite certificates and negative controls

The repository retains exact finite certificates rather than treating them as
proofs of asymptotic statements.  Promoted examples include:

- `E_11={23,67,89}` and `E_13={53,79,131,157,313}` for additive exceptions;
- `(p,K)=(461,23)` with energy `1190`, forced nonzero baseline `902`;
- the Fibonacci slice `Res(Phi_K,X^2+3X+1)=F_K^2`;
- the 28-digit witness `K=131`, `p=F_131`, with excess exactly `32`;
- exact symbolic/finite anchors for the corrected elliptic `2p-8` spike.

## Verification stack

![Verification stack](assets/verification_stack.svg)

The maintained CI runs Python/SymPy exact regressions, independent C++20
verifiers, all active Lean 4 modules, and a fresh TeX manuscript build.
The current Python gates include the additive/product discriminants,
ratio-orbit fourth-power structure and the corrected off/off spike theorem.

Core local reproduction:

```bash
python -m pip install -r requirements.txt
python computations/verification/repository_audit.py
python computations/verification/current_regression.py
python computations/verification/twisted_jacobi_regression.py
python computations/verification/cayley_jacobi_trace_regression.py
python computations/verification/cayley_uniform_cutoff_regression.py
python computations/verification/cayley_resultant_fibonacci.py
python computations/verification/cayley_resultant_mass_budget.py
python computations/verification/cayley_difference_discriminant.py
python computations/verification/cayley_ratio_orbit_factorization.py
python computations/verification/cayley_product_discriminant.py
python computations/verification/offoff_elliptic_spike_regression.py

cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build -j
./build/fourth_moment_pair_key_verifier
./build/cat_map_order verify
./build/cayley_energy_verifier
./build/cayley_fibonacci_verifier
./build/cayley_direct_energy_verifier

cd formalization && lake build
```

## Repository map

```text
.
├── assets/          diagrams
├── computations/   maintained Python/C++ verification and analysis
├── evidence/       promoted certificates, numerical records, reference inputs
├── formalization/  active Lean 4 finite certificates and falsifiers
├── literature/     source map and frontier audit
├── manuscript/     active TeX article and committed PDF
├── mathematics/    authoritative derivations and open obligations
└── record/         claim ledger, retractions and research provenance
```

## What is still genuinely open

The immediate mathematical closure target is the pointwise centered Cayley
energy

```text
E_+(c(H\{1}))=(K-1)^4/p+O(K^(2+o(1))).
```

The current exact Fourier/character, shifted-product, torus--unipotent,
discriminant, multiplicative-rigidity and double-average formulations all
isolate this same gap; none currently removes the `K^(2/3)` pointwise loss.

Even a complete fourth-moment theorem would not prove BGS.  A separate
mean-spacing local eigenphase mechanism is still required.  The literature
boundary is maintained in [`literature/bibliography.md`](literature/bibliography.md)
and [`literature/frontier_2026.md`](literature/frontier_2026.md).
