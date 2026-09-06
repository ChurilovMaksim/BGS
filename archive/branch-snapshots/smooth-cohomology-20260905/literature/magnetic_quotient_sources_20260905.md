# Source audit for the magnetic-quotient route

Date: 2026-09-05. Scope: primary-source metadata and abstracts, not a complete
priority review. No external result below is silently used as a theorem in
`mathematics/magnetic_quotient_semicircle.md`; its stated proof is self-contained.

## Relevant comparison objects

Shamgar Gurevich and Ronny Hadani, *The statistical restricted isometry
property and the Wigner semicircle distribution of incoherent dictionaries*,
arXiv:0812.2602. This concerns normalized Gram fluctuations of incoherent
dictionaries, including constructions from finite harmonic analysis. It
prevents describing semicircle behavior in finite harmonic analysis in general
as new. It is not, on the basis of the abstract alone, a verified theorem for
this repository's odd H-invariant compressed Weyl operator.

Arthur Forey, Javier Fresan, Emmanuel Kowalski and Yuval Wigderson,
*Spectrally indistinguishable pseudorandom graphs*, arXiv:2511.21351
(26 November 2025), and *Jacobian graphs*, arXiv:2603.13198 (13 March 2026).
These are relevant arithmetic graph/spectral constructions. The global law
for an explicit graph family must not be confused with microscopic BGS
universality or automatically transferred to the magnetic quotient here.

Lior Rosenzweig, *On the fluctuations of matrix elements of the quantum cat
map*, arXiv:0909.1410. Matrix-element fluctuation results concern a different
observable/statistic from a proof of microscopic propagator eigenphase laws.

## What remains unverified

This pass does not establish that the exact compressed-observable theorem is
absent from the literature, does not claim priority, and does not replace a
full comparison of assumptions, normalizations, randomization, symmetry
sectors and limits. Abstract-level overlap is recorded as overlap, not as
identity of models or as a novelty certificate.

The project proof explicitly exposes its restrictive regime K=o(log p) and
the obstruction to that regime for the orders of one fixed hyperbolic integral
cat map. Removing that restriction and obtaining Heisenberg-scale local
statistics are separate, unresolved research tasks.
