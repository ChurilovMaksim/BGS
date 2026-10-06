# Collective diffusion: attribution and dependency scope, 6 October 2026

This check accompanies `BGS-FM-019`. The uniform two-copy bound is proved
directly by exact Weyl blocks and a lattice Poincare argument. No new
external theorem is a load-bearing leaf. FM-018's Weyl conventions,
Gaussian calculation and one-step actual-map Egorov estimate are inherited;
its classical mixing theorem is not used in the new diffusion-gap proof.

## Primary sources inspected

| Source and exact locator | What was inspected | Relation and boundary |
|---|---|---|
| E. Onorati, O. Buerschaper, M. Kliesch, W. Brown, A. H. Werner, J. Eisert, *Mixing properties of stochastic quantum Hamiltonians*, arXiv:1606.01914v3, 21 February 2017; CMP 355, 905--947, DOI 10.1007/s00220-017-2950-6 | Full primary PDF; Section 5, Lemma 15, equations (51)--(54), printed pp. 15--16 | Prior moment-semigroup construction for unitary Brownian noise and its invariant sector. The many-body local model and its gap hypotheses do not supply the particular four-Weyl-Hamiltonian, all-odd-N bound D2. No novelty is claimed for shared-noise moment semigroups or their design applications. |
| A. Blumenthal, M. Coti Zelati, R. S. Gvalani, *Exponential mixing for random dynamical systems and an example of Pierrehumbert*, arXiv:2204.13651v1, 28 April 2022 | Full primary PDF; Section 5.3, Proposition 5.5 (two-point irreducibility), and Section 5.4, completion of Theorem 1.1 through Harris conditions | Prior classical alternating randomized-shear mixing. It does not prove a finite-dimensional quantum collective gap or a signed spectral transfer for U_N. The new lattice proof imports none of these ergodic theorems. |
| W. Zhang, *Exponential Mixing for Hamiltonian Shear Flow*, SIAM J. Math. Anal., DOI 10.1137/25M1751876 | Publisher's primary abstract and metadata only, not its full proof | A related recent Hamiltonian-shear result. No theorem, constant, or hypothesis transfer from this source is asserted. |

Primary URLs: [Onorati et al. PDF](https://arxiv.org/pdf/1606.01914v3),
[Blumenthal et al. PDF](https://arxiv.org/pdf/2204.13651v1),
[Zhang publisher page](https://epubs.siam.org/doi/abs/10.1137/25M1751876).
General design comparisons also returned Haferkamp's 2022
[random-circuit paper](https://quantum-journal.org/papers/q-2022-09-08-795/);
only its publisher summary was read, and no result is imported.

## Search and priority boundary

A project-local source-cache lookup returned no retained cache. Targeted
searches used both available engines for collective Weyl/Brownian moments
and randomized shear/two-point mixing. They located the sources above but
did not establish exhaustive coverage or first publication of D2.
The conceptual Brownian/design and alternating-shear methods are prior.
Whether this exact torus-generator bound or its all-parity lattice proof
is already in another source has not been established. A missing search
hit is not evidence of novelty, prize-level significance or BGS closure.

The mathematical dependency for D2--D23 is self-contained finite Weyl
algebra, positivity, elementary lattice paths/geometric sums, projection
algebra and contraction Duhamel. D24--D25 additionally inherit the exact
physical operator and the one-step smooth-symbol Egorov estimate of
FM-018. No claim about individual-noise operator-norm closeness, a long
product Egorov theorem, higher-copy uniform rates or the original
deterministic signed spectrum is justified by these references.
