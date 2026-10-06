# Principal-subresultant scalar support for product-row intersections

**Status: EXACT + EXTERNAL-THEOREM for the fixed-degree principal-subresultant criterion; FINITE-REGRESSION for the Smith anchors; OPEN for polynomial control of the largest supported split prime.**

This note simplifies the exact maximal-real row-support construction in
`cayley_product_row_real_trace_ideal.md`.

Once the valid trace cofactors have been put in a specialization-safe
fixed-degree model, the full coefficient ideals of the first three
subresultant polynomials are not needed to detect the event

```text
row intersection size >= 3.
```

It is enough to use only the first three **principal subresultant coefficients**.
Thus the general ratio class, not only the inverse class, admits an exact
three-scalar determinant formulation.

## 1. Fixed-degree setup

Let `K=2m+1>=7` be an odd prime, let

```text
tau=zeta+zeta^(-1),
O^+=Z[tau],
H_K(T)=(T-2)C_K(T),
```

and fix a normalized product-row ratio `r!=1`.  As in the real-trace note,
remove the unique invalid characteristic-zero trace to obtain

```text
P_(K,r)(T), Q_(K,r)(T) in O^+[T],                       (1)
```

both of degree exactly `m`.  Their leading coefficients are units at every
split prime `p==1 mod K`, `p!=K`.  For every embedding prime `q|p`,

```text
deg gcd(P_(K,r),Q_(K,r) mod q)
 = I_(1,r)(q),                                            (2)
```

the geometric row-intersection count.

The fixed-degree property is load-bearing.  It is exactly what failed for the
older dehomogenized projective `D/G` construction at the point at infinity.

## 2. Principal subresultants

For two fixed-degree polynomials `P,Q` over a commutative ring, let

```text
S_j(P,Q;T)                                                (3)
```

denote the standard `j`-th subresultant polynomial and define its principal
coefficient

```text
psc_j(P,Q) = coefficient of T^j in S_j(P,Q;T).           (4)
```

In particular `psc_0` is the ordinary resultant up to the fixed sign convention.
The coefficients `psc_j` are determinants of the usual principal subresultant
Sylvester minors.

We use the standard fixed-degree subresultant theorem: over a field, if

```text
g=deg gcd(P,Q),
```

then

```text
S_0=...=S_(g-1)=0,
S_g=c*gcd(P,Q),  c!=0.                                   (5)
```

This is the same Brown--Traub subresultant input already used elsewhere in the
repository; no new external theorem is introduced.

### Lemma 1 (principal coefficients detect gcd degree)

Let `k` be a field and let `P,Q in k[T]` specialize with their maintained
fixed degrees. For every integer `1<=d<=min(deg P,deg Q)`,

```text
deg gcd(P,Q)>=d
iff
psc_0(P,Q)=...=psc_(d-1)(P,Q)=0.                         (6)
```

### Proof

Let `g=deg gcd(P,Q)`.  By (5), every subresultant with index below `g`
vanishes, hence so do its principal coefficients.

Conversely, if `g<d`, then (5) says

```text
S_g=c*gcd(P,Q), c!=0.
```

The right side has degree exactly `g`, so its `T^g` coefficient is nonzero.
Thus `psc_g!=0`, contradicting vanishing of all principal coefficients with
index below `d`. `□`

This argument also disposes of the possible ``defective subresultant'' worry:
defect can occur later in a subresultant sequence, but the first nonzero
subresultant at the actual gcd degree has exactly that degree and therefore
nonzero principal coefficient.

## 3. Three-scalar exact order-three support

Apply Lemma 1 with `d=3` to the fixed-degree real-trace cofactors.  Put

```text
pi_0=psc_0(P_(K,r),Q_(K,r)),
pi_1=psc_1(P_(K,r),Q_(K,r)),
pi_2=psc_2(P_(K,r),Q_(K,r)) in O^+,                      (7)
```

and define the principal-subresultant ideal

```text
J^psc_(K,r)=(pi_0,pi_1,pi_2) subset O^+,
J^psc_(K,r) intersect Z = Pi_(K,r)^(3) Z,                (8)
```

with positive generator `Pi_(K,r)^(3)`.

### Theorem 2 (exact principal-scalar split support)

For every split rational prime `p==1 mod K`,

```text
p | Pi_(K,r)^(3)
iff
some embedding prime q|p has I_(1,r)(q)>=3.              (9)
```

Therefore `Pi_(K,r)^(3)`, the full-coefficient real-trace support
`Lambda_(K,r)^(3)`, and the scalar shift-resultant support
`Omega_(K,r)^(3)` have the same **split rational-prime support**.

Equality of the three integers or of their valuations is not claimed.

### Proof

For a chosen split embedding prime, the maintained leading coefficients remain
nonzero and (2) identifies gcd degree with geometric row-intersection count.
Lemma 1 gives

