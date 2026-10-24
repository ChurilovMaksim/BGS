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

Then there is an analytic transfer `u`, unique among analytic transfers modulo constants, such that

```text
h=u-C_A u,                                              (5)
```

More quantitatively, fix the covectors defining `N_A` and put

```text
m_A = inf_(k in Z^2\{0}) N_A(k) >= c_A > 0,
d = (lambda+lambda^(-1))/2-1 = |tr A|/2-1 > 0.
```

Then

```text
|uhat(k)| <= M' exp(-rho N_A(k)),                      (6)
M' = M/[1-exp(-rho d m_A)].
```

Thus the full adapted Fourier exponent survives. This is an estimate in the
coefficient class (3); no claim about preservation of a boundary supremum norm
of a holomorphic extension is needed.

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

If `j>=j_*`, then `X_j>=Y_j`. For every integer `n>=0`,

```text
N_A(k_(j+n))/N_A(k_j)
 = (lambda^n X_j+lambda^(-n)Y_j)/(X_j+Y_j)
 >= (lambda^n+lambda^(-n))/2
 >= 1+n d.                                              (9)
```

The first inequality follows by subtracting the right side: the difference is
`(X_j-Y_j)(lambda^n-lambda^(-n))/(2(X_j+Y_j))>=0`.
For the second, put `a_n=(lambda^n+lambda^(-n))/2`. Its successive
increments are nondecreasing, since
`a_(n+2)-2a_(n+1)+a_n`
equals
`[lambda^n(lambda-1)^2+lambda^(-n)(lambda^(-1)-1)^2]/2>=0`.
Thus `a_n>=a_0+n(a_1-a_0)=1+n d`.

If `j<j_*`, then `Y_j>X_j`; interchanging `X_j,Y_j` gives

```text
N_A(k_(j-n)) >=(1+n d) N_A(k_j),  n>=0.                (10)
```

Condition (4) permits the same coefficient to be written using either tail:

```text
u_j=sum_(ell<=j) h_ell = -sum_(ell>j) h_ell.             (11)
```

Then `h_j=u_j-u_(j-1)`, which is exactly the Fourier form of (5).

For `j>=j_*`, use the forward tail in (11). By (3) and (9),

```text
|u_j| <= M sum_(n>=1)
              exp[-rho (1+n d) N_A(k_j)].              (12)
```

For `j<j_*`, use the backward tail and (10):

```text
|u_j| <= M sum_(n>=0)
              exp[-rho (1+n d) N_A(k_j)].              (13)
```

Since `N_A(k)>=m_A>0` on nonzero integer frequencies, both sums are bounded by

```text
M exp[-rho N_A(k_j)]/[1-exp(-rho d m_A)].               (14)
```

This proves (6) uniformly over all frequency orbits. The exponential bound makes the Fourier series of `u` real analytic. If `h` is real then the decaying solution respects conjugation and `u` may be chosen real.

If two analytic transfers differ, their difference is `C_A`-invariant. On each nonzero frequency orbit invariance would make all Fourier coefficients equal; exponential decay forces them to vanish. Hence the difference is constant.

## Corollary for the analytic resonance problem

Let `g` be real analytic and

```text
h_g={g,C_A g}/(4*pi).
```

Then `h_g` is real analytic and has zero mean, because the integral of a
periodic Poisson bracket vanishes by integration by parts. The orbit-sum
variance identity also holds for analytic observables, not just polynomials.
Indeed, for a mean-zero analytic `h`, absolute Fourier summability and the
absence of nonzero periodic frequencies give

```text
sum_(q in Z) |<C_A^q h,h>|
 <= sum_O (sum_(k in O) |hhat(k)|)^2
 <= (sum_(k != 0) |hhat(k)|)^2 < infinity.
```

Absolute convergence permits rearrangement by orbit. Expanding the squared
norm of `sum_(j=0)^(n-1) C_A^j h` and taking its normalized limit therefore gives
`sum_O |sum_(k in O) hhat(k)|^2`. In particular, if

```text
Gamma_A(g)=0,
```

all oriented frequency-orbit sums of `h_g` vanish. The theorem therefore produces a real-analytic `u` such that

```text
{g,C_A g}/(4*pi)=u-C_A u.                               (15)
```

Combined with `foundations/analytic_bracket_rigidity.md`, every hypothetical nonconstant real-analytic zero-variance observable must satisfy (15) with a **nonzero** analytic left side. The pointwise-zero Gevrey mechanism is impossible in the analytic category.

In ordinary `l1` frequency coordinates, (2) converts any bound

```text
|hhat(k)|<=M exp(-r ||k||_1)
```

into (6) with an explicit positive reduced exponent, for example

```text
|uhat(k)| <= M' exp[- r c_A/C_A ||k||_1].              (16)
```

The remaining all-analytic question is therefore a nonlinear analytic cohomological-rigidity problem, not a regularity problem for the transfer.

## Exact finite regression

Run `python3 computations/verification/analytic_coboundary.py`. The dependency-free
check verifies the scalar growth inequality through exact Chebyshev recurrences
and Laurent-polynomial identities on stated finite ranges, and checks an exact
negative-trace counterexample to replacing frequency orbits of `A` by those of
`-A`. It also checks the transfer recurrence on finite zero-sum data. These
regressions protect the proof conventions; the universal estimates above are
proved analytically, not extrapolated from computation.
