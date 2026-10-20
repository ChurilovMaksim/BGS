# Evidence and execution scope

[The 20 October reconciliation](../record/repository_reconciliation_20261020.md) separates full baseline integrity, executed checks and unavailable suites. Historical negative evidence remains unchanged.

This directory retains promoted finite certificates, diagnostics, preserved
regression inputs and actual execution/build receipts. Promotion means that
an object is useful to the research record; it does not make it a theorem.
[The claim ledger](../record/claim_ledger.md) controls scientific status.

## Categories

| Surface | Interpretation |
|---|---|
| [certificates/](certificates/) | Exact finite arithmetic and bounded implementation regressions; [provenance.md](provenance.md) maps committed certificate files to their validator/interpretation |
| [numerical/](numerical/) | Descriptive floating-point diagnostics, with declared precision and finite coverage |
| [reference/](reference/) | Minimal pinned inputs required by maintained regressions |
| [executions/](executions/README.md) | New commands, source hashes, versions, outputs, failures and build receipts |
| Dated legacy packets | Preserved mixed evidence classes at original paths; [index.json](index.json) records their taxonomy and exceptions |

Not every verifier writes a committed certificate. Reproducible temporary
outputs belong under the requested build/log directory until deliberately
promoted with provenance. Historical evidence is immutable: corrections
identify a superseded object rather than rewriting its original output.

## Selected current packets

| Packet | Actual coverage |
|---|---|
| [Haar feedback, 12 October](executions/20261012/haar-feedback/README.md) | Independent analytic reconstruction and transfer review, five exact colligations, symbolic Jacobians, twelve moment integrals, actual Wolfram identities and separate CI provenance |
| [Two-step drift, 12 October](executions/20261012/two-step-drift/README.md) | Independent one-step theorem reconstruction, exact phase residues and rational unitary controls |
| [Unitary obstruction, 12 October](executions/20261012/unitary-two-step/README.md) | Independent genuine-unitary construction review, exact and descriptive finite controls at their declared scopes |
| [Phase channel and matrix jets, 8 October](executions/20261008/phase-channel-jet/README.md) | Independent internal proof reconstructions; Python finite quadrature; exact C++ counts; Wolfram identities; 20-module Lean build; 280-page TeX build and selected-page inspection |
| [Original channel gap](executions/20261006/original-channel-gap/integration.json) | Source-bound FM-020 finite controls and formalization/integration receipt |
| [Collective exact controls](executions/20261006/collective-diffusion-exact-v2/manifest.json) | Corrected modular/rational controls; the [separate spectrum run](executions/20261006/collective-diffusion-spectrum/manifest.json) is float64 descriptive evidence |
| [Operator transfer](executions/20261006/operator-transfer/manifest.json) | Exact modular, cyclotomic and rational controls; symbolic Wolfram response is separately retained |
| [Noise removal](executions/20261005/noise-removal/manifest.json) | Independent exact generator/character controls and separately labelled binary64 quadrature |

Other packets are discoverable through [index.json](index.json),
[provenance.md](provenance.md), their theorem source and the
[research record](../record/README.md). These links do not report a new rerun
of historical suites.

## Trust rule

Interpret each object at the level stated by its scope, arithmetic, command
and associated review. Finite agreement cannot certify a growing-parameter
limit. A Lean build certifies its stated propositions with printed trust
dependencies, not adjacent informal analytic proofs. A workflow failure
before scientific steps ran is not a failed theorem test.

Historical spectral diagnostics with nonmonotone polynomial unfolding are
not endorsed. The [correction record](../record/audits/spectral_diagnostics_correction_20261006.md)
specifies order-preserving smoothing and sensitivity controls. Corrected
finite spacing plots still do not establish BGS. No packet here removes the
open balanced, signed undamped or deterministic all-order obligations.
