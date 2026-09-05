# Canonical coefficient ideal for higher product-row intersections

**Status: EXACT for the ideal-contraction reduction and Chebyshev/sparse-row identities; EXACT + EXTERNAL-THEOREM for the standard subresultant criterion; FINITE-REGRESSION for the explicit Smith-normal-form anchors; OPEN for growing-`K` control of the resulting split-prime support.**

This note sharpens `cayley_product_row_subresultants.md`.  The integer obtained there by taking a gcd of **individual coefficient norms** is sufficient but arithmetically wasteful: different prime ideals above the same rational prime can divide different coefficients.  A genuine row intersection modulo one chosen reduction `zeta -> h` forces **one and the same prime ideal** to contain every relevant subresultant coefficient.  The correct obstruction is therefore the coefficient ideal itself and its contraction to `Z`.

The refinement keeps the exact pointwise quadratic-energy corollary but replaces the open divisor problem by a strictly smaller canonical integer.

## 1. Setup and the order-three coefficient ideal

Let `K` be an odd prime,

```text
L=Q(zeta),
O_L=Z[zeta],
zeta=exp(2 pi i/K),
m=(K-1)/2.
```

For the homogeneous product-row forms `R_i(U,V)` and a Galois-normalized distinct row pair `(1,r)`, use the notation of `cayley_product_row_subresultants.md`.  Let

```text
S_0^(r), S_1^(r), S_2^(r)
```

be the first three fixed-degree homogeneous subresultants (equivalently, the corresponding determinantal subresultant coefficient arrays).  Let `C_(K,r)^(3)` be the finite set of all their nonzero coefficients in `O_L` and define the nonzero ideal

```text
J_(K,r)^(3)=( C_(K,r)^(3) ) subset O_L.                 (1)
```

The characteristic-zero resultant is nonzero, so `J_(K,r)^(3)` is a nonzero ideal.  Hence `O_L/J_(K,r)^(3)` is finite and

```text
J_(K,r)^(3) intersect Z = D_(K,r)^(3) Z                 (2)
```

for a unique positive integer `D_(K,r)^(3)`.

Equivalently,

```text
D_(K,r)^(3)=exp_additive(O_L/J_(K,r)^(3)),               (3)
```

the exponent of the finite additive group.  Indeed `n in J intersect Z` iff multiplication by `n` annihilates every class of `O_L/J`.

For split-prime applications remove the irrelevant factors `2` and `K`:

```text
D'_(K,r)^(3)=D_(K,r)^(3) with all factors 2 and K removed,
D'_K^(3)=product_[r] D'_(K,r)^(3),                       (4)
```

where `[r]` runs through the unordered ratio classes `r~r^(-1)`.

## 2. Exact rational-prime support of the rank-drop ideal

### Lemma 1 (contraction support)

For every rational prime `p`,

```text
p | D_(K,r)^(3)
iff
there exists a prime ideal P of O_L above p with
J_(K,r)^(3) subset P.                                    (5)
```

### Proof

If `J subset P`, then the positive generator `D` of `J intersect Z` lies in `P intersect Z=(p)`, hence `p|D`.

Conversely assume `p|D`.  By (3), the finite ring `A=O_L/J` has additive exponent divisible by `p`.  Therefore the class of the integer `p` cannot be a unit of `A`: if it were a unit, multiplication by `p` would be an automorphism of the finite additive group and the group would have no `p`-primary part.  Thus `pA` is proper and is contained in a maximal ideal of `A`.  Its inverse image is a prime ideal `P` of `O_L` containing both `J` and `p`, so `P|p`.

This proves (5).

### Theorem 2 (exact order-three rank-drop support)

For every rational prime `p`,

```text
p | D_(K,r)^(3)                                          (6)
```

if and only if there exists a prime ideal `P|p` for which the reductions of the two fixed-degree homogeneous row forms `R_1,R_r` have gcd degree at least three over `O_L/P`.

### Proof

For two fixed-degree binary forms over a field, the classical subresultant theorem says

```text
deg gcd(R_1,R_r)>=3
iff
S_0=S_1=S_2=0.                                           (7)
```

Using homogeneous determinantal subresultants makes (7) insensitive to a common projective root at infinity or to degree drop after dehomogenization.  Thus (7) modulo `P` is equivalent to every coefficient in `C_(K,r)^(3)` belonging to `P`, i.e. `J_(K,r)^(3) subset P`.  Lemma 1 gives the claimed rational-prime equivalence.

The external algebraic input is the standard subresultant criterion, for example W. S. Brown and J. F. Traub, *On Euclid's Algorithm and the Theory of Subresultants*, Journal of the ACM 18 (1971), 505--514, DOI `10.1145/321662.321665`.  The citation and DOI were independently audited; no retraction flag was found.

## 3. Consequence for finite-field row intersections

Let `p==1 mod K` and choose a prime ideal `P|p`, equivalently a reduction

```text
zeta -> h in F_p^*,  ord(h)=K.
```

If two distinct product rows have at least three common finite Cayley parameters, then the reduced homogeneous row forms have at least three distinct common projective roots.  Their gcd therefore has degree at least three, so Theorem 2 gives

```text
I_(i,j)(p)>=3  ==>  p | D'_(K,r)^(3),                    (8)
```

with `r=j/i` up to inversion.

Consequently, if

```text
p does not divide D'_K^(3),                              (9)
```

then every row pair has at most two common parameters.  The exact cross-row energy identity from `cayley_product_row_intersections.md` yields

```text
I_K(p)<=2,
Delta_K(p)<=8(K-1)(K-2),                                 (10)
```

and hence

```text
E_+(c(H\{1}))<=11(K-1)(K-2).                            (11)
```

