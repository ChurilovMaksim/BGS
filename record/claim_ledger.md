# Claim ledger

This file is the repository-wide status authority. Historical commits, old
manuscript text, exploratory notes and finite experiments may contain stronger
language; this file wins.

## Status vocabulary

- **EXACT** — current project derivation with explicit hypotheses.
- **EXACT + EXTERNAL-THEOREM** — exact reduction with a verified named theorem as input.
- **FINITE-CERTIFICATE** — exact statement at explicit finite parameters.
- **FINITE-REGRESSION** — implementation/reference agreement; not a growing-parameter proof.
- **NUMERICAL** — descriptive floating-point evidence only.
- **DRAFT** — route with named unresolved obligations.
- **OPEN** — closure condition not achieved.
- **RETRACTED** — false or superseded.

## Critical row-support correction

The dehomogenized projective-row integers `G'_(K,r)^(3)` and
`D'_(K,r)^(3)` are safe **one-way** obstructions only:

```text
I>=3 ==> p|D' ==> p|G'.
```

Their converses are not active because specialization may drop leading degree
at the projective point `mu=infinity`.

The active exact split support is the fixed-degree maximal-real construction
`Lambda_(K,r)^(3)`.  Two specialization-safe scalar reformulations are also
active:

```text
Omega_(K,r)^(3)  from the first three coefficients of the row shift resultant,
Theta_K          from two coefficients of the inverse-ratio pair-sum polynomial.
```

`Lambda`, `Omega`, `Xi` and `Theta` are asserted to have the same relevant
**split rational-prime support** only in the scopes proved below. Equality of
full integers or valuations is not silently assumed.

## Active claim table

