# A reduced ordinary-resultant filter for inverse cross-class support

**Status: EXACT for the scalar necessary condition, radical divisibility, and reciprocal square-resultant identity; FINITE-REGRESSION for the exhaustive small-`K` gcd-unit audits and displayed cross-class/structural anchors; OPEN for a uniform polynomial bound on the relevant reduced resultants.**

This note supplements

```text
cayley_inverse_associate_quotient.md
cayley_inverse_cyclotomic_unit_normalization.md
```

with a rational scalar obstruction that is cheaper than ideal contraction.
It is deliberately one-way: an ordinary polynomial resultant may have rational
prime divisors that do not correspond to the distinguished real cyclotomic
root `tau`, and no converse is asserted.

## 1. Edge polynomials before specializing `tau`

Let `K=2m+1` be an odd prime and let

```text
C_K(T) in Z[T]
```

be the monic minimal polynomial of

```text
tau=zeta+zeta^-1,
deg C_K=m.
```

Write

```text
t_n(T)=2 T_n(T/2),
v_0(T)=0,
v_n(T)=(t_n(T)-2)/(T-2),
w_(a,b)(T)=2-v_a(T)-v_b(T).                              (1)
```

For a valid edge `e={a,b}`, specializing `T=tau` gives the reduced inverse
edge generator used throughout the associate-quotient notes.

If `b=max(a,b)>=2`, then `v_b` is monic of degree `b-1`, so

```text
deg w_(a,b)=b-1 <= m-1 < deg C_K.                        (2)
```

In particular no valid edge polynomial is divisible by `C_K` over `Q`.

## 2. Remove characteristic-zero polynomial gcds first

Fix two valid edges `e,f`.  Choose the monic primitive gcd

```text
G_(e,f)=gcd_Z[T](w_e,w_f),                               (3)
```

and write

```text
w_e=G A,
w_f=G B,
gcd_Z[T](A,B)=1.                                      (4)
```

By (2),

```text
Res_T(C_K,G) != 0.                                       (5)
```

By construction,

```text
Res_T(A,B) != 0.                                         (6)
```

Define the positive integer

```text
Rred_(K;e,f)
 = |Res_T(C_K,G) Res_T(A,B)|.                            (7)
```

When `G=1`, this is simply the absolute ordinary resultant

```text
|Res_T(w_e,w_f)|.                                        (8)
```

## 3. Exact scalar filter

### Theorem 1 (same-embedding support implies scalar divisibility)

Let `p` be a rational prime and let `q|p` be a prime ideal of `O^+=Z[tau]`.
If

```text
w_e(tau) == w_f(tau) == 0 mod q,                         (9)
```

then

```text
p | Rred_(K;e,f).                                        (10)
```

### Proof

Reduce (4) modulo `q` and write `t` for the residue class of `tau`.
Since `C_K(t)=0`, there are two cases.

If

```text
G(t)=0,
```

then the reductions of `C_K` and `G` have a common root in the residue field,
so their polynomial resultant vanishes modulo `p`:

```text
p | Res_T(C_K,G).                                        (11)
```

If `G(t)!=0`, equations (9) and (4) imply

```text
A(t)=B(t)=0.
```

Hence the reductions of `A` and `B` have a common root and

```text
p | Res_T(A,B).                                          (12)
```

In either case (10) follows.  Degree drop modulo `p` cannot invalidate this
one-way implication: the resultant is a universal polynomial in the
coefficients, and a common root still forces its reduction to vanish. `□`

The theorem does not use splitting.  On the split locus `p==1 mod K`, condition
(9) is exactly a same-real-embedding two-edge event.

## 4. Consequence for associate-quotient contractions

For two nonassociate edges, recall the exact contraction integer

```text
(w_e(tau),w_f(tau)) cap Z = D_(K;e,f) Z.                 (13)
```

### Corollary 2 (radical divisibility)

For every pair of nonassociate valid edges,

```text
rad D_(K;e,f) | rad Rred_(K;e,f).                        (14)
```

Hence

```text
P^+(D_(K;e,f)) <= P^+(Rred_(K;e,f))                     (15)
```

whenever the contraction is nontrivial.

### Proof

Every rational prime divisor of `D_(K;e,f)` is supported by a common prime
ideal `q` containing both edge generators.  Theorem 1 puts that rational prime
in the support of `Rred_(K;e,f)`. `□`

Valuation divisibility is **not** claimed.

### Corollary 3 (support-free polynomial gcd case)

If

```text
|Res_T(C_K,G_(e,f))|=1,                                  (16)
```

then every rational same-embedding support prime divides the single scalar

```text
|Res_T(A,B)|.                                            (17)
```

Thus characteristic-zero common polynomial factors can be discarded entirely
whenever their value at the real `K`-cyclotomic root is a unit.

## 5. Exact reciprocal square identity

