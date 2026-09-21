# Claim ledger

## 21 September 2026 — recovered 14--16 September Heisenberg layer

The earlier BGS working dossiers were reread against the later raw-Weyl and
source-audit corrections.  Only claims surviving that chronology are promoted.

| Claim | Status | Boundary / authority |
|---|---|---|
| Frozen raw-modular map: exact microhop bound, all-near error below `0.145^m`, long-near-run suppression, and multiscale escape to at least `(tau_0/26)N^(1-epsilon)` bulk visits | **PROJECT PROOF + FRESH EXACT/FINITE REGRESSION** | `mathematics/fixed_map_weyl_path_escape.md`; structural path theorem, not signed bulk cancellation |
| Encounter support kernel satisfies `rank_F(B_P)>=s(P)/25` over every field | **EXACT COMBINATORIAL + FRESH FINITE REGRESSION** | induced-matching minor with determinant plus/minus one; same note |
| Every q-only kick for the project cat has an exact antiunitary reversor at every odd N | **EXACT** | `mathematics/one_shear_antiunitary_no_go.md`; rules out the one-shear fallback as a CUE route |
| On `N=19^k`, `ord_N(S)=20*19^(k-1)` and primitive orbit phases obey exact Parseval | **EXACT + FRESH FINITE REGRESSION** | `mathematics/hyperbolic_19adic_dephasing.md` |
| Primitive 19-adic hyperbolic incomplete sums are `O(N^(2/3) log N)` for intervals of length at most N | **PROJECT PROOF + EXTERNAL-THEOREM + FRESH FINITE REGRESSION** | Cluckers arXiv:1001.2013 Prop. 3.3 plus explicit finite-type reduction |
| v9 two-frequency Bourgain incomplete-sum theorem and sliding-variable BCD2 corollary | **RETRACTED** | cited source did not imply the required uniform single incomplete-sum estimate |
| Deterministic final-map “CUE contraction sector” has already been evaluated as `min(m,N)` | **OPEN / HISTORICAL OVERCLAIM** | the CUE reference value is correct; the required deterministic sub-sum decomposition/evaluation was not derived |

## 21 September 2026 — recovered fixed-map continuation

The statements below were recovered from the final conversation handoff,
hash-audited, and their supplied Python checks were freshly rerun.  “Project
proof” is not external referee acceptance; finite replay is not an asymptotic
proof and does not promote the fixed-(\tau) BGS target.

| Claim | Status | Boundary / authority |
|---|---|---|
| Correct ordinary-midpoint symbol for the raw frozen generator; resulting (G_\kappa=S\circ\Phi_g^\kappa) has only power (C^1) commuters, no (C^1) reversor, and no relevant affine (C^1) conjugacy for (0<\operatorname{abs}(\kappa)\le10^{-12}) | **PROJECT PROOF + FRESH FINITE-REGRESSION** | `mathematics/fixed_model_symmetry_theorem.md`; does not exclude quantum (N)-dependent symmetries |
| Odd-Pell full-symbol Gaussian crossover, exact variance (1650797/4000000), and necessary ( \operatorname{abs}(\epsilon_K)\sqrt K\to\infty) for CUE pair behaviour in that family | **PROJECT PROOF + FRESH FINITE-REGRESSION** | `mathematics/fixed_model_pell_crossover.md`; frozen strength is outside the proved bounded window |
| Exact moment inequalities, stronger first-two-level interval, repeated-clock one-upper-loop falsifier, and growing perturbation RMS transfer | **EXACT IDENTITIES / PROJECT ASYMPTOTIC CONSEQUENCES + FRESH REGRESSION** | `mathematics/fixed_map_moment_control_and_transfer.md` |
| Three-orientation residual decay implies the explicit (1/64) differential lower barrier for (L_N(s)) | **CONDITIONAL PROJECT THEOREM + FRESH FINITE-REGRESSION** | `mathematics/three_orientation_resolvent_barrier.md`; hypotheses unproved for frozen (U_N) |
| Fourier-line resonance coercivity with sharp (\kappa_\beta), exact (\kappa_1=\sqrt{(T-2)/(T+2)}), and (H^{3/2}) positivity for trace magnitude at least 6 | **PROJECT PROOF + FRESH EXACT REGRESSION** | `mathematics/fourier_line_resonance_coercivity.md`; arbitrary two-dimensional analytic symbols remain open |
| Strict-minimum local polynomial with nonzero bracket that is nevertheless a polynomial coboundary | **EXACT LOCAL CONSTRUCTION + FRESH SYMBOLIC REGRESSION** | `mathematics/local_jet_resonance_obstruction.md`; not a periodic torus counterexample |
| Microscopic BGS / fixed-(\tau) mixed-resolvent or Heisenberg joint-trace estimate | **OPEN** | none of the recovered continuation results supplies this estimate |

