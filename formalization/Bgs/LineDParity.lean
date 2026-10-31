/-
  BGS Line D: the parity argument for `B_m^sym < 2m` (BGS-TRACE-154),
  as a combinatorial skeleton over an abstract finite group action.
  TEST COPY ONLY — not pushed to the repository, registry untouched,
  `Bgs.lean` aggregator unchanged (this module is built by a direct
  `lake env lean` call, not imported by the aggregator).

  Sources, all on current main HEAD 347f1730… (PR #56), via the
  GitHub connector (`record/claims.json`):
  - 154 boundary (verbatim in essence): "For odd m, D_eff = a_m^2 with
    a_m odd, so the Gamma-invariant support has odd size; the reversal
    involution has a fixed point xi_0 with |Gamma xi_0| <= m, hence
    2m - B_m^sym >= m/D_eff > 0. Same argument whenever 2m does not
    divide D_eff (e.g. m = 6)."
  - 152 boundary (for the definition of `B_m^sym`): "B_m^sym =
    D_eff^{-1} sum_supp |Gamma xi|".
  - 151 boundary (for what the support is): the sum is over
    xi, xi' in Fix_m, with weights phihat and omega; |phihat_s|^2 in
    {0, |V[4]|/D_m}; the support is independent of s; D_eff =
    49, 72, 1681, 4900, 57121 (m = 3..7).

  What is built here, and what is NOT (honest scope):
  - Built: the exact combinatorial argument of 154, with the support
    abstracted as a finite type `α` (its size plays the role of
    `D_eff`), the group `Γ` abstracted as any finite group `G` of
    order `2m`, and the reversal abstracted as an element `ρ : G`
    with `ρ * ρ = 1`, `ρ ≠ 1`. The fixed point is DERIVED (odd
    support + involution), the bound `|Γ ξ₀| ≤ m` is DERIVED
    (orbit–stabilizer: `ρ` lies in the stabilizer, so the stabilizer
    has at least 2 elements), and the average bound is DERIVED
    (one orbit of size `≤ m`, all others `≤ 2m`).
  - NOT built (this is 151-full infrastructure, not 154): the
    concrete set `Fix_m`, the weights `phihat`/`omega`, the
    identification of `Γ` with the dihedral group acting on `Fix_m`,
    and the exact values of `D_eff` at `m ≤ 9` (numerical control
    in the registry, not part of the proof). Boundary 151 does not
    define `Γ`'s generators explicitly, so no such definition is
    invented here: `G` and `ρ` are parameters, and the theorem
    states precisely what follows from the boundary's own inputs.
  - The `2m ∤ D_eff` variant (e.g. `m = 6`) is proved as
    `sym_bound_of_not_dvd`: non-divisibility forces an orbit of
    size `< 2m`, hence `≤ m` (orbit sizes divide `2m`), and the
    same averaging applies.

  No `sorry`, no `admit`, no `axiom`, no `native_decide`, no
  `decide` in this file. `#print axioms` for the two main theorems
  is at the end.
-/

import Mathlib.GroupTheory.GroupAction.Quotient
import Mathlib.GroupTheory.Perm.Cycle.Type
import Mathlib.Data.Rat.Cast.Order
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Tactic.Linarith

namespace Bgs
namespace LineD
namespace Parity

open Finset

variable {G α : Type*} [Group G] [MulAction G α] [Fintype G] [Fintype α] [DecidableEq α]

/-- Every `Γ`-orbit is finite, since the support type is finite. -/
noncomputable instance orbitFintype (G : Type*) {α : Type*} [Group G] [MulAction G α]
    [Fintype G] [Fintype α] (x : α) : Fintype ↥(MulAction.orbit G x) :=
  (Set.finite_range _).fintype

/-- The `Γ`-orbit of `x`, as a `Finset`. Filter form, so that sums
    over it split directly. This is the `|Γ ξ|` carrier: the orbit
    itself, before taking its size. -/
noncomputable def orbitFinset (G : Type*) {α : Type*} [Group G] [MulAction G α] [Fintype α]
    (x : α) : Finset α :=
  @Finset.filter α (fun y => y ∈ MulAction.orbit G x) (Classical.decPred _) Finset.univ

/-- Size of the `Γ`-orbit of `x`: the `|Γ ξ|` of the registry. -/
noncomputable abbrev orbitSize (G : Type*) {α : Type*} [Group G] [MulAction G α] [Fintype α]
    (x : α) : ℕ :=
  (orbitFinset G x).card

/-- The symmetric band average `B_m^sym = D_eff⁻¹ ∑ |Γ ξ|` of
    152/154, as a rational number. `Fintype.card α` plays the role
    of `D_eff` (the size of the `Γ`-invariant support). -/
noncomputable def Bsym (G : Type*) (α : Type*) [Group G] [MulAction G α] [Fintype α] : ℚ :=
  (∑ x : α, ((orbitFinset G x).card : ℚ)) / (Fintype.card α : ℚ)

/-- The orbit `Finset` has the orbit's cardinality. -/
lemma orbitFinset_card (x : α) :
    (orbitFinset G x).card = Fintype.card ↥(MulAction.orbit G x) := by
  have h := Fintype.card_ofFinset (p := MulAction.orbit G x) (orbitFinset G x)
    (fun y => by simp [orbitFinset])
  have hinst : (Fintype.ofFinset (orbitFinset G x) (fun y => by simp [orbitFinset]) :
      Fintype ↥(MulAction.orbit G x)) = orbitFintype G x := Subsingleton.elim _ _
  rw [hinst] at h
  exact h.symm

/-- Every orbit is nonempty (it contains its own point). -/
lemma orbitSize_pos (x : α) : 0 < orbitSize G x := by
  apply Finset.card_pos.mpr
  refine ⟨x, ?_⟩
  have hx : x ∈ MulAction.orbit G x := by simpa using MulAction.mem_orbit x (1 : G)
  simpa [orbitFinset] using hx

/-- Every orbit has size at most `|G|` (orbit–stabilizer: the
    stabilizer has at least one element). -/
lemma orbitSize_le_card (m : ℕ) (x : α) (hG : Fintype.card G = 2 * m) :
    orbitSize G x ≤ 2 * m := by
  have hstab : 0 < Fintype.card ↥(MulAction.stabilizer G x) :=
    Fintype.card_pos_iff.mpr ⟨⟨1, Subgroup.one_mem _⟩⟩
  have hos := MulAction.card_orbit_mul_card_stabilizer_eq_card_group G x
  rw [← orbitFinset_card, hG] at hos
  calc orbitSize G x
      ≤ orbitSize G x * Fintype.card ↥(MulAction.stabilizer G x) :=
        Nat.le_mul_of_pos_right _ hstab
    _ = 2 * m := hos

/-- Parity step: an involution on a finite type of odd cardinality
    has a fixed point. (Via the permutation fixed-point lemma for
    the prime `2`: the reversal permutation has order dividing `2`,
    and `2` does not divide the odd cardinality.) -/
lemma exists_reversal_fixed (ρ : G) (hρ : ρ * ρ = 1) (hodd : Odd (Fintype.card α)) :
    ∃ ξ : α, ρ • ξ = ξ := by
  have h2 : (MulAction.toPermHom G α ρ) ^ (2 ^ 1) = 1 := by
    rw [pow_one, ← map_pow, pow_two, hρ, map_one]
  obtain ⟨ξ, hξ⟩ := Equiv.Perm.exists_fixed_point_of_prime (p := 2) (n := 1)
    (fun h => by obtain ⟨k, hk⟩ := hodd; obtain ⟨c, hc⟩ := h; omega) h2
  exact ⟨ξ, by simpa [MulAction.toPermHom_apply] using hξ⟩

/-- Stabilizer step: the orbit of a reversal-fixed point has size
    at most `m`. (Orbit–stabilizer: the orbit size times the
    stabilizer size is `2m`, and the stabilizer contains both `1`
    and `ρ ≠ 1`, hence has at least 2 elements.) -/
lemma orbitSize_le_of_fixed (m : ℕ) (ξ : α) (ρ : G) (hfix : ρ • ξ = ξ) (hρ1 : ρ ≠ 1)
    (hG : Fintype.card G = 2 * m) :
    orbitSize G ξ ≤ m := by
  have hmem : ρ ∈ MulAction.stabilizer G ξ := MulAction.mem_stabilizer_iff.mpr hfix
  have h2 : 2 ≤ Fintype.card ↥(MulAction.stabilizer G ξ) :=
    Fintype.one_lt_card_iff.mpr ⟨⟨ρ, hmem⟩, ⟨1, Subgroup.one_mem _⟩, by
      simp only [ne_eq, Subtype.mk.injEq]; exact hρ1⟩
  have hos := MulAction.card_orbit_mul_card_stabilizer_eq_card_group G ξ
  rw [← orbitFinset_card, hG] at hos
  have hle : orbitSize G ξ * 2 ≤ m * 2 := by
    calc orbitSize G ξ * 2
        ≤ orbitSize G ξ * Fintype.card ↥(MulAction.stabilizer G ξ) :=
          Nat.mul_le_mul_left _ h2
      _ = 2 * m := hos
      _ = m * 2 := Nat.mul_comm _ _
  exact Nat.le_of_mul_le_mul_right hle (by norm_num)

/-- Averaging step: if one orbit has size `o` with `1 ≤ o ≤ m`
    and every orbit has size at most `2m`, then the sum of orbit
    sizes over the whole support is at most `2m * D - m`.
    (Split the sum into the small orbit, where every point has
    orbit size `o`, and the complement, where every point has
    orbit size at most `2m`.) -/
lemma sum_orbitSize_le (m : ℕ) (ξ : α)
    (ho1 : 1 ≤ orbitSize G ξ) (hom : orbitSize G ξ ≤ m)
    (hle : ∀ x : α, orbitSize G x ≤ 2 * m) :
    ∑ x : α, orbitSize G x ≤ 2 * m * Fintype.card α - m := by
  classical
  set O := orbitFinset G ξ with hOdef
  set o := O.card with hodef
  have hoD : o ≤ Fintype.card α := by
    rw [hodef, hOdef]
    exact Finset.card_le_card (Finset.subset_univ _)
  have hmem : ∀ x ∈ O, orbitSize G x = o := by
    intro x hx
    have hxorb : x ∈ MulAction.orbit G ξ := by
      rw [hOdef] at hx
      simpa [orbitFinset] using hx
    have horb : MulAction.orbit G x = MulAction.orbit G ξ :=
      MulAction.orbit_eq_iff.mpr hxorb
    have hfin : orbitFinset G x = orbitFinset G ξ := by
      apply Finset.ext
      intro y
      simp only [orbitFinset, Finset.mem_filter, Finset.mem_univ, true_and, horb]
    show (orbitFinset G x).card = o
    rw [hfin]
  have hsumO : ∑ x ∈ O, orbitSize G x = o * o := by
    rw [Finset.sum_congr rfl hmem, Finset.sum_const, ← hodef, smul_eq_mul]
  have hsumC : ∑ x ∈ Finset.univ \ O, orbitSize G x
      ≤ (Fintype.card α - o) * (2 * m) := by
    have h1 : ∑ x ∈ Finset.univ \ O, orbitSize G x
        ≤ (Finset.univ \ O).card • (2 * m) :=
      Finset.sum_le_card_nsmul _ _ _ (fun x _ => hle x)
    rw [Finset.card_sdiff_of_subset (Finset.subset_univ O), Finset.card_univ,
      ← hodef, smul_eq_mul] at h1
    exact h1
  have hsplit : ∑ x ∈ Finset.univ \ O, orbitSize G x + ∑ x ∈ O, orbitSize G x
      = ∑ x : α, orbitSize G x :=
    Finset.sum_sdiff (Finset.subset_univ O)
  rw [hsumO] at hsplit
  have hprod1 : o * (2 * m) = 2 * (o * m) := by ring
  have hprod2 : (Fintype.card α - o) * (2 * m) + o * (2 * m)
      = Fintype.card α * (2 * m) := by
    rw [← Nat.add_mul, Nat.sub_add_cancel hoD]
  have hprod3 : Fintype.card α * (2 * m) = 2 * m * Fintype.card α := by ring
  have hbound : o * o + m ≤ o * (2 * m) := by
    have h1 : o * o ≤ o * m := Nat.mul_le_mul_left o hom
    have h2 : m ≤ o * m := by
      calc m = 1 * m := (one_mul m).symm
        _ ≤ o * m := Nat.mul_le_mul_right m ho1
    rw [hprod1]
    omega
  omega

/-- From a small orbit (size between `1` and `m`) to the rational
    bound `2m - B_m^sym ≥ m / D_eff > 0`, hence `B_m^sym < 2m`.
    This is the shared final step of both versions of 154. -/
lemma sym_bound_of_small_orbit (m : ℕ) (hm : 0 < m) (ξ : α)
    (ho1 : 1 ≤ orbitSize G ξ) (hom : orbitSize G ξ ≤ m)
    (hle : ∀ x : α, orbitSize G x ≤ 2 * m) (hDpos : 0 < Fintype.card α) :
    (2 * m : ℚ) - Bsym G α ≥ (m : ℚ) / (Fintype.card α : ℚ)
      ∧ Bsym G α < (2 * m : ℚ) := by
  have hsum := sum_orbitSize_le m ξ ho1 hom hle
  have hDposQ : (0 : ℚ) < (Fintype.card α : ℚ) := by exact_mod_cast hDpos
  have hmD : m ≤ 2 * m * Fintype.card α := by
    calc m = m * 1 := (mul_one m).symm
      _ ≤ m * Fintype.card α := Nat.mul_le_mul_left m hDpos
      _ ≤ 2 * m * Fintype.card α := Nat.mul_le_mul_right _ (by omega)
  have hsumQ : (∑ x : α, ((orbitSize G x : ℕ) : ℚ))
      ≤ (2 * m : ℚ) * (Fintype.card α : ℚ) - m := by
    have h2 : ((∑ x : α, orbitSize G x : ℕ) : ℚ)
        ≤ ((2 * m * Fintype.card α - m : ℕ) : ℚ) :=
      Nat.cast_le.mpr hsum
    rw [Nat.cast_sum] at h2
    have h3 : ((2 * m * Fintype.card α - m : ℕ) : ℚ)
        = (2 * m : ℚ) * (Fintype.card α : ℚ) - m := by
      rw [Nat.cast_sub hmD]
      push_cast
      ring
    rw [h3] at h2
    exact h2
  have hmain : (m : ℚ) / (Fintype.card α : ℚ) ≤ (2 * m : ℚ) - Bsym G α := by
    show (m : ℚ) / (Fintype.card α : ℚ) ≤ (2 * m : ℚ) -
      ((∑ x : α, ((orbitFinset G x).card : ℚ)) / (Fintype.card α : ℚ))
    rw [le_sub_iff_add_le, ← add_div, div_le_iff₀ hDposQ]
    linarith [hsumQ]
  refine ⟨hmain, ?_⟩
  have hpos : (0 : ℚ) < (m : ℚ) / (Fintype.card α : ℚ) :=
    div_pos (by exact_mod_cast hm) hDposQ
  linarith [hmain, hpos]

/-- TRACE-154, main version: for odd `m`, with `D_eff = a²`,
    `a` odd, the `Γ`-invariant support has odd size, the reversal
    involution has a fixed point `ξ₀` with `|Γ ξ₀| ≤ m`, and
    `2m - B_m^sym ≥ m / D_eff > 0`, hence `B_m^sym < 2m`. -/
theorem sym_bound (m : ℕ) (hm : 0 < m) (a : ℕ) (ha : Odd a)
    (hD : Fintype.card α = a * a) (hG : Fintype.card G = 2 * m)
    (ρ : G) (hρ : ρ * ρ = 1) (hρ1 : ρ ≠ 1) :
    (2 * m : ℚ) - Bsym G α ≥ (m : ℚ) / (Fintype.card α : ℚ)
      ∧ Bsym G α < (2 * m : ℚ) := by
  have hoddD : Odd (Fintype.card α) := by
    rw [hD]
    exact ha.mul ha
  obtain ⟨ξ₀, hξ₀⟩ := exists_reversal_fixed ρ hρ hoddD
  have hDpos : 0 < Fintype.card α := by
    obtain ⟨k, hk⟩ := hoddD
    omega
  exact sym_bound_of_small_orbit m hm ξ₀ (orbitSize_pos ξ₀)
    (orbitSize_le_of_fixed m ξ₀ ρ hξ₀ hρ1 hG)
    (fun x => orbitSize_le_card m x hG) hDpos

/-- TRACE-154, second version from the boundary: the same argument
    whenever `2m` does not divide `D_eff` (e.g. `m = 6`).
    Non-divisibility forces an orbit whose size divides `2m` but
    is not `2m`, hence is at most `m`; the averaging is the same. -/
theorem sym_bound_of_not_dvd (m : ℕ) (hm : 0 < m)
    (hG : Fintype.card G = 2 * m) (hnot : ¬ (2 * m ∣ Fintype.card α)) :
    (2 * m : ℚ) - Bsym G α ≥ (m : ℚ) / (Fintype.card α : ℚ)
      ∧ Bsym G α < (2 * m : ℚ) := by
  classical
  have hDpos : 0 < Fintype.card α := by
    rcases Nat.eq_zero_or_pos (Fintype.card α) with h | h
    · exact absurd (by rw [h]; exact dvd_zero (2 * m)) hnot
    · exact h
  have hex : ∃ ξ : α, orbitSize G ξ ≤ m := by
    by_contra hcon
    have hgt : ∀ ξ : α, m < orbitSize G ξ := by
      intro ξ
      by_contra hle
      exact hcon ⟨ξ, not_lt.mp hle⟩
    have hall : ∀ ξ : α, orbitSize G ξ = 2 * m := by
      intro ξ
      have hdvd : orbitSize G ξ ∣ 2 * m := by
        have hos := MulAction.card_orbit_mul_card_stabilizer_eq_card_group G ξ
        rw [← orbitFinset_card, hG] at hos
        exact ⟨Fintype.card ↥(MulAction.stabilizer G ξ), hos.symm⟩
      have hle2 : orbitSize G ξ ≤ 2 * m := orbitSize_le_card m ξ hG
      have hlt : m < orbitSize G ξ := hgt ξ
      obtain ⟨s, hs⟩ := hdvd
      rcases Nat.eq_zero_or_pos s with hs0 | hspos
      · rw [hs0, mul_zero] at hs
        omega
      · rcases Nat.lt_or_ge s 2 with hs1 | hs2
        · have hs1' : s = 1 := by omega
          rw [hs1', mul_one] at hs
          exact hs.symm
        · have hle : orbitSize G ξ * 2 ≤ m * 2 := by
            calc orbitSize G ξ * 2
                ≤ orbitSize G ξ * s := Nat.mul_le_mul_left _ hs2
              _ = 2 * m := hs.symm
              _ = m * 2 := Nat.mul_comm _ _
          have := Nat.le_of_mul_le_mul_right hle (by norm_num)
          omega
    have hcard : Fintype.card α
        = Fintype.card (MulAction.orbitRel.Quotient G α) * (2 * m) := by
      calc Fintype.card α
          = Fintype.card (Σ ω : MulAction.orbitRel.Quotient G α,
              ↥(MulAction.orbit G ω.out)) :=
            Fintype.card_congr (MulAction.selfEquivSigmaOrbits G α)
        _ = ∑ ω, Fintype.card ↥(MulAction.orbit G ω.out) := Fintype.card_sigma
        _ = ∑ _ω : MulAction.orbitRel.Quotient G α, (2 * m) :=
            Finset.sum_congr rfl (fun ω _ => by
              rw [← orbitFinset_card]; exact hall ω.out)
        _ = Fintype.card (MulAction.orbitRel.Quotient G α) * (2 * m) := by
            rw [Finset.sum_const, Finset.card_univ, smul_eq_mul]
    exact hnot ⟨Fintype.card (MulAction.orbitRel.Quotient G α), by
      rw [hcard, Nat.mul_comm]⟩
  obtain ⟨ξ, hξ⟩ := hex
  exact sym_bound_of_small_orbit m hm ξ (orbitSize_pos ξ) hξ
    (fun x => orbitSize_le_card m x hG) hDpos

#print axioms sym_bound
#print axioms sym_bound_of_not_dvd

end Parity
end LineD
end Bgs
