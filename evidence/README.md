# Evidence

`evidence/` contains promoted evidence only. Promotion means that an object is useful to the current research programme; it does not mean every object is a theorem.

## Categories

### `certificates/`

Exact finite certificates, finite implementation regressions, and dated execution records. `provenance.md` is the path-complete current inventory and maps all committed certificate files to their maintained interpretation/validation surface.

Not every verifier writes a committed certificate. In particular, the extremal-resonance producer writes exact witness/replay artifacts to the requested verification log directory and is independently replayed by C++; this is intentional workspace behavior.

### `numerical/`

Descriptive floating-point diagnostics. They are not hypothesis tests and do not establish limiting laws. The maintained spacing/window records diagonalize the full complex Hermitian sector matrix; historical entrywise-real projection is recorded as a bug in `../record/retractions.md`.

### `reference/`

Only minimal preserved inputs required by maintained regressions live here. Consumers pin their hashes before use.

## Trust rule

Interpret a JSON object only at the level stated by its `scope`, `interpretation`, run command and associated review. Numerical agreement is never silently upgraded to proof; a finite certificate is never silently upgraded to a growing-parameter theorem; a failed workflow with `steps=[]` is not treated as a scientific test failure.

Repository-wide claim status is controlled by

- `../record/claim_ledger.md` for the base corpus;
- `../record/claim_ledger_addendum_20260907.md` for the dated later/corrected scopes.

See `provenance.md` for the current certificate inventory.