This file is the repository-wide status authority. Historical commits, old
manuscript text, exploratory notes and finite experiments may contain stronger
language; this file wins.

## Fixed-map update, 20 September 2026

The [current fixed-map chapter](../mathematics/fixed_map_resolvent_frontier.md)
and [indexed supplement](../supplement/fixed_map/README.md) integrate the
previously unpublished work without promoting its open hypotheses.

| Claim | Status | Boundary |
|---|---|---|
| Cotangent mixed-loop and Brownian identities | EXACT | Finite unitary spectra; not residual decay |
| Full normalized mixed hierarchy implies compact all-order anchored correlations | EXACT + EXTERNAL-THEOREM | Bourgade--Huang v2, Theorem 1.9; whole-space moments; model hypothesis OPEN |
| First two mixed levels imply the stated interval for subsequential pair limits | EXACT, conditional | Vanishing residuals unproved; interval does not identify CUE |
| Microscopic RMS preservation forces global CUE entropy/N to diverge | EXACT | Global comparison only; local methods not excluded |
| Algebraic-return and block-memory results | Scoped project proofs | Read exact hypotheses and finite/shrinking-coupling distinctions in the supplement |
| Fixed-coupling BGS at tau=10^-80 | OPEN | No Heisenberg-scale mixed cancellation estimate |
| New Lean kernels | Source formalization pending current build | Integer algebra only; no analytic BGS formalization |

The [publication review](fixed_map_publication_20260920.md) records the
actual verification scope. Dated snapshot statements about earlier
nonpublication and old execution states are historical provenance.

## Recovered amendments, 20 September 2026

Self-review of a previously uncommitted workspace patch; see
[recovery audit](recovery_audit_20260920.md). The newer fixed-map work above
and the positive-measure bandlimit extension remain authoritative.

| Claim | Status | Boundary |
|---|---|---|
| Largest split divisor bound K^(4+o(1)) excludes exceptional primes | Correct only with a fixed power margin | K<=p^(1/4-epsilon), fixed epsilon>0; does not imply the full little-o regime |
| Separated-cluster averaged form-factor estimate (H8) | PROJECT PROOF + SELF-REVIEW + FINITE-REGRESSION | Odd K>=3, D=Kn, phase radius <=1/(4K); finite unitary spectra |
| Compensated-family window mean (H9) equals (d_N/K)(1+o(1)) | CONDITIONAL ON PROJECT PARENT ESTIMATE + SELF-REVIEW | Inversion-even C7 symbol, epsilon=o(N^(1/3)), specified Pell subsequence; vanishing classical strength |
| Matching traces for 0<abs(m)<N/2 does not determine pair statistics | EXACT COUNTEREXAMPLE | Even N; clock versus doubled half-clock; abstract spectra |
| Elliptic monodromy argument and weight conventions | SOURCE-DEPENDENT CLARIFICATION | BLV v2 arithmetic image plus commutators; purity on the lisse locus, bounded omitted stalks |

