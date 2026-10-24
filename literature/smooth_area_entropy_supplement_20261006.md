# Smooth-area entropy: subsequent source verification

**6 October 2026; documentation supplement subsequent to the final local
validated snapshot.** This verifies an alternate primary source for the
entropy input in FM-006 §2 and inherited by FM-018 §4/O11. It changes no
mathematical statement or executable source. It is statement, errata and
applicability verification, not an independent proof audit of the complete
external article or the downstream dependency chain.

## Primary source and corrections

Ricardo Mañé, *A proof of Pesin's formula*, **Ergodic Theory and Dynamical
Systems 1** (1981), 95–102,
[DOI 10.1017/S0143385700001188](https://doi.org/10.1017/S0143385700001188),
[primary PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/99FF7E606E946F18BE42244090483E70/S0143385700001188a.pdf/a-proof-of-pesins-formula.pdf).
Printed p.95, equation (2) (PDF page 1), gives metric entropy as the integral
of the nonnegative Lyapunov exponents counted with multiplicity. Its
hypotheses are a diffeomorphism of a compact boundaryless manifold,
Hölder-continuous derivative, and an invariant probability absolutely
continuous with respect to Lebesgue measure. Ergodicity is not required.

The full **1983 errata**, *ETDS 3*, 159–160,
[DOI 10.1017/S0143385700001863](https://doi.org/10.1017/S0143385700001863),
[primary PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C51073A9D0F762D8884597FA5EC831CC/S0143385700001863a.pdf/errata_to_a_proof_of_pesins_formula.pdf),
were checked. Item (1), p.159, replaces the p.99 equation (11) bound
$\beta$ by $\beta^n$. Item (2) makes Lemma 3's bounds explicit:
$0<\delta<\lambda/[\alpha(1+c)]$ and
$0<\delta<(\lambda-\beta)c/[\alpha(1+c)^2]$.
Item (3), pp.159–160, uses these bounds in Lemma 4; they remain valid with
$\lambda,\beta$ replaced by their positive integer powers. None changes
equation (2) or its hypotheses. The displayed corrections were checked
against the primary PDF, not only its incomplete text extraction.

Retrieved PDF SHA-256 values (2026-10-06):

- 1981: `4746cc83428da9b1a3effab8f392ec6a5af0cb14d2f6cb0f36a124ac63397a7b`
- 1983: `06fe4e930bb0777916b3067eec2fabd68212e8a7d9cb418c1011cfc4db3613c3`

PDFs are not redistributed in this repository. Hashes identify the inspected
copies; they are not proof certificates.

## Dictionary to the maintained argument

In [FM-006](../mathematics/fixed-map/nonlinear_bracket_pressure.md), take
$M=\mathbb T^2$, $f=G_\kappa=S\circ\Phi_g^\kappa$ and $\mu=m$,
normalized smooth area. The analytic area-preserving Anosov properties are
the named [FM-001](../mathematics/fixed-map/fixed_model_symmetry_theorem.md) inputs.
Analyticity on the compact torus supplies Hölder derivative; area
preservation supplies invariance and absolute continuity.

For the one-dimensional unstable bundle and
$\phi=\log\|Df|_{E^u}\|$, multiplicativity gives
$\log\|Df^n|_{E^u}\|=\sum_{j=0}^{n-1}\phi\circ f^j$.
Anosov hyperbolicity makes the unstable exponent the only positive
exponent. Birkhoff's theorem and invariance therefore give
$\int\chi\,dm=\int\phi\,dm$, without requiring ergodicity first.
The cited formula yields precisely $h_m(f)=\int\phi\,dm$.

Together with the already named Ruelle inequality and variational
principle, this yields $P(-\phi)=0$ and makes $m$ an equilibrium state.
The existing Hölder equilibrium-uniqueness input identifies the Gibbs state
used by [FM-018 O11](../mathematics/fixed-map/frozen_operator_transfer_coercivity.md).
This supplement does not independently re-audit those other inputs or
assume a smooth structural conjugacy.

## Provenance boundary

The original audit correctly recorded that the **Pesin (1977) primary text
was not retrieved**. Its claimed Theorem 5.1 / printed p.81 locator remains
unverified in this pass. The theorem's attribution to Pesin is retained;
Mañé supplies an alternate published proof with verified statement and
errata. Original audit findings, source hashes, execution receipts and
snapshot identities are unchanged. The entropy-input retrieval gap is now
resolved through this alternate source, not by claiming recovery of the
1977 text. Universal algebraic FM-019/FM-020 results were already independent
of this entropy input at the implication level. No BGS or novelty claim is
added.
