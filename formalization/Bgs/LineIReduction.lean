import Mathlib

/-!
# BGS-TRACE-213 (exact identity) and BGS-TRACE-317 (level bookkeeping floors)

Source: registry statements of `BGS-TRACE-213`, `BGS-TRACE-317` and the frozen definition of `BGS-TRACE-206`:
`F_m = φ⁻¹ ∑_{ν unit} |Z_ν|²`, `Res_m = φ⁻¹ ∑_ρ [(|Z_ρ|² − RMT_m) + ∑_{d incl.} n_d (|Z_ρ|²/d² − RMT_m)]`,
`W′_m = F_m − RMT_m − Res_m`, `RMT_m = 4m − m²/h`, `Z_ρ = Z_{ν_ρ}`, `n_d = |M_d(ρ)|`, `φ = φ(2h)` the number of units.
Abstract finite model: `U` the units (`φ = |U|`), `X ν = |Z_ν|² ≥ 0`, for each `ρ ∈ Pst` a unit `ν_ρ`, a set `Ds ρ` of
included levels and member sets `Mem ρ d ⊆ U`; `S` the resonant units (all `ν_ρ` and all members).

* `reduction` (BGS-TRACE-213, exact identity) : if the sets `{ν_ρ}` and `M_d(ρ)` are pairwise disjoint and lie in `U`, then
  `W′_m = φ⁻¹ ∑_{ν ∈ U∖S} (|Z_ν|² − RMT_m) + φ⁻¹ ∑_{ρ, d incl.} Dev_d(ρ)`,
  `Dev_d(ρ) = ∑_{ν ∈ M_d(ρ)} (|Z_ν|² − |Z_ρ|²/d²)`;
* `rmt_le` : `RMT_m ≤ 4m`; `NR_ge` (BGS-TRACE-317) : the non-resonant part is `≥ −RMT_m` when `RMT_m ≥ 0`;
  `Dev_ge` : `Dev_d(ρ) ≥ −n_d |Z_ρ|²/d²` (each member term is `≥ −|Z_ρ|²/d²`).

**Partial coverage:** the pairwise disjointness of `{ν_ρ}` and the `M_d(ρ)` (part of BGS-TRACE-213) is a **hypothesis**
here, not derived from the congruence definition; the sufficiency statement (E″), (T″), (D) ⇒ R′ (an `o(m)` argument) is not
formalized; for BGS-TRACE-317 the level floor is formalized only in the form `−n_d|Z_ρ|²/d²` (the form `−(h_p/d)S_ρ` with
its constants, and the inclusion threshold `m₀ = 15` — see `Bgs.LineMInclusion` — are not).  All proofs are kernel-checked.
-/

namespace Bgs.LineIReduction

open Finset

variable {R : Type*} [DecidableEq R]

/-- The resonant units `S = ⋃_ρ ({ν_ρ} ∪ ⋃_d M_d(ρ))`. -/
def resonant (Pst : Finset R) (νr : R → ℕ) (Ds : R → Finset ℕ) (Mem : R → ℕ → Finset ℕ) : Finset ℕ :=
  Pst.biUnion (fun ρ => insert (νr ρ) ((Ds ρ).biUnion (Mem ρ)))

noncomputable def Res (φ RMT : ℝ) (X : ℕ → ℝ) (Pst : Finset R) (νr : R → ℕ) (Ds : R → Finset ℕ)
    (Mem : R → ℕ → Finset ℕ) : ℝ :=
  φ⁻¹ * ∑ ρ ∈ Pst, ((X (νr ρ) - RMT) + ∑ d ∈ Ds ρ, ((Mem ρ d).card : ℝ) * (X (νr ρ) / (d : ℝ) ^ 2 - RMT))

noncomputable def Dev (X : ℕ → ℝ) (νr : R → ℕ) (Mem : R → ℕ → Finset ℕ) (ρ : R) (d : ℕ) : ℝ :=
  ∑ ν ∈ Mem ρ d, (X ν - X (νr ρ) / (d : ℝ) ^ 2)

