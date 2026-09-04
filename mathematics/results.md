# Current results and exact scope

This is the concise theorem index.  The repository-wide status authority is
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
`(K-1)(K-2)` off-diagonal pairs.  The corrected fourth-moment distribution is

```text
B(t)=O(t)+2(p-2)C_H(t)+(p-2)^2 1_{t=0},
```

with

```text
|V4|=(K^2+1)p^2-(6K^2+3K)p+13K^2-3K.
```

Finite Fourier orthogonality gives the exact nonzero-frequency mean/variance
identities.  See [`fourth_moment_reduction.md`](fourth_moment_reduction.md).

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

Thus the mixed layer is the additive energy of `A`.  For odd prime `K`,
Chowla cotangent independence implies that in characteristic zero every
nonzero equal-difference collision is identity or central inversion-swap.

See [`cayley_additive_energy.md`](cayley_additive_energy.md).

## 3. Direct pointwise Cayley bound — EXACT + EXTERNAL-THEOREM

For

```text
100<K<p^(3/4)/3,
```

the Cayley sum fiber is an absolutely irreducible bilinear curve.  A
source-exact application of Vyugin--Makarychev gives

```text
E_+(A)<34K^(8/3),
```

and the mixed centered variance is `<136pK^(8/3)` in the repository
normalization.  See [`cayley_direct_energy.md`](cayley_direct_energy.md).

## 4. Sharp pointwise centered target — OPEN

Exactly

```text
E_+(A)=|A|^4/p+(1/p)sum_{q!=0}|1_Ahat(q)|^4.
```

The pointwise closure target is

```text
E_+(A)=(K-1)^4/p+O(K^(2+o(1))),
```

or equivalently

```text
sum_{q!=0}|1_Ahat(q)|^4 << pK^(2+o(1)).
```

The current uniform loss is `K^(2/3)`.  See
[`cayley_centered_energy.md`](cayley_centered_energy.md).

## 5. Shifted-energy orbit reduction — EXACT / EXACT + EXTERNAL-THEOREM

For `lambda!=0`, let `T_(lambda H)` be the Cayley parameter orbit obtained from

```text
mu in lambda H,  mu!=-1,
t=2mu/(1+mu).
```

If `r(t)=#{(a,b) in A^2:a+b=t}` and `D_K=2K^2-K`, then exactly

```text
sum_{t in T_(lambda H)} r(t)^2
 <=2(E_x(H+lambda)-D_K).
```

Shkredov's shifted-subgroup theorem therefore gives, for `K^2<p`,

```text
sum_{t in T_C} r(t)^2 << K^2 log K
```

for every nonzero multiplicative coset `C` of `H`.

There is also the exact global identity

```text
sum_{lambda in F_p}(E_x(H+lambda)-D_K)=K^4-E_+(H).
```

Summing the orbit theorem alone yields only `O(K^3)` global Cayley energy away
from `t=0,2`, so this reformulation does **not** improve the maintained
`K^(8/3)` theorem by itself.  Its value is local: it isolates the missing
cross-orbit distribution problem.

See [`cayley_shifted_energy_orbits.md`](cayley_shifted_energy_orbits.md).

## 6. Square resultants and Fibonacci obstruction — EXACT

For every admissible prime-order cleared collision polynomial,

```text
P(X)=(X-1)^3Q(X),
Q(X^-1)=X^(3-T)Q(X),
Res(Phi_K,P)=K^3M^2.
```

Thus `K^3p^2>12^(K-1)` excludes every non-forced split reduction.  The explicit
Fibonacci slice satisfies

```text
Res(Phi_K,X^2+3X+1)=F_K^2,
```

so norm-only polynomial bounds are impossible.  The associated rational model
has exact excess `32`, and the 28-digit `(K,p)=(131,F_131)` finite certificate
also has excess `32`.

See [`cayley_resultant_structure.md`](cayley_resultant_structure.md) and
[`fibonacci_ratio_energy_proof.md`](fibonacci_ratio_energy_proof.md).

## 7. Canonical additive discriminant — EXACT

A single primitive squarefree difference polynomial `S_K` classifies split
additive exceptions:

```text
Delta_K(p)>0 iff p|Disc(S_K),
Delta_K(p)<=4 v_p(Disc(S_K)).
```

See [`cayley_difference_discriminant.md`](cayley_difference_discriminant.md).

## 8. Ratio-orbit / fourth-power discriminant structure — EXACT

The canonical difference polynomial factors into `(K-1)/2` ratio-orbit factors
`F_r`, with exact cross-resultant squares and

```text
|Disc(F_r)|=2^((K-1)^2)K^(K-2)I_r^4,
```

hence

```text
|Disc(S_K)|
 =2^((K-1)^4/4)
  K^((K-1)(K^2-7)/4)
  J_K^4.
```

All split discriminant valuations are therefore multiples of four.  Exact
larger-`K` tests falsify the former `O(K^3 log K)` residual-height heuristic:
cross-resultants retain genuine `K^4`-scale archimedean mass.

See [`cayley_ratio_orbit_factorization.md`](cayley_ratio_orbit_factorization.md).

## 9. Multiplicative Cayley rigidity and discriminant — EXACT

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

This is independent structure, not an additive-transfer theorem.  See
[`cayley_multiplicative_rigidity.md`](cayley_multiplicative_rigidity.md) and
[`cayley_product_discriminant.md`](cayley_product_discriminant.md).

