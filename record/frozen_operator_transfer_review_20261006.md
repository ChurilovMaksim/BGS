# Independent internal review: actual Weyl transfer and common-noise moments

**Claim:** BGS-FM-018. **Base:** `89645900bdbaace5d4956f306f6dccc464163e35`.
One fresh read-only reviewer reconstructed the new implications in three
successive passes. These are passes by one reviewer, not external referee
reports. The author independently checked the primary sources and executed
the maintained exact checker and the separate Wolfram source.

**Closing verdict: O1--O29 proved as written**, relative to the inherited
FM-001 symmetry/Anosov and FM-006 normalized-area Gibbs inputs and the
explicitly checked classical mixing leaf. No full deterministic BGS,
uniform reduced two-copy rate, external priority or analytic formal
certificate follows.

## Obligations and dependency boundary

| Obligation | Independently reconstructed implication | Exact scope |
|---|---|---|
| O5--O10 | Integer-label Weyl/metaplectic signs, sin commutator remainder, uniform operator Egorov bound and aliased trace pairing | Actual finite Fourier symbol; alias signs retained; full smooth input and growing low band |
| O11--O14 | Classical correlations with product Sobolev norms, min with the trivial bound, whole-band twisted average and admissible logarithmic time/power band | Checked PP Proposition 2.4 and coding; inherited area Gibbs identification; noneffective positive exponent |
| O2--O4, O15--O18 | Complete spectral-arc low-frequency exclusion, diffusion coercivity and all-noise singular gap | Traceless actual adjoint; all twists; arbitrary degeneracies; no normality assumption |
| O19--O20, O24 | Actual full-band generator discrepancy, Heisenberg annealed trace limit and signed ramp mismatch | Does not identify fresh-step trace with fixed-matrix spectral moments |
| O21--O23 | Exact two-pair Gaussian Hamiltonian realization and massive quadratic block at a microscopic source | Product kicks in the displayed order; source functional's higher terms and zero-mode approximation unestimated |
| O25 | Identical one-copy channels but different rank-one nonlinear factors and fourth spectral moments | Two finite control ensembles, not perturbations or counterexamples to the actual map |
| O26--O28 | Exact common-noise higher-copy channel, noncommuting two-copy generators and unavoidable swap invariant | Same Gaussian parameters in every copy; independent-copy tensorization would change the target |
| O29 | Full-support equality argument, explicit Weyl generation of su(N) and elementary two-copy commutant | Every finite odd N>=3, including composite dimensions, every u>0, any unitary U; no large-N rate |

The reviewer independently inspected Parry--Pollicott Proposition 2.4
and Appendix III.3, and Zirnbauer's §5 quadratic/nonlinear distinction.
The complete source inventory and exact locators are in the
[source review](../literature/frozen_operator_transfer_sources_20261006.md).
Ruelle/Pesin inputs behind FM-006 and the entire FM-001 proof remain
inherited; this was not a new audit of their complete dependency closure.
The Fannjiang--Nonnenmacher--Wołowski and Nonnenmacher papers are prior-method
attribution and boundary checks by the author, not fresh theorem imports
or independently certified priority.

The last pass checked the full-support Gaussian equality pointwise,
including zero noise; the complexified Lie generation at composite N
requires only nonzero sine coefficients, never an invertible residue.
It then derived the two-copy commutant directly using diagonal phases,
coordinate permutations and one mixing generator. The peripheral
eigenvalue must be 1. Its complement is reducing, so finite-dimensional
compactness gives a positive minimum singular value on the unit circle.
The proof gives no estimate of that minimum as N grows and u shrinks.

## Acceptance pins and correction

| Reviewed or promoted version | SHA256 |
|---|---|
| Accepted O1--O25, with explicit odd N>=3 control-ensemble scope | `63853e1b80cc451e01e9d94945066eea2169afef7f2da52dd071db728bc8ee41` |
| Accepted O1--O28, adding the exact common-noise calculation | `e11d3ef2c54af449e1ae00bbd1d2786cf2545915365cc8cbfb3febd463476d88` |
| Accepted O1--O29 mathematical body | `7de52d7a140fc8f6c74ba56fdd755cc06d55f2917605039c185669f30ba420e4` |
| Promoted proof, updated status and review links only | `ea668cded8831626a15462285ff915cc9e29139dac5a326d104e6e850742ff4c` |

The early pass requested an explicit odd N>=3 restriction for O25; it is
present in the accepted source. No mathematical correction was required
in the final O29 pass. The reviewer reproduced the preceding accepted
O1--O28 hash by restoring that version's closing text. The author compared
the accepted and promoted files after the `## 1. Objects and conclusions`
heading: their complete mathematical bodies are byte-identical.
The hashes identify review scope, not a formal proof certificate.

## Execution and limits

The maintained
[Python checker](../computations/verification/frozen_operator_transfer_coercivity.py)
uses only exact integer phases, integer cyclotomic polynomials and rational
real/imaginary pairs, including an inherited exact frequency-map helper.
Its [contract](../evidence/20261006/frozen_operator_transfer_contract.json),
[bounded manifest](../evidence/executions/20261006/operator-transfer/manifest.json)
and [results](../evidence/executions/20261006/operator-transfer/checks.json)
state every range. It does not compute the actual asymptotic spectrum,
fit an exponent, integrate the nonlinear functional or certify the analytic
gap. A separate exact cyclic example tests the gap mechanism in a different
representation. Composite-dimensional finite Lie-generation controls
supplement the general proof.

The reviewer used additional floating small-dimensional diagnostics,
including N=3,5,9 for finite control moments/noncommutation and residue
generation at N=3,9,15,21. They are reviewer diagnostics, not the author's
reproducible exact evidence packet or an asymptotic certificate.
The maintained checker and Wolfram evaluation are author executions;
they are not attributed to the reviewer.

The [Wolfram source](../computations/verification/frozen_operator_transfer_checks.wl)
returned six explicit True identity checks. The
[raw response](../evidence/20261006/frozen_operator_transfer_wolfram.json)
also preserves the MinValue/MaxValue and general diagnostic messages.
The service did not return kernel version, effective cap or kernel runtime.
These symbolic controls are supplementary and do not replace the separately
recorded exact arithmetic or the analytic review.

The actual unregularized signed stable-band statistic, higher factorial
counterterms, the nonlinear determinant integral, TRACE-005 and
BGS-BGS-001 remain **OPEN**. No world novelty, external refereeing or new
analytic Lean certificate is claimed.
