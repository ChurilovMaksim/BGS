# Wave 7, task 3 — does ω distinguish w-classes? Verdict: NO

## Verdict

**ω does not distinguish w-classes, in principle — not just numerically.**
Route (a) for P_w (let the ω-decay step kill pairs with different w) is
dead. P_w can enter 152 only via route (b) (restate 152 with
(fiber, w)-classes and recomputed Bsym) or route (c) (the O′ route),
neither of which is attempted here.

## The actual ω formula (from main, pinned HEAD, via connector only)

HEAD `d87dce0d9277579568edfee6cffecbc96ea61024`, repo `ChurilovMaksim/BGS`.
All files below were fetched with `sha` = that HEAD (search-index refs
pointed at a newer commit, so fetches were explicitly pinned).

- `mathematics/fixed-map/band_limited_kick_bridge.md`, blob
  `f8efd17768d749a408a669f870174da7cc4627c2`, D3:
  `Ψ_m(s/D) = Σ_{ξ,ξ'} φ̂_s(ξ) conj φ̂_s(ξ') ∏_k ω_k(η(S_k(ξ) − S_k(ξ')))`,
  `S_k(ξ) = Σ_j e(kξ_j)`,
  `ω = J0(a|z|)` (uniform θ, Kluyver average, TRACE-133)
  or `exp(−a²|z|²/4)` (G ensemble).
- `formalization/Bgs/LineDStrongKick.lean`, blob
  `7fab89a797411d89a1c8a4b5d009af16b3237a55`, `pairTerm`:
  `φ s ξ * star (φ s ξ') * ∏ k, ω k (η * (S ξ k − S ξ' k))`.
- `formalization/Bgs/LineDStrongKickBridge.lean`, blob
  `209ea983c4b0cf81374d1fc4ae40e7ab3b3f284f`,
  `strong_kick_limit_phihatFix`: hypotheses `hω0 : ω k 0 = 1`,
  `hωbound : ‖ω k z‖ ≤ 1`, `hωlim : ω k (η·Δ) → 0` for `Δ ≠ 0`.
- `formalization/Bgs/LineDStrongKickConc.lean`, blob
  `9d5a178c1c076cd8c41b02b23a5385201c0321d3`, `gaussOmega`:
  `gaussOmega a k z = exp(−(a k * z)²/4)`, with `gaussOmega_zero`,
  `gaussOmega_bound`, `gaussOmega_lim` (needs `a k ≠ 0`, `Δ ≠ 0`).
  (Caveat: the file header still says "TEST COPY ONLY — not pushed",
  but the file IS in main at this HEAD and IS imported by
  `formalization/Bgs.lean` — 120 imports at this HEAD, including
  StrongKick, StrongKickBridge, StrongKickConc. The header is stale.)
- Source D4 (same bridge doc): "every pair with P_𝒦(ξ) ≠ P_𝒦(ξ') has
  weight → 0 and every pair with equal P_𝒦 has weight 1".
- Source D5(a): for 𝒦 ⊇ {1..m}, P_𝒦 gives the power sums of
  {e(ξ_j)}, hence (Newton) the multiset.

## Why ω is blind within a fiber (argument, not just numerics)

1. `S_k(ξ) = Σ_j e(kξ_j)` is a symmetric sum over coordinates, hence
   a function of the multiset {ξ_j} alone. (The real/imaginary
   doubled-mode values in `modeSumK`/`doubledMode` are Re/Im parts of
   the same sums, so they are multiset-determined too.)
2. A fiber is by definition a set of vectors with the same sorted
   multiset. So for ξ, ξ′ in one fiber, `S_k(ξ) = S_k(ξ')` for every k,
   hence `Δ_k = 0` for every k.
3. Therefore the ω-factor of the pair is `∏_k ω_k(0) = 1` at every η,
   for both forms: Gaussian `exp(0) = 1`, J0 `J0(0) = 1`.
4. `w_y = (H_m y)/D_m` is NOT a function of the multiset (wave 6:
   sorted(w) differs inside bad fibers), so ω sees a strictly coarser
   invariant than w. No choice of 𝒦 helps: shrinking 𝒦 can only
   merge more pairs, never split a fiber.

So ω distinguishes P_𝒦-classes (equivalently, at full 𝒦, fibers), and
nothing finer. The separation hypothesis `hSep` in the bridge is
needed precisely because ω cannot do this job.

## Numerical test (script: wave7_omega_w_test.py)

Mode sums computed independently per vector as
`S_k(y) = Σ_j exp(2πi·k·y_j/D)`, k = 1..m; ω-factor = Gaussian product
with a = 1. J0 factor is 1 analytically at Δ = 0 (J0(0) = 1); J0 is not
formalized in main (Conc header: Mathlib has no Bessel J0), so the J0
half of the claim rests on the source formula, not on a Lean theorem.

| case | sorted(y) equal | sorted(w) equal | max \|ΔS_k\| | ω-factor at η = 0, 1, 5, 20, 100 |
|---|---|---|---|---|
| m=8, first bad fiber (M08 example: fiber 32 = 16+16) | yes | NO: (−1,0,1,2,2,2,3,5) vs (−1,−1,0,2,2,3,4,5) | 8.9e-16 (float rounding) | 1.000000000000 at all η |
| m=12 counterexample pair (wave-4 lift; w cross-checked against sep_m12_pair_result.json) | yes | NO: (0,0,0,0,1,1,3,3,4,4,4,4) vs (0,0,1,1,2,2,2,2,3,3,4,4) | 9.0e-16 (float rounding) | 1.000000000000 at all η |
| control: m=8, y vs y+55488 (different fiber) | no | — | Δ₂=1.79, Δ₄=6.0, Δ₈=3.46 | 2.8e-06 (η=1), 9.6e-140 (η=5), 0 (η=20) |

The control confirms the test is not vacuous: across fibers ω does
decay; within a fiber it is exactly 1 even though sorted(w) differs.

## What this does not show

- It does not kill P_w as a separator: sorted(w) still separates at
  m=8 and on the m=12 pair (wave 6). It kills only route (a).
- It does not touch route (b) (restate 152 by (fiber, w)-classes,
  Bsym recomputed) or route (c) (O′ on the support).
- It does not prove anything about J0 decay at large η (D6: J0 c₁
  grows numerically; the J0 half here uses only ω(0) = 1).
- Repository untouched; Lean not built; numerics are a check of the
  argument above, not the argument itself.
