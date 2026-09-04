# Off/off elliptic correlation after the reducible-fiber spike

**Status: EXACT, using standard Igusa geometric-monodromy and Deligne/Fouvry--Kowalski--Michel trace-function quasi-orthogonality.  FINITE-REGRESSION for the symbolic discriminant, spike factorization, and promoted designs.**

This note repairs and closes the geometric part of the historical off/off
elliptic draft.  The old draft missed one load-bearing feature: every generic
parameter class has a reducible fiber with about `2p` points.  Those spikes do
not disappear under trace-sheaf quasi-orthogonality; their multiplicities are
controlled by the same Cayley additive energy that appears in the mixed
`k=2` layer.

After extracting that spike explicitly, the remaining generic elliptic traces
are uniformly quasi-orthogonal.  Consequently the off/off variance is bounded
by

```text
p E_+(c(H\{1})) + K^2 p + K^4 sqrt(p) + K^4.            (1)
```

Thus the elliptic/sheaf layer is no longer an independent pointwise barrier:
the only superquadratic arithmetic term in the intended `K=o(p^(1/4))` regime
is the already isolated Cayley-energy problem.

Throughout, `p>3` is prime, `H<=F_p^*` has **odd** order `K`, and

```text
A=c(H\{1}),
c(x)=(x+1)/(x-1).                                       (2)
```

The off/off class notation agrees with `fourth_moment_reduction.md`.

## 1. Off/off parameter classes

For an off-diagonal pair key `(u,v)`,

```text
d(u,v)=(u-1)(v-1)/(v-u).                                (3)
```

For a coupling parameter

```text
lambda=(h1,h2) in H^2,                                  (4)
```

let `O_lambda(t)` be the number of valid off-diagonal `(u,v)` such that the
second key `(h1/u,h2/v)` is also off-diagonal and

```text
d(u,v)+d(h1/u,h2/v)=t.                                  (5)
```

Then

```text
O(t)=sum_{lambda in H^2} O_lambda(t).                    (6)
```

If `h1,h2!=1`, put

```text
alpha=c(h1),
beta =c(h2),
s=alpha+beta,
d=alpha-beta.                                            (7)
```

In Cayley coordinates

```text
a=c(u), b=c(v),
T_alpha(a)=(alpha a-1)/(a-alpha),                        (8)
```

and (5) becomes

```text
2/(a-b)+2/(T_alpha(a)-T_beta(b))=t.                      (9)
```

The **generic parameter set** is

```text
Lambda_g={
 (h1,h2) in H^2:
 h1!=1, h2!=1, h1!=h2, h1 h2!=1
}.                                                       (10)
```

Because `K` is odd, the four excluded one-dimensional strata meet only at
`(1,1)`. Hence

```text
|H^2\Lambda_g|=4K-3,
|Lambda_g|=(K-1)(K-3).                                  (11)
```

On `Lambda_g`,

```text
s d !=0,
alpha,beta notin {+-1}.                                 (12)
```

## 2. The branch quartic and its five finite bad fibers

Clear denominators in (9) and view the resulting plane cubic as a quadratic
in `b`.  Its discriminant in `b` is a binary-quartic model of the associated
genus-one curve.  Direct algebra gives, up to an everywhere nonzero scalar,

```text
Disc_a(q)
 =d^2 (d t-2)^4
  (s-d-2)^2(s-d+2)^2(s+d-2)^2(s+d+2)^2
  R_(s,d)(t),                                            (13)
```

where

```text
R_(s,d)(t)
 =d^2 t^4
  +2d(s^2-d^2-4)t^3
  +4(5d^2-s^2+4)t^2
  -64dt+64.                                              (14)
```

The residual quartic has

```text
Disc_t R_(s,d)
 =-2^19 s^2
  (s-d-2)(s-d+2)(s+d-2)(s+d+2).                         (15)
```

All factors on the right are nonzero on `Lambda_g`, so `R_(s,d)` has four
simple roots.  Moreover

```text
R_(s,d)(2/d)=16/d^2 !=0.                                (16)
```

Thus the generic family has exactly five distinct finite singular fibers:

```text
t0=2/d,
and the four roots of R_(s,d).                          (17)
```

Let `I(t)` be the classical binary-quartic invariant.  At the distinguished
fiber,

```text
I(2/d)=256.                                              (18)
```

