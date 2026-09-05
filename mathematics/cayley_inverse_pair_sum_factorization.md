# Inverse-row pair-sum factorization and two-scalar support

**Status: EXACT for the universal pair-sum factorization, inverse-row zero-order identity, two-scalar split support criterion, translated half-degree resultant identity, and the relation to the even/odd resultant; FINITE-REGRESSION for the SymPy/Smith anchors; OPEN for a polynomial bound on the largest supported split prime.**

This note strengthens `cayley_product_row_reflection.md` and specializes the
scalar shift-resultant framework from `cayley_trace_intercept_rigidity.md`.

The inverse shift resultant is a diagonal factor times a perfect square.  The
square root is itself a translated resultant of the two half-degree parity
components.  Thus the inverse order-three event is detected by only **two
scalar algebraic integers**, computable without materializing the full
degree-`m^2` shift resultant.

## 1. Setup

Let `K=2m+1>=7` be an odd prime,

```text
tau=zeta+zeta^(-1),
H_K(T)=(T-2)C_K(T),
P(T)=H_K(T)/(T-tau),
O^+=Z[tau].
```

For the normalized inverse ratio `r=-1`,

```text
alpha=-1,
beta=2tau.
```

Shift the source cofactor to the reflection centre:

```text
F(X)=P(tau+X) in O^+[X].                                 (1)
```

Then `F` is monic of degree `m`.  The inverse scalar shift resultant is

```text
R_-(Z)=Res_X(F(X),F(Z-X)).                               (2)
```

By the general shift-resultant theorem,

```text
ord_(Z=0)(R_-(Z) mod q)=I_-1(q)                         (3)
```

for every split embedding prime `q|p`.

## 2. Universal pair-sum square factorization

The following identity is independent of cyclotomic structure.

### Theorem 1 (pair-sum factorization)

Let `R` be an integral domain and let

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

Since `F` is monic,

```text
Res_X(F(X),F(Z-X))
 =prod_i F(Z-x_i)
 =prod_(i,j)(Z-x_i-x_j).                                 (7)
```

The diagonal ordered pairs give `prod_i(Z-2x_i)`, while each unordered pair
`i<j` occurs twice.  This proves (6).  The coefficients of `S_F` are symmetric
polynomials with integer coefficients in the roots, hence lie in `R`. `□`

The roots of `S_F` are the unordered pair sums.  Equivalently, `S_F` is the
characteristic polynomial of the second additive compound of a companion
matrix for `F`.

## 3. Exact inverse-row halving from the square factor

Write

```text
D(Z)=2^m F(Z/2),
S(Z)=S_F(Z)=s_0+s_1 Z+s_2 Z^2+....                      (8)
```

For a split prime `p==1 mod K`, `p!=K`, the trace polynomial stays squarefree.
Thus

```text
F(0)=P(tau)=H_K'(tau)
```

is nonzero modulo every embedding prime `q|p`; since `p` is odd,
`D(0)=2^mF(0)` is a unit.

### Theorem 2 (pair-sum zero-order identity)

For every split embedding prime `q|p`,

```text
I_-1(q)=2 ord_(Z=0)(S(Z) mod q).                         (9)
```

Consequently

```text
I_-1(q) is even,
I_-1(q)>=3
iff I_-1(q)>=4
iff s_0==s_1==0 mod q.                                  (10)
```

### Proof

Combine (3) and (6).  The factor `D(0)` is a unit, so the order of zero of
`R_-` is twice the order of zero of `S`.  Zero order at least two is equivalent
to vanishing of the constant and linear coefficients. `□`

This both re-proves inverse-row evenness and gives a smaller support detector.

## 4. Two-scalar exact split support

Define

```text
J^pair_K=(s_0,s_1) subset O^+,
J^pair_K intersect Z = Theta_K Z,
Theta_K>0.                                                (11)
```

### Corollary 3 (two-scalar support integer)

For every split rational prime `p==1 mod K`,

```text
p|Theta_K
iff
some inverse-ratio row pair has at least three common parameters. (12)
```

