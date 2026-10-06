# Sources and attribution for the clock moment-channel control

Checked 6 October 2026. This is a bounded attribution check, not a novelty survey.

## Character rigidity

Dipendra Prasad, *Half the sum of positive roots, the Coxeter element, and a
 theorem of Kostant*, arXiv:1402.5504v1, 22 February 2014.
Primary source: https://arxiv.org/html/1402.5504
Theorem 1 states that an irreducible finite-dimensional representation of a
simply connected complex semisimple group has character in {0,1,-1} at its
Coxeter element. The paper explicitly attributes the result to Kostant.

The present proof evaluates the U(N) Weyl alternants directly at all Nth
roots. It thereby handles even N and balanced central characters without
silently identifying D_N with a determinant-one Coxeter lift. The general
character theorem is prior; this elementary specialization is not claimed
as new. Standard highest-weight classification and Weyl character/dimension
formulas are mathematical background, not computational discoveries.

## Isospectral averaging

Lorenzo Leone, Salvatore F. E. Oliviero, Alioscia Hamma,
*Isospectral twirling and quantum chaos*, arXiv:2011.06011v7, 14 July 2021.
Primary source: https://arxiv.org/html/2011.06011
Section 2 defines Haar-conjugate isospectral unitary families and their
moment twirls. This authenticates prior methodology. Its tensor arrangement
is not silently equated with a vectorized superoperator: our proof explicitly
uses U^tensor k tensor conjugate(U)^tensor k.

Neither this source check nor the earlier audit establishes that the exact
all-k clock bound or its universality application is globally new. The only
novelty comparison asserted is against the searched maintained BGS corpus:
TRACE-013 and frozen_spectral_flow_controls.md are related but different
negative controls.

## Dependency distinction

The proof reconstructs the relevant character evaluation and two-copy
constituents. No unverified external chaos/universality theorem is used.
The Sine₂ variance comparison uses the defining determinantal kernel; the
Haar trace identity is a supplementary standard hook-character calculation,
not needed for the lattice obstruction. Source HTML was read in the audit;
no PDF cache or independent publisher-version check is claimed.
