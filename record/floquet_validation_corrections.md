# Validation failures are evidence, not a green badge

The full run 33971705529 reproduced all 40 Python/C++ execution checks and
regenerated the diagnostic certificates, but it did not complete a valid
Lean build or publish the reviewed worktree. The initial UI step summary
incorrectly showed success for Lean. Inspecting its actual retained log
revealed two modules with elaboration errors; `lake build | tee` had hidden
the compiler's nonzero exit code because the shell did not enable pipefail.
An intermediate conversational progress claim of Lean success was therefore
withdrawn immediately after inspecting the log. Only a later successful
compiler run can establish compilation status.

The old magnetic module required explicit `Int.ofNat` conversions when
folding or mapping `List.range`. The new Pell module's nonzero finite test
was restated as the directly decidable Boolean contains-equals-false
assertion; the period, Pell, pair cardinality and distinctness tests are
unchanged. None of these repairs alters an analytic argument.

`build_lean_verified.sh` now enables `set -euo pipefail`, includes a negative
control for a nonzero process piped to tee, and rejects a compiler-error
log even if a command incorrectly returns zero. Independent local fake-tool
checks verified rejection of both a nonzero process and a falsely green
error log, and acceptance of an error-free zero-exit log.

The same run stopped on the row-support companion's use of mixed color
names without loading xcolor. Adding the package was independently compiled
locally. The new eight-page companion layout was also re-rendered; its
bibliographic tail no longer occupies an almost empty extra page. The
main article is seventeen pages. Numerical plots retain the full finite
bias and distinguish stochastic RMS bounds from deterministic intervals.

The successful final workflow, its source commit, exact execution manifest,
and complete compiler log must be used together. An old green step alone
is never a formal certificate. These scope corrections complement
`floquet_continuation_20260905.md` and `claim_ledger.md`.
