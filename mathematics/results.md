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

one has `d(u,v)=2/(c(u)-c(v))` and `c(h^-1)=-c(h)`.  Thus the mixed layer is governed by `E_+(A)`.  For odd prime `K`, Chowla cotangent independence gives complete characteristic-zero nonzero-difference rigidity.

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

It is already closed on the explicit complement of the exact real-trace support `Lambda'_K^(3)` below.

## 5. Shifted-energy orbit reduction — EXACT / EXTERNAL-THEOREM

Each nonzero multiplicative parameter orbit satisfies an exact reduction to the multiplicative energy of a shifted subgroup.  For `K^2<p`, Shkredov's theorem gives orbit square mass `<<K^2 log K`.  The exact global identity

```text
sum_lambda(E_x(H+lambda)-(2K^2-K))=K^4-E_+(H)
```

shows that naive summation of these good local bounds yields only `O(K^3)`, so this route alone does not beat the maintained `K^(8/3)` theorem.

See [`cayley_shifted_energy_orbits.md`](cayley_shifted_energy_orbits.md).

## 6. Fixed-product row decomposition — EXACT

For one valid pair put `u=xy`, `s=x+y`. Then

```text
c(x)+c(y)=2(u-1)/(u-s+1).
```

At fixed `u` and nonzero parameter there is at most one unordered subgroup pair.  If `I_K(p)` is the maximum number of common parameters between two distinct product rows, then exactly

```text
Delta_K(p)
 =2 sum_{u<v} sum_{t in T_u cap T_v} omega_u(t)omega_v(t),

Delta_K(p)<=4 I_K(p)(K-1)(K-2).
```

For rows `w^2,q^2`, row intersection is the constrained affine trace equation

```text
Y=alpha X+beta,
X=z+z^-1,
alpha=(q-q^-1)/(w-w^-1),
beta=2(w/q-q/w)/(w-w^-1).
```

See [`cayley_product_row_intersections.md`](cayley_product_row_intersections.md).

## 7. Exact real-trace order-three support — EXACT + EXTERNAL-THEOREM

Let `K=2m+1`, `tau=zeta+zeta^-1`, and let `C_K(T)` be the minimal polynomial of `tau`.  The full subgroup trace polynomial is

```text
H_K(T)=(T-2)C_K(T).
```

After normalizing a distinct row pair to `(1,r)`, the affine coefficients are the consecutive Chebyshev values

```text
alpha_r=U_(r-1)(tau/2),
beta_r=-2U_(r-2)(tau/2).
```

The unique characteristic-zero common trace is the invalid row class `T=tau`, mapped to the invalid target trace.  Remove it explicitly:

```text
P_(K,r)(T)=H_K(T)/(T-tau),
Q_(K,r)(T)=H_K(alpha_r T+beta_r)/(T-tau).
```

Both are degree `m` polynomials over the maximal real cyclotomic ring `O^+=Z[tau]`.  For every split `p!=K` they remain fixed-degree and squarefree, and for each real embedding prime `q|p`,

```text
deg gcd(P_(K,r),Q_(K,r) mod q)
 = number of common Cayley parameters of that row pair.
```

Let `Jtr_(K,r)^(3)` be the coefficient ideal of the first three fixed-degree subresultants and write

```text
Jtr_(K,r)^(3) cap Z = Lambda_(K,r)^(3) Z.
```

Brown--Traub's subresultant criterion plus the exact trace interpretation gives, for split primes,

```text
p|Lambda_(K,r)^(3)
iff
some row pair in ratio class [r] has at least three common parameters.
```

After removing factors `2,K` and multiplying over row-ratio classes,

```text
p does not divide Lambda'_K^(3)
iff
I_K(p)<=2.
```

Hence outside the **exact** order-three geometric support,

```text
Delta_K(p)<=8(K-1)(K-2),
E_+(A)<=11(K-1)(K-2).
```

Exact Smith-normal-form anchors are

```text
Lambda'_(7,2)^(3)=1,
Lambda'_(11,7)^(3)=1,
Lambda'_(13,3)^(3)=1,
Lambda'_(13,12)^(3)=5^2,
Lambda'_(17,10)^(3)=103,
Lambda'_(23,18)^(3)=47^3*139  (extended).
```

The split primes `103`, `47`, and `139` are genuinely realized by row intersections of size at least three.

The remaining growing-`K` problem is

```text
P_split^+(Lambda'_K^(3))<=K^(4+o(1)).
```

A proof would close the pointwise Cayley-energy bottleneck throughout `K=o(p^(1/4))`.  This is **OPEN**.

See [`cayley_product_row_real_trace_ideal.md`](cayley_product_row_real_trace_ideal.md).

### Scope correction for predecessor invariants

The older dehomogenized projective-row integers `G'_(K,r)^(3)` and `D'_(K,r)^(3)` remain valid **one-way** obstructions:

```text
I>=3 ==> p|D' ==> p|G'.
```

Their converses are not active: a specialization can create leading-degree loss at `mu=infinity`, producing subresultant false positives.  The real-trace `Lambda` construction was introduced precisely to remove this projective degree-drop ambiguity.