Hence the Jacobian has multiplicative type `I_4` at `t0`: its minimal
discriminant has order four and `c4` is a unit.  At a simple root of `R`, the
discriminant has order one; therefore `I` cannot vanish there (otherwise both
binary-quartic invariants would vanish and the discriminant would have order at
least two).  Those four fibers have multiplicative type `I_1`.

In particular all five points have nontrivial tame local monodromy in the
rank-two `R^1` Tate sheaf.

Equation (18) also shows that the elliptic `j`-function has a genuine pole at
`t0`; the generic Jacobian over `F_p(t)` is therefore non-isotrivial.

## 3. The missing reducible spike

The fiber at `t0=2/d` is not merely singular.  The cleared cubic factors into
two distinct affine lines.  Up to a nonzero scalar they are

```text
L_-(a,b)
 =(beta-1)(a-1)-(alpha-1)(b-1),

L_+(a,b)
 =(beta+1)(a+1)-(alpha+1)(b+1).                          (19)
```

Their unique intersection is

```text
(a,b)=(alpha,beta).                                      (20)
```

The valid off/off domain excludes

```text
a,b in {+-1},
a=b,
a=alpha,
b=beta,
T_alpha(a)=T_beta(b).                                    (21)
```

On `L_-`, these exclusions collapse to exactly four points:

```text
(1,1),
its unique a=-1 point,
its unique b=-1 point,
(alpha,beta).                                            (22)
```

On `L_+`, they collapse to exactly

```text
(-1,-1),
its unique a=1 point,
its unique b=1 point,
(alpha,beta).                                            (23)
```

The only point shared by the two lists is `(alpha,beta)`.  Since two distinct
`F_p`-lines have `2p-1` affine points in their union, one gets the exact count

```text
O_lambda(t0)=2p-8                                       (24)
```

for every `lambda in Lambda_g`.

This is the correction missing from the historical off/off draft.

## 4. Uniform trace-function decomposition

Let `E_lambda/F_p(t)` be the Jacobian of the generic genus-one pencil and let
`F_lambda` be the rank-two middle-extension sheaf associated with its `R^1`.
Write

```text
a_lambda(t)
```

for the **unnormalized** Frobenius trace.  On a smooth fiber,

```text
|a_lambda(t)|<=2 sqrt(p).                                (25)
```

At the four `I_1` fibers the projective curve is irreducible nodal and has
`p+O(1)` points.  At the `I_4` fiber, subtracting the extra `p` from (24)
again leaves `p+O(1)`.  The affine/projective and valid-domain boundaries have
bounded degree.  Consequently there is an absolute constant `C` such that,
for every generic `lambda` and every `t in F_p`,

```text
O_lambda(t)
 =p+p 1_{t=t_lambda}-a_lambda(t)+e_lambda(t),            (26)

|e_lambda(t)|<=C,                                        (27)
```

where

```text
t_lambda=2/(alpha-beta).                                 (28)
```

At singular fibers, `a_lambda(t)` denotes the middle-extension trace; it is
bounded absolutely because the local monodromy is tame and semistable.

## 5. Geometric irreducibility and uniform conductor

For `p>3`, Igusa's open-image theorem for a non-isotrivial elliptic curve over
a global function field implies that the geometric monodromy on the rank-two
Tate module is open in the expected `SL_2` group.  In particular the geometric
rank-two `R^1` sheaf is irreducible.

After the standard half-Tate normalization it is pointwise pure of weight zero.
The five finite singularities are tame multiplicative fibers.  There is at
most one additional singular point at infinity.  For elliptic curves in
characteristic `p>3`, wild inertia on the `l`-adic Tate module is trivial;
therefore the Swan conductors vanish.  Hence the normalized sheaves have an
absolute conductor bound independent of `p,K,lambda`.

The only remaining input needed for quasi-orthogonality is geometric
non-isomorphism.  Here the singular support itself classifies the generic
parameters.

## 6. Singular support recovers the parameter class

The finite singular support is the root set of the squarefree polynomial

```text
S_(s,d)(t)=(dt-2)R_(s,d)(t).                             (29)
```

Expanding,

```text
S_(s,d)(t)
 =d^3 t^5
  +(-2d^4+2d^2s^2-10d^2)t^4
  +(24d^3-8ds^2+32d)t^3
  +(-104d^2+8s^2-32)t^2
  +192dt-128.                                            (30)
```

