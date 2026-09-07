# Global Cayley energy from the Corvaja--Zannier curve bound

**Status: EXACT + EXTERNAL-THEOREM.** The internal algebraic geometry and energy bookkeeping are proved below. The only external theorem input is Corvaja--Zannier, *J. Eur. Math. Soc.* 15 (2013), Theorem 2 / Corollary 2, DOI 10.4171/JEMS/409. External priority for this particular Cayley specialization has not been established.

This strengthens the earlier Makarychev--Vyugin curve route in `cayley_energy_curve_bound.md`: the exponent `8/3` is unchanged, but the subgroup-size parity/range restrictions disappear and the leading fixed-curve constant is much smaller. It does not close the sharp centered `K^(2+o(1))` target and has no direct implication for microscopic BGS statistics.

Let `p` be an odd prime, let `H <= F_p^*` have order `K>=2`, and put

```text
c(h)=(h+1)/(h-1),
A=c(H\{1}),
d_rho(x)=((rho*x-1)(x-1))/((1-rho)x),   rho in H\{1}.
```

For the original pair-key multiplicities `C_H(t)`, write

```text
E_C = sum_t C_H(t)^2 = E_+(A)-(K-1)^2.
```

## 1. Ratio-fibre collision curve

For `rho,sigma in H\{1}`, extend each ratio fibre to all `x,y in H` and define

```text
N(rho,sigma)=#{(x,y) in H^2 : d_rho(x)=d_sigma(y)}.
```

Clearing denominators gives

```text
F_{rho,sigma}(x,y)
 = (1-sigma)y(rho*x-1)(x-1)
   -(1-rho)x(sigma*y-1)(y-1).                    (1)
```

For every `rho!=sigma`, this has bidegree `(2,2)`. As a quadratic in `y`, its discriminant is a quartic in `x`; direct elimination gives

```text
disc_x(disc_y F)
 =4096 rho^2 sigma^2 (rho-1)^6 (rho-sigma)^2 (sigma-1)^6.  (2)
```

Thus in odd characteristic, for nonzero distinct nonunit `rho,sigma`, the quadratic discriminant is squarefree and non-square over the algebraic closure. Hence `F` is geometrically irreducible.

The closure in `P^1 x P^1` has exactly the four boundary points

```text
(0,0), (0,infinity), (infinity,0), (infinity,infinity).
```

In the corresponding affine charts, pairs of first derivatives are respectively

```text
(rho-1,                  1-sigma),
(sigma(rho-1),           1-sigma),
(rho-1,                  rho(1-sigma)),
(sigma(rho-1),           rho(1-sigma)).            (3)
```

They are nonzero. The normalization of a geometrically irreducible bidegree `(2,2)` curve has genus one here: equivalently, the squarefree quartic discriminant gives a double cover of `P^1` branched at four points. Since a `(2,2)` divisor has arithmetic genus one, equality with the geometric genus also excludes hidden projective singularities.

The coordinate functions `x,y` each have degree two. Their valuation pairs at the four boundary points are

```text
(1,1), (1,-1), (-1,1), (-1,-1),
```

so `x` and `y` are multiplicatively independent modulo constants. The affine Euler characteristic used by Corvaja--Zannier is therefore

```text
chi = |S|+2g-2 = 4+2-2 = 4.                       (4)
```

Because `p` is odd, the degree-two coordinate maps are separable. Also `p` does not divide `K`, since `K | p-1`.

## 2. Uniform off-diagonal point bound

Apply Corvaja--Zannier Corollary 2 to the curve (1) with

```text
m1=m2=K,  d1=d2=2,  chi=4.
```

For every `rho!=sigma`,

```text
N(rho,sigma)
 <= max(3*cuberoot(32)*K^(2/3), 48*K^2/p).         (5)
```

The trivial quadratic-fibre bound also gives `N(rho,sigma)<=2K`. Hence, writing

```text
B(K,p)=min(2K, max(3*cuberoot(32)*K^(2/3),48*K^2/p)),
```

we have `N(rho,sigma)<=B(K,p)` with no lower-size, upper-size or odd-order restriction.

The first term dominates the characteristic term whenever

```text
128 K^4 <= p^3,
```

i.e.

```text
K <= 2^(-7/4) p^(3/4).                              (6)
```

## 3. Exact restoration correction and the diagonal

The extension from the original ratio fibre to all `x in H` adds exactly two points, `x=1` and `x=rho^(-1)`, and both have value zero. Consequently every ordered pair `(rho,sigma)` contributes exactly four artificial zero-zero collisions. Therefore the relation is exact:

```text
E_C = sum_{rho,sigma!=1} N(rho,sigma) - 4(K-1)^2.  (7)
```

On the diagonal,

```text
F_{rho,rho}(x,y)=-(rho-1)(x-y)(rho*x*y-1).          (8)
```

Summing the intersections of the two components over `rho!=1` gives `K-gcd(2,K)`. Hence

```text
sum_{rho!=1} N(rho,rho)
 = 2K(K-1)-K+gcd(2,K).                              (9)
```

After removing the four artificial points per diagonal ratio, the total diagonal contribution to `E_C` is

```text
D_K = 2K^2-7K+4+gcd(2,K).                           (10)
```

There are `(K-1)(K-2)` ordered off-diagonal parameter pairs. Combining (5)--(10) gives the explicit global theorem.

## 4. Global energy theorem

**Theorem.** Let `p` be odd and `H <= F_p^*` have order `K>=2`. Then

```text
E_+(A)-(K-1)^2
 <= D_K + (K-1)(K-2)(B(K,p)-4),                    (11)
```

where `D_K` and `B(K,p)` are (10) and the definition below (5). In particular

```text
E_+(A) << K^(8/3) + K^4/p                           (12)
```

with an absolute constant, for every subgroup size.

When (6) holds, the off-diagonal coefficient supplied by the external theorem is

```text
3*cuberoot(32) = 9.524406311809196...
```

before lower-order diagonal terms. This improves the earlier project route with coefficient `192` and its size restrictions, but does not improve the exponent.

For exact integer certificates one may use

```text
B_int(K,p)
 = min(2K,
       max(4, floor(cuberoot(864 K^2)), floor(48 K^2/p))).  (13)
```

Since `N(rho,sigma)` is an integer, replacing `B` by `B_int` in (11) is valid.

## 5. Verification

`computations/verification/cayley_curve_uniform.py` checks with exact symbolic arithmetic:

- bidegree `(2,2)`;
- the quartic discriminant-of-discriminant identity (2);
- all four boundary gradients (3);
- diagonal factorization (8);
- the exact restoration identity (7);
- the diagonal sum (9);
- the integer form (13) against direct finite-field energies.

The committed dated certificate runs all subgroup orders `K>=3` occurring for odd primes `p<=257`: 338 exact designs, including 114 odd and 224 even orders, with maximum tested order 256. These finite checks are evidence about algebra and implementation, not a proof of Corvaja--Zannier or of the growing-parameter theorem.

## 6. Boundary of the result

The theorem is a worst-curve estimate summed over `O(K^2)` parameter pairs. It therefore remains at the `K^(8/3)` scale. Reaching the centered target

```text
E_+(A)=(K-1)^4/p + O(K^(2+o(1)))
```

still requires correlation across the specific two-parameter family, stronger arithmetic support control, or another mechanism. Fourth-moment energy control is not a CLT and not a local eigenphase law.