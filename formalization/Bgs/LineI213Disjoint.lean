import Bgs.LineIReduction

/-!
# BGS-TRACE-213 — pairwise disjointness of `{ν_ρ}` and the member sets `M_d(ρ)` from the congruence definition

Source: `mathematics/fixed-map/lineI_rprime_reduction.md` §4 (Theorem I4); registry boundaries of `BGS-TRACE-213` and of the
frozen definition `BGS-TRACE-206`: `ρ = (a, b) ∈ 𝓟* = {(2,8), (−2,8), (2,16), (−2,16)}`, `ν_ρ` the class `bν ≡ a (mod 2h)`,
levels `d ∣ h`, `1 < d ≤ √h`, members `M_d(ρ) = {ν : bν ≡ a (mod 2h/d), not (mod 2h/d′) for d′ ∣ d, d′ < d}`.  The class
`ν_ρ` is the case `d = 1` of the same predicate (`Mem h ρ 1`).  Here `h = h_m` satisfies `h² + 1 = 2y′²` (NSW numbers).

* `same_rho` : a common member of two levels `d ≠ d′` of one `ρ` satisfies the congruence modulo `2h/gcd(d,d′)` and is
  excluded from the larger level;
* `diff_rho` : different `ρ ≠ ρ′` cannot share a member (any admissible levels, `d = 1` included): an integer combination of
  the two congruences gives `2h ∣ d d′ r` with `r ∈ {±2, ±4, ±6}`; `h` odd and `3 ∤ h` (from `h² + 1 = 2y′²`) force
  `h ∣ dd′ ≤ h`, so `d = d′ = √h`, then `d ∣ 3` and `h = 1`;
* `disjoint` : for `h > 1` with `h² + 1 = 2y²`, `Mem h ρ d ν ∧ Mem h ρ′ d′ ν ⇒ ρ = ρ′ ∧ d = d′` (admissible `d, d′`);
* `reduction_congr` : the exact identity `Bgs.LineIReduction.reduction` (BGS-TRACE-213) with the member sets and the
  `ν_ρ` defined by these congruences (filters of a set `U` of units mod `2h`), so its disjointness hypotheses are discharged.

Note: the registry proof sketch bounds the modulus by `2h/max(d,d′) ≥ 2√h`; the Lean proof uses `h ∣ dd′` and the
arithmetic of `h_m` (`h` odd, `3 ∤ h`, from `h² + 1 = 2y′²`) instead, which is where `m ≥ 5` (`h_m > 1`) enters.

**Coverage:** together with `Bgs.LineIReduction`, the exact identity of BGS-TRACE-213 is now formalized without the
disjointness hypothesis.  **Not** formalized: the sufficiency (E″), (T″), (D) ⇒ R′ (`o(m)` / diagonal argument).  All proofs
are kernel-checked.
-/

namespace Bgs.LineI213Disjoint

open Finset

/-- `ν` satisfies the level-`d` congruence of `ρ = (a, b)` and none of the lower levels `d′ ∣ d, d′ < d`. -/
def Mem (h : ℕ) (ρ : ℤ × ℕ) (d : ℕ) (ν : ℤ) : Prop :=
  ((2 * h / d : ℕ) : ℤ) ∣ (ρ.2 : ℤ) * ν - ρ.1 ∧
    ∀ d' : ℕ, d' ∣ d → d' < d → ¬ ((2 * h / d' : ℕ) : ℤ) ∣ (ρ.2 : ℤ) * ν - ρ.1

/-- Admissible level: `d ∣ h`, `0 < d`, `d² ≤ h` (`d = 1` is the class `ν_ρ`). -/
def Adm (h d : ℕ) : Prop := 0 < d ∧ d ∣ h ∧ d * d ≤ h

/-- `𝓟*`. -/
def Pst : Finset (ℤ × ℕ) := {(2, 8), (-2, 8), (2, 16), (-2, 16)}

