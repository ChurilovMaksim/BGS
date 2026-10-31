import Mathlib.Data.ZMod.Units
import Mathlib.Order.Interval.Finset.Nat
import Mathlib.Data.Finset.Image
import Mathlib.Tactic

/-!
# BGS-TRACE-163: equal fibres of the inverse-residue map on a complete block

This discharges the hypothesis `hfib` of `Bgs.LineB.TraceFormula.avg_eq_avg_units`
and `theorem2_avg_error` (the complete-block form of Theorem 2) for the concrete
inverse-residue map and the concrete complete block — not for an abstract map.

What is proved here, and what is NOT:

* The map (source: `phase1_trace_formula.md` §4–§5, boundary of BGS-TRACE-163):
  `ν(N) = N⁻¹ mod g′`, where `g′ ∣ D`. On `N` coprime to `D` it is the inverse
  of the reduction of `N` from `(ZMod D)ˣ` to `(ZMod g′)ˣ`; off the admissible
  set it takes the junk value `1`, which is never hit on the block below.
* The block: `𝒩 = {N ∈ [X, X + D) : gcd(N, D) = 1}` — one full period of length
  `D`, restricted to the admissible residues. This is exactly the source §5
  argument: "there are φ(D) per block of D consecutive integers", then
  "reduction mod D → (Z/g′)ˣ followed by inversion is a surjective
  homomorphism with equal fibres" — the surjectivity is
  `ZMod.unitsMap_surjective` in Mathlib, the equal fibres are cosets of
  its kernel, made explicit here by translation.
* The theorem: all fibres of `ν` over `𝒩` have the same cardinality.
  Fed into `avg_eq_avg_units`, this gives the exact complete-block average
  identity of Theorem 2.

What is NOT claimed:

* The source's actual window `𝒩_X = {N ∈ (X, 2X] : gcd(N, D) = 1}` does NOT
  have exactly equal fibres: its length `X` is in general not a multiple of
  `D`, so the residue counts differ by at most one per class. That
  discrepancy is precisely the `D / X` error term of the source's Theorem 2,
  which `theorem2_avg_error` explicitly leaves unproved (it is the `hEquidist`
  hypothesis of the 175 module). Nothing here redefines the source's window
  to make it provable: the complete block is a different, explicitly named
  object, and the window version remains open in exactly the 175 sense.
* The instantiation `g′ ∣ D` in the 163 setting (`g′ = gp m`,
  `D = D_m = 2(x_m − 1)` in `Bgs.LineB.Derand`): `gp m = (x_m − 1) / gcd(x_m − 1, y_m)`
  divides `x_m − 1`, which divides `2(x_m − 1)`. That one-line divisibility
  is left to the gluing step, not smuggled in as an extra hypothesis here:
  the theorem below takes `g′ ∣ D` as an explicit hypothesis.

No sorry, no axiom, no native_decide, no decide.
-/

namespace Bgs
namespace LineB
namespace Hfib

open Finset

