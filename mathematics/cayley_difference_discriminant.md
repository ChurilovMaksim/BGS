# The Cayley difference discriminant: one canonical obstruction for all split-prime collisions

**Status: EXACT for odd prime `K`, conditional only on the maintained characteristic-zero collision classification.  FINITE-REGRESSION for `K=5,7,11,13`.**

This note replaces the family of individual collision resultants by one canonical
univariate polynomial.  It gives an exact criterion for exceptional split primes
and a valuation bound for the entire non-forced Cayley collision excess.

It does **not** by itself prove the desired pointwise `K^(2+o(1))` energy bound.
Its main value is structural: all exceptional reduction geometry is compressed
into one discriminant, opening a new route to averaged prime budgets through the
prime-to-`2K` part of that discriminant.

## 1. The Cayley root polynomial

Let `K` be an odd prime and define

```text
Q_K(X)=((X+1)^K-(X-1)^K)/2 in Z[X].                     (1)
```

Its degree is `K-1` and its leading coefficient is `K`.  If `zeta` is a
primitive `K`-th root of unity and

```text
c(z)=(z+1)/(z-1),
```

then

```text
Q_K(c(zeta^a))=0,       a=1,...,K-1.                    (2)
```

Indeed `(c(z)+1)/(c(z)-1)=z`.  Thus the roots of `Q_K` are exactly the
characteristic-zero Cayley set

```text
A_K^C={c(zeta^a):a in F_K^*}.                           (3)
```

They are simple.

## 2. The polynomial of pairwise differences

Put

```text
R_K(T)=Res_X(Q_K(X),Q_K(X-T)) in Z[T].                  (4)
```

By the root-product formula for the resultant, the multiplicity of a complex
number `d` as a root of `R_K` is exactly the number of ordered pairs
`(a,b)` with

```text
c(zeta^a)-c(zeta^b)=d.                                  (5)
```

The zero difference has multiplicity `K-1`.  Let

```text
S_K(T)=primitive squarefree part over Q[T]
       of R_K(T)/T^(K-1).                               (6)
```

The roots of `S_K` are therefore the distinct nonzero characteristic-zero
Cayley differences.

The maintained prime-order rigidity theorem says that the only equal-difference
relations in characteristic zero are identity and inversion-swap:

```text
(a,b) ~ (-b,-a).                                        (7)
```

The involution in (7) has `K-1` fixed ordered pairs, namely `b=-a`; every other
orbit has size two.  Consequently

```text
deg S_K
 =(K-1)+[(K-1)(K-2)-(K-1)]/2
 =(K-1)^2/2.                                             (8)
```

For a root `alpha` of `S_K`, let `w(alpha)` be the number of ordered pairs in
(5) producing it.  Then exactly

```text
w(alpha) in {1,2};                                      (9)
```

weight one occurs for the central differences
`c(zeta^a)-c(zeta^(-a))=2c(zeta^a)`, and weight two otherwise.

The coefficients of the monic root polynomial lie in `Z[1/K]`: every
`c(zeta^a)` is integral away from the unique cyclotomic prime above `K` because
`1-zeta^a` is a unit away from `K`.  Hence the primitive integral polynomial
`S_K` has leading coefficient supported only at `K`.  In particular, for every
rational prime `p==1 (mod K)`, its leading coefficient is a `p`-adic unit.

## 3. Reduction at a split prime

Let

```text
p == 1 (mod K)                                           (10)
```

be prime.  Then `p!=K`, and `mu_K subset Q_p`.  Choose a Teichmuller primitive
`K`-th root `zeta_p in Z_p^*`, reducing to a generator `h` of the unique
subgroup `H<=F_p^*` of order `K`.

Every characteristic-zero difference root

```text
alpha=c(zeta_p^a)-c(zeta_p^b)                            (11)
```

is `p`-adically integral, and its reduction is exactly

```text
c(h^a)-c(h^b) in F_p.                                   (12)
```

Thus finite-field non-forced collisions are precisely mergers, modulo `p`, of
**distinct roots of `S_K`**.

Let the roots of `S_K` be partitioned into reduction clusters `C_d`, one for
each nonzero finite-field difference `d`.  Then

```text
r_{A-A}(d)=sum_{alpha in C_d} w(alpha).                  (13)
```

The characteristic-zero forced baseline is

```text
sum_alpha w(alpha)^2
 =(K-1)(2K-5)=:B_K.                                     (14)
```

Therefore the finite-field excess

```text
Delta_K(p)
 :=sum_{d!=0} r_{A-A}(d)^2-B_K                           (15)
```

has the exact cluster expansion

```text
Delta_K(p)
 =2 sum_d sum_{alpha<beta in C_d} w(alpha)w(beta).       (16)
```

This identity is useful independently of any discriminant estimate.

## 4. Discriminant criterion and valuation theorem

Write

```text
Disc_K=Disc(S_K) in Z\{0}.                               (17)
```

### Theorem 1 (single-discriminant classification)
For every odd prime `K` and every prime `p==1 (mod K)`, one has

```text
Delta_K(p)>0    iff    p divides Disc_K.                 (18)
```

Moreover,

