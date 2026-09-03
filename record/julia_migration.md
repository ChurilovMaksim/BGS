# Julia migration — completed current-tree disposition

The supplied snapshot contained **31 Julia paths, 23 byte-distinct sources**.
Every path is accounted for below. The current branch tracks **zero `.jl`
files**.

The migration rule was scientific before linguistic: false or duplicate code
was not translated merely to change the GitHub language bar. Useful exact hot
paths were moved to maintained C++20; symbolic/reference/orchestration work is
maintained in Python; finite facts worth formal certification are in Lean 4.

Original Julia bytes remain recoverable from the supplied snapshot and from
Git history. The last `main` commit that still retained the curated historical
corpus is `d0e414ec26ff7e43ad59e80f77c9d8c679e87c4b`.

| Historical Julia path | SHA-256 (12) | Final disposition | Maintained replacement / reason |
|---|---:|---|---|
| `code/large_m/bigdp_dense.jl` | `1f56d5543118` | **MIGRATED / historical DP** | Useful exact DP logic was consolidated into a C++ relation/shape port during reconstruction; no current theorem depends on that port, so the old source and non-load-bearing port now live only in Git history. |
| `code/large_m/bigdp_r104.jl` | `dc81dda2e021` | **MIGRATED / historical DP** | Same disposition as the consolidated relation/shape C++ regression in Git history. |
| `code/large_m/cdense_transfer.jl` | `a7760efe91f9` | **FALSIFIED** | Not ported: the Perron bracket fails because the zero digit gives a zero-cost self-loop of weight one. |
| `code/large_m/cross_key_check.jl` | `c73f1321c7c2` | **SUPERSEDED** | `computations/cpp/fourth_moment_pair_key_verifier.cpp` plus current Python/Lean gates. |
| `code/large_m/dp_debug.jl` | `2161e8f5411f` | **MIGRATED / historical DP** | Consolidated historical C++ regression; no active theorem dependency. |
| `code/large_m/julia_bigdp.jl` | `c57756f8cb1e` | **MIGRATED / historical DP** | Consolidated historical C++ regression; no active theorem dependency. |
| `code/shape_automaton/dp_exact.jl` | `7cf417d9be17` | **MIGRATED / historical DP** | Consolidated historical C++ regression; no active theorem dependency. |
| `code/shape_automaton/dp_library.jl` | `2f25b51a2ff7` | **MERGED / historical DP** | Merged into the historical C++ relation/shape implementation. |
| `code/shape_automaton/dp_push.jl` | `3002a2365ff3` | **MERGED / historical DP** | Merged into the historical C++ relation/shape implementation. |
| `code/shape_automaton/julia_relation_automaton.jl` | `27f7755437c2` | **SUPERSEDED** | Historical relation/shape regression only; no current theorem dependency. |
| `code/utils/find_small_ord_primes.jl` | `051ad68b7c17` | **PORTED** | `computations/cpp/cat_map_order.cpp`. |
| `code/utils/hecke_real_centraliser.jl` | `a07d837946bd` | **RETRACTED** | Failed Hecke-centering line; no production port. |
| `code/utils/linn_h3_subgroup.jl` | `d9c4f0b0a11d` | **HISTORICAL NUMERICAL DIAGNOSTIC** | No load-bearing current result; preserved by Git history only. |
| `code/utils/projective_order_brute.jl` | `a85516078cf2` | **PORTED WITH NAMING FIX** | `computations/cpp/cat_map_order.cpp`; the implemented condition is full matrix order, not the historical projective-order label. |
| `code/utils/sol6_closed_form.jl` | `bbe1015e439a` | **FALSIFIED** | Not promoted; exact finite rows refuted the suggested prime-independent closed form. |
| `code/verification/julia_cross_key.jl` | `c73f1321c7c2` | **BYTE-IDENTICAL / SUPERSEDED** | Current pair-key C++/Python/Lean verification. |
| `data/legacy/bigdp_dense.jl` | `1f56d5543118` | **BYTE-IDENTICAL DUPLICATE** | No separate port. |
| `data/legacy/bigdp_r104.jl` | `dc81dda2e021` | **BYTE-IDENTICAL DUPLICATE** | No separate port. |
| `data/legacy/cdense_transfer.jl` | `a7760efe91f9` | **BYTE-IDENTICAL DUPLICATE** | No separate port. |
| `data/legacy/cross_key_check.jl` | `c73f1321c7c2` | **BYTE-IDENTICAL DUPLICATE** | No separate port. |
| `data/legacy/dp_debug.jl` | `2161e8f5411f` | **BYTE-IDENTICAL DUPLICATE** | No separate port. |
| `data/legacy/julia_bigdp.jl` | `c57756f8cb1e` | **BYTE-IDENTICAL DUPLICATE** | No separate port. |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v3.jl` | `76235d5f643a` | **RETRACTED SERIES** | Git-history provenance only. |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v4.jl` | `af086284e5e0` | **RETRACTED SERIES** | Git-history provenance only. |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v5.jl` | `b5749d1f5fb7` | **RETRACTED SERIES** | Git-history provenance only. |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v6.jl` | `9678e51c881d` | **RETRACTED SERIES** | Git-history provenance only. |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v7.jl` | `ffa6eb87f09c` | **RETRACTED SERIES** | Git-history provenance only. |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v7_fixed.jl` | `7073020217cc` | **RETRACTED SERIES** | Git-history provenance only. |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v8.jl` | `ba4adef9667e` | **RETRACTED SERIES** | Git-history provenance only. |
| `docs/archive/hecke_centring_failed_line/hecke_real_centraliser_v9_v10.jl` | `37aa0f5cc5f0` | **RETRACTED SERIES** | Git-history provenance only. |
| `docs/review/scripts/julia_crosscheck.jl` | `f6b0542d56d2` | **SUPERSEDED** | Current pair-key C++/Python/Lean verification. |

## Current language boundary

Maintained code has one role per language:

- C++20: independent exact/exhaustive kernels;
- Python: checked arithmetic, symbolic/exact orchestration and numerical
  diagnostics;
- Lean 4: finite certificates and falsifiers;
- TeX: manuscript;
- Julia: no tracked current source.

`computations/verification/repository_audit.py` fails if any `.jl` file appears
anywhere in the current tree, not merely in the active computation directory.
