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
- **SCOPED-HISTORICAL** — useful result at a narrower safe scope.
- **NOT-PROMOTED** — retained evidence/conjecture, not accepted as theorem.
- **RETRACTED** — false or superseded.

## Critical correction: order-three row support

The dehomogenized projective-row integers `G'_(K,r)^(3)` and
`D'_(K,r)^(3)` are **safe one-way obstructions only**:

```text
I_(i,j)(p)>=3  ==>  p|D'_(K,r)^(3)  ==>  p|G'_(K,r)^(3).
```

Their converses are not active. Specialization can make both dehomogenized row
polynomials lose leading degree at `mu=infinity`, causing low subresultants to
vanish without three geometric intersections.

The active exact geometric support is the fixed-degree maximal-real trace
construction `Lambda'_(K,r)^(3)` from
`mathematics/cayley_product_row_real_trace_ideal.md`. For every split prime
`p==1 mod K`,

```text
p|Lambda'_(K,r)^(3)
iff
some product-row pair in ratio class [r] has at least three common parameters.
```

The scalar shift-resultant construction `Omega_(K,r)^(3)` introduced in
`mathematics/cayley_trace_intercept_rigidity.md` is a second, specialization-safe
exact detector with the **same split rational-prime support**. Equality of the
integers or of non-split valuations is not claimed.

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
| exact cross-row excess identity and `Delta_K(p)<=4 I_K(p)(K-1)(K-2)` | **EXACT + FINITE-REGRESSION** | fixed-product-row note + finite controls |
| constrained affine trace equation with `alpha_r=U_(r-1)(tau/2)`, `beta_r=-2U_(r-2)(tau/2)` | **EXACT** | `cayley_product_row_real_trace_ideal.md` |
| `G'` norm-gcd order-three obstruction | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION, one-way only** | `cayley_product_row_subresultants.md` |
| `D'` full-cyclotomic coefficient-ideal obstruction | **EXACT + FINITE-REGRESSION, one-way only** | `cayley_product_row_coefficient_ideal.md`; Smith gate |
| maximal-real trace cofactors have fixed degree and gcd degree exactly equals row-intersection count | **EXACT** | `cayley_product_row_real_trace_ideal.md` |
| `p|Lambda_(K,r)^(3)` iff some split reduction in ratio class `[r]` has `I>=3` | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION** | real-trace ideal + Brown--Traub + Smith gate |
| inverse ratio `r=-1`: reflection identity, `I_-1(q)=2 deg gcd(E,O mod q)`, exact reduced support `Xi_K` | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION** | `cayley_product_row_reflection.md` |
| prime-order characteristic-zero affine trace-intercept fibres have cardinality at most `2`; inverse doubletons are swaps and non-inverse doubletons are the explicit step-two family | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION** | `cayley_trace_intercept_rigidity.md`; Bass cyclotomic-unit theorem; independent C++20 regression |
| valid row intersections are congruences `W_r(b)==V_r(a) mod q` between explicit products of cyclotomic units | **EXACT** | `cayley_trace_intercept_rigidity.md` |
| shift-resultant zero order equals row-intersection count exactly | **EXACT + FINITE-REGRESSION** | `cayley_trace_intercept_rigidity.md`; SymPy resultant/Smith anchors |
| three-generator ideal `J^shift=(c_0,c_1,c_2)` gives `Omega_(K,r)^(3)` with the same split order-three support as `Lambda_(K,r)^(3)` | **EXACT + FINITE-REGRESSION** | scalar shift-resultant theorem + exact anchors |
| for each fixed ratio, split order-three support has logarithmic mass `sum log p = O(K^3)` | **EXACT** | norm bound for the nonzero shift-resultant constant coefficient |
| if split `p` does not divide `Lambda'_K^(3)` (equiv. the product of scalar split supports), then `I_K(p)<=2`, `Delta_K(p)<=8(K-1)(K-2)`, `E_+(A)<=11(K-1)(K-2)` | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION** | exact row support + row-energy identity |
| bound `P_split^+(Lambda'_K^(3))<=K^(4+o(1))`, or equivalent control of the exact scalar support | **OPEN** | sufficient to close pointwise Cayley target for `K=o(p^(1/4))` |
| weighted split-prime excess budget `sum Delta_K(p)log p = O(K^4)` with explicit constant | **EXACT + FINITE-REGRESSION** | `cayley_resultant_mass_budget.md` |
| minimal-extension Frobenius amplification: `f=ord_K(p)` divides `Delta_K^ext(p)` and every non-forced orbit has size exactly `f` | **EXACT + FINITE-REGRESSION** | `cayley_frobenius_amplification.md`; two independent exact implementations |
| all-prime minimal-extension weighted budget has the same explicit `O(K^4)` bound as the split budget | **EXACT + FINITE-REGRESSION** | one-prime-ideal resultant valuation argument |
| minimal-extension discriminant classification `Delta_K^ext(p)>0 iff p|Disc(S_K)` and `Delta_K^ext(p)<=4v_p(Disc(S_K))` | **EXACT + FINITE-REGRESSION** | `cayley_frobenius_amplification.md` |
| for fixed `theta<1/3`, density-one unrestricted prime pairs `K~X^theta,p~X` have exact baseline in the minimal extension | **EXACT + EXTERNAL-THEOREM** | Frobenius amplification + all-prime budget + PNT + Brun--Titchmarsh + divisor bound |
| canonical difference discriminant classification | **EXACT + FINITE-REGRESSION** | `cayley_difference_discriminant.md` |
| ratio-orbit factorization and fourth-power discriminant theorem | **EXACT + FINITE-REGRESSION** | `cayley_ratio_orbit_factorization.md` |
| characteristic-zero multiplicative Cayley rigidity and product discriminant classification | **EXACT + FINITE-REGRESSION** | multiplicative notes/verifiers |
| full ordinary Jacobi trace identity and exact second/fourth trace moments | **EXACT + FINITE-REGRESSION** | `cayley_jacobi_trace_average.md` |
| double-average `Delta_K(p)/K^2 <<_theta X^(3theta-1)` for split pairs and `theta<1/3` | **EXACT + EXTERNAL-THEOREM** | mass budget + Bombieri--Vinogradov + PNT |
| full normalized ordinary Jacobi-trace kurtosis tends to `3` in same double average | **EXACT** | exact moments; not a CLT |
| density-one exact split baseline for fixed `theta<1/5` | **EXACT + EXTERNAL-THEOREM** | `cayley_exact_baseline_density.md` |
| corrected off/off reducible spike and variance `<<pE_+(A)+K^2p+K^4sqrt(p)+K^4` | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION** | `offoff_elliptic_spike_theorem.md` |
| exact partition-Mobius formula expressing distinct-index spectral exponential sums through products of traces | **EXACT** | `trace_to_local_statistics_bridge.md` |
| exact Poisson/Fourier identity expressing microscopic factorial `k`-point statistics through trace combinations | **EXACT** | `trace_to_local_statistics_bridge.md` |
| weighted Heisenberg-scale joint-trace comparison is sufficient for band-limited microscopic RMT correlations | **EXACT** | deterministic comparison theorem in `trace_to_local_statistics_bridge.md` |
| uniform high-frequency tail needed to remove the Fourier band-limit | **OPEN** | isolated in `trace_to_local_statistics_bridge.md` |
| sharp centered pointwise target for every intended split design | **OPEN** | closed outside exact order-three split support |
| Heisenberg-scale trace estimates for the required desymmetrized quantum-map blocks | **OPEN** | deterministic bridge is exact; spectral estimate not proved |
| microscopic BGS/GOE/COE local eigenphase law | **OPEN** | requires Heisenberg-scale trace comparison, not merely fixed/fourth moments |

