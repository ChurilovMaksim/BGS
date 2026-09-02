# Canonical research history

This is a concise forward history. The original long ledger, including superseded claims and run-by-run provenance, is preserved unchanged at `archive/legacy-workspace/HISTORY.md`.

## R82 — twisted-Jacobi computational line

A one-parameter reduction and closed-form twisted-Jacobi implementation produced the baseline used by later work. The 2026-09-02 rebuild reproduced the stored fourth-moment curves at `N=199` and `N=3571` to roughly `1e-13` absolute accuracy.

## R91 — spectral numerical evidence

GOE-like nearest-neighbour spacing and matched number-variance evidence were produced in the desymmetrised sector. These remain numerical evidence. A word-trace proof-engine attempt was found unreliable and is quarantined. A separate N=95419 driver was later found to compare gap ratios against the wrong spacing CDF and is also quarantined.

## R92 — exact k=2 reduction

The `k=2` fluctuation layer was reduced to an exact combinatorial constraint set with `|P|=(K-1)(K-2)`. The current direct check reproduces the identity at `N=53,K=13` and `N=199,K=11`.

## R93–R101 — higher layers and M1 promotion attempt

Useful twist/key decompositions, numerical scaling experiments and finite-field character-sum tests were accumulated. The historical programme then promoted a Möbius-fiber estimate to a theorem. The audit found that promotion unsound: cross-twist terms were not controlled, the asymptotic regime was misstated, and the displayed numerical envelope was violated by one of its own rows.

The finite-N measurements remain preserved as historical numerical evidence, but the theorem-level M1 conclusion was withdrawn.

## R102–R110 — downstream/rank-2 exploration

Rank-2 and downstream experiments remain potentially useful, but any conclusion depending on the old M1 theorem is demoted until an independent proof is supplied.

## R111 — repository reset

The repository was rebuilt around the last non-error dependency chain. The old workspace was preserved whole under `archive/legacy-workspace/`; the active tree now exposes only the current kernels, checks, experiments, results, formal sources and the open M1 target.
