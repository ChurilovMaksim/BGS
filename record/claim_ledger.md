# Claim ledger

This is the repository-wide status authority. Historical files can contain stronger language; this file wins.

## Status vocabulary

- **EXACT** — current algebraic identity/derivation.
- **FINITE-CERTIFICATE** — exact machine/exhaustive statement at explicit finite parameters.
- **NUMERICAL** — descriptive floating-point evidence only.
- **DRAFT** — promising proof route with named unresolved obligations.
- **SCOPED-HISTORICAL** — useful earlier result whose current safe scope is narrower than its old label.
- **RETRACTED** — false or superseded; retained only to prevent regression.

## Active exact chain

| Claim | Status | Current support |
|---|---|---|
| pair-key bijection and diagonal multiplicity `p-2` | EXACT | `mathematics/fourth_moment_reduction.md`; Lean/Python/C++ checks |
| finite `k=2` constraint count / parameterization | FINITE-CERTIFICATE | `formalization/Bgs/PairKeySecondMoment.lean`, design `p=53,K=13` |
| finite `k=4` key multiplicities / `V4` count | FINITE-CERTIFICATE | `formalization/Bgs/PairKeyFourthMoment.lean`, design `p=53,K=13` |
| closed formula `|V4|=(K^2+1)p^2-(6K^2+3K)p+13K^2-3K` | EXACT + FINITE REGRESSION | active C++ and Python |
| Fourier fourth-moment factorization | EXACT + FINITE REGRESSION | current derivation + active C++ |
| Cayley identity and additive-energy reduction | EXACT | `mathematics/cayley_additive_energy.md`; current Python verifier |
| 720 integer matching rank classification; only characteristic-2 extra rank drop | FINITE-CERTIFICATE | `computations/verification/mixed_cayley_energy.py` |
| `E_11={23,67,89}` | FINITE-CERTIFICATE | complete exact resultants recomputed in CI |
| `E_13={53,79,131,157,313}` | FINITE-CERTIFICATE | complete exact resultants recomputed in CI |
| arbitrary-`K` explicit exceptional set / useful uniform growing-`K` bound | OPEN | not inferred from `K=11,13` |
| `(p,K)=(461,23)` energy `1190` vs baseline `902` | FINITE-CERTIFICATE / negative control | current Python + Lean |
| off/off estimate `O(K^2 p+K^4 sqrt(p)+K^4)` | DRAFT | elliptic/sheaf obligations remain |
| microscopic BGS/GOE local eigenphase law | OPEN | no current proof |

## Earlier useful foundations

| Claim | Status | Scope |
|---|---|---|
| torus level-set cardinalities/orbit counts/freeness | FINITE-CERTIFICATE | `p=199,K=11`, Lean `native_decide` |
| recorded branch scale `c^2=5 mod 199` | FINITE-CERTIFICATE | `p=199`, Lean kernel `decide` |
| twisted-Jacobi scalar formula / q-curve moments | FINITE REGRESSION | explicit recorded designs only; historical domain condition enforced in current interpretation |
| antiunitary eigenspace preservation logic | SCOPED-HISTORICAL | audited chart; no blanket global GOE-class promotion |
| relation/shape counts | SCOPED-HISTORICAL finite evidence | useful regression/discovery only |
| all-orders Catalan / full-group arcsine package | NOT PROMOTED | historical word-trace reduction has unresolved rewrite case |

## Numerical records

`evidence/numerical/goe_spacing.json` reports a descriptive empirical CDF distance; its historical IID-KS pass/fail interpretation is withdrawn.

`evidence/numerical/matched_window_count_variance.json` is a descriptive matched-GOE forward-window statistic, not stationary `Sigma^2(L)` and not an inferential pass/fail test.

## Retractions

See `retractions.md` for mechanisms. Historical Möbius/M4D, one-sided mixed counting, ESY-to-BGS shortcut, noncommutative trace shortcut, wrong comparison-prime claims, unresolved word-trace all-orders promotion, Hecke-centering Julia, `cdense_transfer`, `sol6`, and unsupported Sp(2g) extrapolations are not active results.
