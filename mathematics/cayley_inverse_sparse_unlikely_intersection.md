# Sparse unlikely intersections for shared inverse edge factors

**Status: EXACT + EXTERNAL-THEOREM for the bounded-affine-family reduction; OPEN for classification/elimination of the resulting affine exponent families.**

This note attacks the open torsion-factor question from
`cayley_inverse_reduced_resultant_filter.md` by using the unlikely-intersection
structure of a **fixed** algebraic torus variety.  It does not prove that every
shared factor is torsion.  What it proves is that every non-torsion shared factor
forces one bounded-coefficient affine relation among the four edge indices.
Thus the universal torsion-factor conjecture reduces to finitely many affine
exponent families.

The external input is Theorem 3.1 of Amoroso--Leroux--Sombra,
*Overdetermined systems of sparse polynomial equations*, arXiv:1307.5788
(the theorem is stated there in the refined Bombieri--Masser--Zannier form).
Its load-bearing consequence is recalled explicitly in Section 3.

## 1. The inverse edge equation in one multiplicative parameter

For an edge `e={a,b}` put

```text
P_(a,b)(T)=t_a(T)+t_b(T)-2T=-(T-2)w_(a,b)(T),            (1)
```

where

```text
t_n(z+z^-1)=z^n+z^-n.                                    (2)
```

Hence a nonzero complex number `alpha` satisfies

```text
P_(a,b)(alpha+alpha^-1)=0                                (3)
```

if and only if

```text
alpha^a+alpha^-a+alpha^b+alpha^-b
 =2(alpha+alpha^-1).                                      (4)
```

A common irreducible factor of `w_(a,b)` and `w_(c,d)` is called **torsion**
here if every irreducible factor of its reciprocal lift

```text
z^deg(G) G(z+z^-1)                                       (5)
```

is cyclotomic.  Equivalently, all reciprocal roots are roots of unity.

If a common factor is not torsion, one may therefore choose a common trace root
`T_0` and a solution

```text
alpha+alpha^-1=T_0                                      (6)
```

with

```text
alpha notin mu_infinity.                                 (7)
```

Equation (1) then turns that one non-torsion `alpha` into two equations of the
form (4).

## 2. Quotient out the built-in reciprocal relations first

A naive sparse embedding would use separate coordinates for
`alpha^a,alpha^-a,...`.  That is useless for unlikely-intersection purposes:
the exponent vector then has tautological bounded relations such as

```text
a+(-a)=0.                                                (8)
```

Instead use only one coordinate for each endpoint exponent.

For four nonzero endpoint indices define the fixed Laurent polynomials on
`G_m^5` with coordinates `(X,Y,U,V,Z)`:

```text
L_1=X+X^-1+Y+Y^-1-2Z-2Z^-1,
L_2=U+U^-1+V+V^-1-2Z-2Z^-1.                              (9)
```

Let

```text
W=V(L_1,L_2) subset G_m^5.                               (10)
```

For an index quadruple `(a,b,c,d)` define

```text
phi_(a,b,c,d): G_m -> G_m^5,
phi(x)=(x^a,x^b,x^c,x^d,x).                              (11)
```

Then

```text
alpha is a common zero of the two edge equations
iff
phi_(a,b,c,d)(alpha) in W.                               (12)
```

Crucially, `W` is fixed: all dependence on the edge indices is in the
one-parameter homomorphism (11).

## 3. Codimension of the fixed variety

### Lemma 1

Every irreducible component of `W` has codimension exactly `2` in `G_m^5`.

### Proof

Work in the Laurent UFD

```text
R=Q[X^+-1,Y^+-1,U^+-1,V^+-1,Z^+-1].                     (13)
```

The two Laurent polynomials in (9) are coprime.  Indeed, regard the ring as a
Laurent polynomial ring in `X` over the fraction field of the other variables.
Then `L_1` is nonconstant in `X`, whereas `L_2` is a nonzero constant in `X`,
so their gcd in that fraction-field Laurent ring is `1`; Gauss's lemma gives
coprimality in `R`.

Therefore no height-one prime of the UFD `R` contains both `L_1,L_2`.  Every
minimal prime over `(L_1,L_2)` has height at least `2`.  Krull's principal ideal
theorem gives height at most `2`.  The ideal is proper because

```text
(1,1,1,1,1) in W.                                       (14)
```

Hence every component has height, equivalently codimension, exactly `2`. `□`

## 4. External unlikely-intersection input

Theorem 3.1 of Amoroso--Leroux--Sombra states the following form sufficient
here.

> Let `C` be an irreducible subvariety of `G_m^N` of codimension at least `2`.
> There is a constant `c_C`, depending only on `C`, such that if
> `(zeta_1 alpha^a_1,...,zeta_N alpha^a_N)` lies in `C`, with the `zeta_j`
> roots of unity, then there is a nonzero integer vector `r` with
> `max |r_j|<=c_C` whose corresponding multiplicative monomial equals `1`.
> If `alpha` is not a root of unity, this forces
> `sum_j a_j r_j=0`.

