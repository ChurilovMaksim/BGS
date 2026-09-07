# Claim-ledger addendum — 2026-09-07

This file is the authoritative dated extension of `claim_ledger.md`. For claims dated through 2026-09-06, the base ledger remains authoritative. For the scopes below, this addendum wins over older notes, manuscript wording, exploratory files, and earlier audit prose. `OPEN` still means open; finite execution is never promoted to a uniform theorem.

## A. Unrestricted finite-Fourier resonance nondegeneracy

| Claim | Status | Boundary / authority |
|---|---|---|
| For every hyperbolic `A in SL(2,Z)` and every nonconstant real trigonometric polynomial `g`, the second bracket variance `Gamma_A(g)` is strictly positive | **EXACT + FINITE-REGRESSION** | `mathematics/extremal_resonance_nondegeneracy.md`; equivalent all-lag theorem in `manuscript/unified_sections/temporal_resonance.tex` |
| There is an exposed frequency `k=u+Av` with unique support decomposition, nonzero determinant and no nonzero `A`-iterate in `V+AV` | **EXACT + FINITE-REGRESSION** | support-geometric proof; Python exact quadratic-field witness generator plus independent C++ replay |
| Every fixed real mean-zero Fourier box has a positive coercivity minimum | **EXACT** | finite-dimensional compactness; no uniform lower bound as bandwidth grows |
| Positivity for every nonconstant analytic infinite-support observable | **OPEN** | the finite-support maximum is load-bearing; smooth counterexamples remain valid |

**Audit correction.** On 2026-09-07 a repeated synchronization audit found that Section 4 of the standalone mathematical note incorrectly propagated both eigencoordinate rectangle bounds through one time direction. The theorem statement and exact witness checkers were unchanged. Commit `08a4a5d33d631b81abd6083c55187f1840c87660` replaced that paragraph by the correct two-sided argument: `L(k)>t+2` separately forces forward `xi` escape and backward `eta` escape.

## B. Global Cayley subgroup-curve bound

Let `H<=F_p^*`, `|H|=K>=2`, `p` odd, and `A=c(H\{1})` with `c(h)=(h+1)/(h-1)`. For distinct nonunit ratio parameters the extended collision curve is a geometrically irreducible smooth bidegree `(2,2)` genus-one curve with four boundary points. Corvaja--Zannier's positive-characteristic gcd/curve theorem therefore gives

```text
N(rho,sigma)
 <= max(3*cuberoot(32) K^(2/3), 48 K^2/p),
N(rho,sigma)<=2K.
```

Exact restoration of the two artificial zero points in each ratio fibre and exact diagonal factorization yield

```text
E_+(A)-(K-1)^2
 <= D_K+(K-1)(K-2)(B(K,p)-4),
D_K=2K^2-7K+4+gcd(2,K),
E_+(A) << K^(8/3)+K^4/p.
```

| Claim | Status | Boundary / authority |
|---|---|---|
| Curve geometry, restoration correction and diagonal bookkeeping above | **EXACT + FINITE-REGRESSION** | `mathematics/cayley_curve_uniform.md`; `computations/verification/cayley_curve_uniform.py` |
| Uniform point bound and resulting global energy theorem | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION** | Corvaja--Zannier JEMS 2013 is the external input |
| Same exponent with no odd-order or subgroup-size restriction | **EXACT + EXTERNAL-THEOREM** | strengthens the older project Makarychev--Vyugin route; it does not improve the `8/3` exponent |
| Centered pointwise target `E_+(A)=(K-1)^4/p+O(K^(2+o(1)))` | **OPEN** | the new theorem does not supply family-wide cancellation |

The dated exact certificate covers every subgroup order `K>=3` occurring for odd primes `p<=257`: 338 designs, 114 odd orders, 224 even orders, maximum tested order 256. This finite run audits algebra and implementation only. External priority for this specialized Cayley application is not established.

## C. Rare-phase and Gaussian information limits

| Claim | Status | Boundary / authority |
|---|---|---|
| Rare-phase balance radius `x_n~n/e`, radial Hellinger profile, aperture exponent and certified scalar `2.9086102383180<C_*<2.9086102383183` for the explicit fixed-moment vacuum/high-Fock pair | **EXACT + FINITE-CERTIFICATE** | `mathematics/bosonic_information_limits_20260907.md`; dated rare-phase certificate/review |
| At `n=128`, mean photon number one, exactly 10 unrestricted input copies first reach 75% known-pair success; ordinary heterodyne needs `>3e18`, unit-aperture censored heterodyne `>3e218` | **EXACT + FINITE-CERTIFICATE** | explicit known-pair discrimination problem, not full tomography minimax |
| For every fixed finite-mode phase-insensitive Gaussian product channel with positive gains and at least one strictly noisy mode, inaccessible environment and no pre-channel encoding, moment-class input tomography has minimax expected input trace-distance risk `Theta((log B)^(-beta/2))`, even against collective output POVMs | **EXACT** | randomized product homodyne supplies the upper order; fixed channel parameters |
| Corresponding deterministic inverse modulus is `Theta((log(1/delta))^(-beta/2))` | **EXACT** | fixed nonzero channel noise |
| At 50% pure loss, the explicit `n=128` known pair has optimal collective-output 75% threshold `3e39 < B_75 <= 4e39` | **EXACT + FINITE-CERTIFICATE** | known binary pair |
| Uniform pure-loss two-state approximation `|D-sqrt(1-exp(-4t))| <= 5ut+sqrt(u(43t+8sqrt(t)))`, `t=Bu eta^n`, and the critical penalty `eta^{-n}` | **EXACT + FINITE-REGRESSION** | `mathematics/pure_loss_discrimination.md`; Python and independent C++ scalar audits |
| Matching full moment-class minimax transition when physical channel noise vanishes with `B` | **OPEN** | binary-pair theorem is not a full tomography minimax theorem |

## D. Verification, formalization and publication boundary

- The September 7 rare-phase, Gaussian and pure-loss Python/C++ sources were read back from GitHub and matched the independently rerun local sources at Git-blob level where recorded in `record/session_science_sync_20260907.md`.
- The new global Cayley verifier was independently rerun locally and its Git blob equals the remote blob. The committed certificate records the full 338-design run.
- `formalization/Bgs.lean` imports every active `.lean` module under `formalization/Bgs/`; `formalization/drafts/` is outside the active import graph. The general September 7 analytic theorems are not claimed to be fully Lean-formalized.
- Current GitHub-hosted workflow attempts have failed before executing a step (`steps=[]`); this is not positive or negative scientific execution evidence.
- The locally verified 146-page PDF with SHA-256 `55f759c1d4205d76b6499cbf52e52d2caf0273eac18aa0eaa990cbab94c73edd` contains the late rare-phase/Gaussian/pure-loss sections, but predates restoration of the Corvaja--Zannier Cayley theorem. That restored theorem is currently authoritative in the mathematical/evidence layer, not yet in that verified PDF.

## E. Still open

Microscopic BGS/GOE/COE universality remains **OPEN**. In particular, neither positive classical resonance variance, fourth-moment Cayley energy control, noisy tomography limits, nor finite certificates supply the required Heisenberg-scale desymmetrized joint-trace comparison and high-frequency tail control.