## Current split arithmetic obstruction architecture

The exact fourth-moment decomposition is

```text
B(t)=O(t)+2(p-2)C_H(t)+(p-2)^2 1_{t=0}.
```

Both nontrivial layers are controlled by `E_+(A)` for `A=c(H\{1})`. The best
uniform unconditional pointwise theorem remains

```text
E_+(A)<34K^(8/3)
```

in the maintained Stepanov range. The target is quadratic up to subpolynomial
factors.

The fixed-product decomposition isolates all non-forced excess as interference
between distinct product rows. The maximal-real trace cofactors give

```text
deg gcd(P_(K,r),Q_(K,r) mod q)=row intersection count.
```

Their first three fixed-degree subresultants define `Lambda_(K,r)^(3)`. A
second exact encoding uses the scalar shift resultant

```text
R_(K,r)(Z)
 =Res_T(P_1(T),R_r(alpha_r T+beta_r+Z))
 =c_0+c_1 Z+c_2 Z^2+...,
```

for which

```text
ord_(Z=0)(R_(K,r) mod q)=row intersection count,
I>=3  iff  c_0=c_1=c_2=0 mod q.
```

Thus the remaining event is a **simultaneous gcd problem for three explicit
cyclotomic algebraic integers**, not merely a generic subgroup/curve incidence
problem. Equivalently, individual row intersections are congruences

