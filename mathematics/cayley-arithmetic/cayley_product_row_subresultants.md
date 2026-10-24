# Higher product-row intersections and cyclotomic subresultants

**Status: EXACT for the row-polynomial construction and reduction; EXACT + EXTERNAL-THEOREM for the standard subresultant criterion; FINITE-REGRESSION for small prime orders; OPEN for a growing-`K` bound on the eligible split prime divisors.**

This note refines `cayley_product_row_intersections.md`.  The exact row identity
shows that a uniform bound on pairwise product-row intersections would close the
remaining pointwise Cayley-energy gap.  Here intersections of multiplicity at
least **three** are isolated by the first three subresultants of two explicit
cyclotomic row forms.

The main consequence is:

> for each fixed odd prime `K`, every split prime outside an explicit finite set
> already satisfies a pointwise `O(K^2)` Cayley-energy bound, with the explicit
> estimate `E_+(A)<=11(K-1)(K-2)`.

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

There are `m+1` trace classes before the deletion and hence `|A_i|=m`.  For
`a in A_i`, set

```text
N_i=1-zeta^(2i),
D_(i,a)=zeta^i(zeta^a+zeta^(-a))-2.                      (2)
```

The shifted Cayley parameter

```text
mu=t/(2-t)
```

satisfies

```text
mu=N_i/D_(i,a).                                          (3)
```

If `D_(i,a)=0`, equation (3) is the projective value `mu=infinity`, which is
exactly the finite Cayley parameter `t=2`.

Define the homogeneous degree-`m` row form

```text
R_i(U,V)=prod_{a in A_i}(D_(i,a) U-N_i V) in O_L[U,V].   (4)
```

The Mobius map `t -> mu=t/(2-t)` identifies the finite nonzero Cayley
parameters of row `i` bijectively with the projective roots of `R_i`.  In
particular `t=2` is not exceptional for the projective row form: it is simply
`[U:V]=[1:0]`.

Characteristic-zero Cayley rigidity implies that `R_i` and `R_j` have no
common projective root for `i!=j`.

## 2. Galois normalization of row pairs

For `c in F_K^*`, the automorphism

```text
sigma_c(zeta)=zeta^c
```

sends

```text
R_i -> R_(ci).                                            (5)
```

Thus every ordered distinct row pair `(i,j)` is Galois-equivalent to

```text
(1,r),  r=j/i in F_K^*\{1}.                              (6)
```

For unordered row pairs, `r` and `r^(-1)` describe the same Galois orbit.
There are `(K-1)/2` such ratio classes.

## 3. The order-three subresultant integer

For this construction assume `K>=7`, so `m>=3` and indices `0,1,2`
are below the row degree. The projective row construction above still
applies at `K=3,5`.

Fix `r!=1`.  Dehomogenize at `V=1` in characteristic zero and let

```text
S_j^(r)(U)=Sres_j(R_1(U,1),R_r(U,1)),  j=0,1,2,          (7)
```

be the fixed-degree classical polynomial subresultants; `S_0` is the
resultant.  Equivalently, their coefficients are the standard determinantal
minors of the two degree-`m` homogeneous coefficient arrays.  Every coefficient
is an algebraic integer.

Let `C_(K,r)^(3)` be the finite set of all **nonzero** coefficients occurring
in `S_0^(r),S_1^(r),S_2^(r)`, and define

```text
G_(K,r)^(3)
 =gcd{ |N_(L/Q)(c)| : c in C_(K,r)^(3) } in Z_(>0).      (8)
```

The characteristic-zero resultant is nonzero, so (8) is well-defined.
Since every split prime satisfies `p!=2,K`, define

```text
G'_(K,r)^(3)
 =G_(K,r)^(3) with all factors 2 and K removed.           (9)
```

Finally, over one representative from each unordered ratio class, put

```text
G'_K^(3)=prod_[r] G'_(K,r)^(3).                           (10)
```

For `K=3,5`, define `G'_(K,r)^(3)=G'_K^(3)=1` directly as a
small-degree support convention: each row has `m<=2` parameters, so
three common parameters are impossible. No full low-subresultant ideal
or unstripped integer is assigned by this convention.

No growing-`K` bound on (10) is asserted.

## 4. Exact high-intersection obstruction

Let `p==1 mod K` be prime and choose a prime ideal `P` of `O_L` above `p`,
corresponding to a reduction

```text
zeta -> h in F_p^*,   ord(h)=K.
```

Let `I_(i,j)(p)` be the number of common finite Cayley parameters `t` of two
distinct product rows.  By the projective parametrization in Section 1, these
are exactly the common projective roots of the reduced homogeneous row forms.

### Theorem 1 (order-three subresultant obstruction)

If

```text
I_(i,j)(p)>=3,                                            (11)
```

then, with `r=j/i mod K` up to inversion,

```text
p | G'_(K,r)^(3).                                         (12)
```

### Proof

Reduce the two degree-`m` homogeneous row forms modulo `P`.  Condition (11)
gives at least three distinct common projective roots, so their homogeneous gcd
has degree at least three.

For two fixed-degree binary forms over a field, the subresultant theorem says
that a gcd of degree `d` forces

```text
S_0=S_1=...=S_(d-1)=0.                                   (13)
```

