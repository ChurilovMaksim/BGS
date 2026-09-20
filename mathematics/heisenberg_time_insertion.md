# Coherent time summation for Liouville insertions

Status: internal deterministic proof and counterexamples, 2026-09-16.
Base: `18bb3c7`. This is a sufficient mechanism for a missing BGS estimate,
not a verification of that mechanism for the fixed nonlinear map.
No priority claim is made.

## 1. Exact objects

Let U be N-dimensional unitary, N>2, with phases theta_j in R/Z.
On the N^2-dimensional Hilbert space of matrices put A=Ad_U. For w in
C_c^infinity(R), define the normal operator

```text
T_w(t) = sum_(m in Z) w(m/N) exp(2 pi i t m/N) A^m.
```

The trace and trace norm below are on Liouville space. Let mu_N be the
positive anchored factorial pair measure from
`bandlimited_correlation_extension.md`, and put B_N=mu_N([-2,2]).
That note proves the finite bound

```text
sup_x mu_N([x,x+1)) <= 8(1+B_N).                    (1)
```

The coefficient 8 is its k=2 specialization. Multiplicities are allowed.

## 2. A trace-norm bound uniform in modulation

For every fixed w there is C_w independent of N,U and real t such that

```text
||T_w(t)||_1 <= C_w N^2 (1+B_N).                  (2)
```

**Proof.** On the eigenmatrix |j><k| the eigenvalue is

```text
sum_m w(m/N) exp(2 pi i m(theta_j-theta_k+t/N))
 = N sum_l what(N l-N(theta_j-theta_k)-t).
```

Use the triangle inequality only after this exact time summation. Define
the positive lifted measure including equal labels,

```text
nu_N = mu_N + sum_(l in Z) delta_(N l).
```

It is (1/N) times the full ordered-pair lift measure. Consequently

```text
N^-2 ||T_w(t)||_1 <= integral |what(-x-t)| d nu_N(x).
```

By (1), nu_N has uniformly bounded mass per unit interval, at most
C(1+B_N), since N>2. Partition the real line into intervals translated by
-t and sum the Schwartz suprema of what on unit intervals. The sum is
finite and independent of t. This proves (2). It is valid for complex w
and includes the m=0 term. No phase cancellation between eigenmatrices is
assumed. `□`

The ambient-dimension estimate would give O(N^3). The improvement here
comes from the *summed spectral kernel* and requires a local pair bound.
It does not follow just from unitarity.

## 3. Time-dependent insertions: discrete Wiener criterion

Fix sigma with supp(w) contained in [-sigma,sigma]. Let L>2 sigma N+1
be an integer. For a periodic operator array E_m of period L define

```text
Ehat_r=(1/L) sum_(m=0)^(L-1) E_m exp(-2 pi i r m/L),
W(E)=sum_(r=0)^(L-1) ||Ehat_r||op.
```

Then the exact bound is

```text
|N^-2 sum_m w(m/N) Tr(E_m A^m)|
 <= C_w (1+B_N) W(E).                             (3)
```

**Proof.** Insert finite Fourier inversion
`E_m=sum_r Ehat_r exp(2 pi i r m/L)`. The sum over m becomes
`Tr(Ehat_r T_w(r N/L))`. Apply trace-norm duality and (2), which is uniform
in r. The chosen period prevents unintended identifications of the sampled
time values on the support; periodicity outside that support is just an
extension convention. `□`

A directly checkable sufficient condition is

```text
sup_m ||E_m||op + L^2 sup_m ||E_(m+2)-2E_(m+1)+E_m||op -> 0.   (4)
```

Indeed, the zero Fourier coefficient has norm at most sup||E_m||, and for
r nonzero,

```text
||Ehat_r|| <= sup||Delta^2 E|| / (4 sin^2(pi r/L)).
```

Using sin(pi r/L)>=2 min(r,L-r)/L and summing the convergent inverse-square
series yields `W(E)<=sup||E||+C L^2 sup||Delta^2 E||`. This bound uses the
operator norm directly; it has no factor from Hilbert-space dimension.
For a fixed-length periodic C^2 family E_N(s), sampled at s=m/N and with
L=O(N), it suffices that its C^2 operator norm tends to zero.

This is a regularity condition in *rescaled time*, not merely regularity
of an FIO symbol in phase space. The distinction is essential.

## 4. Positive bootstrap: the local pair bound need not be assumed

The apparent circularity in (3) can be removed under an explicit
representation hypothesis.

Choose a real, nonnegative, nonzero eta in C_c^infinity with support close
enough to zero that its Fourier transform does not vanish on [-2,2].
Set

```text
w_0=eta * eta_tilde,   eta_tilde(t)=eta(-t),
chi=what_0=|eta_hat|^2 >= 0,
c_0=min_[-2,2] chi > 0.
```

The support of w_0 can be made to fit any fixed positive time window by
shrinking the support of eta further. Then exactly, by the same Poisson
identity,

```text
Q_N := N^-2 sum_m w_0(m/N) |Tr U^m|^2
     = integral chi(x) d nu_N(x) >= c_0 B_N.       (5)
```

In particular Q_N is real and nonnegative. Suppose on the support of w_0
one has an exact decomposition

```text
|Tr U^m|^2 = b_(m,N) + Tr(E_(m,N) A^m) + r_(m,N),  (6)
```

with the following three independently checkable hypotheses:

```text
|N^-2 sum_m w_0(m/N) b_(m,N)| <= C_0,
N^-2 |sum_m w_0(m/N) r_(m,N)| -> 0,
W(E_N) -> 0.
```

Equations (3) and (5) imply

```text
Q_N <= C_0+o(1)+C W(E_N)(1+Q_N/c_0).
```

