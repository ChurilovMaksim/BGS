# Shift-resultant / principal-subresultant transversality

**Status: EXACT + EXTERNAL-THEOREM for the field-level identity and its split-row specialization; FINITE-REGRESSION for symbolic and finite-field controls.**

This note unifies two exact scalarizations of the product-row intersection
problem:

- the low coefficients of the scalar shift resultant from
  `cayley_trace_intercept_rigidity.md`;
- the principal subresultant coefficients from
  `cayley_principal_subresultant_support.md`.

The relation is local and geometric. At a point where the two fixed-degree row
polynomials have gcd degree exactly `d`, the first nonzero shift coefficient and
the first nonzero principal subresultant differ by an explicit factor that is a
unit on the maintained squarefree split locus.

## 1. Field-level setup

Let `k` be a field and let `f,g in k[T]` be monic polynomials of the same degree
`n`. Assume

```text
G=gcd(f,g)
```

is monic, squarefree and has degree `d`. Write

```text
f=G A,
g=G B,
gcd(A,B)=1.                                           (1)
```

Let

```text
g_Z(T)=g(T)+Z psi(T)+O(Z^2)                              (2)
```

be a degree-preserving deformation over `k[[Z]]`. Define

```text
R(Z)=Res_T(f(T),g_Z(T)).                                  (3)
```

Assume

```text
psi(y)!=0                                                 (4)
```

for every root `y` of `G` in an algebraic closure.

The standard subresultant theorem gives

```text
S_0=...=S_(d-1)=0,
S_d=u Res(A,B) G                                         (5)
```

for a convention-dependent unit/sign `u` when `f,g,G` are monic. Hence

```text
psc_d(f,g)=u Res(A,B).                                    (6)
```

Only the nonzero unit convention in (6) is relevant below.

## 2. First nonzero shift coefficient

The multi-root directional resultant formula from
`cayley_inverse_resultant_transversality.md` applies with `phi=0`. For each
common root `y`,

```text
J_y=f'(y) psi(y).                                         (7)
```

### Theorem 1 (shift/PSC leading coefficient identity)

Under the hypotheses above,

```text
ord_(Z=0) R(Z)=d,                                         (8)
```

and, up to the fixed subresultant/resultant sign convention,

```text
[Z^d]R(Z)
 = psc_d(f,g)
   Res(A,G)
   product_(G(y)=0) psi(y).                              (9)
```

Equivalently,

```text
[Z^d]R(Z) / psc_d(f,g)                                   (10)
```

is a nonzero scalar whenever `f` is squarefree and (4) holds.

### Proof

The general multi-root coefficient formula gives

```text
[Z^d]R(Z)
 =Res(A,G) Res(A,B)
  product_y J_y/f'(y).                                   (11)
```

Substitute `J_y=f'(y)psi(y)` and use (6). The hypotheses make every factor in
(9) nonzero, so the zero order is exactly `d`. `□`

This is a field-level identity. It makes no number-theoretic claim about the
size of the nonzero multiplier in characteristic zero.

## 3. Specialization to the product-row shift

For an odd prime `K=2m+1`, use the specialization-safe maximal-real row
cofactors

```text
P(T), Q(T) in O^+[T],
O^+=Z[tau].                                               (12)
```

For normalized ratio `r`, write the target cofactor in its natural target
coordinate as a monic polynomial `R_r(U)`. The row shift is

```text
Q_Z(T)=R_r(alpha_r T+beta_r+Z).                          (13)
```

Its leading coefficient in `T` is the `Z`-independent unit `alpha_r^m` at every
split prime away from `K`. Normalize

```text
q_Z(T)=alpha_r^(-m) Q_Z(T)                               (14)
```

so that `q_0` is monic. Then

```text
psi(T)=d/dZ q_Z(T)|_0
      =alpha_r^(-m) R_r'(alpha_r T+beta_r).              (15)
```

At a common root `y` of `P` and `q_0`,

```text
q_0'(y)=alpha_r psi(y).                                  (16)
```

