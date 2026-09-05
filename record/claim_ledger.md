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
`Lambda_(K,r)^(3)`. Specialization-safe scalar/local reformulations are also
active:

```text
Omega_(K,r)^(3)  from the first three coefficients of the row shift resultant,
Theta_K          from two coefficients of the inverse-ratio pair-sum polynomial,
J_K^pair          from products of two-generator reduced inverse edge ideals,
J_K^(4)           from products of quartic (e_1,e_3) ideals.
```

`Lambda`, `Omega`, `Xi`, `Theta`, and the inverse local ideals are asserted to
have the same relevant **split rational-prime support** only in the scopes
proved below. Equality of full integers, ideals, or valuations is not silently
assumed.

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
| inverse `I_-1>=3` iff four distinct valid centred roots satisfy `e_1=e_3=0` | **EXACT** | `cayley_inverse_quartic_localization.md` |
| for monic `F` of degree `m`, `Disc(S_F)=Disc(F)^(m-2) Q_F^2`, with `Q_F=prod_(|A|=4)(e_1^3-4e_1e_2+8e_3)` | **EXACT + FINITE-REGRESSION** | pair-sum graph factorization + exact SymPy controls |
| reduced inverse edge equation `2tau-t_a-t_b=(tau-2)(2-v_a-v_b)`, where `v_n=((t_n-2)/(tau-2))` is a square of a real cyclotomic unit | **EXACT** | quartic-localization note |
| products of local two-generator ideals `(w_e,w_f)` over disjoint edges, equivalently quartic `(e_1,e_3)` ideals, have the same split inverse order-three support as `Theta/Xi` | **EXACT + FINITE-REGRESSION** | quartic-localization theorem + exact finite sweep |
| rational `gcd(N(w_e),N(w_f))` is only a candidate filter; same prime ideal / embedding is required | **EXACT + FINITE-CERTIFICATE** | ideal theory + `K=41,p=2908049` negative control |
| for every prime `K>=37`, writing `K=5r+s`, `s=1,2,3,4`, the inverse reduced-edge set contains an explicit pair of disjoint edges whose generators are associates by an explicit real cyclotomic unit; every split divisor of their common norm gives `I_-1>=4` at one embedding | **EXACT + FINITE-REGRESSION** | `cayley_inverse_structural_associates.md`; formal Laurent verifier |
| step-two inverse edges satisfy `w_(a,a+2)=-tau v_(a+1)` and the boundary edge satisfies `w_(0,m-1)=-(tau-1)v_m`; these are unit edges and never contribute finite inverse support | **EXACT + FINITE-REGRESSION** | `cayley_inverse_associate_quotient.md`; exact polynomial anchors |
| quotient inverse edges by `e~f iff w_e/w_f` is a unit; if a split prime divides no contraction `(w_e,w_f) cap Z` from two distinct nonunit associate classes, then all zero edges at one embedding lie in one class and `I_-1<=2B_K` | **EXACT + FINITE-REGRESSION** | `cayley_inverse_associate_quotient.md`; quotient verifier |
| for every `d>=1`, inverse multiplicity satisfies `I_-1=2 deg gcd(E,O)=2 ord_(Z=0) rho(Z)` and `I_-1>=2d` iff some `2d` valid centred roots have `e_1=e_3=...=e_(2d-1)=0` | **EXACT + FINITE-REGRESSION** | `cayley_inverse_even_multiplicity_localization.md`; direct resultant/gcd regression |
| inverse `I_-1>=6` is equivalently three disjoint zero edges, a six-root `e_1=e_3=e_5=0` certificate, `deg gcd(E,O)>=3`, or `rho_0=rho_1=rho_2=0` | **EXACT + FINITE-REGRESSION** | even-multiplicity theorem; exhaustive `K=29,p=59` six-subset control |
| every valid centred inverse root has `x_a=(tau-2)lambda_a` with `lambda_a=v_a-1=eta_(a-1)eta_(a+1)` a real cyclotomic unit | **EXACT + FINITE-REGRESSION** | `cayley_inverse_cyclotomic_unit_normalization.md` |
| a simultaneous `d`-edge inverse event is equivalent away from `K` to `d` Laurent relations at one primitive `K`-th root, each of coefficient `l1`-weight at most `8`; for `d=3` this is a three-generator weight-eight system | **EXACT + FINITE-REGRESSION** | unit-normalization note/verifier; cross-class and large structural controls |
| after removing the polynomial gcd `G` of two inverse edge polynomials, same-embedding support at `q|p` implies `p` divides `|Res(C_K,G) Res(A,B)|`; hence `rad D_(K;e,f)` divides the radical of this reduced scalar filter | **EXACT + FINITE-REGRESSION** | `cayley_inverse_reduced_resultant_filter.md`; exact resultant anchors |
| reciprocal lift `A~(z)=z^deg(A)A(z+z^-1)` satisfies `Res_z(A~,B~)=Res_T(A,B)^2` | **EXACT + FINITE-REGRESSION** | root-product proof + maintained resultant anchors |
| every polynomial factor shared by two distinct valid inverse edge polynomials is torsion / real-cyclotomic | **OPEN** | no counterexample in the exact max-index-50 factor audit; not a growing-index theorem |
| `(K,p)=(59,21713)` is a genuine nonassociate same-embedding event with `(w_(8,26),w_(9,10)) cap Z=21713 Z` | **FINITE-CERTIFICATE** | exact Hermite-normal-form contraction |
| `(K,p)=(89,143207231)` is split inverse support with `I_-1=4` and `p=2.282469... K^4`; therefore a strict finite `p<=K^4` inverse ceiling is false | **FINITE-CERTIFICATE** | independent C++20 + exact reduced-edge norms / same-embedding Python |
| `(K,p)=(229,966684838398077)` is split inverse support with exactly the structural zero edges `(44,91),(48,89)`, `I_-1=4`, and `p=351514.284... K^4` | **FINITE-CERTIFICATE** | exact resultant norms + complete same-embedding finite-field enumeration |
| small-prime split controls `(83,167)` and `(89,179)` have inverse multiplicities `14` and `16`; a global `I_-1=O(1)` statement over all split primes is therefore not the active target | **FINITE-CERTIFICATE** | complete embedding enumeration; both lie outside `K=o(p^(1/4))` |
| polynomial largest-split-divisor bound such as `P_split^+(Lambda'_K^(3))<=K^(4+o(1))` | **OPEN** | correct sufficient route to force `I<=2`, but structurally overstrong in light of universal inverse associate pairs |
| same-embedding row multiplicity `I_K(p)=K^o(1)` (ideally `O(1)`) in the explicit intended regime `K=o(p^(1/4))` | **OPEN** | sufficient via `Delta<=4I_K(K-1)(K-2)` for near-quadratic (respectively quadratic) Cayley excess |
| inverse quotient closure: `B_K=K^o(1)` plus `K^(4+o(1))` control of split divisors of nonassociate cross-class contractions | **OPEN** | sufficient for inverse `I_-1=K^o(1)` in `K=o(p^(1/4))`; general ratios remain open |
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
| sharp centered pointwise Cayley target for every intended split design | **OPEN** | active route is range-explicit multiplicity control rather than eliminating every order-three prime |
| Heisenberg-scale trace estimates for required desymmetrized spectral blocks | **OPEN** | deterministic bridge closed; arithmetic/spectral estimate not proved |
| microscopic BGS/GOE/COE local eigenphase law | **OPEN** | no current theorem |

