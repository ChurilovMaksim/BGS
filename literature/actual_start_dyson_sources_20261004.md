# Exact-source check for actual-start Dyson relaxation

Checked 4 October 2026. Scope: the reference process starts at the
actual centered frozen spectrum; a clock theorem cannot replace that
initial condition. The logarithmic initial regularity comes from the
project's FM-007, not from a literature assumption silently declared true.

## Real-line universality: context, not an imported circular theorem

Landon, Sosoe and Yau, *Fixed energy universality for Dyson Brownian
motion*, [arXiv:1609.09011v3](https://arxiv.org/pdf/1609.09011v3.pdf),
14 January 2019: Definition 2.1, printed p.8; Theorem 2.2, printed p.9.
The source requires a real diagonal initial matrix, two-sided bounds on
its Stieltjes density for $|E|\le G$, $g\le\eta\le10$, polynomial scale
restrictions including $g\le N^{-\delta}$, and
$gN^\sigma\le t\le N^{-\sigma}G^2$.
The displayed theorem compares with GOE using free-convolution unfolding.
The present logarithmic $g_N$ violates its stated polynomial upper scale;
circle geometry and normalization also need proof. Neither theorem nor
its rates are used to conclude Sine$_2$ here. The PDF hypotheses and
unfolding, rather than only its abstract, were inspected.

## Circular local laws: checked initial condition

Adhikari and Landon, *Local law and rigidity for unitary Brownian motion*,
[arXiv:2202.06714v3](https://arxiv.org/pdf/2202.06714), 21 February 2023;
published DOI [10.1007/s00440-023-01230-8](https://doi.org/10.1007/s00440-023-01230-8).
Equation (1.1), printed p.1, starts the normalized process at the identity.
Theorem 1.2 and Corollary 1.3, printed p.6, concern its empirical
transform and interval counts relative to free unitary Brownian density.
This supplies neither arbitrary-start microscopic universality nor the
actual centered-start relaxation implication. Versioned URLs initially
failed; the unversioned PDF successfully returned v3. Failed retrievals
were not counted as source verification.

Bertucci and Pesce, *A new approach for the unitary Dyson Brownian motion
through the theory of viscosity solutions*,
[arXiv:2504.16551v2](https://arxiv.org/pdf/2504.16551), 6 February 2026:
Sections 4--5 concern convergence of empirical measures and the limiting
Dyson equation's regularization and equilibrium. These macroscopic
objects do not establish a microscopic sine kernel for the present family.
Only the displayed setup, contents and introductory scope were checked;
no detailed theorem from this source is load-bearing.

## Exact arbitrary-start circular kernel: prior finite formula

Kieburg, Li, Zhang and Forrester, *Cyclic Pólya Ensembles on the Unitary
Matrices and their Spectral Statistics*,
[arXiv:2012.11993v2](https://arxiv.org/pdf/2012.11993), 24 May 2022;
DOI [10.1007/s00365-023-09630-8](https://doi.org/10.1007/s00365-023-09630-8).
Proposition 12 and (2.4.10), printed p.18, give the shifted theta-function
heat weight. Theorem 7(3), printed p.13, handles a fixed second matrix;
the same page notes confluent limits for degenerate spectra.
Proposition 21, printed pp.33--34, (3.2.2)--(3.2.3), supplies biorthogonal
functions and a double-contour kernel for distinct initial eigenvalues.
The heat weight has a Laurent series on every annulus, as required there.
The source time maps to $t/(2N)$ in this project's Brownian normalization;
the fundamental character then decays as $e^{-t/2}$.
The [route note](../record/circular_kernel_route_20261004.md) reconstructs
the angular formula and its clock specialization. This is prior finite
determinantal structure, not a new universality theorem. Global contour
and microscopic Fredholm asymptotics are not imported.

## Project consequence and search coverage

[FLOW-012](../mathematics/fixed-map/coboundary_general_start.md) proves comparison
to the specified initial Dyson law. [FLOW-013](../mathematics/fixed-map/dyson_relaxation_obstruction.md)
refutes a prescribed relaxation time inferred only from the listed
abstract low-trace hypotheses. [FM-017](../mathematics/fixed-map/frozen_mesoscopic_regularity.md)
derives logarithmic-scale Poisson regularity, local stationary points
and unweighted vertical phase-tail bounds
from FM-007. The separate [FLOW-014 project proof](../mathematics/fixed-map/circular_dyson_actual_start.md)
now derives the gap-independent global contour and full Fredholm argument
at $t_N=8g_N$ from the prior finite kernel. This asymptotic proof is not
imported from any of the sources checked above; priority is unestablished.

Targeted queries used both available search systems: arbitrary-initial
unitary Brownian local universality, circular Dyson deterministic-start
correlation kernels, noncolliding circle Brownian motion, and cyclic
Pólya heat kernels. Secondary overview claims were not promoted. This
bounded check neither establishes priority nor proves that a matching
circular theorem is absent from the literature.

FLOW-013's all-power nonvanishing uses the **existing**
EXT-POPESCU-2023, Corollary 3.2, printed p.16, already checked in
[the earlier source audit](expansion_wavepacket_sources_20261004.md).
The algebraic perturbation mechanism and earlier intensity-loss examples
are credited as prior project/literature inputs.
