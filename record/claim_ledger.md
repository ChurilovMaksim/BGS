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
| pair-key bijection off diagonal and diagonal multiplicity `p-2` | EXACT | `mathematics/fourth_moment_reduction.md`; Python/C++ cross-checks |
| exact `k=2` constraint count / parametrization at audited design | FINITE-CERTIFICATE | `formalization/Bgs/PairKeySecondMoment.lean` |
| exact `k=4` pair-key multiplicities and `V4` count at audited design | FINITE-CERTIFICATE | `formalization/Bgs/PairKeyFourthMoment.lean` |
| closed formula `|V4|=(K^2+1)p^2-(6K^2+3K)p+13K^2-3K` | EXACT + FINITE REGRESSION | current Python/C++ verifier |
| character collapse / Fourier mean-variance reduction | EXACT | `mathematics/fourth_moment_reduction.md` plus finite checks |
| Cayley identity `d(u,v)=2/(c(u)-c(v))` and additive-energy reduction | EXACT | `mathematics/cayley_additive_energy.md`; current exact producer |
| 720 matching rank classification; only characteristic-2 rank drop | FINITE-CERTIFICATE over integer systems | `computations/verification/mixed_cayley_energy.py` |
| `E_11={23,67,89}` | FINITE-CERTIFICATE | exact resultants recomputed in CI |
| `E_13={53,79,131,157,313}` | FINITE-CERTIFICATE | exact resultants recomputed in CI |
| `(p,K)=(461,23)` mixed energy `1190` vs baseline `902` | FINITE-CERTIFICATE / negative control | current Python gate + Lean finite record |
| off/off elliptic/sheaf estimate `O(K^2 p+K^4 sqrt(p)+K^4)` | DRAFT | `mathematics/elliptic_pencil.md`; hypotheses not fully closed |
| microscopic BGS/GOE local eigenphase law | OPEN | no current proof |

## Earlier useful foundations

| Claim | Status | Scope |
|---|---|---|
| torus level-set cardinalities/orbit counts/freeness | FINITE-CERTIFICATE | `p=199`, Lean `native_decide` |
| recorded branch scale `c^2=5 mod 199` | FINITE-CERTIFICATE | `p=199`, kernel `decide` |
| twisted-Jacobi scalar formula / q-curve moments | FINITE REGRESSION | explicit recorded designs only |
| antiunitary eigenspace preservation logic | SCOPED-HISTORICAL | audited kernel chart; no blanket global GOE-class promotion |
| relation/shape counts | SCOPED-HISTORICAL finite evidence | useful regression/discovery only |
| all-orders Catalan / full-group arcsine package | NOT PROMOTED | historical word-trace reduction has unresolved rewrite case |

## Numerical records

`evidence/numerical/goe_spacing.json` is a descriptive empirical CDF-distance record. Its historical IID-KS pass/fail interpretation is withdrawn.

`evidence/numerical/matched_window_count_variance.json` is a descriptive matched-GOE forward-window statistic. It is not standard stationary number variance and carries no inferential pass/fail label.

## Retractions

The complete list and mechanisms are in `retractions.md`. In particular: historical Möbius/M4D, Run-93.2 one-sided mixed counting, ESY-to-BGS shortcut, noncommutative trace shortcut, wrong N=95419 comparison, unresolved word-trace certificate, Hecke-centering Julia, `cdense_transfer`, `sol6`, and unsupported Sp(2g) extrapolation are not active results.
