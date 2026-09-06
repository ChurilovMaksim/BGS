# Polynomial-scale Cayley energy via subgroup curves

**Status: EXACT, conditional only on the explicitly cited Makarychev--Vyugin subgroup-curve theorem.**

This note closes the first unconditional polynomial-scale upper bound in the
mixed Cayley layer.  It does **not** close the off/off elliptic term or the
microscopic BGS bridge.

Let `p` be an odd prime, let `H <= F_p^*` have odd order `K`, and define

```text
c(h)=(h+1)/(h-1),
A=c(H\{1}),
d(u,v)=(u-1)(v-1)/(v-u),
C_H(t)=#{(u,v) in (H\{1})^2 : u!=v and d(u,v)=t}.
```

As recorded in `cayley_additive_energy.md`,

```text
sum_t C_H(t)^2 = E_+(A)-|A|^2.
```

The goal here is to bound this quantity uniformly with `K` growing.

## 1. Ratio fibres

For an admissible ordered pair `(u,v)`, put

```text
rho=u/v in H\{1}.
```

Then `u=rho*v` and

```text
d_rho(v)
 = ((rho*v-1)(v-1))/(v(1-rho))
 = (rho*v + v^(-1) - (rho+1))/(1-rho).
```

Thus the energy counts pairs of ratio fibres with equal values.  If we enlarge
the fibre by allowing all `v in H` (temporarily restoring the two points
`v=1` and `rho*v=1` excluded from the original pair-key domain), then

```text
sum_t C_H(t)^2
 <= sum_{rho,sigma in H\{1}} N(rho,sigma),
```

where

```text
N(rho,sigma)=#{(x,y) in H^2 : d_rho(x)=d_sigma(y)}.
```

This enlargement is only used for an upper bound.

## 2. The fixed-degree curve

Clearing the nonzero denominators gives

```text
F_{rho,sigma}(x,y)
 = (1-sigma)y(rho*x-1)(x-1)
   -(1-rho)x(sigma*y-1)(y-1).
```

Because `K` is odd, squaring is an automorphism of `H`.  Hence the monomial map

```text
(U,V) -> (x,y)=(U/V, U*V)
```

is a bijection `H^2 -> H^2`: its inverse is determined uniquely by

```text
U^2=xy,  V^2=y/x.
```

On the torus `U,V != 0`, dividing by `x=U/V` gives the polynomial

```text
G_{rho,sigma}(U,V)
 = sigma(rho-1) U^2 V^2
   + rho(1-sigma) U^2
   + 2(sigma-rho) U V
   + (1-sigma) V^2
   + (rho-1).
```

The exact identity is

```text
(V/U) F_{rho,sigma}(U/V,U*V)=G_{rho,sigma}(U,V).
```

Thus `N(rho,sigma)` is exactly the number of `H^2`-points on `G=0`.

## 3. Geometric irreducibility off the parameter diagonal

Assume

```text
rho,sigma in H\{1},  rho!=sigma.
```

Regard `G` as a quadratic polynomial in `U` over
`\overline{F_p}[V]`.  Its coefficients are

```text
A(V)=sigma(rho-1)V^2 + rho(1-sigma),
B(V)=2(sigma-rho)V,
C(V)=(1-sigma)V^2 + (rho-1).
```

A direct discriminant computation gives

```text
Delta(V)=B(V)^2-4A(V)C(V)
 = -4(rho-1)(sigma-1)(rho-sigma V^2)(V^2-1).
```

Because `p` is odd and `rho,sigma` are nonzero, nonunit and distinct, the four
geometric roots

```text
V=+1, -1, +sqrt(rho/sigma), -sqrt(rho/sigma)
```

are pairwise distinct.  Therefore `Delta` is not a square in
`\overline{F_p}(V)`.

Also `A,B,C` are primitive as polynomials in `V`: any common divisor would
divide `B`, hence (because `rho!=sigma`) would divide `V`, but
`C(0)=rho-1!=0`.  By Gauss's lemma, the nonsquare discriminant implies that
`G_{rho,sigma}` is irreducible over `\overline{F_p}`.

The remaining hypotheses needed below are explicit:

```text
bidegree (m,n)=(2,2),
G(0,0)=rho-1 != 0,
deg_U G(U,0)=2,
g=1,
```

where `g` is the gcd of differences of occurring `V`-exponents in the notation
of Makarychev--Vyugin.  Here `g=1` because the nonzero `UV` coefficient gives
`V`-exponent `1` in addition to exponents `0,2`.

## 4. External point bound, with hypotheses translated

