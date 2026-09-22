---
title: "The exact second-resonance minimum on one Fourier orbit"
author: "BGS research programme"
date: "5 September 2026"
---

# Scope and notation

This note generalizes [the Pell-only sharp theorem](pell_single_orbit_sharp_constant.md)
already recorded in the project. That earlier theorem already solves
real autocorrelation realizability for the Pell matrix; this is not counted
as a new achievement here. The present proof applies to **every** hyperbolic
matrix $A\in\mathrm{SL}(2,\mathbb Z)$ and supplies independent exact checks
for four matrices, a different uniform positivity argument, and numerical
real spectral factors.
It is a project proof; priority and external referee acceptance are not claimed.
Its spectral-factorization step is the classical Fejer--Riesz theorem, not a
new factorization theorem.

We may assume $\operatorname{tr}A>2$: replacing A by -A leaves its action on
even cosine observables unchanged. Write $\lambda>1$ for its expanding
eigenvalue, $b_v(x)=2\cos(2\pi v\cdot x)$, and
$\mathcal C_A b_v=b_{Av}$. In particular
$\lambda\geq(3+\sqrt5)/2>2$.
For a real even trigonometric polynomial h of zero mean define
$$
 \sigma_A^2(h)=2\sum_{\mathcal O}
          \left(\sum_{w\in\mathcal O/\{\pm1\}}a_w(h)\right)^2,
 \qquad
 \Gamma_A(g)=\sigma_A^2\!\left(\frac{\{g,\mathcal C_Ag\}}{4\pi}\right),
$$
where $a_w$ is the coefficient of $b_w$ and $\mathcal O$ ranges over the
signed A-orbits. This is the finite-Fourier Green--Kubo form.

Fix $v\in\mathbb Z^2\setminus\{0\}$ and consider
$$
 g=\sum_{j\in\mathbb Z}c_jb_{A^jv},\qquad c_j\in\mathbb R,
 \qquad C_r=\sum_jc_jc_{j+r},\qquad d_r=\det(v,A^rv).
$$
The coefficients have finite support. We write its diameter as at most L:
after an integer translation all nonzero coefficients lie in $0\leq j\leq L$.
The number $d_1$ is nonzero: otherwise v is a rational eigendirection of a
hyperbolic determinant-one integral matrix, which is impossible.
Set
$$
 M=\lfloor L/2\rfloor,\qquad
 S_M=\sum_{k=0}^M d_{2k+1}^{-2},\qquad
 S_\infty=\sum_{k=0}^{\infty}d_{2k+1}^{-2}.
$$

# The sharp variational theorem

**Theorem 1.** For every L and every prescribed $C_0=c>0$,
$$
 \boxed{\displaystyle
 \min_{\substack{\operatorname{diam}(\operatorname{supp}c_j)\leq L\\
                 \sum_jc_j^2=c}}
       \Gamma_A(g)=\frac{4\pi^2c^2}{S_M}.}                 \tag{S1}
$$
The minimum is attained by a real sequence supported on the even indices
$0,2,\ldots,2M$. All minimizing autocorrelation sequences are specified by
$$
 C_{2k}=c\,\frac{\sum_{j=k}^M d_{2j+1}^{-2}}{S_M}
          \quad(0\leq k\leq M),\qquad C_{2k+1}=0.           \tag{S2}
$$
Terms beyond the support are zero. There may be more than one coefficient
sequence with these autocorrelations; uniqueness of the coefficients is not
asserted.

Consequently the infimum over all nonzero finite single-orbit polynomials is
$$
 \boxed{\displaystyle
 \inf_g\frac{\Gamma_A(g)}{\|g\|_2^4}
                   =\frac{\pi^2}{S_\infty}.}               \tag{S3}
$$
No finite sequence attains (S3), because $S_M<S_\infty$ for every finite M.
This statement concerns all finite support lengths, not the existence or
regularity of a minimizer in an infinite-frequency function space.

# Step 1: the exact orbit identity

Direct differentiation yields
$$
 \frac{\{b_u,b_w\}}{4\pi}
        =\pi\det(u,w)(b_{u-w}-b_{u+w}).
$$
Combining the terms from times j and j+r in $\{g,\mathcal C_Ag\}$ gives,
for $r\geq1$, coefficient
$\pi d_r(c_jc_{j+r-1}-c_{j+r}c_{j-1})$ on the orbit represented by
$v-A^rv$, and its negative on that represented by $v+A^rv$.
The orbit sums of these coefficients are
$\pm\pi d_r(C_{r-1}-C_{r+1})$.

It is necessary to check that these generated orbits do not coalesce. Define
$Q_A(w)=\det(w,Aw)$, invariant under $w\mapsto\pm Aw$. Since $I\pm A^r$
commutes with A,
$$
 Q_A(v\pm A^rv)=\det(I\pm A^r)Q_A(v)
             =(2\pm(\lambda^r+\lambda^{-r}))Q_A(v).        \tag{S4}
$$
For $r\geq1$ these values have opposite signs for the two choices. Within
each sign their absolute values are strictly increasing with r. All generated
orbits in question are therefore distinct. The variance formula gives exactly
$$
 \boxed{\displaystyle
 \Gamma_A(g)=4\pi^2\sum_{r\geq1}
                    d_r^2(C_{r-1}-C_{r+1})^2.}             \tag{S5}
$$
This proves the identity for a general A; no special quadratic-ring coordinate
system for the Pell example is needed.

# Step 2: a lower bound with an exact equality condition

The even autocorrelations telescope:
$$
 C_0=\sum_{k=0}^{M}(C_{2k}-C_{2k+2}).