```text
Delta_K(p) <= 4 v_p(Disc_K).                             (19)
```

### Proof
Because the leading coefficient of `S_K` is a `p`-adic unit and all of its
roots lie in `Q_p`, the root formula for the discriminant gives

```text
v_p(Disc_K)
 =2 sum_{alpha<beta} v_p(alpha-beta).                    (20)
```

Let `N_p` be the number of unordered pairs of distinct roots of `S_K` that
have the same reduction modulo `p`.  Each such pair has
`v_p(alpha-beta)>=1`; hence

```text
v_p(Disc_K)>=2N_p.                                       (21)
```

Conversely `v_p(Disc_K)>0` means that at least one pair coalesces modulo `p`,
so (18) follows from the cluster description.

For (19), expand (16).  By (9), every product of weights satisfies

```text
w(alpha)w(beta)<=4.
```

Therefore

```text
Delta_K(p)
 <= 8 N_p
 <= 4 v_p(Disc_K),                                      (22)
```

as required.

No resultant-size estimate is used in this proof.

## 5. Weighted split-prime budget from one integer

Theorem 1 immediately implies the exact global inequality

```text
sum_{p==1 mod K} Delta_K(p) log p
 <= 4 sum_{p==1 mod K} v_p(Disc_K) log p
 <= 4 log |Disc_K|_(split),                              (23)
```

where

```text
|Disc_K|_(split)
 := product_{p==1 mod K} p^(v_p(Disc_K)).                (24)
```

Thus the optimal average-prime problem is no longer to bound `O(K^3)`
individual collision resultants separately.  It is to understand the split
part of **one canonical discriminant**.

The completely unconditional estimate obtained by replacing the split part by
`|Disc_K|` need not improve the existing `O(K^4)`-scale budget.  The gain can
only come from exploiting the very special arithmetic factorization of
`Disc_K`.

## 6. Exact small-K factorization

The difference resultant has strikingly structured factorizations.  For
example,

```text
K=5:
R_5(T)
 =5^5 T^4
  (5T^4+20T^2+16)^2
  (5T^4+40T^2+16),                                      (25)
```

and

```text
K=7:
R_7(T)
 =7^7 T^6
  (7T^6+56T^4+112T^2+64)^2
  (7T^6+84T^4+224T^2+64)^2
  (7T^6+140T^4+336T^2+64).                              (26)
```

The last factor in each case is the central-difference factor, proportional to
`Q_K(T/2)`.  The squared factors encode the noncentral forced two-element
classes.

For the squarefree nonzero difference polynomial, exact computation gives:

```text
K=7:
Disc(S_7)=2^348 7^63 13^12,
```

so there is no split exceptional prime (`13==-1 mod 7`).

For the maintained promoted cases,

```text
K=11: split prime divisors of Disc(S_11) = {23,67,89},
K=13: split prime divisors of Disc(S_13) = {53,79,131,157,313}.  (27)
```

These are exactly the complete exceptional sets previously obtained by
individual collision resultants.

The corresponding discriminant exponents are

```text
K=11:
v_23=76, v_67=12, v_89=12;

K=13:
v_53=60, v_79=56, v_131=12, v_157=12, v_313=16.        (28)
```

Direct finite-field energies satisfy (19) in every case; for example

```text
K=11:
Delta(23)=240 <= 4*76,
Delta(67)=48  =  4*12,
Delta(89)=32  <= 4*12.                                  (29)
```

## 7. A new asymptotic target

Exact computations through `K=23` reveal that the enormous `K^4`-scale part
of the full discriminant is dominated by powers of `2` (and, to a smaller
extent, `K`), neither of which can be a split collision prime.  If

```text
Disc_K^(2K)
```

denotes the integer obtained from `Disc_K` by removing all prime factors
`2` and `K`, the observed logarithmic sizes are consistent with

```text
log |Disc_K^(2K)| = O(K^3 log K).                        (30)
```

For example, at `K=23` the exact squarefree difference polynomial has degree
`242`; after removing the full `2`- and `23`-adic parts from its discriminant,

```text
log |Disc_23^(46)| / 23^3 = 1.9246059627... .            (31)
```

Equation (30) is **CONJECTURAL at present**.  It is now a high-value closure
target because, together with (23), it would improve the global weighted
split-prime collision budget from `O(K^4)` to `O(K^3 log K)`.  In the dyadic
double-average framework this would move the exact-baseline density threshold
from `theta<1/5` to `theta<1/4` (up to logarithms) and the normalized quadratic
excess theorem toward the Bombieri--Vinogradov modulus barrier `theta<1/2`.

The required next step is therefore structural: derive the prime-to-`2K`
discriminant via the trace/Chebyshev factorization of the Cayley differences,
rather than bound the full discriminant by generic polynomial height.

## Evidence boundary

- Theorem 1 is a symbolic consequence of the characteristic-zero collision
  classification and the standard root formula for discriminants.
- The exact factorizations and valuation regressions are finite computations;
  they are not used to prove Theorem 1.
- The `O(K^3 log K)` prime-to-`2K` discriminant bound is a research target, not
  an established theorem.
- No statement here proves microscopic BGS/GOE universality.
