> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/fermionic_finite_detector_shell_audit.md`. Embedded SHA256: `c2ec38925db10f7c178d8e3d5e93acd757dddcaff29b53760d638a04eca5c849`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit: exact finite detector shell coherence

Date: 20 October 2026.

## Input and verdict

Input: adversarial_finite_detector_shell_coherence.md

SHA-256:
76aa1ece063eea6b9e673d5fc592fa23ba72c541fee5c93916314a62da85ee6f

Verdict: **PASS**, after reading the complete file and independently
recalculating its leading coefficient, modular error, and tail bounds.
No change to the input was requested.

The continuum comparison was also checked against
fermionic_frequent_shell_coherence.md, SHA-256
21c536cdcb9c8f5dc43aa5c7e74300865b0152f7187b8358b68832b2ae21e285.
The finite proof does not depend on replacing a discrete matrix by that
continuum operator.

## 1. Exact matrix and finite denominator

For consecutive Fourier indices, the geometric sum gives
$$
 |E_{mn}|^2
 =\frac{\sin^2(\pi s(m-n)/N)}
        {N^2\sin^2(\pi(m-n)/N)}
$$
off the diagonal, and $E_{mm}=s/N$. Moving the Fourier window
changes only a removable phase.

For lifted differences $|d|\le N/2$,
$$
 0\le\frac1{N^2\sin^2(\pi d/N)}-\frac1{\pi^2d^2}
 \le C N^{-2}.
$$
The last estimate follows from the bounded continuous extension of
$(1/\sin^2u-1/u^2)$ at zero. The whole coordinate window has diameter
less than $N/2$ for every sufficiently large $N$, so this bound
covers every selected pair, including all shell pairs.

There are at most $r^2$ ordered pairs. The error in any selected
sum of their squared entries is therefore at most $Cr^2/N^2$,
which is $O(1/\log N)$ at the specified dimensions. This is
an absolute error, not a relative error and not an operator norm
approximation.

## 2. Uniform adjacent-interval lemma

The identity
$$
 \sum_{d=1}^a\frac{\sin^2(\pi\sigma d)}d
 =\frac12\log^+(a\sigma)+O(1)
$$
is uniform for $0<\sigma\le1/2$.

For $a\sigma\le1$, the elementary sine bound proves boundedness.
For $a\sigma>1$, summation by parts bounds the tail of the
cosine series by $C/(a\sin\pi\sigma)$. The infinite cosine
series equals $-\log(2\sin\pi\sigma)$, obtained by a radial
limit of the logarithm power series. This yields the stated
uniform logarithm, since $\sin\pi\sigma$ is comparable to
$\sigma$ on the full required interval.

For two adjacent integer intervals with lengths $a,b$, the
number of ordered pairs at distance $d$ is exactly $d$ for
$1\le d\le\min(a,b)$. Beyond that point it is at most
$\min(a,b)$, and its weighted tail is bounded by
$$
 \min(a,b)\sum_{d>\min(a,b)}d^{-2}=O(1).
$$
Their interaction is consequently
$$
 \frac1{2\pi^2}\log^+(\sigma\min(a,b))+O(1).
$$
The separate bound $\sigma^2ab$ is valid even at the deepest
integer scales. No uniformity is lost as $\sigma\to0$.

## 3. Counting every rounded shell

Put $Z=w\sigma$ and
$J=\lfloor\log Z/\log(1/\rho)\rfloor$. Then
$1\le Z\rho^J<1/\rho$.

For all resolved indices $j\le J$, the shell widths are
$$
 (1-\rho)w\rho^j+O(1),
$$
and their smallest scale is a fixed multiple of $1/\sigma$.
Since $\sigma\to0$, every resolved width is positive and
the rounding error is uniformly negligible in comparisons
with that width.

One ordered adjacent interaction on one side gives
$$
 \frac1{2\pi^2}\bigl(\log Z-j\log(1/\rho)\bigr)+O_\rho(1).
$$
Summing $j$ yields
$$
 \frac{(\log Z)^2}{4\pi^2\log(1/\rho)}+O_\rho(\log Z).
$$
There are two ordered directions and two coordinate signs.
Their product is the factor four needed for
$$
 \frac{(\log Z)^2}{\pi^2\log(1/\rho)}.
$$

Nonadjacent same-sign resolved shells have a gap comparable
to the outer scale, so their interaction is at most
$C_\rho\rho^{k-j}$. Opposite-sign resolved shells satisfy
the bound $C_\rho\rho^{|j-k|}$. These sums are
$O_\rho(J+1)$.

The entire unresolved region, including the central singleton,
has $O(1/\sigma)$ sites. Its internal interaction and its
interaction with the last resolved shell are $O_\rho(1)$.
For an earlier resolved shell $j<J$, its interaction with
the entire tail is at most $C_\rho/(Z\rho^j)$; summing
this geometric sequence is again $O_\rho(1)$.

These bounds include every shell. Keeping the positive and
negative intervals at a common index in the same block
retains some opposite-sign terms, but their total is only
$O_\rho(\log Z)$. Hence that convention does not alter
the leading coefficient.

The relation $\log Z=\log L+O(1)$, together with the absolute
modular error above, proves the exact finite statement
$$
 Q_N=\frac{(\log L_N)^2}{\pi^2\log(1/\rho)}
       +O_\rho(\log L_N).
$$

## 4. Purity, coefficients, and determinants

Parseval for the circle interval of length $\sigma$ gives
$\sum_{d\in\mathbb Z}f_\sigma(d)=\sigma$. Therefore
$$
 \sum_{m,n=1}^r f_\sigma(m-n)
 =r\sigma-2\sum_{d<r}d f_\sigma(d)
          -2r\sum_{d\ge r}f_\sigma(d).
$$
The last term is $O(1)$; the middle term is
$\pi^{-2}\log(r\sigma)+O(1)$.
The exact purity formula
$$
 \operatorname{Tr}E_N^2=L_N-\pi^{-2}\log L_N+O(1)
$$
follows with the already controlled modular error.

Pinching is an orthogonal projection in Hilbert--Schmidt
space, so
$$
 Q_N=\|E_N-H_N\|_{\rm HS}^2.
$$
Since the traces agree,
$e_2(E_N)-e_2(H_N)=-Q_N/2$.

For $G_u=H_N+u(E_N-H_N)$, differentiation of
$F(u)=\log\det(I-tG_u)$ gives
$$
 F'(0)=0,\qquad
 F''(u)=-t^2\|R_u^{1/2}(E_N-H_N)R_u^{1/2}\|_{\rm HS}^2,
 \quad R_u=(I-tG_u)^{-1}.
$$
The bounds $I\le R_u\le(1-t)^{-1}I$ work even though
$E_N-H_N$ is indefinite. Integrating $F''$ proves
both determinant inequalities with their correct signs
and the factor $1/2$.

The note correctly distinguishes the divergent logarithm
and the divergent second-coefficient discrepancy from
the absolute determinant difference, which satisfies
$$
 0\le\det(I-tH_N)-\det(I-tE_N)\le e^{-tL_N}\to0.
$$

## 5. Scope of the audit

This theorem concerns exact matrices on the original quantum
space. It does not identify this detector with a nonlinear
stable/unstable marker by a uniform semiclassical theorem,
and it does not estimate the trace powers of $U_N$.
The input explicitly preserves those distinctions.

The growing trace $L_N\sim N/\log N$ also prevents one
from interpreting these elementary symmetric coefficients
as the fixed-test factorial coefficients of $H_{\rm diag}$.
No spectral universality or counterexample is deduced.

