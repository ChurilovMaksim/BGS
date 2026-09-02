# Code map

The code tree contains both a strict canonical layer and a broad preserved research corpus.

## Canonical layer

- `math/` — load-bearing mathematical kernels used by current checks;
- `verification/` — current reproducibility/identity/regression certificates;
- `experiments/` — current numerical experiments; a statistical `PASS` is evidence, not a theorem;
- `maintenance/` — repository health and deterministic inventory tooling.

Canonical code must use current repository paths and explicit output semantics.

## Restored research corpus

- `core/` — cat-map quantisation and core constructions;
- `diagnostics/` — diagnostics, falsifiers, and calibration scripts;
- `kloosterman/` — subgroup/Kloosterman explorations;
- `large_m/` — large-m moments, spectral experiments, M1/M2 investigations, and failed proof-engine material;
- `shape_automaton/` — shape/word/automaton investigations;
- `sp4/` — rank-2/Sp4 experiments;
- `theorems/` — theorem-oriented computational derivations;
- `utils/` — supporting utilities;
- `llm/` — local research-assistance helpers retained from the workspace.

All restored Python sources are kept syntactically valid.  Many predate the `src -> code` and `artifacts -> data/results` migration; stale paths in this research layer are tracked migration debt, not a reason to delete the experiment.  Use `docs/audit/PRODUCER_PATH_MAP.md` before porting an old run.

`large_m/bgs_spacing_N95419.py` is a quarantined historical experiment: it computes a gap-ratio statistic but historically compares it with an ordinary spacing CDF.  `large_m/word_trace_*` contains useful partial algebra but is not a proof-engine certificate.  See `code/large_m/README.md`.

## Historical code

- `legacy_verification/` — pre-rebuild verification scripts, including superseded/quarantined checks;
- `legacy_maintenance/` — pre-rebuild one-off repository/ledger maintenance scripts.

Do not use a research/historical script as a certificate until the mathematical object, producer paths, normalisation, and reference statistic have been re-audited and the output has been rerun into the appropriate `results/` layer.
