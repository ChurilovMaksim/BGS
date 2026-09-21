# Current results and exact scope

## Recovered Heisenberg-scale direct attack, reconciled 21 September 2026

A forensic reread of the 14--16 September working dossiers recovered a
scientifically useful layer that was absent from the consolidated tree.
It has now been re-derived against the actual raw modular Weyl convention,
rather than copied from the historical checkpoint.

- [Repaired one-step unistochastic gap and ramp skeleton](fixed_map_unistochastic_ramp.md): after correcting the midpoint symbol, the spectrally conjugate frozen quantization has eventual `s_2<7/8`; its exact multiplicity-counted cyclic sector is `m+O(mN(7/8)^m)` and therefore supplies the CUE ramp on every fixed window below the plateau.  The post-cyclic signed residual remains open.
- [All-time classical stability sum](fixed_map_classical_sum_rule.md): the corrected real-analytic Anosov map has exact linear-cat periodic counts and stability-weighted sum `1+O(rho_cl^m)` from the analytic Ruelle trace formula.
- [Exact Weyl path escape](fixed_map_weyl_path_escape.md): the frozen map has
  an exact one-kick microhop bound, an all-near contribution
  `1+O(0.145^m)`, and a multiscale theorem forcing every surviving
  nonidentity Heisenberg path through at least
  `(tau_0/26) N^(1-epsilon)` bulk Weyl states after an `o(1)` removal.
  The associated encounter kernel has characteristic-free rank at least
  `s(P)/25`.
- [19-adic hyperbolic dephasing](hyperbolic_19adic_dephasing.md): on
  `N=19^k`, `ord_N(S)=(20/19)N`, primitive orbit phases satisfy exact
  Parseval, and a p-adic finite-type argument with Cluckers' van der Corput
  theorem gives the pointwise bound `O(N^(2/3) log N)` on intervals of
  Heisenberg length.
- [Exact history/reconnection algebra](quantum_history_reconnection.md): open Liouville histories and smooth Parseval histories have exact total Hilbert--Schmidt mass; first-witness gluing has no location-entropy factor; literal fixed-complexity segment reconnections have an exact tensor and flat-link limit `N^{-(L-V)}` once logarithmic links mix.
- [Unitary encounter envelope](unitary_encounter_envelope.md): the standard unitary encounter coefficients obey `A_n^abs <= (27/4)^(n-1)`; together with the published order-by-order unitary cancellation, the pure universal main-term series is absolutely summable for `tau<4/27`.  Uniform frozen-map quantum domination is still open.
- [One-shear antiunitary no-go](one_shear_antiunitary_no_go.md): for the
  project cat, every q-only diagonal kick has an exact antiunitary reversor
  at every odd dimension, so the old one-shear fallback cannot be a CUE
  example merely by changing its classical interpretation.

These are structural/direct cancellation results, not pair BGS.  The signed
bulk insertion and the deterministic triangular CUE main term remain open.
The [dossier reconciliation](../record/verified_state_reconciliation_20260921.md)
also records two historical corrections: the v9 two-frequency
Bourgain/sliding theorem is retracted, and the old phrase “CUE contraction
sector = min(m,N)” was never backed by an explicit deterministic sub-sum
evaluation.

## Fixed-map continuation, 21 September 2026

**Project proofs with fresh exact/finite replay; external priority and referee
validation unestablished.**  The late fixed-map handoff adds the following
maintained results while leaving microscopic BGS open:

