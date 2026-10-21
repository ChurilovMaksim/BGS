> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round7_2026_10_21/r7_audit_physical_fixed_powers49_checks.md`. Embedded SHA256: `35f5d75daad5dfc0b328ebf915045941fa94ec259783bd339a9a7e9b8a76d374`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent exact checks: physical powers through 49

**Result: all checks passed.** These finite computations check exact algebra and constants; the asymptotic conclusion is audited analytically in the companion report.

The script uses only integer/rational arithmetic and cyclotomic polynomial reduction. It never represents the fixed kick by floating point, imports an earlier checker, or samples an asymptotic limit.

## Check counts

| Check | Assertions |
| --- | ---: |
| Fourier majorants | 5 |
| Fourier support | 1 |
| Sigma closed formula | 50 |
| all-odd Gauss parity | 7500 |
| all-power raw label parities | 40800 |
| all-power support bound | 40800 |
| base master SHA256 | 1 |
| complex derivative majorants | 2 |
| cyclotomic construction | 103 |
| cyclotomic exact division | 14698 |
| direct finite Gauss norm | 282 |
| fixed-kick failure at 50 | 1 |
| fixed-kick sufficient range | 49 |
| general modular covariance | 64233 |
| inverse-label exclusion | 1225 |
| marked coefficient | 1 |
| marked frequency noncollision | 50 |
| modular generator covariance | 353700 |
| modular-half symbol correction | 1 |
| power arithmetic | 50 |
| power parities | 50 |
| printed R3 constants | 1 |
| printed Sigma49 | 1 |
| printed Sigma50 | 1 |
| raw covariance parity | 4050 |
| raw ordinary-half phase identity | 4050 |
| remaining Gauss quadratic phase | 62722 |
| symbolic polynomial identities | 6 |

## Exact constants

| R | Sigma_R | Lambda_R |
| ---: | ---: | ---: |
| 1 | 9 | 81 |
| 2 | 72 | 4050 |
| 3 | 441 | 140211 |
| 49 | 73147532610169123199386258094868594249 | 3783418338866262867735066921357682965127835472383998211624955113755480846977 |
| 50 | 426335063173366200380428859644050080712 | 128524850084195532370509613198486105459044441665033026275840880713465733097346 |

The range proof uses the rational enclosure `1/(7*10^80) < t < 1/(6*10^80)`.
The upper enclosure certifies every R from 1 through 49. The lower enclosure excludes R = 50 from this sufficient criterion.

Direct finite Gauss computations: 282 cases; powers 1, 2, 3; odd dimensions 3, 5, 7, 9, 15, 21, 25, 35. This includes gcd(N,b_R) equal to 3, 5, 7, and 35.

## Source revisions

| File | SHA-256 |
| --- | --- |
| `Spectral_research_master.md` | `3534e4d7aa97c2f8621050248652363c639aeedf723f8b7fe7a971dc01ac2302` |
| `research_round6_2026_10_21/round6_main_report.md` | `473b7b5b700a8ff17801eb9ca422c5949be15d0551c252e0b4035997db54b2bf` |
| `research_round6_2026_10_21/r6_original_fixed_powers_49.md` | `3f51c6d7de5b559c28271c72ae62c2f2d331f9c606b24a84cdab80751339d019` |
| `research_round6_2026_10_21/r6_original_twostep_physical_mixing.md` | `7d502a881f133743cd3d28afd6ac373351fd4a12f23e8292c59895358f1e747b` |
| `research_round5_2026_10_21/root_oscillatory_matrix_cancellation.md` | `ff98c2a2ee7dcd55b046c2039a86b2c206c3fcc170df3433c76f49281eff968d` |

## Reproduction

```bash
python research_round7_2026_10_21/r7_audit_physical_fixed_powers49_checks.py
```