These recoveries do not prove fixed-coupling BGS. No new Lean build is claimed.

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
| actual kicked Pell propagator at $\epsilon=\tau/\sqrt{2K}$: all fixed return traces converge in $L^2$ over harmonic windows to the cycle-pair diagram series | **EXACT** | `mathematics/pell_harmonic_returns.md`, Theorem 1; fixed $m,\tau$, full odd space, global law |
| return-law endpoints are wrapped normal and free unitary Brownian; second-return closed formula for $\beta\ge1/6$ | **EXACT + EXTERNAL-THEOREM** | same note (R4)--(R5); moments derived internally, conventional free Brownian identification uses Demni (1) |
| full nonzero lifted-aggregate Bessel weight is $O_{m,\tau}(K^{-1})$ | **EXACT** | same note Lemma 2, cyclic integer image and $\ell^1$ dominance; no growing-$m$ phase theorem |
| finite return-diagram, cyclic-lattice, circle-clique and independent matrix controls | **FINITE-CERTIFICATE + FINITE-REGRESSION** | `evidence/certificates/pell_harmonic_returns_20260910/`; exact checks separated from floating approximation |
| fixed Pell cat map, unit harmonics up to $L=N^{\beta+o(1)}\le\sqrt N$: all fixed compressed-observable moments converge in $L^2$ to circle-graphon moments, uniformly over odd eigenspaces | **EXACT** | `mathematics/pell_harmonic_transition.md`, Theorem 1; sampled harmonics, global observable law only |
| harmonic law has fourth moment $3-2\beta$, explicit sixth moment, weak continuity, and unbounded support for $\beta<1/2$ with semicircle endpoint | **EXACT** | same note, (H6), (H18)--(H19), Corollary 4; no finite-size edge rigidity |
| harmonic weighted ordered quantum moments have graphon limits; complementary normalized half-window commutator squared norm tends to $8\beta(1-\beta)$ | **EXACT** | same note, (H20)--(H21); tracial convergence, no measurement path or BGS claim |
| physical harmonic $a$ produces magnetic parameter $a^2q_0$; 192324 finite oriented word checks and 36 numerical independent spectral comparisons | **FINITE-CERTIFICATE + FINITE-REGRESSION** | `evidence/certificates/pell_harmonic_transition_20260909/`; exact algebra and floating matrix results separated |
| scalar Cayley trace `d_Kol<=C((K-1)^(-1/2)+sqrt((K-1)/log p))`; dyadic rate `O(Q^(-1/2)+sqrt(log Q/log X))` outside fraction `O((log X)X^(-1/4))` for large `Q<=X^(1/4)` | **EXACT + EXTERNAL-THEOREM** | `mathematics/cayley_trace_gaussian_limit.md`, Section 7; Esseen smoothing; constants unoptimized |
| all-order weighted Cayley collision budget `sum_p Delta_w(p) log p = O_w(K^r)` for prime `K`, split primes `p`, and a fixed positive integer word of length `r>=1` | **EXACT + EXTERNAL-THEOREM** | `mathematics/cayley_trace_gaussian_limit.md`, Proposition 3; Chowla input |
| normalized full Cayley--Jacobi trace: joint independent Gaussian limit at fixed distinct positive parameter multipliers for `K->infinity`, `K=o(log p)` | **EXACT + EXTERNAL-THEOREM** | same note, Theorem 1; not traces of matrix powers |
| same joint empirical laws converge weakly in probability over dyadic split designs with `Q->infinity`, `log Q=o(log X)` | **EXACT + EXTERNAL-THEOREM** | same note, Theorem 2; Bombieri--Vinogradov/PNT; does not cover fixed `Q=X^theta` |
| `(K,p)=(11,199)` has `Z4=B4=270` but `Z3=6`, `Z6-B6=1350` | **FINITE-CERTIFICATE** | exact integer convolution in `computations/verification/cayley_higher_moments.py` |
| pair-key bijection; diagonal multiplicity `p-2`; exact constrained count `(K-1)(K-2)` | **EXACT + FINITE-CERTIFICATE** | `mathematics/fourth_moment_reduction.md`; Python/C++/Lean |
| exact `card(V4)=(K^2+1)p^2-(6K^2+3K)p+13K^2-3K` | **EXACT + FINITE-CERTIFICATE** | fourth-moment note + independent checks |
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
| split `p divides Lambda_(K,r)^(3)` iff some row pair in ratio class `[r]` has `I>=3` | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION** | fixed-degree subresultants + Brown--Traub + Smith gate |
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
| all-bandwidth comparison extends to every Schwartz correlation test under positive normalized spectral averages and a reference Schwartz limit | **EXACT** | `bandlimited_correlation_extension.md`; corrected 2026-09-08; no separate tail hypothesis |
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
for the **correct desymmetrized block** at every compact Fourier support.
For positive normalized averages with a reference Schwartz limit, extension to
arbitrary Schwartz correlation tests follows from the translated-cube bound
in `bandlimited_correlation_extension.md` (correction, 2026-09-08).

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

## Magnetic-quotient claims (2026-09-05)

| Claim | Status | Boundary |
|---|---|---|
| Explicit antiunitary and Gauss real gauge | Exact project proof, finite numerical cross-checks | Does not establish GOE universality |
| Signed orbit assembly and all-order Weyl trace identity | Exact project proof; independent Python/C++ histograms | Reference enumeration remains exponential in moment order |
| Reciprocal short-relation rigidity | Proved for prime K, m<K, p^2>m^(K-1) | No polynomial-regime extension asserted |
| Quantitative moment bound and global semicircle law | Complete project derivation, not externally refereed; prime K=o(log p) | Not microscopic BGS; priority not established |
| Fixed-map scope obstruction | Exact growth argument | This regime cannot occur for orders of one fixed hyperbolic integral map |
| Lean magnetic trace checks | Four finite native_decide certificates; compiler execution recorded separately by CI | Not an analytic formalization |
| Triple-resultant filters of draft PR #13 | Necessary divisibility survives; exactness of every triple gcd is false | K=43,p=173 gives 865=5p |

Proof authority for these additions is `mathematics/magnetic_quotient_semicircle.md`.
The earlier ledger remains in force outside these explicitly delimited additions.

## Pell Floquet continuation, 2026-09-05

Proof authority: `mathematics/pell_floquet_normal_form.md`. The argument is
self-contained and does not assume completion of the earlier arithmetic
programme. Status: project theorem with proof, awaiting independent review;
no priority or complete analytic Lean formalization is claimed.

- Exact cyclic cohomological inverse and weighted phase bound
  sum |c_j| a_j <= 2 pi/[K(1-lambda^(-K))].