| Result | Established scope | Boundary |
|---|---|---|
| [Actual frozen-model symmetry theorem](fixed_model_symmetry_theorem.md) | Exact raw-to-midpoint Weyl dictionary; analytic Anosov classical map; trivial (C^1) centralizer, no (C^1) reversor, no relevant affine (C^1) conjugacy for (0<\operatorname{abs}(\kappa)\le10^{-12}) | Does not exclude (N)-dependent quantum commutants or prove trace cancellation |
| [Full-symbol odd-Pell crossover](fixed_model_pell_crossover.md) | Gaussian moment law for (\sqrt K\,\overline A_K), exact variance (1650797/4000000), and necessary escape ( \operatorname{abs}(\epsilon_K)\sqrt K\to\infty) for CUE pair behaviour in the stated family | Frozen (\epsilon_K=\tau N_K) lies beyond the proved crossover window |
| [Moment controls and transfer](fixed_map_moment_control_and_transfer.md) | Stronger two-level moment interval, exact repeated-clock loop-test falsifier, and RMS perturbation-transfer estimate | Conditional/asymptotic inputs do not reach fixed (\tau) |
| [Three-orientation barrier](three_orientation_resolvent_barrier.md) | Under three normalized mixed-residual hypotheses, explicit lower barrier with additive (s^3/[64(1+s^2)^{7/2}]) | Residual decay for the actual propagator is still unproved |
| [Fourier-line resonance coercivity](fourier_line_resonance_coercivity.md) | Sharp lower constant on every real Fourier-line (H^{1+\beta}) class when (\kappa_\beta>0); (\kappa_1=\sqrt{(T-2)/(T+2)}), hence (1/\sqrt2) for the stated project convention; (H^{3/2}) positivity for (\operatorname{abs}(\operatorname{tr}A)\ge6) | Does not solve the full two-dimensional analytic cohomological equation |
| [Local jet obstruction](local_jet_resonance_obstruction.md) | Exact polynomial local coboundary with a strict local minimum | Local model only; shows why fixed-point jets cannot settle the torus problem |

The [final integration audit](../record/final_research_handoff_20260921.md)
records the recovered archive hashes, fresh replay and old-PR disposition.

## Fixed-family reductions, 20 September 2026

[The fixed-map chapter](fixed_map_resolvent_frontier.md) consolidates
algebraic-return, coherent-memory, determinant-ratio and mixed-loop work.
The new exact p=3 mixed identity gives a conditional bounded interval for
the Abel pair statistic when the first two residuals vanish. Those
residuals remain unproved for the fixed map, and the interval does not
identify the CUE value. The full all-order criterion is conditional on an
external loop-characterization theorem and a still-open model estimate.
All recovered proof and computational records are in the indexed supplement.

## Recovered finite-window result and scope corrections

The [compensated-family note](compensated_heisenberg_trace_control.md),
(H8)--(H9), gives an explicit separated-cluster bound and its averaged
Heisenberg-window consequence at epsilon=o(N^(1/3)). The parent operator
estimate, inversion symmetry and vanishing classical strength remain inputs.
The [trace bridge](trace_to_local_statistics_bridge.md) now includes an exact
short-trace counterexample while retaining its later bandlimit extension.
The Cayley support proposals imply exclusion with a fixed power margin;
K^(4+o(1)) is insufficient for the full K=o(p^(1/4)) regime.
See [recovery audit](../record/recovery_audit_20260920.md).

## Short returns and ergodic local limits

**Project proof; self-reviewed; priority unverified.** An ergodic stationary
intensity-one local limit forces vanishing normalized traces uniformly over
all sublinear frequency windows. More generally it forces uniform density
in spatial L1 on every window containing a diverging number of mean spacings.
No second-moment convergence assumption is needed for this implication.
The proof uses a slowly changing mark and preservation of first moments.

Applied to the existing cat-map return laws, it excludes such local limits
when $\epsilon_K\to0$ and $K\epsilon_K^2$ remains bounded. Positive-variance
universality would require $K\epsilon_K^2\to\infty$; this is not sufficient.
An independent Gaussian pair inequality gives explicit Poisson/sine-kernel
discrepancies and low-frequency budgets. The critical conclusion depends on
global mean-spacing unfolding. See
[return_trace_obstruction.md](return_trace_obstruction.md) and its linked review.

Theorem 3 now allows intensity loss. For a folded law
$\mu=\rho\,dy+\mu_{\rm s}$, every marked local limit has conditional
intensity $h\le\rho$; an ergodic limit of intensity $\alpha$ requires
$\alpha\le\operatorname*{ess\,inf}\rho$. Explicit simple-spectrum
constructions attain every admissible $\alpha$. This sharpness is in the
class of abstract spectra, not in the cat-map quantization class.
For the free Brownian harmonic endpoint, $0<t<4$, every local limit has
empty-component weight at least $1-b(t)/\pi$; an ergodic limit is empty.
The density-transport formula also constructs identical return laws with
different locally unfolded statistics. Review and finite evidence:
[return_local_limits_review_20260913.md](../record/return_local_limits_review_20260913.md).

