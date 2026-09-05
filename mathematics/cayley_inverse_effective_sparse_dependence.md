# Effective bounded exponent dependence for shared inverse edge factors

**Status: EXACT + EXTERNAL-THEOREM for effectivity of the bounded exponent relation; OPEN for computing practical numerical bounds and classifying the resulting affine families.**

This note strengthens the bounded-affine-family reduction in
`cayley_inverse_sparse_unlikely_intersection.md`.

The external input is Theorem 2 of Filaseta--Granville--Schinzel,
*Irreducibility and greatest common divisor algorithms for sparse polynomials*,
Number Theory and Polynomials, LMS Lecture Note Series 352 (2008), 155--176.
They state that for fixed coprime

```text
F,G in Q[x_1,...,x_k]
```

there is an **effectively computable** number `B(F,G)` such that, if `xi` is a
nonzero algebraic number and

```text
F(xi^u_1,...,xi^u_k)=G(xi^u_1,...,xi^u_k)=0,             (1)
```

then either `xi` is a root of unity or there is a nonzero integer vector `v`
with

```text
||v||_infinity <= B(F,G),
v dot u = 0.                                                (2)
```

The paper explicitly notes that the bound `B(F,G)` is effectively computable,
although it does not provide this project with a ready small numerical value.

## 1. Interior edge pairs

Use the Laurent equations from the companion note,

```text
L_1=X+X^-1+Y+Y^-1-2Z-2Z^-1,
L_2=U+U^-1+V+V^-1-2Z-2Z^-1.                              (3)
```

Clear negative exponents by the monomials shown below:

```text
F_int = X Y Z L_1,
G_int = U V Z L_2.                                        (4)
```

These are ordinary polynomials in

```text
Q[X,Y,U,V,Z].                                             (5)
```

The project-specific geometry verifier checks exactly that they are coprime.
The proof in `cayley_inverse_sparse_unlikely_intersection.md` gives the same
fact abstractly from Laurent width.

For an interior index quadruple `(a,b,c,d)` and a common reciprocal root
`alpha`, put

```text
u=(a,b,c,d,1).                                            (6)
```

Then the two inverse edge equations imply

```text
F_int(alpha^a,alpha^b,alpha^c,alpha^d,alpha)=0,
G_int(alpha^a,alpha^b,alpha^c,alpha^d,alpha)=0.            (7)
```

### Theorem 1 (effective interior affine relation)

There is an effectively computable absolute integer

```text
B_int = B(F_int,G_int)                                    (8)
```

such that every common **non-torsion** irreducible factor of two interior
inverse edge polynomials forces a nonzero

```text
(r,s,t,u,v) in Z^5,
max(|r|,|s|,|t|,|u|,|v|) <= B_int,                       (9)
```

with

```text
r a+s b+t c+u d+v=0.                                     (10)
```

### Proof

Choose a reciprocal root `alpha` of the common factor which is not a root of
unity.  Apply the external theorem to (7) and (6).  The resulting bounded
integer vector is orthogonal to `(a,b,c,d,1)`, which is exactly (10). `□`

Thus the finite collection of possible coefficient vectors in the affine
reduction is **effectively enumerable in principle**.

## 2. One zero endpoint

For

```text
e={0,b},
f={c,d},                                             (11)
```

use

```text
L_0=2+Y+Y^-1-2Z-2Z^-1,
L_2=U+U^-1+V+V^-1-2Z-2Z^-1,
F_0=Y Z L_0,
G_0=U V Z L_2.                                            (12)
```

The ordinary polynomials `F_0,G_0` are coprime.  The external theorem gives an
effectively computable

```text
B_0=B(F_0,G_0)                                            (13)
```

such that every non-torsion common factor forces

```text
r b+s c+t d+v=0                                           (14)
```

for a nonzero integer vector of sup norm at most `B_0`.

## 3. Both edges contain zero

For distinct

```text
e={0,b},
f={0,d},                                             (15)
```

put

```text
M_1=2+Y+Y^-1-2Z-2Z^-1,
M_2=2+V+V^-1-2Z-2Z^-1,
F_00=Y Z M_1,
G_00=V Z M_2.                                             (16)
```

Again the cleared polynomials are coprime.  Hence an effectively computable

```text
B_00=B(F_00,G_00)                                         (17)
```

exists, and every non-torsion common factor forces

```text
r b+s d+v=0                                               (18)
```

with a nonzero bounded integer vector.

## 4. What 'effective' does and does not mean here

The result is stronger than a purely existential unlikely-intersection
reduction:

```text
non-torsion shared factor
 -> one relation vector from an effectively finite search box.             (19)
```

But two substantial obligations remain.

1. **Practical bound extraction.**  The external paper guarantees that
   `B(F,G)` can be calculated; no small numerical values for the three fixed
   pairs (4), (12), (16) have been extracted in this project.
2. **Affine-family classification.**  Even after the finite set of coefficient
   vectors is known, each equation such as (10) contains infinitely many
   integer endpoint tuples.  One still has to prove that every compatible
   family yields only torsion common factors, or exhibit a genuine non-torsion
   family.

Therefore this note does **not** prove the open statement

```text
all shared inverse edge-polynomial factors are torsion.                 (20)
```

It makes the reduction algorithmic in principle.

## 5. Relation to sparse-GCD algorithms

The same Filaseta--Granville--Schinzel paper proves quasi-linear-in-`log n`
algorithms for several fixed-sparsity factorization/GCD tasks, using repeated
bounded multiplicative-dependence reductions.  Those algorithmic results are
consistent with the present structure but do not by themselves give a uniform
closed form for the inverse edge gcds: our reciprocal edge polynomials can have
cyclotomic factors, and the universal classification of their shared torsion
part remains a separate task.

The present exact chain is therefore

```text
shared inverse edge factor
 -> torsion, or effectively bounded affine exponent relation
 -> classify the finitely many relation types
 -> remove characteristic-zero gcd
 -> reduced ordinary resultant
 -> one-prime-ideal split support.                         (21)
```

The downstream largest-prime, general-ratio, Cayley-energy, and microscopic
BGS problems remain open.
