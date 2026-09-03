# Julia migration inventory

All 31 Julia paths in the supplied ZIP are accounted for here. They reduce to
23 byte-distinct sources. Original Julia bytes remain browsable under
`record/corpus/` and recoverable from Git history; the active implementation
layer contains no Julia.

Policy: do not translate a falsified algorithm merely to change language.
First determine whether the mathematics is still useful; then choose C++20 for
exhaustive/discrete kernels, Python for symbolic and analysis orchestration,
and Fortran only for a profiled dense numerical kernel.

| Historical path | SHA-256 (12) | Disposition | Current replacement / destination |
|---|---|---|---|
| `code/large_m/bigdp_dense.jl` | `1f56d5543118` | **PORTED / CONSOLIDATED** | `computations/cpp/relation_shape_automaton.cpp` |
| `code/large_m/bigdp_r104.jl` | `dc81dda2e021` | **PORTED / CONSOLIDATED** | `computations/cpp/relation_shape_automaton.cpp` |
| `code/large_m/cdense_transfer.jl` | `a7760efe91f9` | **FALSIFIED** | no production port; Perron bracket fails because of the zero-cost self-loop; source retained in `record/corpus/code/large_m/` |
| `code/large_m/cross_key_check.jl` | `c73f1321c7c2` | **SUPERSEDED** | `computations/cpp/fourth_moment_pair_key_verifier.cpp` plus `computations/verification/current_regression.py` |
| `code/large_m/dp_debug.jl` | `2161e8f5411f` | **PORTED / CONSOLIDATED** | `computations/cpp/relation_shape_automaton.cpp` |
| `code/large_m/julia_bigdp.jl` | `c57756f8cb1e` | **PORTED / CONSOLIDATED** | `computations/cpp/relation_shape_automaton.cpp` |
| `code/shape_automaton/dp_exact.jl` | `7cf417d9be17` | **PORTED / CONSOLIDATED** | `computations/cpp/relation_shape_automaton.cpp` |
| `code/shape_automaton/dp_library.jl` | `2f25b51a2ff7` | **PORTED / CONSOLIDATED** | `computations/cpp/relation_shape_automaton.cpp` |
| `code/shape_automaton/dp_push.jl` | `3002a2365ff3` | **PORTED / CONSOLIDATED** | `computations/cpp/relation_shape_automaton.cpp` |
| `code/shape_automaton/julia_relation_automaton.jl` | `27f7755437c2` | **SUPERSEDED** | corrected exact C++ kernel `computations/cpp/relation_shape_automaton.cpp` |
| `code/utils/find_small_ord_primes.jl` | `051ad68b7c17` | **PORTED** | `computations/cpp/cat_map_order.cpp` |
| `code/utils/hecke_real_centraliser.jl` | `a07d837946bd` | **RETRACTED** | failed Hecke-centering line; retain source and Python refutation only in the record |
| `code/utils/linn_h3_subgroup.jl` | `d9c4f0b0a11d` | **PORTED DIAGNOSTIC** | `record/corpus/experiments/number_theory/linn_h3_probe.py`; numerical discriminator only |
| `code/utils/projective_order_brute.jl` | `a85516078cf2` | **PORTED WITH NAMING FIX** | `computations/cpp/cat_map_order.cpp`; historical comment confused full matrix order with projective scalar order |
| `code/utils/sol6_closed_form.jl` | `bbe1015e439a` | **PORTED AS FALSIFIER** | `record/corpus/experiments/verification/sol6_relation_count.py`; historical closed-form claim is false |
| `code/verification/julia_cross_key.jl` | `c73f1321c7c2` | **BYTE-IDENTICAL / SUPERSEDED** | `computations/cpp/fourth_moment_pair_key_verifier.cpp` |
| `data/legacy/bigdp_dense.jl` | `1f56d5543118` | **BYTE-IDENTICAL DUPLICATE** | no separate port |
| `data/legacy/bigdp_r104.jl` | `dc81dda2e021` | **BYTE-IDENTICAL DUPLICATE** | no separate port |
| `data/legacy/cdense_transfer.jl` | `a7760efe91f9` | **BYTE-IDENTICAL DUPLICATE** | no separate port |
| `data/legacy/cross_key_check.jl` | `c73f1321c7c2` | **BYTE-IDENTICAL DUPLICATE** | no separate port |
| `data/legacy/dp_debug.jl` | `2161e8f5411f` | **BYTE-IDENTICAL DUPLICATE** | no separate port |
| `data/legacy/julia_bigdp.jl` | `c57756f8cb1e` | **BYTE-IDENTICAL DUPLICATE** | no separate port |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v3.jl` | `76235d5f643a` | **RETRACTED SERIES** | preserve as failed-line provenance; no production port |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v4.jl` | `af086284e5e0` | **RETRACTED SERIES** | preserve as failed-line provenance; no production port |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v5.jl` | `b5749d1f5fb7` | **RETRACTED SERIES** | preserve as failed-line provenance; no production port |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v6.jl` | `9678e51c881d` | **RETRACTED SERIES** | preserve as failed-line provenance; no production port |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v7.jl` | `ffa6eb87f09c` | **RETRACTED SERIES** | preserve as failed-line provenance; no production port |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v7_fixed.jl` | `7073020217cc` | **RETRACTED SERIES** | preserve as failed-line provenance; no production port |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v8.jl` | `ba4adef9667e` | **RETRACTED SERIES** | preserve as failed-line provenance; no production port |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v9_v10.jl` | `37aa0f5cc5f0` | **RETRACTED SERIES** | preserve as failed-line provenance; no production port |
| `docs/review/scripts/julia_crosscheck.jl` | `f6b0542d56d2` | **SUPERSEDED** | `computations/cpp/fourth_moment_pair_key_verifier.cpp` plus current Python regression |

## Migration gate

A future translation is promoted only after: (1) the historical claim is
checked against `claim_ledger.md`; (2) preserved finite outputs or exact
invariants are identified; (3) the new implementation reproduces them; and
(4) an independent negative control is included when the old line was known to
be fragile.