Thus the desired pointwise quadratic collision scale holds on the explicit subfamily (9).

## 4. Why this is strictly sharper than the gcd-of-norms obstruction

The previous sufficient integer was

```text
G_(K,r)^(3)=gcd{|N_(L/Q)(c)| : c in C_(K,r)^(3)}.        (12)
```

If `p|D_(K,r)^(3)`, Lemma 1 gives one prime ideal `P|p` containing **all** coefficients.  Hence `p` divides every individual coefficient norm and therefore

```text
rad(D_(K,r)^(3)) divides rad(G_(K,r)^(3)).               (13)
```

The converse need not hold: `p` may divide every norm because different primes above `p` divide different coefficients, even though no single prime ideal contains the whole coefficient ideal.  Therefore `D` encodes the actual simultaneous congruence condition whereas `G` can contain rational false positives.

The new growing-parameter target is correspondingly weaker:

```text
P_split^+(D'_K^(3)) <= K^(4+o(1)).                       (14)
```

A proof of (14) closes the pointwise Cayley-energy bottleneck throughout `K=o(p^(1/4))`.  No such proof is currently known.

## 5. Chebyshev form of the normalized two-row equation

Normalize a distinct row pair to

```text
w=zeta,
q=zeta^r.
```

Put

```text
s_n=zeta^n-zeta^(-n),
tau=zeta+zeta^(-1).
```

The constrained affine trace equation in `cayley_product_row_intersections.md` has coefficients

```text
alpha=(q-q^(-1))/(w-w^(-1))=s_r/s_1,
beta =-2 s_(r-1)/s_1.                                   (15)
```

Using the Chebyshev polynomial of the second kind,

```text
s_n/s_1=U_(n-1)(tau/2),                                  (16)
```

so exactly

```text
alpha=U_(r-1)(tau/2),
beta=-2U_(r-2)(tau/2).                                   (17)
```

Thus the affine copy of the cyclotomic trace set is not generic: its slope and intercept are consecutive Chebyshev values in the maximal real cyclotomic field.

If

```text
t_a=zeta^a+zeta^(-a),
t_b=zeta^b+zeta^(-b),                                    (18)
```

then one common row parameter is equivalent to

```text
s_r t_a-s_1 t_b-2s_(r-1)=0.                              (19)
```

Equivalently, with a Laurent variable `Z`, define

```text
F_(a,b,r)(Z)
 =(Z^r-Z^(-r))(Z^a+Z^(-a))
 -(Z-Z^(-1))(Z^b+Z^(-b))
 -2(Z^(r-1)-Z^(1-r)).                                    (20)
```

After multiplication by a suitable monomial to clear negative exponents,

```text
(Z-1)^3 | F_(a,b,r)(Z).                                  (21)
```

One direct proof sets `Z=e^u`; up to the common factor `4`, (20) becomes

```text
sinh(ru)cosh(au)-sinh(u)cosh(bu)-sinh((r-1)u).           (22)
```

This is odd in `u`, and its linear term is `r-1-(r-1)=0`, so the zero at `u=0`, hence at `Z=1`, has order at least three.

For two distinct trace classes,

```text
t_a-t_c=(zeta^a-zeta^c)(1-zeta^(-a-c)).                 (23)
```

Thus subtracting two equations (19) expresses the common slope as a quotient of products of cyclotomic units after removal of the unique prime above `K`.  Three row intersections impose two simultaneous congruences among such units.  This is the most structured current route toward (14): control the **ideal gcd** of several cyclotomic-unit differences, not their separate archimedean norms.

## 6. Exact finite Smith-normal-form anchors

`computations/verification/cayley_product_row_coefficient_ideal.py` constructs the selected subresultant coefficient ideal as a `Z`-lattice in the basis

```text
1,zeta,...,zeta^(K-2)
```

and computes the Smith normal form.  The largest invariant factor is exactly the exponent (3), hence `D_(K,r)^(3)`.

Exact computations give

```text
K=7,  r=2:   D=2*7^2,                  D'=1,
K=11, r=2:   D=2*11^4,                 D'=1,
K=13, r=3:   D=2*3*13^6,               D'=3,
K=13, r=12:  D=2^5*5^2*13^6,           D'=5^2,
K=17, r=10:  D=2^2*17^9*103,           D'=103.          (24)
```

A slower extended computation gives

```text
K=23, r=18:
D=2*23^13*47^3*139,
D'=47^3*139.                                              (25)
```

Compare the older norm-gcd values

```text
G'_(13,3)=3^3,
G'_(13,12)=5^8,
G'_(17,10)=103^2,
G'_(23,18)=47^20*139^2.                                  (26)
```

The coefficient ideal preserves the relevant realized split-prime support in these anchors while removing substantial artificial valuation inflation.  These finite computations verify only the stated finite examples; they do not prove (14).

## 7. Current closure condition

The product-row route is now reduced to the following arithmetic problem:

> **Coefficient-ideal divisor problem.**  Bound the split rational prime divisors of `D'_K^(3)` uniformly for odd prime `K`; in particular prove (14), or otherwise prove `I_K(p)=K^(o(1))` on the exceptional support.

Generic subgroup-on-curve technology does not currently supply the needed bounded intersection.  In particular, the proved subgroup-curve estimates retain a `K^(2/3)` scale, while Konyagin--Shparlinski--Vyugin (2020) formulate a bounded-solution statement for a related special Möbius equation only as a conjecture.  The special Chebyshev/cyclotomic-unit structure (17)--(23), rather than a generic incidence theorem, is therefore the present high-value target.

No Gaussian limit, local eigenvalue law, or microscopic BGS/GOE theorem is claimed here.