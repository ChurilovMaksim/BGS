# A periodic-orbit CLT does not by itself close the fixed-strength Fourier gap

Checked 5 October 2026, base
`9555cd19dbf7cac335320dc231f2a7b7bb71954f`.
Primary source: M. F. I. Kieler, F. Fritzsch, A. Bäcker,
*Semiclassical foundation of universality in chaotic quantum circuits*,
[arXiv:2605.27052v1 HTML](https://arxiv.org/html/2605.27052v1).
This is a bounded applicability check, not a priority survey or a new
load-bearing external theorem.

The Setting specifies interacting product maps. Equation (2) retains an
SFF average, with time-window averaging mentioned. Equations (5)--(8)
introduce $\sqrt\Lambda=\epsilon\sqrt{T_{\rm H}}/\hbar$ and the
shrinking-interaction limit at fixed $\Lambda$. The CLT is invoked for
normalized periodic-orbit action fluctuations. These passages were read,
not merely the title or search snippet.

There is no established dictionary from those product-orbit families
and that scaling to the unchanged single-map operator at fixed
$\tau=10^{-80}$. A fixed-strength adaptation would require justified
trace errors and growing-frequency control of the actual weighted orbit
measure. The source is not imported as such an estimate. This is a
limitation of the proposed adaptation, not a refutation of its stated
setting.

## Self-contained discriminator for the weak-CLT shortcut

Let $Z$ be a standard real Gaussian and let $a_n\to\infty$. Define

$$
X_n=\frac{2\pi}{a_n}
\left\lfloor\frac{a_nZ}{2\pi}+\frac12\right\rfloor.
$$

Then $|X_n-Z|\le\pi/a_n$ deterministically. Hence $X_n\to Z$ in
every finite $L^p$, and all fixed moments converge, using
$|X_n|\le|Z|+\pi$ eventually and dominated convergence. Nevertheless

$$
\mathbb E e^{ia_nX_n}=1,\qquad
\mathbb E e^{ia_nZ}=e^{-a_n^2/2}\longrightarrow0.
$$

Thus even moment convergence and a deterministic vanishing coupling
error do not supply characteristic-function control at the growing
frequency. This elementary rounding example is author self-review,
not a periodic-orbit realization, a counterexample to the source's
additional hypotheses, or a world-priority claim. No finite experiment
is needed to decide its exact integer-phase identity.

For the actual map, a uniform oscillatory weighted-orbit estimate
remains an open possible continuation. An unchanged invocation of
weak Gaussian convergence would repeat the demonstrated logical
failure; an appropriate nonlattice/local-limit estimate could change
that step. Actual signed Heisenberg cancellation and BGS remain open.