| Claim | Status | Current support |
|---|---|---|
| pair-key bijection; diagonal multiplicity `p-2`; exact constrained count `(K-1)(K-2)` | **EXACT + FINITE-CERTIFICATE** | `mathematics/fourth_moment_reduction.md`; Python/C++/Lean |
| exact `|V4|=(K^2+1)p^2-(6K^2+3K)p+13K^2-3K` | **EXACT + FINITE-CERTIFICATE** | fourth-moment note + independent checks |
| corrected `B(t)=O(t)+2(p-2)C_H(t)+(p-2)^2 1_{t=0}` and Fourier mean/variance | **EXACT + FINITE-REGRESSION** | `fourth_moment_reduction.md` |
| Cayley identity and additive-energy reduction for `A=c(H\{1})` | **EXACT** | `cayley_additive_energy.md` |
| prime-order characteristic-zero additive collision rigidity | **EXACT** | Chowla cotangent independence + cross-polytope argument |
| `Res(Phi_K,P)=K^3 M^2`; Fibonacci slice; `(K,p)=(131,F_131)` excess `32` | **EXACT + FINITE-CERTIFICATE** | resultant/Fibonacci notes + Lucas/Python/C++ certificates |
| for `100<K<p^(3/4)/3`, `E_+(A)<34K^(8/3)` | **EXACT + EXTERNAL-THEOREM** | `cayley_direct_energy.md`; Vyugin--Makarychev |
| centered Fourier identity and shifted-energy orbit reductions | **EXACT / EXTERNAL-THEOREM** | centered/shifted Cayley notes; Shkredov input where stated |
| summing shifted-energy orbits alone gives only `O(K^3)` | **EXACT** | exact global identity |
| one unordered pair per fixed-product row/nonzero parameter and exact cross-row excess identity | **EXACT + FINITE-REGRESSION** | `cayley_product_row_intersections.md` |
| `Delta_K(p)<=4 I_K(p)(K-1)(K-2)` | **EXACT** | fixed-product-row identity |
| affine trace equation with `alpha_r=U_(r-1)(tau/2)`, `beta_r=-2U_(r-2)(tau/2)` | **EXACT** | `cayley_product_row_real_trace_ideal.md` |
| dehomogenized `G'` and `D'` order-three invariants | **EXACT, one-way only** | subresultant/coefficient-ideal notes; degree-drop correction |
| fixed-degree real-trace cofactors have gcd degree exactly equal to row-intersection count | **EXACT** | real-trace note |
| split `p|Lambda_(K,r)^(3)` iff some row pair in ratio class `[r]` has `I>=3` | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION** | fixed-degree subresultants + Brown--Traub + Smith gate |
| outside product support `Lambda'_K^(3)`: `I_K<=2`, `Delta<=8(K-1)(K-2)`, `E_+(A)<=11(K-1)(K-2)` | **EXACT + EXTERNAL-THEOREM** | exact support + row-energy identity |
| inverse ratio reflection `Q(T)=-P(2tau-T)` and `I_-1(q)=2 deg gcd(E,O mod q)` | **EXACT + FINITE-REGRESSION** | `cayley_product_row_reflection.md` |
| inverse exact support integer `Xi_K` from the half-degree reflection problem | **EXACT + FINITE-REGRESSION** | reflection note/verifier |
| every characteristic-zero affine intercept fibre has size at most `2`; all double fibres classified | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION** | `cayley_trace_intercept_rigidity.md`; Bass 1966; C++20 regression |
| valid finite row intersections are explicit cyclotomic-unit congruences `W_r(b)=V_r(a) mod q` | **EXACT** | trace-intercept note |
| general row shift-resultant zero order equals row-intersection count | **EXACT + FINITE-REGRESSION** | scalar shift-resultant theorem |
| three-generator `Omega_(K,r)^(3)` has the same split order-three support as `Lambda_(K,r)^(3)` | **EXACT + FINITE-REGRESSION** | shift-resultant/Smith anchors |
| for each fixed ratio, split order-three primes satisfy `sum log p=O(K^3)` | **EXACT** | norm bound for nonzero shift-resultant constant |
| inverse shift resultant factors `R_-(Z)=2^m F(Z/2) S(Z)^2` with `S(Z)=prod_{i<j}(Z-x_i-x_j)` | **EXACT + FINITE-REGRESSION** | `cayley_inverse_pair_sum_factorization.md` |
| inverse `I_-1(q)=2 ord_0 S`; hence `I_-1>=3 iff S(0)=S'(0)=0 mod q` | **EXACT + FINITE-REGRESSION** | pair-sum factorization note/verifier |
| inverse two-scalar contraction `Theta_K=(S(0),S'(0)) cap Z` has the same split order-three support as `Xi_K` / inverse `Lambda` | **EXACT + FINITE-REGRESSION** | pair-sum note + Smith anchors |
| writing `F(X)=E(X^2)+X O(X^2)`, one has `S(0)=+-Res(E,O)` | **EXACT** | pair-sum/reflection resultant identity |
| for `F_Z(X)=F(X+Z/2)=E_Z(X^2)+X O_Z(X^2)`, `S(Z)=+-Res(E_Z,O_Z)` | **EXACT + FINITE-REGRESSION** | translated half-degree resultant theorem |
| inverse order-three support is equivalently simultaneous vanishing of `Res(E,O)` and its translation derivative | **EXACT + FINITE-REGRESSION** | translated resultant theorem + exact anchors |
| polynomial largest-split-divisor bound such as `P_split^+(Lambda'_K^(3))<=K^(4+o(1))` | **OPEN** | sufficient pointwise arithmetic closure target |
| weighted split-prime excess budget is explicit `O(K^4)` | **EXACT + FINITE-REGRESSION** | `cayley_resultant_mass_budget.md` |
| canonical difference discriminant classification and ratio-orbit fourth-power structure | **EXACT + FINITE-REGRESSION** | difference-discriminant / ratio-orbit notes |
| characteristic-zero multiplicative Cayley rigidity and product discriminant classification | **EXACT + FINITE-REGRESSION** | multiplicative notes/verifiers |
| minimal-extension Frobenius amplification: `f=ord_K(p)` divides `Delta_K^ext(p)` and every non-forced orbit has size exactly `f` | **EXACT + FINITE-REGRESSION** | `cayley_frobenius_amplification.md` |
| all-prime minimal-extension weighted budget and discriminant classification | **EXACT + FINITE-REGRESSION** | one-prime-ideal resultant argument |
| unrestricted prime pairs have density-one exact minimal-extension baseline for fixed `theta<1/3` | **EXACT + EXTERNAL-THEOREM** | Frobenius amplification + PNT + Brun--Titchmarsh + divisor bound |
| full ordinary Cayley/Jacobi trace identity and exact second/fourth trace moments | **EXACT + FINITE-REGRESSION** | `cayley_jacobi_trace_average.md` |
| split double-average `Delta/K^2 <<_theta X^(3theta-1)` for `theta<1/3`; full trace kurtosis tends to `3` | **EXACT + EXTERNAL-THEOREM** | mass budget + Bombieri--Vinogradov + PNT |
| density-one exact split baseline for fixed `theta<1/5` | **EXACT + EXTERNAL-THEOREM** | `cayley_exact_baseline_density.md` |
| corrected off/off spike and `Var O << pE_+(A)+K^2p+K^4sqrt(p)+K^4` | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION** | `offoff_elliptic_spike_theorem.md` |
| partition-Mobius formula for distinct-index spectral sums | **EXACT** | `trace_to_local_statistics_bridge.md` |
| exact Poisson/Fourier trace-to-microscopic-statistics identity | **EXACT** | trace-to-local note |
| weighted Heisenberg-scale joint-trace comparison is sufficient for band-limited microscopic RMT correlations | **EXACT** | deterministic comparison theorem |
| uniform high-frequency tail needed to remove Fourier band-limit | **OPEN** | trace-to-local note |
| sharp centered pointwise Cayley target for every intended split design | **OPEN** | closed outside exact order-three support only |
| Heisenberg-scale trace estimates for required desymmetrized spectral blocks | **OPEN** | deterministic bridge closed; arithmetic/spectral estimate not proved |
| microscopic BGS/GOE/COE local eigenphase law | **OPEN** | no current theorem |