Only this existence statement is used below.  No effective numerical value of
the constants is asserted in this project.

Since `W` has finitely many irreducible components, Lemma 1 lets us set

```text
C_int=max_C c_C,                                         (15)
```

where the maximum runs over those components.

## 5. Interior-edge reduction

### Theorem 2 (bounded affine relation for a non-torsion common factor)

Let

```text
2<=a<b,
2<=c<d,                                                   (16)
```

and suppose `w_(a,b)(T)` and `w_(c,d)(T)` have a common non-torsion irreducible
factor over `Q`.

Then there exists

```text
(r,s,t,u,v) in Z^5 \ {0},
max(|r|,|s|,|t|,|u|,|v|) <= C_int,                       (17)
```

such that

```text
r a+s b+t c+u d+v=0.                                     (18)
```

The constant `C_int` is independent of `a,b,c,d` and of the cyclotomic
conductor `K` in which the edge indices may later be used.

### Proof

Choose a non-torsion reciprocal root `alpha` as in (6)--(7).  By (12),

```text
(alpha^a,alpha^b,alpha^c,alpha^d,alpha) in W.             (19)
```

It lies in one irreducible component `C` of `W`, and Lemma 1 gives
`codim(C)=2`.  Apply the external theorem with all torsion multipliers equal to
`1` and exponent vector

```text
(a,b,c,d,1).                                              (20)
```

We obtain a nonzero integer vector as in (17) for which

```text
alpha^(r a+s b+t c+u d+v)=1.                             (21)
```

Because `alpha` is not a root of unity, the exponent in (21) is zero.  This is
(18). `□`

### Corollary 3 (finite affine-family reduction)

All interior quadruples supporting a non-torsion common factor lie in the
finite union

```text
union_(0!=q in Z^5, ||q||_infinity<=C_int)
  { (a,b,c,d): q_1 a+q_2 b+q_3 c+q_4 d+q_5=0 }.          (22)
```

Thus the non-torsion shared-factor problem is no longer a four-parameter
unrestricted problem: it is a finite collection of affine three-parameter
families with bounded integer coefficients.

This does **not** say that those families actually contain non-torsion factors.

## 6. Boundary edge with index zero

Valid inverse edges may contain the class `0`.  For a pair of **disjoint**
edges, at most one edge can contain `0`.  Suppose for definiteness

```text
e={0,b},
f={c,d},
```

with `b,c,d>=2` distinct.

Use the fixed variety in `G_m^4` with coordinates `(Y,U,V,Z)`:

```text
L_0=2+Y+Y^-1-2Z-2Z^-1,
L_2=U+U^-1+V+V^-1-2Z-2Z^-1.                              (23)
```

Exactly the argument of Lemma 1 shows that every irreducible component of

```text
W_0=V(L_0,L_2)                                           (24)
```

has codimension `2`.  Applying the same external theorem to

```text
x |-> (x^b,x^c,x^d,x)                                    (25)
```

gives an absolute constant `C_0` and a nonzero bounded vector

```text
(r,s,t,v) in Z^4,
max |.| <= C_0,                                           (26)
```

such that every non-torsion common factor forces

```text
r b+s c+t d+v=0.                                         (27)
```

The case in which the second edge contains `0` is symmetric.

## 7. What the reduction buys

The open torsion classification

```text
all shared inverse edge-polynomial factors are torsion                 (28)
```

is now reduced to the following sharper task:

1. classify the finitely many bounded-coefficient affine relations supplied by
   Theorem 2 and its boundary analogue that are compatible with distinct valid
   edges;
2. on each surviving affine family, prove that the common polynomial factors
   are cyclotomic/torsion, or exhibit a genuine non-torsion family.

The external theorem alone does not perform step 1 or 2.  In particular, the
finite max-index-50 audit in
`evidence/cayley_inverse_torsion_gcd_audit_20260905.txt` cannot be promoted to a
universal theorem merely because the affine coefficients are bounded: the
constant is not computed here and each affine hyperplane has infinitely many
integer points.

## 8. Relation to the large-prime inverse route

This characteristic-zero reduction sits **before** the finite-prime arithmetic:

```text
shared polynomial factor
    -> torsion factor or bounded affine exponent relation
    -> remove/classify characteristic-zero gcd
    -> coprime reduced ordinary resultant
    -> same-embedding split-prime filter
    -> inverse multiplicity.
```

If all surviving affine families can be shown torsion, then the first factor
`Res(C_K,G)` in the reduced-resultant filter becomes support-free uniformly
outside the finitely compatible torsion conductors.  The remaining open
arithmetic problem would be the largest split prime in the coprime resultant
`Res(A,B)` for nonassociate edge classes.

This note does not solve that prime-size problem, the other normalized ratio
classes, or microscopic BGS/RMT universality.
