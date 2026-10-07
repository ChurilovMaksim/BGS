# R6 checked implementation repair

7 October 2026. All changes are confined to the isolated full repair checkout;
HEAD remains d37c92e563d10d25bb1d6ab85bedffc1f160f773 and the prior unpublished
staged tree is retained. The old failed remote run remains a failure record.
No stage, commit or publication is performed by this checkpoint integration.

## Repaired implementation contracts

- **R6-01/R6-02 replay freshness:** the final v3 intermediate-layer wrapper
  removes stale-output acceptance, compares fresh scientific fields against
  cached immutable expectations with typed explicit provenance exemptions,
  and checks copied worker inputs against original source pins after execution.
  The old baseline no-op false PASS is reproduced and retained. Initial repair
  generations are distinct from the final v3 receipt. All 24 final actual
  worker replays pass: six workers on Python 3.12/3.13, normal and optimized.
  Wrapper SHA-256:
  1714435ce1d59f04b2e0af118ff958eb292d31cd8de5e9000b960048e7132a16;
  maintenance test SHA-256:
  2d8cdf0ec24f8a8949d36e7c47dd0dcf7aecb3dfbe374ea6f5414e77a64c617b;
  final execution SHA-256:
  4440f437f8fa5365f8ab99e58d5ab57fe5044beac8f22717061b756c34d83d26.
- **R6-03/R6-04 arithmetic APIs:** magnetic/twisted public residues are checked
  as exact integer types and reduced as Python integers before int64 vector
  multiplication. Float/bool/string coercion is rejected; true bool/np.bool_
  remains the explicit parity contract. The original large np.int64 q overflow
  and fractional-q matrix/histogram disagreement are reproduced in the old
  probes, and fresh corrected probes agree. The 18-method suite executes
  533 expected-exception cases plus declared dense/histogram/root comparisons
  on both runtimes/modes. Unchanged recurrence, quantization, model formulas
  and reference expected scientific evidence are retained. The untouched
  finite-field module and exact arithmetic source pins are in the manifest.

These are implementation/input-contract repairs, not theorem corrections or
BGS identification. Counter-content normalization, full N=3571 trace-curve
rerun and practical extremely-small-tau asymptotic certification are excluded.
The assertion-dependent magnetic entry intentionally rejects optimized mode;
that refusal is recorded as an expected control rather than a numerical pass.

## Actual build and review boundary

The source-bound pre-final-freeze C++22 build compiled all 22 maintained C++
sources with fresh binary/source hashes. The Lean19 build compiled all 19
active modules in 22 jobs. Their source hashes match the prior unpublished
snapshot. They do not formalize new analytic phase/Schur/coercivity theorems.
Full post-freeze scientific, maintenance, manuscript and aggregate checks
remain the root integrator's separate gate. The fresh independent R6 protocol
review accepts the exact final source pins: 88 independent protocol fixtures
and 12 focused test runs pass in both runtimes/modes, and all 172 final v3
actual/expected/input/environment/process/log artifacts are verified.
Its [review](../evidence/r6_repair_checkpoint_20261007/bgs_r6_independent_review/REVIEW.md)
and [final seal](../evidence/r6_repair_checkpoint_20261007/bgs_r6_independent_review/final_seal.json)
are retained; seal SHA-256 is
2ca37c9944ef8575caeca856ed5b77cee130fa3b090b675f92d938c8e2b246fd.
Preparatory successes are not substituted for this final review.

## Receipts

[The explicit import](r6_checked_checkpoint_import.json) links original final
v3 expected/actual/copied-input/log receipts, arithmetic before/after and
bounded-coverage receipts, and the source-bound C++/Lean build records.
Historical paths and execution identities are unchanged. Generated binaries
and build trees are excluded. Build log envelopes decode losslessly to the
original bytes and SHA-256. Final whole-tree freeze and review manifests are
kept outside the repository until their separately authorized disposition.

## CI artifact lifetime

[The explicit CI routing delta](checkpoint_ci_artifact_routing.json) passes
the durable-output option to intermediate-layer, charge, Schur and generic
packet replays under each fresh logs/certificates-* directory. Existing CI
upload now retains their actual worker/output/provenance artifacts rather
than relying on a discarded temporary directory. Root-owned routing tests
pass in normal and optimized modes; this changes artifact lifetime, not the
scientific comparison or any theorem.
