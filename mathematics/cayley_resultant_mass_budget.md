# Global resultant budget for non-forced Cayley collision mass

**Status: EXACT for odd prime subgroup order `K`; FINITE-REGRESSION for the maintained `K=11,13` exceptional sets.**

This note extracts an averaged theorem stronger than treating each collision
resultant independently.  The two structural inputs are:

1. quotient collision quadruples by simultaneous Galois scaling of their
   exponents;
2. use the exact square structure `Res(Phi_K,P)=K^3 M^2` to remove the inert
   `K^3` factor from every split-prime collision budget.

The result does **not** replace the pointwise theorem in
[`cayley_direct_energy.md`](cayley_direct_energy.md).  It gives a global
arithmetic budget for the total non-forced energy carried by all split primes.

## 1. Setup and excess energy

Let `K` be an odd prime.  For a rational prime

```text
p == 1 (mod K),
```

let `H<=F_p^*` be the unique subgroup of order `K`, and put

```text
A=c(H\{1}),
c(h)=(h+1)/(h-1).
```

Let

```text
E_K(p)=sum_{d!=0} r_{A-A}(d)^2
```

be the nonzero difference energy. Identity and central inversion force

```text
B_K=(K-1)(2K-5).
```

Define

```text
Delta_K(p)=E_K(p)-B_K >= 0.                              (1)
```

Because `B_K` is exactly the size of the union of the identity and
inversion-swap collision relations, `Delta_K(p)` literally counts ordered
collision quadruples outside those forced relations.

## 2. Galois scaling orbits

Index the elements of `A` by nonzero residues modulo `K`. An admissible
collision quadruple is

```text
q=(i,j,r,s),
i,j,r,s in F_K^*,
i!=j,
r!=s.
```

The group `F_K^*` acts freely by

```text
a*q=(a i,a j,a r,a s).                                  (2)
```

Every orbit has size `K-1` and a unique representative with `i=1`.

There are

```text
M=(K-1)(K-2)
```

ordered nonzero difference pairs.  The full collision-pair space has size
`M^2`, while the forced union has size `B_K`. Hence the number of non-forced
scaling orbits is

```text
N_K=(M^2-B_K)/(K-1)
   =(K-1)(K-2)^2-(2K-5)
   =K^3-5K^2+6K+1.                                      (3)
```

For `K=11,13`, this is exactly `793,1431`, agreeing with the maintained
normalized resultant enumeration.

## 3. One resultant controls a whole orbit

For a normalized non-forced representative `q=(i,j,r,s)`, let `P_q(X)` be the
cleared Cayley collision polynomial

```text
P_q(X)
 = X^(r+s+i)-X^(r+s+j)-X^(r+i+j)+2X^(r+j)-X^r
   +X^(s+i+j)-2X^(s+i)+X^s+X^i-X^j,
```

with exponents reduced modulo `K` after collecting terms, and put

```text
R_q=Res(Phi_K,P_q).                                      (4)
```

Prime-order characteristic-zero rigidity gives `R_q!=0`.  The coefficient
bound gives

```text
|R_q|<=12^(K-1).                                        (5)
```

The square-resultant theorem gives more:

```text
R_q=K^3 M_q^2,   M_q in Z\{0}.                           (6)
```

Fix a split prime `p==1 (mod K)` and a generator `h` of `H`.  The roots of
`Phi_K` modulo `p` are

```text
h^a,  a in F_K^*.
```

For a given `a`,

```text
P_q(h^a)=0                                               (7)
```

is exactly the Cayley collision attached to the scaled quadruple `a*q`.
Therefore the number of colliding members of this orbit is

```text
s_q(p)=#{a in F_K^*:P_q(h^a)=0}.                         (8)
```

Because `p!=K`, `Phi_K` is separable modulo `p` and splits completely.  Lift
its simple roots to `Z_p`.  Since `Phi_K` is monic,

```text
R_q=product_{Phi_K(alpha)=0}P_q(alpha)
```

