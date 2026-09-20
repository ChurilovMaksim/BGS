# The higher-order target at Heisenberg times

19 September 2026. Internal derivation and self-review; not a new BGS theorem
and not a claim of priority. This corrects the blanket higher-trace vanishing
target in the two uploaded research summaries. Dimension is denoted by d;
for a parity block d is (N+1)/2 or (N-1)/2, not N.

## 1. A decisive cubic calculation

Let V have the CUE_d distribution and T(m)=Tr(V^m). For positive integers
a,b, the exact identity is

\[
\mathbb E[T(a)T(b)T(-a-b)]
=d-(d-a)_+-(d-b)_++(d-a-b)_+.                 \tag{1}
\]

There is no proper zero-sum subset of (a,b,-a-b). Consequently this moment
is also its third joint cumulant. It is zero when a+b<=d; for a,b<d<a+b
it equals a+b-d. For a,b>=d it equals d.

In particular, for d divisible by four and a=b=3d/4, the answer is d/2,
not zero. The phenomenon is a finite-dimensional reference effect at the
very time scale needed for BGS, not an arithmetic defect of a cat map.

Let w be a nonnegative smooth amplitude of integral one supported in
(0.71,0.79)^2, symmetric about (3/4,3/4). Riemann summation gives

\[
\lim_{d\to\infty}d^{-3}\sum_{a,b>0}w(a/d,b/d)
\mathbb E[T(a)T(b)T(-a-b)]=\tfrac12.          \tag{2}
\]

Thus the claimed all-compact-support zero target is inconsistent with
the CUE reference already at order three. The subsequent calculation in
`cubic_variance.md` strengthens this for factorized smooth amplitudes:
the appropriately normalized cubic statistic tends to 1/2 in L2, with
variance O(1/d). No almost-sure concentration claim is used.

If the report intended a *CUE-subtracted* trace product, or restricted
Fourier support to a+b<d, it must say so. Neither restriction is present
in the displayed all-amplitude vanishing statement. Restricting to that
small support would not settle the full microscopic problem.

## 2. Derivation, with all-order counterterms

Take CUE eigenangles in cycles. Their joint density is
|det(e^{2pi i j theta_k})_{0<=j<d}|^2/d!. Let P_d be the projection onto
Fourier modes 0,...,d-1 on the circle, and E_m multiplication by
e^{2pi i m theta}. Expanding the two determinants and integrating yields

\[
\mathbb E\exp\Big(\sum_j t_jT(m_j)\Big)
=\det\big[I+P_d(e^{\sum_jt_jE_{m_j}}-I)P_d\big].       \tag{3}
\]

