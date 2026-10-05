# Sources and scope for the all-order continuation

Checked 5 October 2026 from base
`be2e7a9c236df20a0e026a714c8c97327bde973a`.
This is exact-source verification and a bounded overlap search, not a
certification of world priority or of a solution of BGS.

## Spatial ergodicity actually used

Alexander Soshnikov, *Determinantal random point fields*,
[arXiv:math/0002099v4](https://arxiv.org/pdf/math/0002099v4),
28 November 2000. Section 3, printed pp.38--42; Theorem 7 at p.40.
The version header and raw page text were checked through alphaXiv's PDF
query tool, in addition to the earlier
[project extraction](return_local_limits_sources.md). The theorem gives
ergodicity, mixing of every multiplicity, and absolutely continuous spectra
under spatial translations for the translation-invariant determinantal
fields in the source's setting on $\mathbb R^d$ or $\mathbb Z^d$.

For this application, $d=1$ and the intensity-one sine kernel is the
Fourier projection onto $[-1/2,1/2]$ under the $e^{2\pi i x\xi}$ convention.
It is Hermitian, a positive contraction, and locally trace class. Its
determinantal probability law is translation invariant. Thus the spatial
ergodicity conclusion applies. Local factorial observables belong to $L^2$
by the determinant bound and finite count moments. The mean ergodic theorem
then supplies convergence of their spatial averages in $L^2$. Periodic-law
Jensen and the order of limits are proved in FLOW-017, not quoted from this
paper. Temporal ergodicity of an infinite Dyson diffusion is not used.

Cache lookup for the exact identifier found no retained PDF in this
workspace. Raw extracted pages were inspected; no PDF-byte hash or local
PDF availability is claimed. The imported result is **known after
translation of notation**. A renewed public source read is recorded rather
than silently changing the September extraction.

## Quantum-graph route: no imported arrow

Sven Gnutzmann and Alexander Altland, *Universal Spectral Statistics in
Quantum Graphs*, [arXiv:nlin/0402029v2](https://arxiv.org/pdf/nlin/0402029v2),
27 September 2004. Raw title/setup pages 1--2 were checked through PDF
queries. The PDF's generated title date differs from the arXiv version
header; the latter pins the inspected version.

The spectrum is defined by zeros of the secular determinant as a function
of wave number. The two-point correlation uses a wave-number/energy
average. Rational independence of bond lengths converts that average into
an average over bond phases (their equation (2)). The paper's classical
mixing condition is used in that graph and averaging setup, with its stated
symmetry assumptions. None of those averaging hypotheses is shown to hold
for the one fixed matrix $U_N$ in this repository. Therefore no theorem
from this paper is registered as a load-bearing input. A stochasticity
matrix spectral gap alone does not provide the missing mapping.

## Transport route and overlap boundary

Web discovery used “point process transport local moments Hardy Littlewood
maximal”, “unitary Schatten eigenvalue matching geodesic eigenangles Lp
perturbation theorem”, and the Soshnikov theorem title. A separate graph
query used “quantum graphs spectral universality rational independence
spectral gap”. Primary source inspection was confined to the two papers
above; adjacent geometry/perturbation hits were discovery leads only.

Hardy--Littlewood strong bounds, moment interpolation, unitary path
perturbation and the ergodic averaging principle are standard. FLOW-016
proves its particular packing estimate directly and applies already
maintained covariance estimates; FLOW-017 is an extension of those chain
estimates. Neither result is labelled apparently new worldwide. No full
backward/forward citation search, probability-textbook survey or exhaustive
comparison with stochastic averaging literature was performed. The exact
candidate formulas are project derivations with **priority unverified**.
