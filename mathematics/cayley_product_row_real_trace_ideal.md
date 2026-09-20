# Exact real-trace ideal for three product-row intersections

**Status: EXACT for the trace reduction and prime-support equivalence; EXACT + EXTERNAL-THEOREM for the classical subresultant criterion; FINITE-REGRESSION for the Smith-normal-form anchors; OPEN for growing-`K` control of the resulting split support.**

This note repairs and sharpens the order-three obstruction.  The dehomogenized projective row polynomials used in `cayley_product_row_subresultants.md` are a safe **one-way** obstruction, but their leading coefficients can vanish after reduction, so their coefficient ideals may contain projective degree-drop false positives.  The trace coordinate removes that defect completely.

The key point is that all subgroup traces are finite, the relevant affine map has unit slope, and the unique characteristic-zero common trace is the invalid row class.  After dividing out that forced root, the two trace polynomials keep fixed degree at every split prime `p!=K`.  Their gcd degree is therefore exactly the number of common product-row parameters.

## 1. The full trace polynomial

Let `K=2m+1` be an odd prime, let `zeta` be a primitive `K`-th root of unity, and put

```text
tau=zeta+zeta^(-1),
L^+=Q(tau),
O^+=Z[tau].                                              (1)
```

For prime conductor, `O^+` is the ring of integers of the maximal real cyclotomic field and `[L^+:Q]=m`.

Let `C_K(T)` be the monic minimal polynomial of `tau`.  Equivalently,

```text
Phi_K(Z)=Z^m C_K(Z+Z^(-1)),                              (2)
```

or explicitly

```text
C_K(T)=1+2 sum_{a=1}^m T_a(T/2),                         (3)
```

where `T_a` is the Chebyshev polynomial of the first kind.

Define

```text
H_K(T)=(T-2)C_K(T).                                      (4)
```

Its roots are exactly the `m+1` trace classes

```text
t_a=zeta^a+zeta^(-a),  a in F_K/{+-1},                  (5)
```

including `t_0=2`.

## 2. The normalized affine row map

Normalize two distinct noncentral product rows by Galois scaling to indices `(1,r)`, `r!=1`.  Put

```text
s_n=zeta^n-zeta^(-n).
```

The exact common-parameter equation from `cayley_product_row_intersections.md` is

```text
Y=alpha_r X+beta_r,                                     (6)
```

with

```text
alpha_r=s_r/s_1=U_(r-1)(tau/2),
beta_r=-2s_(r-1)/s_1=-2U_(r-2)(tau/2).                  (7)
```

Thus `alpha_r,beta_r in O^+`, and `alpha_r` is a cyclotomic unit.  In particular its reduction is nonzero at every prime above a rational prime `p!=K`.

The invalid source trace is `X=tau`.  Equation (6) sends it to the invalid target trace:

```text
alpha_r tau+beta_r=zeta^r+zeta^(-r)=t_r.                (8)
```

Define the two degree-`m` cofactor polynomials

```text
P_(K,r)(T)=H_K(T)/(T-tau),                               (9)

Q_(K,r)(T)=H_K(alpha_r T+beta_r)/(T-tau).               (10)
```

Both belong to `O^+[T]`.  The second divisibility follows from (8); division by the monic factor `T-tau` preserves integrality.  The leading coefficient of `P` is `1`, while that of `Q` is `alpha_r^(m+1)`, hence a unit.

## 3. Exact finite-field interpretation

Let `p==1 (mod K)` be prime and let `q` be a prime ideal of `O^+` above `p`.  Choose a primitive `K`-th root `h in F_p^*` corresponding to this real embedding, up to `h<->h^(-1)`.

Because `p!=K`, the trace values

```text
h^a+h^(-a),  a mod +-1,                                 (11)
```

are pairwise distinct.  Indeed equality of two such traces implies `h^a=h^(+-b)`.  Hence `H_K mod q` is squarefree and split.