## General hyperbolic return laws and sharp regularity

**Project proof with limited internal review; external priority unverified.**
For every fixed hyperbolic matrix in SL(2,Z), explicit odd-dimensional
arithmetic subsequences support Gevrey return suppression and an absolute
Gaussian approximation of order $K^{-1/2}$ at the stated small scaled
replica amplitude. Every fixed finite Gevrey order is allowed; constants
are not uniform as the Fourier-decay exponent tends to zero.

For period-averaged observables, a square-root logarithmic Fourier weight
suffices for a joint Gaussian limit. For each map a fixed continuous symbol
shows that every smaller logarithmic exponent is insufficient, even after
subtracting the quantum mean. See
[general_cat_return_laws.md](general_cat_return_laws.md), Theorems 1–3.
These are global, arithmetic-subsequence results. They do not close the
Heisenberg-time, fixed-classical-strength BGS comparison.

## Harmonic-scale laws of the actual kicked return propagator

**EXACT (project proof; independently audited by a second agent).** In the
Pell harmonic window described below, set $\epsilon=\tau/\sqrt{2K}$ and
$U_{\epsilon,a}=e^{i\epsilon B_a}U_0$. For every fixed $m,\tau$, the normalized
odd trace of $U_{\epsilon,a}^{mK}$ converges in $L^2$ over harmonics to the
absolutely convergent cycle-pair diagram series in `pell_harmonic_returns.md`.
It determines a weakly continuous family of probability measures on the
circle. At $\beta=0$ its moments are $e^{-m^2\tau^2/2}$; at $\beta=1/2$
they are $e^{-m\tau^2/2}L_{m-1}^{(1)}(m\tau^2)/m$.
The second moment equals
$e^{-t}(1-te^{-(1-2\beta)t/2})$ for $t=\tau^2$ and $\beta\ge1/6$.

The key additional estimate is uniform control of nonzero aggregate
relations in the full Fourier--Bessel expansion, using the integer image
of $S^2-6S+I$ and its $\ell^1$ lower bound. The endpoint probability laws
are known. Arithmetic priority, external referee assessment and BGS are
not established. Fixed $mK\asymp\log N$ is the precise time scope.

## Harmonic-scale transition in the fixed Pell cat map

**EXACT (project proof).** For prime Pell periods $K\to\infty$, sample
integers $1\le a\le L_K\le\sqrt{N_K}$ coprime to $N_K$, with
$\log L_K/\log N_K\to\beta\in[0,1/2]$. Compressions of the physical harmonic
$2\cos(2\pi ax/N_K)$ have global empirical spectral measures converging in
probability, uniformly over all odd cat eigenspaces, to the circle-graphon
law of radius $(1-2\beta)/2$. Every fixed moment converges in $L^2$.

The fourth moment is $3-2\beta$. With $\rho=1-2\beta$, the sixth is
$5+6\rho+15\rho^2/4+(3\rho/2-1)_+^2$. These laws have unbounded support for
$\beta<1/2$, while the endpoint is the variance-one semicircle. They vary
weakly continuously. A weighted ordered-moment theorem interpolates between
commuting Gaussian and free semicircular fields; normalized complementary
half-window commutators have limiting squared norm $8\beta(1-\beta)$.

The proof, exact scopes and prior graphon results are in
`pell_harmonic_transition.md`. The key arithmetic input is quadratic
harmonic-phase averaging, not finite independence of the Weyl variables.
This does not prove local statistics of a quantum propagator. Priority
for the arithmetic realization remains unverified.

This is the concise theorem index. The repository-wide status authority is
[`../record/claim_ledger.md`](../record/claim_ledger.md); historical commits or
notes do not override it.

## September 9: full Cayley--Jacobi trace Gaussian limit

