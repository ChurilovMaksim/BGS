# Claim-ledger addendum — 2026-09-07

This file is the authoritative dated extension of `claim_ledger.md`. For claims dated through 2026-09-06, the base ledger remains authoritative. For the scopes below, this addendum wins over older notes, manuscript wording, exploratory files, and earlier audit prose. `OPEN` still means open; finite execution is never promoted to a uniform theorem.

## A. Finite-Fourier, generic infinite-support and analytic resonance structure

| Claim | Status | Boundary / authority |
|---|---|---|
| For every hyperbolic `A in SL(2,Z)` and every nonconstant real trigonometric polynomial `g`, the second bracket variance `Gamma_A(g)` is strictly positive | **EXACT + FINITE-REGRESSION** | `mathematics/extremal_resonance_nondegeneracy.md`; equivalent all-lag theorem in `manuscript/unified_sections/temporal_resonance.tex` |
| There is an exposed frequency `k=u+Av` with unique support decomposition, nonzero determinant and no nonzero `A`-iterate in `V+AV` | **EXACT + FINITE-REGRESSION** | support-geometric proof; Python exact quadratic-field witness generator plus independent C++ replay |
| Every fixed real mean-zero Fourier box has a positive coercivity minimum | **EXACT** | finite-dimensional compactness; no uniform lower bound as bandwidth grows |
| If `g=p+r` and `E=M_0(p)M_A(r)+M_0(r)M_A(p)+M_0(r)M_A(r)<D=|det(u,Av)||phat(u)phat(v)|`, then `Gamma_A(g)>=2 pi^2(D-E)^2` | **EXACT + FINITE-REGRESSION** | `mathematics/resonance_wiener_stability.md`; exact integer regression in `computations/verification/resonance_wiener_stability.py` |
| In the natural first-moment weighted-Wiener Banach space, `{Gamma_A>0}` is open and dense and `{Gamma_A=0}` is closed nowhere dense | **EXACT** | `mathematics/generic_wiener_resonance.md`; continuity of the orbit-sum map plus density of finite truncations |
| The same open-dense statement holds in every fixed analytic Wiener strip | **EXACT** | continuous embedding into weighted Wiener space; finite polynomials dense |
| The same open-dense statement holds in `H^s(T^2;R)` for every `s>2` and in `C^infinity(T^2;R)` | **EXACT** | Cauchy--Schwarz gives continuous `H^s -> X_A` embedding for `s>2`; smooth conclusion follows through any such Sobolev norm |
| A real-analytic `g` satisfying `{g,C_A g}=0` identically must be constant | **EXACT** | `mathematics/analytic_bracket_rigidity.md`; level-line equivariance, recurrence and projective hyperbolicity |
| An analytic zero-mean `h` with zero sum on every oriented frequency orbit has an analytic transfer `h=u-C_Au`; in an adapted exponential norm the exponent loses at most a factor two | **EXACT** | `mathematics/analytic_coboundary_regularization.md`; direct bilateral Fourier-tail construction |
| Therefore any nonconstant real-analytic `g` with `Gamma_A(g)=0` must satisfy `{g,C_Ag}/(4*pi)=u-C_Au` with a **nonzero** bracket and real-analytic transfer `u` | **EXACT reduction** | combines the preceding two analytic theorems |
| Positivity for **every** nonconstant analytic infinite-support observable | **OPEN** | reduced to exclusion or construction of the nontrivial analytic nonlinear coboundary equation above |

**Audit correction.** On 2026-09-07 a repeated synchronization audit found that Section 4 of the standalone finite-Fourier mathematical note incorrectly propagated both eigencoordinate rectangle bounds through one time direction. The theorem statement and exact witness checkers were unchanged. Commit `08a4a5d33d631b81abd6083c55187f1840c87660` replaced that paragraph by the correct two-sided argument: `L(k)>t+2` separately forces forward `xi` escape and backward `eta` escape.

## B. Global Cayley subgroup-curve and dense Fourier bounds

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

A complementary complete-field Fourier argument uses the annihilator-character expansion of `1_H`. If `m=(p-1)/K`, `n=K-1`, then for every nonzero additive frequency

```text
|Ahat(q)| <= 2*((m-1)*sqrt(p)+1)/m <= 2sqrt(p),
```

where the nontrivial-character input is the classical mixed Weil/Deligne bound for `chi((z+1)/(z-1)) e_p(qz)`. Parseval then gives

```text
0 <= E_+(A)-n^4/p
   <= 4*((m-1)*sqrt(p)+1)^2/(m^2*p) * n(p-n)
   <= 4n(p-n).
```

Consequently

