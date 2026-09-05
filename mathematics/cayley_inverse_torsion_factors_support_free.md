# Torsion inverse edge factors are prime-conductor support-free

**Status: EXACT + EXTERNAL-THEOREM for conductor-coprimality of every torsion reciprocal root and unit evaluation of every torsion edge factor; OPEN only for whether disjoint edge gcds can have non-torsion factors.**

This note upgrades the finite support-free gcd audits and the elementary
shared-endpoint theorem.  The conclusion no longer depends on how a torsion
factor arises: **every** torsion factor of **every** valid inverse edge
polynomial is harmless at the prime conductor `K`.

The external input is the minimal vanishing-sum theorem quoted in Section 2 of
Filaseta--Granville--Schinzel,
*Irreducibility and greatest common divisor algorithms for sparse polynomials*
(2008): if

```text
S=sum_(j=1)^t a_j omega_j=0                                (1)
```

is a minimal vanishing sum, with nonzero rational coefficients `a_j` and roots
of unity `omega_j`, and `k` is its reduced exponent (the least positive integer
for which every ratio `omega_i/omega_1` has `k`-th power `1`), then

```text
t >= gamma(k)=2+sum_(q|k)(q-2),                           (2)
```

and `k` is squarefree.  In particular every prime divisor of `k` is at most
`t`.

No finite-characteristic vanishing-sum theorem is used here; this is a purely
characteristic-zero statement about cyclotomic factors.

## 1. One valid edge

Let `K=2m+1>=7` be an odd prime and let

```text
e={a,b},
0<=a<b<=m,
a,b!=1.                                                    (3)
```

The reciprocal edge relation is

```text
L_e(z)
 =z^a+z^-a+z^b+z^-b-2z-2z^-1.                            (4)
```

It is related to the reduced real-trace edge polynomial by

```text
L_e(z)=-(T-2)w_e(T),
T=z+z^-1.                                                  (5)
```

After collecting equal integer exponents, (4) has at most six nonzero terms.
For `a=0` the two constant terms merge into one coefficient `2`; the invalid
class `1` is absent, so no other collisions with the `+-1` exponents occur.

Every difference between two **distinct collected exponents** in

```text
{a,-a,b,-b,1,-1}                                          (6)
```

has nonzero absolute value strictly less than `K`.  Indeed the largest possible
absolute difference is `2b<=2m=K-1`.

## 2. A torsion root cannot have order divisible by K

### Theorem 1 (prime-conductor coprimality)

Let `alpha` be a root of unity satisfying

```text
L_e(alpha)=0.                                              (7)
```

Then

```text
gcd(ord(alpha),K)=1.                                      (8)
```

### Proof

Write `N=ord(alpha)` and assume for contradiction that `K|N`.

Partition the collected vanishing sum (7) into minimal vanishing subsums.  Let
one such subsum contain `t` terms.  Since the full relation has at most six
collected terms,

```text
2<=t<=6.                                                   (9)
```

Take two distinct terms in that minimal subsum, with integer exponents `r!=s`
from (6).  Their root-of-unity ratio is

```text
alpha^(r-s).                                               (10)
```

Because

```text
0<|r-s|<K                                                  (11)
```

and `K|N`, the order

```text
N/gcd(N,r-s)                                               (12)
```

of (10) is still divisible by `K`.  Hence the reduced exponent of the minimal
subsum is divisible by `K`.

The external minimal-sum theorem says that every prime divisor of that reduced
exponent is at most `t<=6`.  But `K>=7`, a contradiction.

Therefore a minimal subsum cannot contain two distinct collected exponents.
It also cannot contain only one term, because a nonzero rational multiple of a
root of unity is nonzero.  This contradiction proves (8). `□`

The proof uses the **number of collected terms**, not coefficient `l1`-weight;
the coefficients `-2` in (4) are allowed by the external theorem.

## 3. Every torsion real-trace factor evaluates to a unit

Let `G(T) in Z[T]` be any monic polynomial divisor of a valid edge polynomial
`w_e(T)` whose reciprocal lift

```text
G~(z)=z^deg(G)G(z+z^-1)                                   (13)
```

is a product of cyclotomic polynomials.  By Theorem 1 every cyclotomic factor
`Phi_N` occurring in `G~` satisfies

```text
gcd(N,K)=1.                                                (14)
```

The reciprocal lift of the prime-conductor real cyclotomic polynomial is

```text
z^m C_K(z+z^-1)=Phi_K(z).                                  (15)
```

We use the elementary identity, valid whenever `gcd(N,K)=1`:

```text
|Res(Phi_N,Phi_K)|=1.                                     (16)
```

Indeed, if `omega` runs over the primitive `N`-th roots, then
`omega -> omega^K` permutes them and

```text
product_omega Phi_K(omega)
 =product_omega (omega^K-1)/(omega-1)
 =1.                                                       (17)
```

### Theorem 2 (all torsion edge factors are support-free)

For every torsion divisor `G` as above,

```text
|Res_T(C_K,G)|=1.                                         (18)
```

### Proof

Equations (14)--(17) give

```text
|Res_z(Phi_K,G~)|=1.                                      (19)
```

The exact reciprocal-square identity

```text
Res_z(Phi_K,G~)=Res_T(C_K,G)^2                            (20)
```

from `cayley_inverse_reduced_resultant_filter.md` proves (18). `□`

Thus no rational prime can enter the real-conductor support through a torsion
polynomial factor of one edge.

## 4. Consequence for shared edge gcds

Let

```text
G_(e,f)=gcd_Z[T](w_e,w_f).                                (21)
```

Split it in `Q[T]` as

```text
G_(e,f)=G_tor G_nt,                                       (22)
```

where the reciprocal irreducible factors of `G_tor` are cyclotomic and
`G_nt` contains the non-torsion reciprocal factors.

Theorem 2 gives exactly

```text
|Res(C_K,G_tor)|=1.                                       (23)
```

Therefore the first factor in the reduced-resultant filter can have nontrivial
prime support **only** through `G_nt`.

The shared-endpoint theorem already proves

```text
G_nt=1                                                     (24)
```

whenever the two edges share a vertex.  Hence the only unresolved
characteristic-zero gcd sector is

```text
four distinct endpoints.                                 (25)
```

This is the same disjoint-edge sector that can occur simultaneously in one
finite-field inverse matching.

## 5. Relation to the finite audits

The exhaustive `K=31,37,41,43` reduced-resultant regressions found

```text
|Res(C_K,G_(e,f))|=1                                      (26)
```

for every nonconstant pairwise gcd.  The max-index-50 development audit found
only cyclotomic reciprocal factors among all shared irreducible factors.

Those computations remain finite evidence for the stronger statement

```text
G_nt=1 for every disjoint pair.                           (27)
```

Theorem 2 explains why, **conditional only on torsion**, all those observed
factors must be support-free.  It does not promote (27) to a theorem.

## 6. Revised open problem

The characteristic-zero shared-factor problem is now sharply isolated:

```text
Can two disjoint valid inverse edge polynomials share a non-torsion
irreducible factor?                                       (28)
```

If the answer is no, then every polynomial gcd factor can be removed from the
same-embedding arithmetic with unit resultant, and the cross-class support is
controlled entirely by the coprime ordinary resultant `Res(A,B)`.

The sparse unlikely-intersection and Filaseta--Granville--Schinzel reductions
show that any counterexample to (28) must lie in effectively bounded affine
exponent families.  Classifying those families remains open.
