# Quantized cat maps and BGS: research workspace

This repository studies spectral statistics of quantized hyperbolic cat maps after symmetry reduction. The long-term question is whether an explicit arithmetic family can be brought all the way from exact finite-field formulas to a rigorous random-matrix local law.

**Current status: the general BGS conclusion is not proved.** The strongest active line now starts from an exact pair-key description of the fourth-moment object, with independently checked finite identities and a sharply stated remaining variance problem. Historical proof attempts that used a Möbius-fiber surrogate are retained only in the archive because that surrogate is not the exact finite object.

## Start here

1. `STATUS.md` — what is established, numerical, open, or retracted.
2. `ROADMAP.md` — the research programme and promotion rules.
3. `research/ledger.md` — chronological scientific decisions and new findings.
4. `research/theory.md` — the current mathematical core, without historical overclaims.
5. `research/problems/m1_fluctuation_energy.md` — the present load-bearing theorem target.
6. `references/bibliography.md` — verified literature and why each source matters.

## Working layout

- `src/python/bgs/` — reusable mathematical kernels, including the exact pair-key geometry.
- `src/cpp/verification/` — independent C++20 verification/high-throughput implementations kept as source.
- `experiments/verification/` — exact or regression checks that produce `results/verified/`.
- `experiments/m1/` — current analytic-bottleneck diagnostics and falsifiers.
- `experiments/spectral/` — numerical spectral-statistics experiments.
- `results/` — only curated outputs with an explicit trust category.
- `formal/` — Lean finite certificates. A file is not called verified merely because it is Lean source; build status is stated in `formal/README.md`.
- `paper/` — future current manuscript only. Historical “proof/complete” manuscripts are not active.
- `references/` — checked literature and search/symbolic provenance.
- `archive/legacy-workspace/` — immutable pre-restructure research corpus, including failed routes and raw provenance.

The archive is deliberately large; the active workspace is deliberately small. Useful old results are promoted out of the archive only after their producer and conventions are reconstructed, an independent check is performed, and the claim is rewritten with an honest status.