We use Theorem 2 of

S. Makarychev and I. Vyugin,
*Solutions of Polynomial Equations in Subgroups of F_p^**,
Arnold Mathematical Journal **5** (2019), 105--121,
DOI `10.1007/s40598-019-00112-z`.

For `h=1` their `G`-independence condition is vacuous.  Their theorem gives

```text
# {(U,V) in H^2 : G_{rho,sigma}(U,V)=0}
 <= 12*m*n*g*(m+n)*K^(2/3)
 = 192 K^(2/3),
```

provided

```text
10^3 < K < (1/3) p^(3/4)
```

and

```text
1 < (40*m*n^2)^(-3) K^2.
```

For `(m,n)=(2,2)` the last condition is

```text
K^2 > 320^3 = 32768000,
```

so it holds for every integer `K>=5725`.

No genericity phrase is being used here: Section 3 verifies geometric
irreducibility for every ordered off-diagonal parameter pair
`rho!=sigma`.

## 5. The parameter diagonal

For `rho=sigma`, the transformed curve factors exactly:

```text
G_{rho,rho}(U,V)
 = (rho-1)(V^2-1)(rho U^2-1).
```

Since `H` has odd order, `V^2=1` has exactly the solution `V=1` in `H`, and
`rho U^2=1` has exactly one solution `U in H`.  The two components meet in one
point, hence

```text
N(rho,rho)=2K-1.
```

## 6. Explicit energy theorem

### Theorem

Let `p` be an odd prime and `H <= F_p^*` an odd-order subgroup of size `K`.
If

```text
5725 <= K < (1/3) p^(3/4),
```

then

```text
sum_t C_H(t)^2
 <= (K-1)(2K-1)
    + 192 (K-1)(K-2) K^(2/3).
```

In particular

```text
sum_t C_H(t)^2 = O(K^(8/3))
```

with an absolute implied constant in this range.

### Proof

There are `K-1` diagonal parameter pairs and `(K-1)(K-2)` ordered
parameter-off-diagonal pairs.  Section 5 gives `2K-1` points on each enlarged
diagonal fibre; Sections 3--4 give at most `192 K^(2/3)` points on each
off-diagonal fibre.  Summing and recalling the domain enlargement from
Section 1 proves the displayed bound.

For `K<5725`, the trivial estimate

```text
sum_t C_H(t)^2 <= ((K-1)(K-2))^2 < K^4
```

absorbs the bounded range.  Therefore, throughout

```text
K < (1/3)p^(3/4),
```

one may write uniformly

```text
sum_t C_H(t)^2 << K^(8/3)
```

with an absolute constant.  For example the deliberately coarse explicit
constant `102393` suffices for the small range, while the high-`K` theorem has
coefficient below `194` after the lower-order diagonal term is absorbed.

The theorem therefore applies automatically in the intended asymptotic regime
`K=o(p^(1/4))` once the parameters are sufficiently large.

## 7. Exact propagation into the mixed Fourier fluctuation

Let

```text
M(t)=2(p-2) C_H(t),   t in F_p^*.
```

Writing variance over the `p-1` nonzero values of `t`,

```text
Var_{t!=0} M(t)
 <= (1/(p-1)) sum_{t!=0} M(t)^2
 = 4(p-2)^2/(p-1) * sum_t C_H(t)^2.
```

The same finite-Fourier orthogonality used in
`fourth_moment_reduction.md` gives

```text
Var_{q!=0} \widehat M(q)
 = p Var_{t!=0} M(t).
```

Hence in the range above,

```text
Var_{q!=0} \widehat M(q)
 << p^2 K^(8/3).
```

This is a genuine polynomial-scale control of the mixed piece.  It does not by
itself control the covariance with the off/off contribution `O(t)` and is not
a microscopic eigenvalue-statistics theorem.

## 8. Independent checks and scope

The polynomial transform, discriminant identity and diagonal factorization were
rederived independently in exact symbolic arithmetic before promotion.  The
maintained regression added with this route checks those identities and compares
the direct Cayley energy with the ratio-curve decomposition on several finite
designs.

What this theorem **does not** establish:

- it does not improve the exponent `8/3` to the subgroup-like `5/2` scale;
- it does not close the centered off/off elliptic estimate;
- it does not prove that `8/3` is optimal;
- it does not imply microscopic BGS/GOE statistics.

The highest-value next question is whether the two-parameter family can be
averaged nontrivially (rather than bounding each `rho,sigma` curve separately),
which is the natural route from `K^(8/3)` toward `K^(5/2)` or better.
