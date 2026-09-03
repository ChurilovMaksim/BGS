# Julia migration inventory

All 31 Julia paths in the supplied ZIP are accounted for here. They reduce to 23 byte-distinct sources. Julia is not copied into the active implementation layer. Original bytes are recoverable from the broad parent/provenance commit and are hash-accounted in `source_snapshot_manifest.tsv`.

Policy: do not translate a falsified algorithm merely to change language. First determine whether the mathematics is still useful; then choose C++20 for exhaustive/discrete kernels, Python for symbolic and analysis orchestration, and Fortran only for a profiled dense numerical kernel.

| Historical path | SHA-256 (12) | Disposition | Current replacement / destination |
|---|---|---|---|
| `code/large_m/bigdp_dense.jl` | `1f56d5543118` | **PORTED / CONSOLIDATED** | `computations/cpp/shape/relation_automaton.cpp` — Useful exact DP logic consolidated; obsolete/buggy variants not cloned. |
| `code/large_m/bigdp_r104.jl` | `dc81dda2e021` | **PORTED / CONSOLIDATED** | `computations/cpp/shape/relation_automaton.cpp` — Useful exact DP logic consolidated; obsolete/buggy variants not cloned. |
| `code/large_m/cdense_transfer.jl` | `a7760efe91f9` | **FALSIFIED** | `computations/cpp/shape/relation_automaton.cpp` — Perron bracket fails because of zero-cost self-loop. |
| `code/large_m/cross_key_check.jl` | `c73f1321c7c2` | **SUPERSEDED** | `computations/cpp/verification/fourth_moment_factorization.cpp + computations/verification/current_regression.py` — Stronger current independent checks. |
| `code/large_m/dp_debug.jl` | `2161e8f5411f` | **PORTED / CONSOLIDATED** | `computations/cpp/shape/relation_automaton.cpp` — Historical bug diagnostic becomes a regression condition. |
| `code/large_m/julia_bigdp.jl` | `c57756f8cb1e` | **PORTED / CONSOLIDATED** | `computations/cpp/shape/relation_automaton.cpp` — Exact DP/Bessel calibration consolidated. |
| `code/shape_automaton/dp_exact.jl` | `7cf417d9be17` | **PORTED / CONSOLIDATED** | `computations/cpp/shape/relation_automaton.cpp` — Corrected exact Run-82 DP. |
| `code/shape_automaton/dp_library.jl` | `2f25b51a2ff7` | **PORTED / CONSOLIDATED** | `computations/cpp/shape/relation_automaton.cpp` — Library merged into one supported kernel. |
| `code/shape_automaton/dp_push.jl` | `3002a2365ff3` | **PORTED / CONSOLIDATED** | `computations/cpp/shape/relation_automaton.cpp` — Large-budget path consolidated. |
| `code/shape_automaton/julia_relation_automaton.jl` | `27f7755437c2` | **SUPERSEDED** | `computations/cpp/shape/relation_automaton.cpp` — Early prototype replaced by corrected exact kernel. |
| `code/utils/find_small_ord_primes.jl` | `051ad68b7c17` | **PORTED** | `computations/cpp/number_theory/catmap_order.cpp` — Candidate scan replacement. |
| `code/utils/hecke_real_centraliser.jl` | `a07d837946bd` | **RETRACTED** | `record/corpus/code/diagnostics/hecke_centring_refutation.py` — Failed Hecke-centering line. |
| `code/utils/linn_h3_subgroup.jl` | `d9c4f0b0a11d` | **PORTED DIAGNOSTIC** | `record/corpus/experiments/number_theory/linn_h3_probe.py` — Numerical discriminator only. |
| `code/utils/projective_order_brute.jl` | `a85516078cf2` | **PORTED WITH NAMING FIX** | `computations/cpp/number_theory/catmap_order.cpp` — Historical comment confused full matrix order with projective scalar order. |
| `code/utils/sol6_closed_form.jl` | `bbe1015e439a` | **PORTED AS FALSIFIER** | `record/corpus/experiments/verification/sol6_relation_count.py` — Historical closed-form claim is false. |
| `code/verification/julia_cross_key.jl` | `c73f1321c7c2` | **BYTE-IDENTICAL / SUPERSEDED** | `computations/cpp/verification/fourth_moment_factorization.cpp` — Duplicate of the historical cross-key source. |
| `data/legacy/bigdp_dense.jl` | `1f56d5543118` | **BYTE-IDENTICAL DUPLICATE** | no separate port — duplicate of canonical historical source. |
| `data/legacy/bigdp_r104.jl` | `dc81dda2e021` | **BYTE-IDENTICAL DUPLICATE** | no separate port — duplicate of canonical historical source. |
| `data/legacy/cdense_transfer.jl` | `a7760efe91f9` | **BYTE-IDENTICAL DUPLICATE** | no separate port — duplicate of canonical historical source. |
| `data/legacy/cross_key_check.jl` | `c73f1321c7c2` | **BYTE-IDENTICAL DUPLICATE** | no separate port — duplicate of canonical historical source. |
| `data/legacy/dp_debug.jl` | `2161e8f5411f` | **BYTE-IDENTICAL DUPLICATE** | no separate port — duplicate of canonical historical source. |
| `data/legacy/julia_bigdp.jl` | `c57756f8cb1e` | **BYTE-IDENTICAL DUPLICATE** | no separate port — duplicate of canonical historical source. |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v3.jl` | `76235d5f643a` | **RETRACTED SERIES** | `record/corpus/code/diagnostics/hecke_centring_refutation.py` — preserve only as failed-line provenance. |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v4.jl` | `af086284e5e0` | **RETRACTED SERIES** | same failed line; no mechanical production port. |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v5.jl` | `b5749d1f5fb7` | **RETRACTED SERIES** | same failed line; no mechanical production port. |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v6.jl` | `9678e51c881d` | **RETRACTED SERIES** | same failed line; no mechanical production port. |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v7.jl` | `ffa6eb87f09c` | **RETRACTED SERIES** | same failed line; no mechanical production port. |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v7_fixed.jl` | `7073020217cc` | **RETRACTED SERIES** | same failed line; no mechanical production port. |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v8.jl` | `ba4adef9667e` | **RETRACTED SERIES** | same failed line; no mechanical production port. |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v9_v10.jl` | `37aa0f5cc5f0` | **RETRACTED SERIES** | same failed line; no mechanical production port. |
| `docs/review/scripts/julia_crosscheck.jl` | `f6b0542d56d2` | **SUPERSEDED** | `computations/cpp/verification/fourth_moment_factorization.cpp + computations/verification/current_regression.py` — stronger current independent checks. |

## Migration gate

A future translation is promoted only after: (1) the historical claim is checked against the current claim ledger, (2) preserved finite outputs or exact invariants are identified, (3) the new implementation reproduces them, and (4) an independent negative control is included when the old line was known to be fragile.
