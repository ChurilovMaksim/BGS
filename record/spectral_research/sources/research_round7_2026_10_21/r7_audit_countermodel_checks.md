> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round7_2026_10_21/r7_audit_countermodel_checks.md`. Embedded SHA256: `7eb286ea14bd946ac4518d45a43cb7cc7dd5621b0dde171812e64868ba815b8a`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/closure.md).

# Independent exact countermodel checks

**All checks passed.** No earlier checker was imported or executed.

These finite checks supplement the analytic proof in r7_audit_countermodel.md. They do not construct the generic algebraic eigenbasis, numerically test transcendence, or approximate the long return tail.

| Check | Assertions |
| --- | ---: |
| Hessian inverse | 20 |
| N^12 normalized moment bound | 9 |
| all-subset binary exponents | 4 |
| alternating reverse-edge coefficient | 20 |
| complete two-dimensional Gauss norm | 1604 |
| completed-square identity | 163316 |
| direct nontrivial trace modulus | 20 |
| exact formal base first returns | 92 |
| full reverse-edge phase | 163316 |
| multiplicity trace cross-check | 20 |
| nontrivial ordered binary differences | 4032 |
| outside probability exponent | 9 |
| positive return-probability bracket | 9 |
| raw finite-field group law | 17667 |
| reverse-edge nonsingularity | 20 |
| reverse-edge row orthogonality | 1604 |
| spectral multiplicity range | 3 |
| spectral multiplicity total | 3 |
| weighted-cycle product | 20 |

The raw finite-field calculations use primes 5, 7, and 11, including every field parameter in each stated finite loop. Cyclotomic checks use exact integer coefficient vectors modulo the prime cyclotomic polynomial.

Binary ordered differences were checked on indices 0 through 63. All subset exponents on 14 indices were checked at powers -7, -1, 1, and 13. Their universal injectivity and applicability to every nonzero integer power are proved analytically in the audit.

| Source | SHA-256 |
| --- | --- |
| research_round7_2026_10_21/root_unipotent_flat_clock.md | 8f8e4cdbcd5c6576eb6bb9ce976d7a29ae4e77a310271576719ee8e39ad9d0bd |
| research_round7_2026_10_21/r7_return_generic_microperturbation.md | 1127ad366de39f1c9293bb54fa4fe9ca88183e3baf44d355262f031d73b6cb34 |

Reproduce with:

    python research_round7_2026_10_21/r7_audit_countermodel_checks.py