$$
Cauchy--Schwarz with weights $d_{2k+1}^2$ gives
$$
 C_0^2\leq S_M\sum_{k=0}^Md_{2k+1}^2(C_{2k}-C_{2k+2})^2.
$$
The omitted even-r terms in (S5) are nonnegative. Therefore (S1)'s right
side is a lower bound. Equality in the weighted inequality requires
$$
 C_{2k}-C_{2k+2}=\frac{C_0}{S_Md_{2k+1}^2}.
$$
Equality in the omitted terms requires all successive odd autocorrelations to
be equal, hence zero by finite support. These are precisely (S2).

A lower bound alone does **not** solve the problem: the desired sequence
of C's must be realizable as the autocorrelation of real finite coefficients.
That constraint is checked next.

# Step 3: positive spectral density and a real spectral factor

Cayley--Hamilton gives
$$
 \frac{d_r}{d_1}=
 \frac{\lambda^r-\lambda^{-r}}{\lambda-\lambda^{-1}}.
$$
Let $q=\lambda^{-4}<1/16$. The positive inverse weights $u_k=d_{2k+1}^{-2}$
satisfy $u_{k+1}<q u_k$. Define the normalized targets
$$
 a_k=\frac{\sum_{j=k}^M u_j}{S_M},\qquad a_0=1.
$$
Termwise comparison of the tails gives $0\leq a_k\leq q^k$. Hence the real
Laurent polynomial
$$
 P_M(z)=1+\sum_{k=1}^M a_k(z^k+z^{-k})
$$
is strictly positive on the unit circle, with the explicit bound
$$
 P_M(e^{i\theta})\geq1-\frac{2q}{1-q}>0.                    \tag{S6}
$$
The classical Fejer--Riesz theorem provides a polynomial
$p_M(z)=\sum_{j=0}^M b_jz^j$ with $P_M(e^{i\theta})=|p_M(e^{i\theta})|^2$.
It can be chosen with real coefficients. To see the real property directly,
consider $z^MP_M(z)$: its coefficients are real and its zeros come in conjugate
and reciprocal-conjugate pairs, with no zero on the unit circle. Choosing
one complete conjugation-invariant side of each reciprocal pair gives a real
factor, up to a real normalization. This is also a consequence of uniqueness
of the outer factor with positive value at zero.

Set $c_{2j}=\sqrt c\,b_j$ and $c_{2j+1}=0$. Comparing the Laurent
coefficients in $|p_M|^2=P_M$ shows that its autocorrelations are exactly
(S2), including $\sum c_j^2=c$. Thus the lower bound is attained. This
completes (S1), and the monotone limit in M proves (S3).

A primary account of the factorization theorem is Dritschel and Rovnyak,
*The Operator Fejer--Riesz Theorem*, [arXiv:0903.3639](https://arxiv.org/abs/0903.3639),
Section 1. Only its scalar, one-variable theorem is used here.

# Explicit examples and a tail estimate

For the Pell matrix $A=\left(\begin{smallmatrix}3&2\\4&3\end{smallmatrix}\right)$,
$v=(1,0)$, we have $d_1=4$ and
$$
 d_r=4s_r,\qquad s_0=0,\quad s_1=1,\quad s_{r+1}=6s_r-s_{r-1}.
$$
For L=2 or 3, $s_3=35$, so the sharp ratio to the single-mode value is
$$
       \frac{1}{d_1^2S_1}=\frac{1225}{1226}.                 \tag{S7}
$$
The minimizing coefficients can be chosen at times 0 and 2. Put $a=1/1226$,
$$
 c_0=\sqrt{\frac{1+\sqrt{1-4a^2}}{2}},\qquad
 c_2=\frac a{c_0},\qquad c_1=0.
$$
They have $C_0=1$ and $C_2=a$, and attain (S1). Thus the assertion that a
single mode minimizes Gamma at fixed L2 norm would already be false at L=2.

The all-length infimum has ratio
$$
 \frac{1}{d_1^2S_\infty}
  =0.999183632503157206914040180941060306\ldots .             \tag{S8}
$$
The displayed number is high-precision arithmetic, not interval-certified
rounding. An analytic positive tail bound is
$$
 0<S_\infty-S_M
   \leq \frac{d_{2M+3}^{-2}}{1-\lambda^{-4}}
   \leq\frac{\lambda^{-4(M+1)}}{d_1^2(1-\lambda^{-4})}.       \tag{S9}
$$
Inverting $S_M$ and $S_M$ plus this upper bound brackets the sharp constant
in exact real arithmetic.

For the trace-three cat matrix $\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)$
and $v=(1,0)$, the L=2 ratio is $64/65$. The phenomenon and its proof are not
peculiar to the Pell recurrence.

# Verification and boundaries

The Python checker first builds the full Poisson-bracket Fourier polynomial,
reduces its frequency orbits by exact integer neighbour descent, and compares
the variance to (S5). The C++ checker instead represents frequencies in a
quadratic ring and uses a finite exhaustive orbit window, with a boundary
failure check. They agree on 726 exact Pell cases. Python independently checks
720 additional exact cases for three other hyperbolic matrices. Rational
arithmetic verifies the finite optimizer energy and strict positivity at
nine support lengths. Six real spectral factors are additionally constructed
with 100-digit arithmetic; these numerical roots are not the existence proof.

This theorem does not solve the variational problem for arbitrary unions of
frequency orbits. In that case the values in (S4) can overlap and the squared
orbit sums must include cross-orbit cancellations. It also does not prove
random-matrix statistics of quantum spectra. Its completed content is the
sharp, attained finite-support extremum and the sharp all-length infimum.