See [`cayley_product_row_subresultants.md`](cayley_product_row_subresultants.md) and [`cayley_product_row_coefficient_ideal.md`](cayley_product_row_coefficient_ideal.md).

## 8. Square resultants and Fibonacci obstruction — EXACT

Every admissible prime-order cleared collision polynomial satisfies

```text
P(X)=(X-1)^3Q(X),
Res(Phi_K,P)=K^3M^2.
```

Thus the maintained exponential norm cutoff excludes all non-forced reductions.  The Fibonacci slice

```text
Res(Phi_K,X^2+3X+1)=F_K^2
```

shows why a polynomial bound on every individual collision resultant is impossible.  The associated rational model and the `(K,p)=(131,F_131)` finite certificate both exhibit exact excess `32`.

## 9. Canonical additive discriminant and ratio-orbit structure — EXACT

A single squarefree difference polynomial `S_K` satisfies

```text
Delta_K(p)>0 iff p|Disc(S_K),
Delta_K(p)<=4v_p(Disc(S_K)).
```

It factors into ratio-orbit factors with exact cross-resultant square structure, and globally

```text
|Disc(S_K)|
 =2^((K-1)^4/4)K^((K-1)(K^2-7)/4)J_K^4.
```

Exact larger-`K` computations falsify the former residual-height `O(K^3 log K)` heuristic: genuine `K^4` archimedean mass remains.

## 10. Multiplicative Cayley rigidity — EXACT

Characteristic-zero product collisions are swap and simultaneous inversion only, giving

```text
E_x(A_K)=4(K-1)(K-2).
```

A canonical product discriminant gives the corresponding finite-field exceptional-prime classification.  This is independent structure, not an additive-transfer theorem.

## 11. Global split-prime additive mass budget — EXACT

For odd prime `K`,

```text
sum_{p==1 mod K}Delta_K(p)log p
 <=(K^3-5K^2+6K+1)((K-1)log12-3logK).
```

This is a deterministic `O(K^4)` logarithmic budget over all split primes.

## 12. Full Cayley/Jacobi trace identity — EXACT

For the normalized full annihilator twisted-Jacobi matrix,

```text
1_Ahat(r)=K Tr M_S(2r),
```

with exact second and fourth trace moments

```text
sum_q|Tr M_S(q)|^2=p(K-1)/K^2,
sum_q|Tr M_S(q)|^4=pE_+(A)/K^4.
```

This is the ordinary full trace and does not revive the retracted historical noncommutative trace shortcut.

## 13. Averaged theorems — EXACT + EXTERNAL-THEOREM

For fixed `theta<1/3`, prime `K~X^theta`, split prime `p~X`, Bombieri--Vinogradov and PNT imply

```text
average Delta_K(p)/K^2 <<_theta X^(3theta-1)->0.
```

The full ordinary Jacobi-trace kurtosis tends to `3` in the same double average; this is not a CLT.

For fixed `theta<1/5`, integrality of `Delta_K(p)` strengthens the result to density-one **exact** baseline:

```text
Delta_K(p)=0,
E_+(A)=3(K-1)(K-2)
```

for asymptotically almost every dyadic split pair.

## 14. Corrected off/off elliptic theorem — EXACT + EXTERNAL-THEOREM

The generic off/off family has a distinguished reducible fiber with exact valid count `2p-8`.  After spike extraction, Igusa monodromy and Grothendieck--Lefschetz/Deligne quasi-orthogonality give

```text
Var O << pE_+(A)+K^2p+K^4sqrt(p)+K^4.
```

Thus the off/off layer has collapsed onto the same pointwise Cayley-energy bottleneck.

## 15. Adversarial finite controls

- `(K,p)=(29,728017)` and `(31,1042903)` have `p>K^4` but excess `48`; bare `p>K^4 => exact baseline` is false.
- `(K,p)=(41,2908049)` has a row pair with two common parameters; `I_K(p)<=1` is false.
- complete additive exceptional sets remain `E_11={23,67,89}` and `E_13={53,79,131,157,313}`;
- `(p,K)=(461,23)` has energy `1190` versus forced baseline `902`.

Finite computation proves only its explicit finite statements.

## 16. Retractions and scope boundaries

Historical all-orders Catalan/arcsine promotion, the noncommutative trace shortcut, unsupported higher-rank extrapolations, the former spike-free off/off theorem, the residual-height `O(K^3 log K)` heuristic, and the two-sided geometric interpretation of the dehomogenized `D/G` row ideals are not active.

See [`../record/retractions.md`](../record/retractions.md).

## 17. Microscopic BGS/GOE — OPEN

No theorem in this repository proves a mean-spacing local eigenphase law.  Even closing the exact real-trace split-support problem and the complete fourth-moment layer leaves a separate local-statistics/comparison problem.

The current frontier is

```text
split support of Lambda'_K^(3)
        -> pointwise centered Cayley energy for all intended designs
        -> complete fourth-moment control
        -> new local-law/comparison mechanism
        -> microscopic BGS/GOE.
```
