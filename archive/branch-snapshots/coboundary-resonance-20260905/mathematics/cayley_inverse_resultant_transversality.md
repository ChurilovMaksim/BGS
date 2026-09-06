# Transversality of the inverse translated resultant

**Status: EXACT for the directional derivative formula, the squarefree inverse transversality theorem, and the leading-order multi-root formula; FINITE-REGRESSION for generic symbolic and cyclotomic finite-field controls.**

This note refines the two-scalar inverse support from
`cayley_inverse_pair_sum_factorization.md`.

The pair-sum theorem already gives

```text
I_-1(q)>=3
iff
rho(0)=rho'(0)=0,                                       (1)
```

where

```text
rho(Z)=Res_Y(E_Z,O_Z),
F(X+Z/2)=E_Z(X^2)+X O_Z(X^2).                            (2)
```

Here we prove a local formula for `rho'(0)` at a simple common root.  It shows
that the translation direction is automatically transverse to the resultant
hypersurface whenever the inverse gcd has degree exactly one.  Thus the second
scalar is not an accidental detector: its non-vanishing is forced by
squarefreeness of the original trace polynomial.

## 1. A general directional derivative of the resultant

Let `k` be a field, let

```text
f,g,phi,psi in k[Y],                                     (3)
```

and assume that `f` and `g` have exactly one common root `y` in an algebraic
closure, simple in each polynomial.  Write

```text
f=(Y-y)A,
g=(Y-y)B,
gcd(A,B)=1.                                             (4)
```

Assume the perturbations

```text
f_t=f+t phi,
g_t=g+t psi                                             (5)
```

preserve the displayed degrees near `t=0`.

### Theorem 1 (simple-common-root derivative)

With the standard resultant convention

```text
Res(f,g)=lc(f)^deg(g) product_(f(alpha)=0) g(alpha),      (6)
```

one has

```text
d/dt Res(f_t,g_t)|_(t=0)
 =(-1)^(deg(f)-1) Res(A,B)
   [ f'(y) psi(y) - g'(y) phi(y) ].                      (7)
```

In particular the derivative is nonzero exactly when the local Jacobian
bracket in (7) is nonzero.

### Proof

Let `y(t)` be the root of `f_t` with `y(0)=y`.  Since the root is simple,
implicit differentiation gives

```text
y'(0)=-phi(y)/f'(y).                                     (8)
```

Therefore

```text
g_t(y(t))
 =t[psi(y)-g'(y)phi(y)/f'(y)] + O(t^2).                  (9)
```

All other roots of `f_t` converge to roots of `A`, where `g` is nonzero.  The
non-vanishing part of the root product in (6) is

```text
lc(A)^deg(g) product_(A(alpha)=0) g(alpha)
 =Res(A,g)
 =Res(A,Y-y) Res(A,B).                                   (10)
```

Since

```text
Res(A,Y-y)=(-1)^(deg(f)-1) A(y)
           =(-1)^(deg(f)-1) f'(y),                       (11)
```

multiplying (9)--(11) proves (7). `□`

The formula is self-contained; no smoothness theorem for the global resultant
hypersurface is required.

## 2. Specialization to inverse translation

Let

```text
F(X)=E(X^2)+X O(X^2)                                    (12)
```

be the centred inverse-row cofactor.  Translation by `Z/2` gives, to first
order,

```text
E_Z=E+Z phi+O(Z^2),
O_Z=O+Z psi+O(Z^2),                                      (13)
```

with

```text
phi(Y)=(O(Y)+2Y O'(Y))/2,
psi(Y)=E'(Y).                                             (14)
```

Suppose modulo a field of odd characteristic that `E,O` have exactly one
common root `y`.  Then at that root

```text
phi(y)=y O'(y),
psi(y)=E'(y).                                             (15)
```

Theorem 1 therefore gives:

### Corollary 2 (inverse transversality formula)

If `E,O` have exactly one simple common root `y`, then

```text
rho'(0)
 =(-1)^(deg(E)-1)
   Res(E/(Y-y), O/(Y-y))
   [ E'(y)^2 - y O'(y)^2 ].                              (16)
```

The formula is taken in the splitting field of `y`; the right side is fixed by
Galois because the left side lies in the base field.

## 3. The local Jacobian is a product of derivatives of F

Assume `y!=0` and choose `z` with `z^2=y`.  Since `E(y)=O(y)=0`, direct
differentiation of (12) gives

```text
F'(z)= 2z [E'(y)+z O'(y)],
F'(-z)=-2z [E'(y)-z O'(y)].                              (17)
```

Hence

```text
E'(y)^2-y O'(y)^2
 =-F'(z)F'(-z)/(4y).                                     (18)
```

### Theorem 3 (automatic transversality on the squarefree split locus)

Let the characteristic be odd.  Assume

```text
F is squarefree,
F(0)!=0.                                                  (19)
```

If

```text
deg gcd(E,O)=1,
```

then

```text
rho(0)=0,
rho'(0)!=0.                                               (20)
```

If `deg gcd(E,O)>=2`, then

```text
rho(0)=rho'(0)=0.                                        (21)
```

Consequently

```text
deg gcd(E,O)>=2
iff
rho(0)=rho'(0)=0.                                        (22)
```

### Proof

If the gcd has degree one, let `y` be its root.  The condition `F(0)!=0`
forces `y!=0`.  Squarefreeness of `F` gives

```text
F'(z)F'(-z)!=0,
```

