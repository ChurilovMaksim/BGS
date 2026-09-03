# Claim ledger

Status vocabulary:

- **EXACT** — an exact statement with a current derivation and/or independent current regression.
- **FINITE-CERTIFICATE** — a finite design statement checked by Lean or an exact program; not a uniform theorem.
- **NUMERICAL** — finite numerical evidence only.
- **DRAFT** — a mathematically assembled route with load-bearing obligations still open.
- **HISTORICAL-UNREVIEWED** — scientifically relevant old claim retained, but not re-certified in the present rebuild.
- **RETRACTED** — not available for use as a theorem input.

## Current load-bearing results

| Claim | Status | Current evidence |
|---|---|---|
| Off-diagonal pair-key map is bijective with `d(u,v)=(u-1)(v-1)/(v-u)`; diagonal has weight `N-2` | **EXACT** | `mathematics/fourth_moment_reduction.md`, Python/C++ regressions |
| `k=2` constrained off-diagonal mass is `(K-1)(K-2)` | **EXACT** | derivation + finite Lean `K2Reduction` |
| Exact `k=4` total `sum_t B(t)=(K^2+1)N^2-(6K^2+3K)N+13K^2-3K` | **EXACT** | derivation + Python/C++ finite anchors |
| Character collapse `sum |J|^4=m^2 Sigma4` | **EXACT finite-field identity** | current derivation; finite scalar/twist regressions |
| Fourier duality `Var_{q!=0} Sigma4 = N Var_{t!=0} B(t)` | **EXACT** | finite Fourier orthogonality |
| Decomposition `B=O+2(N-2)C_H+(N-2)^2 1_0` | **EXACT** | current pair-key derivation |
| Cayley identity and additive-energy interpretation of `C_H` | **EXACT** | current derivation/regression |
| Odd-prime-`K` characteristic-zero Cayley collision classification | **COMPUTER-ASSISTED EXACT** | 720 matching systems; current exact verifier |
| `E_11={23,67,89}`, `E_13={53,79,131,157,313}` | **FINITE-CERTIFICATE** | exact resultant audit |
| `(N,K)=(461,23)` has Cayley energy `1190`, not forced baseline `902` | **FINITE-CERTIFICATE** | independent Python regression + Lean |
| Pair-key anchors `(23,11),(53,13),(199,11),(461,23)` | **FINITE-CERTIFICATE** | independent Python/C++ implementations |
| Twisted-Jacobi scalar implementation checks at selected designs | **FINITE-CERTIFICATE** | stored current certificate |
| Twisted-Jacobi moment reproduction against preserved R82 q-curves | **FINITE-CERTIFICATE** | stored current certificate |
| Generic off/off organization by an elliptic pencil | **DRAFT / structural** | symbolic algebra and current notes |
| Restricted M1 `K=o(N^(1/4))` variance estimate | **DRAFT** | requires publication-grade algebraic family certificate and source-exact sheaf-correlation hypotheses |
| Microscopic BGS/GOE local eigenphase law | **OPEN** | no valid bridge from current moment concentration to a local law |

## Formal finite certificates

| Lean source | Exact scope |
|---|---|
| `TorusLevelSets.lean` | finite level-set/orbit facts at the audited design `N=199`; not the general analytic theorem |
| `ScaleLaw.lean` | finite scale-law certificate at the audited `N=199` design |
| `K2Reduction.lean` | finite `k=2` counting/bijection certificate at its design |
| `K4Variety.lean` | finite `k=4` variety/key multiplicity certificate at its design |
| `CayleyExceptionalK23.lean` | finite exceptional Cayley energy at `(461,23)` |
| `M1DegenerateFiber.lean` | finite certificate for the historical degenerate Möbius fiber; diagnostic only, not a proof of current M1 |
| `OpLocal.lean` | specification/open formalization with admitted (`sorry`) obligations; **not** a theorem certificate |

## Earlier rank-1 foundations recovered from the research record

The old workspace contains theorem labels A--II (symmetry class, trace identities,
moment/shape decompositions, torus level sets and twisted Jacobi formulas). They
must not all be silently erased, but the present rebuild does not re-certify
every old analytic proof. Their current disposition is:

- finite torus-level-set and scale-law parts: **FINITE-CERTIFICATE** via Lean;
- twisted-Jacobi formula at selected designs: **FINITE-CERTIFICATE** via current
  independent implementation checks;
- historical symmetry claims (`Theta^2=+1`, parity/Hecke antiunitary structure):
  **HISTORICAL-UNREVIEWED** in this pass, retained in the broad corpus;
- historical Catalan/shape-moment statements through finite orders:
  **HISTORICAL-UNREVIEWED / NUMERICAL** unless a specific current certificate is cited;
- old full-group arcsine formulas: **HISTORICAL-UNREVIEWED** pending a fresh
  line-by-line audit of the exact statement and hypotheses.

This conservative downgrade is deliberate: preservation is not promotion.

## Rank-2 / Sp4 line

The broad corpus contains exact-looking diagonal/coset identities and numerical
flatness experiments. They are retained because they may be useful, but they
are **HISTORICAL-UNREVIEWED** in the present M1-focused re-audit. In particular,
old extrapolation from the diagonal/coset calculations to a general `Sp(2g)`
theorem is not active.

## Spectral evidence

Parity-reduced spacing and number-variance computations at stored designs are
**NUMERICAL** evidence. A historical `N=95419` test that compared a gap-ratio
statistic to the ordinary spacing CDF is quarantined and must not be cited as a
valid KS spacing test.
