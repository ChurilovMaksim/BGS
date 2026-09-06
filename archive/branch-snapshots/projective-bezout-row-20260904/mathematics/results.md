# Current results and exact scope

This is the concise theorem index. The repository-wide status authority is
[`../record/claim_ledger.md`](../record/claim_ledger.md); historical commits or
notes do not override it.

## 1. Pair-key and fourth-moment reduction — EXACT

For odd prime `p` and `x,y in F_p\{0,1}`, the key

```text
u=x/y,  v=(x-1)/(y-1),  d=x-y
```

is an off-diagonal bijection with inverse

```text
y=(1-v)/(u-v),
x=u(1-v)/(u-v),
d=(u-1)(v-1)/(v-u).
```

The diagonal has multiplicity `p-2`; subgroup constraints give exactly
`(K-1)(K-2)` off-diagonal pairs. The corrected fourth-moment distribution is

```text
B(t)=O(t)+2(p-2)C_H(t)+(p-2)^2 1_{t=0},
```

and

```text
|V4|=(K^2+1)p^2-(6K^2+3K)p+13K^2-3K.
```

Finite Fourier orthogonality gives the exact nonzero-frequency mean/variance
identities. See [`fourth_moment_reduction.md`](fourth_moment_reduction.md).

## 2. Cayley additive-energy reduction — EXACT

For

```text
c(h)=(h+1)/(h-1),
A=c(H\{1}),
```

one has

```text
d(u,v)=2/(c(u)-c(v)),
c(h^-1)=-c(h).
```

Thus the mixed layer is governed by `E_+(A)`. For odd prime `K`, Chowla
cotangent independence implies that in characteristic zero every nonzero
equal-difference collision is identity or central inversion-swap.

See [`cayley_additive_energy.md`](cayley_additive_energy.md).

## 3. Direct pointwise Cayley bound — EXACT + EXTERNAL-THEOREM

For

```text
100<K<p^(3/4)/3,
```

the Cayley sum fiber is an absolutely irreducible bilinear curve. A source-exact
application of Vyugin--Makarychev gives

```text
E_+(A)<34K^(8/3),
```

and mixed centered variance `<136pK^(8/3)`. See
[`cayley_direct_energy.md`](cayley_direct_energy.md).

## 4. Sharp pointwise centered target — OPEN globally

Exactly

```text
E_+(A)=|A|^4/p+(1/p)sum_{q!=0}|1_Ahat(q)|^4.
```

The target for every intended split design is

```text
E_+(A)=(K-1)^4/p+O(K^(2+o(1))).
```

It is now proved on the explicit subfamily `p does not divide G'_K^(3)` below;
the higher-row exceptional support remains open.

See [`cayley_centered_energy.md`](cayley_centered_energy.md).

## 5. Shifted-energy orbit reduction — EXACT / EXTERNAL-THEOREM

For `lambda!=0`, let `T_(lambda H)` be the Cayley parameter orbit from

```text
mu in lambda H, mu!=-1,
t=2mu/(1+mu).
```

If `r(t)=#{(a,b) in A^2:a+b=t}` and `D_K=2K^2-K`, then

```text
sum_{t in T_(lambda H)}r(t)^2
 <=2(E_x(H+lambda)-D_K).
```

Shkredov's shifted-subgroup theorem gives, for `K^2<p`,

```text
sum_{t in T_C}r(t)^2 << K^2 log K
```

for every nonzero coset `C` of `H`. Also exactly

```text
sum_{lambda in F_p}(E_x(H+lambda)-D_K)=K^4-E_+(H).
```

Naive summation therefore gives only `O(K^3)` globally and does not improve the
maintained `K^(8/3)` theorem by itself.

See [`cayley_shifted_energy_orbits.md`](cayley_shifted_energy_orbits.md).

## 6. Fixed-product row decomposition — EXACT

For one valid pair put `u=xy`, `s=x+y`. Then

```text
c(x)+c(y)=2(u-1)/(u-s+1).
```

For fixed `u` and nonzero Cayley parameter `t`, the sum `s` is fixed, hence
there is at most one unordered subgroup pair in that row. If `T_u` is the
nonzero parameter set of row `u` and `omega_u(t)` is `1` for a diagonal pair
and `2` otherwise, then for odd prime `K` and split prime `p`

```text
Delta_K(p)
 =2 sum_{u<v} sum_{t in T_u cap T_v} omega_u(t)omega_v(t).
```

Consequently, with

```text
I_K(p)=max_{u!=v}|T_u cap T_v|,
```

one has exactly

```text
Delta_K(p)<=4I_K(p)(K-1)(K-2).
```

For `xy=w^2`, `x=wz`, `y=wz^-1`, a common parameter between rows `w^2,q^2`
becomes the constrained affine trace-set equation