## Current split arithmetic obstruction architecture

The fourth-moment bottleneck is the pointwise Cayley energy. Fixed-product rows
reduce all non-forced excess to row intersections. The exact split event
`I>=3` now has several compatible specialization-safe descriptions:

```text
fixed-degree real-trace subresultants             -> Lambda,
general scalar shift coefficients c_0,c_1,c_2   -> Omega,
explicit cyclotomic-unit matching W_r/V_r,
inverse reflection gcd(E,O)                      -> Xi,
inverse pair-sum coefficients S(0),S'(0)         -> Theta,
inverse disjoint reduced-edge ideals (w_e,w_f)   -> J^pair,
inverse four-root ideals (e_1,e_3)               -> J^(4).
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

The same event is now localized even further. Two zero pair sums must be
disjoint, so

```text
I_-1>=3
iff four distinct centred roots have e_1=e_3=0
iff some q contains (w_e,w_f) for two disjoint edges.
```

Here

```text
v_n=(t_n-2)/(tau-2),
w_(a,b)=2-v_a-v_b,
2tau-t_a-t_b=(tau-2)w_(a,b),
|N(tau-2)|=K.
```

Thus the ubiquitous `K` factor is removed before the split-prime question and
the remaining generators are sums of squares of real cyclotomic units.

The inverse multiplicity filtration is exact at every even level. If

```text
F(X)=E(X^2)+X O(X^2),
rho(Z)=Res_Y(E_Z,O_Z),
```

then

```text
I_-1=2 deg gcd(E,O)=2 ord_(Z=0) rho(Z).
```

Equivalently, `I_-1>=2d` iff some `2d` valid centred roots have every odd
elementary symmetric function `e_1,e_3,...,e_(2d-1)` equal to zero. In
particular the first threshold not already forced by universal size-two
associate classes is

```text
I_-1>=6
iff three disjoint zero edges
iff six roots satisfy e_1=e_3=e_5=0
iff rho_0=rho_1=rho_2=0.
```

There is also a rootwise cyclotomic-unit normalization

```text
x_a=(tau-2)lambda_a,
lambda_a=v_a-1=eta_(a-1)eta_(a+1) in O^(+x).
```

For one edge, `w_(a,b)=-(lambda_a+lambda_b)`. More economically for sparse
arithmetic, multiplying by the `K`-unit `tau-2` gives

```text
P_(a,b)=t_a+t_b-2tau,
```

which at a primitive `K`-th root is a Laurent relation of coefficient `l1`
weight `8`. Row-subtracting one edge equation from the others keeps every
additional generator at weight at most `8`. Thus `I_-1>=6` is a same-embedding
three-generator weight-eight sparse system.

For two edge polynomials before specializing `T=tau`, write

```text
G=gcd(w_e,w_f) in Z[T],
w_e=G A,
w_f=G B,
gcd(A,B)=1.
```

Then same-embedding support at a prime ideal above `p` forces

```text
p | Res_T(C_K,G) Res_T(A,B).
```

Hence the exact cross-class contraction support is contained in the radical of
this ordinary reduced resultant filter. The reciprocal change of variables
`T=z+z^-1` loses no prime information: for reciprocal lifts one has exactly

```text
Res_z(A~,B~)=Res_T(A,B)^2.
```

Finite exhaustive audits support, but do not prove, the stronger structural
claim that every polynomial factor shared by two distinct inverse edges is a
torsion / real-cyclotomic factor. The development-scale max-index-50 audit is
recorded in `evidence/cayley_inverse_torsion_gcd_audit_20260905.txt` and is not
promoted to a theorem.

There is now an additional characteristic-zero structure. For every prime
`K>=37`, one explicit pair of disjoint inverse edges (depending only on
`K mod 5`) has reduced generators satisfying

```text
w_e = epsilon_K w_f,
epsilon_K in O^(+x),
```

with `epsilon_K` an explicit quotient of four real cyclotomic units. Hence a
split prime ideal dividing one generator automatically divides the other and
creates `I_-1>=4`. Literal elimination of all order-three inverse support is
therefore a structurally overstrong objective.

The inverse problem is now quotient by characteristic-zero association. Write

```text
e~f iff w_e/w_f is a unit,
B_K=max size of a nonunit associate class,
(w_e,w_f) cap Z=D_(K;e,f) Z  for e!~f.
```

Unit edges are support-free. If a split `p` divides no cross-class `D_(K;e,f)`,
then every zero edge at one embedding lies in a single associate class and

```text
I_-1<=2B_K.
```

Thus the active inverse closure separates into

```text
(A) B_K=K^o(1), ideally O(1),
(B) exclude p from cross-class contractions in K=o(p^(1/4)).
```

A sufficient form of (B) is a `K^(4+o(1))` largest-split-divisor bound for the
product of cross-class contractions. This bound is deliberately applied only
after quotienting structural associate classes.

For the full row problem, the intended pointwise arithmetic closure target is
**range-explicit multiplicity**, not mere support:

```text
K=o(p^(1/4)),
I_K(p)=K^o(1),     ideally I_K(p)=O(1).                  (*)
```

By the exact row-energy inequality this yields respectively
`Delta_K(p)=K^(2+o(1))` or `Delta_K(p)=O(K^2)`. The former full-support
largest-split-divisor target remains a logically valid sufficient route to the
stronger statement `I<=2`, but it is no longer the preferred mechanism.

The range restriction is load-bearing: `(K,p)=(83,167)` and `(89,179)` have
inverse multiplicities `14` and `16`, respectively, but lie far outside
`K=o(p^(1/4))`. Conversely the exact `K=139` and `K=229` large-prime
structural witnesses have `I_-1=4` well beyond `K^4`, exactly as the quotient
picture permits.

The existing per-ratio logarithmic mass `O(K^3)` and global `O(K^4)` mass are
not multiplicity bounds. The exact structural witnesses do not settle any
`K^(4+o(1))` asymptotic.

## Minimal-extension / Frobenius extension

For every rational prime `p!=2,K`, put

```text
f=ord_K(p), q=p^f, H=mu_K(F_q), A_(K,p)=c(H\{1}).
```

Every non-forced collision Frobenius orbit has size exactly `f`, hence
`f|Delta_K^ext(p)`. The normalized resultant and canonical discriminant
arguments extend to all such primes. This yields density-one exact baseline
for unrestricted prime pairs with `K~X^theta`, `p~X` and fixed `theta<1/3`.
It does not improve the split slice, where `f=1`.

## Heisenberg-scale spectral closure

For an `N x N` unitary matrix, partition-lattice Mobius inversion and Poisson
summation give exact formulas expressing microscopic factorial correlations in
terms of joint traces. In particular,

```text
C_(2,N)(U;phi)
 =N^(-2) sum_m phihat(m/N)(|Tr U^m|^2-N).
