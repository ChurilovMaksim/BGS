# Inverse-row pair-sum factorization and two-scalar support

**Status: EXACT for the universal pair-sum factorization, inverse-row zero-order identity, two-scalar split support criterion, and the relation to the even/odd resultant; FINITE-REGRESSION for the SymPy/Smith anchors; OPEN for a polynomial bound on the largest supported split prime.**

This note strengthens the inverse-row reflection analysis in
`cayley_product_row_reflection.md` and specializes the scalar shift-resultant
framework from `cayley_trace_intercept_rigidity.md`.

The key point is that the inverse shift resultant is not merely a generic
resultant with an even order of vanishing. It is a **diagonal factor times a
perfect square**. Therefore the order-three event is detected by only two
scalar algebraic integers.

## 1. Setup

Let `K=2m+1>=7` be an odd prime,

```text
tau=zeta+zeta^(-1),
H_K(T)=(T-2)C_K(T),
P(T)=H_K(T)/(T-tau).
```

For the normalized inverse ratio `r=-1`, the affine trace map is

```text
alpha=-1,
beta=2tau.
```

Shift the source cofactor to the reflection centre:

```text
F(X)=P(tau+X) in O^+[X],
O^+=Z[tau].                                               (1)
```

Then `F` is monic of degree `m` and

```text
P(2tau-T)=F(-X)  when T=tau+X.
```

The inverse scalar shift resultant is

```text
R_-(Z)
 =Res_X(F(X),F(Z-X)).                                    (2)
```

By the general shift-resultant theorem,

```text
ord_(Z=0)(R_-(Z) mod q)=I_-1(q)                         (3)
```

for every split embedding prime `q|p`.

## 2. Universal pair-sum factorization

The following identity does not use cyclotomic structure.

### Theorem 1 (pair-sum square factorization)

Let `R` be an integral domain of characteristic zero and let

```text
F(X)=prod_(i=1)^m (X-x_i)
```

be monic over a splitting extension. Define

```text
D_F(Z)=prod_i (Z-2x_i)=2^m F(Z/2),                       (4)
S_F(Z)=prod_(i<j)(Z-x_i-x_j).                            (5)
```

Then `D_F,S_F` lie in `R[Z]`, `S_F` is monic of degree `binom(m,2)`, and

```text
Res_X(F(X),F(Z-X))=D_F(Z) S_F(Z)^2.                      (6)
```

### Proof

Because `F` is monic, the root-product formula gives

```text
Res_X(F(X),F(Z-X))
 =prod_i F(Z-x_i)
 =prod_(i,j)(Z-x_i-x_j).                                 (7)
```

Separate diagonal ordered pairs `i=j` from the two ordered copies of every
unordered pair `i<j`:

```text
prod_(i,j)(Z-x_i-x_j)
 =prod_i(Z-2x_i) prod_(i<j)(Z-x_i-x_j)^2.                (8)
```

The diagonal product is `2^m F(Z/2)`. The coefficients of `S_F` are symmetric
polynomials with integer coefficients in the roots, so the fundamental theorem
of symmetric polynomials puts them in the coefficient ring `R`. `□`

The polynomial `S_F` is the characteristic polynomial of the second additive
compound of any companion matrix for `F`: its roots are precisely the unordered
pair sums `x_i+x_j`. This gives a scalable route for computing its low
coefficients without materializing the degree-`m^2` resultant.

## 3. Exact inverse-row halving from the square factor

Specialize Theorem 1 to the cyclotomic `F` in (1). Put

```text
D(Z)=2^m F(Z/2),
S(Z)=S_F(Z)=s_0+s_1 Z+s_2 Z^2+....                      (9)
```

For a split prime `p==1 mod K`, `p!=K`, the trace polynomial remains squarefree.
Hence

```text
F(0)=P(tau)=H_K'(tau)
```

is nonzero modulo every embedding prime `q|p`. Since `p` is odd,

```text
D(0)=2^m F(0)
```

is a `q`-adic unit.

### Theorem 2 (pair-sum zero-order identity)

For every split embedding prime `q|p`,

```text
I_-1(q)=2 ord_(Z=0)(S(Z) mod q).                         (10)
```

Consequently

```text
I_-1(q) is even,                                         (11)
I_-1(q)>=3
iff I_-1(q)>=4
iff s_0==s_1==0 mod q.                                  (12)
```

### Proof

Combine (3) with the factorization

```text
R_-(Z)=D(Z)S(Z)^2.
```

The factor `D(0)` is a unit, so the zero order of the right-hand side is twice
the zero order of `S`. A polynomial has zero order at least two exactly when
its constant and linear coefficients vanish. `□`

This is a second proof of the evenness theorem from the reflection note, but it
also produces a smaller exact support detector.

## 4. Two-scalar exact split support

Define

```text
J^pair_K=(s_0,s_1) subset O^+,
J^pair_K intersect Z = Theta_K Z,
Theta_K>0.                                                (13)
```

### Corollary 3 (two-scalar support integer)

For every split rational prime `p==1 mod K`,

```text
p|Theta_K
iff
some inverse-ratio row pair has at least three common parameters. (14)
```

Thus `Theta_K`, the reflection support `Xi_K`, the inverse-ratio real-trace
support `Lambda_(K,-1)^(3)`, and the inverse scalar shift support all have the
same **split rational-prime support**.

No equality of the full integers or of their valuations is asserted.

This is the smallest current exact inverse-row support formulation: two scalar
algebraic integers instead of two subresultant polynomials or three scalar
coefficients of the unsquared shift resultant.

