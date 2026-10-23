# R6 independent repair review

## Current verdict

All four R6 repairs pass the scoped implementation review, bounded focused
checks, and final-revision real-replay artifact verification on the final
frozen wrapper revision 1714435c… and final arithmetic hashes below. The
diagnostic-preservation issue identified during this review is resolved.
The implementation and finite assertions are verified in the stated range.
No mathematical theorem status changes follow from this engineering audit.

Audit target: full isolated `/workspace/shared/bgs_r6_repair_checkout`, HEAD
`d37c92e563d10d25bb1d6ab85bedffc1f160f773`, with the inherited prepared index.
This reviewer did not edit maintained repository sources, stage, commit,
publish, or modify `/workspace/shared/BGS`.

## Contract and dependency closure

- R6-01: compare every scientific JSON field recursively and type-strictly,
  excluding only the declared step-specific top-level environment and timing
  fields. Preserve both old and replay environment information. Reject invalid
  environment/timing metadata. Preserve actual/expected bytes and differing
  paths when scientific equality fails.
- R6-02: a successful producer process must create its declared regular,
  nonsymlink, contained output in a new private step directory where that
  output was absent beforehand. Original expected bytes remain outside this
  directory. Every copied original input must remain regular, nonsymlink,
  contained, and byte-identical after execution. This is a bounded correctness
  contract; it is not a security sandbox against arbitrary malicious Python.
- R6-03: normalize exact integer q representatives to Python ints and reduce
  modulo p before scalar or vectorized multiplication. All int64 vectorized
  products are confined to the existing safe prime range.
- R6-04: named integer scalar parameters and entries of H, q_values,
  character-index and discrete-log arrays reject floats, strings, fractions,
  complex numbers and booleans. NumPy integer scalars remain accepted.
  odd_parity remains a genuine bool/np.bool_ input. Counter contents retain the
  explicitly documented exact canonical histogram caller contract; validating
  arbitrary Counter keys/counts is outside this repair's accepted scope.

The six maintained replay workers only write their declared output. None
reads that output as an input. Their actual read dependencies are retained in
the new private directory, including the historical source bytes used by the
two residual controls' source_sha256 fields. Those identities are not silently
excluded by the scientific comparison. See
`dependency_and_sibling_wrapper_review.json` for exact read/write expressions,
line numbers and module hashes.

The mathematical interpretation remains six exact finite reviewer controls.
All-depth conclusions depend on separately accepted mathematical bridges;
these checks do not imply U-simplicity, gaps, or the BGS conjecture.

## Decisive checks

### Replay protocol

The first wrapper repair passed 72 expanded fixtures in Python 3.12/3.13,
normal and -O. Adding copied-input integrity produced 88 passing fixtures on
b51a968e…; all 88 were rerun successfully on final wrapper 1714435c…:

- zero-exit no-op, early return, and deleted output rejected
- directory, direct symlink, and broken symlink output rejected
- ancestor-directory symlink output escape rejected
- absolute, `..`, and dot output paths rejected
- malformed JSON rejected; raw actual output preserved with the evidence flag
- missing, extra, wrong-type and changed scientific fields rejected
- fresh correct output accepted, without staging its historical output first
- copied input mutation/deletion/directory/symlink/ancestor escape rejected
- original root source/config/blob bytes unchanged in every fixture
- scientific mismatches retain exact actual/expected bytes, their hashes, and
  the differing JSON paths

The input-integrity strengthening initially ran before optional actual output
preservation. A worker that mutated an input and created a fresh result was
correctly rejected, but its actual result would be removed with temporary
storage. The author moved fresh-result reading/preservation before the
input-integrity assertion. This changes failure evidence only. Independent
fixtures confirm fresh actual bytes, expected bytes, and process/log files
are preserved on copied-input mutation, deletion, directory replacement,
direct symlink replacement, and ancestor symlink escape failures.

