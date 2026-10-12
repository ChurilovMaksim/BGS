# Haar feedback: source comparison and priority boundary

Checked 12 October 2026 against the primary sources below. This note
distinguishes prior mathematical objects from the self-contained proof of
[TRACE-076](../mathematics/haar_feedback_clock_law_20261012.md).
No world-priority claim is established.

| Primary source | Exact locator read | Relation to this result |
|---|---|---|
| P. Bourgade, J. Najnudel and A. Nikeghbali, *A unitary extension of virtual permutations*, [arXiv:1102.2633v1](https://arxiv.org/abs/1102.2633v1), 13 February 2011 | Introduction: Hermitian Hua–Pickrell density at parameter zero, Cayley transform and Schur projection; Proposition 3.2 and its Haar compatibility proof | Haar-compatible unitary projections and the Hermitian Cauchy ensemble are prior. The introduction credits Neretin's projection construction. |
| Y. A. Neretin, *Matrix beta-integrals: an overview*, [arXiv:1411.2110v2](https://arxiv.org/abs/1411.2110v2), 16 January 2015 | Section 2.2, equation (2.3), printed page 4; Section 2.3, printed pages 5–6 | Rectangular determinant beta integrals, singular-value Jacobians and their Selberg reductions are prior. |

The first article's current HTML renderer displays a later date inside the
document. The pinned identity here is its arXiv v1 submission, not that
renderer date. The overview's rectangular formulas must be read with the
appropriate smaller dimension; the maintained proof independently derives
the Jacobian using \(r=\min(q,u)\), including the singular regime \(q<u\).

Our proof derives, rather than assumes, the Cayley Haar density, both block
Jacobians, the graph factorization, the feedback derivative coupling,
the exact rectangular eigenvalue law and its finite-moment boundary.
Its unconditional clock conclusion uses the already maintained
TRACE-060 theorem; the Haar marginal gives the required all-time
probability bound. Binary relative entropy then gives the
\(O(\log N)\) initial-law extension with the order of limits stated
explicitly. These derivations are internally reviewed project results.
They do not assert that Cauchy, matrix-beta, Jacobi, Haar-preserving Schur
projections or general entropy event bounds are newly discovered.

No external theorem from these two papers is a load-bearing leaf of the
finite factorization proof. Therefore the external registry retains its
46 entries. The inherited TRACE-060 concentration leaf keeps its existing
Tropp locator. Its [explicit impact review](../record/bibliographic_impact_haar_20261012.json)
adds TRACE-076 as a transitive user for the clock corollaries only; all
source observations and earlier cache bytes remain unchanged.
No claim is made that these sources transfer a Haar
ensemble to the maintained deterministic quantum map or prove BGS.
