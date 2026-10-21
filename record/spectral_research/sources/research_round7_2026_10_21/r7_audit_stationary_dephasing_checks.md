> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round7_2026_10_21/r7_audit_stationary_dephasing_checks.md`. Embedded SHA256: `58a6f5044838de401ab1e02bc37a6948214eb45e63c88b9153e9433a8c7ec1c8`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/dephasing.md).

# Exact checks accompanying the stationary-dephasing audit

21 October 2026. Integer and Gaussian-rational arithmetic only.

**Result: 78,425 assertions passed.**

| Group | Assertions |
| --- | ---: |
| exact complex eigenbases | 8 |
| stationary and eigenbasis positivity | 192 |
| exact Fejer compression | 36 |
| exact Fejer domination | 576 |
| signed first-return identities | 8 |
| Fourier embedding without aliases | 77,396 |
| Anosov cone constants | 8 |
| exact Fejer normalization | 200 |
| source pin | 1 |

The abstract finite identities were checked on complex rational unitary examples in dimensions 3, 4, and 5, including degenerate spectra. These are algebra checks and are not computations of the original tiny-kick family.
Signed first-return derivatives were checked directly using the compressed Ad(U) blocks in dimensions 3, 4.
Centered Fourier embedding was checked for every odd N from 3 through 65, polynomial coordinate degree up to five, and every retained input and output mode.
Ergodicity, compactness, all limit operations, and the original-family asymptotic conclusions have separate analytic proofs in the audit; the script does not claim to verify them by finite tests.

## Provenance

| Source | SHA-256 |
| --- | --- |
| research_round7_2026_10_21/r7_return_uniform_stationary_dephasing.md | c2bf50a33a642b984afa7bfa83fdc0d28b8019c79d4f47121ab52adee5e53075 |
| research_round7_2026_10_21/r7_return_all_fixed_powers_phase_separation.md | 46982efaa581d322d4e82d5f5782ccf69f979a5a59adfb863dd40ef292205527 |
| research_round7_2026_10_21/root_original_intensity_at_prescribed_phase.md | deea7755070222fdfca37d5c8f2721dc82b62afa34d56b18df614756308b5c63 |

Checker SHA-256: 1fa3708987334148dd8070a968b514d9aa6fdd4940d6b7fc275e4d4a71888098
