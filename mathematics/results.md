# Current results and exact scope

This is the concise theorem index. The repository-wide status authority is
[`../record/claim_ledger.md`](../record/claim_ledger.md); historical commits or
notes do not override it.

## 1. Pair-key and fourth-moment reduction — EXACT

For odd prime `p`, the off-diagonal pair key

```text
u=x/y, v=(x-1)/(y-1), d=x-y
```

is bijective with the maintained inverse formulas; the diagonal has
multiplicity `p-2`. Under subgroup constraints there are exactly
`(K-1)(K-2)` off-diagonal pairs, and

```text
|V4|=(K^2+1)p^2-(6K^2+3K)p+13K^2-3K.
```

The corrected fourth-moment distribution is

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

one has `d(u,v)=2/(c(u)-c(v))` and `c(h^-1)=-c(h)`. Thus the mixed layer is
governed by `E_+(A)`. For odd prime `K`, Chowla cotangent independence gives
complete characteristic-zero nonzero-difference rigidity.

## 3. Best unconditional pointwise bound — EXACT + EXTERNAL-THEOREM

For

```text
100<K<p^(3/4)/3,
```

a source-exact application of Vyugin--Makarychev gives

```text
E_+(A)<34K^(8/3).
```

The corresponding mixed centered variance is `<136pK^(8/3)`.

See [`cayley_direct_energy.md`](cayley_direct_energy.md).

## 4. Sharp pointwise target — OPEN globally

Exactly

```text
E_+(A)=|A|^4/p+(1/p)sum_{q!=0}|1_Ahat(q)|^4.
```

The target for every intended split design is

```text
E_+(A)=(K-1)^4/p+O(K^(2+o(1))).
```

It is already closed on the complement of the exact order-three row support
described below.

## 5. Shifted-energy orbit reduction — EXACT / EXTERNAL-THEOREM

Each nonzero multiplicative parameter orbit reduces exactly to multiplicative
energy of a shifted subgroup. For `K^2<p`, Shkredov's theorem gives orbit square
mass `<<K^2 log K`. The exact global identity

```text
sum_lambda(E_x(H+lambda)-(2K^2-K))=K^4-E_+(H)
```

shows that naive summation yields only `O(K^3)`, so this route alone does not
beat the maintained `K^(8/3)` theorem.

See [`cayley_shifted_energy_orbits.md`](cayley_shifted_energy_orbits.md).

## 6. Fixed-product row decomposition — EXACT

For one valid pair put `u=xy`, `s=x+y`. Then

```text
c(x)+c(y)=2(u-1)/(u-s+1).
```

At fixed `u` and nonzero parameter there is at most one unordered subgroup
pair. If `I_K(p)` is the maximum number of common parameters between two
distinct product rows, then

```text
Delta_K(p)
 =2 sum_{u<v} sum_{t in T_u cap T_v} omega_u(t)omega_v(t),

Delta_K(p)<=4 I_K(p)(K-1)(K-2).
```

For normalized rows `(1,r)`, the intersection problem is an affine trace map

```text
Y=alpha_r X+beta_r,
alpha_r=U_(r-1)(tau/2),
beta_r=-2U_(r-2)(tau/2),
tau=zeta+zeta^-1.
```

See [`cayley_product_row_intersections.md`](cayley_product_row_intersections.md).

## 7. Exact real-trace order-three support — EXACT + EXTERNAL-THEOREM

Let `K=2m+1` and `C_K(T)` be the minimal polynomial of `tau`. Put

```text
H_K(T)=(T-2)C_K(T).
```

The unique characteristic-zero common trace of the two full row polynomials is
the invalid row class. After dividing it out,

```text
P_(K,r)(T)=H_K(T)/(T-tau),
Q_(K,r)(T)=H_K(alpha_r T+beta_r)/(T-tau)
```

are degree-`m` polynomials over the maximal real cyclotomic ring. For every
split `p!=K` and embedding prime `q|p`,

```text
deg gcd(P_(K,r),Q_(K,r) mod q)
 = number of common Cayley parameters of that row pair.
```

The coefficient ideal of their first three fixed-degree subresultants contracts
to `Lambda_(K,r)^(3) Z`, and Brown--Traub gives

```text
p|Lambda_(K,r)^(3)
iff
some row pair in ratio class [r] has at least three common parameters.
```

After removing factors `2,K` and multiplying over ratio classes,

```text
p does not divide Lambda'_K^(3)
iff
I_K(p)<=2,
```

hence