```text
W_r(b)=V_r(a) mod q
```

between explicit products of prime-order cyclotomic units.

The characteristic-zero intercept classification shows that every intercept
fibre has size at most two and explicitly identifies all double fibres. Hence
order-three support is genuinely a finite-reduction phenomenon, not a hidden
characteristic-zero degeneracy.

Outside the product exact support one has

```text
I_K(p)<=2,
Delta_K(p)<=8(K-1)(K-2),
E_+(A)<=11(K-1)(K-2).
```

For each fixed ratio the split order-three primes already satisfy

```text
sum log p = O(K^3),
```

but summing over `O(K)` ratios returns the existing `O(K^4)` global scale. The
open pointwise closure condition remains, for example,

```text
P_split^+(Lambda'_K^(3))<=K^(4+o(1)),
```

or an equivalent largest-prime theorem for the scalar `Omega` support. A
further height estimate on `c_0` alone will not close this; the highest-value
next target is simultaneous arithmetic cancellation/common-factor control for
`c_0,c_1,c_2` or for the explicit cyclotomic-unit matching graph.

For `r=-1`, the reflection identity

```text
Q(T)=-P(2tau-T)
```

halves the fixed-degree problem: after `F(tau+Z)=E(Z^2)+Z O(Z^2)`, exactly

```text
I_-1(q)=2 deg gcd(E,O mod q).
```

This special class has its own exact support integer `Xi_K` and is currently
the most structured individual ratio class.

## Minimal-extension / Frobenius extension

For every rational prime `p!=2,K`, put

```text
f=ord_K(p),
q=p^f,
H=mu_K(F_q),
A_(K,p)=c(H\{1}).
```

Frobenius acts on exponent collision tuples by multiplication by `p` modulo
`K`. No nontrivial power below `f` fixes a tuple, hence every non-forced orbit
has size exactly `f` and

```text
f | Delta_K^ext(p).
```

The normalized resultant argument works at a single prime ideal above `p`, so
the explicit `O(K^4)` weighted collision budget extends from split primes to
all `p!=2,K`; the canonical difference discriminant likewise classifies the
exceptional minimal-extension reductions.

This amplification is invisible in the original split family because
`p==1 mod K` means `f=1`. For unrestricted dyadic prime pairs, however, the
scarcity of small-order residue classes plus the all-prime budget gives a
density-one **exact** baseline for every fixed `theta<1/3`.

## Heisenberg-scale local-statistics closure

For an `N x N` unitary matrix `U`, Mobius inversion on the partition lattice
expresses each distinct-index exponential sum as a finite combination of
products

