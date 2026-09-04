# Higher product-row intersections and cyclotomic subresultants

**Status: EXACT for the subresultant obstruction and its quadratic-energy corollary away from an explicit finite exceptional integer; FINITE-REGRESSION for small prime orders; OPEN for a growing-`K` bound on the eligible split prime divisors.**

This note refines `cayley_product_row_intersections.md`.  The exact row identity
shows that a uniform bound on pairwise product-row intersections would close the
remaining pointwise Cayley-energy gap.  Here we isolate intersections of
multiplicity at least four by the first three subresultants of two explicit
cyclotomic row polynomials.

The main consequence is:

> for each fixed odd prime `K`, every split prime outside an explicit finite set
> already satisfies a pointwise `O(K^2)` Cayley excess bound.

The unresolved issue is no longer the existence of occasional non-forced
collisions.  It is the arithmetic size and split-prime support of the much
smaller **higher-intersection subresultant integers** defined below.

## 1. Projective row polynomial

Let `K` be an odd prime, let

```text
zeta=exp(2 pi i/K),
L=Q(zeta),
O_L=Z[zeta],
m=(K-1)/2.
```

A noncentral product row is indexed by a nonzero exponent `i mod K`, with

```text
w=zeta^i,
xy=w^2.
```

Write

```text
x=w zeta^a,
y=w zeta^(-a).
```

The trace class `a~-a` determines the unordered pair.  The invalid pair with
`x=1` or `y=1` is exactly the trace class `a=+-i`, so let

```text
A_i=(F_K/{+-1}) \ {+-i}.                                 (1)
```

It has `m` elements.  For `a in A_i`, set

```text
N_i=1-zeta^(2i),
D_(i,a)=zeta^i(zeta^a+zeta^(-a))-2.                      (2)
```

The shifted Cayley parameter `mu=t/(2-t)` satisfies

```text
mu=N_i/D_(i,a).                                          (3)
```

If `D_(i,a)=0`, equation (3) is the projective value `mu=infinity`,
corresponding to `t=2`.

Define the homogeneous degree-`m` row form

```text
R_i(U,V)=prod_{a in A_i}(D_(i,a) U-N_i V) in O_L[U,V].   (4)
```

Its projective roots are exactly the valid nonzero Cayley parameters supported
by row `i`, expressed in the `mu` coordinate.  The dehomogenization

```text
R_i(U)=R_i(U,1)                                           (5)
```

records all finite roots; a root at infinity appears as a drop of leading
degree after reduction.

Characteristic-zero Cayley rigidity implies that `R_i` and `R_j` have no
common projective root for `i!=j`.

## 2. Galois normalization of row pairs

For `c in F_K^*`, the automorphism

```text
sigma_c(zeta)=zeta^c
```

sends

```text
R_i -> R_(ci).                                            (6)
```

Thus every ordered distinct row pair `(i,j)` is Galois-equivalent to

```text
(1,r),  r=j/i in F_K^*\{1}.                              (7)
```

For unordered row pairs, `r` and `r^(-1)` describe the same Galois orbit.
There are `(K-1)/2` such ratio classes.

## 3. The order-three subresultant integer

Fix `r!=1`.  Let

```text
S_j^(r)(U)=Sres_j(R_1(U),R_r(U)),  j=0,1,2,              (8)
```

be the classical polynomial subresultants over `O_L`; `S_0` is the resultant.
Every coefficient of every `S_j^(r)` is an algebraic integer.

Let `C_(K,r)^(3)` be the finite set of all **nonzero** coefficients occurring
in `S_0^(r),S_1^(r),S_2^(r)`, and define

```text
G_(K,r)^(3)
 =gcd{ |N_(L/Q)(c)| : c in C_(K,r)^(3) } in Z_(>0).      (9)
```

The resultant is nonzero in characteristic zero, so the set contains a nonzero
norm and (9) is well-defined.

Since every split prime satisfies `p!=2,K`, define the eligible part

```text
G'_(K,r)^(3)
 =G_(K,r)^(3) with all factors 2 and K removed.           (10)
```

Finally, over one representative from each unordered ratio class, put

```text
G'_K^(3)=prod_[r] G'_(K,r)^(3).                           (11)
```

No bound on (11) is asserted yet.

## 4. Exact high-intersection obstruction

Let `p==1 mod K` be prime and choose a prime ideal `P` of `O_L` above `p`,
corresponding to a reduction `zeta -> h` with `h` of exact order `K` in
`F_p^*`.

For two product rows, let `I_(i,j)(p)` be the number of common **finite Cayley
parameters `t`** in the notation of `cayley_product_row_intersections.md`.
There can be at most one common projective parameter with `t=2`.

### Theorem 1 (subresultant obstruction)

