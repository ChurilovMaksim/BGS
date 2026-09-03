# Evidence

`evidence/` contains **promoted evidence only**. Promotion means that an object
is still useful to the current research programme; it does not mean every
object is a theorem.

## Categories

### `certificates/`

Exact finite certificates or finite implementation regressions. Each JSON file
states its scope and maintained producer. The fixed-`K` Cayley audit is
regenerated from scratch in CI and compared structurally with the committed
JSON.

### `numerical/`

Descriptive floating-point diagnostics. These are not hypothesis tests and do
not establish a limiting law.

- `goe_spacing.json` reports an empirical CDF sup-distance to the Wigner
  surmise. The old IID-KS `pass` interpretation is rejected because unfolded
  gaps from the same spectra are dependent.
- `matched_window_count_variance.json` compares a cat-map statistic with GOE
  under the **same forward-window algorithm**. That algorithm is edge-truncated
  and is not stationary number variance `Sigma^2(L)`.

Both maintained numerical records diagonalize the **full complex Hermitian**
sector matrix `M+M^*`. CI recomputes the complete committed diagnostics and
compares them numerically. A temporary reconstruction-era entrywise-real
projection is recorded as a bug in `../record/retractions.md`.

### `reference/`

Only the minimal preserved inputs required by a maintained regression live
here. Their SHA-256 hashes are pinned before use.

## Trust rule

A JSON file is interpreted only at the level stated by its `scope` or
`interpretation` field. Numerical agreement is never silently upgraded to a
proof; a fixed finite certificate is never silently upgraded to a uniform
asymptotic theorem.

See [`provenance.md`](provenance.md) for producer/validator mapping and
[`../record/claim_ledger.md`](../record/claim_ledger.md) for repository-wide
claim status.
