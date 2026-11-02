/-! BREAKTHROUGH DRAFT — research record, not a theorem.
    Source: BGS breakthrough program (Nov 2026), wave notes in evidence/breakthrough/methods/.
    Status: built in test-copy project: 8706 jobs, 0 errors, 5 sorry (diagonal model only, not the full propagator).
    Not imported by formalization/Bgs.lean. Registry status unchanged. -/

import Mathlib

/-! ### Probe stubs (NOT main's definitions)

The test copy has no Derand/NAverage/Bridge/Units/Tsum/Expand modules, so the
names the draft uses are stubbed here with the signatures the draft needs.
All proofs in the body are `sorry` regardless; this probe checks statement
well-formedness only. -/

namespace Bgs.LineB.Derand

noncomputable def Dm (m : ℕ) : ℤ := 0

def gp (m : ℕ) : ℕ := 0

end Bgs.LineB.Derand

namespace Bgs.LineB.NAverage

noncomputable def window (X : ℝ) (D : ℕ) : Finset ℕ := ∅

noncomputable def winAvg (W : Finset ℕ) (f : ℕ → ℝ) : ℝ := 0

end Bgs.LineB.NAverage

namespace Bgs.LineB.NAverageBridge

noncomputable def Btup (m : ℕ) (ĝ : ℤ → ℂ) : ZMod (Bgs.LineB.Derand.gp m) → ℝ :=
  fun _ => 0

noncomputable def Ztup (m : ℕ) (ĝ : ℤ → ℂ) : ZMod (Bgs.LineB.Derand.gp m) → ℂ :=
  fun _ => 0

end Bgs.LineB.NAverageBridge

namespace Bgs.LineB.NAverageUnits

noncomputable def nuAvgUnits {g : ℕ} (f : ZMod g → ℝ) : ℝ := 0

end Bgs.LineB.NAverageUnits

namespace Bgs.LineB.Tsum

noncomputable def kickMatInf (N : ℕ) (ĝ : ℤ → ℂ) : Matrix (ZMod N) (ZMod N) ℂ := 0

end Bgs.LineB.Tsum

namespace Bgs.LineB.Expand

noncomputable def catMat (N : ℕ) (a : ZMod N) : Matrix (ZMod N) (ZMod N) ℂ := 0

end Bgs.LineB.Expand

namespace Bgs.LineB.TraceFormula

end Bgs.LineB.TraceFormula

namespace Bgs.LineB.NAverageM1

end Bgs.LineB.NAverageM1

/-!
# Claim 175 as a diagonal-model theorem — Lean draft (statements only, all proofs `sorry`)

This file is a WORKSPACE DRAFT, not part of main. It restates
`methods/wave21_175_diagonal_restatement.md` as Lean statements that
instantiate main's bridge theorem `nAverageTup_units` (conditional on
`hEquidistUnits`) with the diagonal-model trace. Nothing here is proved:
every proof is `by sorry`, and the analytic inputs (G3, G4b) are
hypotheses, not Lean theorems.

## Sources, all via the GitHub connector at HEAD
## `4b86d7f306473837127b0ee67769aac0c15343e3` (PR #79), verified 2026-11-01

- Bridge `formalization/Bgs/LineBNAverageBridge.lean`, blob `3373aa6b…`:
  `Bgs.LineB.NAverageBridge`, `phaseTup`, `Ztup`, `Btup`,
  `pointwiseTup`, `traceHenceTup`, `nAverageTup` (target `NAverage.nuAvg`).
- Units `formalization/Bgs/LineBNAverageUnits.lean`, blob `ae0e303d…`:
  `Bgs.LineB.NAverageUnits`, `nuAvgUnits`, `nuAvgUnits_one`,
  `nAverageM1_units`, `nAverageTup_units` (target `nuAvgUnits`).
- Derand `formalization/Bgs/LineBDerand.lean`, blob `01fa6e63…`:
  `Bgs.LineB.Derand`, flat import `Bgs.LineBDerand` (the dotted name is
  the namespace inside the file, not the import path),
  `Dm (m : Nat) : Int := 2 * (pellX m - 1)`, `gp (m : Nat) : Nat`,
  `yp (m : Nat) : Nat`, `pellQ pellP : Nat → Int`.
