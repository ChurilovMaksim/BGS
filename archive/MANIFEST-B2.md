# MANIFEST-B2 — phase 1, package B2: root integration receipts of evidence/executions

Byte-for-byte archival copies of the 14 dated integration receipts that lived in the root of
`evidence/executions/`, moved under `archive/evidence/executions/` with the original paths
preserved after the `archive/` prefix. Source tree: post-package-C tree (main @ 2401f0f).

**claims.json migration is part of this package.** `record/claims.json` is migrated in the same
commit: exactly 10 `evidence[]` path values in 8 claims (BGS-FLOW-011, BGS-FLOW-021, BGS-FM-013,
BGS-FM-016, BGS-FM-019, BGS-TRACE-011, BGS-TRACE-012, BGS-TRACE-013) gain the `archive/` prefix;
no other field or value is touched. `evidence/executions/README.md` is migrated in the same
commit: its 3 markdown links to the receipts now point to `../../archive/evidence/executions/…`.

**11 working-layer notes under `record/` are deliberately NOT edited by this package**
(`signed_heisenberg_review_20260930.md`, `folded_quadratic_review_20261001.md`,
`resonant_density_review_20261001.md`, `folded_quadratic_audit_20261004.md`,
`polynomial_coboundary_review_20261004.md`, `all_order_program_20261005.md`,
`critical_noise_program_20261005.md`, `growing_degree_program_20261005.md`,
`noise_removal_program_20261005.md`, `heisenberg_pair_program_20261005.md`,
`frozen_operator_transfer_program_20261006.md`). Their links to the pre-move receipt paths are
frozen wave records; they resolve through this manifest. Recomputing their link geometry is an
**entry condition of package F** (archival of the notes themselves).

Frozen evidence carriers (53 files / 624 lines) that mention the receipt paths are likewise not
edited and resolve through this manifest. `evidence/index.json` and `evidence/provenance.md` do
not index these receipts; this manifest is their index after the move.

| Old path | New path | git blob SHA | Bytes |
|---|---|---|---:|
| `evidence/executions/20260930-signed-heisenberg.json` | `archive/evidence/executions/20260930-signed-heisenberg.json` | `73daccabad9e34345dee70059ba295b77b72777f` | 127771 |
| `evidence/executions/20261001-folded-quadratic.json` | `archive/evidence/executions/20261001-folded-quadratic.json` | `43fe83622857621efad31216f433f6a3fbfe1400` | 19730 |
| `evidence/executions/20261001-resonant-density.json` | `archive/evidence/executions/20261001-resonant-density.json` | `15683cb1931d87e9c2f649c4ea19a69f28f106f7` | 22203 |
| `evidence/executions/20261004-completion.json` | `archive/evidence/executions/20261004-completion.json` | `b0799789df6f6ef51837591652479b00937c7f9b` | 21448 |
| `evidence/executions/20261004-expansion-wavepacket.json` | `archive/evidence/executions/20261004-expansion-wavepacket.json` | `d3ebec52672234e34cac961b99ca26d2b9e83e9b` | 9503 |
| `evidence/executions/20261004-folded-quadratic-format-correction.json` | `archive/evidence/executions/20261004-folded-quadratic-format-correction.json` | `ca3eedf226b2258dac99ac786e4ea69bc6362b18` | 5943 |
| `evidence/executions/20261004-polynomial-integration.json` | `archive/evidence/executions/20261004-polynomial-integration.json` | `636e3e4561933db5349ad1fc63a5f6c9d586894b` | 26360 |
| `evidence/executions/20261005-all-order-integration.json` | `archive/evidence/executions/20261005-all-order-integration.json` | `dd168b9c9ea2006bac0dbcab2839b22252e0bc58` | 9046 |
| `evidence/executions/20261005-critical-noise-integration.json` | `archive/evidence/executions/20261005-critical-noise-integration.json` | `b4cc2f36c37ac4264557ba2dd925b47fd86561a2` | 12046 |
| `evidence/executions/20261005-degree-growth-integration.json` | `archive/evidence/executions/20261005-degree-growth-integration.json` | `719459d39ec49df044bc0dca6c05e1af567a66c0` | 11659 |
| `evidence/executions/20261005-noise-removal-integration.json` | `archive/evidence/executions/20261005-noise-removal-integration.json` | `3459ad2041fc3929c90ee7fd3c292c4a53cddcfa` | 20214 |
| `evidence/executions/20261005-pair-heat-integration.json` | `archive/evidence/executions/20261005-pair-heat-integration.json` | `db1858b095ef10d1e47d54451672c793863263ce` | 12945 |
| `evidence/executions/20261006-collective-diffusion-integration.json` | `archive/evidence/executions/20261006-collective-diffusion-integration.json` | `ea6df25f3a664a612519c4f859751055287866db` | 19658 |
| `evidence/executions/20261006-operator-transfer-integration.json` | `archive/evidence/executions/20261006-operator-transfer-integration.json` | `c757e1124cef51985be7db7a1d30ac00b27e6868` | 50408 |

Total: 14 files, 368934 bytes.