/-- The inverse-residue map `ν(N) = N⁻¹ mod g′` of the 163 chain
(`phase1_trace_formula.md` §4: `ν = N⁻¹ mod g′_m`). For `N` coprime to `D`
it is the inverse of the reduction of `N` from `(ZMod D)ˣ` to `(ZMod g′)ˣ`;
otherwise it is the junk value `1`. -/
noncomputable def nuMap {g' D : ℕ} (hdiv : g' ∣ D) (N : ℕ) : (ZMod g')ˣ :=
  if h : Nat.Coprime N D then (ZMod.unitsMap hdiv (ZMod.unitOfCoprime N h))⁻¹ else 1

/-- The complete block of admissible `N`: one full period of length `D`,
restricted to `N` coprime to `D` (source §5: `φ(D)` per block of `D`
consecutive integers). -/
def admBlock (X D : ℕ) : Finset ℕ :=
  (Finset.Ico X (X + D)).filter (fun N => Nat.Coprime N D)

lemma mem_admBlock {X D N : ℕ} :
    N ∈ admBlock X D ↔ X ≤ N ∧ N < X + D ∧ Nat.Coprime N D := by
  simp [admBlock, Finset.mem_Ico, and_assoc]

/-- On a full period, the residue mod `D` determines `N`. -/
lemma cast_injective_on_Ico {X D : ℕ} [NeZero D] {N₁ N₂ : ℕ}
    (h₁ : N₁ ∈ Finset.Ico X (X + D)) (h₂ : N₂ ∈ Finset.Ico X (X + D))
    (h : (N₁ : ZMod D) = (N₂ : ZMod D)) : N₁ = N₂ := by
  rw [Finset.mem_Ico] at h₁ h₂
  have hmod : N₁ ≡ N₂ [MOD D] := (ZMod.natCast_eq_natCast_iff N₁ N₂ D).mp h
  obtain ⟨a, ha⟩ : ∃ a, N₁ = X + a := ⟨N₁ - X, by omega⟩
  obtain ⟨b, hb⟩ : ∃ b, N₂ = X + b := ⟨N₂ - X, by omega⟩
  rw [ha, hb] at hmod
  have hab : a ≡ b [MOD D] := Nat.ModEq.add_left_cancel' X hmod
  have hab' : a = b := Nat.ModEq.eq_of_lt_of_lt hab (by omega) (by omega)
  rw [ha, hb, hab']

/-- The residues mod `D` of a full period exhaust `ZMod D`. -/
lemma image_cast_Ico {X D : ℕ} [NeZero D] :
    (Finset.Ico X (X + D)).image (fun N : ℕ => (N : ZMod D)) = Finset.univ := by
  apply Finset.eq_univ_of_card
  rw [Finset.card_image_of_injOn]
  · rw [Nat.card_Ico, Nat.add_sub_cancel_left, ZMod.card]
  · intro N₁ h₁ N₂ h₂ h
    exact cast_injective_on_Ico (Finset.mem_coe.mp h₁) (Finset.mem_coe.mp h₂) h

/-- Every unit mod `D` is hit by a unique admissible `N` in the block. -/
lemma exists_adm_of_unit {X D : ℕ} [NeZero D] (w : (ZMod D)ˣ) :
    ∃ N ∈ admBlock X D, ∀ h : Nat.Coprime N D, ZMod.unitOfCoprime N h = w := by
  have hmem : (w : ZMod D) ∈ (Finset.Ico X (X + D)).image (fun N : ℕ => (N : ZMod D)) := by
    rw [image_cast_Ico]
    exact Finset.mem_univ _
  obtain ⟨N, hNIco, hNcast⟩ := Finset.mem_image.mp hmem
  have hcop : Nat.Coprime N D := by
    have hunit : IsUnit (N : ZMod D) := by
      rw [hNcast]
      exact w.isUnit
    exact (ZMod.isUnit_iff_coprime N D).mp hunit
  refine ⟨N, ?_, fun h => ?_⟩
  · rw [mem_admBlock]
    exact ⟨(Finset.mem_Ico.mp hNIco).1, (Finset.mem_Ico.mp hNIco).2, hcop⟩
  · apply Units.ext
    rw [ZMod.coe_unitOfCoprime]
    exact hNcast

/-- On admissible `N`, `ν` is the inverse of the reduction, by definition. -/
lemma nuMap_of_coprime {g' D : ℕ} (hdiv : g' ∣ D) {N : ℕ} (h : Nat.Coprime N D) :
    nuMap hdiv N = (ZMod.unitsMap hdiv (ZMod.unitOfCoprime N h))⁻¹ := by
  simp only [nuMap, dif_pos h]

/-- The `ν`-fibres over the block are the unit-fibres over `(ZMod D)ˣ`,
transported along the bijection `N ↦ unitOfCoprime N`. -/
lemma card_filter_nuMap_eq {g' D X : ℕ} [NeZero D] [NeZero g'] (hdiv : g' ∣ D)
    (u : (ZMod g')ˣ) :
    ((admBlock X D).filter (fun N => nuMap hdiv N = u)).card
      = (Finset.univ.filter
          (fun w : (ZMod D)ˣ => (ZMod.unitsMap hdiv w)⁻¹ = u)).card := by
  refine Finset.card_bij
    (fun N hN => ZMod.unitOfCoprime N (mem_admBlock.mp (Finset.mem_filter.mp hN).1).2.2)
    ?_ ?_ ?_
  · intro N hN
    have hcop : Nat.Coprime N D :=
      (mem_admBlock.mp (Finset.mem_filter.mp hN).1).2.2
    rw [Finset.mem_filter]
    refine ⟨Finset.mem_univ _, ?_⟩
    rw [← nuMap_of_coprime hdiv hcop]
    exact (Finset.mem_filter.mp hN).2
  · intro N₁ h₁ N₂ h₂ h
    have hcop₁ : Nat.Coprime N₁ D :=
      (mem_admBlock.mp (Finset.mem_filter.mp h₁).1).2.2
    have hcop₂ : Nat.Coprime N₂ D :=
      (mem_admBlock.mp (Finset.mem_filter.mp h₂).1).2.2
    have hcast : (N₁ : ZMod D) = (N₂ : ZMod D) := by
      have := congr_arg (fun w : (ZMod D)ˣ => (w : ZMod D)) h
      rwa [ZMod.coe_unitOfCoprime, ZMod.coe_unitOfCoprime] at this
    exact cast_injective_on_Ico
      (Finset.mem_Ico.mpr ⟨(mem_admBlock.mp (Finset.mem_filter.mp h₁).1).1,
        (mem_admBlock.mp (Finset.mem_filter.mp h₁).1).2.1⟩)
      (Finset.mem_Ico.mpr ⟨(mem_admBlock.mp (Finset.mem_filter.mp h₂).1).1,
        (mem_admBlock.mp (Finset.mem_filter.mp h₂).1).2.1⟩)
      hcast
  · intro w hw
    have hw' : (ZMod.unitsMap hdiv w)⁻¹ = u := (Finset.mem_filter.mp hw).2
    obtain ⟨N, hNadm, hNw⟩ := exists_adm_of_unit (X := X) (D := D) w
    have hcop : Nat.Coprime N D := (mem_admBlock.mp hNadm).2.2
    refine ⟨N, Finset.mem_filter.mpr ⟨hNadm, ?_⟩, hNw hcop⟩
    rw [nuMap_of_coprime hdiv hcop, hNw hcop]
    exact hw'

/-- The unit-fibres of the reduction map are all equal: they are translates
of each other by an element mapping to the required ratio (surjectivity is
`ZMod.unitsMap_surjective`). -/
lemma card_filter_units_inv_eq {g' D : ℕ} [NeZero D] [NeZero g'] (hdiv : g' ∣ D)
    (u₁ u₂ : (ZMod g')ˣ) :
    (Finset.univ.filter (fun w : (ZMod D)ˣ => (ZMod.unitsMap hdiv w)⁻¹ = u₁)).card
      = (Finset.univ.filter
          (fun w : (ZMod D)ˣ => (ZMod.unitsMap hdiv w)⁻¹ = u₂)).card := by
  obtain ⟨w₀, hw₀⟩ := ZMod.unitsMap_surjective (m := D) (n := g') hdiv (u₁ * u₂⁻¹)
  refine Finset.card_bij (fun w _ => w * w₀) ?_ ?_ ?_
  · intro w hw
    have hw1 : (ZMod.unitsMap hdiv w)⁻¹ = u₁ := (Finset.mem_filter.mp hw).2
    have hfw : ZMod.unitsMap hdiv w = u₁⁻¹ := by rw [← hw1, inv_inv]
    rw [Finset.mem_filter]
    refine ⟨Finset.mem_univ _, ?_⟩
    calc (ZMod.unitsMap hdiv (w * w₀))⁻¹
        = ((ZMod.unitsMap hdiv w) * (ZMod.unitsMap hdiv w₀))⁻¹ := by rw [map_mul]
      _ = (u₁⁻¹ * (u₁ * u₂⁻¹))⁻¹ := by rw [hfw, hw₀]
      _ = u₂ := by rw [inv_mul_cancel_left, inv_inv]
  · intro w₁ _ w₂ _ h
    exact mul_right_cancel h
  · intro w hw
    have hw2 : (ZMod.unitsMap hdiv w)⁻¹ = u₂ := (Finset.mem_filter.mp hw).2
    have hfw : ZMod.unitsMap hdiv w = u₂⁻¹ := by rw [← hw2, inv_inv]
    refine ⟨w * w₀⁻¹, Finset.mem_filter.mpr ⟨Finset.mem_univ _, ?_⟩, ?_⟩
    · calc (ZMod.unitsMap hdiv (w * w₀⁻¹))⁻¹
          = ((ZMod.unitsMap hdiv w) * (ZMod.unitsMap hdiv w₀)⁻¹)⁻¹ := by
            rw [map_mul, map_inv]
        _ = (u₂⁻¹ * (u₁ * u₂⁻¹)⁻¹)⁻¹ := by rw [hfw, hw₀]
        _ = (u₂⁻¹ * (u₂ * u₁⁻¹))⁻¹ := by group
        _ = u₁ := by rw [inv_mul_cancel_left, inv_inv]
    · exact by group

/-- The complete block is nonempty: it contains the element `≡ 1 mod D`. -/
lemma admBlock_nonempty {X D : ℕ} [NeZero D] : (admBlock X D).Nonempty := by
  have hmem : (1 : ZMod D) ∈ (Finset.Ico X (X + D)).image (fun N : ℕ => (N : ZMod D)) := by
    rw [image_cast_Ico]
    exact Finset.mem_univ _
  obtain ⟨N, hNIco, hNcast⟩ := Finset.mem_image.mp hmem
  have hcop : Nat.Coprime N D := by
    have hunit : IsUnit (N : ZMod D) := by
      rw [hNcast]
      exact isUnit_one
    exact (ZMod.isUnit_iff_coprime N D).mp hunit
  exact ⟨N, mem_admBlock.mpr ⟨(Finset.mem_Ico.mp hNIco).1, (Finset.mem_Ico.mp hNIco).2,
    hcop⟩⟩

/-- Equal fibres of the inverse-residue map on a complete block: this is
exactly the hypothesis `hfib` of `Bgs.LineB.TraceFormula.avg_eq_avg_units`
and `theorem2_avg_error`, instantiated at `𝒩 := admBlock X D`,
`νmap := nuMap hdiv`. -/
theorem hfib_of_complete_block {g' D X : ℕ} [NeZero D] [NeZero g'] (hdiv : g' ∣ D) :
    ∀ u₁ u₂ : (ZMod g')ˣ,
      ((admBlock X D).filter (fun N => nuMap hdiv N = u₁)).card
        = ((admBlock X D).filter (fun N => nuMap hdiv N = u₂)).card := by
  intro u₁ u₂
  rw [card_filter_nuMap_eq hdiv u₁, card_filter_nuMap_eq hdiv u₂,
    card_filter_units_inv_eq hdiv u₁ u₂]

/- Axiom audit for all main theorems of this module. -/
#print axioms Bgs.LineB.Hfib.cast_injective_on_Ico
#print axioms Bgs.LineB.Hfib.image_cast_Ico
#print axioms Bgs.LineB.Hfib.exists_adm_of_unit
#print axioms Bgs.LineB.Hfib.nuMap_of_coprime
#print axioms Bgs.LineB.Hfib.admBlock_nonempty
#print axioms Bgs.LineB.Hfib.card_filter_nuMap_eq
#print axioms Bgs.LineB.Hfib.card_filter_units_inv_eq
#print axioms Bgs.LineB.Hfib.hfib_of_complete_block

end Hfib
end LineB
end Bgs
