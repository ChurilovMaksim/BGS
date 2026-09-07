# Generic infinite-support resonance nondegeneracy in weighted Wiener spaces

**Status: EXACT.** This is a topological consequence of the unrestricted finite-Fourier theorem plus the weighted-Wiener bracket estimate. It proves open-dense nondegeneracy for a natural infinite-support Banach class and for every fixed analytic Wiener strip. It does **not** prove that every analytic observable is nondegenerate.

Fix a hyperbolic `A in SL(2,Z)`. For a Fourier series `f` define

```text
M_0(f)=sum_v ||v||_1 |f^(v)|,
M_A(f)=sum_v ||A v||_1 |f^(v)|,
||f||_X=|f^(0)|+M_0(f)+M_A(f).                          (1)
```

Let `X_A` be the real Banach space of Fourier series for which (1) is finite. Since `A` is invertible, `M_0` and `M_A` are equivalent first-moment seminorms; the constant mode is included only to make a genuine norm. The resonance functional is invariant under adding constants.

Put

```text
B_A(f,g)={f,C_A g}/(4*pi),
h_g=B_A(g,g),
P h = (sum_(k in O) h^(k))_O,
Gamma_A(g)=||P h_g||_ell2(O)^2.                         (2)
```

## 1. Continuity of the orbit-sum map

For every absolutely summable Fourier sequence `h^`, the oriented orbits partition `Z^2\{0}`, hence

```text
||P h||_ell2 <= ||P h||_ell1 <= ||h^||_ell1.            (3)
```

The weighted-Wiener bracket estimate is

```text
||B_A(f,g)^||_ell1 <= pi M_0(f) M_A(g).                 (4)
```

Therefore

```text
h_g-h_f=B_A(g-f,g)+B_A(f,g-f)
```

and

```text
|| (h_g-h_f)^ ||_ell1
 <= pi [M_0(g-f) M_A(g)+M_0(f) M_A(g-f)].               (5)
```

Equations (3)--(5) show that

```text
g -> P h_g in ell2(O)
```

is continuous on `X_A`. Consequently `Gamma_A` is a continuous nonnegative functional on `X_A`.

## 2. Open-dense theorem

### Theorem

The set

```text
N_A={g in X_A : Gamma_A(g)>0}                            (6)
```

is open and dense in `X_A` modulo constants. Equivalently, the exact-cancellation set

```text
Z_A={g in X_A : Gamma_A(g)=0}                            (7)
```

is closed and nowhere dense.

### Proof

Openness of (6) follows immediately from continuity of `Gamma_A` and the fact that `(0,infinity)` is open.

For density, Fourier truncations converge in the norm (1): if

```text
p_R=sum_(||v||_1<=R) g^(v)e_v,
```

then absolute convergence of the two weighted first moments gives

```text
||g-p_R||_X -> 0.                                       (8)
```

If `g` is nonconstant, `p_R` is nonconstant for all sufficiently large `R`. The unrestricted finite-Fourier theorem then gives

```text
Gamma_A(p_R)>0.                                         (9)
```

Thus every neighbourhood of every nonconstant `g` contains a member of `N_A`. A constant can likewise be approximated by adding an arbitrarily small nonzero cosine mode, which is again covered by the finite theorem. Hence `N_A` is dense. Since its complement is closed and has empty interior, (7) is nowhere dense.

## 3. Fixed analytic Wiener strips

For `rho>0`, define the real analytic Wiener space

```text
X_rho={f: ||f||_rho=sum_v exp(rho ||v||_1)|f^(v)|<infinity}.  (10)
```

The embedding `X_rho -> X_A` is continuous because

```text
M_0(f) <= C_rho ||f||_rho,
M_A(f) <= ||A||_(1->1) C_rho ||f||_rho,
C_rho=sup_(n>=1) n exp(-rho n)<infinity.                (11)
```

Finite trigonometric polynomials are dense in `X_rho`. The same proof therefore gives:

### Corollary

For every `rho>0`, the set

```text
{g in X_rho : Gamma_A(g)>0}
```

is open and dense in `X_rho` modulo constants. Its zero-variance complement is closed and nowhere dense.

Any function holomorphic in a strictly wider complex strip belongs to `X_rho` after shrinking the strip width, so the corollary applies to the usual nested analytic scales.

## 4. What this settles and what remains open

The project now has three distinct levels:

```text
all nonconstant finite Fourier symbols:       Gamma_A>0;
weighted-Wiener / fixed analytic strip:       Gamma_A>0 generically (open dense);
arbitrary nonconstant analytic symbol:        still OPEN.
```

Thus smooth or analytic exact cancellations, if they exist in these Banach classes, are topologically unstable: they cannot contain any open set. What remains unresolved is an all-members theorem for analyticity alone, or a construction of an analytic exact-cancellation counterexample.

This result is classical-topological and does not by itself imply Heisenberg-scale trace statistics or microscopic BGS universality.