so (18) makes the Jacobian bracket in (16) nonzero.  The reduced resultant in
(16) is nonzero because the common root was unique.  Hence `rho'(0)!=0`.

If the gcd has at least two distinct roots, the root-product formula for the
resultant has at least two vanishing factors at `Z=0`; therefore the constant
and linear coefficients of `rho(Z)` both vanish.  The same conclusion follows
from the pair-sum identity `ord_0 rho=deg gcd(E,O)`. `□`

For the maintained inverse row at a split prime `p==1 mod K`, `p!=K`, the
hypotheses (19) are automatic: the valid real-trace cofactor remains squarefree
and its value at the reflection centre is a unit.  Thus (22) is an independent
local proof of the two-scalar support criterion.

## 4. Relation to the first principal subresultant

Under the hypotheses of Corollary 2, the standard first nonzero subresultant is

```text
S_1(E,O;Y)
 =c (Y-y),                                                (23)
```

where, in the standard normalization,

```text
c=+-Res(E/(Y-y),O/(Y-y)).                                (24)
```

Therefore (16) may be read schematically as

```text
rho'(0)
 = principal_subresultant_1(E,O)
   * local_squarefree_Jacobian                            (25)
```

up to the fixed resultant sign.

On the maintained split locus the Jacobian factor is nonzero whenever the gcd
has degree one.  Hence, after imposing `rho(0)=0`, vanishing of `rho'(0)` and
vanishing of the first principal subresultant define the same **prime support**.
Their valuations need not agree.

This links the inverse two-scalar translated-resultant support directly to the
principal-subresultant scalarization in
`cayley_principal_subresultant_support.md`.

## 5. Leading coefficient for several common roots

The preceding calculation extends to the first nonzero derivative when the gcd
has higher degree.

Let

```text
G=gcd(f,g)=product_(j=1)^d (Y-y_j)                       (26)
```

be monic and squarefree, and write

```text
f=G A,
g=G B,
gcd(A,B)=1.                                             (27)
```

Assume every common root is simple in both polynomials.  For the perturbation
`f_t=f+t phi`, `g_t=g+t psi`, define

```text
J_j=f'(y_j) psi(y_j)-g'(y_j) phi(y_j).                   (28)
```

### Theorem 4 (first nonzero resultant coefficient)

The resultant vanishes to order exactly `d` provided all `J_j!=0`, and its
`t^d` coefficient is

```text
[t^d] Res(f_t,g_t)
 =Res(A,G) Res(A,B)
   product_j J_j/f'(y_j).                                (29)
```

Equivalently, up to the convention-dependent sign,

```text
[t^d] Res(f_t,g_t)
 = Res(A,B)/Disc(G) * product_j J_j.                     (30)
```

### Proof

For every common root `y_j`, implicit differentiation gives one vanishing
resultant factor

```text
t J_j/f'(y_j)+O(t^2).                                    (31)
```

All roots coming from `A` contribute the nonzero factor

```text
Res(A,g)=Res(A,G)Res(A,B).                               (32)
```

Multiplication gives (29).  Since

```text
f'(y_j)=G'(y_j)A(y_j)
```

and `Res(A,G)` is, up to sign, `product_j A(y_j)`, cancellation leaves
`product_j G'(y_j)` in the denominator.  For monic squarefree `G` this equals
`Disc(G)` up to the standard sign, proving (30). `□`

For inverse translation, `J_j=E'(y_j)^2-y_jO'(y_j)^2`, so squarefreeness of
`F` makes every local factor nonzero.  Hence the translated half-degree
resultant satisfies the sharper exact identity

```text
ord_(Z=0) rho(Z)=deg gcd(E,O).                           (33)
```

The pair-sum factorization proves the same order statement globally; Theorem 4
explains its local multiplicity mechanism.

## 6. Finite exact controls

`computations/verification/cayley_inverse_resultant_transversality.py` contains
three independent styles of checks.

1. Generic exact integer-polynomial examples verify Theorem 1 against direct
   symbolic differentiation of a resultant.
2. Generic inverse parity examples verify (16) exactly.
3. Cyclotomic finite-field examples realize the three possible first-order
   cases:

```text
K=11, p=23, tau=14 (embedding 1): deg gcd(E,O)=0, rho(0)!=0,
K=11, p=23, tau=10 (embedding 2): deg gcd(E,O)=1, rho(0)=0, rho'(0)!=0,
K=23, p=47, tau=10 (embedding 1): deg gcd(E,O)=2, rho(0)=rho'(0)=0.  (34)
```

The earlier K=7,p=29 positive anchor was false: all three real embeddings
give degree zero. It is retained as a negative control; the degree-one
case uses the explicitly specified second embedding of K=11,p=23.
The regression also compares a direct reflected trace set with the gcd.
The finite checks are regression only; the universal statements are proved
above.

## 7. Arithmetic implication and limitation

The exact inverse support can now be seen as a transversality failure:

```text
rho(0)=0
```

means one inverse pair collision, while

```text
rho'(0)=0
```

means that the translation direction is tangent to the resultant divisor;
on the squarefree split locus this happens exactly when a second common root is
present.

This interpretation does **not** yet bound the largest rational split prime in
the common divisor of `rho(0),rho'(0)`.  Its value is structural: it identifies
the second scalar with a reduced resultant / principal-subresultant factor
multiplied by a local squarefree Jacobian.  A future Bezout or norm argument can
therefore target the common arithmetic of the reduced resultant and the
translation Jacobian rather than treat `rho'(0)` as an opaque determinant.