## Current split arithmetic obstruction architecture

The fourth-moment bottleneck is the pointwise Cayley energy.  Fixed-product rows
reduce all non-forced excess to row intersections.  The exact split event
`I>=3` now has several compatible specialization-safe descriptions:

```text
fixed-degree real-trace subresultants             -> Lambda,
general scalar shift coefficients c_0,c_1,c_2   -> Omega,
explicit cyclotomic-unit matching W_r/V_r,
inverse reflection gcd(E,O)                      -> Xi,
inverse pair-sum coefficients S(0),S'(0)         -> Theta.
```

For a general ratio,

```text
R_(K,r)(Z)=Res_T(P_1(T),R_r(alpha_r T+beta_r+Z)),
ord_0 R_(K,r)=I_(1,r).
```

For `r=-1`, writing `F(X)=P(tau+X)` gives the stronger exact factorization

```text
R_-(Z)=2^m F(Z/2) S(Z)^2,
S(Z)=prod_(i<j)(Z-x_i-x_j).
```

For split primes `2^mF(0)` is a unit, hence

```text
I_-1=2 ord_0 S,
I_-1>=3 iff S(0)=S'(0)=0.
```

Moreover, with

```text
F_Z(X)=F(X+Z/2)=E_Z(X^2)+X O_Z(X^2),
```

one has

```text
S(Z)=+-Res(E_Z,O_Z).
```

Thus inverse order-three support is the common-divisor problem for a
half-degree resultant and its translation derivative.  Computationally this
reduces the required determinant dimension to `O(K)` and eliminates the
full degree-`m^2` shift resultant.