This is an identity near t=0 and hence of the formal Taylor coefficients
needed below. The determinant is on the d-dimensional range of P_d.
It follows either directly from the density or from the finite-rank
determinantal generating-function identity. The latter framework is
also described in Soshnikov, *Determinantal Random Point Fields*,
[Theorem 2, equation (1.28)](https://arxiv.org/pdf/math/0002099).
The specific formulas below are derived here rather than quoted from it.

For integers m_1,...,m_r with total zero, let an ordered partition
(B_1,...,B_l) have block sums b_j=sum_{i in B_j}m_i. Put
s_0=0, s_j=b_1+...+b_j and
R(B)=max_{0<=j<=l}s_j-min_{0<=j<=l}s_j.
Then

\[
K_{d,r}(m)=
\sum_{\ell=1}^r\frac{(-1)^{\ell-1}}{\ell}
\sum_{(B_1,\ldots,B_\ell)}(d-R(B))_+.                  \tag{4}
\]

For nonzero total sum the cumulant is zero by rotation invariance.
To prove (4), expand log det(I+X) as sum (-1)^{l-1}Tr(X^l)/l.
The coefficient multilinear in t_1,...,t_r is the sum over ordered
nonempty blocks. Each block contributes the multiplier E_{b_j}.
The trace of P E_{b_1} P ... E_{b_l} P counts integers n for which all
visited Fourier indices remain in [0,d-1]. Their interval intersection
has exactly (d-R(B))_+ elements. Reversing the order of the visited
partial sums, if using the opposite operator convention, does not change
that span.

For r=3 the one-block term is d. The two-block terms subtract
(d-a)_+,(d-b)_+,(d-a-b)_+. The three-block terms add
2(d-a-b)_+. This proves (1), including the cases d=1 and a+b=d.

For every fixed r, (4) has the exact scaling

\[
K_{d,r}(m)=d\,k_r(m/d),\qquad
k_r(x)=\sum_{\ell=1}^r\frac{(-1)^{\ell-1}}\ell
\sum_B(1-R_x(B))_+.                                  \tag{5}
\]

The kernel k_r is piecewise linear on the zero-sum hyperplane. It is
generally nonzero. For instance,

\[
K_{d,r}(d,\ldots,d,-(r-1)d)=d\quad(r\ge3).             \tag{6}
\]

Every proper nonempty subset here has a nonzero sum of modulus >=d.
Thus every term in (4) with at least two blocks has span >=d, and only
the one-block contribution survives. Small neighborhoods in the scaled
hyperplane also have nonzero k_r. There is no general higher-order zero
target at Heisenberg scale.

## 3. Correct deterministic comparison

For a deterministic d-dimensional U, write T_U(m)=Tr(U^m). On an open
region of the zero-sum hyperplane without a proper zero-sum subset, the
appropriate connected reference is K_{d,r}, because all proper blocks
have zero CUE expectation. The natural required comparison is

\[
d^{-r}\sum_{\sum m_i=0}a(m/d)
\left[\prod_iT_U(m_i)-d\,k_r(m/d)\right]\longrightarrow0,       \tag{7}
\]

for amplitudes supported in that region. Equation (7) is a corrected
research obligation, NOT an estimate established for the fixed map.

On the proper zero-sum strata, the full CUE moment is instead

\[
M_d(m_1,\ldots,m_r)
=\sum_{\pi\in\Pi_r}\prod_{B\in\pi}K_{d,|B|}(m_B).    \tag{8}
\]

Here a cumulant of a block with nonzero total sum is zero, and K_{d,1}(0)=d.
The full trace-to-factorial bridge is already maintained at
`mathematics/trace_to_local_statistics_bridge.md`:

\[
D_U(m)=\sum_{\pi\in\Pi_k}
\prod_{B\in\pi}(-1)^{|B|-1}(|B|-1)!
\prod_{B\in\pi}T_U\left(\sum_{i\in B}m_i\right).      \tag{9}
\]

Replace the final product in (9) by (8), evaluated on the block sums,
to obtain the exact CUE counterterm. Fourier summation with factor d^{-k}
is then exactly the factorial-correlation discrepancy. This handles
zero modes, coincident powers, and lower-order partitions explicitly.

In general the reducible partitions are not just constants and pairs.
Already a (2,1,1) partition at k=4 leaves a cubic product of block traces.
At k=6 two zero-sum triples can contribute the product of two cubic
moments. A claim that all such terms have collapsed to pairs needs an
additional proof; the displayed partition formula does not supply it.

This repair is consistent with the sine-process identity
rho_3(0,x,y)=1-s(x)^2-s(y)^2-s(x-y)^2+2s(x)s(y)s(x-y),
where s(x)=sin(pi x)/(pi x). Its cyclic term cannot simply be deleted.

## 4. Executed verification and remaining work

`verify.py` checks (1) for every d=1,...,6 and a,b=1,...,2d: 364 cases.
It uses an independent constant-term integration of the CUE Vandermonde
density, not simulated random matrices. The general moment formula is
checked by the same independent integration on 45 seeded cases at
d=2,3,4 and r=2,...,6, including zero modes and nonzero total sums.
The high-frequency family (6) and smooth-amplitude diagnostic (2) are
also checked. These finite tests audit the formulas; (3)--(6) are their
analytic proof.

The fixed deterministic map still requires (7) and the corresponding
stratum estimates. Neither the verified symbol algebra in the new
reports nor our previous comparison theorems supplies them. A small
Fourier-support Gaussian identity cannot replace these obligations.