Suppose two generic normalized `R^1` sheaves are geometrically isomorphic.
Their local monodromy loci coincide, hence their five finite singular points
coincide.  Therefore their support polynomials are proportional.  The constant
coefficient in (30) is always `-128`, so the proportionality constant is one.
The coefficient of `t` then gives

```text
d'=d,                                                    (31)
```

and the coefficient of `t^2` gives

```text
s'^2=s^2.                                                (32)
```

Thus either

```text
(s',d')=(s,d)                                            (33)
```

or

```text
(s',d')=(-s,d).                                          (34)
```

Returning to `(alpha,beta)`, these are exactly

```text
(alpha',beta')=(alpha,beta)                              (35)
```

or

```text
(alpha',beta')=(-beta,-alpha).                           (36)
```

Because `c(h^(-1))=-c(h)`, the second case is the exact parameter involution

```text
lambda*=(h2^(-1),h1^(-1)).                               (37)
```

Consequently every generic sheaf has at most two generic parameters that can
belong to its geometric isomorphism class.  No separate classification of
function-field isogenies is required.

## 7. Generic trace quasi-orthogonality

Normalize

```text
K_lambda(t)=a_lambda(t)/sqrt(p).                         (38)
```

The sheaves behind `K_lambda` are geometrically irreducible, pointwise pure of
weight zero, and have uniformly bounded conductor.  The standard
Deligne/Fouvry--Kowalski--Michel quasi-orthogonality theorem therefore gives,
for generic `lambda,mu` outside the same/involution relation,

```text
sum_t a_lambda(t) overline(a_mu(t))=O(p^(3/2)),          (39)
```

with an absolute implied constant.  For the `O(K^2)` same/involution ordered
pairs, the trivial Weil bound gives

```text
sum_t |a_lambda(t)a_mu(t)|=O(p^2).                       (40)
```

There are `O(K^4)` remaining ordered generic pairs.  Hence, with

```text
A_g(t)=sum_{lambda in Lambda_g} a_lambda(t),             (41)
```

one has

```text
sum_t |A_g(t)|^2
 =O(K^2p^2+K^4p^(3/2)).                                  (42)
```

## 8. The spike is exactly a Cayley-difference energy

Define

```text
D(t)=#{lambda in Lambda_g:t_lambda=t}.                   (43)
```

The map `d -> 2/d` permutes the nonzero field elements.  Since
`d=alpha-beta` and `Lambda_g` is a subset of the ordered distinct pairs from
`A`,

```text
sum_{t!=0}D(t)^2
 <=sum_{x!=0}r_(A-A)(x)^2
 <=E_+(A).                                               (44)
```

Summing (26) over generic parameters gives

```text
O_g(t)
 =|Lambda_g|p+pD(t)-A_g(t)+E_g(t),                       (45)

|E_g(t)|=O(K^2).                                         (46)
```

Therefore, with variance over `t!=0`,

```text
Var O_g
 =O(
      p E_+(A)
      +K^2p
      +K^4 sqrt(p)
      +K^4
    ).                                                   (47)
```

The term `K^2p` has been retained although it is already present in (42), to
make the self-correlation scale explicit.

## 9. The `O(K)` special parameter strata

It remains to bound

```text
Lambda_s=H^2\Lambda_g,
|Lambda_s|=4K-3.                                         (48)
```

No pairwise sheaf independence is needed here.

### 9.1 `h1=h2!=1`

Putting `d=0` in the cleared cubic factors out the forbidden diagonal `a-b`.
The residual valid curve is bilinear:

```text
8ab+A(t)a+B(t)b+8=0,                                    (49)
```

where

```text
A(t)=s^2t-4s-4t,
B(t)=-s^2t-4s+4t.                                       (50)
```

Equivalently,

```text
(8a+B(t))(8b+A(t))=A(t)B(t)-64.                         (51)
```

For all but at most two `t`, this has `p-1` affine points before bounded domain
corrections.  At the exceptional `t` it has `O(p)` points.  Thus each diagonal
class has variance `O(p)`.

### 9.2 `h1h2=1`, `h1!=1`

