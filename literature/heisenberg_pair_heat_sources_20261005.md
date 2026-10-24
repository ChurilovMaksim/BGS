# Exact pair heat formula: source and transfer boundary

5 October 2026. The mathematical derivation is in
[FLOW-021](../mathematics/fixed-map/heisenberg_pair_heat_formula.md).
No world-priority or exhaustive literature-search claim is made.

## Load-bearing inputs

The exact stable Haar Gram input remains Diaconis--Evans Theorem 2.1(a),
with the corrected degree gate recorded in
[the existing source audit](signed_heisenberg_sources.md).
FLOW-020 G6 supplies the Wick isometry and the full operator formula
proved in G15 supplies the reducing-space generator. Its displayed
interval alone would not suffice. G8 supplies the unchanged operator's
uniform exponential trace bound. All three dependencies are internal
proofs with their previously recorded review boundary. No new external
character theorem is needed for H5--H13: the generating-function
calculation proves the required hook eigenvalues and orthogonality.

## Prior cut-and-join mechanism

Thierry Levy, *Schur-Weyl duality and the heat kernel measure on the
unitary group*, [arXiv:math/0703690v2](https://arxiv.org/abs/math/0703690v2),
15 January 2008; primary PDF inspected at Proposition 2.3, printed
page 4. The standard-trace identity there has generator
$\Delta/2=-Nq/2-\mathcal C_q$ on holomorphic degree $q$.
Our normalized generator is $\Delta/(2N)$, hence
$-q/2-\mathcal C_q/N$. The neutral Wick tensor has two holomorphic
factors, giving $-q-(\mathcal C_q\otimes I+I\otimes\mathcal C_q)/N$.
This is prior group heat calculus, not a new mechanism or a theorem
about the fixed quantum map. The source is background attribution;
the required normalization is independently derived in FLOW-020.

## Executed alternative: Riemann--Siegel determinant resummation

P. Braun and F. Haake, *Chaotic maps and flows: Exact Riemann-Siegel
lookalike for spectral fluctuations*,
[arXiv:1206.4222v1](https://arxiv.org/abs/1206.4222v1),
19 June 2012. The full primary text was retrieved through alphaXiv,
including Sections 2, 3, 4.1--4.3; this was not an abstract-only check.
The web PDF endpoint failed in this session, whereas the primary-text
retrieval succeeded. No local PDF-byte hash is asserted.

Section 2, equations (8)--(11), gives the exact finite determinant
self-inversiveness and half-Heisenberg decomposition. Section 3,
equations (16)--(17), defines center-phase and offset averages.
Sections 4.1--4.2 use a semiclassical trace formula, orbit-count
replacement and diagonal phase matching. Section 4.3 reserves a
complete finite-N off-diagonal argument and describes bounded
order-by-order diagram cancellations. Thus the algebraic determinant
identity is available, but no quantitative, uniform Heisenberg-time
remainder for the prescribed fixed-strength U_N is imported here.

The exact dictionary is $F=U_N$, $A(z)=\det(I-zU_N)$, and
$t_j=p_j(U_N)$. The self-inversive relation holds at every finite N.
It still involves coefficients through order N/2. The new H22--H25
construction shows that these data cannot be recovered from arbitrary
sublinear short traces alone. The missing model-specific signed orbit
or determinant estimate remains an open route, rather than a refutation
of the resummation mechanism or of the source paper.

No paper retrieved in the bounded search was promoted to an external
proof of the maintained deterministic BGS target. This statement is
about the inspected sources and is not a claim about all literature.
