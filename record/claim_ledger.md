# Claim ledger

This is the repository-wide status authority. Historical commits can contain
stronger language; this file wins.

## Status vocabulary

- **EXACT** — current algebraic identity/derivation with stated hypotheses.
- **FINITE-CERTIFICATE** — exact exhaustive or kernel-checked statement at
  explicit finite parameters.
- **FINITE-REGRESSION** — finite implementation/reference agreement; useful for
  reproducibility but not a symbolic theorem.
- **NUMERICAL** — descriptive floating-point evidence only.
- **DRAFT** — promising proof route with named unresolved obligations.
- **OPEN** — closure condition not yet achieved.
- **SCOPED-HISTORICAL** — useful earlier result whose safe present scope is
  narrower than its old label.
- **NOT-PROMOTED** — retained as evidence/conjectural structure but not accepted
  into the current theorem set.
- **RETRACTED** — false or superseded.

## Active exact chain

| Claim | Status | Current support |
|---|---|---|
| pair-key bijection and diagonal multiplicity `p-2` | **EXACT** | `mathematics/fourth_moment_reduction.md`; Python/C++/Lean finite checks |
| constrained off-diagonal pair count `(K-1)(K-2)` | **EXACT + FINITE-CERTIFICATE** | immediate from pair-key bijection; `PairKeySecondMoment.lean` checks `(53,13)` |
| finite `k=2` pair-key parametrization at `(53,13)` | **FINITE-CERTIFICATE** | `formalization/Bgs/PairKeySecondMoment.lean` |
| finite `k=4` key multiplicities / `V4` count at `(53,13)` | **FINITE-CERTIFICATE** | `formalization/Bgs/PairKeyFourthMoment.lean` |
| `|V4|=(K^2+1)p^2-(6K^2+3K)p+13K^2-3K` | **EXACT + FINITE-CERTIFICATE** | current derivation + independent C++/Python checks |
| character/Fourier fourth-moment collapse and nonzero-frequency mean/variance | **EXACT + FINITE-REGRESSION** | `mathematics/fourth_moment_reduction.md`, C++/Python |
| Cayley identity and additive-energy reduction | **EXACT** | `mathematics/cayley_additive_energy.md` |
| 720 matching rank classification; only characteristic-2 extra rank drop | **FINITE-CERTIFICATE** | `computations/verification/mixed_cayley_energy.py` |
| `E_11={23,67,89}` | **FINITE-CERTIFICATE** | complete exact resultants recomputed in CI |
| `E_13={53,79,131,157,313}` | **FINITE-CERTIFICATE** | complete exact resultants recomputed in CI |
| generic/exceptional finite Cayley-energy controls | **FINITE-CERTIFICATE** | independent C++/Python plus `formalization/Bgs/CayleyEnergy.lean` |
| arbitrary-`K` explicit exceptional set / useful uniform growing-`K` bound | **OPEN** | not inferred from `K=11,13` |
| `(p,K)=(461,23)` energy `1190` vs baseline `902` | **FINITE-CERTIFICATE** negative control | C++/Python/Lean |
| off/off estimate `O(K^2 p+K^4 sqrt(p)+K^4)` | **DRAFT** | elliptic/sheaf obligations remain |
| microscopic BGS/GOE local eigenphase law | **OPEN** | no current proof |

## Earlier useful foundations

| Claim | Status | Scope |
|---|---|---|
| torus level-set cardinalities/orbit counts/freeness | **FINITE-CERTIFICATE** | `p=199,K=11`, Lean |
| recorded branch scale `c^2=5 mod 199` | **FINITE-CERTIFICATE** | `p=199`, Lean |
| twisted-Jacobi scalar formula / q-curve moments | **FINITE-REGRESSION** | explicit designs; maintained producer `twisted_jacobi_regression.py` |
| antiunitary eigenspace-preservation logic | **SCOPED-HISTORICAL** | no blanket global GOE-class promotion |
| relation/shape finite counts | **SCOPED-HISTORICAL** | no current theorem dependency; provenance in Git history |
| all-orders Catalan / full-group arcsine package | **NOT-PROMOTED** | unresolved historical word-trace rewrite |
| higher-rank/Sp(2g) exploratory diagnostics | **NOT-PROMOTED** | useful historical tests, but no current general theorem re-certified |

## Numerical records

`evidence/numerical/goe_spacing.json` is a descriptive empirical CDF-distance
record produced from the **full complex Hermitian** sector matrix. Its
historical IID-KS pass/fail interpretation is withdrawn.

`evidence/numerical/matched_window_count_variance.json` is a descriptive
matched-GOE forward-window statistic. It is not stationary `Sigma^2(L)` and is
not an inferential pass/fail test.

A reconstruction-era implementation accidentally replaced `M+M^*` by its
entrywise real part before diagonalization. The numerical records were
regenerated after this was detected; no exact claim depended on those records.

## Retractions

See [`retractions.md`](retractions.md) for mechanisms. In particular, the
historical Möbius/M4D M1 proof, one-sided mixed counting, ESY-to-BGS shortcut,
noncommutative trace shortcut, Hecke-centering Julia line, `cdense_transfer`,
`sol6`, unsupported Sp(2g) extrapolations, the temporary real-projection
spectral bug, and all-orders promotion from the unresolved word-trace route are
not active results.