The direct trace edge polynomial from
`cayley_inverse_cyclotomic_unit_normalization.md` is

```text
P_(a,b)(T)=t_a(T)+t_b(T)-2T.                             (18)
```

The exact identity

```text
P_(a,b)(T)=-(T-2) w_(a,b)(T)                             (19)
```

shows why every cleared Laurent edge equation has a universal double root at
`z=1`: under `T=z+z^-1`, the factor `T-2` becomes `(z-1)^2/z`.

The square observed in reciprocal Laurent resultants is itself exact.

### Theorem 4 (reciprocal lift squares the resultant)

Let `A(T),B(T)` be nonzero polynomials over a field, of degrees `r,s`, and set

```text
A~(z)=z^r A(z+z^-1),
B~(z)=z^s B(z+z^-1).                                     (20)
```

Then

```text
Res_z(A~,B~)=Res_T(A,B)^2.                               (21)
```

### Proof

Write

```text
A(T)=a_r product_i (T-alpha_i).
```

For every root `alpha_i`, the equation

```text
z+z^-1=alpha_i
```

has the reciprocal pair of roots `z_i,z_i^-1`; this remains true with
multiplicity at the branch values `alpha_i=+-2`.  Moreover

```text
B~(z_i) B~(z_i^-1)
 =z_i^s z_i^-s B(alpha_i)^2
 =B(alpha_i)^2.                                          (22)
```

The leading coefficient of `A~` is `a_r`.  Therefore the root-product formula
gives

```text
Res_z(A~,B~)
 =a_r^(2s) product_i B(alpha_i)^2
 =[a_r^s product_i B(alpha_i)]^2
 =Res_T(A,B)^2.                                          (23)
```

This proves (21). `□`

Thus, after dividing the universal `(z-1)^2` factor coming from `T-2`, the
Laurent/reciprocal resultant carries exactly the same prime information as the
real-trace resultant, with doubled valuations.  The real variable `T` is the
more economical representation.

## 6. Finite exact audits

`computations/verification/cayley_inverse_reduced_resultant_filter.py` contains
three kinds of exact regression.

### Exhaustive gcd-unit audits

For every unordered pair of valid inverse edges at

```text
K=31,37,41,43,                                            (24)
```

the script computes `G=gcd(w_e,w_f)`.  Whenever `deg G>0`, it checks exactly

```text
|Res(C_K,G)|=1.                                          (25)
```

For example at `K=31` there are `105` valid edges and `5460` edge pairs;
`1283` pairs have a nonconstant polynomial gcd, and all `1283` gcds are
support-free in the sense (25).

This is finite evidence, not a growing-`K` theorem.

A separate exact factor inspection at `K=31` finds that all `15` distinct gcd
polynomials lift under `T=z+z^-1` to products of ordinary cyclotomic
polynomials (orders at most `8` in this audit).  This strongly suggests a
torsion-factor classification, but no universal classification is claimed here.

### Cross-class anchors

For the calibrated same-embedding cross-class pairs one obtains

```text
K=59,  e=(8,26),  f=(9,10):
  Res(w_e,w_f)=283 * 21713;

K=73,  e=(2,3),   f=(8,34):
  Res(w_e,w_f)=13^2 * 6571 * 19301;

K=97,  e=(4,13),  f=(22,30):
  Res(w_e,w_f)=23 * 443 * 69259.                         (26)
```

In each displayed case the actual split same-embedding support prime occurs as
one factor of the ordinary resultant.  The additional factors are false
positives for the distinguished `K`-cyclotomic embedding; this is why Theorem 1
is not stated as a converse.

### Structural large-prime anchors

For the universal characteristic-zero associate families:

```text
K=89,  e=(16,35), f=(20,33):
  |Res(w_e,w_f)|=143207231;

K=229, e=(44,91), f=(48,89):
  |Res(w_e,w_f)|=33893 * 966684838398077.                (27)
```

The large structural prime can therefore remain enormous even in this scalar
presentation.  This is expected: the reduced-resultant filter does not quotient
characteristic-zero edge association by itself.

## 7. What this changes, and what it does not

For nonassociate edge classes, the ideal contraction `D_(K;e,f)` remains the
exact same-embedding object.  The new scalar `Rred_(K;e,f)` is a **necessary
filter** whose prime support is easier to compute and may be easier to bound.

The highest-value next structural theorem would be:

```text
all polynomial gcd factors G_(e,f) are torsion factors whose evaluation at
C_K is a unit, for prime K in the valid range.            (28)
```

If (28) holds, every cross-class support prime divides the ordinary coprime
resultant `Res(A,B)`.  A second, still open, step would then be to prove a
polynomial largest-split-prime bound for these reduced resultants, ideally below
the `K^(4+o(1))` threshold required by the intended `K=o(p^(1/4))` regime.

Neither (28) nor such a prime-size bound is claimed here.