```text
Delta_K(p)<=8(K-1)(K-2),
E_+(A)<=11(K-1)(K-2).
```

Exact anchors include

```text
Lambda'_(7,2)^(3)=1,
Lambda'_(11,7)^(3)=1,
Lambda'_(13,3)^(3)=1,
Lambda'_(13,12)^(3)=5^2,
Lambda'_(17,10)^(3)=103,
Lambda'_(23,18)^(3)=47^3*139.
```

The split primes `103`, `47`, and `139` are genuinely realized by row
intersections of size at least three.

The growing-`K` closure target remains

```text
P_split^+(Lambda'_K^(3))<=K^(4+o(1)).
```

See [`cayley_product_row_real_trace_ideal.md`](cayley_product_row_real_trace_ideal.md).

### Scope correction for predecessor invariants

The older dehomogenized integers `G'_(K,r)^(3)` and `D'_(K,r)^(3)` remain valid
only in the direction

```text
I>=3 ==> p|D' ==> p|G'.
```

Their converses fail under specialization degree drop at `mu=infinity`.

## 8. Inverse-row reflection reduction — EXACT / EXTERNAL-THEOREM

For `r=-1`,

```text
alpha=-1,
beta=2tau,
Q(T)=-P(2tau-T).
```

After shifting to `tau`, write

```text
F(Z)=P(tau+Z)=E(Z^2)+Z O(Z^2).
```

For every split embedding prime,

```text
I_-1(q)=2 deg gcd(E,O mod q).
```

Thus inverse-row intersections are automatically even, and `I_-1>=3` is a
corank-two half-degree problem. A specialization-safe coefficient ideal gives
an exact support integer `Xi_K`. The Chebyshev fibre identity

```text
2(T_K(T/2)-1)=(T-2)C_K(T)^2
```

shows that this is a reflection self-intersection of one explicit Dickson fibre.

Finite split anchors include support prime `47` at `K=23`, `59` at `K=29`, and
`311,1303` at `K=31`; at `(K,p)=(31,1303)`, `I_-1(p)=4`.

See [`cayley_product_row_reflection.md`](cayley_product_row_reflection.md).

## 9. Characteristic-zero trace-intercept rigidity — EXACT + EXTERNAL-THEOREM

For trace classes `[a],[b]`, define

```text
gamma_r(a,b)=t_b-alpha_r t_a.
```

Bass's prime-conductor cyclotomic-unit theorem implies multiplicative
independence of

```text
|1-zeta|, |1-zeta^2|, ..., |1-zeta^m|.
```

Using

```text
|s_n|=E_[2n],
|t_x-t_y|=E_[x-y]E_[x+y],
```

one obtains a complete fibre classification.

### Theorem

For every odd prime `K>=7` and every normalized ratio `r!=1`, every
characteristic-zero fibre of `gamma_r` has cardinality at most `2`.

- For `r=-1`, every double fibre is only a swap.
- For `r!=+-1`, every double fibre is, up to signs and exchange,

```text
([a],   [a+1-r]),
([a+2], [a+1+r]),
```

and the equality follows exactly from

```text
t_(x+r)-t_(x-r)=s_r s_x.
```

A third point would create a triangle in the step-two quotient of the odd
`K`-cycle by `a~-a`; this quotient is a path and has no such triangle.

In particular the distinguished characteristic-zero row intersection
`([1],[r])` is isolated. Order-three support is therefore genuinely created by
finite reduction, not by a hidden characteristic-zero triple.

An independent C++20 sparse group-ring verifier checks all normalized ratios in
the maintained quick range through `K=199`; an extended recorded run also checks
prime `K=251,307,401,503,601,701,809`, always with maximum fibre size `2`.

See [`cayley_trace_intercept_rigidity.md`](cayley_trace_intercept_rigidity.md).

## 10. Cyclotomic-unit matching and scalar shift-resultant support — EXACT

For valid trace classes define `u_n=s_n/s_1` and

```text
W_r(b)=u_((b+r)/2)u_((b-r)/2),
V_r(a)=u_r u_((a+1)/2)u_((a-1)/2).
```

Then

```text
gamma_r(a,b)-beta_r=s_1^2(W_r(b)-V_r(a)).
```

Since `s_1` is a unit away from `K`, every split row intersection is exactly a
congruence

```text
W_r(b)=V_r(a) mod q
```

between explicit products of cyclotomic units.

There is also a scalar exact-support encoding. Let

