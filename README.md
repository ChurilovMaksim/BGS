# Arithmetic quantum cat maps — exact reductions and the BGS frontier

[![Scientific verification](https://github.com/ChurilovMaksim/WoW/actions/workflows/ci.yml/badge.svg)](https://github.com/ChurilovMaksim/WoW/actions/workflows/ci.yml)
[![Manuscript PDF](https://img.shields.io/badge/manuscript-PDF-b31b1b.svg)](manuscript/arithmetic_cat_map_moments.pdf)
[![Lean 4](https://img.shields.io/badge/formalization-Lean%204-ffffff.svg)](formalization/)

This repository is a research programme on arithmetic quantum cat maps, exact
finite-field moment reductions, arithmetic collision geometry and the still
open microscopic Bohigas--Giannoni--Schmit/RMT local-statistics problem.

> **Status discipline.** The repository-wide authority is
> [`record/claim_ledger.md`](record/claim_ledger.md). Historical commits and
> exploratory notes do not override it. The working/reproducibility discipline
> is recorded in
> [`record/research_operating_protocol.md`](record/research_operating_protocol.md).

![Research pipeline](assets/research_pipeline.svg)

## Status at a glance — 5 September 2026

| Layer | Status | Current statement |
|---|---|---|
| Pair-key geometry | **EXACT** | off-diagonal bijection; diagonal multiplicity `p-2` |
| Fourth-moment distribution | **EXACT** | exact `B(t)` decomposition, total count and Fourier mean/variance |
| Cayley mixed reduction | **EXACT** | mixed collisions are additive energy of `A=c(H\{1})` |
| Direct pointwise Cayley bound | **EXACT + EXTERNAL-THEOREM** | `E_+(A)<34K^(8/3)` in the maintained Stepanov range |
| Characteristic-zero additive rigidity | **EXACT** | only identity and central inversion-swap for odd prime `K` |
| Difference discriminant / ratio orbits | **EXACT** | canonical exceptional-prime polynomial; fourth-power discriminant structure |
| Fixed-product rows | **EXACT** | non-forced excess is cross-row interference |
| Exact order-three row support | **EXACT + EXTERNAL-THEOREM** | maximal-real trace ideal `Lambda'_K^(3)` gives the exact split-prime support of `I_K(p)>=3` |
| Pointwise quadratic subfamily | **EXACT + EXTERNAL-THEOREM** | outside `p|Lambda'_K^(3)`, `E_+(A)<=11(K-1)(K-2)` |
| Global split-prime additive mass | **EXACT** | deterministic explicit `O(K^4)` weighted excess budget |
| Split almost-all exact baseline | **EXACT + EXTERNAL-THEOREM** | for fixed `theta<1/5`, density-one split pairs have `Delta_K(p)=0` |
| Minimal-extension Frobenius amplification | **EXACT** | for `f=ord_K(p)`, `f|Delta_K^ext(p)` and every non-forced orbit has size `f` |
| Minimal-extension almost-all exact baseline | **EXACT + EXTERNAL-THEOREM** | unrestricted prime pairs have exact baseline with density one for fixed `theta<1/3` |
| Full Cayley/Jacobi trace | **EXACT** | `1_Ahat(r)=K Tr M_S(2r)` and exact second/fourth trace moments |
| Corrected off/off elliptic layer | **EXACT + EXTERNAL-THEOREM** | reducible spike extracted; variance is controlled by the same `E_+(A)` |
| Trace-to-local-statistics Fourier bridge | **EXACT** | factorial microscopic statistics are exact partition-Mobius/Poisson sums of joint traces |
| Sharp pointwise centered energy | **OPEN** | split-prime target `(K-1)^4/p+O(K^(2+o(1)))` |
| Heisenberg-scale spectral trace comparison | **OPEN** | need joint traces for the correct desymmetrized block at `|n|=Theta(N)` |
| Microscopic BGS/GOE/COE law | **OPEN** | no claimed universality theorem |

The concise theorem index is [`mathematics/results.md`](mathematics/results.md).

## 1. Exact fourth-moment reduction

For odd prime `p`, subgroup `H<=F_p^*` of order `K`, and
`x,y in F_p\{0,1}`, define

```text
u=x/y,
v=(x-1)/(y-1),
d=x-y.
```

Off the diagonal this is a bijection with

```text
y=(1-v)/(u-v),
x=u(1-v)/(u-v),
d=(u-1)(v-1)/(v-u).
```

The diagonal collapses to `(u,v,d)=(1,1,0)` with multiplicity `p-2`, and the
subgroup constraints leave exactly `(K-1)(K-2)` admissible off-diagonal pairs.
The corrected fourth-moment distribution is

```text
B(t)=O(t)+2(p-2)C_H(t)+(p-2)^2 1_{t=0},
```

with

```text
|V4|=(K^2+1)p^2-(6K^2+3K)p+13K^2-3K.
```

Finite Fourier orthogonality gives the exact nonzero-frequency mean/variance
identities. No probabilistic independence assumption enters the reduction.

## 2. One Cayley energy controls both nontrivial fourth-moment layers

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

so the mixed term is governed by additive energy `E_+(A)`. The corrected
off/off analysis finds a coherent reducible fiber of size `2p-8` in every
generic parameter class; after spike extraction the residual elliptic trace
functions are square-root quasi-orthogonal. The maintained bound is

```text
Var_{t!=0} O(t)
 << pE_+(A)+K^2p+K^4sqrt(p)+K^4.
```

The best uniform pointwise theorem currently available is

```text
E_+(A)<34K^(8/3)
```

for `100<K<p^(3/4)/3`. The sharp pointwise split target is

```text
E_+(A)=(K-1)^4/p+O(K^(2+o(1))),
```

or equivalently

```text
sum_{q!=0}|1_Ahat(q)|^4 << pK^(2+o(1)).
```

## 3. Exact row geometry and the current split-prime obstruction

The fixed-product decomposition shows that all non-forced excess comes from
interference between distinct product rows. If `I_K(p)` is the maximum number
of common nonzero Cayley parameters of two distinct rows, then exactly

```text
Delta_K(p)<=4 I_K(p)(K-1)(K-2).
```

The older dehomogenized subresultant integers `G'` and `D'` are retained only
as **one-way** obstructions. An adversarial degree-drop check at the projective
point `mu=infinity` showed that their converses are false.

The exact support is instead described in the maximal real cyclotomic field.
With `tau=zeta+zeta^(-1)`, the normalized row map has Chebyshev coefficients

```text
alpha_r=U_(r-1)(tau/2),
beta_r=-2U_(r-2)(tau/2).
```

The fixed-degree real-trace cofactors have gcd degree exactly equal to the row
intersection count. The coefficient ideal of their first three subresultants
contracts to

```text
Lambda_(K,r)^(3) Z.
```

For split primes,

```text
p|Lambda'_(K,r)^(3)
iff
some row pair in ratio class [r] has at least three common parameters.
```

Therefore outside

```text
Lambda'_K^(3)=product_[r] Lambda'_(K,r)^(3)
```

one has

```text
I_K(p)<=2,
Delta_K(p)<=8(K-1)(K-2),
E_+(A)<=11(K-1)(K-2).
```

The active arithmetic closure problem is

```text
P_split^+(Lambda'_K^(3))<=K^(4+o(1)),
```

or another growing-`K` estimate strong enough to control the exact split
support. Such a theorem would close the pointwise Cayley-energy bottleneck in
`K=o(p^(1/4))`.

See
[`mathematics/cayley_product_row_real_trace_ideal.md`](mathematics/cayley_product_row_real_trace_ideal.md).

## 4. Discriminants, resultants and split-prime averages

Characteristic-zero cotangent rigidity gives the forced nonzero baseline

```text
(K-1)(2K-5),
```

and every maintained cleared collision polynomial satisfies

```text
Res(Phi_K,P)=K^3 M^2.
```

The canonical difference polynomial `S_K` classifies additional split
collisions:

```text
Delta_K(p)>0 iff p|Disc(S_K),
Delta_K(p)<=4v_p(Disc(S_K)).
```

Its ratio-orbit factorization yields

```text
|Disc(S_K)|
 =2^((K-1)^4/4)
  K^((K-1)(K^2-7)/4)
  J_K^4.
```

The total residual archimedean mass genuinely remains `K^4`-scale. The global
weighted collision budget is

```text
sum_{p==1 mod K} Delta_K(p) log p
 <=(K^3-5K^2+6K+1)((K-1)log12-3logK).
```

For prime `K~X^theta`, prime `p~X`, `p==1 mod K`:

```text
average Delta_K(p)/K^2 <<_theta X^(3theta-1) -> 0
```

for fixed `theta<1/3`, while for fixed `theta<1/5` asymptotically almost every
split pair has

```text
Delta_K(p)=0,
E_+(A)=3(K-1)(K-2)
```

exactly.

## 5. Frobenius amplification over minimal finite extensions

The split condition erases a useful symmetry. For arbitrary rational prime
`p!=2,K`, put

```text
f=ord_K(p),
q=p^f,
H=mu_K(F_q),
A_(K,p)=c(H\{1}).
```

Frobenius multiplies every exponent in a collision tuple by `p mod K`. Every
non-forced Frobenius orbit has size exactly `f`, hence

```text
f | Delta_K^ext(p).
```

The collision-resultant valuation argument works at one prime ideal over `p`,
so the same explicit `O(K^4)` weighted budget extends to all `p!=2,K`, and

```text
Delta_K^ext(p)>0 iff p|Disc(S_K),
Delta_K^ext(p)<=4v_p(Disc(S_K)).
```

For unrestricted prime pairs `K~X^theta,p~X`, PNT + Brun--Titchmarsh + the
standard divisor bound show that for every fixed `theta<1/3`, asymptotically
almost every pair has

```text
Delta_K^ext(p)=0,
E_+(A_(K,p))=3(K-1)(K-2)
```

in the minimal extension. This does **not** improve the original split slice,
because split primes have `f=1`.

See
[`mathematics/cayley_frobenius_amplification.md`](mathematics/cayley_frobenius_amplification.md).

## 6. The exact trace-to-local-statistics closure map

For an `N x N` unitary matrix `U`, partition-lattice Mobius inversion expresses
each distinct-index exponential sum exactly as a finite combination of joint
trace products

```text
prod_B Tr U^(sum_(a in B)m_a).
```

Poisson summation then converts microscopic factorial `k`-point statistics into
weighted sums of these combinations. For pair correlation,

```text
C_(2,N)(U;phi)
 =N^(-2) sum_m phihat(m/N)(|Tr U^m|^2-N).
```

Thus a band-limited microscopic test requires trace information through

```text
|m|=Theta(N),
```

the Heisenberg scale. The Fourier bridge is exact; the missing theorem is a
weighted comparison of the **correct desymmetrized spectral-block** joint
traces with the corresponding RMT ensemble. Removing the Fourier band-limit
also requires a uniform high-frequency tail estimate.

This is why a complete fourth-moment theorem would still not, by itself, prove
BGS.

See
[`mathematics/trace_to_local_statistics_bridge.md`](mathematics/trace_to_local_statistics_bridge.md).

## 7. Full Cayley/Jacobi trace identity

For the normalized full annihilator twisted-Jacobi matrix

```text
M_S(q)=e_p(-q/2)J_S(q)/(p-1),
```

one has exactly

```text
1_Ahat(r)=K Tr M_S(2r),
sum_q |Tr M_S(q)|^2=p(K-1)/K^2,
sum_q |Tr M_S(q)|^4=pE_+(A)/K^4.
```

The double-average normalized fourth/second moment ratio tends to the
real-Gaussian value `3`, but this is not a CLT and not a microscopic
local-statistics statement.

## 8. Finite certificates and adversarial controls

Promoted exact finite checks include:

- complete split exceptional sets `E_11={23,67,89}` and
  `E_13={53,79,131,157,313}`;
- `(p,K)=(461,23)` with energy `1190`, forced baseline `902`;
- the Fibonacci slice `Res(Phi_K,X^2+3X+1)=F_K^2`;
- `(K,p)=(131,F_131)` with excess exactly `32`;
- `(K,p)=(29,728017)` and `(31,1042903)` with `p>K^4` but excess `48`,
  falsifying a bare `p>K^4 => exact baseline` rule;
- `(K,p)=(41,2908049)` with a row pair sharing two parameters, falsifying
  `I_K(p)<=1`;
- exact real-trace support anchors including
  `Lambda'_(17,10)^(3)=103` and the extended
  `Lambda'_(23,18)^(3)=47^3*139`;
- minimal-extension controls
  `(K,p,f,Delta)=(7,13,2,32),(11,43,2,128),(13,3,3,432),(13,5,4,496)`,
  with exact Frobenius orbit sizes.

Finite computation proves only the stated finite assertions.

## 9. Verification stack

![Verification stack](assets/verification_stack.svg)

The maintained CI runs exact Python/SymPy regressions, independent C++20
verifiers, all active Lean 4 modules, and a fresh TeX manuscript build.

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
python computations/verification/cayley_frobenius_extension.py
python computations/verification/cayley_difference_discriminant.py
python computations/verification/cayley_ratio_orbit_factorization.py
python computations/verification/cayley_product_row_intersections.py
python computations/verification/cayley_product_row_subresultants.py
python computations/verification/cayley_product_row_coefficient_ideal.py
python computations/verification/cayley_product_row_real_trace_ideal.py
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

Use other languages/tools when they make a computation more reliable or more
efficient; see the repository operating protocol above.

## Repository map

```text
.
├── assets/          reproducible diagrams / visual research artifacts
├── computations/   maintained Python/C++ verification and analysis
├── evidence/       promoted certificates, numerical records, reference inputs
├── formalization/  active Lean 4 certificates and falsifiers
├── literature/     primary-source map and frontier audits
├── manuscript/     active TeX article and committed PDF
├── mathematics/    authoritative derivations and open obligations
└── record/         claim ledger, protocol, retractions and provenance
```

## What is still genuinely open

Two different scales now have precise closure conditions.

**Arithmetic fourth-moment frontier.** Prove the sharp centered Cayley-energy
bound for all intended split designs. The highest-value current route is exact
split support through `Lambda'_K^(3)` plus cyclotomic-unit/Chebyshev structure.

**Microscopic BGS frontier.** Prove the required joint trace estimates at
Heisenberg scale for the correct desymmetrized spectral blocks and control the
high-frequency tail when passing beyond band-limited tests.

Neither target has been silently weakened. Full microscopic BGS/GOE/COE
universality remains **OPEN**.
