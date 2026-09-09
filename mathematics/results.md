# Current results and exact scope

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