```text
P_1(T)=H_K(T)/(T-t_1),
R_r(U)=H_K(U)/(U-t_r),
mathcal R_(K,r)(Z)
 =Res_T(P_1(T),R_r(alpha_r T+beta_r+Z))
 =c_0+c_1 Z+c_2 Z^2+....
```

Over every split embedding prime,

```text
ord_(Z=0)(mathcal R_(K,r) mod q)=I_(1,r)(q).
```

Therefore

```text
I>=3 iff c_0=c_1=c_2=0 mod q.
```

The three-generator ideal

```text
J^shift_(K,r)=(c_0,c_1,c_2)
```

contracts to an integer `Omega_(K,r)^(3)` having the same **split
rational-prime support** as `Lambda_(K,r)^(3)`. Equality of the full integers or
non-split valuations is not claimed.

SymPy/Smith anchors are

```text
(K,r)=(7,2):   Omega=7^3,                  Omega'=1,
(K,r)=(11,7):  Omega=11^5,                 Omega'=1,
(K,r)=(13,3):  Omega=13^6,                 Omega'=1,
(K,r)=(13,12): Omega=2^4*5^2*13^6,         Omega'=5^2.
```

Finally, the nonzero constant coefficient already gives for every fixed ratio

```text
sum_(p==1 mod K, I_r(p)>=3) log p = O(K^3).
```

This does not close the largest-prime target: summing over `O(K)` ratio classes
returns the existing `O(K^4)` global scale. The next arithmetic target is a
simultaneous-gcd theorem for `c_0,c_1,c_2` or the explicit cyclotomic-unit
matching graph, not another height bound on `c_0` alone.

See [`cayley_trace_intercept_rigidity.md`](cayley_trace_intercept_rigidity.md).

## 11. Square resultants and Fibonacci obstruction — EXACT

Every admissible prime-order cleared collision polynomial satisfies

```text
P(X)=(X-1)^3Q(X),
Res(Phi_K,P)=K^3M^2.
```

The Fibonacci slice

```text
Res(Phi_K,X^2+3X+1)=F_K^2
```

shows why a polynomial bound on every individual collision resultant is
impossible. The associated rational model and `(K,p)=(131,F_131)` certificate
both exhibit exact excess `32`.

## 12. Canonical additive discriminant and ratio-orbit structure — EXACT

A single squarefree difference polynomial `S_K` satisfies for split primes

```text
Delta_K(p)>0 iff p|Disc(S_K),
Delta_K(p)<=4v_p(Disc(S_K)).
```

It factors into ratio-orbit factors with exact cross-resultant square structure,
and globally

```text
|Disc(S_K)|
 =2^((K-1)^4/4)K^((K-1)(K^2-7)/4)J_K^4.
```

Exact larger-`K` computations falsify the former residual-height
`O(K^3 log K)` heuristic: genuine `K^4` archimedean mass remains.

## 13. Multiplicative Cayley rigidity — EXACT

Characteristic-zero product collisions are swap and simultaneous inversion
only, giving

```text
E_x(A_K)=4(K-1)(K-2).
```

A canonical product discriminant gives the finite-field exceptional-prime
classification. This is independent structure, not an additive-transfer
theorem.

## 14. Global split-prime additive mass budget — EXACT

For odd prime `K`,

```text
sum_{p==1 mod K}Delta_K(p)log p
 <=(K^3-5K^2+6K+1)((K-1)log12-3logK).
```

This is a deterministic `O(K^4)` logarithmic budget over all split primes.

## 15. Frobenius amplification over minimal finite extensions — EXACT

For arbitrary rational prime `p!=2,K`, put

```text
f=ord_K(p),
q=p^f,
H=mu_K(F_q),
A_(K,p)=c(H\{1}).
```

Every non-forced collision orbit under Frobenius has size exactly `f`, hence

```text
f | Delta_K^ext(p).
```

The normalized collision-resultant argument at one prime ideal extends the
weighted budget to all `p!=2,K`, and the canonical discriminant classification
extends as well:

```text
Delta_K^ext(p)>0 iff p|Disc(S_K),
Delta_K^ext(p)<=4v_p(Disc(S_K)).
```

For unrestricted prime pairs `K~X^theta,p~X`, PNT, Brun--Titchmarsh and the
Frobenius multiplicity imply a density-one exact baseline for every fixed
`theta<1/3`.

This does **not** improve the split slice, where `ord_K(p)=1`.

See [`cayley_frobenius_amplification.md`](cayley_frobenius_amplification.md).

