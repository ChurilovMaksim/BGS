# Results

This directory is the **status-controlled result layer**. The broader historical/research output corpus is restored under `data/`; see `data/MANIFEST.md`.

- `verified/` contains outputs rerun or independently checked as part of the canonical computational checks.
- `numerical/` contains current useful spectral experiments that remain numerical evidence.
- `historical-numerical/` contains selected finite-N measurements whose interpretation or surrounding proof claim was superseded or quarantined.

Additional raw and intermediate outputs — moment scans, diagnostics, spectral experiments, rank-2/Sp4 calculations and old proof-oriented JSON — live under `data/{diagnostics,moments,proof,rank2_sp4,spectral,legacy}` rather than being discarded.

JSON filenames and old `PASS` fields do not confer theorem status. Root `STATUS.md` is authoritative. A research output should be copied/promoted into `results/verified/` only after the producing code and the mathematical statistic have both been audited.