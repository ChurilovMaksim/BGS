# Claim ledger

This file is the repository-wide status authority. Historical commits, old
manuscript text and exploratory notes may contain stronger claims; this file
wins.

## Status vocabulary

- **EXACT** — current project derivation with explicit hypotheses.
- **EXACT + EXTERNAL-THEOREM** — exact reduction with a verified named theorem as input.
- **FINITE-CERTIFICATE** — exact statement at explicit finite parameters.
- **FINITE-REGRESSION** — implementation/reference agreement; not a growing-parameter proof.
- **NUMERICAL** — descriptive floating-point evidence only.
- **DRAFT** — route with named unresolved obligations.
- **OPEN** — closure condition not achieved.
- **SCOPED-HISTORICAL** — useful result at a narrower safe scope.
- **NOT-PROMOTED** — retained evidence/conjecture, not accepted as theorem.
- **RETRACTED** — false or superseded.

## Critical correction: order-three row support

The dehomogenized projective-row integers `G'_(K,r)^(3)` and
`D'_(K,r)^(3)` are **safe one-way obstructions only**:

```text
I_(i,j)(p)>=3  ==>  p|D'_(K,r)^(3)  ==>  p|G'_(K,r)^(3).
```

Their converses are **not active claims**.  Specialization can make both
dehomogenized row polynomials lose leading degree at `mu=infinity`, causing
low subresultants to vanish without three geometric intersections.  This
failure was found by adversarial specialization at small `K` and is documented
in `mathematics/cayley_product_row_real_trace_ideal.md`.

The active exact geometric support is the maximal-real-field trace ideal
`Lambda'_(K,r)^(3)` defined there.  For every split prime `p==1 mod K`,

```text
p|Lambda'_(K,r)^(3)
iff
some product-row pair in ratio class [r] has at least three common parameters.
```

This correction overrides any older wording that called `D` or `G` the exact
geometric support.

## Active claim table

| Claim | Status | Current support |
|---|---|---|
| pair-key bijection; diagonal multiplicity `p-2` | **EXACT** | `mathematics/fourth_moment_reduction.md` |
| constrained off-diagonal count `(K-1)(K-2)` | **EXACT + FINITE-CERTIFICATE** | pair-key proof + Lean finite certificate |
| exact `|V4|=(K^2+1)p^2-(6K^2+3K)p+13K^2-3K` | **EXACT + FINITE-CERTIFICATE** | Python/C++/Lean checks |
| corrected `B(t)=O(t)+2(p-2)C_H(t)+(p-2)^2 1_{t=0}` and Fourier mean/variance | **EXACT + FINITE-REGRESSION** | `fourth_moment_reduction.md` |
| Cayley identity and additive-energy reduction | **EXACT** | `cayley_additive_energy.md` |
| odd-prime-order characteristic-zero additive collision rigidity | **EXACT** | Chowla cotangent independence + cross-polytope argument |
| `Res(Phi_K,P)=K^3M^2` and exponential exact-baseline cutoff | **EXACT + FINITE-REGRESSION** | `cayley_resultant_structure.md` |
| Fibonacci collision slice and rational excess-32 family | **EXACT + FINITE-CERTIFICATE** | `fibonacci_ratio_energy_proof.md` |
| `(K,p)=(131,F_131)` has excess `32` | **FINITE-CERTIFICATE** | Lucas primality + independent Python/C++ checks |
| for `100<K<p^(3/4)/3`, `E_+(c(H\{1}))<34K^(8/3)` | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION** | `cayley_direct_energy.md`; Vyugin--Makarychev |
| centered Fourier identity and Cayley character/Gram formulations | **EXACT** | `cayley_centered_energy.md` |
| shifted-energy orbit inequality and global lambda identity | **EXACT + FINITE-REGRESSION** | `cayley_shifted_energy_orbits.md` |
| each nonzero shifted-energy orbit has `L^2 << K^2 log K` for `K^2<p` | **EXACT + EXTERNAL-THEOREM** | Shkredov 2015, Theorem 6 |
| summing shifted-energy orbits alone gives only `O(K^3)` | **EXACT** | exact global identity; documented limitation |
| one unordered pair per fixed-product row and nonzero parameter | **EXACT + FINITE-REGRESSION** | `cayley_product_row_intersections.md` |
| exact cross-row excess identity | **EXACT + FINITE-REGRESSION** | same note + generic/exceptional checks |
| `Delta_K(p)<=4 I_K(p)(K-1)(K-2)` | **EXACT** | cross-row identity |
| constrained affine trace equation for row intersections | **EXACT + FINITE-REGRESSION** | `cayley_product_row_intersections.md` |
| normalized coefficients `alpha=U_(r-1)(tau/2)`, `beta=-2U_(r-2)(tau/2)` and sparse `(X-1)^3` relation | **EXACT** | `cayley_product_row_real_trace_ideal.md` |
| `G'` norm-gcd order-three obstruction | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION, one-way only** | `cayley_product_row_subresultants.md` |
| `D'` full-cyclotomic coefficient-ideal obstruction | **EXACT + FINITE-REGRESSION, one-way only** | `cayley_product_row_coefficient_ideal.md`; Smith gate |
| maximal-real trace cofactors have fixed degree and gcd degree exactly equal to row-intersection count | **EXACT** | `cayley_product_row_real_trace_ideal.md` |
| `p|Lambda_(K,r)^(3)` iff some split reduction in ratio class `[r]` has `I>=3` | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION** | real-trace ideal + Brown--Traub + Smith gate |
| if split `p` does not divide `Lambda'_K^(3)`, then `I_K(p)<=2`, `Delta_K(p)<=8(K-1)(K-2)`, `E_+(A)<=11(K-1)(K-2)` | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION** | real-trace ideal + exact row energy |
| bound `P_split^+(Lambda'_K^(3))<=K^(4+o(1))`, or equivalent control of exact order-three split support | **OPEN** | sufficient to close pointwise Cayley target for `K=o(p^(1/4))` |
| weighted split-prime excess budget `sum Delta_K(p)log p = O(K^4)` with explicit constant | **EXACT + FINITE-REGRESSION** | `cayley_resultant_mass_budget.md` |
| canonical difference discriminant classification | **EXACT + FINITE-REGRESSION** | `cayley_difference_discriminant.md` |
| ratio-orbit factorization and fourth-power discriminant theorem | **EXACT + FINITE-REGRESSION** | `cayley_ratio_orbit_factorization.md` |
| characteristic-zero multiplicative Cayley rigidity and product discriminant classification | **EXACT + FINITE-REGRESSION** | multiplicative notes/verifiers |
| full ordinary Jacobi trace identity and exact second/fourth trace moments | **EXACT + FINITE-REGRESSION** | `cayley_jacobi_trace_average.md` |
| double-average `Delta_K(p)/K^2 <<_theta X^(3theta-1)` for `theta<1/3` | **EXACT + EXTERNAL-THEOREM** | mass budget + Bombieri--Vinogradov + PNT |
| full normalized ordinary Jacobi-trace kurtosis tends to `3` in same double average | **EXACT** | exact moments; not a CLT |
| density-one exact baseline for fixed `theta<1/5` | **EXACT + EXTERNAL-THEOREM** | `cayley_exact_baseline_density.md` |
| corrected off/off reducible spike and variance `<<pE_+(A)+K^2p+K^4sqrt(p)+K^4` | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION** | `offoff_elliptic_spike_theorem.md` |
| sharp centered pointwise target for every intended split design | **OPEN** | closed outside exact support `p|Lambda'_K^(3)` |
| microscopic BGS/GOE local eigenphase law | **OPEN** | no mean-spacing local-law/comparison mechanism |