## 16. Full Cayley/Jacobi trace identity — EXACT

For the normalized full annihilator twisted-Jacobi matrix,

```text
1_Ahat(r)=K Tr M_S(2r),
```

with exact moments

```text
sum_q|Tr M_S(q)|^2=p(K-1)/K^2,
sum_q|Tr M_S(q)|^4=pE_+(A)/K^4.
```

This is the ordinary full trace, not a desymmetrized spectral-block theorem.

## 17. Averaged split theorems — EXACT + EXTERNAL-THEOREM

For fixed `theta<1/3`, prime `K~X^theta`, split prime `p~X`,
Bombieri--Vinogradov and PNT give

```text
average Delta_K(p)/K^2 <<_theta X^(3theta-1)->0.
```

The full ordinary Jacobi-trace kurtosis tends to `3` in the same double
average; this is not a CLT.

For fixed `theta<1/5`, integrality strengthens the result to density-one exact
baseline:

```text
Delta_K(p)=0,
E_+(A)=3(K-1)(K-2).
```

## 18. Corrected off/off elliptic theorem — EXACT + EXTERNAL-THEOREM

The generic off/off family has a distinguished reducible fibre with exact valid
count `2p-8`. After spike extraction, Igusa monodromy and
Grothendieck--Lefschetz/Deligne quasi-orthogonality give

```text
Var O << pE_+(A)+K^2p+K^4sqrt(p)+K^4.
```

Thus the off/off layer has collapsed onto the same pointwise Cayley-energy
bottleneck.

## 19. Exact trace-to-local-statistics bridge — EXACT

For an `N x N` unitary matrix, Mobius inversion on set partitions expresses
each distinct-index exponential sum exactly through products of traces. Poisson
summation then gives microscopic factorial `k`-point statistics as weighted
sums of those products. In the pair case,

```text
C_(2,N)(U;phi)
 =N^(-2) sum_m phihat(m/N)(|Tr U^m|^2-N).
```

Compact Fourier support requires exponents of order `N`, the Heisenberg scale.
Thus a weighted joint-trace comparison with the target RMT ensemble on that
range is sufficient for the corresponding band-limited microscopic theorem.

The deterministic bridge is exact. The required Heisenberg-scale trace
estimates for the correct desymmetrized arithmetic spectral block are **OPEN**.
Removing the Fourier band-limit also requires a uniform high-frequency tail.

See [`trace_to_local_statistics_bridge.md`](trace_to_local_statistics_bridge.md).

## 20. Adversarial finite controls

- `(K,p)=(29,728017)` and `(31,1042903)` have `p>K^4` but excess `48`; bare `p>K^4 => exact baseline` is false.
- `(K,p)=(41,2908049)` has a row pair with two common parameters; `I_K(p)<=1` is false.
- `(K,p)=(31,1303)` has inverse-row intersection size `4`.
- complete additive exceptional sets include `E_11={23,67,89}` and `E_13={53,79,131,157,313}`;
- `(p,K)=(461,23)` has energy `1190` versus forced baseline `902`;
- minimal-extension regression controls are `(7,13,2,32),(11,43,2,128),(13,3,3,432),(13,5,4,496)` in `(K,p,f,Delta)` notation;
- independent C++20 trace-intercept regression reaches prime `K=809` in the extended recorded run with maximum fibre size `2` throughout.

Finite computation proves only its explicit finite statements.

## 21. Retractions and scope boundaries

Historical all-orders Catalan/arcsine promotion, the noncommutative trace
shortcut, unsupported higher-rank extrapolations, the former spike-free
off/off theorem, the residual-height `O(K^3 log K)` heuristic, and the two-sided
geometric interpretation of the dehomogenized `D/G` row ideals are not active.

The scalar support `Omega` is not silently identified with `Lambda` beyond the
proved equality of **split rational-prime support**.

See [`../record/retractions.md`](../record/retractions.md).

## 22. Microscopic BGS/GOE/COE — OPEN

No theorem in this repository proves a mean-spacing local eigenphase law. The
current frontier separates into two chains:

```text
cyclotomic-unit / scalar order-three split support
        -> pointwise centered Cayley energy for all intended split designs
        -> complete fourth-moment control

and independently

Heisenberg-scale desymmetrized joint trace estimates
        -> band-limited microscopic RMT correlations
        -> high-frequency tail control
        -> full microscopic BGS/GOE/COE.
```

The deterministic Fourier arrow in the second chain is already exact; the
arithmetic and spectral estimates themselves remain open.