in a splitting `p`-adic ring. Every root counted by (8) contributes at least
one factor of `p`, hence

```text
s_q(p)<=v_p(R_q)=2v_p(M_q).                              (9)
```

This step is what saves one full factor of `K`: one resultant controls the
whole `K-1` member Galois-scaling orbit.

## 4. Exact global weighted-prime budget

Summing (8) over all non-forced scaling orbits reconstructs the excess:

```text
Delta_K(p)=sum_q s_q(p).                                 (10)
```

For a split prime `p`, `p!=K`, so the fixed factor `K^3` in (6) carries no
collision valuation.  Consequently

```text
sum_{p == 1 (mod K)} Delta_K(p) log p
 <= sum_q 2 log |M_q|
 =  sum_q log(|R_q|/K^3)
 <= N_K ((K-1)log 12-3log K).                           (11)
```

Thus:

> **Weighted prime-budget theorem.** For every odd prime `K`, with
>
> ```text
> C_K=(K-1)log 12-3log K,
> N_K=K^3-5K^2+6K+1,
> ```
>
> one has
>
> ```text
> sum_{p == 1 (mod K)} Delta_K(p) log p <= N_K C_K.      (12)
> ```
>
> The sum is over rational primes.

The right side is `O(K^4)`.  In particular only finitely many split primes have
nonzero excess.  The factor `-3 log K` is not cosmetic: it records that the
universal `K^3` factor in every resultant can never be responsible for a split
prime collision.

## 5. Tail and sparsity corollaries

For every real `P>=2`, (12) implies

```text
sum_{p == 1 (mod K), p>=P} Delta_K(p)
 <= N_K C_K/log P.                                      (13)
```

For every `L>0`,

```text
#{p == 1 (mod K), p>=P : Delta_K(p)>=L}
 <= N_K C_K/(L log P).                                  (14)
```

At the polynomial scale `P=K^A`,

```text
sum_{p>=K^A, p==1 mod K} Delta_K(p)=O(K^4/log K),        (15)
```

and primes carrying excess at least `K^(2+delta)` satisfy

```text
#{p>=K^A, p==1 mod K : Delta_K(p)>=K^(2+delta)}
 =O(K^(2-delta)/log K).                                 (16)
```

These are arithmetic average/sparsity statements, not a pointwise
`Delta_K(p)=O(K^2)` theorem.  No prime-number theorem in arithmetic progressions
is used. Turning (13)--(16) into a normalized average over a chosen interval
requires an independent lower bound for the number of split primes in that
interval.

## 6. Finite regression

`computations/verification/cayley_resultant_mass_budget.py` recomputes the
normalized resultants on the complete promoted exceptional sets

```text
K=11: p in {23,67,89},
K=13: p in {53,79,131,157,313}.
```

It checks exactly that common-root counts are bounded by resultant valuations
and that their orbit sums reproduce direct finite-field energy excess.  For
these finite designs, the stronger equality

```text
sum_q s_q(p)=sum_q v_p(R_q)=Delta_K(p)
```

happens to hold.  The theorem uses only the robust inequality (9), not that
finite equality.

The weighted theorem is also regressed without floating-point logarithms via
the equivalent integer inequality

```text
K^(3N_K) product_p p^(Delta_K(p)) <= 12^((K-1)N_K)
```

on the promoted exceptional primes.  This finite product omits primes with
zero observed excess; it is a regression anchor, not the proof of (12).

## Scope

The theorem is uniform in every odd prime `K` but averages over rational split
primes.  Its significance for the BGS programme is that the entire population
of large-energy exceptional reductions has a deterministic global `O(K^4)`
logarithmic budget.  A prime-averaged moment theorem can combine this with an
independent distribution theorem for primes `p==1 mod K`; a pointwise BGS route
still needs the centered-energy improvement isolated in
[`cayley_centered_energy.md`](cayley_centered_energy.md).