Here `s=0`, `d!=0`.  Formula (13) is not identically zero: outside at most five
`t` the branch quartic is squarefree and the projective fiber is smooth genus
one.  Hasse gives `p+O(sqrt(p))` points on those fibers, while each of the
boundedly many singular fibers has `O(p)` points by the degree bound.  Hence
each inverse-pair class has variance `O(p)`.

### 9.3 Exactly one of `h1,h2` equals `1`

For example, if `h1=1` and `h2!=1`, then `c(1/u)=-a`.  With
`beta=c(h2)`, clearing

```text
2/(a-b)+2/(-a-T_beta(b))=t                              (52)
```

produces a plane cubic quadratic in each variable.  Its branch-quartic
discriminant is, up to a nonzero scalar,

```text
t^6(beta-1)^2(beta+1)^2(t^2+8 beta t+16).               (53)
```

Since `beta!=+-1`, on the variance domain `t!=0` there are at most two singular
fibers.  The same smooth-genus-one/Hasse argument gives variance `O(p)` per
class.  The case `h2=1` is symmetric.

### 9.4 `(h1,h2)=(1,1)`

Both transformed Cayley coordinates change sign, so the two differences cancel
identically.  Hence

```text
O_(1,1)(t)=0,  t!=0.                                    (54)
```

By Cauchy--Schwarz across the `O(K)` special classes,

```text
Var O_s=O(K^2p).                                         (55)
```

## 10. Main theorem

### Theorem 1 (corrected off/off elliptic variance)
Let `p>3` be prime and let `H<=F_p^*` have odd order `K`.  For the pure off/off
term `O(t)` in the exact fourth-moment pair-key decomposition,

```text
Var_{t!=0} O(t)
 << p E_+(c(H\{1}))
    +K^2p
    +K^4 sqrt(p)
    +K^4,                                                (56)
```

with an absolute implied constant.

### Proof
Decompose `O=O_g+O_s`.  Equation (47) bounds the generic part and (55) bounds
the special part.  The covariance is absorbed by

```text
Var(X+Y)<=2Var X+2Var Y.                                 (57)
```

This proves (56).

## 11. Unconditional consequence from the maintained direct Cayley bound

The maintained Stepanov theorem gives, whenever

```text
100<K<p^(3/4)/3,                                         (58)
```

```text
E_+(A)<34K^(8/3).                                        (59)
```

Therefore

```text
Var_{t!=0}O(t)
 << pK^(8/3)+K^4 sqrt(p)+K^2p+K^4.                      (60)
```

In particular, in the BGS-moment regime

```text
K=o(p^(1/4)),                                             (61)
```

the elliptic cross-correlation term is lower order and

```text
Var_{t!=0}O(t)<<pK^(8/3).                                (62)
```

Thus the former elliptic/sheaf draft is no longer an independent obstacle at
that scale.  Improving `8/3` to the natural quadratic exponent is exactly the
same pointwise centered Cayley-energy problem already isolated in the mixed
layer.

If the desired centered estimate

```text
E_+(A)=(K-1)^4/p+O(K^(2+o(1)))                           (63)
```

is eventually proved, (56) immediately gives

```text
Var O(t)
 <<pK^(2+o(1))+K^4 sqrt(p)+K^4,                          (64)
```

and hence the natural quadratic off/off scale throughout `K=o(p^(1/4))`.

## 12. Correction to the historical draft

The historical target

```text
O(K^2p+K^4 sqrt(p)+K^4)
```

was missing the reducible-fiber spike (24).  It is therefore not valid without
an additional Cayley-energy hypothesis.  The corrected unconditional statement
is (56).

This correction is structural, not cosmetic: parameter classes with equal
`alpha-beta` place their `O(p)` spikes at the same `t`, and their aggregate
second moment is precisely controlled by the Cayley difference energy in
(44).

## Evidence boundary

- The algebraic discriminant, line factorization, singular-support recovery,
  and special-stratum formulas are exact symbolic identities.
- Igusa's theorem is used only to deduce geometric irreducibility from the
  explicitly proved non-isotriviality.
- Deligne/Fouvry--Kowalski--Michel quasi-orthogonality is invoked only after
  purity, bounded conductor, and geometric non-isomorphism have been checked.
- The finite regression is not used as proof of Theorem 1.
- Theorem 1 is a fourth-moment/off-off variance result, not a microscopic
  BGS/GOE local-statistics theorem.