```

Compact Fourier support probes `|m|=Theta(N)`. The Fourier conversion is exact;
the open spectral problem is a weighted Heisenberg-scale joint-trace comparison
for the **correct desymmetrized block**, plus high-frequency tail control for
arbitrary Schwartz tests.

## Adversarial finite controls

- `(K,p)=(29,728017)` and `(31,1042903)` have `p>K^4` but positive excess: bare `p>K^4 => exact baseline` is false.
- `(K,p)=(41,2908049)` has a row pair with two common parameters: `I_K<=1` is false. The same rational prime is also a useful inverse norm-gcd false positive: rational edge norms can share `p` without a common embedding prime.
- `(K,p)=(31,1303)` has inverse-row intersection size `4`; its two zero edges form an additional noncanonical characteristic-zero associate class.
- `(K,p)=(59,21713)` is a nonassociate same-embedding event and calibrates the cross-class contraction problem.
- `(K,p)=(83,167)` and `(89,179)` have inverse intersection sizes `14` and `16`; these are deliberate negative controls against silently dropping the intended large-`p` range.
- `(K,p)=(89,143207231)` has inverse-row intersection size `4` with `p/K^4=2.282469...`; strict finite `p<=K^4` inverse support is false.
- `(K,p)=(139,3596704231)` lies above `K^4` and has exactly the canonical structural pair of zero edges, so `I_-1=4`.
- `(K,p)=(229,966684838398077)` has exactly the structural inverse zero edges `(44,91),(48,89)` in one embedding, so `I_-1=4`, while `p/K^4=351514.284...`.
- at the `K=89` witness, `|N(w_(16,35))|=|N(w_(20,33))|=143207231`, and one split embedding has exactly those two zero pair sums.
- at `K=229`, `|N(w_(44,91))|=|N(w_(48,89))|=33893*966684838398077`; both factors are split modulo `229`.
- `K=29,p=59` has exactly three inverse zero edges at the maximal embedding; all `3003` six-subsets were checked and exactly one satisfies `e_1=e_3=e_5=0`.
- the `K=229,p=966684838398077` structural weight-eight edge relations are indecomposable modulo `p`: no nonempty proper submultiset of the corresponding eight `2K`-th roots vanishes.
- the exact max-index-50 shared-factor audit factored `1225` edge polynomials over `Z[T]`; all `24` irreducible factors repeated across distinct edges had cyclotomic reciprocal lifts (largest encountered cyclotomic order `25`). This is finite evidence only.
- small exact associate-class audits through the recorded conductors find all observed nonunit classes of size `2`, but the four `K mod 5` structural families are not complete; no general `B_K<=2` theorem is claimed.
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
- independent C++20 `K=89` witness verification checks primality, exact subgroup order, distinct trace classes, the two zero pair sums, and the quartic `e_1=e_3=0` certificate.
- the inverse structural-associate verifier checks all four `K mod 5` Laurent identities formally in the affine exponent `r`, exact `K=89`/`K=229` norms, and the complete `K=229` zero-edge witness.
- the inverse associate-quotient verifier checks the unit-edge skeleton, a noncanonical `K=31` associate class, the exact `K=59` cross-class contraction, small-`p` multiplicity controls, and a large-`p` `K=139` structural control.
- the inverse even-multiplicity verifier checks gcd degree, translated-resultant order, odd symmetric invariants, and exhaustive six-subset localization at `K=29,p=59`.
- the inverse cyclotomic-unit verifier checks exact root normalization, weight-eight trace generators, cross-class/associate anchors, and the `K=229` indecomposability control.
- the inverse reduced-resultant verifier exhausts `K=31,37,41,43` polynomial gcds, checks support-free gcd evaluation, exact cross-class/structural resultants, and the reciprocal square identity.
- exact reduced-edge support sweeps completed through the explicitly recorded prime `K=101`; a later interrupted symbolic batch contributes no promoted data.
- minimal-extension controls remain
  `(K,p,f,Delta)=(7,13,2,32),(11,43,2,128),(13,3,3,432),(13,5,4,496)`.

Finite computation proves only the displayed finite statements.

## Evidence boundaries

- finite regression is not a growing-parameter proof;
- equal split support does not imply equality of `Lambda`, `Omega`, `Xi`, `Theta`, or the local ideal products as integers/ideals/valuations;
- `gcd(N(w_e),N(w_f))` does not imply one prime ideal divides both edge elements; same-embedding verification is load-bearing;
- the reduced ordinary resultant is a one-way rational support filter; its extra prime factors need not correspond to the distinguished `K`-cyclotomic embedding;
- for a proved structural associate pair, the same-ideal implication is exact because `(w_e)=(w_f)` as principal ideals, not because their rational norms happen to agree;
- the inverse perfect-square, quartic, weight-eight, or reduced-resultant reformulations do not by themselves bound the largest supported split prime;
- the `K=89` and `K=229` witnesses refute strict finite `K^4` ceilings but do not refute `K^(4+o(1))`;
- the four structural associate families are proved, but completeness of all unit-associate reduced-edge pairs is **not** claimed;
- the torsion classification of every shared edge-polynomial factor is **OPEN** despite the max-index-50 exact audit;
- bounded inverse multiplicity is not asserted uniformly over small split primes; every such target is scoped to the explicit intended regime `K=o(p^(1/4))`;
- the inverse quotient reduction does not solve the other normalized ratio classes;
- Dvornicich--Zannier and Hoechsmann remain unmatched literature leads until their exact hypotheses are verified for the one-prime-ideal / multiplicity setting;
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