- Exact four-letter pair-support dissociation for odd prime K>=11 and
  composite Pell N; exact full-HS commutator formula, bounded by 9/K.
- Actual kicked-propagator normal form with odd normalized HS error
  <=12 epsilon^2/sqrt(K), valid for all real epsilon.
- Critical wrapped Gaussian law for U_epsilon^K at epsilon=tau/sqrt(2K).
  The comparison error is 6|m|tau^2/sqrt(K); the additional Gaussian
  characteristic-function error is only asserted to be o(1).
- Subcritical folded-phase W2 limit under epsilon sqrt(K)->0; no statement
  that the old clusters remain separate or keep identifiable ranks.
- Independent C++/Python finite checks and finite/general-algebraic Lean
  kernels are recorded at their own scope, not promoted to the full limit.
- Gamma decimal corrected to 5.614220692151198071627965... and now enclosed
  by a pure-integer interval certificate. Three legacy K=7,p=29 anchors
  corrected with negative controls and explicit positive embeddings.

Not established: Heisenberg-scale joint traces, microscopic local statistics,
fixed nonzero classical-kick universality, or full BGS. K is logarithmic in N
and the critical classical kick is of order 1/(N sqrt(K)).

## Compact-test microscopic obstruction in the Pell family

Section 7 of `mathematics/pell_floquet_normal_form.md` proves a negative
microscopic consequence under global mean-density unfolding of the complete
odd space. For every fixed L and finite nonzero tau=lim epsilon sqrt(2K),
liminf C_d(phi_L)>=Theta(tau)-1/L and liminf Var N_L>=L^2(Theta(tau)-1),
where Theta(tau)=sum_m exp(-m^2 tau^2)>1. Subcritical tau->0 gives divergence
of every such fixed-L pair statistic. Therefore a bounded clustering pair
limit requires |epsilon|sqrt(K)->infinity. Compact tests avoid any hidden
Schwartz-tail assumption. No sufficient condition for positive universality,
no density-adapted unfolding result, and no further-sector result is claimed.
The forty finite configurations are checked independently by pair sums and
moving-window integration; they are evidence about implementation, not the
proof. Priority and analytic Lean formalization are not established.

## Temporal hierarchy and spectral modules (2026-09-06)

Proof authority: `manuscript/unified_sections/temporal_resonance.tex`,
`manuscript/unified_sections/spectral_modules.tex`, and `cayley_scaling.tex`.
These are complete project derivations with the displayed hypotheses, not
independent referee acceptance, established priority, or full Lean proofs.
They supersede the old finite-band nondegeneracy open status only.

| Claim | Status | Boundary |
|---|---|---|
| All finite-lag h_r={g,C^r g}/(4 pi) independent modulo L2 coboundaries for every real nonconstant Fourier polynomial | EXACT + FINITE-REGRESSION | Both trace signs, arbitrary finite phases/support |
| Full quadratic temporal cancellation iff all lag-diagonal sums vanish; explicit transfer | EXACT + FINITE-REGRESSION | Finite combinations |
| Reciprocal-filter cancellation and autocorrelation classification | EXACT + FINITE-REGRESSION | Second-order classes, not quantum spectra |
| Positive fixed-band coercivity and Gevrey stretched-exponential upper bound | EXACT | Not arbitrary infinite analytic support |
| All h_r free over C[z,z^-1]; all-frequency spectral positivity; Riesz bounds uniform in time window | EXACT + FINITE-REGRESSION | Constants depend on the largest lag and fixed symbol |
| Every finite Fourier symbol has an exact high-lag pair-orbit Gram formula and Toeplitz comparison | EXACT + FINITE-REGRESSION | Sufficiently large fixed starting lag; classical covariance |
| High-lag smallest eigenvalue Theta(n^(-2M)) classified by common orbit-filter divisor on hyperbolic circles | EXACT + FINITE-REGRESSION | General Toeplitz zero-order mechanism is prior theory |
| One-harmonic repair of the q-filter family has uniform crossover (n^(-2q)+epsilon^2)^2 | EXACT | Fixed A,q,v and sufficiently large starting lag; not kicked BGS |
| Complementary separate filters remove common soft zeros | EXACT + FINITE-REGRESSION | Sum of separate covariance matrices, not covariance of their sum |
| No-alias physical-Weyl HS variance lower bound | EXACT + NUMERICAL | Sufficient window logarithmic |
| Regular semisimple finite quantum cyclic module with exact all-time variance | EXACT + FINITE-REGRESSION + NUMERICAL | Odd order with arbitrary nonzero c; observable commutators, not eigenphase correlations |
| Balanced phase extends exact orthogonality/all-time formula to even order | EXACT + FINITE-REGRESSION + NUMERICAL | c=a+ib, a^2=b^2>0; correct modular-centred Weyl convention |
| Even-order phase-rank transition: K(K-2)/2 for ab!=0, K(K-2)/8 for nonzero pure real/imaginary c | EXACT + FINITE-REGRESSION | Finite commutator-observable module, not spectral universality |
| Cayley scaling classes are inversion pairs; unimodular toric classes have at most four members | EXACT + FINITE-REGRESSION | No energy-exponent improvement |