The determinantal proof is also useful here.  If the two degree-`m` forms are
`HF` and `HG`, with `deg H=d`, the Sylvester multiplication map has a kernel
of dimension at least `d`; the minors defining every coefficient of the
subresultants of index `<d` therefore vanish.  This formulation automatically
includes a common root at infinity, so no degree-preservation assumption on a
dehomogenized specialization is needed.

Applying (13) with `d>=3` shows that every coefficient of the specialized
`S_0,S_1,S_2` vanishes modulo `P`.  Hence `P` divides every algebraic-integer
coefficient in `C_(K,r)^(3)`.  Taking absolute norms to `Q`, the rational prime
`p` divides every nonzero norm in (8), and therefore their gcd.

Finally `sigma_(i^(-1))` normalizes `(i,j)` to `(1,r)` and merely permutes the
prime ideals above the completely split rational prime `p`.  Thus
`p|G_(K,r)^(3)`.  Since `p!=2,K`, equation (12) follows.

The standard subresultant implication (13) is the fundamental theorem of
W. S. Brown and J. F. Traub, *On Euclid's Algorithm and the Theory of
Subresultants*, Journal of the ACM 18 (1971), 505--514,
DOI `10.1145/321662.321665`.  The bibliographic record and DOI were independently
verified in the current audit.

## 5. Quadratic Cayley energy away from the higher-intersection integer

Let

```text
I_K(p)=max_{i!=j} I_(i,j)(p).                             (14)
```

The exact row-intersection theorem gives

```text
Delta_K(p)<=4 I_K(p)(K-1)(K-2).                          (15)
```

### Corollary 2 (explicit pointwise quadratic subfamily)

If

```text
p does not divide G'_K^(3),                              (16)
```

then Theorem 1 excludes three common parameters for every row pair, so

```text
I_K(p)<=2,                                                (17)
Delta_K(p)<=8(K-1)(K-2),                                 (18)
```

and, using the exact forced total energy
`3(K-1)(K-2)`,

```text
E_+(c(H\{1}))
 <=11(K-1)(K-2).                                         (19)
```

Thus the desired quadratic collision scale already holds pointwise for every
split prime outside the explicit higher-intersection exceptional integer (10).
Equation (19) is stronger than the maintained `K^(8/3)` theorem on this
subfamily.

This is still not a theorem for **all** split primes: no sufficient growing-`K`
control on the prime divisors of `G'_K^(3)` is known.

## 6. Exact finite evidence

`computations/verification/cayley_product_row_subresultants.py` independently
constructs the row polynomials and their first three subresultants.  The default
exact anchors are

```text
K=7,  r=2:   G'_(K,r)^(3)=1,
K=11, r=2:   G'_(K,r)^(3)=1,
K=13, r=3:   G'_(K,r)^(3)=3^3,
K=13, r=12:  G'_(K,r)^(3)=5^8,
K=17, r=10:  G'_(K,r)^(3)=103^2.                         (20)
```

The last prime is split (`103==1 mod 17`), and the finite design
`(K,p)=(17,103)` has a row pair of ratio class `r=10` with exactly three common
parameters, as Theorem 1 predicts must be supported by (20).

A slower independently rerun extended computation gives

```text
K=23, r=18:
G'_(K,r)^(3)=47^20 * 139^2.                              (21)
```

Both rational primes are split, and finite row geometry realizes

```text
p=47:   a row pair has 5 common parameters,
p=139:  a row pair has 3 common parameters.              (22)
```

These calculations are finite regressions, not a proof of any asymptotic bound
on (10).  Their value is mechanistic: the order-three subresultant integer
detects precisely the repeated row intersections that the quadratic-energy
argument must control.

## 7. The remaining arithmetic lemma

The pointwise closure problem has now narrowed to:

> **Higher-row divisor problem.**  Control the split prime divisors of
> `G'_K^(3)` uniformly in odd prime `K`.  In particular, prove a bound strong
> enough that in the regime `K=o(p^(1/4))`, a split prime `p` cannot divide
> `G'_K^(3)`; or prove directly that `I_K(p)=K^(o(1))` on this exceptional
> support.

A bound

```text
P_split^+(G'_K^(3)) <= K^(4+o(1))                        (23)
```

would, together with Corollary 2, close the pointwise Cayley-energy problem
for each fixed `0<epsilon<1/4` when `K<=p^(1/4-epsilon)`. The full intended
regime `K=o(p^(1/4))` would follow from the stronger bound
`P_split^+(G'_K^(3))=O(K^4)`; an unspecified subpower loss in (23) does not
establish that conclusion. Both proposed bounds are **OPEN**.

The structure behind (23) is unusually rigid.  Differences of cyclotomic trace
values factor as

```text
(zeta^a+zeta^(-a))-(zeta^b+zeta^(-b))
 =(zeta^a-zeta^b)(1-zeta^(-a-b)),                        (24)
```

so slopes determined by two row intersections are cyclotomic units.  Three
intersections force simultaneous congruences among several such units.  The
next proof attempt should exploit ideal gcds of these cyclotomic-unit
differences rather than their individual archimedean norms.

No Gaussian limit, local eigenvalue statistic, or microscopic BGS/GOE theorem
is claimed here.
