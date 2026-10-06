# Bounded confirmation of the domain-only v2

6 October 2026, 22:59 UTC. This is a separate addendum. The original target, review, input manifest, computation provenance, and review summary are preserved unchanged.

**Primary verdict for v2: proved as written**, with the same explicit inherited FM-021 flatness/singular-gap inputs and the same review boundaries as the original audit. The inherited FM-021 analytic proof is not newly certified here.

The corrected target is `bgs_weighted_plateau_route/collective_hierarchy_v2.md`, SHA-256 `cb09192dac743bd78fd21b76f6bd9d32c79050e4f616c7a04644e3f8c4c9c037`. Byte comparison verifies exactly one replacement:

    For m>=2 the lower bound A_(m,N)>=1/N follows from the exact q=2 term.

becomes

    For N>=2 and m>=2 the lower bound A_(m,N)>=1/N follows from the exact q=2 term.

No other byte changed. The diff SHA-256 is `22ba1cc0553fdf4bc8a6e072c3ed56b509c5583c253f51f1e6767fa090ee9167`; the author's delta mapping SHA-256 is `614fab8413828b5ada966c9bc1ece6a5b1803ab2adccd1ab11ae0eb65b8a749c`. These files are copied under `v2_frozen/`. The original target still has hash `8c68dacb6a9480c0805d8caf0d7b0af427be7bc7f767eaf1ab9c746e3aa7a8e0`, and the original review still has hash `3801a9aaa707704337ee63d2b45ec384150736e27d533d61152075805d800636`.

This addresses the sole literal-domain exception identified by the audit. At N=1, the centered coefficient spaces and A vanish; that case no longer contradicts the corrected lower-bound sentence. The actual odd-N>=3 application, C1–C15 proof chain, original N^-2 normalization, and separately audited residual interface are unchanged. No computational rerun is necessary to confirm a one-line restriction already justified in the original audit.

## Worktree observation scope

The original audit's clean-worktree statements describe observations at the initial input snapshot and the final 22:57 UTC check. They are not continuing assertions about the worktree.

At this addendum's 22:59 UTC check, the canonical worktree is **not clean**. Direct `git status --porcelain` and `git diff` show exactly one changed file, `.github/workflows/ci.yml`, and exactly one replacement, the computation job's `timeout-minutes: 20` to `timeout-minutes: 40`. There are no other current worktree modifications. All 30 originally pinned input hashes, including every proof input, remain unchanged. The canonical HEAD remains `801de3ab760cab4349e68b9843dcd67955314e62`. This addendum makes no changes to canonical BGS.

The machine-readable verification, timestamp, current Git observation, and v2 frozen hashes are in `v2_confirmation.json`. The safe mathematical outcome remains the bounded actual-U collective-sector theorem, not a theorem about the complete balanced complement, the whole residual, or BGS.