**EXACT + EXTERNAL-THEOREM.** For odd prime subgroup order `K`, split prime `p`,
and `n=K-1`, the real variable
`n^(-1/2) sum_(a in c(H\{1})) e_p(qa)`, with uniform `q!=0`,
converges to `N(0,1)` whenever `K->infinity` and `K=o(log p)`.
At any finitely many distinct positive fixed integer multiples of `q`,
the joint limit is a vector of independent standard normals.

The same empirical joint laws converge weakly in probability over dyadic
split designs `K in (Q/2,Q]`, `p in (X/2,X]`, whenever
`Q->infinity`, `log Q=o(log X)`. The proof controls all fixed weighted moments
by a global `O_w(K^r)` collision budget. Its quantitative average normalized
excess is `O_w(Q^(r/2+1)/X)`.

The scalar law also has the quantitative pointwise estimate
`d_Kol <= C((K-1)^(-1/2)+sqrt((K-1)/log p))`.
For sufficiently large `X,Q` with `Q<=X^(1/4)`, outside a design fraction
`O((log X)X^(-1/4))`, its Kolmogorov distance is
`O(Q^(-1/2)+sqrt(log Q/log X))`. The additional input is classical
Esseen smoothing; the uniform growing-moment budget is proved explicitly.

This is a full-trace distribution theorem, not a local spectral theorem or
a theorem about traces of matrix powers. External inputs: Chowla independence,
and Bombieri--Vinogradov/PNT for the density version. Global novelty has not
been established. See [`cayley_trace_gaussian_limit.md`](cayley_trace_gaussian_limit.md).

## 1. Pair-key / fourth-moment reduction — EXACT

For odd prime `p`, the off-diagonal key

```text
u=x/y, v=(x-1)/(y-1), d=x-y
```

is bijective with the maintained inverse formulas; the diagonal has
multiplicity `p-2`. Under subgroup constraints there are exactly
`(K-1)(K-2)` off-diagonal pairs and

```text
|V4|=(K^2+1)p^2-(6K^2+3K)p+13K^2-3K.
```

The corrected distribution is

```text
B(t)=O(t)+2(p-2)C_H(t)+(p-2)^2 1_{t=0}.
```

See [`fourth_moment_reduction.md`](fourth_moment_reduction.md).

## 2. Cayley additive-energy reduction — EXACT

For

```text
c(h)=(h+1)/(h-1),
A=c(H\{1}),
```

one has `d(u,v)=2/(c(u)-c(v))` and `c(h^-1)=-c(h)`.  Thus the mixed layer is
controlled by `E_+(A)`.  Prime-order characteristic-zero additive collisions
are only the forced identity/inversion-swap relations.

## 3. Best uniform pointwise theorem — EXACT + EXTERNAL-THEOREM

For

```text
100<K<p^(3/4)/3,
```

Vyugin--Makarychev gives

```text
E_+(A)<34K^(8/3).
```

The sharp target remains

```text
E_+(A)=(K-1)^4/p+O(K^(2+o(1))).
```

## 4. Fixed-product rows — EXACT

For one valid pair put `u=xy`, `s=x+y`. Then

```text
c(x)+c(y)=2(u-1)/(u-s+1).
```

At fixed product and nonzero parameter there is at most one unordered subgroup
pair. If `I_K(p)` is the maximal intersection size of two distinct product
rows, then

```text
Delta_K(p)<=4 I_K(p)(K-1)(K-2).
```

The normalized row ratio `r` has affine trace map

```text
Y=alpha_r X+beta_r,
alpha_r=U_(r-1)(tau/2),
beta_r=-2U_(r-2)(tau/2),
tau=zeta+zeta^-1.
```

## 5. Exact maximal-real order-three support — EXACT + EXTERNAL-THEOREM

Let `C_K(T)` be the minimal polynomial of `tau` and

```text
H_K(T)=(T-2)C_K(T).
```

After removing the unique invalid characteristic-zero trace, the source/target
cofactors have fixed degree `m=(K-1)/2`. For every split embedding prime,

```text
deg gcd(P_(K,r),Q_(K,r) mod q)=row intersection count.
```

The first three fixed-degree subresultants define an ideal contracting to
`Lambda_(K,r)^(3) Z`, and

```text
p|Lambda_(K,r)^(3)
iff
some row pair in ratio class [r] has I>=3.
```

