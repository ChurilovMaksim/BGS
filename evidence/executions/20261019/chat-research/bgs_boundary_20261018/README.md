# BGS research checkpoint: polynomial trace windows

18 October 2026. Main BGS and the original two-channel target remain open.
No repository mutation, new subagent, publication or priority claim.

Read BGS_mesoscopic_result_ru.md first. Full proofs:

- polynomial_trace_window_ru.md: exact mixed-moment estimate, trace powers
  o(N^(1/5)) for symplectic Fourier families, and the whole open disk limit.
- generic_bilinear_window_ru.md: powers o(N^(1/(6b))) for generic fixed
  bilinear seeds, with complex Gauss phases retained.
- gaussian_comparison_boundary_ru.md: an exact lower-bound obstruction to
  extending positive Gaussian majorization to Heisenberg times.
- self_review.md: normalized claims, dependencies, audit and remaining gap.
- inputs/: unchanged prior raw proof notes supplying fixed trace limits.

The new proofs are elementary author proofs with self-review, not independent
refereeing. The scripts check finite assertions and do not certify asymptotics.

## Exact finite checks

Run from this directory with Python 3.12, standard library only:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_polynomial_window.py replay_base/result.json
PYTHONDONTWRITEBYTECODE=1 python3 verify_generic_window.py replay_generic/result.json
PYTHONDONTWRITEBYTECODE=1 python3 verify_rank_completion.py replay_completion/result.json
```

The third checker reads the preserved run/result.json. First two checkers
retain initial weaker geometric bounds; the third explicitly checks the
strengthened principal-minor and Pfaffian bounds used in final proofs.
Do not overwrite preserved run/, generic_run/ or completion_run/.

Original bounded runs used computation-audit 4.0.0 run_experiment.py with
55 s wall, 50 s CPU, 1 GiB address space, one core/thread and 12,000 log bytes.
Contracts, executed inputs, exact outputs, commands and input/output hashes
are preserved. Every manifest has status completed; each result has passed.

## Scope and reproducibility

Whole-disk convergence means fixed compact subsets of |z|<1. It asserts
neither uniform integrability of determinants on that disk nor a limit at
z_N=exp(-s/N). No implication to local spacings or the two-channel target
has been proved.

source_bindings.json and research_checkpoint.json record parent hashes,
unchanged goals, resolved claims, scoped failures and next obligations.
repo_integrity.json checks the 716-file BGS snapshot against its baseline.
SHA256SUMS binds package files; archive_summary.json describes the archive
without a self-referential archive hash inside it. Private save helpers are
excluded. build_package.py regenerates packaging without rerunning experiments.
