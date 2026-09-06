# Product-row decomposition and elliptic cross-row geometry for Cayley energy

**Status: EXACT for the row decomposition, affine trace reduction, and genus-one cross-row reduction; FINITE-REGRESSION for the adversarial designs below.  The desired uniform/average `O(1)` cross-row intersection theorem remains OPEN.**

This note sharpens the product-row frontier isolated in
`cayley_shifted_energy_orbits.md`.  The main exact point is that the entire
characteristic-zero forced Cayley-energy baseline is contained in the
**self-energy of individual product rows**.  Consequently every finite-field
excess `Delta_K(p)` is exactly cross-row intersection mass.

The same cross-row term is a subgroup-point count on an explicit genus-one
curve.  This explains both the empirical small-intersection phenomenon and the
current `K^(2/3)` loss: generic fixed-degree curve/subgroup technology gives the
same exponent and does not close the quadratic target.

Throughout, `p` is an odd prime, `H<=F_p^*` has odd order `K`,

```text
B=H\{1},
c(x)=(x+1)/(x-1),
A=c(B),
```

and

```text
r(t)=#{(x,y) in B^2 : c(x)+c(y)=t}.
```

For the active BGS programme `K` is an odd prime, but the elementary row
identities below only require odd `K`.

## 1. Product rows

For `u in H`, define

```text
r_u(t)=#{(x,y) in B^2 : xy=u, c(x)+c(y)=t}.              (1)
```

Then

```text
r(t)=sum_{u in H} r_u(t).                                (2)
```

For `s=x+y` and `u=xy`, direct algebra gives

```text
c(x)+c(y)=2(u-1)/(u-s+1).                                (3)
```

The denominator is `(x-1)(y-1)` and is therefore nonzero on `B^2`.

### Central row `u=1`

If `xy=1`, then `y=x^(-1)` and

```text
c(y)=-c(x).
```

Hence

```text
r_1(0)=K-1,
r_1(t)=0 for t!=0,                                      (4)
```

so

```text
sum_t r_1(t)^2=(K-1)^2.                                 (5)
```

### Noncentral rows `u!=1`

There are exactly `K-2` ordered pairs `(x,y) in B^2` with `xy=u`: the two
choices `x=1` and `x=u` are excluded from the `K` pairs in `H^2`.

Because `u!=1`, equation (3) is injective in the symmetric coordinate `s`.
For fixed `(u,s)`, the two coordinates are the roots of

```text
Z^2-sZ+u=0,
```

so a represented value has row multiplicity at most two, with multiplicity two
coming exactly from swapping a non-diagonal pair.

Since `K` is odd, squaring is a bijection on `H`.  Thus there is a unique
`w in H` with `w^2=u`; for `u!=1` the pair `(w,w)` is the unique diagonal
pair in the row.  The other `K-3` ordered pairs form `(K-3)/2` swap pairs.
Therefore

```text
sum_t r_u(t)^2
 =1+4*(K-3)/2
 =2K-5                                                   (6)
```

for every `u!=1`.

## 2. Exact decomposition of the Cayley excess

Summing (5) and (6) over the `K` rows gives

```text
sum_{u in H} sum_t r_u(t)^2
 =(K-1)^2+(K-1)(2K-5)
 =3(K-1)(K-2).                                           (7)
```

The central row is supported only at `t=0`; every noncentral row has `t!=0`
by (3).  Expanding the square in (2), we obtain the exact identity

```text
E_+(A)
 :=sum_t r(t)^2
 =3(K-1)(K-2)
  +sum_{u!=v} sum_t r_u(t)r_v(t).                        (8)
```

For odd prime `K`, the repository excess is

```text
Delta_K(p)
 =E_+(A)-3(K-1)(K-2).                                   (9)
```

Indeed `A=-A`, and subtracting the zero-difference class `(K-1)^2` from
(7) recovers the maintained nonzero forced baseline `(K-1)(2K-5)`.
Consequently