Outside the product support `Lambda'_K^(3)`,

```text
I_K(p)<=2,
Delta_K(p)<=8(K-1)(K-2),
E_+(A)<=11(K-1)(K-2).
```

Exact anchors include

```text
Lambda'_(13,12)=5^2,
Lambda'_(17,10)=103,
Lambda'_(23,18)=47^3*139.
```

The older dehomogenized `D'/G'` invariants remain one-way obstructions only;
their converse failed a degree-drop audit at projective infinity.

See [`cayley_product_row_real_trace_ideal.md`](cayley_product_row_real_trace_ideal.md).

## 6. Characteristic-zero trace-intercept rigidity — EXACT + EXTERNAL-THEOREM

For trace classes define

```text
gamma_r(a,b)=t_b-alpha_r t_a.
```

Bass's prime-conductor cyclotomic-unit theorem implies multiplicative
independence of

```text
|1-zeta|,...,|1-zeta^m|.
```

Using

```text
|s_n|=E_[2n],
|t_x-t_y|=E_[x-y]E_[x+y],
```

one gets a complete fibre classification: every characteristic-zero fibre has
size at most `2`. For `r=-1` doubletons are swaps; for `r!=+-1` every doubleton
is, up to signs/exchange,

```text
([a],   [a+1-r]),
([a+2], [a+1+r]).
```

The identity comes from `t_(x+r)-t_(x-r)=s_r s_x`.  A third point would create
a triangle in the step-two quotient of an odd cycle, which is impossible.

An independent C++20 group-ring verifier checks every normalized ratio through
the quick range `K<=199`; the recorded extended run reaches prime `K=809`.

See [`cayley_trace_intercept_rigidity.md`](cayley_trace_intercept_rigidity.md).

## 7. Cyclotomic-unit matching and general scalar support — EXACT

With `u_n=s_n/s_1`, valid row intersections satisfy exactly

```text
W_r(b)=V_r(a) mod q,
W_r(b)=u_((b+r)/2)u_((b-r)/2),
V_r(a)=u_r u_((a+1)/2)u_((a-1)/2).
```

Define the scalar shift resultant

```text
R_(K,r)(Z)
 =Res_T(P_1(T),R_r(alpha_r T+beta_r+Z))
 =c_0+c_1Z+c_2Z^2+....
```

Then

```text
ord_0 R_(K,r)=I_(1,r),
I>=3 iff c_0=c_1=c_2=0 mod q.
```

The three-generator contraction `Omega_(K,r)^(3)` has the same split
rational-prime support as `Lambda_(K,r)^(3)`.  For each fixed ratio,

```text
sum_(p==1 mod K, I_r(p)>=3) log p=O(K^3).
```

This is not a polynomial largest-prime theorem; summing over `O(K)` ratios
returns the existing `O(K^4)` scale.

## 8. Inverse-row reflection — EXACT

For `r=-1`,

```text
alpha=-1,
beta=2tau,
Q(T)=-P(2tau-T).
```

Writing

```text
F(X)=P(tau+X)=E(X^2)+X O(X^2),
```

one has for every split embedding prime

```text
I_-1(q)=2 deg gcd(E,O mod q).
```

Thus inverse intersections are automatically even. A fixed-degree half-size
support ideal defines `Xi_K`. At `(K,p)=(31,1303)`, the direct intersection
size is `4`.

See [`cayley_product_row_reflection.md`](cayley_product_row_reflection.md).

## 9. Inverse pair-sum perfect square — EXACT

Let the roots of `F` be `x_1,...,x_m` and define

```text
R_-(Z)=Res_X(F(X),F(Z-X)).
```

Then universally

```text
R_-(Z)=2^m F(Z/2) S(Z)^2,
S(Z)=prod_(i<j)(Z-x_i-x_j).
```

For split primes, `2^mF(0)` is a unit, so

```text
I_-1(q)=2 ord_0 S(Z),
I_-1(q)>=3 iff S(0)=S'(0)=0 mod q.
```

The two-scalar ideal `(S(0),S'(0))` contracts to `Theta_K`; `Theta_K` has the
same split order-three support as `Xi_K` and the inverse factor of `Lambda`.
Full integer equality is not claimed.

