# Research history — current index

This is the short, readable history index. The active detailed chronology is `research/ledger.md`. The complete pre-rebuild ledger is preserved verbatim in `docs/HISTORY_FULL_PRE_REBUILD.md`; it contains known mojibake from an older encoding error but has not been discarded.

## Major phases

1. **Quantized cat-map infrastructure and spectral experiments** — construction/quantization code, symmetry reduction, spacing and rigidity diagnostics, moment computations and finite-field utilities accumulated across `code/core`, `code/diagnostics`, `code/large_m`, `code/kloosterman`, `data/spectral` and `data/moments`.
2. **Large-m / shape / automaton investigations** — extensive relation-counting, moment-design and shape-mode work, including Run-82 calibration material. Useful exact relation-DP logic is now consolidated in C++20; old Julia implementations remain only in immutable provenance.
3. **Rank-2 / Sp4 line** — computational exploration and falsification work retained in `code/sp4`, `data/rank2_sp4` and associated notes.
4. **Historical proof attempts and red-team phase** — multiple proof-oriented routes were written and stress-tested. The historical Mobius-fiber/M4D proof route was retracted after object/multiplicity and asymptotic defects were identified. Several other producer/statistic mismatches were quarantined rather than erased.
5. **Exact pair-key reconstruction** — the fourth-moment problem was rebuilt around the exact pair-key distribution `B(t)`, exact Fourier identities and independent finite verification.
6. **Current M1 program** — exact mixed `k=2` Cayley-energy control, mean geometry and generic off/off elliptic-family analysis were assembled into a restricted M1 concentration proof chain. As of 2026-09-03 it remains audit/formalization pending, and general BGS remains open.
7. **Repository/language consolidation** — the full research corpus was restored to ordinary working paths while theorem trust was separated from preservation. Historical Julia sources were audited path-by-path and useful components migrated/consolidated into Python/C++ without creating another Julia copy.
8. **Manuscript consolidation** — active exposition is being kept in one `paper/main.tex` source rather than multiple competing proof/final section trees.

For exact dates, run identifiers, intermediate claims and negative results, use `research/ledger.md` and `docs/HISTORY_FULL_PRE_REBUILD.md`. For current truth status, always use `STATUS.md`.