Therefore `Theta_K`, the reflection support `Xi_K`, the inverse factor of the
real-trace support `Lambda_(K,-1)^(3)`, and the inverse scalar shift support all
have the same **split rational-prime support**.

No equality of the full integers or of their valuations is claimed.

## 5. Constant coefficient and the reflection resultant

Decompose

```text
F(X)=E(X^2)+X O(X^2).                                    (13)
```

If `m` is even, `E` is monic of degree `m/2`; if `m` is odd, `O` is monic of
degree `(m-1)/2`.  This fixed unit-leading component is the specialization
safeguard already used in the reflection note.

### Theorem 4 (constant pair-sum coefficient)

In `O^+`,

```text
s_0^2=Res_Y(E(Y),O(Y))^2,                                (14)
s_0=+-Res_Y(E,O),                                        (15)
```

and

```text
R_-(0)=2^m E(0) Res_Y(E,O)^2.                            (16)
```

### Proof

Let `x_i` be the roots of `F`.  At a root,

```text
F(-x_i)-F(x_i)=-2x_i O(x_i^2),
```

hence

```text
R_-(0)
 =prod_i F(-x_i)
 =(-2)^m prod_i x_i prod_i O(x_i^2).                    (17)
```

Since `F` is monic with constant term `E(0)`,

```text
prod_i x_i=(-1)^mE(0).                                   (18)
```

Also

```text
prod_i O(x_i^2)=Res_X(F(X),O(X^2)).                      (19)
```

If `m` is even, the monic component `E` has degree `m/2`; if `m` is odd,
`O` is monic.  Applying the root-product formula to the roots `+-sqrt(y)` of
`O(X^2)` gives in both parity cases

```text
Res_X(F,O(X^2))=Res_Y(E,O)^2.                            (20)
```

Equations (17)--(20) give (16).  On the other hand Theorem 1 gives

```text
R_-(0)=D(0)s_0^2=2^mE(0)s_0^2.                          (21)
```

The coefficient ring is a domain and `E(0)!=0`, so (14)--(15) follow. `□`

Thus the old reflection resultant is exactly, up to sign, the constant
coefficient of the pair-sum square root.  The genuinely new order-three datum
is one more scalar, `s_1`.

## 6. The entire pair-sum polynomial is a translated half-degree resultant

The previous theorem extends from `Z=0` to the whole polynomial.

Introduce an indeterminate `Z` and translate by half the target pair sum:

```text
F_Z(X)=F(X+Z/2)
      =E_Z(X^2)+X O_Z(X^2)                               (22)
```

in `L^+[Z,1/2][X]`.  The roots of `F_Z` are

```text
y_i=x_i-Z/2.
```

### Theorem 5 (translated parity-resultant identity)

There is a sign `eps_m in {+1,-1}`, depending only on the resultant convention
and `m`, such that

```text
S_F(Z)=eps_m Res_Y(E_Z(Y),O_Z(Y)).                       (23)
```

In particular the right-hand side, although written after adjoining `1/2`, is
actually the integral polynomial `S_F(Z) in O^+[Z]` up to sign.

### Proof

Apply Theorem 4 to the monic polynomial `F_Z` over the coefficient field
`L^+(Z)`.  Its pair-sum polynomial at zero is

```text
prod_(i<j)(-y_i-y_j)
 =prod_(i<j)(Z-x_i-x_j)
 =S_F(Z).                                                 (24)
```

Theorem 4 identifies the square of this quantity with the square of
`Res(E_Z,O_Z)`.  Both sides are nonzero polynomials and the coefficient ring is
a domain, so they differ by a sign.  Monicity fixes that sign once `m` and the
resultant convention are fixed. `□`

Hence

```text
s_0=eps_m Res(E,O),                                      (25)
s_1=eps_m d/dZ Res(E_Z,O_Z)|_(Z=0).                     (26)
```

The first-order translation is especially simple.  Differentiating
`F(X+Z/2)` at `Z=0` gives

```text
dE_Z/dZ|_0 = (O(Y)+2Y O'(Y))/2,                         (27)
dO_Z/dZ|_0 = E'(Y).                                      (28)
```