```text
I_(1,r)(q)>=3
iff
pi_0==pi_1==pi_2==0 mod q.                               (10)
```

The standard contraction criterion says that a rational prime divides the
positive generator of `J^psc cap Z` exactly when the ideal is contained in some
prime ideal above that rational prime.  This gives (9).  The same geometric
event defines the split support of `Lambda` and `Omega`. `□`

## 4. Why this formulation is smaller

The original real-trace construction stored every coefficient of

```text
S_0(P,Q;T), S_1(P,Q;T), S_2(P,Q;T).                      (11)
```

For an order-three event this is more data than necessary.  The exact detector
is just

```text
psc_0, psc_1, psc_2.                                     (12)
```

Each is a single determinant of a nested Sylvester-type matrix.  This gives a
third exact scalarization of the same support:

```text
full subresultant coefficient ideal  Lambda,
shift-resultant low coefficients     Omega,
principal subresultant coefficients  Pi.                 (13)
```

For future arithmetic work, `Pi` is attractive because its generators are
canonical nested determinants rather than coefficients of an auxiliary shift
polynomial.

## 5. Relation to the per-ratio mass budget

The first scalar is the ordinary row resultant:

```text
pi_0=+-Res_T(P_(K,r),Q_(K,r)).                           (14)
```

Up to the harmless normalization convention, this is the `Z=0` coefficient of
the scalar shift resultant used in `cayley_trace_intercept_rigidity.md`.
Therefore the same archimedean argument gives, for each fixed ratio,

```text
sum_(p==1 mod K, I_r(p)>=3) log p = O(K^3).              (15)
```

The principal-scalar reformulation does not improve the size of `pi_0` by
itself.  Its value is that the exceptional event is now the common-divisor
condition

```text
q | pi_0,
q | pi_1,
q | pi_2.                                                 (16)
```

The next arithmetic target is to exploit algebraic relations among these
**nested determinant minors**, rather than bound the norm of any one generator
separately.

## 6. Exact finite regression

`computations/verification/cayley_principal_subresultant_support.py` extracts
only the three principal coefficients from the already maintained fixed-degree
real-trace subresultants and contracts their ideal by Smith normal form.

The default anchors are

```text
(K,r)=(7,2):
    Pi=7,                         Pi'=1,

(K,r)=(11,7):
    Pi=11^2,                      Pi'=1,

(K,r)=(13,3):
    Pi=13^3,                      Pi'=1,

(K,r)=(13,12):
    Pi=2^4*5^3*13^3,              Pi'=5^3,

(K,r)=(17,10):
    Pi=2^2*17^5*103,              Pi'=103.               (17)
```

The prime-to-`2K` support agrees with the corresponding `Lambda` / `Omega`
anchors.  At `(13,12)` the exponent of `5` differs from both previously
maintained scalarizations, which is a useful negative control against silently
identifying the support integers themselves.

The reference computation is materially cheaper than contracting every
coefficient of three subresultant polynomials, although Smith normal form can
still dominate at larger `K`.  A scalable implementation should use modular or
fraction-free exact lattice arithmetic.

## 7. Inverse-ratio specialization

For `r=-1`, the general principal-scalar criterion is compatible with the more
structured two-scalar inverse formulations:

```text
I_-1>=3
iff deg gcd(E,O)>=2
iff Res(E,O)=0 and psc_1(E,O)=0
iff S(0)=S'(0)=0
iff rho(0)=rho'(0)=0,                                    (18)
```

where

```text
rho(Z)=Res(E_Z,O_Z)
```

is the translated half-degree resultant from
`cayley_inverse_pair_sum_factorization.md`.

The inverse two-scalar route remains preferable computationally and
structurally, because reflection halves the degree and the pair-sum square
explains the even intersection multiplicity.

## 8. Current open target

The pointwise split closure condition is unchanged.  A sufficient theorem is,
for example,

```text
P_split^+( product_[r] Pi'_(K,r)^(3) ) <= K^(4+o(1)),    (19)
```

which is equivalent at the level of split prime support to the maintained
`Lambda` or `Omega` largest-prime target.

This proposed bound excludes supported split primes for each fixed
`0<epsilon<1/4` when `K<=p^(1/4-epsilon)`. It does not alone cover all of
`K=o(p^(1/4))`; an `O(K^4)` largest-split-divisor bound would suffice for
that full regime. See the quantifier distinction in
`cayley_product_row_real_trace_ideal.md`, Section 8.

The useful new formulation is that the general exceptional prime must divide
three canonical nested Sylvester determinants simultaneously.  A high-value
next step is a Desnanot--Jacobi / Bezout / subresultant identity that forces a
small common divisor of `pi_0,pi_1,pi_2`, rather than another estimate for their
individual norms.