See [`cayley_inverse_pair_sum_factorization.md`](cayley_inverse_pair_sum_factorization.md).

## 10. Inverse pair sums are a translated half-degree resultant — EXACT

The square root itself has a much cheaper description. Translate

```text
F_Z(X)=F(X+Z/2)=E_Z(X^2)+X O_Z(X^2).
```

Then, up to a convention-dependent sign,

```text
S(Z)=+-Res_Y(E_Z,O_Z).
```

In particular

```text
S(0)=+-Res(E,O),
S'(0)=+-d/dZ Res(E_Z,O_Z)|_(Z=0).
```

The first-order deformation is

```text
dE_Z/dZ|_0=(O+2Y O')/2,
dO_Z/dZ|_0=E'.
```

Hence inverse order-three support is simultaneous vanishing of a half-degree
resultant and its translation derivative. Both scalars can be computed with
one Sylvester determinant over dual numbers `eps^2=0`, avoiding the degree-`m^2`
shift resultant.

Exact two-scalar anchors are

```text
Theta'_7=1,
Theta'_11=1,
Theta'_13=5,
Theta'_17=1,
Theta'_19=37,
Theta'_23=47^2*137.
```

For comparison `Xi'_23=47*137`: split prime support agrees, valuations differ.
The translated route is orders of magnitude faster than the full shift
resultant in the maintained SymPy reference computation; Smith normal form is
the next finite-algebra bottleneck.

## 11. Square collision resultants and canonical discriminants — EXACT

Every maintained prime-order cleared collision polynomial satisfies

```text
Res(Phi_K,P)=K^3M^2.
```

The Fibonacci slice

```text
Res(Phi_K,X^2+3X+1)=F_K^2
```

shows individual resultants may be exponentially large.  The canonical
difference polynomial gives for split primes

```text
Delta_K(p)>0 iff p|Disc(S_K),
Delta_K(p)<=4v_p(Disc(S_K)),
```

with exact ratio-orbit fourth-power structure

```text
|Disc(S_K)|
 =2^((K-1)^4/4)K^((K-1)(K^2-7)/4)J_K^4.
```

## 12. Global split-prime mass and averaged theorems — EXACT / EXTERNAL-THEOREM

For odd prime `K`,

```text
sum_(p==1 mod K) Delta_K(p)log p
 <=(K^3-5K^2+6K+1)((K-1)log12-3logK).
```

For prime `K~X^theta`, split prime `p~X`, Bombieri--Vinogradov and PNT imply

```text
average Delta_K(p)/K^2 <<_theta X^(3theta-1)
```

for fixed `theta<1/3`.  For fixed `theta<1/5`, asymptotically almost every split
pair has the exact baseline

```text
Delta_K(p)=0,
E_+(A)=3(K-1)(K-2).
```

## 13. Frobenius amplification in minimal finite extensions — EXACT

For arbitrary prime `p!=2,K`, put

```text
f=ord_K(p), q=p^f, H=mu_K(F_q).
```

Every non-forced collision Frobenius orbit has size exactly `f`, hence

```text
f | Delta_K^ext(p).
```

The weighted resultant budget and canonical discriminant classification extend
to all such rational primes.  For unrestricted prime pairs `K~X^theta,p~X`,
PNT + Brun--Titchmarsh + the Frobenius multiplicity give a density-one exact
baseline for every fixed `theta<1/3` in the minimal extension.  This does not
improve the split slice, where `f=1`.

See [`cayley_frobenius_amplification.md`](cayley_frobenius_amplification.md).

## 14. Full Cayley/Jacobi trace identity — EXACT

For the normalized full annihilator twisted-Jacobi matrix,

```text
1_Ahat(r)=K Tr M_S(2r),
sum_q|Tr M_S(q)|^2=p(K-1)/K^2,
sum_q|Tr M_S(q)|^4=pE_+(A)/K^4.
```

The normalized fourth/second moment ratio tends to `3` in the maintained split
double average below `theta<1/3`. This is not a CLT and not a local spectral
law.

## 15. Corrected off/off elliptic theorem — EXACT + EXTERNAL-THEOREM

