# Sources for the harmonic-transition proof

Checked 9 September 2026. This is an overlap and hypothesis check, not a
global novelty determination. No external theorem is required for the
new quadratic-phase convergence proof.

| Primary source | Exact location checked | Relation to the project |
|---|---|---|
| Cébron, Oliveira Santos, Youssef, *Graphon-Theoretic Approach to Central Limit Theorems for epsilon-Independence*, [arXiv:2411.13062v2](https://arxiv.org/html/2411.13062v2), revision 29 November 2024 | Theorem 1.1, formula (4), Sections 4--5; Proposition 2.6 | Graphon crossing-moment laws and weighted/multivariate versions are prior work. The finite independence assumptions are not asserted for the Pell Weyl orbit. Proposition 2.6 needs essential supremum below one; it does not establish density for the intermediate indicator kernels. |
| Same authors, *Central limit theorem for epsilon-independent products and higher-order tensors*, [arXiv:2504.10059v1](https://arxiv.org/html/2504.10059v1), 14 April 2025 | Theorem 1.1 and its attribution to the previous paper | Confirms the predecessor and the same crossing-graph notation. |
| Kieler, Fritzsch, Bäcker, *Semiclassical foundation of universality in chaotic quantum circuits*, [arXiv:2605.27052v1](https://arxiv.org/html/2605.27052v1), 26 May 2026 | Discussion following formula (11), before the conclusion | The authors identify a long-period resummation issue and conjecture a rescaled form factor. This does not provide the missing rigorous Heisenberg-scale input here. |

The notation translation for the first source is exact: its graphon is
$w_\beta(x,y)=\mathbf1_{\{\operatorname{dist}(x,y)<(1-2\beta)/2\}}$, and its
intersection graph is our crossing graph $G_\pi$. This identifies the class
of limiting measures. It does not prove that these measures occur for the
Pell compressions: that is the separate arithmetic argument in (H7)--(H17).

Searches included “graphon central limit theorem noncommutative”,
“crossing graph Gaussian semicircle”, “cat map graphon”, and “cat map
mesoscopic Gaussian”, with backward checking from the 2025 paper to the
2024 primary text. The all-field historical literature, unpublished work,
and every citation descendant were not exhausted. The conclusion is
**known abstract law; arithmetic realization priority unverified**.

A separate search of reciprocal shifted-subgroup energies produced no
verified improvement applicable to the project's sparse Cayley range.
This negative search result is not evidence that such an improvement is
unknown. No energy exponent was changed.
