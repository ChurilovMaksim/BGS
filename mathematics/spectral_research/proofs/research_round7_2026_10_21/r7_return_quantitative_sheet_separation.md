> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round7_2026_10_21/r7_return_quantitative_sheet_separation.md`. Embedded SHA256: `3ae2af7e36c90fc2c1214315a1513936a09b6aa10fc150295ddfd4e8062cadbf`.
> [Thematic guide](../../topics/dephasing.md).

# A quantitative lower bound for the mixed sheet derivative on the full endpoint cover

21 October 2026. This is a consequence for the **original** fixed-
$\tau$ family of the global sheet construction in
`r7_return_all_fixed_powers_phase_separation.md`. The norm in the theorem
is over the full endpoint cover of period $b_R$, not over one prescribed
unit endpoint cell. This distinction matters for any proposed estimate
uniform when $R$ grows with $N$.

## 1. Statement

Use
$$
 \mathsf S^R=\begin{pmatrix}a&b\\c&a\end{pmatrix},\qquad
 \lambda=3+2\sqrt2,\qquad
 \epsilon=14000\tau,\qquad A_R=(1+\epsilon)^R,
 \qquad\tau=10^{-80}.
$$
Let $\Phi_m$ be the exact real-analytic sheet actions constructed in
the companion proof, $\Theta_m$ their initial quadratic phases, and
$S(q,s)=\Phi_0(q,s)-\Theta_0(q,s)$. For $0<d<b$, define
$$
 D_d(q,s)=S(q,s+d)-S(q,s),\qquad
 \eta_{R,d}=\sup_{(q,s)\in\mathbb R^2}
                   |\partial_q\partial_sD_d(q,s)|.
$$
The supremum is finite and attained on a compact period rectangle, since
$S$ is $b$-periodic in both variables. Then
$$
 \boxed{\qquad
 \eta_{R,d}\ge
 \frac{\tau\lambda^R}{8400\,b^3(1+\epsilon)^R}
 \ge\frac{\tau}{8400\,b^2(1+\epsilon)^R}>0.
 \qquad}
 \tag{1.1}
$$
The same full-cover lower bound holds for the mixed derivative of every
$\Phi_m-\Phi_n$, $m\ne n\pmod b$, by translation of $s$.
The proof uses the quantitative translation characters, not just the
qualitative absence of exact translation intertwiners.

## 2. Small mixed derivative would make both first derivatives small

The companion proof establishes the exact period lattice
$(b,0),(a,1)$ for $S$. Consequently
$\overline S(s)=b^{-1}\int_0^bS(q,s)\,dq$ is one-periodic.
For the integer $d$, therefore,
$$
 \int_0^bD_d(q,s)\,dq=0.
 \tag{2.1}
$$
Translation invariance of the integral over a full $s$-period also
gives $\int_0^bD_d(q,s)\,ds=0$. Differentiation shows that
$D_{d,s}$ has zero mean in $q$, and $D_{d,q}$ has zero mean
in $s$.

A continuously differentiable periodic real function of period $b$
with zero mean and derivative bounded by $L$ has absolute value at
most $bL$: it has a zero and the fundamental theorem of calculus
along an interval of length at most $b$ gives the bound. Applying this
to the two first derivatives yields
$$
 \|D_{d,q}\|_\infty\le b\eta_{R,d},\qquad
 \|D_{d,s}\|_\infty\le b\eta_{R,d}.
 \tag{2.2}
$$
No bound on a separate additive function of an endpoint is assumed;
the exact zero means remove those possible constants.

## 3. The near-translation relation for the physical iterate

Let $F=\Phi_{-\tau}\mathsf S^{-1}$ be the physical map as in the
companion proof; here $\Phi_u$ denotes the flow of
$(a_p,-a_q)/(2\pi)$, not a sheet phase. To keep notation explicit,
write $F_R=F^R$. The generating-function identity is
$$
 \Phi_0(q,s+d)-\Phi_0(q,s)
 =\frac{dq-ad s-ad^2/2}{b}+D_d(q,s).
$$
At endpoints $(q,s)$, put $p=-\Phi_{0,s}(q,s)$ and
$P=\Phi_{0,q}(q,s)$. Differentiation gives
$$
 F_R\left(s+d,p+\frac{ad}{b}-D_{d,s}\right)
   =\left(q,P+\frac d b+D_{d,q}\right).
 \tag{3.1}
$$
The lift has homology
$\mathsf S^{-R}=\left(\begin{smallmatrix}a&-b\\-c&a\end{smallmatrix}\right)$.
Removing the integer input shift $d$ from (3.1), and defining
$$
 h=(0,ad/b),\qquad k=(-ad,cd+d/b),
$$
therefore produces
$$
 F_R(z+h)=F_R(z)+k+E(z).
 \tag{3.2}
$$
The global twist established in the companion proof means that $(q,s)$
covers all input $z=(s,p)$, so (3.2) holds on the full real lift.

The positive-coordinate derivative bound gives
$$
 \operatorname{Lip}_\infty(F_R)
 \le A_R(a+b)<2bA_R.
$$
By (2.2) and (3.1),
$$
 \|E\|_\infty
 \le(\operatorname{Lip}_\infty(F_R)+1)b\eta_{R,d}
 \le3b^2A_R\eta_{R,d}.
 \tag{3.3}
$$
The error is a periodic function because the left side of (3.2), after
subtracting its constant, is a difference of two lifts with the same
integer equivariance.

## 4. Use a conjugate with a discounted expanding coordinate

It would be wasteful to invert (3.2), since that introduces another
Lipschitz constant for a long iterate. Instead put
$$
 C(q,p)=(q,-p),\qquad L=\mathsf S C,
 \qquad G=LFL^{-1}=\mathsf S\kappa_\tau,
 \quad \kappa_u=C\Phi_{-u}C.
$$
The flow $\kappa$ has exactly the vector field
$(\widetilde a_r,-\widetilde a_q)/(2\pi)$, where
$\widetilde a(q,r)=a(q,-r)$. Thus the discounted-coordinate proof
in Section 5 of the companion note applies to $G$ with the same
constants. Its symbol has the same support and coefficient norm, and
the magnitudes of its coefficients at $(1,0)$ and $(0,1)$ are the
same as before. With $\ell=(1,\sqrt2)/\sqrt3$, the periodic function
$$
 v_R^G(w)=\lambda^{-R}\ell G^R(w)-\ell w
$$
therefore satisfies, for every positive $R$,
$$
 |\widehat v_R^G(e_i)|\ge\tau/800,\qquad i=1,2.
 \tag{4.1}
$$
All hypotheses of that explicit discounted proof have just been checked;
no structural stability or genericity theorem is invoked.

Conjugating (3.2) by the fixed matrix $L$, whose maximum row-sum norm
is seven, gives
$$
 G^R(w+H)=G^R(w)+K+E_G(w),\qquad
 H=Lh,\quad K=Lk,
\quad \|E_G\|_\infty\le21b^2A_R\eta_{R,d}.
$$
Consequently
$$
 v_R^G(w+H)-v_R^G(w)
 =\text{a constant}+\lambda^{-R}\ell E_G(w).
 \tag{4.2}
$$
Since $\|\ell\|_1<2$, every nonzero Fourier coefficient of the
right side is bounded by
$42\lambda^{-R}b^2A_R\eta_{R,d}$.

The input translation is
$$
 H=(-4ad/b,-3ad/b).
$$
At least one of its two coordinates is nonintegral. Otherwise $b$
would divide both $4ad$ and $3ad$, hence would divide $ad$,
and $\gcd(a,b)=1$ would force $b\mid d$, contrary to $0<d<b$.
Its nonintegral coordinate has distance at least $1/b$ from the
integers. For that coordinate $i$,
$$
 |e^{2\pi iH_i}-1|\ge4/b.
$$
The elementary inequality used here is
$\sin(\pi x)\ge2x$ for $0\le x\le1/2$, obtained from concavity.
Taking the corresponding Fourier coefficient in (4.2), and using (4.1),
gives
$$
 \frac{\tau}{200b}
 \le42\lambda^{-R}b^2A_R\eta_{R,d}.
$$
This is the first inequality in (1.1). The second uses
$b_R=(\lambda^R-\lambda^{-R})/\sqrt2<\lambda^R$.

## 5. Quantitative reach and the next unproved estimate

The lower bound is exponential in $R$, with explicit constants. It
is a uniform exclusion of near-separability on the full $b_R$-periodic
cover. In particular it identifies a measured phase property of the
original map that is not supplied by short-power entry norms.

For a fixed pair of sheets the quantum matrix uses one unit endpoint
cell. The supremum in (1.1) may be achieved in another cell of the large
cover. Integer endpoint translations permute common sheet shifts, and
qualitative analyticity propagates nonvanishing to every cell, but no
quantitative propagation estimate is proved here. Even such a supremum
bound on each cell would still need a bound on sublevel volumes of the
aliased rectangular-cycle gradients to give an effective oscillatory rate.

Thus (1.1) is not a logarithmic-time estimate for the quantum kernel.
The next missing quantitative step in this direction is a bound, uniform
over the required sheet pairs and aliases as $R$ grows, for the measure
of the region where the rectangular-cycle gradient is small. Together
with the growth of amplitude derivatives, the number of sheets, and the
finite-shift residual, it would determine an admissible relation between
$N$ and $R$. None of those requirements is hidden in the statement
of (1.1).