Python and independent C++ witness sources are now supplied, and the previously
dangling Fourier-tail reference points to a maintained proof. The Lean draft
is outside active imports until compiler execution is verified. Exact integer
checks, floating-point diagnostics, analytic proofs, and remote CI are separate
evidence categories. The all-time finite-field statement does not furnish
joint traces of a perturbed quantum propagator. Positive microscopic BGS /
GOE / COE / GUE universality remains OPEN.


## Holomorphic shell rigidity and spectral resolution

The intervening Wiener, control, and polynomial-shell results and their
corrections are recorded in `continuation_review_20260906.md`. The following
entries extend the polynomial-shell branch, not the BGS universality claim.
Proofs are included in the single canonical manuscript.

| Claim | Status | Boundary |
|---|---|---|
| Rank-r holomorphic kernels have positive product-curve contacts of total multiplicity at most r-1 | EXACT + FINITE-REGRESSION | Centred bidisk, finite separated rank, positive product constants |
| Two holomorphic maps to C^d are identified up to one unitary by 2d total shell/normal-jet conditions | EXACT + FINITE-REGRESSION | Whole interior spheres, centre included; no rationality or degree assumption |
| 2d-1 prescribed conditions do not suffice, including mixed repeated-shell allocations | EXACT + FINITE-REGRESSION | Sharp in one complex dimension; nonpolynomial entire examples included |
| Scalar two-circle uniqueness | PRIOR THEOREM | Perez, arXiv:2009.02061v2, Theorem 2.2; not claimed as new |
| Punctured-domain scalar functions agree in intensity on infinitely many shells without a constant phase | EXACT + NUMERICAL | Analytic theta construction; numerical checks are diagnostics only |
| Bounded disk-holomorphic pairs have no degree-uniform Holder intensity-recovery estimate from two circles | EXACT + FINITE-REGRESSION | Explicit polynomial sequence; norms bounded above and below; no measurement lower bound assumed |
| Any uniform modulus is at least c exp(-C sqrt(log(1/delta))) | EXACT | Lower bound only; a matching upper rate is OPEN |
| Simple clock spectra agree on all traces below N/2 but have different microscopic spacing laws | EXACT + FINITE-REGRESSION | Abstract unitary negative control, not chaotic dynamics |
| Spectral rounding preserves O(1/N) Egorov while producing collapsed spacings, including a simple-spectrum variant | EXACT | Weak quantization axioms only; no fixed microlocal symbol-class assertion |

Fresh execution coverage, exact source hashes, literature attribution and the
limited PDF build scope are in `holomorphic_shell_review.md` and
`../evidence/certificates/holomorphic_shell_review.json`. These entries do not
assert external priority, full-repository referee acceptance, Lean compilation,
or successful cloud CI. Positive microscopic BGS universality remains OPEN.


## Bosonic Husimi-shell application

Proof authority: `manuscript/unified_sections/husimi_shell_tomography.tex`,
using the finite-rank holomorphic contact theorem above. The Hilbert space is
not truncated. Each sphere carries ideal complete angular data.

| Claim | Status | Boundary |
|---|---|---|
| Ranks a and b are distinguished by a+b total complete shell/normal-jet conditions in any finite number of bosonic modes | EXACT | No photon cutoff; ideal continuum data, not finite-copy sample complexity |
| Any 2r circles give rank-r completeness; normalized Laguerre mixtures show 2r-1 can fail at trace distance one | EXACT + FINITE-REGRESSION | Sharp universal guarantee over radius choices; not failure at every prescribed design |
| Rank-r strict completeness does not follow: ranks r and r+1 can agree on 2r circles | EXACT + FINITE-REGRESSION | Unknown competitor rank is a different tomography problem |
| No finite set of coherent-state projectors identifies every pure state without a cutoff | EXACT + FINITE-REGRESSION | Infinite-dimensional orthogonal-complement construction |
| Without an energy bound, bounded-region Husimi data have no uniform trace-distance inverse modulus | EXACT | Orthogonal number-state sequence |
| Fixed mean energy restores uniform continuity on rank-bounded states, but not a Holder modulus even with a measured intensity floor | EXACT + FINITE-REGRESSION | Explicit pure-state pairs; modulus at least c sqrt(loglog(1/delta)/log(1/delta)); no matching upper rate |

