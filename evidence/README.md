# Evidence

`evidence/` contains **promoted evidence only**. Promotion means that the object is still useful to the current research programme; it does not mean that every object is a theorem.

## Categories

### `certificates/`

Finite exact or finite-regression records. Each JSON file states its scope and producer. The load-bearing fixed-`K` Cayley certificate is regenerated from scratch in CI and compared with the committed JSON.

### `numerical/`

Descriptive floating-point diagnostics. These are not hypothesis tests and do not establish a limiting law. In particular:

- the spacing record reports an empirical CDF sup-distance to the Wigner surmise; the old IID-KS `pass` interpretation was removed because unfolded gaps from the same spectra are dependent;
- the matched window-count record compares the cat-map statistic with GOE under the **same historical window-count algorithm**. That algorithm is not the standard stationary number variance `Sigma^2(L)`, so the old `two-sigma/pass` language was removed.

### `reference/`

Minimal preserved inputs needed to reproduce or cross-check promoted finite records.

## Trust rule

A JSON file is interpreted only at the level stated by its `scope` or `interpretation` field. Numerical agreement is never silently upgraded to a proof; a fixed finite certificate is never silently upgraded to a uniform asymptotic theorem.

See `provenance.md` for the producer/validator mapping and `../record/claim_ledger.md` for repository-wide claim status.