For every maintained split embedding prime:

- `alpha_r` is nonzero;
- the valid target cofactor is squarefree;
- therefore `q_0'(y)!=0` and hence `psi(y)!=0`.

### Corollary 2 (row-stratum transversality)

Let a split embedding prime `q` satisfy

```text
d=I_(1,r)(q)=deg gcd(P,q_0 mod q).                       (17)
```

Then

```text
ord_(Z=0) Res(P,q_Z)=d,                                  (18)
```

and the first nonzero shift coefficient satisfies

```text
c_d
 = unit_q * psc_d(P,q_0)                                (19)
```

in the residue field, where `unit_q` is explicitly

```text
unit_q
 =+-Res(A,G) product_(G(y)=0) psi(y) !=0.                (20)
```

Thus the shift-resultant and principal-subresultant coordinates are transverse
coordinate systems on the same fixed-degree gcd stratum.

This gives a mechanism-level explanation for the exact support equality
between `Omega` and `Pi`; it is stronger than merely observing that both
criteria encode the same gcd degree.

## 4. Consequences for the first strata

At a split embedding prime:

### gcd degree zero

```text
psc_0!=0,
c_0!=0.                                                   (21)
```

### gcd degree one

```text
psc_0=c_0=0,
psc_1!=0,
c_1!=0,

c_1=unit_q*psc_1.                                         (22)
```

### gcd degree two

```text
psc_0=psc_1=c_0=c_1=0,
psc_2!=0,
c_2!=0,

c_2=unit_q*psc_2.                                         (23)
```

### gcd degree at least three

```text
psc_0=psc_1=psc_2=0,
c_0=c_1=c_2=0.                                            (24)
```

Hence the order-three event is the common zero locus of either triple, and the
first nonzero coordinate immediately after each lower stratum differs only by
a residue-field unit.

## 5. Relation to the inverse transversality theorem

For `r=-1`, reflection changes variables to

```text
F(X)=E(X^2)+X O(X^2),
rho(Z)=Res(E_Z,O_Z).                                      (25)
```

The inverse note proves the more explicit degree-one formula

```text
rho'(0)
 =+-Res(E/(Y-y),O/(Y-y))
   [E'(y)^2-yO'(y)^2].                                   (26)
```

This is exactly Theorem 1 with the local shift multiplier evaluated in closed
form. The squarefree Jacobian

```text
E'(y)^2-yO'(y)^2=-F'(z)F'(-z)/(4y)                       (27)
```

is the inverse specialization of the general nonzero unit in (20).

## 6. Finite regression

`computations/verification/cayley_shift_psc_transversality.py` checks two
independent mechanisms.

1. Generic exact monic integer-polynomial examples with gcd degree `1` and `2`
   verify the coefficient identity (9) against a directly expanded resultant.
2. Split cyclotomic row examples compare gcd degree, the first nonzero shift
   coefficient and the first nonzero PSC modulo the split prime.

Maintained finite controls include strata of degrees `0`, `1`, `2` and `>=3`.
The finite checks are not the proof of Theorem 1.

## 7. Arithmetic limitation and next target

Equation (19) is a **residue-field unit relation at the first nonzero stratum**.
It does not imply equality of the integral contractions `Pi` and `Omega`, and
finite anchors already disprove such equality of valuations.

The order-three arithmetic problem remains simultaneous divisibility of the
three lower coordinates. The value of the theorem is structural: it shows that
`Pi` and `Omega` are two transverse coordinate systems for one determinantal
stratification, so future common-divisor work should be phrased intrinsically in
terms of the Sylvester/Fitting module rather than treating the two triples as
unrelated integers.

A high-value next step is to exploit identities among consecutive principal
Sylvester minors (Desnanot--Jacobi / subresultant PRS / Bezoutian identities) to
control the common split prime divisors of

```text
psc_0, psc_1, psc_2.                                     (28)
```

Bounding any one of their norms separately cannot close the largest-prime
target.