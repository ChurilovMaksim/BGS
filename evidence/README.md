# Evidence

This directory contains promoted evidence, separated by evidentiary strength.

- `certificates/` — exact finite machine-readable certificates and regression
  anchors. These certify only their stated finite scope unless the associated
  mathematical note proves a uniform statement.
- `numerical/` — finite numerical spectral/statistical evidence. These files do
  not establish a limiting law.
- `reference/` — minimal preserved inputs needed by active regression checks.
- `provenance.md` — resolves generation-time paths embedded in retained JSON
  records to their present locations.

Some retained JSON files intentionally keep the `producer` string that was
written at generation time. If that old path is no longer active, the source is
preserved under `record/corpus/<producer>`. CI checks that every such producer
resolves either directly or through this historical prefix, and that retained
reference inputs still resolve under `evidence/`.

For historical outputs that have not been re-audited, use
`record/corpus/data/` instead. The distinction is intentional.