omit [DecidableEq R] in
theorem reduction (U : Finset ℕ) (hU : U.Nonempty) (RMT : ℝ) (X : ℕ → ℝ) (Pst : Finset R) (νr : R → ℕ)
    (Ds : R → Finset ℕ) (Mem : R → ℕ → Finset ℕ)
    (h1 : (Pst : Set R).PairwiseDisjoint (fun ρ => insert (νr ρ) ((Ds ρ).biUnion (Mem ρ))))
    (h2 : ∀ ρ ∈ Pst, νr ρ ∉ (Ds ρ).biUnion (Mem ρ))
    (h3 : ∀ ρ ∈ Pst, ((Ds ρ : Set ℕ)).PairwiseDisjoint (Mem ρ))
    (hS : resonant Pst νr Ds Mem ⊆ U) :
    ((U.card : ℝ)⁻¹ * ∑ ν ∈ U, X ν) - RMT - Res (U.card : ℝ) RMT X Pst νr Ds Mem
      = (U.card : ℝ)⁻¹ * ∑ ν ∈ U \ resonant Pst νr Ds Mem, (X ν - RMT)
        + (U.card : ℝ)⁻¹ * ∑ ρ ∈ Pst, ∑ d ∈ Ds ρ, Dev X νr Mem ρ d := by
  have hφ : (U.card : ℝ) ≠ 0 := by
    have : 0 < U.card := hU.card_pos
    exact_mod_cast this.ne'
  have hsplit : ∑ ν ∈ U, (X ν - RMT)
      = ∑ ν ∈ U \ resonant Pst νr Ds Mem, (X ν - RMT) + ∑ ν ∈ resonant Pst νr Ds Mem, (X ν - RMT) := by
    rw [sum_sdiff hS]
  have hres : ∑ ν ∈ resonant Pst νr Ds Mem, (X ν - RMT)
      = ∑ ρ ∈ Pst, ((X (νr ρ) - RMT) + ∑ d ∈ Ds ρ, ∑ ν ∈ Mem ρ d, (X ν - RMT)) := by
    unfold resonant
    rw [sum_biUnion h1]
    refine sum_congr rfl (fun ρ hρ => ?_)
    rw [sum_insert (h2 ρ hρ), sum_biUnion (h3 ρ hρ)]
  have hdev : ∀ ρ d, ∑ ν ∈ Mem ρ d, (X ν - RMT) - ((Mem ρ d).card : ℝ) * (X (νr ρ) / (d : ℝ) ^ 2 - RMT)
      = Dev X νr Mem ρ d := by
    intro ρ d
    unfold Dev
    rw [sum_sub_distrib, sum_sub_distrib, sum_const, sum_const, nsmul_eq_mul, nsmul_eq_mul]
    ring
  have hF : ((U.card : ℝ)⁻¹ * ∑ ν ∈ U, X ν) - RMT = (U.card : ℝ)⁻¹ * ∑ ν ∈ U, (X ν - RMT) := by
    rw [sum_sub_distrib, sum_const, nsmul_eq_mul]
    field_simp
  have key : ∑ ρ ∈ Pst, ∑ d ∈ Ds ρ, Dev X νr Mem ρ d
      = ∑ ρ ∈ Pst, ((X (νr ρ) - RMT) + ∑ d ∈ Ds ρ, ∑ ν ∈ Mem ρ d, (X ν - RMT))
        - ∑ ρ ∈ Pst, ((X (νr ρ) - RMT) + ∑ d ∈ Ds ρ, ((Mem ρ d).card : ℝ) * (X (νr ρ) / (d : ℝ) ^ 2 - RMT)) := by
    rw [← sum_sub_distrib]
    refine sum_congr rfl (fun ρ _ => ?_)
    rw [← sum_congr rfl (fun d (_ : d ∈ Ds ρ) => hdev ρ d), sum_sub_distrib]
    ring
  rw [hF, hsplit, hres, key]
  unfold Res
  ring

theorem rmt_le (m h : ℝ) (hh : 0 < h) : 4 * m - m ^ 2 / h ≤ 4 * m := by
  have : 0 ≤ m ^ 2 / h := div_nonneg (sq_nonneg m) hh.le
  linarith

/-- **Non-resonant floor:** `φ⁻¹ ∑_{ν∈N} (|Z_ν|² − RMT) ≥ −RMT` for `N ⊆ U`, `RMT ≥ 0`. -/
theorem NR_ge (U N : Finset ℕ) (hU : U.Nonempty) (hN : N ⊆ U) (RMT : ℝ) (hR : 0 ≤ RMT) (X : ℕ → ℝ)
    (hX : ∀ ν, 0 ≤ X ν) :
    -RMT ≤ ((U.card : ℝ))⁻¹ * ∑ ν ∈ N, (X ν - RMT) := by
  have hc : (0 : ℝ) < U.card := by exact_mod_cast hU.card_pos
  have hle : (N.card : ℝ) ≤ U.card := by exact_mod_cast card_le_card hN
  have h1 : -(N.card : ℝ) * RMT ≤ ∑ ν ∈ N, (X ν - RMT) := by
    rw [sum_sub_distrib, sum_const, nsmul_eq_mul]
    have := sum_nonneg (fun ν (_ : ν ∈ N) => hX ν)
    linarith
  rw [le_inv_mul_iff₀ hc]
  nlinarith

omit [DecidableEq R] in
/-- **Level floor:** `Dev_d(ρ) ≥ −n_d |Z_ρ|²/d²`. -/
theorem Dev_ge (X : ℕ → ℝ) (hX : ∀ ν, 0 ≤ X ν) (νr : R → ℕ) (Mem : R → ℕ → Finset ℕ) (ρ : R) (d : ℕ) :
    -(((Mem ρ d).card : ℝ) * (X (νr ρ) / (d : ℝ) ^ 2)) ≤ Dev X νr Mem ρ d := by
  unfold Dev
  rw [sum_sub_distrib, sum_const, nsmul_eq_mul]
  have := sum_nonneg (fun ν (_ : ν ∈ Mem ρ d) => hX ν)
  linarith

end Bgs.LineIReduction
