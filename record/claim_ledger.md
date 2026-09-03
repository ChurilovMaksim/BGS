# Claim ledger

This is the repository-wide status authority. Historical commits can contain
stronger language; this file wins.

## Status vocabulary

- **EXACT** — current algebraic identity/derivation.
- **FINITE-CERTIFICATE** — exact machine/exhaustive statement at explicit
  finite parameters.
- **NUMERICAL** — descriptive floating-point evidence only.
- **DRAFT** — promising proof route with named unresolved obligations.
- **SCOPED-HISTORICAL** — useful earlier result whose safe current scope is
  narrower than its old label.
- **RETRACTED** — false or superseded.

## Active exact chain

| Claim | Status | Current support |
|---|---|---|
| pair-key bijection and diagonal multiplicity `p-2` | **EXACT** | `mathematics/fourth_moment_reduction.md`; Python/C++/Lean finite checks |
| finite `k=2` constraint count / parametrization | **FINITE-CERTIFICATE** | `formalization/Bgs/PairKeySecondMoment.lean`, `p=53,K=13` |
| finite `k=4` key multiplicities / `V4` count | **FINITE-CERTIFICATE** | `formalization/Bgs/PairKeyFourthMoment.lean`, `p=53,K=13` |
| `|V4|=(K^2+1)p^2-(6K^2+3K)p+13K^2-3K` | **EXACT + FINITE REGRESSION** | current derivation + C++/Python |
| Fourier fourth-moment factorization and nonzero-frequency mean/variance | **EXACT + FINITE REGRESSION** | `mathematics/fourth_moment_reduction.md`, C++/Python |
| Cayley identity and additive-energy reduction | **EXACT** | `mathematics/cayley_additive_energy.md` |
| 720 matching rank classification; only characteristic-2 extra rank drop | **FINITE-CERTIFICATE** | `computations/verification/mixed_cayley_energy.py` |
| `E_11={23,67,89}` | **FINITE-CERTIFICATE** | complete exact resultants recomputed in CI |
| `E_13={53,79,131,157,313}` | **FINITE-CERTIFICATE** | complete exact resultants recomputed in CI |
| generic/exceptional finite Cayley-energy controls | **FINITE-CERTIFICATE** | independent C++/Python plus `formalization/Bgs/CayleyEnergy.lean` |
| arbitrary-`K` explicit exceptional set / useful uniform growing-`K` bound | **OPEN** | not inferred from `K=11,13` |
| `(p,K)=(461,23)` energy `1190` vs baseline `902` | **FINITE-CERTIFICATE / negative control** | C++/Python/Lean |
| off/off estimate `O(K^2 p+K^4 sqrt(p)+K^4)` | **DRAFT** | elliptic/sheaf obligations remain |
| microscopic BGS/GOE local eigenphase law | **OPEN** | no current proof |

## Earlier useful foundations

| Claim | Status | Scope |
|---|---|---|
| torus level-set cardinalities/orbit counts/freeness | **FINITE-CERTIFICATE** | `p=199,K=11`, Lean |
| recorded branch scale `c^2=5 mod 199` | **FINITE-CERTIFICATE** | `p=199`, Lean |
| twisted-Jacobi scalar formula / q-curve moments | **FINITE REGRESSION** | explicit recorded designs; maintained producer in `computations/verification/twisted_jacobi_regression.py` |
| antiunitary eigenspace-preservation logic | **SCOPED-HISTORICAL** | no blanket global GOE-class promotion |
| relation/shape counts | **SCOPED-HISTORICAL finite evidence** | no current theorem dependency; provenance in Git history |
| all-orders Catalan / full-group arcsine package | **NOT PROMOTED** | historical word-trace reduction had an unresolved rewrite case |

## Numerical records

`evidence/numerical/goe_spacing.json` is a descriptive empirical CDF-distance
record. Its historical IID-KS pass/fail interpretation is withdrawn.

`evidence/numerical/matched_window_count_variance.json` is a descriptive
matched-GOE forward-window statistic. It is not stationary `Sigma^2(L)` and is
not an inferential pass/fail test.

## Retractions

See `retractions.md` for mechanisms. In particular, the historical
Möbius/M4D M1 proof, one-sided mixed counting, ESY-to-BGS shortcut,
noncommutative trace shortcut, Hecke-centering Julia line, `cdense_transfer`,
`sol6`, unsupported Sp(2g) extrapolations, and all-orders promotion from the
unresolved word-trace route are not active results.
