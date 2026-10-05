# Primary sources and normalization for the critical noise continuation

Checked 5 October 2026. This is a bounded source/application check, not a
world-priority survey. The maintained claims are
[FLOW-018](../mathematics/clock_structure_and_noise_scale.md) and
[FLOW-019](../mathematics/fixed_degree_heat_projection.md).

## Prior kernels, with exact versions

P. J. Forrester, *Some exact correlations in the Dyson Brownian motion
model for transitions to the CUE*, arXiv:chao-dyn/9603010v1, 25 March 1996;
Physica A 223 (1996), 365--390. The canonical
[PDF](https://arxiv.org/pdf/chao-dyn/9603010) identifies itself as v1.
Raw pages 1 and 14--16 were read; page 16 was also visually inspected.
Sections 5.1--5.2, (5.1)--(5.9), give equispaced initial data and their
finite and thermodynamic biorthogonal kernels. These are prior results.
The project uses FLOW-007's separately derived odd-N normalization and
not a verbatim transcription of the source's even-N indices.

The dimensionless parameter in FLOW-018 is $\tau=Nt$ for the project
generator with individual angle noise variance $dt/N$. At unit unfolded
density its ordinary spatial diffusion time is $\tau/(4\pi^2)$.
The source's theta nome matches $e^{-\tau/2}$ after time conversion.

There is a material source inconsistency to avoid importing. The **visible
PDF**, not just extracted text, prints a plus in (5.10), and states a
linear small-wave-number behavior. Direct Fourier integration of the
adopted equispaced kernel instead gives, in the open band $0<|\xi|<1$,

$$
s_\tau(\xi)=|\xi|(1-e^{-\tau|\xi|}).
$$

The finite-N identity $\mathbb E|p_m|^2=m(1-e^{-tm})$ for $0<m<N$
has value zero at time zero and derivative $m^2$, also obtained directly
from the independent radial/trace generator. A plus-sign expression
does not satisfy these initial data. The full stationary covariance
measure additionally has Bragg atoms at nonzero integers from the
averaged product of the conditional one-point densities; these atoms
cannot change the formula inside that open low-frequency band.
FLOW-018 does **not** import (5.4) or (5.10) as a theorem. This record
identifies the incompatibility with the present definitions; it does
not assert a checked correction to the journal version, which was not
read in this pass, or a newly discovered error in all editions.

M. Katori and H. Tanemura, *Non-Equilibrium Dynamics of Dyson's Model
with an Infinite Number of Particles*,
[arXiv:0812.4108v3](https://arxiv.org/abs/0812.4108), 19 June 2009;
Communications in Mathematical Physics 293 (2010), 469--497,
DOI 10.1007/s00220-009-0912-3. Raw pinned PDF pages 1--4, 7 and
20--21 were inspected, including (1.1), (1.5)--(1.7), Theorem 2.2 and
Section 4.3's kernel derivation. Their Brownian particle variance is
$ds$, so their equal-time parameter is $s=\tau/(4\pi^2)$.
After transposition and phase translation their lattice kernel agrees
with S9. Their lattice-to-sine mechanism is credited as prior; no new
infinite-dimensional SDE construction is claimed. FLOW-018 proves its
finite-circle limit directly, avoiding a transfer from a different
finite line truncation or the paper's stronger initial-configuration
topology without checking it.

Exact-ID local source searches found no retained PDF for these two
versions. Raw source pages were accessed through the PDF query service;
the canonical Forrester PDF was additionally rendered by the web reader.
Version-suffixed web URLs were unavailable in this pass. No local PDF
byte hash is invented, and tool-extracted text is not relabelled as
downloaded source bytes.

## Stable-range moments

FLOW-019 uses the already authenticated EXT-DE-2001 source:
Diaconis--Evans, *Linear functionals of eigenvalues of random matrices*,
Theorem 2.1(a), printed pp.3--4 of the author-hosted Berkeley report 577.
The existing [exact-source entry](signed_heisenberg_sources.md) was read.
No new PDF acquisition or full re-refereeing is claimed. Its hypothesis
mapping here is explicit: each Gram product has both weighted degrees
at most $2Q\le N$. The stable Gaussian Gram matrix is not assumed
outside that range. The generator's invariance and evaluation bounds
are project derivations from FLOW-015 and FM-013.

## Overlap and search scope

Discovery used two search engines with equispaced/crystalline Dyson
initial data, clock relaxation, Bragg peaks, structure factors and
synchronous eigenangle contraction. The closest primary kernels were
verified as above, with the bibliography and Section 4.3 of
Katori--Tanemura consulted for attribution. A recently indexed
infinite-Dyson extension was a discovery hit only and is not imported.
This was not a complete forward-citation or all-language search.

Classification: the critical kernel and lattice relaxation are **known
after normalization**. The finite second moment, signed mesh compensation,
pair rate and fixed-degree projection estimates are presented as
**formal/project derivations from prior or standard inputs**, with no
claim that these formulas or rates are new to the literature. Monotone
drift contraction and Ito moment induction are standard mechanisms.
The original-chain critical all-order consequence uses separately proved
project comparison estimates. None of these sources proves actual-map
noise removal or full deterministic BGS.