> **Theorem 1 (cross-row excess identity).**
> For every odd prime `K` and split prime `p==1 (mod K)`,
>
> ```text
> Delta_K(p)=sum_{u!=v} <r_u,r_v>,
> <r_u,r_v>=sum_t r_u(t)r_v(t).                          (10)
> ```
>
> In particular every non-forced Cayley collision is cross-row: the full
> forced baseline is already exhausted by the row self-energies.

For distinct noncentral rows put

```text
I(u,v)=#{t : r_u(t)r_v(t)>0}.                            (11)
```

Since every noncentral row multiplicity is at most two,

```text
<r_u,r_v> <=4 I(u,v),                                   (12)
```

and therefore

```text
Delta_K(p)
 <=8 sum_{unordered {u,v} subset H\{1}} I(u,v).          (13)
```

Thus a uniform `I(u,v)=O(1)` theorem would immediately imply
`Delta_K(p)=O(K^2)`.

The single parameter `t=2` never causes a larger-scale obstruction: trivially
`r(2)<=K-1`, so its whole contribution to `E_+(A)` is at most `(K-1)^2`.
Accordingly it is enough, up to an already-quadratic term, to control finite
parameters after the Mobius change below.

## 3. Trace-set form of one row

Fix a noncentral row `u=w^2`, where the square root `w in H` is unique.  Write

```text
x=wz,
y=wz^(-1),
z in H.                                                   (14)
```

Put

```text
X=z+z^(-1).
```

Equation (3) becomes

```text
t_w(X)=2(w^2-1)/(w^2-wX+1).                              (15)
```

For `t!=2`, introduce

```text
mu=t/(2-t).
```

Then

```text
mu_w(X)=(1-w^2)/(wX-2).                                  (16)
```

The full trace set

```text
Z_H={z+z^(-1):z in H}                                   (17)
```

has cardinality `(K+1)/2`.  The two forbidden points `x=1` or `y=1` in
(14) correspond to the single trace value

```text
X=w+w^(-1),
```

and (16) sends this value to the artificial parameter `mu=-1`.  A zero
denominator `wX-2=0` is exactly the projective parameter `mu=infinity`, i.e.
`t=2`.

Hence the finite valid row is a fractional-linear image of `Z_H` with one
forced invalid trace removed and, when present, one pole removed.

## 4. Affine intersection of two trace copies

Let `u=w^2`, `v=q^2` be distinct noncentral rows.  Equality of two finite
parameters in (16) is equivalent to

```text
Y=alpha X+beta,                                          (18)
```

where

```text
X=z+z^(-1),
Y=y+y^(-1),
alpha=w(1-q^2)/(q(1-w^2)),
beta =2(q^2-w^2)/(q(1-w^2)).                             (19)
```

This is the exact affine trace-set reduction already anticipated in
`cayley_shifted_energy_orbits.md`.

The formulation (18) is useful computationally, but there is a stronger
geometric interpretation.

## 5. The cross-row curve has genus one

Regard (16) as a degree-two rational map on `P^1`:

```text
phi_w(z)
 =(1-w^2)z/(w(z^2+1)-2z).                                (20)
```

It is invariant under `z -> z^(-1)`.  Differentiating gives, up to a nonzero
scalar and the square of the denominator,

```text
phi_w'(z) proportional to 1-z^2.                         (21)
```

Thus the two ramification points are `z=+-1`, with branch values

```text
b_w^- =-(w+1)/2,
b_w^+ =(w-1)/2.                                          (22)
```

For two distinct `w,q in H\{1}`, the branch sets are disjoint.  Equality of a
branch value for `w` and one for `q` forces `q=w` or `q=-w`; the first is
excluded and the second is impossible because an odd-order subgroup does not
contain `-1`.

The fiber product

```text
C_(w,q): phi_w(z)=phi_q(y)                               (23)
```

has the explicit bidegree `(2,2)` equation

```text
(1-w^2) z [q(y^2+1)-2y]
 -(1-q^2) y [w(z^2+1)-2z]=0.                             (24)
```

Because the two quadratic covers have disjoint branch loci, their function
fields are distinct quadratic extensions of `Fbar_p(mu)` and the fiber product
is connected.  The degree-four map from its normalization to `P^1_mu` has four
branch values; above each, two points have ramification index two.  Therefore
Riemann--Hurwitz gives