For all sufficiently large N the coefficient of Q_N on the right is less
than 1/2. Absorb it to obtain `sup_N Q_N<infinity`, hence `sup_N B_N<infinity`.
Equation (3) then proves that the insertion contribution tends to zero for
any other fixed test w with its own vanishing Wiener budget. There is no
additional time-count factor N.

Thus, if (6) with these hypotheses and a known main term were established
for the fixed quantum map, it would close the indicated weighted pair
window. The bootstrap uses one positive window around zero. A result only
for weights supported away from zero does *not* supply its hypotheses.
For the CUE candidate, set b_(0,N)=N^2 explicitly; one must not use
min(|m|,N) at m=0. An unistochastic ramp term for m!=0 can be used only after
its requisite mixing estimate is proved for the actual quantization.

## 5. Two exact obstruction tests

### Unitarity alone does not bound the summed kernel

Take U=I_N. All N^2 eigenmatrices have phase difference zero. For w>=0
nonzero near zero,

```text
||T_w(0)||_1=N^2 sum_m w(m/N) ~ N^3 integral w.
```

Here B_N=N-1, so (2) has the right order. Dropping the local-pair or
bootstrap hypothesis would make the theorem false.

### Small norm alone does not control a time-varying insertion

Let U be the simple unit clock, whose B_N is bounded. For an integer time m
put `E_m=epsilon_N A^(-m)`. This is periodic with period N (or any integer
multiple of N), and `||E_m||=epsilon_N`. Nevertheless

```text
N^-2 Tr(E_m A^m)=epsilon_N,
N^-2 sum_m w(m/N) Tr(E_m A^m)
 = epsilon_N sum_m w(m/N) ~ N epsilon_N integral w.
```

Its finite Fourier coefficients are epsilon_N times the N distinct spectral
projections of A, all nonzero. Consequently

```text
W(E)=N epsilon_N.
```

The proposed criterion detects exactly the lost factor. Even for a
simple, locally bounded spectrum, a merely o(1) norm insertion need not be
negligible. This also precludes a universal repair using only first-witness
HS budgets and unitarity.

## 6. Attempt to connect this mechanism to the fixed-map proof

Executed routes and current outcomes:

1. Remove the factor by unitarity alone: refuted by the identity spectrum;
   even adding bounded local correlations fails for arbitrary time-dependent
   insertions, by the clock example above.
2. Sum coherently first: (2)–(4) prove a valid mechanism with a precise
   discrete Fourier/operator regularity budget.
3. Eliminate an assumed local pair bound: (5)–(6) give an absorption argument.
   This avoids assuming the very spectral boundedness one hopes to prove.

The model-specific remaining statement is not supplied by the upload's
Parseval/Stinespring identities: one must express its *coherent noncyclic
remainder* in form (6), with small W(E_N), or prove an equally strong
signed time-summed estimate directly. The first-witness location depends
on m; current phase-space derivative bounds do not bound Delta_m^2 E.
No such representation or estimate has been proved for the frozen map.

There is therefore no claim of pair BGS, much less all-k universality.
A successful pair theorem would still require an additional all-k
joint-trace argument. The exact formulas and counterexamples here specify
what an attempted cancellation argument must actually control.

## 7. Reproducible diagnostic and what it rules out

`computations/verification/heisenberg_time_insertion.py` performs exact
finite spectral sums in floating-point arithmetic, with seed 20260916.
It checks Fourier inversion, trace reconstruction, and the projection
counterexample's identity W(E)=N epsilon. No stochastic trace estimation is
used. Four clock dimensions and sixteen model instances were executed.

For the model comparison it uses the *canonical diagnostic insertion*

```text
E_m=chi(m/N) R_m A^(-m)/N^2,
R_m=|Tr U^m|^2-min(|m|,N) for m!=0, R_0=0,
```

with a fixed smooth cutoff chi supported in (-0.4,0.4). This is a tautological
representation, not a dynamical derivation. Its Fourier coefficients are
computed on period L=2N+1. The following Wiener budgets were observed:

| N | Clock | Linear cat | Two Haar controls (range) |
|---|---:|---:|---:|
| 15 | 0.05965 | 0.02929 | 0.04418–0.04954 |
| 31 | 0.06011 | 0.03573 | 0.02354–0.02428 |
| 63 | 0.06024 | 0.98551 | 0.02353–0.02617 |
| 127 | 0.06027 | 0.04547 | 0.01763–0.01861 |

At N=127 the clock insertion has operator sup norm about 0.00113, yet its
weighted residual is about -0.06457. Small insertion norm plainly does not
certify a small form-factor error. Its Wiener budget stays visibly nonzero.
The Haar controls only test that the proposed diagnostic is not immediately
incompatible with familiar random-matrix samples; two samples per dimension
do not establish a rate or a limiting law. The cat data are arithmetic and
nonmonotone. The frozen nonlinear map was not simulated.

### Explicit cost of the tautological representation

For the diagnostic array above, write

```text
F_N(t)=sum_m chi(m/N) R_m exp(-2 pi i m t).
```

Because A is diagonal in the eigenmatrix basis, exactly

```text
||Ehat_r|| = (L N^2)^(-1)
             max_(j,k) |F_N(theta_j-theta_k+r/L)|,
W(E) <= N^-2 sup_(t in R/Z) |F_N(t)|.
```

Therefore a uniform modulated form-factor estimate `sup|F_N|=o(N^2)` would
suffice for the diagnostic criterion, but has not been proved. This exposes
rather than hides the cost of this representation. Merely defining E from
the unknown residual is not a solution; the next proof must exploit genuine
structure of the nonlinear dynamics or its exact quantum generator.
