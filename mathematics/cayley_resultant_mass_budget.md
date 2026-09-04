# Global resultant budget for non-forced Cayley collision mass

**Status: EXACT for odd prime subgroup order `K`; FINITE-REGRESSION for the maintained `K=11,13` exceptional sets.**

This note extracts an averaged statement that is stronger than treating each
collision resultant independently.  The key point is to quotient collision
quadruples by the Galois scaling action on their exponents and then use the
`p`-adic valuation of one resultant to count how many members of the whole
orbit collide after reduction modulo a split prime.

The result does **not** replace the pointwise direct energy theorem in
[`cayley_direct_energy.md`](cayley_direct_energy.md), but it gives a global
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

be the nonzero difference energy.  Identity and central inversion force the
baseline

```text
B_K=(K-1)(2K-5).
```

Define the non-forced excess

```text
Delta_K(p)=E_K(p)-B_K >= 0.                              (1)
```

Because `B_K` is exactly the size of the union of the identity and
inversion-swap collision relations, `Delta_K(p)` is literally the number of
ordered collision quadruples not belonging to those forced relations.

## 2. Galois scaling orbits

Index the elements of `A` by nonzero residues modulo `K`.  An admissible
collision quadruple is

```text
q=(i,j,r,s),
i,j,r,s in F_K^*,
i!=j,
r!=s.
```

The group `F_K^*` acts freely by simultaneous scaling

```text
a*q=(a i,a j,a r,a s).                                  (2)
```

The action is free because `i!=0`; hence every orbit has size `K-1` and has a
unique representative with `i=1`.

There are

```text
M=(K-1)(K-2)
```

ordered nonzero difference pairs.  The total number of admissible collision
quadruples is `M^2`.  The forced union has size `B_K`, so the number of
**non-forced scaling orbits** is

```text
N_K=(M^2-B_K)/(K-1)
   =(K-1)(K-2)^2-(2K-5)
   =K^3-5K^2+6K+1.                                      (3)
```

For `K=11,13`, this gives exactly `793` and `1431`, the normalized counts in
the maintained fixed-`K` resultant audit.

## 3. One resultant controls a whole orbit

For a normalized non-forced representative `q=(i,j,r,s)`, let `P_q(X)` be the
cleared Cayley collision polynomial from
[`cayley_additive_energy.md`](cayley_additive_energy.md):

```text
P_q(X)
 = X^(r+s+i)-X^(r+s+j)-X^(r+i+j)+2X^(r+j)-X^r
   +X^(s+i+j)-2X^(s+i)+X^s+X^i-X^j,
```

with exponents reduced modulo `K` after collecting terms.  Put

```text
R_q=Res(Phi_K,P_q).                                      (4)
```

Prime-order characteristic-zero rigidity implies `R_q!=0` for every
non-forced orbit, and the coefficient bound gives

```text
|R_q| <= 12^(K-1).                                      (5)
```

Fix a split prime `p==1 (mod K)` and a generator `h` of `H`.  The roots of
`Phi_K` in `F_p` are exactly

```text
h^a,  a in F_K^*.
```

For a given `a`,

```text
P_q(h^a)=0                                               (6)
```

is exactly the Cayley collision attached to the scaled quadruple `a*q`.
Therefore the number of colliding members of the orbit of `q` is

```text
s_q(p)=#{a in F_K^*: P_q(h^a)=0}.                        (7)
```

Since `p!=K`, the cyclotomic polynomial `Phi_K` is separable modulo `p` and
splits completely.  Hensel lifting its `K-1` simple roots to `Z_p` and using
that `Phi_K` is monic gives

```text
R_q=product_{Phi_K(alpha)=0} P_q(alpha)
```

inside a splitting `p`-adic ring.  Every root counted by (7) contributes at
least one factor of `p`, hence

```text
s_q(p) <= v_p(R_q).                                      (8)
```

This is the step that saves one full factor of `K` compared with summing a
separate norm bound for every unnormalized collision quadruple.

## 4. Exact global weighted-prime budget

Summing (7) over all non-forced scaling orbits reconstructs the excess energy:

```text
Delta_K(p)=sum_q s_q(p).                                 (9)
```

Using (8), unique factorization of the integer `R_q`, and then (5),

```text
sum_{p == 1 (mod K)} Delta_K(p) log p
 <= sum_q sum_p v_p(R_q) log p
 <= sum_q log |R_q|
 <= N_K (K-1) log 12.                                   (10)
```

Thus:

> **Weighted prime-budget theorem.** For every odd prime `K`,
>
> ```text
> sum_{p == 1 (mod K)} Delta_K(p) log p
> <= (K^3-5K^2+6K+1)(K-1) log 12.                       (11)
> ```
>
> The sum is over rational primes.  In particular only finitely many split
> primes have nonzero excess.

The finiteness is already implicit in the resultant construction; (11) gives a
quantitative global collision-mass budget of order `K^4`.

## 5. Tail and sparsity corollaries

For every real `P>=2`, (11) immediately implies

```text
sum_{p == 1 (mod K), p>=P} Delta_K(p)
 <= N_K (K-1) log 12 / log P.                            (12)
```

More generally, for every `L>0`,

```text
#{p == 1 (mod K), p>=P : Delta_K(p)>=L}
 <= N_K (K-1) log 12 / (L log P).                        (13)
```

For example, at the polynomial scale `P=K^A`,

```text
sum_{p>=K^A, p==1 mod K} Delta_K(p)
 = O(K^4/log K),                                         (14)
```

with an explicit constant `log(12)/A` up to the exact polynomial factor in
(11).  Likewise primes carrying excess at least `K^(2+delta)` are globally
sparse:

```text
#{p>=K^A, p==1 mod K : Delta_K(p)>=K^(2+delta)}
 = O(K^(2-delta)/log K).                                 (15)
```

These are arithmetic average/sparsity statements, not a pointwise
`Delta_K(p)=O(K^2)` theorem.  No prime-number theorem in arithmetic progressions
is used in (11)--(15); converting them into an average over a chosen interval
requires an independent lower bound for the number of split primes in that
interval.

## 6. Finite regression

`computations/verification/cayley_resultant_mass_budget.py` recomputes the
normalized resultants and checks the orbit/root/valuation mechanism on the
complete promoted exceptional sets

```text
K=11: p in {23,67,89},
K=13: p in {53,79,131,157,313}.
```

For these finite designs, the stronger equality

```text
sum_q s_q(p)=sum_q v_p(R_q)=Delta_K(p)
```

happens to hold.  The proof above uses only the robust inequality
`s_q(p)<=v_p(R_q)` and does not extrapolate equality.

## Scope

The theorem is uniform in every odd prime `K` but is an average over rational
split primes, not a pointwise replacement for the `K^(8/3)` direct theorem.
Its significance for the BGS programme is that the entire population of
large-energy exceptional reductions has a deterministic global `O(K^4)`
logarithmic budget.  A future prime-averaged moment theorem can combine this
budget with distribution results for primes `p==1 mod K`; a pointwise BGS route
still needs the centered-energy improvement isolated in
[`cayley_centered_energy.md`](cayley_centered_energy.md).