The pure scalar two-circle case and the definitions of rank-r versus strict
completeness are prior work, explicitly cited. This application is not a BGS
result. Execution, source hashes, and the combined-excerpt build scope are
recorded in `husimi_shell_review.md` and its evidence certificate.


## Aperture-dependent statistical tomography (2026-09-06)

Proofs: `manuscript/unified_sections/coherent_aperture_minimax.tex` and
`heterodyne_aperture_minimax.tex`. Status: EXACT project derivations, with
FINITE-REGRESSION for scalar identities and NUMERICAL high-precision
reconstruction tests; not independently refereed or fully Lean formalized.

For fixed s,beta,E,R0>0, states obey Tr(rho N_total^beta)<=E, without a
rank or hard Fock cutoff. Define K_R(T)=T/(1+log_+(T/R^2)). Uniformly over
R>=R0, including infinity and R varying with the budget:

- Complete-ball coherent-probability modulus is Theta(K_R(log(1/delta))^(-beta/2)).
- Adaptive fresh-copy binary coherent tests have minimax expected trace
  distance Theta(K_R(log B)^(-beta/2)); a nonadaptive finite design suffices.
- Heterodyne censored outside the ball, with an outside flag and every copy
  counted, has the same minimax order. Infinity is ordinary heterodyne.
- Pure-state vacuum/high-Fock pairs already imply all three lower bounds.
- At beta=1 fixed radius requires exp(Theta(epsilon^-2 log(1/epsilon)))
  copies; unrestricted amplitudes/full heterodyne require exp(Theta(epsilon^-2)).

The estimator cutoff has a proved uniform bias; it is not a state truncation
hypothesis. Constants are not uniform in s,beta,E. The proof does not cover
homodyne, arbitrary squeezed Gaussian or collective measurements. It does
not provide the still-missing upper rate for finitely many fixed shells.
The one-mode numerical implementation has narrower dimensional scope than
the analytic theorem. No established world priority or BGS universality is
claimed. The source-level comparison with published heterodyne bounds is
recorded narrowly in `literature/coherent_minimax_context.md`.


## Arithmetic returns: smooth symbols and periodic points (2026-09-11)

Working-proof base: 9ed93cd1bc5e3362c1dbf520f0f391478dfb6969.
The sources below are working mathematical notes; this entry does not
claim their incorporation into the canonical manuscript or PDF.
EXACT retains its project-derivation meaning. Independent review,
priority verification, and Lean formalization of these results are open.

| Claim | Status | Proof and boundary |
|---|---|---|
| Fixed-harmonic return suppression, uniformly in every replica count with r abs(epsilon) below a fixed radius; explicit quartic replica correction | EXACT + FINITE-REGRESSION + NUMERICAL | mathematics/fixed_harmonic_return_gas.md; one arithmetic sequence, fixed harmonic, vanishing classical kick |
| Entire-lattice weighted resonance bound; Gaussian return estimate for analytic position symbols | EXACT + FINITE-REGRESSION | mathematics/analytic_kick_return_gas.md, Sections 1–4; all Fourier modes and 32 classes included |
| First Edgeworth correction is the classical third-cumulant rate, uniformly in replicas at epsilon=t/(r sqrt(K)) | EXACT + FINITE-REGRESSION | Same note, Section 6; O(1/K) error for analytic symbols, bounded t |
| Smooth position symbols with finite order-32 Fourier moment have the same first correction with O(K^(-7/12)) error | EXACT | Same note, Section 7; controlled moving truncation, not the whole large-variance regime |
| General real smooth symbols on T² admit a one-return comparison with an explicit classical periodic-point average, with O(K^(-q)) error for every q at epsilon=t/sqrt(K) | EXACT + FINITE-REGRESSION + NUMERICAL | mathematics/periodic_point_trace_comparison.md; balanced Weyl quantization; accuracy is in K, not N |
| Centered-cell coupling to Haar measure; one-return Gaussian law with the full Green–Kubo variance for finite fourth Fourier moment | EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION | Same note, Section 7; Cohen–Conze Theorem 2.18 checked at source; no imported Gaussian convergence rate |
| Uniform comparison of all integer replicas with error O(K^(-1/2)) for finite fourth Fourier moment | EXACT + LIMITED INTERNAL AUDIT + FINITE-REGRESSION + NUMERICAL | Same note, Sections 8–9; epsilon=t/(r sqrt(K)); normalized Hilbert–Schmidt normal form, not operator-norm normal form |
| Smooth zero variance iff smooth coboundary; first-scale operator return error O(1/N); uniform second-order Gaussian return law | EXACT + LIMITED INTERNAL AUDIT + FINITE-REGRESSION + NUMERICAL | Same note, Section 10; second-scale epsilon=±sqrt(t N/(r sqrt(K))); generated variance may vanish |
| Joint characteristic trace law for any fixed finite family of physical critical return operators | EXACT + NUMERICAL | Same note, Section 11; self-reviewed deduction from normal-form commutator estimates; not Heisenberg-scale joint traces |
| General analytic phase-space kicks: exponential return suppression and absolute Gaussian approximation O(K^(-1/2)), uniformly when r abs(epsilon) is below a fixed radius | EXACT + LIMITED INTERNAL AUDIT + FINITE-REGRESSION + NUMERICAL | mathematics/phase_space_return_gas.md, Sections 1–6; full orbit variance, vector Weyl phases and all 32 classes; vanishing classical strength |
| Joint Gaussian characteristic traces of period-averaged observables under sum abs(f_hat(v)) sqrt(log(2+norm(v))) < infinity | EXACT + LIMITED INTERNAL AUDIT + FINITE-REGRESSION | Same note, Section 7; averaged observables only, including zero variance; full space and even symbols on the odd block |
| The logarithmic exponent one half is sharp as a class guarantee, including after quantum centering | EXACT + LIMITED INTERNAL AUDIT + FINITE-REGRESSION + NUMERICAL | Same note, Sections 8–9; fixed continuous examples for all smaller exponents; centered example has at least 1/25-o(1) escaping mass |
| Replacing the classical period by rK fails at quadratic order; keeping period K and scaling the kick fails at order 1/K | EXACT + FINITE-REGRESSION | Same note, (P15)–(P16); failures of proposed comparisons, not counterexamples to BGS |
| Required Heisenberg-scale joint traces and microscopic BGS universality | OPEN | Neither comparison supplies the missing long-time estimate or a fixed nonzero classical perturbation |