- NAverage `formalization/Bgs/LineBNAverage.lean`, blob `8b2ce39c…`:
  `Bgs.LineB.NAverage`, `window X D = (Ioc ⌊X⌋₊ ⌊2X⌋₊).filter (Coprime · D)`,
  `winAvg W f = (∑ N ∈ W, f N) / W.card`.
- Tsum `formalization/Bgs/LineBTsum.lean`, blob `dc17b0dc…`:
  `Bgs.LineB.Tsum`, `kickValInf N ĝ x = ∑' k, ĝ k * chi N (k * x)`,
  `kickMatInf N ĝ = Matrix.diagonal (kickValInf N ĝ)`.
- Expand `formalization/Bgs/LineBExpand.lean`:
  `Bgs.LineB.Expand`, `catMat N a = N^{-1/2} · χ_N(a·(3x²−2xy+3y²))`.

## Why a restatement is needed (from the note)

The bridge's `hTrU` mentions no actual kick: it only says an abstract
trace function `TrU` agrees on the window with the tsum trace
`((kickMatInf N ĝ * catMat N (a N)) ^ m).trace`. And
"kickMatInf = the actual kick" is FALSE as an equality with the full
fixed propagator (non-diagonal, `l = ±1` rows, `τN ≈ 10⁻⁷⁸` versus the
diagonal model at `η = O(1)`). So the honest 175 is a theorem about the
diagonal model kick below. Transfer to TRACE-005 is open (G4c).

## Explicitly NOT claimed by any statement in this file

1. Nothing about the full propagator, about `exp (iτN • A_N)` versus
   `D_{η,N}`, or about any relation between `τN` and `η = O(1)`.
2. No TRACE-005, no spectrum, no CUE/Sine₂ conclusion.
3. No exact constant as a theorem: the bound below keeps the bridge's
   first error term as stated (the `≈2π` discrepancy is a separate
   `henceTup` issue).
4. No discrete-grid coefficients: the statement uses continuum `ĝ_η`;
   substituting N-grid coefficients needs aliasing bookkeeping.
5. No uniformity in `η` beyond the per-`η` bound (`s0, s2` depend on `η`).
6. No claim about `s`-dependence or the limit `X → ∞` beyond the
   stated `1 / X` bound at fixed `X`.

## Status of each ingredient

- `traceHenceTup`, `nAverageTup_units` (conditional), `Ztup_norm_le`,
  window lemmas: proved in main (Lean).
- G4b (`kickValInf = exp (iηf_diag)`, `catMat = MN`, duality
  `Ztup = Z_all`, norm class): proved analytically (waves 11–12),
  NOT in Lean — it enters below as hypothesis `hDiag`.
- G3 S-bound and the `hEquidistUnits` assembly from it: proved
  analytically (waves 5–6), NOT in Lean — `hEquidistUnits` stays a
  hypothesis, exactly as in `nAverageTup_units`. Analytic values at
  `m = 3/4/5/6`: `S ≤ 784/9216/26896/627200`, valid for all real `η`.
- This restatement as a Lean theorem: NOT formalised; it is an
  instantiation, not a new proof.
-/

open Bgs.LineB
open Bgs.LineB.TraceFormula Bgs.LineB.Derand Bgs.LineB.Tsum Bgs.LineB.Expand
open Bgs.LineB.NAverageBridge Bgs.LineB.NAverage Bgs.LineB.NAverageM1
open Bgs.LineB.NAverageUnits

namespace Bgs.LineB.Diagonal175

/-! ### §1. The diagonal model: `ℓ¹`/`ℓ²` sums, the diagonal kick, the trace. -/

/-- The `ℓ¹` sum of the continuum coefficients: `s0 = ∑' ‖ĝ k‖`. -/
noncomputable def s0 (ĝ : ℤ → ℂ) : ℝ := ∑' k : ℤ, ‖ĝ k‖

/-- The weighted `ℓ²` sum: `s2 = ∑' k²‖ĝ k‖`. -/
noncomputable def s2 (ĝ : ℤ → ℂ) : ℝ := ∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖

/-- The bridge's first-error constant: `C' = π·m·s2·s0^(m−1)`. -/
noncomputable def C' (m : ℕ) (ĝ : ℤ → ℂ) : ℝ :=
  Real.pi * (m : ℝ) * s2 ĝ * s0 ĝ ^ (m - 1)

/-- The diagonal kick at level `N`: `D_{η,N} = diagonal (exp (iη·f_diag (x/N)))`.
    This is the G4b identification of `kickMatInf N ĝ_η` (analytic, not Lean);
    see hypothesis `hDiag` in the theorems below. -/
noncomputable def diagKick (η : ℝ) (f_diag : ℝ → ℝ) (N : ℕ) :
    Matrix (ZMod N) (ZMod N) ℂ :=
  Matrix.diagonal (fun x : ZMod N =>
    Complex.exp (Complex.I * (η : ℂ) * (f_diag ((x.val : ℝ) / (N : ℝ)) : ℂ)))

/-- The diagonal-model trace: `TrU_diag N = ((D_{η,N} * catMat N (a N)) ^ m).trace`.
    In main's language this is exactly the tsum trace, so the bridge's `hTrU`
    holds for it BY DEFINITION (see `TrU_diag_hTrU`); it is not an extra
    hypothesis of the diagonal restatement.
    FIX (wave 31, task 5): the wave-30 probe failed here because `Matrix.mul`
    over `ZMod N` needs `Fintype (ZMod N)`, available only under `[NeZero N]`,
    and the use sites in `diagonal_175`/`diagonal_175_m1` apply `TrU_diag` to
    bare window elements with no instance in scope (their lambdas are plain
    `ℕ → ℝ`, so no membership proof is available to conjure one). Threading
    `[NeZero N]` through the def would therefore force statement changes.
    Instead the def case-splits: `N = 0` gives `0` by convention, and for
    `N ≠ 0` the instance is supplied from the negation, so the trace is the
    product trace exactly where it is used. All theorem statements below are
    byte-identical to the draft. -/
noncomputable def TrU_diag (m : ℕ) (ĝ : ℤ → ℂ) (a : ∀ N : ℕ, ZMod N) (N : ℕ) : ℂ :=
  if h : N = 0 then 0
  else
    haveI : NeZero N := ⟨h⟩
    ((Tsum.kickMatInf N ĝ * catMat N (a N)) ^ m).trace

/-- `hTrU` for the diagonal-model trace, by definition of `TrU_diag`.
    (Proof: `rfl` after unfolding; left as `sorry` per the draft convention.) -/
theorem TrU_diag_hTrU (m : ℕ) (ĝ : ℤ → ℂ) (a : ∀ N : ℕ, ZMod N) (X : ℝ) :
    ∀ N ∈ NAverage.window X (Dm m).toNat, ∀ [NeZero N],
      TrU_diag m ĝ a N = ((Tsum.kickMatInf N ĝ * catMat N (a N)) ^ m).trace := by
  sorry

/-! ### §2. The main theorem: 175-diagonal for `m ≥ 2`.

This is `nAverageTup_units` with `TrU := TrU_diag`, plus the parameters
`η, f_diag` and the G4b identification `hDiag` that make it a statement
about the diagonal model. The window is `(X, 2X]` with `gcd (N, Dm) = 1`
(`NAverage.window X (Dm m).toNat`, via `Nat.Coprime`).
The `(D : ℝ)` cast in the bound is main's own spelling in
`nAverageTup_units` (`D` is already `ℝ` there). -/

theorem diagonal_175 (m : ℕ) [NeZero m] [NeZero (gp m)]
    (η : ℝ) (f_diag : ℝ → ℝ) (ĝ : ℤ → ℂ)
    (a : ∀ N : ℕ, ZMod N) (X : ℝ) (D Deff : ℝ)
    (hm : 2 ≤ m) (hX1 : 1 < X)
    (hs2 : Summable fun k : ℤ => (k : ℝ) ^ 2 * ‖ĝ k‖)
    (ha : ∀ N ∈ NAverage.window X (Dm m).toNat, 2 * (a N) * (-4) = 1)
    (hDiag : ∀ N : ℕ, ∀ [NeZero N], Tsum.kickMatInf N ĝ = diagKick η f_diag N)
    (hW : (NAverage.window X (Dm m).toNat).Nonempty)
    (hC'le : Real.pi * (m : ℝ) * s2 ĝ * s0 ĝ ^ (m - 1) ≤ X)
    (hEquidistUnits : ∀ ν : ℕ → ZMod (gp m),
      (∀ N ∈ NAverage.window X (Dm m).toNat, (ν N) * (N : ZMod (gp m)) = 1) →
      |NAverage.winAvg (NAverage.window X (Dm m).toNat) (fun N => Btup m ĝ (ν N))
        - nuAvgUnits (Btup m ĝ)|
        ≤ (D : ℝ) * min (s0 ĝ ^ (2 * m)) Deff / X) :
    |NAverage.winAvg (NAverage.window X (Dm m).toNat)
        (fun N => ‖TrU_diag m ĝ a N‖ ^ 2) - nuAvgUnits (Btup m ĝ)|
      ≤ ((2 * s0 ĝ ^ m + 1)
          * (Real.pi * (m : ℝ) * s2 ĝ * s0 ĝ ^ (m - 1))) / X
        + (D : ℝ) * min (s0 ĝ ^ (2 * m)) Deff / X := by
  sorry

/-! ### §3. The `m = 1` case, separately.

Mirrors `nAverageM1_units` (with `TrU := TrU_diag 1`) and
`winAvg_units_one` (window mean of `Btup` equals the units mean, gap `0`).
Here `gp 1 = 2` and the units of `ZMod 2` are `{1}`, so
`nuAvgUnits (Btup 1 ĝ) = Btup 1 ĝ 1` (`nuAvgUnits_one` in main). -/

theorem diagonal_175_m1 (η : ℝ) (f_diag : ℝ → ℝ) (ĝ : ℤ → ℂ)
    (a : ∀ N : ℕ, ZMod N) (X : ℝ)
    (hX1 : 1 < X)
    (hs2 : Summable fun k : ℤ => (k : ℝ) ^ 2 * ‖ĝ k‖)
    (ha : ∀ N ∈ NAverage.window X (Dm 1).toNat, 2 * (a N) * (-4) = 1)
    (hDiag : ∀ N : ℕ, ∀ [NeZero N], Tsum.kickMatInf N ĝ = diagKick η f_diag N)
    (hW : (NAverage.window X (Dm 1).toNat).Nonempty)
    (hC'le : Real.pi * s2 ĝ ≤ X) :
    |NAverage.winAvg (NAverage.window X (Dm 1).toNat)
        (fun N => ‖TrU_diag 1 ĝ a N‖ ^ 2)
      - nuAvgUnits (Btup 1 ĝ)|
      ≤ ((2 * s0 ĝ + 1) * (Real.pi * s2 ĝ)) / X := by
  sorry

/-- At `m = 1` the window mean of the profile equals the units mean
    (gap `0`); only the first error term survives. Mirrors main's
    `winAvg_units_one` (used inside `nAverageM1_units`). -/
theorem diagonal_175_m1_units_mean (ĝ : ℤ → ℂ) (ν : ℕ → ZMod (gp 1)) (X : ℝ)
    (hν : ∀ N ∈ NAverage.window X (Dm 1).toNat,
      (ν N) * (N : ZMod (gp 1)) = 1)
    (hW : (NAverage.window X (Dm 1).toNat).Nonempty) :
    NAverage.winAvg (NAverage.window X (Dm 1).toNat) (fun N => Btup 1 ĝ (ν N))
      = nuAvgUnits (Btup 1 ĝ) := by
  sorry

/-- G4b at `m = 1` (analytic, not Lean): the profile values are the full
    sums `Z_all(0) = ∑' ĝ_η` and `Z_all(1) = ∑' (−1)^k ĝ_η(k)`, via the
    duality `Ztup = Z_all`. Stated for `Ztup` at `ν = 0, 1 : ZMod (gp 1)`. -/
theorem diagonal_175_m1_Z_values (ĝ : ℤ → ℂ) :
    Ztup 1 ĝ 0 = ∑' k : ℤ, ĝ k ∧
    Ztup 1 ĝ 1 = ∑' k : ℤ, (-1 : ℂ) ^ k * ĝ k := by
  sorry

/-! ### §4. What would close transfer to TRACE-005 (G4c, open).

An estimate comparing `exp (iτN • A_N)` with `D_{η,N}` (including the
`l = ±1` rows) plus a regime relation between `τN` and `η`, neither of
which exists in main. Until G4c is done, 175-as-proved is exactly the
theorem of §2 (and §3 at `m = 1`), and any citation of 175 for the full
fixed map over-claims by exactly that step. No statement in this file
mentions the full propagator as an object of a claim. -/

end Bgs.LineB.Diagonal175
