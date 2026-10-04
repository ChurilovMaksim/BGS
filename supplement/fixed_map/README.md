# Fixed-map research supplement

This supplement preserves the mathematical proofs, computational sources and
finite evidence recovered from the previously unpublished research of
13--20 September 2026. The current scientific entry point is
[the fixed-map frontier](../../mathematics/fixed_map_resolvent_frontier.md).
**Microscopic BGS universality for the prescribed fixed map remains open.**

## Reading order and evidence boundary

| Topic | Main reading | Established scope |
|---|---|---|
| Algebraic return | [Theorem](algebraic-return/exact_return_theorem.md), [quantitative limitations](algebraic-return/quantitative_split.md) | Exclusion of exact algebraic returns under stated hypotheses; finite simplicity certificates |
| Ergodic comparison | [Transfer theorem](ergodic-transfer/ergodic_spectral_transfer.md) | Structured subprincipal comparison under ergodicity and Egorov; correlation transfer needs occupation bounds |
| Coherent return | [Derivation](coherent-return/research_checkpoint.md) | Exact memory identities; positive classical mixing does not erase quantum memory |
| Fixed coupling | [Barrier](design-return/fixed_coupling_barrier.md), [sparse orbit theorem](design-return/sparse_orbit_theorem.md) | Finite and arithmetic bounds with explicit regimes |
| Block memory | [Theorem](block-memory/block_memory_theorem.md), [Abel bound](block-memory/abel_memory_bound.md) | Closed dynamics and reset dynamics differ even with a mixing reset chain |
| Uploaded report audit | [Audit](report-audit-20260919/audit.md), [CUE reference](report-audit-20260919/cue_reference.md) | Corrected cubic reference, variance calculation and scope of redesigned-symbol experiments |
| Secular sums | [Attempt](secular-route/attempt.md), [weighted sums](weighted-secular/attempt.md) | Actual principal minors checked; asymptotic cancellation unresolved |
| Determinant ratios | [Boundary and reduction](weighted-secular/determinant_boundary.md) | Covariance alone is insufficient; exact Abel/ratio target |
| Mixed loops | [Full criterion](resolvent-flow/loop_bridge.md), [low-order bounds](resolvent-flow/low_order_bounds.md) | Conditional all-order correlation criterion and exact finite identities |
| Entropy comparison | [Obstruction](resolvent-flow/entropy_obstruction.md) | Global entropy cannot be small while preserving one spectrum at vanishing microscopic RMS distance |

The [20--21 September continuation](continuation-20260921/README.md) indexes
the late handoff now promoted into maintained theorem notes: fixed-model
symmetry exclusion, full-symbol Pell crossover, moment/transfer controls,
the three-orientation barrier, Fourier-line coercivity, and the local-jet
negative control.

The remaining `echo-research`, `fixed-map-audit`, and `time-insertion`
folders retain preliminary diagnostics and their limitations. They are not
additional asymptotic theorems.

## Reproduce without changing retained evidence

From the repository root:

```sh
python -m pip install -r requirements.txt
python computations/maintenance/verify_fixed_map_supplement.py
```

The runner verifies every inventory hash and every Python source's syntax,
then runs 28 selected checks in separate writable copies under `build/`.
These include exact Python and C++ certificate replay, the independent
Jacobi assembly, weighted minors through N=23, and direct loop/Laplacian
checks. The command returns failure if a selected execution fails or times
out. `--audit-only` checks inventory and syntax without numerical execution;
`--only topic/script.py` selects a listed check.

Wolfram scripts and the exploratory echo/monodromy simulations are retained
with their historical results; they are not silently counted as freshly
executed checks. Each script can also be run manually in a writable copy.
Do not run output-writing scripts directly in this source directory.

## Provenance and historical wording

`inventory.json` records original paths and the current edition's byte counts
and SHA-256 values. Dated reviews and checkpoint metadata retain their
historical contents. The 4 October 2026 integrity repair synchronizes the
mixed-loop proof's already corrected text with this inventory; it does not
rewrite the historical checkpoint hashes. The
[integrity review](../../record/history/2026/ci_integrity_20261004.md) records
the failure and fresh replay. References to `build/topic/` mean
the original working layout;
the replay runner reconstructs that layout. Earlier statements such as
"unpublished" or "no push" describe their historical checkpoint, not the
current publication status. Old checkpoint hashes refer to those historical
snapshots, while `inventory.json` governs this recovered edition.

The external Bourgade--Huang PDF and its extracted full text are not
redistributed. Its exact version, URL and hash are recorded in
`resolvent-flow/checkpoint.json`. No compiled executable, LaTeX temporary
file or third-party package is included here. Internal reviews are not
external peer review; finite tests are not proofs of asymptotic claims.