Therefore the inverse order-three event is equivalently simultaneous
vanishing of a half-degree resultant and its **translation derivative**.

## 7. A much smaller exact computation

Let

```text
rho(Z)=Res_Y(E_Z,O_Z).
```

For split odd primes, factors of two are units and Theorem 5 gives

```text
I_-1(q)>=3
iff
rho(0)==rho'(0)==0 mod q.                                (29)
```

This suggests a substantially cheaper exact implementation than either the
full shift resultant or the additive-compound matrix:

1. work only to first order in a dual parameter `eps`, `eps^2=0`;
2. use

```text
E_eps=E + eps*(O+2Y O')/2,
O_eps=O + eps*E';                                        (30)
```

3. compute the fixed-degree Sylvester determinant

```text
Res_Y(E_eps,O_eps)=rho_0+eps rho_1;                       (31)
```

4. contract the two algebraic integers `rho_0,rho_1` to `Z`.

The Sylvester matrix has dimension only `deg E+deg O=O(K)`.  A fraction-free
implementation over `Z[tau]` can compute both scalars in one determinant over
dual numbers.  This is preferable to materializing the degree-`m^2` polynomial
`R_-(Z)` or even the `binom(m,2)` additive compound when only order-three
support is needed.

## 8. Exact norm structure of the unsquared constant term

For reference,

```text
F(0)=P(tau)=H_K'(tau)=(tau-2)C_K'(tau).                  (32)
```

For prime `K`,

```text
|Disc(C_K)|=K^(m-1),
|N(tau-2)|=K,
```

so

```text
|N_(L^+/Q)(F(0))|=K^m.                                  (33)
```

Taking norms in (16),

```text
|N(R_-(0))|
 =2^(m^2) K^m |N(Res(E,O))|^2.                          (34)
```

Every rational prime away from `2K` therefore occurs with even valuation in
the norm of the unsquared inverse shift constant.  This explains part of the
square pattern seen in finite data, but does **not** imply equality of
`Lambda`, `Xi`, `Theta`, or their valuations.

## 9. Finite exact regressions

`computations/verification/cayley_inverse_pair_sum_factorization.py` checks two
mechanisms:

- small full-resultant anchors divide `R_-` by `D`, recover the integral monic
  square root `S`, and verify Theorems 1 and 4 exactly;
- the cheaper translated parity-resultant computes `rho(0),rho'(0)` directly
  and contracts their two-scalar ideal by Smith normal form.

Observed two-scalar contractions are

```text
K= 7: Theta=7,                    Theta'=1,
K=11: Theta=11^2,                 Theta'=1,
K=13: Theta=5*13^3,               Theta'=5,
K=17: Theta=17^4,                 Theta'=1,
K=19: Theta=37*19^4,              Theta'=37,
K=23: Theta=23^6*47^2*137,        Theta'=47^2*137.       (35)
```

For comparison,

```text
Xi'_13=5,
Xi'_19=37,
Xi'_23=47*137,                                      (36)
```

so the split rational-prime support agrees while valuations need not.  At
`K=13`, the full real-trace inverse factor has

```text
Lambda'_(13,-1)^(3)=5^2.                                (37)
```

These data are consistent with the square-factor mechanism, but no general
integer equality is promoted.

The old full shift-resultant route already becomes materially slow around
`K=17`.  The translated half-degree calculation reaches `K=23` in seconds in
the same SymPy environment; larger Smith contractions, rather than the
half-degree resultant itself, become the next computational bottleneck.

## 10. Remaining inverse-row target

The exact inverse support can now be written in four compatible ways:

```text
deg gcd(E,O)>=2,
ord_0 S>=2,
q|(s_0,s_1),
rho(0)=rho'(0)=0 mod q.                                 (38)
```

A sufficient pointwise theorem remains, for example,

```text
P_split^+(Theta'_K)<=K^(4+o(1)).                         (39)
```

The translated resultant formulation makes the next high-value arithmetic
question very concrete: derive a Bezout or norm identity coupling
`rho(0)=Res(E,O)` to its translation derivative `rho'(0)` strongly enough to
control their **common** split prime divisors.  A height bound for either scalar
alone is not enough.