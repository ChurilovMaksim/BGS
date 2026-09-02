# Code

The active code surface is deliberately small.

- `math/` — load-bearing mathematical kernels with no historical command-line side effects.
- `verification/` — current reproducibility/identity checks.
- `experiments/` — numerical spectral experiments; never treat their PASS labels as proofs.
- `maintenance/` — repository health gate.

Historical scripts remain available under `archive/legacy-workspace/code/`. Promote one back into active code only after removing stale paths, stating its assumptions, and deciding whether it is a verification or an experiment.