```text
2g-2=4*(-2)+4*2=0,
```

so

> **Theorem 2 (elliptic cross-row reduction).**
> For distinct noncentral product rows, the normalization of `C_(w,q)` is a
> smooth geometrically connected genus-one curve.

Moreover, after excluding the two invalid-coordinate traces and the possible
`t=2` poles,

```text
sum_{t!=2} r_(w^2)(t) r_(q^2)(t)                         (25)
```

is exactly the number of corresponding `H x H` points on (24).

The two quadratic discriminants over the `mu`-line are

```text
D_w(mu)
 =(w^2-1)(-2mu+w-1)(2mu+w+1),                            (26)
```

and the analogous expression for `q`.  The quadratic subcover defined by
`D_w(mu)D_q(mu)` is a genus-one quartic with four branch points (22).  Their
cross-ratio can be chosen as

```text
lambda=((w-q)/(w+q))^2.                                  (27)
```

This quartic is a degree-two genus-one quotient of the biquadratic fiber
product; equation (27) is **not** used to identify the two curves as the same
elliptic curve.

## 6. Why generic curve technology does not close the target

Corvaja--Zannier subgroup-point technology, in the quantitative form quoted as
Lemma 3.1 by L. Merai and I. E. Shparlinski, *Sparsity of curves and additive
and multiplicative expansion of rational maps over finite fields*,
arXiv:1803.02165 (2018), bounds a fixed-degree non-exceptional curve on
`G x H` by a term of shape

```text
max(d^2 |G||H|/p, d^(4/3)(|G||H|)^(1/3)).                (28)
```

For the fixed-degree curve (24), `G=H` and `K^2<p`, this is only

```text
O(K^(2/3))                                                (29)
```

per row pair.  Summed over `O(K^2)` row pairs it lands at the already familiar
`O(K^(8/3))` scale.  Thus the genus-one reduction is not a disguised proof of
the sharp result: a successful argument must exploit **correlation across this
specific family** or stronger arithmetic restrictions on its split reductions,
not merely a worst-curve point theorem.

This literature comparison is an obstruction audit, not an additional active
bound used elsewhere in the repository.

## 7. Adversarial finite regression

`computations/verification/cayley_product_rows.py` verifies Theorem 1, the trace
parameterization, and the branch-locus separation on the following exact
designs:

```text
(p,K)=(199,11):      Delta=0,    max finite row intersection=0,
(p,K)=(461,23):      Delta=288,  max finite row intersection=2,
(p,K)=(47,23):       Delta=3856, max finite row intersection=5,
(p,K)=(680453,67):   Delta=624,  max finite row intersection=4,
(p,K)=(2908049,41):  Delta=192,  max finite row intersection=2,
(p,K)=(728017,29):   Delta=48,   max finite row intersection=1.
```

These are deliberately mixed positive and negative controls.

In particular:

- `(23,47)` disproves a uniform `I(u,v)<=3` claim with no size hypothesis;
- `(67,680453)` has `p>K^3` and disproves any inference that a cubic field-size
  inequality alone forces `I(u,v)<=2`;
- `(41,2908049)` has `p>K^4` and retains the previously recorded counterexample
  to the stronger exploratory `I(u,v)<=1` claim;
- the large `p>K^4` exceptional design `(29,728017)` still has nonzero Cayley
  excess, so small row intersections do not mean exact baseline.

Finite sweeps are not promoted to a growing-parameter theorem.

## 8. Closure target

The exact remaining target can now be stated in either of two equivalent
styles:

1. prove enough average sparsity for the affine intersections
   `Z_H intersect (alpha Z_H+beta)` with `(alpha,beta)` constrained by (19), or
2. prove an average `O(1)` (or `K^o(1)`) bound for the admissible `H x H` points
   on the genus-one family (24).

Either route would turn (10)--(13) into

```text
Delta_K(p)=O(K^(2+o(1))),                                (30)
```

which is the missing pointwise scale for the sharp centered Cayley-energy
programme.  No such theorem is proved here, and no microscopic BGS/GOE claim
follows from the present fourth-moment reductions.
