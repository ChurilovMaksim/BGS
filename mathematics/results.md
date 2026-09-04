# Current results and exact scope

This is the concise theorem index.  The repository-wide status authority is
[`../record/claim_ledger.md`](../record/claim_ledger.md); historical commits or
notes do not override it.

## 1. Pair-key geometry — EXACT

For odd prime `p` and `x,y in F_p\{0,1}`, set

```text
u=x/y,
v=(x-1)/(y-1),
d=x-y.
```

Off the diagonal this is a bijection onto
`u,v in F_p^*\{1}`, `u!=v`, with

```text
y=(1-v)/(u-v),
x=u(1-v)/(u-v),
d=(u-1)(v-1)/(v-u).
```

The diagonal collapses to `(1,1,0)` with multiplicity `p-2`.  If the two
constraints are `u,v in H`, `|H|=K`, the number of admissible off-diagonal
ordered pairs is exactly `(K-1)(K-2)`.

## 2. Fourth-moment coupling — EXACT

The corrected weighted difference distribution is

```text
B(t)=O(t)+2(p-2)C_H(t)+(p-2)^2 1_{t=0},
```

and

```text
|V4|=(K^2+1)p^2-(6K^2+3K)p+13K^2-3K.
```

With `Sigma4(q)=sum_t B(t)e_p(qt)`, finite Fourier orthogonality gives

```text
E_{q!=0} Sigma4(q)=(pZ-V)/(p-1),
Var_{q!=0} Sigma4(q)=p Var_{t!=0}B(t).
```

No stochastic-independence hypothesis enters.

See [`fourth_moment_reduction.md`](fourth_moment_reduction.md).

## 3. Cayley mixed reduction — EXACT

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

Thus the mixed term is governed by the additive energy `E_+(A)`.  The
centrally symmetric characteristic-zero relations force the nonzero baseline

```text
(K-1)(2K-5).
```

See [`cayley_additive_energy.md`](cayley_additive_energy.md).

## 4. Direct pointwise Cayley bound — EXACT + EXTERNAL-THEOREM

For every odd prime `p` and subgroup `H<=F_p^*` of order

```text
100<K<p^(3/4)/3,
```

the Cayley sum fiber is the absolutely irreducible bilinear curve

```text
(2-t)xy+t(x+y)-(2+t)=0.
```

A source-exact application of Vyugin--Makarychev gives

```text
E_+(A)<34K^(8/3).
```

The mixed centered variance in the repository normalization is therefore
`<136pK^(8/3)`.

See [`cayley_direct_energy.md`](cayley_direct_energy.md).

## 5. Sharp pointwise target — OPEN

For every `A subset F_p`,

```text
E_+(A)=|A|^4/p+(1/p)sum_{q!=0}|1_Ahat(q)|^4.
```

The natural pointwise Cayley target is

```text
E_+(A)=(K-1)^4/p+O(K^(2+o(1))),
```

or equivalently

```text
sum_{q!=0}|1_Ahat(q)|^4 << pK^(2+o(1)).
```

This remains open.  The remaining loss in the current uniform theorem is
`K^(2/3)`.

See [`cayley_centered_energy.md`](cayley_centered_energy.md).

## 6. Prime-order characteristic-zero additive rigidity — EXACT

For odd prime `K`, Chowla's rational independence of
`cot(pi*a/K)`, `1<=a< K/2`, turns the characteristic-zero Cayley set into a
rational cross-polytope.  Every equal-difference collision is either identity
or central inversion-swap.  No finite enumeration in `K` is used.

## 7. Square collision resultants — EXACT

For each admissible cleared collision polynomial `P`,

```text
P(X)=(X-1)^3Q(X),
Q(X^-1)=X^(3-T)Q(X),
Res(Phi_K,P)=K^3M^2,
```

with `M in Z`.  Hence if `K|p-1`, `K` is odd prime, and

```text
K^3 p^2 > 12^(K-1),
```

then every finite-field additive collision is forced.

See [`cayley_resultant_structure.md`](cayley_resultant_structure.md).

## 8. Fibonacci slice — EXACT + FINITE-CERTIFICATE

