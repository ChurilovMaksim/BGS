# Claim status map — 2026-09-03

This map is a compact index for the full research corpus.  It does not replace proofs; root `STATUS.md` is authoritative when a historical file disagrees.

| Claim / route | Current status | What survives |
|---|---|---|
| R82 twisted-Jacobi baseline | **REPRODUCED** | q-curve/fourth-moment baseline at `N=199,3571` |
| Exact H3 `k=2` reduction | **REPRODUCED / finite exact** | `|P|=(K-1)(K-2)` and checked energy identity at audited designs |
| Theorem-II matrix-element formula, computational regression | **REPRODUCED** | direct scalar-sum agreement at `N=461,19489` |
| GOE nearest-neighbour spacing | **NUMERICAL EVIDENCE** | `N=3571` freshly reproduced; `N=19489` retained prior result |
| Matched GOE number variance | **NUMERICAL EVIDENCE / fresh rerun** | all audited `L` values within `|z|<2` at `N=19489` |
| Historical `N=95419` spacing test | **QUARANTINED** | raw gap-ratio measurements only; KS comparison used wrong reference statistic |
| Historical Möbius-fiber M1 theorem | **INVALID / OPEN GAP** | exact parametrisations and finite fiber-sum measurements remain useful |
| R86/R87 trace-fluctuation lemma | **INVALID AS STATED** | named H3 target and experiments remain research ideas; Step 1 noncommutative binomial error blocks the reduction |
| Cycle-2 additive Sub-Weyl toy | **EXPLORATORY NUMERICAL** | additive toy behaviour only; no multiplicative H3 theorem |
| Cycle-3 trace fluctuation run | **EXPLORATORY NUMERICAL** | finite-design measurements only |
| Word-trace proof engine | **INCOMPLETE / QUARANTINED** | partial trace identities and recurrence data; rewrite closure unresolved |
| H3 `k=4` factorisation JSON | **FINITE-DESIGN EXACT + NUMERICAL** | exact checked factorisation where stated; asymptotic fluctuation remains unproved |
| Even-k H3 template | **FINITE-DESIGN ONLY** | checked at the explicitly recorded `k=6,N=23` point; no general theorem |
| Sigma4 second moment | **FINITE-DESIGN EXACT** | exact at the stated `N=53` calibration; scaling open |
| Rank-2 diagonal identity | **FINITE-DESIGN EXACT** | exact stored identity/calibration |
| Rank-2 coset flatness / sector / period-4 | **FINITE-DESIGN EXACT** | exact `N=53` calibration identities |
| Rank-2 G0 / edge mass / trace fluctuation | **EXPERIMENTAL / NUMERICAL** | useful mechanism probes; no uniform higher-genus theorem |
| General BGS | **NOT PROVED** | desired downstream target only |

## Formal status

`formal/Bgs/OpLocal.lean` deliberately contains admitted `sorry` obligations and an `opaque spectralBound`; it specifies an open target rather than proving it.  Finite certificates in the other Lean files must be interpreted at their stated parameters.  No fresh Lean build is claimed by the 2026-09-03 audit because Lean/Lake was unavailable in the audit runtime.
