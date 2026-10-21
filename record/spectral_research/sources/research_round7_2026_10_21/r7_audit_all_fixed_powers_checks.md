> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round7_2026_10_21/r7_audit_all_fixed_powers_checks.md`. Embedded SHA256: `6e0289187425ddcb295566a1b98df37b6389ef5c18c4333b23c559d0084a8816`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Exact checks for the independent all-fixed-power audit

21 October 2026. All computations use integers and exact rational arithmetic.
No numerical flow, stationary-phase experiment, author checker, or prior audit checker is used.

**Result: 353,499 assertions passed.**

| Check group | Assertions |
| --- | ---: |
| exact corrected Fourier symbol | 69 |
| finite modular covariance | 308,520 |
| unitary Fourier coefficient | 12,340 |
| ordinary-half parity covariance | 11,500 |
| integer iterate and deck lattice | 1,280 |
| surviving Fourier labels | 256 |
| nontrivial induced translations | 3,069 |
| exact phase deck identities | 4,320 |
| image-kernel polynomial intertwining | 384 |
| all-odd Gauss differences | 738 |
| wrapped-grid phases | 1,280 |
| every intermediate stage word | 9,408 |
| fixed-tau constants | 7 |
| surviving Fourier coefficients | 3 |
| rectangular-cycle algebra | 324 |
| source pin | 1 |

## Scope

Direct modular covariance was checked on every grid point for each odd dimension 3 through 41 and all shifts and multipliers from -2 through 2.
Integer iterate and period-lattice identities were checked through R=256; every partial-stage noncommutative word was checked through R=96.
The exact Fourier symbol was rebuilt from the original prescription before applying the modular-half correction.
Image-phase identities and wrapped-grid phases use rational arithmetic; surviving Gauss differences include the common divisors listed below.
Polynomial rectangular cycles through separate degrees eight check the elementary algebra only.
The global analytic graph construction, no-translation theorem, decay of every Poisson alias, and the asymptotic WKB and return conclusions are proved analytically in the audit. These finite checks do not replace those proofs.

Observed Gauss common divisors: 1, 3, 5, 7, 17, 29, 35, 41, 51.

## Source provenance

| Source | SHA-256 |
| --- | --- |
| research_round7_2026_10_21/r7_return_all_fixed_powers_phase_separation.md | 46982efaa581d322d4e82d5f5782ccf69f979a5a59adfb863dd40ef292205527 |
| research_round6_2026_10_21/round6_main_report.md | 473b7b5b700a8ff17801eb9ca422c5949be15d0551c252e0b4035997db54b2bf |
| research_round2_2026_10_20/arithmetic_iterated_sector_covariance.md | c8e02b81819350ab52e7bc3dd791ffbeb1ae1a2192a9a99f1168c4c56d7123e2 |
| research_round5_2026_10_21/root_oscillatory_matrix_cancellation.md | ff98c2a2ee7dcd55b046c2039a86b2c206c3fcc170df3433c76f49281eff968d |

Checker SHA-256: e03e90c4ff8291279eee4671fd89cba9103399fef3bf4b56e4aea0f69a03f0d9