```text
Y=alpha X+beta,
X=z+z^-1,
Y=y+y^-1,
alpha=(q-q^-1)/(w-w^-1),
beta=2(w/q-q/w)/(w-w^-1).
```

See [`cayley_product_row_intersections.md`](cayley_product_row_intersections.md).

## 7. Order-three product-row subresultant theorem — EXACT + EXTERNAL-THEOREM

For odd prime `K`, let `zeta` be a primitive `K`-th root of unity and
`m=(K-1)/2`. A noncentral product row indexed by `i` has homogeneous form

```text
R_i(U,V)=prod_a(D_(i,a)U-N_iV),
N_i=1-zeta^(2i),
D_(i,a)=zeta^i(zeta^a+zeta^(-a))-2,
```

where the invalid trace class `a=+-i` is omitted. Its projective roots are
exactly the valid nonzero Cayley parameters in the coordinate
`mu=t/(2-t)`; `t=2` is the point at infinity.

Galois scaling normalizes a distinct row pair `(i,j)` to `(1,r)` with `r=j/i`.
Let `S_0,S_1,S_2` be the first three fixed-degree subresultants of the two row
polynomials and define

```text
G'_(K,r)^(3)
```

as the gcd of the absolute cyclotomic norms of all their nonzero coefficients,
after removing factors `2` and `K`. Let

```text
G'_K^(3)=prod_[r]G'_(K,r)^(3)
```

over unordered ratio classes.

Brown--Traub's subresultant theorem yields the exact implication

```text
I_(i,j)(p)>=3  ==>  p|G'_(K,r)^(3).
```

Therefore every split prime satisfying

```text
p does not divide G'_K^(3)
```

obeys

```text
I_K(p)<=2,
Delta_K(p)<=8(K-1)(K-2),
E_+(A)<=11(K-1)(K-2).
```

So the pointwise quadratic Cayley-energy scale is already closed on this
explicit arithmetic subfamily.

Exact CI anchors include

```text
G'_(7,2)^(3)=1,
G'_(11,2)^(3)=1,
G'_(13,3)^(3)=3^3,
G'_(13,12)^(3)=5^8,
G'_(17,10)^(3)=103^2.
```

The remaining growing-`K` problem is to control eligible split prime divisors of
`G'_K^(3)`. A bound

```text
P_split^+(G'_K^(3))<=K^(4+o(1))
```

would close the pointwise Cayley-energy target throughout `K=o(p^(1/4))`.
This divisor bound is **OPEN**.

See [`cayley_product_row_subresultants.md`](cayley_product_row_subresultants.md).

## 8. Square resultants and Fibonacci obstruction — EXACT

For every admissible prime-order cleared collision polynomial,

```text
P(X)=(X-1)^3Q(X),
Q(X^-1)=X^(3-T)Q(X),
Res(Phi_K,P)=K^3M^2.
```

Thus `K^3p^2>12^(K-1)` excludes every non-forced split reduction. The explicit
Fibonacci slice satisfies

```text
Res(Phi_K,X^2+3X+1)=F_K^2,
```

so norm-only polynomial bounds are impossible. The associated rational model
has exact excess `32`, and the 28-digit `(K,p)=(131,F_131)` finite certificate
also has excess `32`.

See [`cayley_resultant_structure.md`](cayley_resultant_structure.md) and
[`fibonacci_ratio_energy_proof.md`](fibonacci_ratio_energy_proof.md).

## 9. Canonical additive discriminant — EXACT

A single primitive squarefree difference polynomial `S_K` classifies split
additive exceptions:

```text
Delta_K(p)>0 iff p|Disc(S_K),
Delta_K(p)<=4v_p(Disc(S_K)).
```

See [`cayley_difference_discriminant.md`](cayley_difference_discriminant.md).

## 10. Ratio-orbit and fourth-power discriminant structure — EXACT

The difference polynomial factors into `(K-1)/2` ratio-orbit factors `F_r` with
exact cross-resultant squares and

```text
|Disc(F_r)|=2^((K-1)^2)K^(K-2)I_r^4.
```

Globally,

```text
|Disc(S_K)|
 =2^((K-1)^4/4)K^((K-1)(K^2-7)/4)J_K^4.
```

All split discriminant valuations are multiples of four. Exact larger-`K` tests
falsify the former `O(K^3 log K)` residual-height heuristic: genuine
`K^4`-scale archimedean mass remains.

See [`cayley_ratio_orbit_factorization.md`](cayley_ratio_orbit_factorization.md).

## 11. Multiplicative Cayley rigidity and discriminant — EXACT

Characteristic-zero product collisions are exactly swap and simultaneous
inversion, so

```text
E_x(A_K)=4(K-1)(K-2).
```

A canonical product polynomial similarly satisfies