The analytic-symbol verifier exhausts 612,864 ordered cubic atom words,
2,532,760 independently organized unordered multisets, and 5,152,304
multisets classified by exact rational preimages. The finite sets overlap
between methods; these are not counts of distinct systems.
The computation found additional winding aliases and corrected the
initial cubic prediction. The logarithmic coefficient is explicitly
per period length in (A14).

The two-dimensional verifier checks 960 rational-preimage cases and
1,206 integer-word phases, including 603 odd local areas, and compares
an N=35 physical matrix with all 39,200 classical periodic points.
Exact algebra and floating diagnostics are reported separately.
Reproduction commands are in the notes; generated outputs are
build/analytic-kick-return-gas-precheck.json and
build/periodic-point-trace-comparison-precheck.json.
Continuation on the same date closes the formerly missing classical step.
A direct centered-time coupling transfers the checked Haar CLT; no
periodic-point theorem is silently imported. Source version and hashes
are in literature/periodic_return_clt_sources.md.
The updated verifier additionally exhausts 1,122,112 ordered pair
representations, including a K=262 case in the theorem's range; checks
seven exact distance bounds; and separately tests the unitary normal
form, joint products, and second-order loops on physical N=35 matrices.
The limited internal analytic review covers the pair multiplicity,
weighted fourth-moment estimate, and second-order proof. The coupling
and joint-law extension remain self-reviewed, and none of this is
external referee acceptance or a completed Lean proof.
Uniformity in the replica count is at the explicitly scaled amplitude;
it does not give Heisenberg-time control at a fixed classical strength.

The analytic phase-space continuation removes the position-only
restriction on the small-amplitude, all-variance return theorem.
Orbit-representative cohomology removes quadratic finite-component
resonances; a positive Fourier-atom majorant then starts at degree three.
The proof keeps the onsite phase and the nontrivial antipodal phase.
The logarithmic regularity theorem uses an early-return estimate.
Its centered counterexample retains spectral escape after the actual
quantum mean is removed. This is a regularity boundary for period
averages, not a closure of microscopic BGS.

The new verifier passes 320 exact phase identities, 3,000 rational
endpoint inequalities, 120 finite runs, 1,224 finite atomic exclusions,
25 early-return cases, both counterexample arithmetic constructions,
and separately labeled small-matrix diagnostics. Reproduction and
precise internal review scope are in the phase-space note, Section 10.
Growing-parameter proofs are not inferred from finite checks.

## General hyperbolic toral automorphisms (2026-09-12)

