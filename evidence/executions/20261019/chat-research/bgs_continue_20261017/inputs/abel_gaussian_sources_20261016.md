# Source and priority audit: Abel rigidity and the flat Gaussian comparison

Checked 16 October 2026. This is a precise mapping of inputs, not a world-priority
certificate. Classical Gaussian formulas, Schur identities and sphere moments
are not being presented as discoveries of this project.

| Primary source | Exact locator | Use and limit |
|---|---|---|
| C. Kristjansen, J. Plefka, G. W. Semenoff, M. Staudacher, [A New Double-Scaling Limit of N=4 Super Yang-Mills Theory and PP-Wave Strings](https://arxiv.org/abs/hep-th/0205033), v2, 3 June 2002 | Equations (2.4), (2.8), Appendix A; PDF pages 5, 7, 20--22 | Classical unscaled Gaussian trace moment, with factor 1/(m+1), and the sinh double-scaling function. Their displayed finite formula assumes N>m; the project kernel derivation covers m>=N too. |
| S.-S. Byun, P. J. Forrester, [Progress on the study of the Ginibre ensembles I: GinUE](https://arxiv.org/html/2211.16223v3), v3, 12 January 2023 | Propositions 2.1--2.2, equations (2.3), (2.9)--(2.10) | Normalized Ginibre eigenvalue PDF and finite determinantal kernel. Monomial integration in the project gives the precise trace specialization and Schur norm. No physical BGS theorem is imported. |
| G. Akemann, G. Vernizzi, [Characteristic Polynomials of Complex Random Matrix Models](https://arxiv.org/pdf/hep-th/0212051), v2, 12 December 2002 | Section 6, equation (6.2), PDF page 18 | Useful prior literature, but its printed Gaussian trace formula omits 1/(m+1). It is not used as a correctly normalized input. |
| H. Cohn, A. Kumar, [Universally optimal distribution of points on spheres](https://arxiv.org/abs/math/0607446v2) | Theorem 1.2, already pinned as EXT-CK-2006 | Prior universal optimality supplies the clock floor in TRACE-007. The new Abel decomposition and its stability proof are self-contained; no priority is claimed for the minimum. |

The normalization discrepancy is detectable already at m=1: unit-variance
independent entries give E|Tr Y|^2=N, whereas the expression printed in the
later equation (6.2) gives 2N. The original 2002 equation (2.4) contains the
correct divisor. The PDF text and page were inspected. This is an audit of
the pinned versions, not a claim about every later edition.

For m/sqrt(N)->c, the Gaussian benchmark divided by m has the prior limit
sinh(c^2/2)/(c^2/2). The earlier project TRACE-089 transfers that expression
to its positive equal-edge sector in its stated window. TRACE-093 proves a
stronger relative comparison for every m=o(N), using a different Fock/Haar
argument. Priority of that comparison, its Heisenberg rate transfer and
collision results has not been exhaustively established.

The Abel Fourier minorant is an instance of the standard positive-Fourier
energy method. Its explicit transform, periodization, general stationary
gap argument and sharp exponent are derived in TRACE-092. A search for
universal optimality and Cauchy/lattice stability identifies related energy
minimization literature but does not certify novelty of the particular
quantitative statement. It is appropriate for external mathematical review;
it is not evidence of a Fields- or Poincare-level contribution.

Wolfram evaluated the three displayed symbolic residuals as zero and returned
the small-s expansion of the CUE low-mode integral. The exact executed
[Wolfram source](../computations/verification/research_20261016/abel_identity.wl)
and [returned output](../evidence/executions/20261016/abel-gaussian/wolfram_result.json)
are supplementary checks. The generic theorems are established by the written
arguments, not by the computer-algebra output or a source citation.
