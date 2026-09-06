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
