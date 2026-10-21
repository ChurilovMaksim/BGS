> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round4_2026_10_21/dual_audit_center_phase_c17.md`. Embedded SHA256: `f9389738b8ff10a520d3c8a9c2d1ad4467e7990273433de4d7e517ccfdd87ad0`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit of the explicit C17 center-phase bound

21 October 2026. Auditor: the Weyl dual-dynamics branch.

Audited source: `counter_center_phase_c17_bound.md`, SHA-256
`992f35db1916f680083fe304caa3001bc71720e2a864f28ea3513f080b5340c5`.
Its definitions and input flow bounds were checked against Sections 1--2 of
`counter_one_step_pinching_hs.md`, SHA-256
`a8babde8cfa7cdf0ef794775ac73672431bd9f9d36491f50e3bf19515543c629`.
Both hashes were verified and neither source was modified.

## Verdict

**The claimed sum of C17 derivative seminorms is proved as stated:**
$$
\sum_{|\alpha|\le17}
\left\|\partial^\alpha\left(S_t/t-a\right)\right\|_\infty
<\frac1{100000}<\frac1{4000},
\qquad t=\frac{10^{-80}}{2\pi}.
$$
The wider strip is justified by the original contraction construction, not by
an unproved extension of a function originally known only on the narrower
strip. The complex Hamilton--Jacobi bound, polydisk Cauchy estimate, count of
multiindices and exact rational arithmetic are all correct.

This audit checks the C17 supplement and the source definitions needed for
it. It does not replace the separate full audit of the source's quantization,
WKB residual, pinching identity or all-time arithmetic-history theorem.

## 1. The inverse midpoint map really exists on the wider strip

The source fixes $\rho=10^{-3}$, $t_0=10^{-10}$ and the analytic flow
$\Phi_s$ of $-J\nabla a$. For initial points in the strip of width rho,
it establishes
$$
\|\Phi_s(y)-y\|_\infty\le200s,
\quad
q_s(y):=(\Phi_s(y)-y)/2,
\quad\|q_s\|_\infty\le100s,
\quad\|Dq_s\|_{\infty\to\infty}\le10^4s\le10^{-6}.
$$
All these bounds use the Hamiltonian coefficients on the wider strip of width
$2\rho$. Let now the endpoint x have coordinate imaginary parts of modulus
at most $3\rho/4$. The closed complex sup-norm ball
$\|y-x\|_\infty\le200s$ is within the initial-point strip because
$$
\frac{3\rho}{4}+200t_0
=\frac3{4000}+\frac2{10^8}
=0.00075002<0.001.
$$
The exact remaining margin is $12499/50000000>0$.

On this ball, the map $y\mapsto x-q_s(y)$ has contraction factor at most
$10^{-6}$, and its image is within distance $100s$ of x, hence remains
inside the ball. It therefore has a unique fixed point $y_s(x)$. Local
uniform convergence of its holomorphic iterations, or the invertibility of
$I+Dq_s$ and the holomorphic implicit equation, proves that $y_s$ is
holomorphic in x throughout the open strip of width $3\rho/4$.
Uniqueness makes these local inverses agree and preserves integer translations.
At s=0 the inverse is the identity. Thus this is a common strip for every
$0\le s\le t_0$.

Composing the source's action integral with this inverse constructs S directly
on the wider strip. Its integrand is holomorphic in the initial point and
the relevant trajectories stay in the source's flow domain. The differentiated
action identity continues to hold there:
$$
\nabla S_s(x)=J(\Phi_s(y_s(x))-y_s(x)),
\qquad\|\nabla S_s\|_\infty\le200s.
$$
The source's Hamilton equations also give the same Hamilton--Jacobi equation
on this common strip. Hence the supplement correctly preserves both the
gradient bound and the equation when it widens the endpoint domain.

## 2. Complex Hamilton--Jacobi difference and action normalization

The exact equation is
$$
\partial_sS_s(x)=a(x-J\nabla S_s(x)/2).
$$
Each coordinate displacement on its right has modulus at most $100s$,
because J has sup-norm operator norm one. The whole complex line segment
from x to this shifted point remains in the strip of width $2\rho$: its
imaginary coordinate magnitudes are at most $3\rho/4+100t_0<2\rho$.
The source bounds each partial derivative of a there by 200.

The integral of the complex differential along the segment consequently obeys
$$
|\partial_sS_s(x)-a(x)|
\le\sum_{j=1}^2 200\cdot100s=40000s.
$$
Since $S_0=0$, integration from zero to t gives uniformly on the wider strip
$$
\|S_t-ta\|_\infty\le20000t^2,
\qquad \|S_t/t-a\|_\infty\le20000t.
$$
This checks the factor two from integrating s and the division by the exact
positive t. The argument needs no estimate comparing $\tau N$ with one.

## 3. Cauchy radii, all mixed derivatives, and the rational comparison

About any real point, a complex polydisk of radius $R<3\rho/4$ in each
coordinate lies inside the constructed strip. Applying the one-variable
Cauchy formula successively to both coordinates gives
$$
|\partial^\alpha(S_t/t-a)|
\le\alpha! R^{-|\alpha|}\,20000t.
$$
The bound on the function is independent of R, so letting
$R\uparrow3\rho/4$ gives exactly the source's factor
$(4/(3\rho))^{|\alpha|}=(4000/3)^{|\alpha|}$. No boundary holomorphy
outside the open strip is required for this limiting step.

There are $\sum_{j=0}^{17}(j+1)=171$ multiindices in two variables of total
order at most 17. For each, $\alpha_1!\alpha_2!\le17!$, and
$(4000/3)^{|\alpha|}\le(4000/3)^{17}$. Finally
$t=10^{-80}/(2\pi)<10^{-80}$. Thus their summed bound is strictly below
$$
B=171\cdot17!\left(\frac{4000}{3}\right)^{17}\cdot20000\cdot10^{-80}
=\frac{75942437322752}{46927928924560546875}.
$$
The rational simplification and cross-multiplication were checked with exact
integer/Fraction arithmetic. More explicitly,
$$
46927928924560546875
-100000\cdot75942437322752
=39333685192285346875>0.
$$
Therefore $B<1/100000$, and the claimed derivative sum has the same strict
upper bound. All displayed rational comparisons are exact; floating point
arithmetic is unnecessary.

## 4. Boundary of what has been established

The supplement provides the necessary uniform closeness of the exact normalized
center phase to its explicit finite Fourier polynomial through order 17.
It does not itself construct a derivative extractor or prove that order 16
suffices for all translated normalized phase differences. That is a distinct
finite polynomial argument to be audited separately. Once such an argument is
proved with a margin exceeding this perturbation bound, it can legitimately
fix the exponent in the already audited uniform oscillation lemma.