## 10. Global split-prime additive mass budget — EXACT

For odd prime `K`,

```text
sum_{p==1 mod K} Delta_K(p) log p
 <=(K^3-5K^2+6K+1)((K-1)log12-3logK).
```

This is a deterministic `O(K^4)` logarithmic budget over all split rational
primes.  See [`cayley_resultant_mass_budget.md`](cayley_resultant_mass_budget.md).

## 11. Full Cayley/Jacobi trace identity — EXACT

For the normalized full annihilator twisted-Jacobi matrix `M_S(q)`,

```text
1_Ahat(r)=K Tr M_S(2r),
```

and exactly

```text
sum_q |Tr M_S(q)|^2=p(K-1)/K^2,
sum_q |Tr M_S(q)|^4=pE_+(A)/K^4.
```

This is the ordinary full trace; it does not revive the retracted historical
noncommutative trace shortcut.  See
[`cayley_jacobi_trace_average.md`](cayley_jacobi_trace_average.md).

## 12. Double-averaged quadratic excess — EXACT + EXTERNAL-THEOREM

For fixed `0<theta<1/3`, prime `K~X^theta`, prime `p~X`, `p==1 mod K`,
Bombieri--Vinogradov plus PNT gives

```text
average Delta_K(p)/K^2 <<_theta X^(3theta-1)->0.
```

The full ordinary Jacobi-trace second/fourth moment ratio tends to `3` in the
same double average.  This is not a CLT and not microscopic BGS.

## 13. Almost-all exact Cayley baseline — EXACT + EXTERNAL-THEOREM

Using integrality of `Delta_K(p)`, for the same dyadic design family

```text
#bad/#all <<_theta X^(5theta-1).
```

Hence for every fixed `0<theta<1/5`, asymptotically almost every split pair has

```text
Delta_K(p)=0,
E_+(A)=3(K-1)(K-2)
```

exactly.  See
[`cayley_exact_baseline_density.md`](cayley_exact_baseline_density.md).

## 14. Corrected off/off elliptic theorem — EXACT + EXTERNAL-THEOREM

Every generic off/off parameter class has a distinguished reducible fiber with
exact valid count

```text
O_lambda(t_lambda)=2p-8.
```

The other four finite singular fibers are simple multiplicative fibers, and the
finite singular support recovers the generic parameter up to

```text
(h1,h2)<->(h2^(-1),h1^(-1)).
```

After extracting the spikes, Igusa monodromy and
Grothendieck--Lefschetz/Deligne quasi-orthogonality yield

```text
Var_{t!=0}O(t)
 << pE_+(A)+K^2p+K^4sqrt(p)+K^4.
```

Thus the off/off layer has collapsed onto the same pointwise Cayley-energy
bottleneck.  In `K=o(p^(1/4))`, the maintained direct bound gives
`Var O<<pK^(8/3)`.

See [`offoff_elliptic_spike_theorem.md`](offoff_elliptic_spike_theorem.md).

## 15. Finite certificates / adversarial regressions

Promoted finite checks include:

- pair-key and fourth-moment anchors at `(53,13)`;
- complete additive exceptional sets `E_11={23,67,89}` and
  `E_13={53,79,131,157,313}`;
- `(p,K)=(461,23)` with additive energy `1190` versus forced baseline `902`;
- the 28-digit Fibonacci-slice certificate;
- additive/product discriminant and ratio-orbit symbolic regressions;
- the corrected elliptic `2p-8` spike regression;
- shifted-energy orbit checks at `(199,11)`, `(461,23)`, and the large split
  exceptions `(728017,29)`, `(1042903,31)`.  The last two satisfy `p>K^4` and
  have non-forced Cayley excess `48`, so `p>K^4` alone does not imply exact
  baseline.

Finite computation proves only the stated finite assertions.

## 16. Current high-value unproved row-intersection target

Grouping valid subgroup pairs by product `xy=w^2` rewrites a common Cayley
parameter between two distinct product rows `w^2` and `q^2` as

```text
Y=alpha X+beta,
X=z+z^(-1), Y=y+y^(-1),
alpha=w(1-q^2)/(q(1-w^2)),
beta=2(q^2-w^2)/(q(1-w^2)).
```

If every two distinct product rows had `O(1)` common parameters in the
polynomial-size split-prime regime, the non-forced Cayley energy would be
`O(K^2)`.  This is **OPEN**.  Finite sweeps motivate it but are not promoted to
a theorem; in particular the stronger tentative bound `<=1` is false (for
example `(K,p)=(41,2908049)` has a row pair with two common parameters).

## 17. Earlier scoped foundations / retractions

Earlier torus, branch-scale, twisted-Jacobi and antiunitary facts remain at
their audited finite or logical scope.  Historical all-orders Catalan/arcsine
promotion, the noncommutative trace shortcut, unsupported higher-rank
extrapolations, the former spike-free off/off theorem and the residual-height
`O(K^3 log K)` heuristic are not active.  See
[`../record/retractions.md`](../record/retractions.md).

## 18. Microscopic BGS/GOE — OPEN

No theorem in this repository proves a mean-spacing local eigenphase law.
Even a pointwise quadratic Cayley-energy theorem and complete fourth-moment
control would leave a separate local-statistics/comparison problem.

The exact frontier is

```text
pointwise centered Cayley energy
        -> complete fourth-moment control
        -> new local-law/comparison mechanism
        -> microscopic BGS/GOE.
```
