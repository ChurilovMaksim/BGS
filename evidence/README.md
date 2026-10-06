# Evidence

The [collective exact run](executions/20261006/collective-diffusion-exact-v2/manifest.json)
and [checks](executions/20261006/collective-diffusion-exact-v2/checks.json)
record FM-019's finite sign/projection controls under its
[contract](20261006/collective_diffusion_contract_v2.json). The separate
[spectrum run](executions/20261006/collective-diffusion-spectrum/manifest.json)
records descriptive float64 values and selected-block exclusions under
its [contract](20261006/collective_diffusion_spectrum_contract.json).
Neither run proves the universal analytic gap or original BGS.
The [arithmetic correction](../record/history/2026/collective_diffusion_arithmetic_correction_20261006.md)
identifies the superseded initial run and preserves its original inputs.

The [6 October operator-transfer run](executions/20261006/operator-transfer/manifest.json)
and [results](executions/20261006/operator-transfer/checks.json) record
FM-018's exact modular, cyclotomic and rational controls. The
[contract](20261006/frozen_operator_transfer_contract.json) states the
ranges and resources. The [Wolfram response](20261006/frozen_operator_transfer_wolfram.json)
preserves six True identities and all printed diagnostics. The
[integration record](executions/20261006-operator-transfer-integration.json)
separates local checks and manuscript build from the analytic theorem.

The [5 October noise-removal run](executions/20261005/noise-removal/manifest.json)
and [results](executions/20261005/noise-removal/checks.json) record FLOW-015's
independent rational generator/character/gap controls and separately labelled
binary64 quadrature. The [contract](20261005/noise_removal_contract.json)
declares exact coverage, resources and non-claims.
The [integration record](executions/20261005-noise-removal-integration.json)
separates five focused regressions, source synchronization, full manuscript
build and selected-page inspection from proof and remote CI.

The [polynomial coboundary run](executions/20261004/polynomial-coboundary/manifest.json)
records FLOW-011 finite coefficient and exact exponent controls.
[Wolfram evidence](20261004/polynomial_coboundary_wolfram.json) contains
the actual scalar/exponent response; it is not a stochastic proof certificate.
The [integration record](executions/20261004-polynomial-integration.json)
separates focused regression, source synchronization and manuscript build.

The [signed Heisenberg packet](20260930/signed_heisenberg_manifest.json)
records TRACE-010 finite controls. Its
[execution record](executions/20260930-signed-heisenberg.json) separates
exact algebra, focused regression, manuscript parsing and selected-page review.

`evidence/` contains promoted evidence only. Promotion means that an object is useful to the current research programme; it does not mean every object is a theorem.

## Categories

### `certificates/`

Exact finite certificates, finite implementation regressions, and dated execution records. `provenance.md` is the path-complete current inventory and maps all committed certificate files to their maintained interpretation/validation surface.

Not every verifier writes a committed certificate. In particular, the extremal-resonance producer writes exact witness/replay artifacts to the requested verification log directory and is independently replayed by C++; this is intentional workspace behavior.

### `numerical/`

Descriptive floating-point diagnostics. They are not hypothesis tests and do not establish limiting laws. The maintained spacing/window records diagonalize the full complex Hermitian sector matrix; historical entrywise-real projection is recorded as a bug in `../record/retractions.md`.

### `reference/`

Only minimal preserved inputs required by maintained regressions live here. Consumers pin their hashes before use.

### `executions/`

New execution/build manifests belong here. Legacy execution records remain at
their original paths when moving them would destroy path-level provenance.
`index.json` records the canonical evidence taxonomy and those legacy
exceptions.

### Dated research packets

`20260922/` preserves an earlier finite-orbit delivery and its historical
execution manifest. `20260923/` contains the exact finite frozen-symbol
check and the separately labelled floating frozen-kick diagnostics. These
directories mix evidence types; consult each object's scope and its dated
integration review. They are indexed separately in `index.json`, not treated
as general execution logs or continuum proofs.

## Trust rule

Interpret a JSON object only at the level stated by its `scope`, `interpretation`, run command and associated review. Numerical agreement is never silently upgraded to proof; a finite certificate is never silently upgraded to a growing-parameter theorem; a failed workflow with `steps=[]` is not treated as a scientific test failure.

Repository-wide claim status is controlled solely by
`../record/claim_ledger.md`. Stable IDs and cross-layer links live in
`../record/claims.json` and cannot strengthen that ledger.

See `provenance.md` for the current certificate inventory and `index.json`
for machine-readable evidence classes.