| Claim | Status | Proof and boundary |
|---|---|---|
| For every fixed hyperbolic A in SL(2,Z), an explicit odd-dimensional arithmetic subsequence carries the same analytic return suppression and O(K^(-1/2)) Gaussian approximation | EXACT + LIMITED INTERNAL AUDIT + FINITE-REGRESSION + NUMERICAL | mathematics/general_cat_return_laws.md, Theorem 1; constants depend on A,f; all replicas with r abs(epsilon) below the stated fixed radius |
| The return suppression and approximation extend to every fixed finite Gevrey order, with Fourier weight exp(rho norm(v)^alpha), 0<alpha<=1 | EXACT + LIMITED INTERNAL AUDIT + FINITE-REGRESSION | Same note, Section 6; capped Weyl phases give logarithmic particle weights and conditional-field penalties; no uniform alpha-to-zero limit or all-smooth theorem |
| The weighted logarithmic averaged-observable joint CLT holds for every such A, and exponent one half is sharp even after quantum centering | EXACT + LIMITED INTERNAL AUDIT + FINITE-REGRESSION | Same note, Theorems 2–3; counterexample is a fixed continuous symbol for each A; subsequence depends on A |
| Universal quadratic refinement, composite odd moduli, negative traces, and exact arithmetic class count Delta q_A² | EXACT + LIMITED INTERNAL AUDIT + FINITE-REGRESSION + NUMERICAL | Same note, Sections 2–3; excludes N=1; central character at (N,0) is minus the identity in this convention |
| Generic microscopic BGS for fixed nonlinear chaotic systems | OPEN | Generality over linear hyperbolic maps and global return laws does not establish Heisenberg-scale joint spectral correlations |

The generalization changes both the arithmetic subsequence and the
Weyl convention. The invariant refinement v1*v2+v1+v2 modulo two
works for all SL(2,Z); its negative central sign is retained in the
counterexample. The latter uses an odd prime other than five dividing
b5=t^4-3t²+1, followed by prime-square lifting. A fixed positive
fraction of the centered empirical spectrum then escapes.
The arithmetic, phase, estimate-transfer, and prime-lifting arguments
received limited independent internal review. External priority and
formal verification remain open.

The Gevrey extension uses a further analytic estimate: the bounded
Weyl phase gives a logarithmic, rather than linear, charge cost.
A size Ds²L in the tree criterion retains the connected O(Ks⁴)
remainder. The subadditive alpha quasi-norm of the cyclic Green
operator supplies the stretched-exponential lattice estimate.
The general verifier covers 72 matrices, 200 admissible dimension
cases, 800 exact cyclic preimages, 3,200 exact phase identities,
28 prime-lifting cases, eight counterexample cases, and 72 exact
capped-kernel envelope sums. Physical quantization tests at four
small dimensions are explicitly floating diagnostics.

## Publication integration (2026-09-12)

The five fixed-harmonic, position-kick, periodic-point, phase-space, and
general return-law proof modules are now included in the canonical TeX
manuscript. `sync_return_sections.py --check` verifies source synchronization.
This is publication integration, not a new mathematical scope promotion.

The general modulo-two refinement already had a Lean invariance certificate.
Its polarization identity and nontrivial central parity are now also
kernel-checked without axioms. The full 16-module build passed; the general
analytic return and regularity theorems remain unformalized. Eight focused
return-law Python checks passed. The complete historical Python/C++ suite
was not rerun in this revision. See `publication_review_20260912.md`.


## Short-return obstruction (2026-09-12)

| Claim | Status | Exact boundary |
|---|---|---|
| Ergodic intensity-one local-process convergence forces uniformly vanishing normalized sublinear-frequency traces | PROJECT PROOF + SELF-REVIEW | return_trace_obstruction.md, Theorem 1; first-moment uniform integrability, no second-moment hypothesis |
| The same convergence forces spatial L1 self-averaging on every window with a diverging number of mean spacings | PROJECT PROOF + SELF-REVIEW | Same note, bounded-Lipschitz strengthening; no mixing-rate assumption |
| Critical Gevrey/harmonic returns preclude those local limits and standard globally unfolded pair limits | DERIVED FROM PROJECT RETURN THEOREMS + SELF-REVIEW | Existing return-law proofs remain inputs; shrinking quantum kicks, stated spectral sectors, global unfolding |
| Positive microscopic BGS at fixed classical strength | OPEN | The new criterion is necessary only; a density-dependent unfolding can remove the return obstruction |

Finite exact Fourier/marked-convolution checks and separate floating Gaussian
controls are in the companion verifier. No new full analytic Lean formalization
or external referee validation is claimed. Review: return_obstruction_review_20260912.md.


## Return intensity and local unfolding (2026-09-13)

Theorem 3 of mathematics/return_trace_obstruction.md proves conditional-intensity domination by the absolutely continuous return density, with an essential-infimum cap for ergodic local limits and explicit sharp abstract-spectrum constructions. Formula (S22) quantifies possible first-moment loss. Formula (S25) supplies the origin-weighted density transport; (S26) realizes the same return law with different locally unfolded statistics.

Status: PROJECT PROOF + SELF-REVIEW. The free Brownian support-gap consequence (S24), for 0<t<4, additionally uses the existing project harmonic return theorem and the checked Demni--Hmidi source. It does not identify the full cat-map local limit. Finite rational, symbolic, and floating controls have distinct scopes. External priority and full analytic formalization remain unverified. See record/return_local_limits_review_20260913.md.