```text
Delta_K^x(p)>0 iff p|Disc(S_K^x),
Delta_K^x(p)<=16v_p(Disc(S_K^x)).
```

This is independent structure, not an additive-transfer theorem. See
[`cayley_multiplicative_rigidity.md`](cayley_multiplicative_rigidity.md) and
[`cayley_product_discriminant.md`](cayley_product_discriminant.md).

## 12. Global split-prime additive mass budget — EXACT

For odd prime `K`,

```text
sum_{p==1 mod K}Delta_K(p)log p
 <=(K^3-5K^2+6K+1)((K-1)log12-3logK).
```

This is a deterministic `O(K^4)` logarithmic budget over all split rational
primes. See [`cayley_resultant_mass_budget.md`](cayley_resultant_mass_budget.md).

## 13. Full Cayley/Jacobi trace identity — EXACT

For the normalized full annihilator twisted-Jacobi matrix `M_S(q)`,

```text
1_Ahat(r)=K Tr M_S(2r),
```

and

```text
sum_q|Tr M_S(q)|^2=p(K-1)/K^2,
sum_q|Tr M_S(q)|^4=pE_+(A)/K^4.
```

This is the ordinary full trace and does not revive the retracted historical
noncommutative trace shortcut. See
[`cayley_jacobi_trace_average.md`](cayley_jacobi_trace_average.md).

## 14. Double-averaged quadratic excess — EXACT + EXTERNAL-THEOREM

For fixed `0<theta<1/3`, prime `K~X^theta`, prime `p~X`, `p==1 mod K`,
Bombieri--Vinogradov plus PNT gives

```text
average Delta_K(p)/K^2 <<_theta X^(3theta-1)->0.
```

The full ordinary Jacobi-trace second/fourth moment ratio tends to `3` in the
same double average. This is not a CLT and not microscopic BGS.

## 15. Almost-all exact Cayley baseline — EXACT + EXTERNAL-THEOREM

Using integrality of `Delta_K(p)`, for the same dyadic design family

```text
#bad/#all <<_theta X^(5theta-1).
```

Hence for fixed `0<theta<1/5`, asymptotically almost every split pair has

```text
Delta_K(p)=0,
E_+(A)=3(K-1)(K-2)
```

exactly. See [`cayley_exact_baseline_density.md`](cayley_exact_baseline_density.md).

## 16. Corrected off/off elliptic theorem — EXACT + EXTERNAL-THEOREM

Every generic off/off parameter class has a distinguished reducible fiber with
exact valid count

```text
O_lambda(t_lambda)=2p-8.
```

After extracting these spikes, Igusa monodromy and
Grothendieck--Lefschetz/Deligne quasi-orthogonality yield

```text
Var_{t!=0}O(t)
 << pE_+(A)+K^2p+K^4sqrt(p)+K^4.
```

Thus the off/off layer has collapsed onto the same pointwise Cayley-energy
bottleneck. See [`offoff_elliptic_spike_theorem.md`](offoff_elliptic_spike_theorem.md).

## 17. Adversarial finite controls

Promoted checks include:

- complete additive exceptional sets `E_11={23,67,89}` and
  `E_13={53,79,131,157,313}`;
- `(p,K)=(461,23)` with additive energy `1190` versus forced baseline `902`;
- `(K,p)=(29,728017)` and `(31,1042903)`, both with `p>K^4` but non-forced
  Cayley excess `48`, falsifying any bare `p>K^4 => exact baseline` rule;
- `(K,p)=(41,2908049)` with a row pair sharing two parameters, falsifying the
  exploratory `I_K(p)<=1` claim;
- the order-three subresultant anchors above. A slower independent check gives
  `G'_(23,18)^(3)=47^20*139^2`, with row intersections of sizes `5` at `p=47`
  and `3` at `p=139`.

Finite computation proves only these finite assertions.

## 18. Earlier scoped foundations / retractions

Earlier torus, branch-scale, twisted-Jacobi and antiunitary facts remain at
their audited finite or logical scope. Historical all-orders Catalan/arcsine
promotion, the noncommutative trace shortcut, unsupported higher-rank
extrapolations, the former spike-free off/off theorem and the residual-height
`O(K^3 log K)` heuristic are not active. See
[`../record/retractions.md`](../record/retractions.md).

## 19. Microscopic BGS/GOE — OPEN

No theorem in this repository proves a mean-spacing local eigenphase law. Even
closing the higher-row divisor problem and the complete fourth-moment layer
would leave a separate local-statistics/comparison problem.

The current frontier is

```text
split support of G'_K^(3)
        -> pointwise centered Cayley energy for all intended designs
        -> complete fourth-moment control
        -> new local-law/comparison mechanism
        -> microscopic BGS/GOE.
```