```text
E_+(A)-(K-1)^4/p
 << min(pK, K^(8/3)+K^4/p).
```

| Claim | Status | Boundary / authority |
|---|---|---|
| Curve geometry, restoration correction and diagonal bookkeeping above | **EXACT + FINITE-REGRESSION** | `mathematics/cayley_curve_uniform.md`; `computations/verification/cayley_curve_uniform.py` |
| Uniform curve point bound and resulting global energy theorem | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION** | Corvaja--Zannier JEMS 2013 is the external input |
| Same curve exponent with no odd-order or subgroup-size restriction | **EXACT + EXTERNAL-THEOREM** | strengthens the older project Makarychev--Vyugin route; it does not improve the `8/3` exponent |
| Annihilator-character decomposition, Parseval reduction, exact centered inequality above | **EXACT + FINITE-REGRESSION** | `mathematics/cayley_fourier_hybrid.md`; Python and independent C++20 exact implementations |
| Pointwise Fourier bound `|Ahat(q)|<=2*((m-1)sqrt(p)+1)/m` | **EXACT + EXTERNAL-WEIL** | project-internal character algebra plus classical mixed Weil/Deligne estimate `|T_chi(q)|<=2sqrt(p)` |
| Hybrid centered error `<< min(pK,K^(8/3)+K^4/p)` | **EXACT + EXTERNAL-THEOREMS** | combines the preceding Fourier and genus-one bounds |
| Strict exponent improvement over `K^(8/3)` when `K=p^(alpha+o(1))`, `alpha>3/5` | **EXACT consequence** | Fourier branch is `K^(1+1/alpha+o(1))`; this is dense-regime only |
| Centered pointwise target `E_+(A)=(K-1)^4/p+O(K^(2+o(1)))` uniformly in the sparse/intermediate arithmetic regime | **OPEN** | neither the genus-one worst-curve theorem nor complete mixed-Weil cancellation closes this range |

The global-curve dated exact certificate covers every subgroup order `K>=3` occurring for odd primes `p<=257`: 338 designs, 114 odd orders, 224 even orders, maximum tested order 256. The dense-Fourier certificate covers every subgroup design for odd primes through `p<=509`: 807 designs, 364 strict dense-side cases `K^5>p^3`, maximum order 508. Both finite runs audit algebra and implementation only. External priority for these specialized Cayley applications is not established.

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
- The global Cayley curve verifier was independently rerun locally: 338 exact designs through odd primes `p<=257`, including even subgroup orders, with status PASS.
- The dense Cayley Fourier verifier was read back from `main` and rerun through `p<=509`: Python and independently compiled C++20 both returned PASS on 807 designs, including 364 strict dense-side cases. This audit detected stale source hashes in the first dated certificate; commit `6770d9a1101c2a209c94f7a63b0347c753181b96` refreshed the provenance without changing theorem values.
- The weighted-Wiener stability regression was freshly executed against the current exact temporal witness implementation: eight hyperbolic matrices, support radii one through three, and sixteen admitted integer tail multipliers all passed the exact lower-bound assertions.
- The analytic bracket-rigidity and analytic coboundary-regularity manuscript section was compiled independently through two pdfTeX passes, then preflighted and visually inspected; no LaTeX warning or overfull box remains in the standalone build.
- `formalization/Bgs.lean` imports every active `.lean` module under `formalization/Bgs/`; `formalization/drafts/` is outside the active import graph. The general September 7 analytic theorems are not claimed to be fully Lean-formalized.
- A fresh local Lean build was attempted: the repository pins `leanprover/lean4:v4.33.1`, but this container has no Lean toolchain and its restricted network could not fetch the roughly 570 MB official release archive. GitHub-hosted workflow attempts continue to terminate with `steps=[]`; neither condition is scientific execution evidence.
- The 146-page base PDF with SHA-256 `55f759c1d4205d76b6499cbf52e52d2caf0273eac18aa0eaa990cbab94c73edd` remains byte-stable. The canonical TeX source now includes the restored global Cayley theorem, the dense Fourier complement, weighted-Wiener stability, Sobolev/smooth/analytic-strip genericity, and the analytic-rigidity/coboundary reduction. Locally rendered addendum pages have been preflighted and visually checked; a full fresh canonical-source rebuild remains blocked by the unavailable complete private checkout in this container.

## E. Still open

Microscopic BGS/GOE/COE universality remains **OPEN**. In particular, neither positive classical resonance variance, generic Sobolev/analytic-strip nondegeneracy, analytic pointwise rigidity, improved dense-regime Cayley fourth-moment control, noisy tomography limits, nor finite certificates supply the required Heisenberg-scale desymmetrized joint-trace comparison and high-frequency tail control.