The collision

```text
c(h^2)-c(h)=c(h)-c(h^-1)
```

is equivalent to `h^2+3h+1=0`, and for every odd prime `K`,

```text
Res(Phi_K(X),X^2+3X+1)=F_K^2.
```

Thus norm-only attempts to make every collision resultant polynomially small
cannot work.  Nevertheless the rational model

```text
S_N={+-L_n/F_n:1<=n<=N}
```

has exact nonzero difference energy

```text
2N(4N-3)+32,  N>=3.
```

At `K=131`, `p=F_131`, the exact 28-digit finite-field witness has excess `32`.

See [`fibonacci_ratio_energy_proof.md`](fibonacci_ratio_energy_proof.md).

## 9. Canonical additive difference discriminant — EXACT

Let `S_K` be the canonical primitive squarefree polynomial whose roots are the
distinct nonzero characteristic-zero Cayley differences.  For every split
prime `p==1 mod K`,

```text
Delta_K(p)>0  iff  p | Disc(S_K),
Delta_K(p) <= 4 v_p(Disc(S_K)).
```

Thus all non-forced additive reductions are compressed into one integer.

See [`cayley_difference_discriminant.md`](cayley_difference_discriminant.md).

## 10. Ratio-orbit and fourth-power discriminant structure — EXACT

The polynomial `S_K` factors into `(K-1)/2` ratio-orbit factors `F_r`.  The
project proves exact cross-resultant square formulas and

```text
|Disc(F_r)|=2^((K-1)^2) K^(K-2) I_r^4.
```

Globally,

```text
|Disc(S_K)|
 =2^((K-1)^4/4)
  K^((K-1)(K^2-7)/4)
  J_K^4.
```

Hence every split-prime discriminant valuation is divisible by four.  Exact
cross-resultant computations through `K=47` also falsify the earlier heuristic
that the residual prime-to-`2K` logarithmic mass should be only
`O(K^3 log K)`: genuine `K^4`-scale archimedean mass remains.

See [`cayley_ratio_orbit_factorization.md`](cayley_ratio_orbit_factorization.md).

## 11. Characteristic-zero multiplicative Cayley rigidity — EXACT

Every characteristic-zero product collision is generated by swap and
simultaneous inversion.  Consequently

```text
E_x(A_K)=4(K-1)(K-2).
```

See [`cayley_multiplicative_rigidity.md`](cayley_multiplicative_rigidity.md).

## 12. Canonical multiplicative discriminant — EXACT

For the canonical squarefree product polynomial `S_K^x` and every split prime,

```text
Delta_K^x(p)>0  iff  p | Disc(S_K^x),
Delta_K^x(p) <= 16 v_p(Disc(S_K^x)).
```

This is independent exact structure; it is not presented as a transfer theorem
for additive energy.

See [`cayley_product_discriminant.md`](cayley_product_discriminant.md).

## 13. Global split-prime additive mass budget — EXACT

For odd prime `K`, define

```text
Delta_K(p)=sum_{d!=0}r_{A-A}(d)^2-(K-1)(2K-5).
```

Then

```text
sum_{p==1 mod K} Delta_K(p) log p
 <=(K^3-5K^2+6K+1)((K-1)log12-3logK).
```

This is a deterministic `O(K^4)` logarithmic budget over all split rational
primes.

See [`cayley_resultant_mass_budget.md`](cayley_resultant_mass_budget.md).

## 14. Full Cayley/Jacobi trace identity — EXACT

Let `S=H^perp` and define the normalized full annihilator twisted-Jacobi matrix
`M_S(q)` in the maintained convention.  Then

```text
1_Ahat(r)=K Tr M_S(2r),
```

and exactly

```text
sum_q |Tr M_S(q)|^2 = p(K-1)/K^2,
sum_q |Tr M_S(q)|^4 = pE_+(A)/K^4.
```

This is an ordinary full trace identity and does not use the retracted
historical noncommutative trace shortcut.

See [`cayley_jacobi_trace_average.md`](cayley_jacobi_trace_average.md).

## 15. Double-averaged quadratic excess — EXACT + EXTERNAL-THEOREM

