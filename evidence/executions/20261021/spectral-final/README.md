# Final spectral corpus: provenance and fresh execution

Source: final uploaded master, SHA256
`b035e30034b20c60a8ced1d28a072767c1ea7afc5deaeea545aa20730e1948cb`,
8,849,820 bytes. [Review](../../../../record/spectral_final_integration_20261021.md),
[catalog](../../../../record/spectral_research/catalog.json),
[reading edition](../../../../mathematics/spectral_research/README.md).

## Source and author evidence

`original/master.part01.gz` through `master.part06.gz` independently compress
consecutive source chunks. Decompress each and concatenate in order to recover
the complete original bytes. Part sizes and hashes are in the catalog.
The maintained reconstruction tool checks these and all 535 source projections:

```sh
python3 computations/maintenance/rebuild_spectral_corpus.py --check
python3 computations/maintenance/render_spectral_research.py --check
```

`author/` contains preserved source-session receipts, numerical data and
editorial patches; these are not freshly generated results. The large
simplicity JSON is individually gzip-compressed without losing original bytes.
Six historical source-version differences are recorded in the catalog and
review, rather than relabeled as matching their earlier declared hashes.

## Fresh executions and context repairs

`fresh/replay_results.json` and `fresh/initial-and-retry-logs-logs.json.gz` retain the
initial 49/55 successful runs, six failures and retries. The failures were
historical-input/CLI packaging conditions, not failed mathematical assertions.
`fresh/replay_retries.json` records all six successful retries.
`fresh/unipotent-manifest.json` and `fresh/unipotent.stdout` record the
separately inspected checker with 186,042 exact finite assertions.

`fresh/packaged-first-run/` retains 55/56 success with the `mpmath` dependency
absent from the interpreter's default path. With numpy and mpmath available,
`fresh/packaged-replay/receipt.json` records **56/56 success** from the
maintained disposable-workspace replay. All original output logs are retained
in the correspondingly named `fresh/*-logs.json.gz` dictionaries, keyed by
original log filenames; empty logs are retained as empty string values.
The current environment provided mpmath 1.3.0 through its documented dependency
path. No dependency package is vendored into the repository.

```sh
python3 computations/verification/replay_spectral_corpus.py --output-dir /tmp/bgs-spectral-replay-results
python3 -O computations/verification/weighted_trace_hessian_checks.py
```

Each original checker runs with Python asserts enabled, a 35-second CPU limit,
40-second wall limit, 2-GiB address-space limit and 20-MiB output-file limit.
The launcher is sequential and restores source bytes after historical replay.
Eleven document builders are excluded; no Wolfram kernel is run.

Historical snapshots before rounds 6--14 are recovered by hash from nested
master blocks (`fresh/frozen_recovery.json`). The round 7 and round 9 generic
master aliases use exactly their expected snapshots. The global endpoint
probe is bounded to `--n 3 --max-total 3`.

The round 14 coordinate checker expects the pre-editorial source hash
`7b6657c8e1ca2ee91391509c2c97b9054715681a0afa2cedff94f8dd4c4ecc3f`.
The launcher reverses only the recorded carriage-return patch in its temporary
workspace, verifies that hash, runs the unchanged checker, and restores the
final source. The receipt explicitly records this context. The final corrected
source itself is preserved and hash-checked separately.

## Independent checks, rendering and limits

`fresh/hessian_checks.json` records the independent direct/block Hessian
comparison on three artificial repeated-clock spectra, executed with `-O`.
It uses explicit exceptions and is not a finite-difference check or an
experiment on the original asymptotic coupling.

`receipt.json` records final source/math/link/registry/build validation.
Formula parsing, manuscript compilation and inspected page images have
separate coverage. Neither a finite PASS nor a successful build establishes
the original microscopic asymptotic law. No new Lean or C++ certification,
world-priority verdict or external referee acceptance is claimed.