The roots of `P mod q` are exactly the valid source trace classes for row `1`: all classes except `a=+-1`.  Since `alpha_r` is a unit, the roots of `Q mod q` are exactly the inverse affine images under (6) of the valid target trace classes for row `r`: all classes except `b=+-r`.

The fractional-linear change from source trace to the projective Cayley parameter is

```text
mu=(1-h^2)/(hX-2).                                      (12)
```

Its determinant is nonzero for `p!=K`, so it is injective on the projective line.  Therefore common roots of `P,Q` are in bijection with common Cayley parameters of the two product rows, including the possible parameter at infinity.  Thus

### Theorem 1 (exact gcd/intersection identity)

```text
deg gcd(P_(K,r),Q_(K,r) mod q)
 = I_(1,r)(q),                                           (13)
```

where the right side is the number of common parameters of the normalized row pair for the reduction associated with `q`.

Simultaneous inversion sends row pair `(i,j)` to `(-i,-j)` and negates every Cayley sum, so intersection cardinality is unchanged.  The real embeddings, indexed by `i mod +-1`, therefore cover all physical row pairs of a fixed ratio class.  Swapping the two rows identifies `r` with `r^(-1)`.

## 4. The canonical order-three real-trace ideal

Let

```text
S_0^(r), S_1^(r), S_2^(r)                               (14)
```

be the first three fixed-degree subresultants of the degree-`m` polynomials `P_(K,r),Q_(K,r)`.  Let `Jtr_(K,r)^(3)` be the ideal of `O^+` generated by every nonzero coefficient of these three subresultants:

```text
Jtr_(K,r)^(3)=(coefficients of S_0,S_1,S_2).             (15)
```

It is nonzero in characteristic zero, because the only common root of the two **full** trace polynomials is the forced invalid trace (8), which has already been divided out; equivalently the maintained characteristic-zero Cayley rigidity gives no valid common row parameter.

Write

```text
Jtr_(K,r)^(3) intersect Z = Lambda_(K,r)^(3) Z,          (16)
```

with `Lambda_(K,r)^(3)>0`.  As for any nonzero ideal in a number ring,

```text
Lambda_(K,r)^(3)=exp_additive(O^+/Jtr_(K,r)^(3)).        (17)
```

### Lemma 2 (rational-prime contraction support)

For a rational prime `p`,

```text
p | Lambda_(K,r)^(3)
iff
there exists q|p in O^+ with Jtr_(K,r)^(3) subset q.     (18)
```

The proof is the standard contraction argument: one implication uses `q intersect Z=(p)`; conversely, if `p` divides the additive exponent of the finite quotient, the class of `p` is not a unit and lies in a maximal ideal of the quotient.

### Theorem 3 (exact geometric split-prime support)

For every split prime `p==1 mod K`, `p!=K`,

```text
p | Lambda_(K,r)^(3)
iff
some product-row pair in ratio class [r]
has at least three common Cayley parameters.             (19)
```

### Proof

By the classical fixed-degree subresultant criterion,

```text
deg gcd(P,Q)>=3
iff
S_0=S_1=S_2=0.                                           (20)
```

Because both `P,Q` retain degree exactly `m` modulo every `q|p`, there is no specialization degree-drop ambiguity.  Equations (18), (20), and the exact identity (13) give (19).

The external algebraic input is the standard subresultant theorem; a maintained reference is W. S. Brown and J. F. Traub, *On Euclid's Algorithm and the Theory of Subresultants*, Journal of the ACM 18 (1971), 505--514, DOI `10.1145/321662.321665`.

## 5. Pointwise quadratic Cayley energy outside the exact support

Remove factors `2` and `K` from `Lambda_(K,r)^(3)` and set

```text
Lambda'_(K,r)^(3)=prime-to-2K part,
Lambda'_K^(3)=product_[r] Lambda'_(K,r)^(3),              (21)
```

where `[r]` runs over distinct row-ratio classes modulo inversion.

Theorem 3 gives the exact equivalence