/-- `(2h/d) ∣ x ⇔ 2h ∣ d x` for `d ∣ h`. -/
lemma dvd_iff (h d : ℕ) (hd : 0 < d) (hdh : d ∣ h) (x : ℤ) :
    ((2 * h / d : ℕ) : ℤ) ∣ x ↔ ((2 * h : ℕ) : ℤ) ∣ d * x := by
  obtain ⟨e, rfl⟩ := hdh
  have : 2 * (d * e) / d = 2 * e := by
    rw [show 2 * (d * e) = d * (2 * e) by ring, Nat.mul_div_cancel_left _ hd]
  rw [this]; push_cast
  rw [show (2 : ℤ) * (d * e) = d * (2 * e) by ring]
  exact (mul_dvd_mul_iff_left (by exact_mod_cast hd.ne')).symm

lemma arith_of_nsw (h y : ℕ) (hy : h ^ 2 + 1 = 2 * y ^ 2) : ¬ 2 ∣ h ∧ ¬ 3 ∣ h := by
  constructor
  · rintro ⟨k, rfl⟩
    have := congrArg (· % 2) hy; simp [Nat.add_mod, Nat.pow_mod] at this
  · rintro ⟨k, rfl⟩
    have h3 : ((3 * k : ℕ) : ZMod 3) ^ 2 + 1 = 2 * (y : ZMod 3) ^ 2 := by
      exact_mod_cast congrArg (Nat.cast : ℕ → ZMod 3) hy
    have e : ((3 * k : ℕ) : ZMod 3) = 0 := by
      rw [Nat.cast_mul]; rw [show ((3 : ℕ) : ZMod 3) = 0 from rfl, zero_mul]
    have key : ∀ z : ZMod 3, (0 : ZMod 3) ^ 2 + 1 ≠ 2 * z ^ 2 := by decide
    rw [e] at h3; exact key _ h3

theorem same_rho (h : ℕ) (ρ : ℤ × ℕ) (d d' : ℕ) (hd : Adm h d) (hd' : Adm h d') (hne : d ≠ d') (ν : ℤ)
    (h1 : Mem h ρ d ν) (h2 : Mem h ρ d' ν) : False := by
  set x := (ρ.2 : ℤ) * ν - ρ.1
  have a1 := (dvd_iff h d hd.1 hd.2.1 x).1 h1.1
  have a2 := (dvd_iff h d' hd'.1 hd'.2.1 x).1 h2.1
  set g := Nat.gcd d d'
  have hg : (g : ℤ) = d * Nat.gcdA d d' + d' * Nat.gcdB d d' := Nat.gcd_eq_gcd_ab d d'
  have hgx : ((2 * h : ℕ) : ℤ) ∣ g * x := by
    rw [hg, add_mul, mul_right_comm, mul_right_comm (d' : ℤ)]
    exact dvd_add (dvd_mul_of_dvd_left a1 _) (dvd_mul_of_dvd_left a2 _)
  have gpos : 0 < g := Nat.gcd_pos_of_pos_left _ hd.1
  have gh : g ∣ h := (Nat.gcd_dvd_left d d').trans hd.2.1
  have hx : ((2 * h / g : ℕ) : ℤ) ∣ x := (dvd_iff h g gpos gh x).2 hgx
  rcases lt_or_gt_of_ne hne with hlt | hlt
  · exact h2.2 g (Nat.gcd_dvd_right d d') (lt_of_le_of_lt (Nat.le_of_dvd hd.1 (Nat.gcd_dvd_left d d')) hlt) hx
  · exact h1.2 g (Nat.gcd_dvd_left d d') (lt_of_le_of_lt (Nat.le_of_dvd hd'.1 (Nat.gcd_dvd_right d d')) hlt) hx

/-- Core arithmetic: two congruences at admissible levels with `c₁x₁ + c₂x₂ = 2s`, `s ∈ {±1, ±2, ±3}`, are incompatible. -/
lemma core (h d d' : ℕ) (hh : 1 < h) (h2 : ¬ 2 ∣ h) (h3 : ¬ 3 ∣ h) (hd : Adm h d) (hd' : Adm h d')
    (x1 x2 c1 c2 s : ℤ) (hs : s = 1 ∨ s = -1 ∨ s = 2 ∨ s = -2 ∨ s = 3 ∨ s = -3)
    (a1 : ((2 * h : ℕ) : ℤ) ∣ d * x1) (a2 : ((2 * h : ℕ) : ℤ) ∣ d' * x2) (hc : c1 * x1 + c2 * x2 = 2 * s) :
    False := by
  have hcop : IsCoprime (h : ℤ) s := by
    rw [Int.isCoprime_iff_gcd_eq_one]
    rcases hs with rfl | rfl | rfl | rfl | rfl | rfl <;> simp [Int.gcd] <;>
      first
      | rfl
      | exact (Nat.coprime_comm.1 ((Nat.coprime_primes (by norm_num) (by norm_num)).2 rfl)).symm
      | skip
    all_goals
      first
      | exact Nat.Coprime.symm ((Nat.Prime.coprime_iff_not_dvd Nat.prime_two).2 h2)
      | exact Nat.Coprime.symm ((Nat.Prime.coprime_iff_not_dvd Nat.prime_three).2 h3)
      | exact Nat.odd_iff.2 (by omega)
  -- 2h ∣ d d' (2 s)
  have b1 : ((2 * h : ℕ) : ℤ) ∣ (d : ℤ) * d' * (2 * s) := by
    rw [← hc, mul_add]
    refine dvd_add ?_ ?_
    · have := dvd_mul_of_dvd_left a1 (d' * c1); exact this.trans ⟨1, by ring⟩
    · have := dvd_mul_of_dvd_left a2 (d * c2); exact this.trans ⟨1, by ring⟩
  have b2 : (h : ℤ) ∣ (d : ℤ) * d' * s := by
    obtain ⟨k, hk⟩ := b1
    exact ⟨k, by push_cast at hk; linarith⟩
  have b3 : (h : ℤ) ∣ (d : ℤ) * d' := hcop.dvd_of_dvd_mul_right b2
  have b4 : h ∣ d * d' := by exact_mod_cast b3
  have hle : h ≤ d * d' := Nat.le_of_dvd (Nat.mul_pos hd.1 hd'.1) b4
  have e1 : d = d' := by nlinarith [hd.2.2, hd'.2.2]
  subst e1
  have ehd : h = d * d := le_antisymm hle hd.2.2
  -- 2h ∣ d (2s)
  have c3 : ((2 * h : ℕ) : ℤ) ∣ (d : ℤ) * (2 * s) := by
    rw [← hc, mul_add]
    exact dvd_add ((dvd_mul_of_dvd_left a1 c1).trans ⟨1, by ring⟩) ((dvd_mul_of_dvd_left a2 c2).trans ⟨1, by ring⟩)
  have c4 : (d : ℤ) ∣ s := by
    obtain ⟨k, hk⟩ := c3
    rw [ehd] at hk; push_cast at hk
    have hd0 : (d : ℤ) ≠ 0 := by exact_mod_cast hd.1.ne'
    refine ⟨k, ?_⟩
    have : (d : ℤ) * (2 * s) = (d : ℤ) * (2 * (d * k)) := by rw [hk]; ring
    have := mul_left_cancel₀ hd0 this
    linarith
  have c5 : d ∣ 6 := by
    have : (d : ℤ) ∣ 6 := by
      rcases hs with rfl | rfl | rfl | rfl | rfl | rfl
      all_goals first
        | exact c4.trans (by norm_num)
        | exact (dvd_neg.2 c4).trans (by norm_num)
    exact_mod_cast this
  have hdh : d ∣ h := hd.2.1
  have : d = 1 := by
    have hd6 : d ∈ Nat.divisors 6 := Nat.mem_divisors.2 ⟨c5, by norm_num⟩
    have : Nat.divisors 6 = {1, 2, 3, 6} := by decide
    rw [this] at hd6
    simp only [Finset.mem_insert, Finset.mem_singleton] at hd6
    rcases hd6 with e | e | e | e
    · exact e
    · exact absurd (e ▸ hdh) h2
    · exact absurd (e ▸ hdh) h3
    · exact absurd ((show 2 ∣ 6 by norm_num).trans (e ▸ hdh)) h2
  subst this; omega

theorem diff_rho (h : ℕ) (hh : 1 < h) (h2 : ¬ 2 ∣ h) (h3 : ¬ 3 ∣ h) (ρ ρ' : ℤ × ℕ) (hρ : ρ ∈ Pst) (hρ' : ρ' ∈ Pst)
    (hne : ρ ≠ ρ') (d d' : ℕ) (hd : Adm h d) (hd' : Adm h d') (ν : ℤ) (m1 : Mem h ρ d ν) (m2 : Mem h ρ' d' ν) :
    False := by
  have a1 := (dvd_iff h d hd.1 hd.2.1 _).1 m1.1
  have a2 := (dvd_iff h d' hd'.1 hd'.2.1 _).1 m2.1
  simp only [Pst, Finset.mem_insert, Finset.mem_singleton] at hρ hρ'
  rcases hρ with rfl | rfl | rfl | rfl <;> rcases hρ' with rfl | rfl | rfl | rfl <;>
    first
    | exact hne rfl
    | (refine core h d d' hh h2 h3 hd hd' _ _ 1 (-1) 2 (by norm_num) a1 a2 ?_; push_cast; linarith)
    | (refine core h d d' hh h2 h3 hd hd' _ _ 1 (-1) (-2) (by norm_num) a1 a2 ?_; push_cast; linarith)
    | (refine core h d d' hh h2 h3 hd hd' _ _ 2 (-1) 1 (by norm_num) a1 a2 ?_; push_cast; linarith)
    | (refine core h d d' hh h2 h3 hd hd' _ _ 2 (-1) (-1) (by norm_num) a1 a2 ?_; push_cast; linarith)
    | (refine core h d d' hh h2 h3 hd hd' _ _ 2 (-1) 3 (by norm_num) a1 a2 ?_; push_cast; linarith)
    | (refine core h d d' hh h2 h3 hd hd' _ _ 2 (-1) (-3) (by norm_num) a1 a2 ?_; push_cast; linarith)
    | (refine core h d d' hh h2 h3 hd hd' _ _ 1 (-2) 1 (by norm_num) a1 a2 ?_; push_cast; linarith)
    | (refine core h d d' hh h2 h3 hd hd' _ _ 1 (-2) (-1) (by norm_num) a1 a2 ?_; push_cast; linarith)
    | (refine core h d d' hh h2 h3 hd hd' _ _ 1 (-2) 3 (by norm_num) a1 a2 ?_; push_cast; linarith)
    | (refine core h d d' hh h2 h3 hd hd' _ _ 1 (-2) (-3) (by norm_num) a1 a2 ?_; push_cast; linarith)

/-- **Disjointness (BGS-TRACE-213).**  For `h = h_m > 1` (`h² + 1 = 2y²`), the classes `ν_ρ` (`d = 1`) and the member sets
`M_d(ρ)` (`ρ ∈ 𝓟*`, admissible `d`) are pairwise disjoint. -/
theorem disjoint (h y : ℕ) (hh : 1 < h) (hy : h ^ 2 + 1 = 2 * y ^ 2) (ρ ρ' : ℤ × ℕ) (hρ : ρ ∈ Pst) (hρ' : ρ' ∈ Pst)
    (d d' : ℕ) (hd : Adm h d) (hd' : Adm h d') (ν : ℤ) (m1 : Mem h ρ d ν) (m2 : Mem h ρ' d' ν) :
    ρ = ρ' ∧ d = d' := by
  obtain ⟨h2, h3⟩ := arith_of_nsw h y hy
  by_cases e : ρ = ρ'
  · subst e
    refine ⟨rfl, ?_⟩
    by_contra hne
    exact same_rho h ρ d d' hd hd' hne ν m1 m2
  · exact (diff_rho h hh h2 h3 ρ ρ' hρ hρ' e d d' hd hd' ν m1 m2).elim

open Classical in
/-- **BGS-TRACE-213, exact identity with the disjointness derived.**  `U ⊆ ℕ` the units mod `2h` (representatives), `νr ρ ∈ U`
the class `ν_ρ` (`Mem h ρ 1`), `Ds ρ` included levels (`1 < d`, admissible), members `M_d(ρ) = {ν ∈ U : Mem h ρ d ν}`. -/
theorem reduction_congr (h y : ℕ) (hh : 1 < h) (hy : h ^ 2 + 1 = 2 * y ^ 2) (U : Finset ℕ) (hU : U.Nonempty)
    (RMT : ℝ) (X : ℕ → ℝ) (νr : ℤ × ℕ → ℕ) (hνU : ∀ ρ ∈ Pst, νr ρ ∈ U) (hν : ∀ ρ ∈ Pst, Mem h ρ 1 (νr ρ))
    (Ds : ℤ × ℕ → Finset ℕ) (hDs : ∀ ρ ∈ Pst, ∀ d ∈ Ds ρ, 1 < d ∧ Adm h d) :
    let Memb : ℤ × ℕ → ℕ → Finset ℕ := fun ρ d => U.filter (fun ν => Mem h ρ d ν)
    ((U.card : ℝ)⁻¹ * ∑ ν ∈ U, X ν) - RMT - Bgs.LineIReduction.Res (U.card : ℝ) RMT X Pst νr Ds Memb
      = (U.card : ℝ)⁻¹ * ∑ ν ∈ U \ Bgs.LineIReduction.resonant Pst νr Ds Memb, (X ν - RMT)
        + (U.card : ℝ)⁻¹ * ∑ ρ ∈ Pst, ∑ d ∈ Ds ρ, Bgs.LineIReduction.Dev X νr Memb ρ d := by
  intro Memb
  have adm1 : Adm h 1 := ⟨one_pos, one_dvd h, by omega⟩
  -- every element of the ρ-block is a member at some admissible level
  have blk : ∀ ρ ∈ Pst, ∀ ν ∈ insert (νr ρ) ((Ds ρ).biUnion (Memb ρ)),
      ∃ d, Adm h d ∧ Mem h ρ d ν ∧ (ν = νr ρ ↔ d = 1) := by
    intro ρ hρ ν hν'
    rcases Finset.mem_insert.1 hν' with rfl | hm
    · exact ⟨1, adm1, hν ρ hρ, by simp⟩
    · obtain ⟨d, hdD, hm⟩ := Finset.mem_biUnion.1 hm
      have hm' := (Finset.mem_filter.1 hm).2
      refine ⟨d, (hDs ρ hρ d hdD).2, hm', ⟨fun e => ?_, fun e => ?_⟩⟩
      · subst e
        exact absurd (disjoint h y hh hy ρ ρ hρ hρ d 1 (hDs ρ hρ d hdD).2 adm1 _ hm' (hν ρ hρ)).2
          (by have := (hDs ρ hρ d hdD).1; omega)
      · have := (hDs ρ hρ d hdD).1; omega
  refine Bgs.LineIReduction.reduction U hU RMT X Pst νr Ds Memb ?_ ?_ ?_ ?_
  · intro ρ hρ ρ' hρ' hne
    refine Finset.disjoint_left.2 (fun ν a b => hne ?_)
    obtain ⟨d, hd, md, -⟩ := blk ρ hρ ν a
    obtain ⟨d', hd', md', -⟩ := blk ρ' hρ' ν b
    exact (disjoint h y hh hy ρ ρ' hρ hρ' d d' hd hd' ν md md').1
  · intro ρ hρ hmem
    obtain ⟨d, hdD, hm⟩ := Finset.mem_biUnion.1 hmem
    have hm' := (Finset.mem_filter.1 hm).2
    have := (disjoint h y hh hy ρ ρ hρ hρ d 1 (hDs ρ hρ d hdD).2 adm1 _ hm' (hν ρ hρ)).2
    have := (hDs ρ hρ d hdD).1; omega
  · intro ρ hρ d hd d' hd' hne
    refine Finset.disjoint_left.2 (fun ν a b => hne ?_)
    exact (disjoint h y hh hy ρ ρ hρ hρ d d' (hDs ρ hρ d hd).2 (hDs ρ hρ d' hd').2 ν
      (Finset.mem_filter.1 a).2 (Finset.mem_filter.1 b).2).2
  · intro ν hνS
    unfold Bgs.LineIReduction.resonant at hνS
    obtain ⟨ρ, hρ, hb⟩ := Finset.mem_biUnion.1 hνS
    rcases Finset.mem_insert.1 hb with rfl | hm
    · exact hνU ρ hρ
    · obtain ⟨d, -, hm⟩ := Finset.mem_biUnion.1 hm
      exact (Finset.mem_filter.1 hm).1

end Bgs.LineI213Disjoint