```text
prod_B Tr U^(sum_(a in B)m_a).
```

Poisson summation then expresses microscopic factorial `k`-point statistics as
weighted sums of these trace combinations. In particular,

```text
C_(2,N)(U;phi)
 =N^(-2) sum_m phihat(m/N)(|Tr U^m|^2-N).
```

A compactly Fourier-supported microscopic test therefore requires trace
information at `|m|=Theta(N)`, the Heisenberg scale. The Fourier conversion is
exact; the open problem is the weighted joint-trace comparison with the target
RMT ensemble for the **correct desymmetrized spectral block**. Arbitrary
Schwartz tests additionally require uniform high-frequency tail control.

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
least three.

- Inverse-row reflection anchors include split support `47` at `K=23`, `59` at
  `K=29`, and `311*1303` at `K=31`; at `(K,p)=(31,1303)` the inverse-row
  intersection has size `4`.
- The independent C++20 characteristic-zero intercept regression checks every
  normalized ratio through the maintained quick range `K<=199`; an extended
  run also checks prime `K=251,307,401,503,601,701,809`. Every fibre has maximum
  size `2` and every doubleton has the predicted exact form. This is regression,
  not the proof.
- Scalar shift-resultant/Smith anchors are

```text
(K,r)=(7,2):   Omega=7^3,                  Omega'=1,
(K,r)=(11,7):  Omega=11^5,                 Omega'=1,
(K,r)=(13,3):  Omega=13^6,                 Omega'=1,
(K,r)=(13,12): Omega=2^4*5^2*13^6,         Omega'=5^2.
```

Their prime-to-`2K` split support agrees with the corresponding `Lambda'`
anchors; full valuation equality is not claimed.
- Minimal-extension regression:

```text
(K,p,f,Delta_K^ext(p))
=(7,13,2,32),
(11,43,2,128),
(13,3,3,432),
(13,5,4,496).
```

Every non-forced Frobenius orbit has size exactly `f` in these checks.
- Complete fixed-order additive certificates remain
  `E_11={23,67,89}`, `E_13={53,79,131,157,313}`; `(p,K)=(461,23)` has energy
  `1190` versus forced baseline `902`.

## Evidence boundaries

- finite computation never proves a growing-parameter theorem;
- the C++ intercept regression verifies the implementation, not Bass's theorem
  or the universal fibre classification;
- the scalar `Omega` and subresultant `Lambda` are asserted to have the same
  **split prime support**, not to be identical integers;
- the per-ratio `O(K^3)` logarithmic support budget does not bound the largest
  supported split prime polynomially;
- Dvornicich--Zannier's modulo-prime root-of-unity theorem is not promoted to
  the current one-prime-ideal problem without checking its exact hypotheses;
- fourth-moment/kurtosis control is not a CLT or local eigenvalue law;
- ordinary full trace is not a parity/desymmetrized spectral block;
- the exact trace-to-local-statistics identity does not prove the required
  Heisenberg-scale trace estimates;
- the minimal-extension Frobenius theorem does not improve the split slice
  where `ord_K(p)=1`;
- multiplicative Cayley rigidity is not silently transferred to additive rigidity.

## Retractions and superseded routes

See [`retractions.md`](retractions.md). Historical Mobius/M4D M1, one-sided
mixed counting, ESY-to-BGS shortcut, noncommutative trace shortcut,
Hecke-centering Julia line, unsupported higher-rank promotion, the spike-free
off/off theorem, the residual `O(K^3 log K)` height heuristic, and the
**two-sided geometric equivalence for dehomogenized `D/G` row ideals** are not
active claims.

Microscopic BGS/GOE/COE universality remains open. The local-statistics Fourier
bridge is exact, so the spectral closure condition is a Heisenberg-scale
joint-trace comparison plus high-frequency tail control when the Fourier
band-limit is removed.