# Large-m research corpus

These scripts are preserved because they contain much of the higher-moment, spectral, M1/M2, and word-algebra exploration.  They are research material, not a second canonical verification suite.

Before rerunning a script, migrate old `src/` / `artifacts/` paths and check what statistic it actually computes.  Use `docs/audit/PRODUCER_PATH_MAP.md` for historical producer names.

Explicit quarantine: `bgs_spacing_N95419.py` forms consecutive-gap ratios but historically compared the result with the ordinary Wigner spacing CDF; its raw output is retained under `results/historical-numerical/`.  `word_trace_algebra.py` / `word_trace_proof.py` contain partial identities but the old rewrite engine did not close higher words, so they are not proof certificates.

Canonical reruns of promoted material belong in `code/verification/` or `code/experiments/`, with outputs under `results/`.
