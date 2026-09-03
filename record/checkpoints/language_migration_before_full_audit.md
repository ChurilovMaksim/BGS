# Language migration: Julia audit and supported implementations

This manifest accounts for every Julia source in the preserved pre-restructure workspace. The active repository does **not** create a second Julia archive: original sources remain once, inside the immutable `archive/legacy-workspace/` provenance snapshot and Git history. Supported work is migrated or consolidated into Python/C++ only when it still has scientific value.

## Language policy

- **Python**: symbolic/exact research glue, reproducible numerical probes, data analysis, manuscript tooling.
- **C++20**: expensive finite-field loops, dynamic programs, exhaustive combinatorics, independent verification.
- **Fortran**: reserved for a future measured dense-numerical kernel only; no current Julia task benefits enough to justify a third implementation language.
- A second language implementation exists only where independence is itself part of the scientific certificate.

## Audit findings

- 31 Julia paths reduce to 23 byte-distinct files. Six `data/legacy/*.jl` files are exact duplicates of `code/large_m/*.jl`; `code/verification/julia_cross_key.jl` is also byte-identical to `code/large_m/cross_key_check.jl`.
- The corrected relation DP has been ported to one C++20 component. It reproduces preserved Run-82 exact counts through `R=56`, the glue check, and the preserved `K=17` Bessel calibration values.
- The historical `cdense_transfer.jl` Perron equation is falsified as written: the zero digit creates a zero-cost self-loop of weight one, so at `B=4` the port finds `rho(0.30)=1.00714371814>1`; the script's bisection bracket cannot hold. No production replacement asserts that claim.
- The prime/order C++ port reproduces all four saved v8 candidates. It also exposes a terminology bug: `projective_order_brute.jl` actually waits for `A^k=I`; for `A=[[2,1],[1,1]] mod 31` that full order is 15, while the comment said 5.
- The exact Python `sol6` enumerator reproduces preserved rows and confirms that the filename's closed-form claim is false (e.g. `k=30` depends on `p`).
- The Hecke-centring Julia series is not revived. Its later Python red-team already identifies the line as an artifact, so eight historical Julia versions map to one refutation rather than eight new clones.

## Complete path map

