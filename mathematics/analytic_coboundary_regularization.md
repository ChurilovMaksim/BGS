# Analytic regularity of the hyperbolic orbit-sum coboundary

**Status: EXACT.** This is a direct Fourier proof for hyperbolic toral automorphisms. It upgrades the zero-orbit-sum criterion from an `L2` statement to an analytic transfer statement. The result is standard in spirit as a Livsic-type regularity phenomenon; no external priority claim is made.

Let `A in SL(2,Z)` be hyperbolic and let `C_A f=f o A^T`. Frequencies are transported by `A`. Put `s=sign(tr A)`, `B=sA`, and let `lambda>1` be the expanding eigenvalue of `B`. Choose real eigen-covectors `xi,eta` such that

```text
xi(Bk)=lambda xi(k),
eta(Bk)=lambda^(-1) eta(k).
```

Define the adapted frequency norm

```text
N_A(k)=|xi(k)|+|eta(k)|.                                (1)
```

Because `xi,eta` are independent, there are constants `0<c_A<=C_A<infinity` with

```text
c_A ||k||_1 <= N_A(k) <= C_A ||k||_1.                  (2)
```

For `rho>0`, let `A_rho(N_A)` denote the Fourier class satisfying

```text
|hhat(k)| <= M exp(-rho N_A(k))                         (3)
```

for some `M` and every nonzero integer `k`.

## Theorem

Let `h` have zero mean and satisfy (3). Assume that on every oriented `A`-orbit `O` in `Z^2\{0}`,

```text
sum_(k in O) hhat(k)=0.                                 (4)
```

Then there is a transfer `u`, unique modulo constants, such that

```text
h=u-C_A u,                                              (5)
```

and `u` is analytic. More quantitatively, there is a constant `M'`, depending only on `A,rho,M`, such that

```text
|uhat(k)| <= M' exp(-(rho/2) N_A(k)).                   (6)
```

Thus an exponential Fourier strip survives, with at most a factor-two loss in the adapted exponent.

## Proof

Fix one oriented frequency orbit and write

```text
k_j=A^j k_0,
h_j=hhat(k_j).
```

The eigen-covector absolute values satisfy

```text
X_j=|xi(k_j)|=lambda^j X_0,
Y_j=|eta(k_j)|=lambda^(-j)Y_0,                           (7)
```

because the sign `s^j` is irrelevant. A nonzero integer frequency lies on neither irrational eigenline, so `X_j,Y_j` are positive.

Choose the unique switching integer `j_*` such that

```text
X_(j_*) >= Y_(j_*),
X_(j_*-1) < Y_(j_*-1).                                  (8)
```

If `j>=j_*`, then `X_j>=Y_j`, hence `N_A(k_j)<=2X_j`, and for every `n>=0`,

```text
N_A(k_(j+n)) >= X_(j+n)
                  =lambda^n X_j
                  >=(lambda^n/2) N_A(k_j).              (9)
```

If `j<j_*`, then `Y_j>X_j`, and similarly

```text
N_A(k_(j-n)) >=(lambda^n/2) N_A(k_j),  n>=0.            (10)
```

Condition (4) permits the same coefficient to be written using either tail:

```text
u_j=sum_(ell<=j) h_ell = -sum_(ell>j) h_ell.             (11)
```

Then `h_j=u_j-u_(j-1)`, which is exactly the Fourier form of (5).

For `j>=j_*`, use the forward tail in (11). By (3) and (9),

```text
|u_j| <= M sum_(n>=1)
              exp[-(rho/2) lambda^n N_A(k_j)].           (12)
```

For `j<j_*`, use the backward tail and (10):

```text
|u_j| <= M sum_(n>=0)
              exp[-(rho/2) lambda^n N_A(k_j)].           (13)
```

By (2), `N_A(k)>=c_A` for every nonzero integer `k`. Since `lambda^n>=1+n(lambda-1)`, both sums are bounded by a constant depending only on `A,rho` times

```text
exp[-(rho/2) N_A(k_j)].                                 (14)
```

This proves (6) uniformly over all frequency orbits. The exponential bound makes the Fourier series of `u` real analytic. If `h` is real then the decaying solution respects conjugation and `u` may be chosen real.

If two analytic transfers differ, their difference is `C_A`-invariant. On each nonzero frequency orbit invariance would make all Fourier coefficients equal; exponential decay forces them to vanish. Hence the difference is constant.

## Corollary for the analytic resonance problem

Let `g` be real analytic and

```text
h_g={g,C_A g}/(4*pi).
```

Then `h_g` is real analytic and has zero mean. If

```text
Gamma_A(g)=0,
```

all oriented frequency-orbit sums of `h_g` vanish. The theorem therefore produces a real-analytic `u` such that

```text
{g,C_A g}/(4*pi)=u-C_A u.                               (15)
```

Combined with `analytic_bracket_rigidity.md`, every hypothetical nonconstant real-analytic zero-variance observable must satisfy (15) with a **nonzero** analytic left side. The pointwise-zero Gevrey mechanism is impossible in the analytic category.

In ordinary `l1` frequency coordinates, (2) converts any bound

```text
|hhat(k)|<=M exp(-r ||k||_1)
```

into (6) with an explicit positive reduced exponent, for example

```text
|uhat(k)| <= M' exp[- r c_A/(2 C_A) ||k||_1].           (16)
```

The remaining all-analytic question is therefore a nonlinear analytic cohomological-rigidity problem, not a regularity problem for the transfer.
