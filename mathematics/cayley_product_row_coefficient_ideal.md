# Full-cyclotomic coefficient ideal for higher product-row intersections

**Status: EXACT for the ideal-contraction construction and the one-way geometric obstruction; FINITE-REGRESSION for Smith-normal-form anchors; SUPERSEDED as an exact geometric-support object by `cayley_product_row_real_trace_ideal.md`.**

## Correction notice

An adversarial specialization audit found a real limitation of the original formulation of this note.  The row polynomials used here are dehomogenized projective forms.  At a split prime, both leading coefficients can vanish, corresponding to a common projective point at `mu=infinity`.  Standard dehomogenized subresultants can then vanish to higher order even when there are fewer than three distinct geometric row intersections.

Therefore the active statement is only

```text
I_(i,j)(p)>=3  ==>  p | D'_(K,r)^(3).                    (1)
```

The converse is **not** claimed.  In particular, `D` may contain degree-drop false positives in addition to the rational false positives already removed relative to the older gcd-of-norms integer `G`.

The exact two-sided geometric support is now given by the fixed-degree maximal-real-field trace cofactors and their contraction integer `Lambda` in [`cayley_product_row_real_trace_ideal.md`](cayley_product_row_real_trace_ideal.md).  That note is authoritative for the current order-three frontier.

## 1. The full-cyclotomic coefficient ideal

Let `K` be an odd prime, `L=Q(zeta)`, `O_L=Z[zeta]`, and let `R_1,R_r` be the Galois-normalized dehomogenized product-row polynomials of degree `m=(K-1)/2` in characteristic zero.  Let

```text
S_0^(r), S_1^(r), S_2^(r)
```

be the first three characteristic-zero subresultants used in the maintained verifier.  If `C_(K,r)^(3)` is the set of all their nonzero coefficients, define

```text
J_(K,r)^(3)=(C_(K,r)^(3)) subset O_L,                    (2)
J_(K,r)^(3) intersect Z = D_(K,r)^(3) Z,                 (3)
```

with positive generator `D_(K,r)^(3)`.

Since `J` is a nonzero ideal,

```text
D_(K,r)^(3)=exp_additive(O_L/J_(K,r)^(3)).               (4)
```

For every rational prime `p`,

```text
p|D_(K,r)^(3)
iff
there is a prime ideal P|p containing J_(K,r)^(3).       (5)
```

This contraction lemma is exact.  What failed in the older wording was the additional identification of `J subset P` with **three distinct projective row intersections** after a specialization where the dehomogenized degree itself can drop.

## 2. Safe geometric consequence

If a split reduction has at least three distinct common row parameters, the corresponding fixed-degree homogeneous Sylvester map has corank at least three.  In any dehomogenized chart this forces the maintained low subresultants to vanish after specialization (degree drop can create extra vanishing, but cannot remove the vanishing forced by three genuine common factors).  Hence the safe implication (1) holds.

After stripping factors `2,K` and multiplying over row-ratio classes, define `D'_K^(3)` as before.  Then

```text
p does not divide D'_K^(3)
==> I_K(p)<=2
==> Delta_K(p)<=8(K-1)(K-2)
==> E_+(c(H\{1}))<=11(K-1)(K-2).                        (6)
```

Thus this note still supplies a valid explicit **sufficient** arithmetic subfamily for quadratic Cayley energy.  It is simply not the minimal/exact exceptional support.

## 3. Relation to the older gcd-of-norms integer

The previous integer was

```text
G_(K,r)^(3)=gcd{|N_(L/Q)(c)|:c in C_(K,r)^(3)}.          (7)
```

If `p|D`, one prime ideal `P|p` contains all coefficients, so `p` divides every coefficient norm. Therefore

```text
rad(D_(K,r)^(3)) divides rad(G_(K,r)^(3)).               (8)
```

This improvement remains correct: `D` removes rational false positives caused by **different prime ideals above the same rational prime dividing different coefficients**.  The subsequent real-trace refinement removes the separate **projective degree-drop** false positives.

The hierarchy is therefore

```text
genuine I>=3 support
   subset support(D')
   subset support(G').                                   (9)
```

The first inclusion can be strict; the second can also be strict.

## 4. Chebyshev and sparse cyclotomic structure

Normalize rows by `w=zeta`, `q=zeta^r` and put

```text
s_n=zeta^n-zeta^(-n),
tau=zeta+zeta^(-1).
```

The affine trace equation has

```text
alpha=s_r/s_1=U_(r-1)(tau/2),
beta=-2s_(r-1)/s_1=-2U_(r-2)(tau/2).                    (10)
```

For trace classes `t_a=zeta^a+zeta^(-a)`, `t_b=zeta^b+zeta^(-b)`, a common parameter satisfies

```text
s_r t_a-s_1 t_b-2s_(r-1)=0.                              (11)
```

Equivalently the Laurent polynomial

```text
F_(a,b,r)(Z)
 =(Z^r-Z^(-r))(Z^a+Z^(-a))
 -(Z-Z^(-1))(Z^b+Z^(-b))
 -2(Z^(r-1)-Z^(1-r))                                    (12)
```

has, after clearing a monomial, a universal factor

```text
(Z-1)^3.                                                 (13)
```

Indeed at `Z=e^u`, up to a factor `4`, (12) is

```text
sinh(ru)cosh(au)-sinh(u)cosh(bu)-sinh((r-1)u),           (14)
```

an odd function whose linear term cancels.  Subtracting two relations (11) expresses `alpha` as a quotient of products of cyclotomic units.  This structure survives unchanged in the sharper real-trace formulation.

## 5. Finite Smith-normal-form anchors

The maintained verifier constructs `J` as a `Z`-lattice in the basis

```text
1,zeta,...,zeta^(K-2)
```

and computes its Smith normal form. Exact anchors include

```text
K=7,  r=2:   D'=1,
K=11, r=2:   D'=1,
K=13, r=3:   D'=3,
K=13, r=12:  D'=5^2,
K=17, r=10:  D'=103,                                    (15)
```

with the slower extended value

```text
K=23, r=18:  D'=47^3*139.                               (16)
```

These values are still correct for this full-cyclotomic dehomogenized ideal.  What changed is their interpretation.  For example, factors can occur because of specialization at the projective point at infinity even when the distinct intersection count is below three.

## 6. Active successor

The exact geometric closure condition is no longer a split-divisor bound for `D'_K^(3)`.  It is the sharper problem

```text
P_split^+(Lambda'_K^(3)) <= K^(4+o(1)),                 (17)
```

where `Lambda` is the maximal-real-field trace-cofactor contraction from `cayley_product_row_real_trace_ideal.md`.

This proposed bound excludes supported split primes for each fixed
`0<epsilon<1/4` when `K<=p^(1/4-epsilon)`. It does not alone cover all of
`K=o(p^(1/4))`; an `O(K^4)` largest-split-divisor bound would suffice for
that full regime. See the quantifier distinction in
`cayley_product_row_real_trace_ideal.md`, Section 8.

No Gaussian limit, local eigenvalue law, or microscopic BGS/GOE theorem is claimed here.