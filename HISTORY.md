# Canonical research history

This is the concise forward chronology.  The full run-by-run ledger is preserved in two forms: the raw provenance copy at `archive/legacy-workspace/HISTORY.md`, and a surfaced copy at `docs/HISTORY_FULL_PRE_REBUILD.md` that retains the known legacy mojibake until a dedicated content-migration commit.  Historical status labels in those files are snapshots, not current authority.

## R82 — twisted-Jacobi computational line

A one-parameter reduction and twisted-Jacobi implementation produced the baseline used by later work.  The 2026-09-03 sync again reproduced the stored fourth-moment curves at `N=199` and `N=3571` to approximately `1e-13` absolute accuracy.

## R91 — spectral numerical evidence

GOE-like nearest-neighbour spacing and matched number-variance evidence were produced in the desymmetrised sector.  A word-trace proof-engine attempt remained incomplete.  A separate `N=95419` driver was later found to compare gap ratios with the wrong spacing CDF and is quarantined.

## R92 — exact `k=2` reduction

The `k=2` fluctuation layer was reduced to an exact combinatorial constraint set with `|P|=(K-1)(K-2)`.  The current direct check reproduces the identity at `N=53,K=13` and `N=199,K=11`.

## R93-R101 — higher layers and M1 promotion attempt

Useful twist/key decompositions, numerical scaling experiments, finite-field character-sum tests, and higher-moment data were accumulated.  The programme then promoted a Möbius-fiber estimate to a theorem.  The audit found that promotion unsound: cross-twist terms were not controlled, the asymptotic regime was misstated, normalisations drifted, and the displayed envelope was contradicted by one of its own rows.  The finite-N measurements remain preserved; the theorem-level M1 conclusion is withdrawn.

## R102-R110 — downstream and rank-2 exploration

Rank-2/Sp4 work produced several useful exact finite-design identities and numerical probes, especially at `N=53`.  Those results are preserved in the active research corpus.  Claims that the full rank-2 mechanism or general BGS had thereby been closed are superseded because they relied on unproved extrapolation and/or the invalid M1 promotion.

## R111 — canonical reset

The repository was first rebuilt around the last non-error dependency chain.  That first reset was too aggressive for a live research workspace: it made the canonical layer clear but hid too much useful experimental material under a legacy snapshot.

## R112 — full-workspace restoration and complete sync (2026-09-03)

The research corpus was restored into ordinary `code/`, `data/`, `docs/`, and `paper/` paths while preserving a narrow authoritative layer (`STATUS.md`, `research/`, current verification code/results).  The full audit then indexed every visible working-corpus file, deduplicated the review by content hash, rendered every unique PDF, parsed every JSON, syntax-checked every Python/JS/shell source that the environment could check, reviewed the Lean source boundary, and generated a producer-path migration map.

This audit also found a separate defect in the R86/R87 trace-fluctuation lemma: its Step 1 uses a scalar binomial expansion for generally noncommuting matrices.  That route is now explicitly superseded.  The historical-ledger mojibake was diagnosed and a reversible repair was verified locally; the large historical source was intentionally left unchanged in this structural sync, with checksums/method recorded for a dedicated migration.  The current research frontier remains the exact cross-twist M1 assembly or an independent route that bypasses it.