## Current obstruction architecture

The exact fourth-moment decomposition is

```text
B(t)=O(t)+2(p-2)C_H(t)+(p-2)^2 1_{t=0}.
```

Both nontrivial layers are controlled by `E_+(A)` for
`A=c(H\{1})`.  The best unconditional pointwise theorem remains

```text
E_+(A)<34K^(8/3)
```

in the maintained Stepanov range.  The sharp target is quadratic up to
subpolynomial factors.

The fixed-product decomposition isolates all non-forced excess as interference
between distinct product rows.  In the exact real trace coordinate, let

```text
C_K = minimal polynomial of tau=zeta+zeta^(-1),
H_K(T)=(T-2)C_K(T),
P(T)=H_K(T)/(T-tau),
Q_r(T)=H_K(alpha_r T+beta_r)/(T-tau).
```

For split `p!=K` these degree-`m` polynomials remain squarefree/fixed-degree and

```text
deg gcd(P,Q_r mod q)=row intersection count
```

for the embedding `q`.  The coefficient ideal of their first three
subresultants contracts to `Lambda_(K,r)^(3) Z`, giving the exact rational
support of the event `I>=3`.  Thus outside

```text
Lambda'_K^(3)=product_[r] Lambda'_(K,r)^(3)
```

one has

```text
I_K(p)<=2,
Delta_K(p)<=8(K-1)(K-2),
E_+(A)<=11(K-1)(K-2).
```

The remaining arithmetic lemma is the split-divisor bound

```text
P_split^+(Lambda'_K^(3))<=K^(4+o(1)).
```

No proof is known. Generic subgroup-on-curve technology retains the
`K^(2/3)` loss; related bounded Möbius/subgroup intersection statements remain
conjectural, so the special Chebyshev/cyclotomic-unit structure must be used.

## Adversarial finite controls

- `(K,p)=(29,728017)` and `(31,1042903)` have `p>K^4` but excess `48`: bare `p>K^4 => exact baseline` is false.
- `(K,p)=(41,2908049)` has a row pair with two common parameters: `I_K(p)<=1` is false.
- Real-trace exact-support anchors:

```text
Lambda'_(7,2)^(3)=1,
Lambda'_(11,7)^(3)=1,
Lambda'_(13,3)^(3)=1,
Lambda'_(13,12)^(3)=5^2,
Lambda'_(17,10)^(3)=103,
Lambda'_(23,18)^(3)=47^3*139  (extended).
```

`103`, `47`, and `139` are genuinely realized by intersections of size at
least three.  Factors present only in the dehomogenized `D/G` predecessors may
disappear from `Lambda`; this is an intentional removal of degree-drop false
positives.

Complete fixed-order additive certificates remain
`E_11={23,67,89}`, `E_13={53,79,131,157,313}`, and `(p,K)=(461,23)` has
energy `1190` versus baseline `902`.

## Evidence boundaries

- finite computation never proves a growing-parameter theorem;
- fourth-moment/kurtosis control is not a CLT or local eigenvalue law;
- ordinary full trace is not a parity/desymmetrized spectral block;
- multiplicative Cayley rigidity is not silently transferred to additive rigidity.

## Retractions and superseded routes

See [`retractions.md`](retractions.md). Historical Möbius/M4D M1, one-sided
mixed counting, ESY-to-BGS shortcut, noncommutative trace shortcut,
Hecke-centering Julia line, unsupported higher-rank promotion, the spike-free
off/off theorem, the residual `O(K^3 log K)` height heuristic, and the
**two-sided geometric equivalence for dehomogenized `D/G` row ideals** are not
active claims.

Microscopic BGS/GOE universality remains open even if the present fourth-moment
programme is completed.
