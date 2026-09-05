# Shared sum-difference signatures force torsion inverse gcds

**Status: EXACT for the torsion classification when two edge signatures intersect; EXACT + EXTERNAL-THEOREM for prime-conductor support-freeness via the general torsion-factor theorem; FINITE-REGRESSION for the maintained `K=31` census.**

The shared-endpoint theorem removes one elementary sector from the inverse
shared-factor problem.  This note removes a second sector that includes many
**disjoint** edge pairs.

For an edge

```text
e={a,b},  0<=a<b,                                          (1)
```

define its sum-difference signature

```text
Sigma(e)={a+b,b-a}.                                        (2)
```

If two distinct valid edges have intersecting signatures, then every common
reciprocal root is a root of unity.  Hence their polynomial gcd is torsion and,
for prime conductor `K`, support-free.

## 1. Half-angle product identity

Let `z!=0` and choose `y` with

```text
y^2=z.                                                     (3)
```

Put

```text
q_n(y)=y^n+y^-n.                                           (4)
```

For `e={a,b}`, set

```text
S_e=a+b,
D_e=b-a.                                                   (5)
```

Then

```text
t_a(z+z^-1)+t_b(z+z^-1)
 =q_(S_e)(y) q_(D_e)(y).                                  (6)
```

Indeed the right side expands to

```text
y^(2b)+y^(-2b)+y^(2a)+y^(-2a)
 =z^b+z^-b+z^a+z^-a.                                      (7)
```

## 2. Intersecting signatures force torsion

Let `e,f` be distinct valid edges and suppose

```text
Sigma(e) cap Sigma(f) != empty.                           (8)
```

Choose

```text
n in Sigma(e) cap Sigma(f).                               (9)
```

Write the other signature entries as `r` for `e` and `s` for `f`, so that

```text
{S_e,D_e}={n,r},
{S_f,D_f}={n,s}.                                          (10)
```

### Theorem 1 (signature-torsion theorem)

Every common irreducible factor of the inverse edge polynomials

```text
w_e(T), w_f(T)                                             (11)
```

is torsion.

### Proof

Let `T_0` be a common root and choose

```text
T_0=z+z^-1,
z=y^2.                                                     (12)
```

The direct trace identity

```text
-(T-2)w_e(T)=t_a(T)+t_b(T)-2T                             (13)
```

shows that both edge equations have the same right side `2T_0`.  Subtracting
them and applying (6) gives

```text
q_n(y)(q_r(y)-q_s(y))=0.                                  (14)
```

If

```text
q_n(y)=0,
```

then

```text
y^(2n)=-1,                                                (15)
```

so `y`, hence `z=y^2`, is a root of unity.

Otherwise

```text
q_r(y)=q_s(y).                                            (16)
```

Multiplying by `y^r` factors exactly as

```text
(y^(r-s)-1)(y^(r+s)-1)=0                                  (17)
```

(up to exchanging `r,s` if necessary).  Again `y` and `z` are roots of unity.

Thus every reciprocal root of every common factor is torsion. `□`

The proof does not require the two edges to be disjoint.  Its main use is the
disjoint sector not covered by the shared-endpoint theorem.

## 3. Prime-conductor support is automatically empty

Let `K>=7` be the prime conductor and assume the two edges are valid for that
`K`.  The general theorem in

```text
cayley_inverse_torsion_factors_support_free.md
```

proves that every torsion factor `G` of a valid inverse edge satisfies

```text
|Res_T(C_K,G)|=1.                                         (18)
```

### Corollary 2

If (8) holds and

```text
G=gcd_Z[T](w_e,w_f),                                      (19)
```

then

```text
|Res_T(C_K,G)|=1.                                         (20)
```

Hence intersecting-signature gcd factors can be removed completely before the
same-embedding reduced-resultant arithmetic.

## 4. What remains open

Combining this note with `cayley_inverse_shared_endpoint_torsion.md`, a
non-torsion shared factor can occur only if

```text
1. e and f are disjoint, and
2. Sigma(e) cap Sigma(f)=empty.                            (21)
```

This is a strictly smaller input class for the sparse unlikely-intersection and
Filaseta--Granville--Schinzel reductions.

At `K=31`, the exact census in the companion verifier is:

```text
861 disjoint edge pairs with nonconstant polynomial gcd,
255 have intersecting sum-difference signatures,
606 remain signature-disjoint.                            (22)
```

All `861` are torsion in this finite conductor audit, but only the first `255`
are covered by Theorem 1.  The remaining `606` are finite evidence for the
still-open generic disjoint torsion classification.

## 5. Finite regression

`computations/verification/cayley_inverse_signature_torsion.py` checks:

- the half-angle product identity (6) on an integer grid;
- the factorization (17);
- the exact `K=31` census in (22);
- support-free real-cyclotomic resultants for every nonconstant gcd in the
  intersecting-signature sector.

The finite census is regression only; Theorem 1 is exact.