If two distinct product rows satisfy

```text
I_(i,j)(p)>=4,                                            (12)
```

then, with `r=j/i mod K` (up to inversion),

```text
p | G'_(K,r)^(3).                                         (13)
```

### Proof

At most one of the common parameters in (12) is the projective value `t=2`.
Therefore the reductions of the dehomogenized row polynomials have at least
three distinct common finite roots.  Their gcd over `F_p[U]` has degree at
least three.

The standard subresultant criterion then forces every coefficient of

```text
S_0, S_1, S_2
```

to vanish modulo `P`.  Hence `P` divides every algebraic-integer coefficient
in `C_(K,r)^(3)`.  Taking absolute norms to `Q`, the rational prime `p`
divides every nonzero norm in (9), and therefore divides their gcd.

Applying the Galois automorphism `sigma_(i^(-1))` normalizes `(i,j)` to
`(1,r)` and merely permutes the prime ideals above the split rational prime
`p`.  Thus `p|G_(K,r)^(3)`.  Since `p!=2,K`, equation (13) follows.

Degree drops of a row polynomial after reduction do not invalidate the
argument: the subresultants are universal minors of the Sylvester matrices,
and three common finite roots force the relevant rank deficiency; leading
coefficient vanishing can only increase that deficiency.

## 5. Quadratic Cayley energy away from the higher-intersection integer

Let

```text
I_K(p)=max_{i!=j} I_(i,j)(p).                             (14)
```

The exact row-intersection theorem gives

```text
Delta_K(p)<=4 I_K(p)(K-1)(K-2).                          (15)
```

### Corollary 2

If

```text
p does not divide G'_K^(3),                              (16)
```

then

```text
I_K(p)<=3,                                                (17)
Delta_K(p)<=12(K-1)(K-2),                                (18)
```

and therefore

```text
E_+(c(H\{1}))
 <=15(K-1)(K-2).                                         (19)
```

Thus the desired quadratic collision scale holds pointwise for every split
prime outside the explicit higher-intersection exceptional integer (11).

Equation (19) is stronger than the maintained `K^(8/3)` theorem on this
subfamily.  It is still not a theorem for **all** split primes because no
sufficient growing-`K` control on the prime divisors of `G'_K^(3)` has yet been
proved.

## 6. Exact finite evidence

`computations/verification/cayley_product_row_subresultants.py` independently
constructs the row polynomials and subresultants.  The default finite anchors
include

```text
K=7,  r=2:   G'_(K,r)^(3)=1,
K=11, r=2:   G'_(K,r)^(3)=1,
K=13, r=3:   G'_(K,r)^(3)=3^3,
K=13, r=12:  G'_(K,r)^(3)=5^8,
K=17, r=10:  G'_(K,r)^(3)=103^2.                         (20)
```

The last prime is split (`103==1 mod 17`) and the finite design `(K,p)=(17,103)`
has a row pair of ratio class `r=10` with three common parameters.

A slower extended computation gives

```text
K=23, r=18:
G'_(K,r)^(3)=47^20 * 139^2,                              (21)
```

and both split primes are realized geometrically:

```text
p=47:   a row pair has 5 common parameters,
p=139:  a row pair has 3 common parameters.              (22)
```

These finite calculations are not a proof of any asymptotic bound on (11).
Their value is mechanistic: the higher-subresultant integer detects exactly the
kind of repeated row intersections that the quadratic-energy argument must
exclude.

## 7. The remaining arithmetic lemma

The new pointwise closure problem is:

> **Higher-row divisor problem.**  Control the split prime divisors of
> `G'_K^(3)` uniformly in odd prime `K`.  In particular, prove a bound strong
> enough that in the regime `K=o(p^(1/4))`, a split prime `p` cannot divide
> `G'_K^(3)`; or prove directly that `I_K(p)=K^(o(1))` on the exceptional
> support.

A polynomial bound

```text
P_split^+(G'_K^(3)) <= K^(4+o(1))                        (23)
```

would, together with Corollary 2, close the pointwise Cayley-energy problem in
the intended fourth-moment regime.  This bound is **OPEN**.

The structure behind (23) is unusually rigid: differences of cyclotomic trace
values factor as

```text
(zeta^a+zeta^(-a))-(zeta^b+zeta^(-b))
 =(zeta^a-zeta^b)(1-zeta^(-a-b)),                        (24)
```

so slopes determined by two row intersections are cyclotomic units.  Three or
more intersections force simultaneous congruences among several such units.
The next proof attempt should exploit the ideal gcd of these cyclotomic-unit
differences rather than their individual archimedean norms.

No Gaussian limit, local eigenvalue statistic, or microscopic BGS/GOE theorem
is claimed here.