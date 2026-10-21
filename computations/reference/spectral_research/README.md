# Historical spectral research programs

This directory preserves 76 source programs from the final research corpus:
67 Python files and nine Wolfram Language files. Programs retain their exact
embedded bytes. They are research reference code, separate from maintained
verification entry points and from freshly executed evidence.

The [catalog](../../../record/spectral_research/catalog.json) maps every
program to its original path and SHA256. Some original programs expect a
historical working directory, frozen master or source hash, and several write
local JSON receipts. Run them in the disposable replay workspace rather
than over the maintained proof edition.

From the repository root, with numpy and mpmath available:

```sh
python3 computations/maintenance/rebuild_spectral_corpus.py --check
python3 computations/verification/replay_spectral_corpus.py --output-dir /tmp/bgs-spectral-replay-results
python3 -O computations/verification/weighted_trace_hessian_checks.py
```

The replay executes 56 bounded mathematical checks with original assertions
enabled; eleven historical document builders are excluded. It reconstructs
exact old snapshots, supplies the bounded global-probe CLI and reverses the
documented editorial patch only for the checker requiring the old source hash.
CPU, memory, file-size and wall-time caps are imposed per process.
The proof edition and archive are not mutated.

Wolfram programs are retained for reproducibility but were not executed in
this integration. Historical Wolfram responses remain author evidence.
Finite checks do not certify the all-order microscopic limit.