The next arithmetic closure target is not another individual height bound. It
is a uniform theorem controlling the **common split prime divisors** of these
small scalar systems strongly enough to imply, for example,

```text
P_split^+(Lambda'_K^(3))<=K^(4+o(1)).
```

The existing per-ratio logarithmic mass `O(K^3)` and global `O(K^4)` mass are
not polynomial largest-prime bounds.

## Minimal-extension / Frobenius extension

For every rational prime `p!=2,K`, put

```text
f=ord_K(p), q=p^f, H=mu_K(F_q), A_(K,p)=c(H\{1}).
```

Every non-forced collision Frobenius orbit has size exactly `f`, hence
`f|Delta_K^ext(p)`.  The normalized resultant and canonical discriminant
arguments extend to all such primes.  This yields density-one exact baseline
for unrestricted prime pairs with `K~X^theta`, `p~X` and fixed `theta<1/3`.
It does not improve the split slice, where `f=1`.

## Heisenberg-scale spectral closure

For an `N x N` unitary matrix, partition-lattice Mobius inversion and Poisson
summation give exact formulas expressing microscopic factorial correlations in
terms of joint traces.  In particular,

```text
C_(2,N)(U;phi)
 =N^(-2) sum_m phihat(m/N)(|Tr U^m|^2-N).
```

Compact Fourier support probes `|m|=Theta(N)`.  The Fourier conversion is exact;
the open spectral problem is a weighted Heisenberg-scale joint-trace comparison
for the **correct desymmetrized block**, plus high-frequency tail control for
arbitrary Schwartz tests.

## Adversarial finite controls

- `(K,p)=(29,728017)` and `(31,1042903)` have `p>K^4` but positive excess: bare `p>K^4 => exact baseline` is false.
- `(K,p)=(41,2908049)` has a row pair with two common parameters: `I_K<=1` is false.
- `(K,p)=(31,1303)` has inverse-row intersection size `4`.
- real-trace anchors include `Lambda'_(13,12)=5^2`, `Lambda'_(17,10)=103`, `Lambda'_(23,18)=47^3*139`.
- inverse reflection anchors include `Xi'_13=5`, `Xi'_19=37`, `Xi'_23=47*137`.
- two-scalar inverse anchors are

```text
Theta'_7=1,
Theta'_11=1,
Theta'_13=5,
Theta'_17=1,
Theta'_19=37,
Theta'_23=47^2*137.
```

These agree with `Xi` on split rational-prime support but not necessarily on
valuations.
- independent C++20 characteristic-zero intercept regression reaches prime
  `K=809` in the recorded extended run with maximum fibre size `2` throughout.
- minimal-extension controls remain
  `(K,p,f,Delta)=(7,13,2,32),(11,43,2,128),(13,3,3,432),(13,5,4,496)`.

Finite computation proves only the displayed finite statements.

## Evidence boundaries

- finite regression is not a growing-parameter proof;
- equal split support does not imply equality of `Lambda`, `Omega`, `Xi`, or `Theta` as integers;
- the inverse perfect-square factorization does not by itself bound the largest supported split prime;
- Dvornicich--Zannier remains an unmatched literature lead until its exact congruence hypotheses are verified for the one-prime-ideal setting;
- fourth moments/kurtosis are not a CLT or local eigenvalue law;
- the ordinary full Jacobi trace is not a parity/desymmetrized spectral block;
- the exact trace-to-local-statistics identity does not prove the required Heisenberg-scale trace estimates.

## Retractions and superseded routes

See [`retractions.md`](retractions.md). Historical all-orders Catalan/arcsine
promotion, ESY-to-BGS shortcut, noncommutative trace shortcut, unsupported
higher-rank extrapolations, the former spike-free off/off theorem, the residual
`O(K^3 log K)` height heuristic, and the two-sided geometric interpretation of
dehomogenized `D/G` row ideals are not active.

Microscopic BGS/GOE/COE universality remains open.