| Historical Julia path | SHA-256 | Status | Supported replacement | Audit note |
|---|---:|---|---|---|
| `code/large_m/bigdp_dense.jl` | `1f56d5543118` | **CONSOLIDATED** | `src/cpp/shape/relation_automaton.cpp` | Exact DP + Bessel modes; corrected exact filter. |
| `code/large_m/bigdp_r104.jl` | `dc81dda2e021` | **CONSOLIDATED** | `src/cpp/shape/relation_automaton.cpp` | Same historical stack; superseded by corrected exact DP. |
| `code/large_m/cdense_transfer.jl` | `a7760efe91f9` | **FALSIFIED** | `src/cpp/shape/relation_automaton.cpp` | Legacy Perron bracket fails because zero-cost digit gives weight-1 self-loop; retained only as falsifier. |
| `code/large_m/cross_key_check.jl` | `c73f1321c7c2` | **SUPERSEDED** | `experiments/verification/verify_fourth_moment_factorization.py + src/cpp/verification/fourth_moment_factorization.cpp` | Current exact key-table verifier is stronger and already independently cross-checked. |
| `code/large_m/dp_debug.jl` | `2161e8f5411f` | **CONSOLIDATED** | `src/cpp/shape/relation_automaton.cpp` | Historical bug diagnostic becomes a permanent exact-regression gate. |
| `code/large_m/julia_bigdp.jl` | `c57756f8cb1e` | **CONSOLIDATED** | `src/cpp/shape/relation_automaton.cpp` | Exact DP and Bessel calibration preserved; obsolete width state removed. |
| `code/shape_automaton/dp_exact.jl` | `7cf417d9be17` | **PORTED** | `src/cpp/shape/relation_automaton.cpp` | Exact corrected Run-82 algorithm; saved anchors reproduced. |
| `code/shape_automaton/dp_library.jl` | `2f25b51a2ff7` | **MERGED** | `src/cpp/shape/relation_automaton.cpp` | Library logic merged into the C++ component; no second implementation. |
| `code/shape_automaton/dp_push.jl` | `3002a2365ff3` | **MERGED** | `src/cpp/shape/relation_automaton.cpp` | Large-budget CLI is the count subcommand; same exact kernel. |
| `code/shape_automaton/julia_relation_automaton.jl` | `27f7755437c2` | **SUPERSEDED** | `src/cpp/shape/relation_automaton.cpp` | Early automaton prototype replaced by corrected exact kernel. |
| `code/utils/find_small_ord_primes.jl` | `051ad68b7c17` | **PORTED** | `src/cpp/number_theory/catmap_order.cpp` | Candidate scan reproduced exactly. |
| `code/utils/hecke_real_centraliser.jl` | `a07d837946bd` | **RETRACTED** | `archive/legacy-workspace/code/diagnostics/hecke_centring_refutation.py` | Historical line invalid; existing Python red-team is the supported explanation, not a new simulation clone. |
| `code/utils/linn_h3_subgroup.jl` | `d9c4f0b0a11d` | **PORTED_DIAGNOSTIC** | `experiments/number_theory/linn_h3_probe.py` | Deterministic seeded numerical probe; no theorem claim. |
| `code/utils/projective_order_brute.jl` | `a85516078cf2` | **PORTED_WITH_NAMING_FIX** | `src/cpp/number_theory/catmap_order.cpp` | Implementation computes full matrix order, not projective scalar order. Legacy p=31 comment was inconsistent. |
| `code/utils/sol6_closed_form.jl` | `bbe1015e439a` | **PORTED_AS_FALSIFIER** | `experiments/verification/sol6_relation_count.py` | Exact enumerator reproduces preserved rows and records counterexamples to alleged closed form. |
| `code/verification/julia_cross_key.jl` | `c73f1321c7c2` | **SUPERSEDED** | `experiments/verification/verify_fourth_moment_factorization.py + src/cpp/verification/fourth_moment_factorization.cpp` | Byte-identical to old cross_key_check; current verifier is stronger. |
| `data/legacy/bigdp_dense.jl` | `1f56d5543118` | **BYTE_IDENTICAL_DUPLICATE** | `src/cpp/shape/relation_automaton.cpp` | Byte-identical duplicate of code/large_m source; no extra port. |
| `data/legacy/bigdp_r104.jl` | `dc81dda2e021` | **BYTE_IDENTICAL_DUPLICATE** | `src/cpp/shape/relation_automaton.cpp` | Byte-identical duplicate of code/large_m source; no extra port. |
| `data/legacy/cdense_transfer.jl` | `a7760efe91f9` | **BYTE_IDENTICAL_DUPLICATE** | `src/cpp/shape/relation_automaton.cpp` | Byte-identical duplicate of code/large_m source; no extra port. |
| `data/legacy/cross_key_check.jl` | `c73f1321c7c2` | **BYTE_IDENTICAL_DUPLICATE** | `experiments/verification/verify_fourth_moment_factorization.py + src/cpp/verification/fourth_moment_factorization.cpp` | Byte-identical duplicate of code/large_m source; no extra port. |
| `data/legacy/dp_debug.jl` | `2161e8f5411f` | **BYTE_IDENTICAL_DUPLICATE** | `src/cpp/shape/relation_automaton.cpp` | Byte-identical duplicate of code/large_m source; no extra port. |
| `data/legacy/julia_bigdp.jl` | `c57756f8cb1e` | **BYTE_IDENTICAL_DUPLICATE** | `src/cpp/shape/relation_automaton.cpp` | Byte-identical duplicate of code/large_m source; no extra port. |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v3.jl` | `76235d5f643a` | **RETRACTED_SERIES** | `archive/legacy-workspace/code/diagnostics/hecke_centring_refutation.py` | Version in one failed Hecke-centring research line; consolidated into the later Python refutation and historical provenance only. |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v4.jl` | `af086284e5e0` | **RETRACTED_SERIES** | `archive/legacy-workspace/code/diagnostics/hecke_centring_refutation.py` | Same failed line; no new clone. |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v5.jl` | `b5749d1f5fb7` | **RETRACTED_SERIES** | `archive/legacy-workspace/code/diagnostics/hecke_centring_refutation.py` | Same failed line; no new clone. |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v6.jl` | `9678e51c881d` | **RETRACTED_SERIES** | `archive/legacy-workspace/code/diagnostics/hecke_centring_refutation.py` | Same failed line; no new clone. |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v7.jl` | `ffa6eb87f09c` | **RETRACTED_SERIES** | `archive/legacy-workspace/code/diagnostics/hecke_centring_refutation.py` | Same failed line; no new clone. |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v7_fixed.jl` | `7073020217cc` | **RETRACTED_SERIES** | `archive/legacy-workspace/code/diagnostics/hecke_centring_refutation.py` | Same failed line; no new clone. |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v8.jl` | `ba4adef9667e` | **RETRACTED_SERIES** | `archive/legacy-workspace/code/diagnostics/hecke_centring_refutation.py` | Same failed line; no new clone. |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v9_v10.jl` | `37aa0f5cc5f0` | **RETRACTED_SERIES** | `archive/legacy-workspace/code/diagnostics/hecke_centring_refutation.py` | Same failed line; no new clone. |
| `docs/review/scripts/julia_crosscheck.jl` | `f6b0542d56d2` | **SUPERSEDED** | `experiments/verification/verify_fourth_moment_factorization.py + src/cpp/verification/fourth_moment_factorization.cpp` | Old second-language spot check replaced by exact Python/C++ verification gate. |

## Promotion gates

A migrated component is allowed into the active tree only after (1) strict compile/syntax checks, (2) comparison to preserved artifacts or exact invariants, and (3) explicit handling of any historical mismatch. Historical scripts that encode a falsified claim remain archive-only and are not mechanically translated into a new production language.