The four first-repair real six-step receipts were independently checked
against decoded historical expectations and current worker module hashes.
The four input-integrity v2 six-step replays were additionally checked down
to all 172 preserved actual/expected/input/provenance/log artifacts. Final
v3 verification likewise passed all 24 replay steps and all 172 preserved
artifacts, including exact raw expectations, fresh actual result hashes,
type-strict scientific equality, every copied original input hash, both
environment records, and process/log hashes. Parent-owned six-step replays
were not duplicated by this audit.

The final execution receipt is
`/workspace/shared/bgs_r6_replay_repair/v3/execution.json`, SHA256
`4440f437f8fa5365f8ab99e58d5ab57fe5044beac8f22717061b756c34d83d26`.
The complete read-only verification is in
`real_replay_artifact_review_v3.json`. All four recorded executions used the
same frozen final wrapper SHA256 shown below.

### Arithmetic

Independent scalar Python-int modular arithmetic and direct complex scalar
sums passed in all four runtime/mode combinations:

- 20 full scalar Weyl-shift/compression matrices at p=7,31,43,199, each with
  direct matrix powers of orders 1,2,3 against exact word histograms
- 24 direct scalar character-sum moment checks at p=31,199, residue classes
  0,1 and both parity sectors
- 3 direct scalar Gauss-sum checks at p=199
- signed/unsigned NumPy q representatives up to uint64 scale, enormous
  positive and negative Python-int representatives, and huge character-index
  representatives

These are finite complex128 numerical oracles at the recorded tolerances.
They do not establish an asymptotic spectral law. Their source hashes are
checked before and after execution in `arithmetic_*_*.json`.

The maintained integer suite additionally checks 117 dense/histogram cases,
1144 exhaustive small square-root/representative probes, exact type errors,
nonpositive orders, zero q residues, int64 allocation bounds, mixed boolean
sequences, input array preservation, individual closed-form q probes, and
legitimate Python/NumPy boolean parity. The complete focused tests are rerun
in both runtimes and modes; see `maintained_tests_receipt.json`.

### Bounded sibling wrapper check

All ten declared cat_jet outputs are absent from their staged group mappings.
The five examined neighboring wrappers use fresh temporary output paths and
read expectations outside those paths. This was a static staging check, not
a full execution or repository-wide claim.

## Reviewed frozen source hashes

- intermediate_old_layers_certificates.py:
  `1714435ce1d59f04b2e0af118ff958eb292d31cd8de5e9000b960048e7132a16`
- test_intermediate_replay_freshness.py:
  `2d8cdf0ec24f8a8949d36e7c47dd0dcf7aecb3dfbe374ea6f5414e77a64c617b`

- magnetic_quotient.py:
  `a1ac5f2b025a20141ade087f5c31b2973ac3a8dd70ba3f03506e23c582bdf7dc`
- twisted_jacobi.py:
  `4f48218acc5c2fab9d6689e553d3dd1e8ce9f815ae00943c4fd08b825f146b04`
- jacobi.py:
  `5179856965d5bceff13d3e48b3d57400e485f04cfea1d264be685015835bd851`
- test_twisted_magnetic_integer_contracts.py:
  `fb35751966faba4c3e50854caa4655f9a4be343f3c6053c536139c801499b7b0`

## Residual boundaries

- Range-valid dlog arrays are not authenticated as actual logarithm tables;
  callers retain that existing semantic obligation.
- Supplied H must be a genuine subgroup; type/residue checking is not a new
  general subgroup certificate.
- Counter key/count validation remains caller-owned as explicitly scoped.
- Vectorized prime bounds prevent integer overflow, not memory exhaustion.
- The replay wrapper is not a malicious-code sandbox, and its captured-log
  cap is checked after capture. Those documented resource boundaries were not
  expanded by this repair.
- Full repository build/tests, publication, and mathematical proof promotion
  are outside this independent narrow review.

## Reproduction

From this evidence directory, run:

1. `python replay_boundary_checks.py`
2. `python run_maintained_tests.py`
3. For python3.12 and python3.13, with and without -O:
   `PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3.12 -B arithmetic_independent_checks.py`

All outputs stay in the evidence directory or private temporary fixtures.
No maintained-source write or staging is required.