Every generic class has a coherent reducible fibre of exact size `2p-8`.
After extraction, Igusa monodromy and Deligne/Fouvry--Kowalski--Michel
quasi-orthogonality give

```text
Var O << pE_+(A)+K^2p+K^4sqrt(p)+K^4.
```

Thus the elliptic layer is governed by the same Cayley-energy bottleneck.

## 16. Exact trace-to-local-statistics bridge — EXACT

For an `N x N` unitary matrix, partition-lattice Mobius inversion expresses
distinct-index exponential sums through products of traces. Poisson summation
then gives microscopic factorial statistics as weighted sums of those trace
products. In particular,

```text
C_(2,N)(U;phi)
 =N^(-2) sum_m phihat(m/N)(|Tr U^m|^2-N).
```

Band-limited microscopic tests require trace powers `|m|=Theta(N)`.
A weighted Heisenberg-scale joint-trace comparison with the target RMT ensemble
is sufficient for the corresponding band-limited microscopic theorem. For
positive normalized averages and a reference Schwartz limit, comparison on
**every** compact Fourier support extends automatically to all Schwartz tests.
The proof uses a positive band-limited majorant and uniform translated-cube
bounds; see `bandlimited_correlation_extension.md`. The required dynamical
Heisenberg-scale estimates remain **OPEN**; a fixed Fourier cap is insufficient.

See [`trace_to_local_statistics_bridge.md`](trace_to_local_statistics_bridge.md).

## 17. Verification and adversarial controls

Promoted finite controls include:

- `(K,p)=(29,728017)` and `(31,1042903)` with `p>K^4` but positive excess;
- `(K,p)=(41,2908049)` with a row pair sharing two parameters;
- `(K,p)=(31,1303)` with inverse intersection size `4`;
- `(K,p)=(131,F_131)` with exact excess `32`;
- C++20 characteristic-zero intercept regression through an extended prime
  anchor `K=809`;
- inverse translated-resultant/Smith anchors through `K=23`;
- minimal-extension controls
  `(K,p,f,Delta)=(7,13,2,32),(11,43,2,128),(13,3,3,432),(13,5,4,496)`.

Finite computation proves only its explicit finite statements.

## 18. Current frontier — OPEN

The arithmetic chain is

```text
common split divisors of small cyclotomic scalar systems
        -> pointwise centered Cayley energy
        -> complete fourth-moment control.
```

A sufficient target remains, for example,

```text
P_split^+(Lambda'_K^(3))<=K^(4+o(1)),
```

or an equivalent theorem for `Omega` / inverse `Theta` support.

The microscopic chain is independently

```text
Heisenberg-scale desymmetrized joint traces
        -> correlations at every compact Fourier support
        -> Schwartz correlations by positivity and occupation bounds.

The dynamical trace comparison is open; the extension arrow is proved.
Spacing/process conclusions require their own stated hypotheses.
```

Full microscopic universality remains **OPEN**.

## Magnetic quotient: restricted global law (2026-09-05)

See [the complete proof](magnetic_quotient_semicircle.md). Exact: geometric
antiunitary, orbit-basis equivalence and all-order signed trace histograms.
Derived under explicit hypotheses: quantitative even-moment L2 bounds and
global semicircle convergence for prime K=o(log p). Not derived: fixed-cat-map
or microscopic BGS universality. Equation (21) proves the fixed-map obstruction.

## Pell Floquet normal form and recurrence spectrum (2026-09-05)

The [self-contained proof](pell_floquet_normal_form.md) establishes an explicit
normal form for the actual fixed-map cosine-kicked propagator: odd normalized
HS error at most 12 epsilon^2/sqrt(K), for every real epsilon and odd prime
K>=11, with composite Pell moduli allowed. At epsilon=tau/sqrt(2K), the
K-th power has wrapped normal eigenvalue law, with Fourier coefficients
exp(-m^2 tau^2/2). Subcritical folded phases have a W2 Gaussian limit under
epsilon sqrt(K)->0. These are project proofs, not externally refereed or
fully Lean-formalized results; priority and microscopic BGS remain open.

The corrected fourth-moment decimal is 5.614220692151198071627965... . A
separate integer-interval verifier certifies it without floating point.

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
