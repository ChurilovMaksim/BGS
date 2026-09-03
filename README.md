# Quantized cat maps and BGS: research workspace

This repository studies spectral statistics of quantized hyperbolic cat maps after symmetry reduction.  The long-term question is whether an explicit arithmetic family can be brought all the way from exact finite-field formulas to a rigorous random-matrix local law.

**Current status: the general BGS conclusion is not proved.**  The strongest active line consists of exact character-orthogonality reductions, independently reproduced finite-design identities, and numerical GOE evidence.  The main analytic obstruction is the fluctuation/cross-correlation problem recorded in `research/problems/m1_fluctuation_energy.md`.

## Start here

1. `STATUS.md` — what is established, numerical, open, or retracted.
2. `ROADMAP.md` — the research programme and promotion rules.
3. `research/ledger.md` — chronological scientific decisions and new findings.
4. `research/theory.md` — the current mathematical core, without historical overclaims.
5. `references/bibliography.md` — verified literature and why each source matters.

## Working layout

- `src/python/bgs/` — reusable mathematical kernels.
- `src/cpp/` — independent/high-throughput implementations kept as source.
- `experiments/verification/` — exact or regression checks that produce `results/verified/`.
- `experiments/m1/` — current analytic-bottleneck experiments.
- `experiments/spectral/` — numerical spectral-statistics experiments.
- `results/` — only curated outputs with an explicit trust category.
- `formal/` — Lean finite certificates.  A file is not called verified merely because it is Lean source; build status is stated in `formal/README.md`.
- `paper/` — future current manuscript only.  Historical “proof/complete” manuscripts are not active.
- `archive/legacy-workspace/` — immutable pre-restructure research corpus, including failed routes and raw provenance.

The archive is deliberately large; the active workspace is deliberately small.  Useful old results are promoted out of the archive only after an independent recheck and a status rewrite.
