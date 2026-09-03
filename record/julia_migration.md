# Julia migration inventory

All 31 Julia paths in the supplied ZIP are accounted for here. They reduce to 23 byte-distinct sources. Original Julia bytes remain browsable under `record/corpus/` and recoverable from Git history; no Julia source is allowed in the active `computations/`, `mathematics/`, `formalization/`, `manuscript/`, or `evidence/` trees.

The migration rule is mathematical before linguistic: do not port a false or scientifically obsolete algorithm just to remove Julia. Use C++20 for expensive exact/exhaustive kernels, Python for symbolic/orchestration/analysis work, and introduce Fortran only if profiling later identifies a genuinely dense numerical kernel that benefits from it.

| Historical Julia path | SHA-256 (12) | Disposition | Final destination / replacement |
|---|---:|---|---|
| `code/large_m/bigdp_dense.jl` | `1f56d5543118` | **PORTED, now historical regression** | `record/engineering/historical_cpp/relation_shape_automaton.cpp` |
| `code/large_m/bigdp_r104.jl` | `dc81dda2e021` | **PORTED, now historical regression** | `record/engineering/historical_cpp/relation_shape_automaton.cpp` |
| `code/large_m/cdense_transfer.jl` | `a7760efe91f9` | **FALSIFIED** | no production port; source retained under `record/corpus/code/large_m/` |
| `code/large_m/cross_key_check.jl` | `c73f1321c7c2` | **SUPERSEDED** | `computations/cpp/fourth_moment_pair_key_verifier.cpp` + current Python gates |
| `code/large_m/dp_debug.jl` | `2161e8f5411f` | **PORTED, now historical regression** | `record/engineering/historical_cpp/relation_shape_automaton.cpp` |
| `code/large_m/julia_bigdp.jl` | `c57756f8cb1e` | **PORTED, now historical regression** | `record/engineering/historical_cpp/relation_shape_automaton.cpp` |
| `code/shape_automaton/dp_exact.jl` | `7cf417d9be17` | **PORTED, now historical regression** | `record/engineering/historical_cpp/relation_shape_automaton.cpp` |
| `code/shape_automaton/dp_library.jl` | `2f25b51a2ff7` | **MERGED, now historical regression** | `record/engineering/historical_cpp/relation_shape_automaton.cpp` |
| `code/shape_automaton/dp_push.jl` | `3002a2365ff3` | **MERGED, now historical regression** | `record/engineering/historical_cpp/relation_shape_automaton.cpp` |
| `code/shape_automaton/julia_relation_automaton.jl` | `27f7755437c2` | **SUPERSEDED** | historical C++ regression only; no active theorem dependency |
| `code/utils/find_small_ord_primes.jl` | `051ad68b7c17` | **PORTED** | `computations/cpp/cat_map_order.cpp` |
| `code/utils/hecke_real_centraliser.jl` | `a07d837946bd` | **RETRACTED** | failed-line source plus refutation remain under `record/corpus/` |
| `code/utils/linn_h3_subgroup.jl` | `d9c4f0b0a11d` | **HISTORICAL NUMERICAL DIAGNOSTIC** | `record/corpus/experiments/number_theory/linn_h3_probe.py` |
| `code/utils/projective_order_brute.jl` | `a85516078cf2` | **PORTED WITH NAMING FIX** | `computations/cpp/cat_map_order.cpp`; full matrix order, not projective order |
| `code/utils/sol6_closed_form.jl` | `bbe1015e439a` | **PORTED AS FALSIFIER** | `record/corpus/experiments/verification/sol6_relation_count.py` |
| `code/verification/julia_cross_key.jl` | `c73f1321c7c2` | **BYTE-IDENTICAL / SUPERSEDED** | current pair-key C++/Python verification |
| `data/legacy/bigdp_dense.jl` | `1f56d5543118` | **BYTE-IDENTICAL DUPLICATE** | no separate port |
| `data/legacy/bigdp_r104.jl` | `dc81dda2e021` | **BYTE-IDENTICAL DUPLICATE** | no separate port |
| `data/legacy/cdense_transfer.jl` | `a7760efe91f9` | **BYTE-IDENTICAL DUPLICATE** | no separate port |
| `data/legacy/cross_key_check.jl` | `c73f1321c7c2` | **BYTE-IDENTICAL DUPLICATE** | no separate port |
| `data/legacy/dp_debug.jl` | `2161e8f5411f` | **BYTE-IDENTICAL DUPLICATE** | no separate port |
| `data/legacy/julia_bigdp.jl` | `c57756f8cb1e` | **BYTE-IDENTICAL DUPLICATE** | no separate port |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v3.jl` | `76235d5f643a` | **RETRACTED SERIES** | provenance only |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v4.jl` | `af086284e5e0` | **RETRACTED SERIES** | provenance only |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v5.jl` | `b5749d1f5fb7` | **RETRACTED SERIES** | provenance only |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v6.jl` | `9678e51c881d` | **RETRACTED SERIES** | provenance only |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v7.jl` | `ffa6eb87f09c` | **RETRACTED SERIES** | provenance only |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v7_fixed.jl` | `7073020217cc` | **RETRACTED SERIES** | provenance only |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v8.jl` | `ba4adef9667e` | **RETRACTED SERIES** | provenance only |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v9_v10.jl` | `37aa0f5cc5f0` | **RETRACTED SERIES** | provenance only |
| `docs/review/scripts/julia_crosscheck.jl` | `f6b0542d56d2` | **SUPERSEDED** | current pair-key C++/Python verification |

## What is active today

Only two C++ programs are on the default build surface: `fourth_moment_pair_key_verifier.cpp` and `cat_map_order.cpp`. The relation/shape C++ port remains useful because it preserves and cross-checks several Julia-era exact DP anchors, but it is now intentionally historical: no current theorem or manuscript conclusion depends on it.

## Gate for the later full Julia migration

For each row above, before translating anything further:

1. resolve the historical claim against `record/claim_ledger.md` and `record/retractions.md`;
2. identify exact invariants or preserved finite outputs;
3. decide whether the computation is still scientifically useful;
4. choose the implementation language from the workload, not from a blanket rewrite policy;
5. reproduce the invariants and add a negative control when the historical line was fragile;
6. promote only the smallest canonical replacement; do not keep parallel language copies without a verification reason.
