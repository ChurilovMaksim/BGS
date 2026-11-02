# Wave 22, task 2: cancellation deficit Δ(36)

Extends wave-20 task 3 (Δ = 0 at m = 16, 20; 5.27×10⁻¹³ at m = 24) to
m = 36, the open case named there. Same methodology: only global
fibers containing an on-support split component fiber can contribute
(Γ-invariance sketch for S_q); rigid construction + rigidity sweep +
generic sampling + full-φ̂ validation. Repository untouched; no Lean
build. New difficulty: D₃₆ ≈ 3.6×10²⁷ > 2⁶³, so global CRT values
are Python object ints (int64 only mod q); and the first run died by
OOM (full P matrix at q = 32041 is 8.2 GB) — fixed by per-pair dot
products, and by replacing the S2 filter (see below).

## Factorisation and component census (all exact)

D₃₆ = 3629521257408972904004611200 = 2⁷·3⁶·5²·7²·11²·73²·179²·197²·199²,
prime powers [25, 49, 121, 128, 729, 5329, 32041, 38809, 39601],
|supp| = D/16 = 226845078588060806500288200. Every component is
enumerable (max 39601 points). Split component fibers occur ONLY at
q = 729, both FULLY supported; no partial fibers anywhere; zero is
supported at every component except q = 128; supported 128-fibers are
[1, 13, 21, 28, 37] with sizes [2, 2, 1, 2, 1].

| q | fibers | split | supp pts |
|---|---|---|---|
| 25, 49, 121, 5329, 32041, 38809, 39601 | 5–2300 | 0 | all points |
| 128 | 39 | 0 | 8 (5 fibers) |
| 729 | 17 | 2 (see below) | 729 (all) |

## The two 729 split fibers (S₇₂₉, correction mode verified at all 9 q)

|S₇₂₉| = 27 = √729 on every orbit of both fibers (so the phase-only
deficit formula is exact); S₁₂₈ has |S| = 32√2 on all supported
128-fibers (common factor).

- Fiber 14: 324 points, 9 orbits of 36. Orbit phases form an
  arithmetic progression with step 2π/9 (to printed precision), so
  the coherent sum vanishes: every rigid fiber built on it FULLY
  cancels.
- Fiber 15: 36 points, 3 orbits of 12, all three at phase π/3 —
  identical phases, so every rigid fiber built on it has deficit 0.
  (Contrast m = 12/24, where the 81-split fiber's 3 orbits sat 120°
  apart and fully cancelled; at m = 36 the small split fiber is
  phase-aligned and harmless, and the cancelling fiber is the new
  9-orbit one.)

## Rigid fibers and Δ(36)

10 rigid global fibers (5 supported 128-fibers × 2 splits), each the
full product of its component contents (one global fiber per pair):

| f729 | n128 = 2 (3 fibers) | n128 = 1 (2 fibers) |
|---|---|---|
| 14 | size 648, 9 orbits of 72, deficit 419904 = 648² | size 324, 9 orbits of 36, deficit 104976 = 324² |
| 15 | size 72, 3 orbits of 24, deficit 0 | size 36, 3 orbits of 12, deficit 0 |

ΣΔ_F = 3·419904 + 2·104976 = 1,469,664, hence exactly

  **Δ(36) = 1469664 / 226845078588060806500288200
         = 36 / 5556659773370096181175 ≈ 6.4787×10⁻²¹.**

## Completeness checks

- Rigidity sweep: sorted-multiset filter mod two primes (P₁ =
  1000000007, P₂ = 998244353) over all 115975 nonzero other-component
  points × 5 supported 128-fibers × 2 splits: **0 survivors**, so no
  extra rigid family with one nonzero other component. (Method note:
  the S2 filter used at m = 24 is vacuous here — 795240/1159680
  triples passed — because class-sum preservation forces
  Σ tᵢ(a₀ᵢ − a₁ᵢ) = 0 for most kernel points t; the multiset filter
  is the sound necessary condition and it passes nobody.)
- Generic sampling: 20 random global fibers seeded from a split
  729-fiber are all single Γ-orbits (size 72) spanning exactly one
  729-orbit, deficit 0 — as at m = 24, generic fibers do not split.
- Cross-check: (v₀, v₁) enumeration of a rigid fiber reproduces
  size 648 exactly.
- Full φ̂ at a rigid point (per-point S_q at all 9 components):
  |φ̂|² = 16/D with relative error 3.1×10⁻¹⁵ — modulus dichotomy
  and all correction modes validated at m = 36.

## The Δ sequence and the limit

| m | ΣΔ_F | Δ(m) |
|---|---|---|
| 12 | 18144 | 1.889×10⁻⁴ |
| 24 | 77760 | 5.268×10⁻¹³ |
| 36 | 1469664 | 6.479×10⁻²¹ |

Collapse factor 24 → 36 is ≈ 8.1×10⁷. Mechanism as at m = 24: the
numerator grows only ~19× per 12 steps (supported 2-fiber count ×
split-fiber size squared) while |supp| = D/16 grows ~1.5×10⁹×. This
is consistent with Δ → 0, hence with the corrected limit reading
R → Bsym_fiber — but it is NOT a proof. Open, as before:
(i) the Γ-invariance of S_q is a sketch; (ii) joint-nonzero
other-component rigid families are excluded only by the
CRT-injectivity sketch argument, not by the sweep; (iii) no control
at larger m (next test: m = 48, where the 2-component is 512 and the
3-component 3⁸ = 6561 — CORRECTION (wave 23): the components at m = 48 are 2¹¹ = 2048 and 3⁴ = 81, by v₂(D_m) = 2v₂(m)+3 and the 3-adic LTE v₃(D_m) = 2v₃(m)+2 for 4|m); (iv) the exact 2π/9 phase progression and the
phase alignment of fiber 15 are numerical observations, not theorems.

## Files

- `wave22_m36_deficit.py`, `wave22_m36_deficit.log`,
  `wave22_m36_deficit.json` (10 rigid fibers with orbits/phases),
  `wave22_comp_analysis.py`, `wave22_comp_analysis.json`,
  `wave22_Xrow36.npy` (adjugate first row; X·H = D·I verified exactly,
  avoiding the 181 s sympy adjugate).
