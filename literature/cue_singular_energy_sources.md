# Small CUE gaps: exact source check for BGS-CUE-001

Checked 25 September 2026 against the published
[author-hosted PDF](https://math.nyu.edu/~bourgade/papers/ExtremeGaps.pdf)
of G. Ben Arous and P. Bourgade, *Extreme gaps between eigenvalues of random
matrices*, Annals of Probability 41 (2013), 2648--2681,
DOI:10.1214/11-AOP710; arXiv:1010.1294.

**Exact input:** Theorem 1.1, pp. 2650--2651, states convergence of
the process of consecutive circular eigenangle gaps, marked by
position, after multiplying the gaps by $N^{4/3}$. Its intensity
on a gap set $A\subset\mathbb R_+$ and positional arc
$I\subset(0,2\pi)$ is

$$
\frac{1}{24\pi}\left(\int_Au^2\,du\right)
                   \left(\int_I\frac{d\theta}{2\pi}\right).
$$

The project's angles have period $2\pi$, so integrating the mark
over the circle gives $u^2du/(24\pi)$. The restriction
$I\subset(0,2\pi)$ is handled by excluding a narrow arc at
the seam and controlling it by rotation invariance and the
project's explicit two-point bound. The theorem itself does
not assert convergence of inverse powers of gaps or removal of
a singular cutoff: these are separate project steps in
[the maintained proof](../mathematics/cue_singular_energy.md).

Comparison checked against A. Aguirre, A. Soshnikov and J. Sumpter,
[*Pair Dependent Linear Statistics for CβE*,
arXiv:1912.07110v3](https://arxiv.org/abs/1912.07110).
Their Theorems 2.1, 2.4 and 2.5 require regular
test functions; in particular the microscopic theorem
uses $f\in C_c^\infty(\mathbb R)$. Their Section 4 computes
CUE trace-power covariances. One cannot insert the nonintegrable
kernel $|2\sin(\delta/2)|^{-2}$ directly into those theorems.
No claim of novelty follows from this limited comparison:
no exhaustive backward/forward citation audit or
external referee review has been completed.
