# Green compression: exact review and finite scope

**Claim:** BGS-TRACE-077. Base main:
`54e45c1e45930587c0268244fffc29c8114b5627`.

The frozen [candidate](candidate_reviewed.md) was independently reconstructed
in the [report](independent_review.md). The candidate hash is
`4ca12a1de53fd141ab0ff60cf36644ae7bd985a6e0c4e957bbf4c6bcd0a4d8d8`;
the report hash is
`ea00ace98859aa7df92ffcb0bce080721dcf89f5775f1b5cb6fef9c5150c4b37`.
The maintained version corrects “predictable increments” to “adapted
martingale differences with predictable coefficients and stop mask” and
spells out existence of the reduced inverse. Its probability estimate
is for the stopped prefix and includes the first crossing. It does not
bound the probability of early entry exit.

New independent root controls were actually executed with:

```sh
PYTHONPATH=/workspace/scratch/06745ba532e4/research_session/runtime_deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 timeout 90 \
python3 computations/verification/green_compression.py \
  --output build/green-compression/controls.json
```

The exact [output](controls.json) is a byte copy of that run. SymPy rational
arithmetic checked four nonnormal stochastic complements (including
singleton and empty deletion), one noncommuting inverse expansion and
rejection of two incorrect algebraic variants. NumPy complex128 checked
four adaptive feedback steps from an explicitly perturbed Fourier unitary
of size 96. Maximum operator residual was below `9e-16`; asserted tolerance
was `2e-12`. This is not an exhaustive phase test, probability experiment,
actual fixed-coupling map simulation or proof of BGS.

The reviewer's controls are separately described in its report and were
not relabelled as this root execution. The analytic proof, finite controls,
metadata checks and any later CI run have different evidentiary roles.
No new Lean or C++ certificate is claimed for this theorem.

[Maintained-source transfer check](transfer_review.md) pins the proof SHA256
`fb134739b13587648ac8e820e170717343b589b4f085c6ceb74f599a39663748`.
No later substantive proof changes are covered by that report.

## Repository and manuscript execution

The promoted workspace receipt records six selected checks, all passed,
with the source tree unchanged during execution. It is a scoped run, not
a new full-workspace or Lean run. Logs retain their original build paths.
The unified manuscript passed three LaTeX passes (295 pages); every page
was parsed, final source hashes were rechecked, and pages 290–291 containing
the new theorem were visually inspected. PDF SHA256:
`783c0da0b08fa0e13d3e9ad63aeb7ad37a4cf2a8fda387dbb8a2f2a9d48b098c`.

`preceding_ci_run.json` and the two decoded logs are actual retrieved
GitHub receipts for **preceding** head
`54e45c1e45930587c0268244fffc29c8114b5627`, run `38244276392`,
which succeeded on 12 October at 12:07:33 UTC. Its computation log records
236 maintenance tests; its formalization log records a successful build
of 26 jobs. These are not TRACE-077 head receipts or formal certificates
for the new analytic argument. Historical caches and evidence remain unchanged.