```text
p does not divide Lambda'_K^(3)
iff
I_K(p)<=2                                                (22)
```

for split primes `p` (with the harmless convention that ratio classes with trivial `Lambda'` contribute `1`).  Therefore the exact cross-row energy theorem yields

```text
Delta_K(p)<=8(K-1)(K-2),                                 (23)
```

and hence

```text
E_+(c(H\{1}))<=11(K-1)(K-2).                            (24)
```

This is the pointwise quadratic Cayley-energy scale, with **exact** arithmetic exceptional support.

## 6. Why this repairs the earlier coefficient ideal

The dehomogenized projective-row obstruction `D_(K,r)^(3)` from `cayley_product_row_coefficient_ideal.md` remains a valid one-way detector:

```text
I>=3  ==>  p|D.                                          (25)
```

However the converse can fail when a specialization makes both dehomogenized row polynomials lose leading degree at `mu=infinity`.  This can force low subresultants to vanish without three distinct projective intersections.

The trace formulation has no such failure mode:

- every trace root is finite;
- `H_K mod q` is squarefree for split `p!=K`;
- `alpha_r` is a unit, so `Q` never loses degree;
- the unique characteristic-zero common trace is divided out explicitly.

Thus `Lambda` is the canonical exact support for the order-three **geometric** row-intersection event, whereas `D` and the older norm-gcd `G` are safe supersets.

## 7. Exact finite anchors

`computations/verification/cayley_product_row_real_trace_ideal.py` constructs `C_K`, `P,Q`, their selected subresultants, and the coefficient ideal in the integral basis

```text
1,tau,...,tau^(m-1).                                    (26)
```

Smith normal form gives the additive exponent (17).  Exact computations give

```text
K=7,  r=2:   Lambda=7,                       Lambda'=1,
K=11, r=7:   Lambda=11^2,                    Lambda'=1,
K=13, r=3:   Lambda=13^3,                    Lambda'=1,
K=13, r=12:  Lambda=2^4*5^2*13^3,            Lambda'=5^2,
K=17, r=10:  Lambda=2^2*17^5*103,            Lambda'=103. (27)
```

A slower extended anchor gives

```text
K=23, r=18:
Lambda=23^8*47^3*139,
Lambda'=47^3*139.                                         (28)
```

The primes `103`, `47`, and `139` are genuinely realized by row intersections of sizes at least three in the maintained finite corpus.  By contrast, factors such as the `23` appearing in a dehomogenized full-cyclotomic coefficient ideal at `K=11` disappear here because they came from a projective degree-drop event rather than three geometric intersections.

Finite anchors verify only the stated finite cases.

## 8. Current closure condition

The pointwise Cayley-energy problem is now reduced to the exact geometric support integer `Lambda'_K^(3)`.  A sufficient growing-parameter theorem is

```text
P_split^+(Lambda'_K^(3)) <= K^(4+o(1)).                  (29)
```

For each fixed `0<epsilon<1/4`, (29) implies that every sufficiently large split design with `K<=p^(1/4-epsilon)` lies outside the exact order-three exceptional support and hence satisfies (24). It does not by itself cover the full regime `K=o(p^(1/4))`: the unspecified subpower factor in `K^(4+o(1))` may exceed the diverging ratio `p/K^4`. A bound `P_split^+(Lambda'_K^(3))=O(K^4)` would suffice for that full regime. For example, a loss `exp(sqrt(log K))` is permitted by (29), while `p/K^4` could grow only like `log K`; the proposed estimate alone does not compare those scales.

No proof of (29) is currently known.  Generic subgroup-on-curve estimates retain the `K^(2/3)` loss, and bounded-solution statements for related Möbius/subgroup equations remain conjectural in the literature.  The active route is therefore to exploit the special Chebyshev/cyclotomic-unit structure of (7), not to invoke a nonexistent generic `O(1)` incidence theorem.

No Gaussian limit, local eigenvalue law, or microscopic BGS/GOE theorem is claimed here.