Fix `0<theta<1/3`, let `K~X^theta`, `p~X`, with both prime and `p==1 mod K`.
Bombieri--Vinogradov and PNT, applied after averaging over the varying moduli
`K`, give

```text
average Delta_K(p)/K^2 <<_theta X^(3theta-1) -> 0.
```

Thus for every fixed `eta>0`, the proportion of split pairs with
`Delta_K(p)>=eta K^2` tends to zero.  The corresponding full Jacobi trace
second/fourth moment ratio tends in double average to `3`.

This is not a CLT and not microscopic BGS.

## 16. Almost-all exact Cayley baseline — EXACT + EXTERNAL-THEOREM

Because `Delta_K(p)` is a nonnegative integer, the same global mass budget also
counts bad designs.  For the dyadic split family and fixed `0<theta<1/2`,

```text
#bad <<_theta X^(5theta)/(log X)^2,
#bad/#all <<_theta X^(5theta-1).
```

Consequently, for every fixed

```text
0<theta<1/5,
```

asymptotically almost every split pair has

```text
Delta_K(p)=0
```

exactly and therefore

```text
E_+(A)=3(K-1)(K-2).
```

See [`cayley_exact_baseline_density.md`](cayley_exact_baseline_density.md).

## 17. Corrected off/off elliptic theorem — EXACT + EXTERNAL-THEOREM

For the generic off/off parameter class `lambda=(h1,h2)`, put

```text
alpha=c(h1),
beta=c(h2),
d=alpha-beta.
```

The genus-one pencil has a distinguished reducible fiber at

```text
t_lambda=2/d
```

and after all valid-domain exclusions

```text
O_lambda(t_lambda)=2p-8.
```

The four remaining finite bad fibers are simple multiplicative fibers.  The
finite singular support recovers the generic parameter up to the involution

```text
(h1,h2) <-> (h2^(-1),h1^(-1)).
```

After extracting the reducible spikes, Igusa geometric monodromy together with
Grothendieck--Lefschetz and Deligne quasi-orthogonality gives

```text
Var_{t!=0} O(t)
 << pE_+(A)+K^2p+K^4sqrt(p)+K^4.
```

The old unconditional spike-free target
`O(K^2p+K^4sqrt(p)+K^4)` is superseded.  Combining the corrected theorem with
the direct Cayley estimate yields

```text
Var O << pK^(8/3)+K^4sqrt(p)+K^2p+K^4,
```

and hence `Var O << pK^(8/3)` in `K=o(p^(1/4))`.

See [`offoff_elliptic_spike_theorem.md`](offoff_elliptic_spike_theorem.md).

## 18. Finite certificates and regression anchors

Promoted finite statements include:

- exact pair-key and fourth-moment anchors at `(53,13)`;
- complete additive exceptional sets `E_11={23,67,89}` and
  `E_13={53,79,131,157,313}`;
- `(p,K)=(461,23)` with exact additive energy `1190` versus baseline `902`;
- the 28-digit Fibonacci-slice witness with excess `32`;
- exact symbolic/finite checks for additive/product discriminants,
  ratio-orbit fourth-power structure and the elliptic `2p-8` spike.

Finite computations support these finite statements only; they are not used as
proofs of the universal theorems above.

## 19. Earlier scoped foundations

Earlier torus, branch-scale, twisted-Jacobi and antiunitary facts are retained
at their audited finite or logical scope.  Historical all-orders
Catalan/arcsine promotion, the noncommutative trace shortcut, unsupported
higher-rank extrapolations and the former spike-free off/off theorem are not
active claims.  See [`../record/retractions.md`](../record/retractions.md).

## 20. Microscopic BGS/GOE — OPEN

No current theorem in this repository proves a mean-spacing local eigenphase
law.  Completing the pointwise Cayley energy and the full fourth-moment layer
would still leave a separate local-statistics/comparison problem.

The exact current frontier is therefore:

```text
pointwise centered Cayley energy
        -> complete fourth-moment control
        -> NEW local-law/comparison mechanism
        -> microscopic BGS/GOE.
```
