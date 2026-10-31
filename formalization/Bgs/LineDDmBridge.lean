/- Bridge: the two `Dm` definitions coincide.

  `Bgs.LineD.Defs.Dm m = (Hmat m ℤ).det` (the determinant side, used by
  the 151-full chain) equals `Bgs.LineB.Derand.Dm m = 2 * (pellX m - 1)`
  (the Pell side, used by the 163 chain: TraceFormula / Gauss / Expand).

  Proof: `det_formula` gives `(Dm : ℂ) = lamC ^ m + muC ^ m - 2`, and
  `lam_add_lamInv_pow` (with `lamC`, `muC` identified with the real
  `lam`, `lamInv` under the `ℝ → ℂ` coercion) gives
  `lamC ^ m + muC ^ m = 2 * pellX m`. Note: `TraceFormula` opens
  `Bgs.LineB.Derand`, so its `pellX` IS `Derand.pellX` — there are not
  two Pell sequences to identify.

  No `sorry`, no `axiom`, no `native_decide` anywhere in this file.
-/

import Bgs.LineBTraceFormula
import Bgs.LineDOrbitPairFull

/-- The complex root `lamC` is the coercion of the real root `lam`. -/
theorem lamC_eq_ofReal :
    Bgs.LineD.OrbitPairFull.lamC
      = ((Bgs.LineB.TraceFormula.lam : ℝ) : ℂ) := by
  simp only [Bgs.LineD.OrbitPairFull.lamC, Bgs.LineB.TraceFormula.lam]
  push_cast
  ring

/-- The complex root `muC` is the coercion of the real root `lamInv`. -/
theorem muC_eq_ofReal :
    Bgs.LineD.OrbitPairFull.muC
      = ((Bgs.LineB.TraceFormula.lamInv : ℝ) : ℂ) := by
  simp only [Bgs.LineD.OrbitPairFull.muC, Bgs.LineB.TraceFormula.lamInv]
  push_cast
  ring

/-- The Pell power identity in `ℂ`: `lamC ^ m + muC ^ m = 2 * pellX m`. -/
theorem lamC_pow_add_muC_pow (m : ℕ) :
    Bgs.LineD.OrbitPairFull.lamC ^ m + Bgs.LineD.OrbitPairFull.muC ^ m
      = 2 * (Bgs.LineB.Derand.pellX m : ℂ) := by
  have h := Bgs.LineB.TraceFormula.lam_add_lamInv_pow m
  have hC := congrArg Complex.ofReal h
  push_cast at hC
  rw [lamC_eq_ofReal, muC_eq_ofReal]
  exact hC

/-- The determinant `Dm` equals the Pell `Dm`, as complex numbers. -/
theorem dm_eq_derand_dm_complex (m : ℕ) [NeZero m] :
    ((Bgs.LineD.Defs.Dm m : ℤ) : ℂ)
      = ((Bgs.LineB.Derand.Dm m : ℤ) : ℂ) := by
  rw [Bgs.LineD.OrbitPairFull.det_formula, lamC_pow_add_muC_pow]
  simp only [Bgs.LineB.Derand.Dm]
  push_cast
  ring

/-- The determinant `Dm` equals the Pell `Dm`, as integers. -/
theorem dm_eq_derand_dm (m : ℕ) [NeZero m] :
    Bgs.LineD.Defs.Dm m = Bgs.LineB.Derand.Dm m := by
  have h := dm_eq_derand_dm_complex m
  exact_mod_cast h

/- Axiom audit for the bridge theorems. -/
#print axioms lamC_eq_ofReal
#print axioms muC_eq_ofReal
#print axioms lamC_pow_add_muC_pow
#print axioms dm_eq_derand_dm_complex
#print axioms dm_eq_derand_dm
