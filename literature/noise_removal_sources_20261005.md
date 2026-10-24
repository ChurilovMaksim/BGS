# Exact source boundaries for deterministic noise removal

Checked 5 October 2026. This is an exact implication/source audit, not a
priority or exhaustive literature review. The new proof is
[microscopic_noise_removal.md](../mathematics/fixed-map/microscopic_noise_removal.md).

| Primary source actually read | Exact locator | Translation and permitted use | Unsupported inference |
|---|---|---|---|
| T. Lemoine, *Almost flat highest weights and application to Wilson loops on compact surfaces*, [canonical PDF](https://arxiv.org/pdf/2303.11286), internally marked arXiv:2303.11286v3, 26 May 2025; title-page date 27 May | Section 1.2, printed p.3; Section 2, (17)--(18), printed p.10 | Prior character heat multiplier and normalized unitary Casimir. Project generator is half the normalized Laplacian; for highest weight (r,0,...,-r) the decay rate is r(r+N-1)/N. Fundamental and determinant characters both have rate 1/2 for full Brownian motion; traceless motion has determinant rate zero and fundamental rate (1-N^-2)/2. The project rederives the charge-zero multiplier with the Vandermonde heat conjugation. | Yang--Mills large-N results do not prove deterministic local spectral universality; a global character is not a compact local Laplace test. |
| M. Erbar, M. Huesmann, T. Leblé, *The one-dimensional log-gas free energy has a unique minimiser*, [canonical PDF](https://arxiv.org/pdf/1812.06929), internally arXiv:1812.06929v1, 17 December 2018; title-page date 18 December | Theorem 1 and Corollary 1.1, printed p.2; Definition 2.9, (2.17), and Definition 2.10, (2.18), p.7 | Prior variational characterization of Sine_beta, with the source's intensity-one convention and specific entropy relative to Poisson. The finite periodic spectral-field entropy calculation is elementary and proved separately. | Mere stationary unit intensity, noisy convergence, or finite-N deterministic empirical fields do not supply the minimizing property. A limit's entropy cannot be bounded above by invoking lower semicontinuity. |
| H. Osada, R. Tsuboi, [*Ergodicity of unlabeled dynamics of Dyson's model in infinite dimensions*](https://arxiv.org/pdf/2203.15036), source title/setup read | Theorems 1.1--1.2, printed p.5; Lemma 5.1, p.12 | Discovery/source-scope check only: ergodicity in L2 of the stated sine_2-reversible Dirichlet form and extremality of that invariant law. No theorem from this source is imported into FLOW-015. | Ergodicity for a specified invariant law is not identification of every possible stationary microscopic subsequential limit. |
| P. Bourgade, J. Huang, [*Loop Equations Characterize Random Matrix Statistics*](https://arxiv.org/abs/2607.07617) | Primary title/author/abstract rechecked against the existing EXT-BH-2026 record | The existing full-loop-hierarchy route is retained as a distinct conditional route. This pass does not re-certify every hypothesis of Theorem 1.9. | D17's unscaled full-class stationarity obstruction does not refute normalized microscopic mixed loop equations. |

The two first canonical PDFs were successfully read, including their
internal version headers and the displayed formulas/definitions. Fetches
of the version-suffixed PDF URLs returned an unavailable-source error.
No local PDF bytes or SHA-256 are claimed: the exact-ID local cache
lookups returned no cache, and the browser source was not converted into
a fictitious downloaded artifact. The mathematical character calculation
is also independently given in D18--D19; the entropy proof uses the
explicit definition in D21.

The inherited clock kernel and its asymptotic Fredholm bound are already
credited to Forrester in [the 29 September source review](quadratic_noise_sources_20260929.md).
The prior factorial Fourier/Mobius bridge and prior arbitrary-start noisy
relaxation are cited directly in FLOW-015. Neither is presented as new.

Search scope: primary-source discovery used unitary Brownian character/
Casimir terminology, static infinite-Dyson invariance, sine-beta Gibbs
uniqueness and log-gas free-energy uniqueness. The search led to the
specific sources above and an additional no-spectral-gap paper, whose
theorem was not imported. No absence of other character, heat-flatness,
entropy or deterministic-transfer results is asserted. The new statements
are project proofs/diagnostics; their world priority is unestablished.
