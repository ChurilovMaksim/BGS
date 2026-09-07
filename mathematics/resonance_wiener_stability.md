# Weighted-Wiener stability of finite-Fourier resonance nondegeneracy

**Status: EXACT + FINITE-REGRESSION.** This is a project theorem derived from the unrestricted finite-Fourier isolated-mode theorem. It extends nondegeneracy to an explicit infinite-support neighbourhood of every nonconstant real trigonometric polynomial. It does **not** prove positivity for every analytic or smooth observable, and no external priority claim is made.

Let `A in SL(2,Z)` be hyperbolic, put `C_A f=f o A^T`, and define

```text
B_A(f,g) = {f,C_A g}/(4*pi),
h_g = B_A(g,g),
Gamma_A(g) = sum_O |sum_{k in O} h_g^(k)|^2,
```

where `O` runs over oriented `A`-orbits in `Z^2\{0}`. For a Fourier series `f`, set

```text
M_0(f) = sum_v ||v||_1 |f^(v)|,
M_A(f) = sum_v ||A v||_1 |f^(v)|.                       (1)
```

Constants do not contribute to either seminorm or to the Poisson bracket.
We work in the weighted Wiener class in which the quantities in (1) are finite.

## 1. Bilinear Wiener bound

The Fourier coefficient of `B_A(f,g)` at `k` is

```text
B_A(f,g)^(k)
 = -pi * sum_{u+A v=k} det(u,A v) f^(u) g^(v).          (2)
```

Since

```text
|det(u,w)| <= ||u||_1 ||w||_1,
```

absolute summation gives

```text
|| B_A(f,g)^ ||_ell1 <= pi M_0(f) M_A(g).               (3)
```

Thus if `M_0(f),M_A(g)<infinity`, the bracket has absolutely summable Fourier coefficients. In particular every oriented orbit sum converges absolutely and `Gamma_A` is well-defined.

## 2. Explicit perturbative stability theorem

Let `p` be a nonconstant real trigonometric polynomial. The unrestricted finite-Fourier theorem supplies support frequencies `u,v` and

```text
k=u+A v
```

such that

1. `k` has a unique ordered decomposition in `supp(p)+A supp(p)`;
2. `d=|det(u,A v)|>=1`;
3. `A^j k` does not belong to `supp(p)+A supp(p)` for any nonzero integer `j`.

Hence the `A`-orbit of `k` contains exactly one Fourier coefficient of `h_p`, namely

```text
|h_p^(k)| = pi D,
D = d |p^(u) p^(v)| > 0.                               (4)
```

Let now

```text
g=p+r,
P_0=M_0(p),   P_A=M_A(p),
e_0=M_0(r),   e_A=M_A(r).
```

### Theorem (weighted-Wiener stability)

If

```text
E := P_0 e_A + e_0 P_A + e_0 e_A < D,                  (5)
```

then

```text
Gamma_A(g) >= 2 pi^2 (D-E)^2 > 0.                      (6)
```

In particular the resonance variance is strictly positive for every real weighted-Wiener perturbation satisfying (5), even when `r` has infinite Fourier support.

### Proof

By bilinearity,

```text
h_g-h_p = B_A(p,r)+B_A(r,p)+B_A(r,r).
```

Applying (3) term by term gives

```text
|| (h_g-h_p)^ ||_ell1
 <= pi (P_0 e_A + e_0 P_A + e_0 e_A)
 = pi E.                                                (7)
```

Let `O(k)` be the oriented orbit of the isolated finite-support witness. By (4),

```text
sum_{q in O(k)} h_p^(q)=h_p^(k),
|h_p^(k)|=pi D.
```

The perturbation of that orbit sum is bounded by its global Fourier `ell1` norm, so (7) yields

```text
|sum_{q in O(k)} h_g^(q)| >= pi(D-E)>0.                 (8)
```

For real `g`, the orbit of `-k` has the conjugate orbit sum and is distinct from `O(k)` because a hyperbolic integer matrix has no nonzero vector satisfying `A^j k=-k`. Therefore those two oriented orbits alone contribute at least

```text
2 pi^2 (D-E)^2
```

to `Gamma_A(g)`. This proves (6).

## 3. A scalar certified radius

Put

```text
P=P_0+P_A,
e=max(e_0,e_A).
```

Then `E<=P e+e^2`. Hence it is enough that

```text
e < e_*(p;u,v),
e_* = (sqrt(P^2+4D)-P)/2.                               (9)
```

The number `e_*>0` is completely explicit once the isolated support witness is chosen. Thus every nonconstant real trigonometric polynomial has a nonempty open weighted-Wiener neighbourhood on which `Gamma_A` is uniformly positive with the quantitative lower bound

```text
Gamma_A(g) >= 2 pi^2 (D-P e-e^2)^2.                    (10)
```

This is stronger than mere continuity of `Gamma_A`: it identifies a single protected orbit and provides a computable coercive margin.

## 4. Analytic and Gevrey corollaries

Every analytic torus function, and more generally every Fourier series with sufficiently fast weighted absolute decay, lies in the class of (1). Consequently:

**Corollary.** Let `p` be a nonconstant real trigonometric polynomial and let `r` be real analytic. If its weighted Fourier tail satisfies (5), then `Gamma_A(p+r)>0`.

For an explicit coefficient envelope

```text
|r^(v)| <= C exp(-rho ||v||_1),                         (11)
```

one may bound `e_0,e_A` by convergent geometric tails. If `r` is supported outside `||v||_1>R`, then, writing

```text
L_A=max_j sum_i |A_ij|
```

for the `ell1` operator norm of `A`,

```text
M_A(r) <= L_A M_0(r),
M_0(r)
 <= 4 C sum_{n=R+1}^infinity n^2 exp(-rho n).           (12)
```

The factor `4 n` is the exact number of lattice points with `||v||_1=n`, and another factor `n` comes from the weight. Inserting (12) into (5) gives a fully explicit analytic-tail sufficient condition.

The conclusion is deliberately local in function space. An arbitrary analytic `g` need not come with a truncation whose isolated witness coefficient dominates its remaining tail. Therefore this theorem does not close the global analytic nondegeneracy question.

## 5. Exact finite regression

`computations/verification/resonance_wiener_stability.py` uses the exact quadratic-field witness implementation from `extremal_resonance.py`. For deterministic real integer Fourier coefficients it checks exactly that

```text
|| (h_(p+r)-h_p)^ / pi ||_ell1 <= E,
|orbit_sum_(O(k))(h_(p+r))/pi| >= D-E,
Gamma_A(p+r)/pi^2 >= 2(D-E)^2.
```

The maintained deterministic regression covers eight hyperbolic matrices, support boxes of radii one through three, and sixteen admitted integer tail multipliers. The finite run audits the algebra and implementation; the theorem itself is the argument above.

## 6. Research consequence

The earlier dichotomy was too coarse:

```text
finite Fourier support: Gamma_A>0,
general smooth support: counterexamples with Gamma_A=0.
```

The correct current picture contains a quantitative intermediate region:

```text
finite polynomial p
    -> explicit protected orbit and margin D
    -> weighted-Wiener ball of infinite-support symbols
    -> Gamma_A>0 throughout that ball.
```

What remains open is not stability but **global coverage**: whether every nonconstant real-analytic observable necessarily enters one of these protected finite-core neighbourhoods, or whether analytic exact cancellations can survive at infinite support.
