# Unconditional feedback flatness: exact scope and evidence

**Claim:** BGS-TRACE-080. Reviewed base main:
`53d60cbb4b51d64b3ff82d396ab74e21f704f3a9`.

The frozen [candidate](candidate_reviewed.md) SHA256 is
`1264e43e74652b814fef953def70eb64702e287eb06e2dd3d7d0f86ee41b2d1c`.
The [independent reconstruction](independent_review.md) SHA256 is
`52467495bd3dcac810198ebabf3380f8ba2bdc6eb37cf4764d3576575dd96122`.
It separately checks cutoff-matched clock and reversal corollaries as
named-input deductions. It does not re-audit the entire earlier clock
induction, FM-021 or FM-022.

The main result gives unconditional flatness for a deterministic initial
unitary with entry bound `C0/N` and centered intensity singular norm at
most `1/100`, under uniform port selection and fresh uniform phases, down
to `ceil(log(2N)^(4+kappa))`. Its row/column energy and two-step estimates
share the same complete first-crossing stop. No deterministic microscopic
spectral identification or BGS conclusion is asserted.

Root [executed controls](root_executed_source.py), [output](root_controls.json)
and [log](root_controls.log) use exact rational residues for two rows of a
nonsymmetric 16-dimensional unitary and check all six coefficient sums,
the general mean and raw second moment. That fixture has `delta=49/400`;
the smaller-delta restoring-drift hypothesis is deliberately not asserted
for it. The separate size-64 fixture has `delta<1/16` and `rho<1/10`;
128-point complex-double quadrature checks two rows and two columns and
the stated pointwise range. The quadrature is not an exact integral.
The [failed initial fixture check](root_failed_fixture.log) is preserved:
an identical rotation in every Walsh column pair unexpectedly kept the
matrix symmetric. A single rotated pair supplies the intended nonsymmetric
fixture; the failure was a fixture-design error, not a mathematical
counterexample.

The reviewer's [independent code](independent_control_source.py) and
[output](independent_controls.json) record 628 exact rational expansions
and separate complex nonnormal row/column/diagonal checks. These are distinct
from the root execution and from the analytic proof.

Maintained reproduction:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 timeout 90 \
python3 computations/verification/feedback_row_energy.py
```

The maintained Green paragraph explicitly uses `12/11`, `6/11`, `12/5`
to preserve constants `18,432` at the changed cutoff. The clock reference
atom and pathwise rank bound retain their source scope; no exact finite-N
atomic equality is added. Reversal convergence additionally requires its
separate initial-norm premise. No new Lean/C++ certificate or priority
claim is made. Finite controls and successful software execution are not
the analytic proof of the asymptotic trajectory theorem.

## Completed execution and source binding

The maintained proof's transfer review binds SHA256
`4fa287dad66d7d9006af7b6736086249cbe29a39df3bdafe802a19c9e86d0fd0`;
[transfer_review.md](transfer_review.md) retains that exact independent pass.
The resource-capped [bounded execution](bounded/manifest.json) completed
successfully and its manifest validator passed. It declares five hashed
inputs and one result artifact; the finite scope above remains unchanged.

The shared [workspace receipt](workspace.json) records **8/8 selected
Python checks**, with an unchanged source tree during that run. Its logs
are retained here. It is a focused run, not a full new-head workspace replay.
The separate [maintenance log](maintenance_full.log) records **236 passing
tests**. The [manuscript receipt](manuscript_build_manifest.json) records
three successful LaTeX passes, 298 pages, no forbidden warnings, unchanged
TeX inputs, and PDF SHA256
`6f0c242cd4aed92bec05778ba79dc7f6e0e8c061b4b2f8cdd59b9a733c418eae`.
The newly added pages were visually inspected separately.

The [preceding CI receipt](preceding_ci_run.json) is specifically for
**parent** `53d60cbb4b51d64b3ff82d396ab74e21f704f3a9`, workflow run
`38375557288`, whose scientific pipeline completed successfully. Its
[computation log](preceding_computation.log) records 225 checks, including
25 C++ checks, and its [formalization log](preceding_formalization.log)
records a 26-job Lean build. These parent checks certify neither the new
analytic proofs nor a full executable replay of this later source tree.

[source_manifest.json](source_manifest.json) binds the actual preserved
files and the scientific sources at this checked checkpoint. It is not
a requirement that a future enlarged manuscript retain this checkpoint's
hash. The [bibliographic impact record](../../../../record/bibliographic_impact_feedback_20261013.json)
adds the inherited TRACE-060/Tropp dependency to TRACE-080 only; the core
concentration and feedback arguments derive their scalar exponential
inequality internally. The updated metadata audit actually passed all
416 negative controls. No new theorem-priority assertion is added.