## 5. Relation to the even/odd reflection resultant

Write, as in the reflection note,

```text
F(X)=E(X^2)+X O(X^2).                                    (15)
```

One parity component has unit leading coefficient:

- if `m` is even, `E` is monic of degree `m/2`;
- if `m` is odd, `O` is monic of degree `(m-1)/2`.

### Theorem 4 (constant pair-sum coefficient)

In `O^+`,

```text
s_0^2=Res_Y(E(Y),O(Y))^2.                                (16)
```

Equivalently,

```text
s_0=+-Res_Y(E,O).                                        (17)
```

Moreover

```text
R_-(0)=2^m E(0) Res_Y(E,O)^2.                            (18)
```

### Proof

Let `x_i` be the roots of `F`. At a root `x_i`,

```text
F(-x_i)-F(x_i)=-2x_i O(x_i^2),
```

so, because `F(x_i)=0`,

```text
R_-(0)
 =prod_i F(-x_i)
 =(-2)^m prod_i x_i prod_i O(x_i^2).                    (19)
```

Since `F` is monic with constant term `E(0)`,

```text
prod_i x_i=(-1)^m E(0).                                  (20)
```

It remains to evaluate `prod_i O(x_i^2)`. The same quantity is

```text
Res_X(F(X),O(X^2)).                                      (21)
```

If `m` is even, `E` is monic of degree `m/2`; if `m` is odd, `O` is monic.
Applying the root-product formula to the roots `+-sqrt(y)` of `O(X^2)` gives in
both parity cases

```text
Res_X(F,O(X^2))=Res_Y(E,O)^2.                            (22)
```

Substitution into (19)--(20) proves (18).

On the other hand Theorem 1 at `Z=0` gives

```text
R_-(0)=D(0)s_0^2=2^mE(0)s_0^2.                          (23)
```

The coefficient ring is an integral domain and `E(0)!=0`, so comparison with
(18) gives (16), hence (17). `□`

Thus the constant coefficient of the square-root pair-sum polynomial is,
up to sign, exactly the ordinary reflection resultant already implicit in the
`E/O` formulation. The genuinely new datum for order three is the single
additional scalar `s_1`.

## 6. Exact norm structure of the unsquared constant term

For reference,

```text
F(0)=P(tau)=H_K'(tau)=(tau-2)C_K'(tau).                  (24)
```

For prime `K`, the maximal-real cyclotomic discriminant is

```text
|Disc(C_K)|=K^(m-1),
```

and `|N(tau-2)|=K`. Hence

```text
|N_(L^+/Q)(F(0))|=K^m.                                  (25)
```

Taking norms in (18) gives the exact shape

```text
|N(R_-(0))|
 =2^(m^2) K^m |N(Res(E,O))|^2.                          (26)
```

In particular every rational prime away from `2K` occurs with even valuation
in the norm of the inverse unsquared constant shift coefficient. This explains
a substantial part of the square patterns seen in finite data, but it does
**not** prove equality between `Lambda`, `Xi`, `Theta`, or their valuations.

## 7. Finite exact regressions

`computations/verification/cayley_inverse_pair_sum_factorization.py` constructs
the full inverse shift resultant at small `K`, divides out the diagonal factor,
recovers the monic square root `S` exactly in `Z[tau][Z]`, verifies (6), (16),
and contracts `(s_0,s_1)` by Smith normal form.

Observed anchors are

```text
K= 7: Theta=7,       Theta'=1,
K=11: Theta=11^2,    Theta'=1,
K=13: Theta=5*13^3,  Theta'=5,
K=17: Theta=17^4,    Theta'=1.                           (27)
```

Here `Theta'` denotes the prime-to-`2K` part. The `K=17` full-resultant reference
run is materially slower and is therefore an optional extended regression, not
a default CI gate.

For `K=13`,

```text
Theta'_13=Xi'_13=5,
Lambda'_(13,-1)^(3)=5^2.                                (28)
```

This is consistent with the square-factor mechanism but is not promoted to a
general integer equality.

## 8. Computational consequence: use the additive compound

The full shift resultant has degree `m^2`, while `S` has degree

```text
binom(m,2).
```

More importantly, order-three support needs only `s_0,s_1`. If `C_F` is a
companion matrix of `F`, the second additive compound `C_F^[2]` has eigenvalues
`x_i+x_j`, `i<j`, and therefore

```text
S(Z)=det(Z I-C_F^[2]).                                   (29)
```

A scalable implementation should compute only

```text
s_0=(-1)^N det(C_F^[2]),
s_1=coefficient of Z in det(ZI-C_F^[2]),                 (30)
```

with `N=binom(m,2)`, using fraction-free exact linear algebra in
`O^+=Z[tau]`. This avoids the degree-`m^2` symbolic resultant and its subsequent
perfect-square extraction.

## 9. Remaining inverse-row target

The exact inverse-row closure condition can now be written as a simultaneous
two-scalar divisibility problem:

```text
q | s_0,
q | s_1.                                                 (31)
```

A sufficient pointwise theorem remains, for example,

```text
P_split^+(Theta'_K)<=K^(4+o(1)).                         (32)
```

The factorization (6), the relation `s_0=+-Res(E,O)`, the half-degree reflection
formulation, and the additive-compound representation give four compatible
exact views of the same inverse support. None currently supplies a polynomial
largest-prime bound.

The next high-value test is to derive a closed or low-height formula for `s_1`
(or a Bezout identity coupling `s_0` and `s_1`) and determine whether their
common ideal has substantially smaller norm/support than either scalar alone.