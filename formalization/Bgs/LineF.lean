import Mathlib

/-!
# Line F: the vertex/edge inclusion–exclusion lemma behind the lifted transfer operators

For a word `fs = [f₀, …, f_{m-1}]` of integer maps (in the application `f_x(k) = ⌊(k+x)/λ + 1/2⌋`, real shift `x` = letter `n` (k1) or `n/7` (49-state law)),
a closed *vertex chain* is a `k` with `F k = k` (`F` = composite, `f₀` applied first), and a closed *edge chain*
is an `e` such that every step is non-degenerate (`f (x+1) = f x + 1` along the orbit of `e`) and `F e = e`.
Main results:
* `step_round`   : `k ↦ ⌊(k+n)·μ + 1/2⌋` has increments in {0,1} for `0 ≤ μ < 1`.
* `edgeOK_iff`   : for step-{0,1} maps, the edge chain from `e` is non-degenerate iff `F (e+1) = F e + 1`.
* `count_identity` : if `F` has step-{0,1} increments and `F A > A`, `F B < B` (`A ≤ B`) then
     #{k ∈ [A,B] : F k = k} − #{k ∈ [A,B) : F k = k ∧ F (k+1) = k+1} = 1.
* `fix_outside`  : no fixed point outside `(A,B)`; so the counts are the global counts.
* `eventually_below_comp` / `eventually_above_comp` / `round_below` / `round_above`: existence of `A`, `B` for composites of
     rounding maps with `0 < μ < 1`.
Hence (#closed vertex chains) − (#closed edge chains) = 1 for every word: the identity `t_m = Tr L_V^m − Tr L_E^m`.
No `sorry`, no `native_decide`.

Scope (integration note, BGS-TRACE-197): formalised here are only the fixed-point / adjacent-fixed-pair counting
(`vertex_minus_edge`, `count_identity`, `fix_outside`) and the characterisation of closed edge chains (`edge_closed_iff`).
Not formalised: trace class of the lifted operators, the Ruelle / Bandtlow–Jenkinson trace formula, the link from
closed chains to operator blocks, and all ball-arithmetic certificates (BGS-TRACE-198..201).
-/

namespace Bgs.LineF

/-- increments in {0,1} -/
def StepOK (f : ℤ → ℤ) : Prop := ∀ k, f (k + 1) = f k ∨ f (k + 1) = f k + 1

theorem step_round (n : ℝ) (μ : ℝ) (h0 : 0 ≤ μ) (h1 : μ < 1) :
    StepOK (fun k : ℤ => ⌊((k : ℝ) + n) * μ + 1 / 2⌋) := by
  intro k
  have hy' : (((k + 1 : ℤ) : ℝ) + n) * μ + 1 / 2 = (((k : ℝ) + n) * μ + 1 / 2) + μ := by push_cast; ring
  show ⌊(((k + 1 : ℤ) : ℝ) + n) * μ + 1 / 2⌋ = ⌊((k : ℝ) + n) * μ + 1 / 2⌋ ∨
       ⌊(((k + 1 : ℤ) : ℝ) + n) * μ + 1 / 2⌋ = ⌊((k : ℝ) + n) * μ + 1 / 2⌋ + 1
  rw [hy']
  generalize ((k : ℝ) + n) * μ + 1 / 2 = y
  have a1 : ⌊y⌋ ≤ ⌊y + μ⌋ := Int.floor_le_floor (by linarith)
  have a2 : ⌊y + μ⌋ < ⌊y⌋ + 2 := by
    rw [Int.floor_lt]
    have := Int.lt_floor_add_one y
    push_cast; linarith
  omega

theorem StepOK.mono {f : ℤ → ℤ} (hf : StepOK f) : Monotone f := by
  apply monotone_int_of_le_succ
  intro k; rcases hf k with h | h <;> omega

theorem StepOK.comp {f g : ℤ → ℤ} (hf : StepOK f) (hg : StepOK g) : StepOK (g ∘ f) := by
  intro k
  simp only [Function.comp]
  rcases hf k with h | h
  · left; rw [h]
  · rw [h]; exact hg (f k)

/-- composite, first map applied first -/
def comp : List (ℤ → ℤ) → ℤ → ℤ
  | [], x => x
  | f :: fs, x => comp fs (f x)

def AllStep : List (ℤ → ℤ) → Prop
  | [] => True
  | f :: fs => StepOK f ∧ AllStep fs

theorem comp_step : ∀ fs : List (ℤ → ℤ), AllStep fs → StepOK (comp fs)
  | [], _ => by intro k; right; rfl
  | f :: fs, ⟨hf, hfs⟩ => by
      have := StepOK.comp hf (comp_step fs hfs)
      intro k; exact this k

/-- non-degenerate edge chain from edge (e, e+1) -/
def edgeOK : List (ℤ → ℤ) → ℤ → Prop
  | [], _ => True
  | f :: fs, e => f (e + 1) = f e + 1 ∧ edgeOK fs (f e)

theorem edgeOK_iff : ∀ (fs : List (ℤ → ℤ)), AllStep fs → ∀ e, (edgeOK fs e ↔ comp fs (e + 1) = comp fs e + 1)
  | [], _, e => by simp [edgeOK, comp]
  | f :: fs, ⟨hf, hfs⟩, e => by
      simp only [edgeOK, comp]
      rw [edgeOK_iff fs hfs (f e)]
      constructor
      · rintro ⟨h1, h2⟩; rw [h1]; exact h2
      · intro h
        rcases hf e with h1 | h1
        · rw [h1] at h; omega
        · exact ⟨h1, by rw [h1] at h; exact h⟩

/-- closed edge chain at e  ↔  e and e+1 both fixed -/
theorem edge_closed_iff (fs : List (ℤ → ℤ)) (hs : AllStep fs) (e : ℤ) :
    (edgeOK fs e ∧ comp fs e = e) ↔ (comp fs e = e ∧ comp fs (e + 1) = e + 1) := by
  rw [edgeOK_iff fs hs e]
  constructor
  · rintro ⟨h1, h2⟩; exact ⟨h2, by rw [h1, h2]⟩
  · rintro ⟨h1, h2⟩; exact ⟨by rw [h2, h1], h1⟩

/-- vertex-minus-edge count on [A, A+n] -/
def V (F : ℤ → ℤ) (A : ℤ) (n : ℕ) : ℤ :=
  ∑ i ∈ Finset.range (n + 1), if F (A + i) = A + i then 1 else 0
def E (F : ℤ → ℤ) (A : ℤ) (n : ℕ) : ℤ :=
  ∑ i ∈ Finset.range n, if (F (A + i) = A + i ∧ F (A + i + 1) = A + i + 1) then 1 else 0

theorem VE_step (F : ℤ → ℤ) (hF : StepOK F) (A : ℤ) (hA : A < F A) :
    ∀ n : ℕ, V F A n - E F A n = if F (A + n) ≤ A + n then 1 else 0 := by
  intro n
  induction n with
  | zero =>
    simp only [V, E, Finset.sum_range_succ, Finset.sum_range_zero]
    simp
    have : ¬ F A ≤ A := by omega
    have h2 : ¬ F A = A := by omega
    simp [this, h2]
  | succ n ih =>
    have hV : V F A (n + 1) = V F A n + (if F (A + (n + 1 : ℕ)) = A + (n + 1 : ℕ) then 1 else 0) := by
      simp only [V]; rw [Finset.sum_range_succ (n := n + 1)]
    have hE : E F A (n + 1) = E F A n +
        (if (F (A + n) = A + n ∧ F (A + n + 1) = A + n + 1) then 1 else 0) := by
      simp only [E]; rw [Finset.sum_range_succ]
    rw [hV, hE]
    have key : V F A n + (if F (A + (n + 1 : ℕ)) = A + (n + 1 : ℕ) then 1 else 0)
        - (E F A n + (if (F (A + n) = A + n ∧ F (A + n + 1) = A + n + 1) then 1 else 0))
        = (V F A n - E F A n) + (if F (A + (n + 1 : ℕ)) = A + (n + 1 : ℕ) then 1 else 0)
          - (if (F (A + n) = A + n ∧ F (A + n + 1) = A + n + 1) then 1 else 0) := by ring
    rw [key, ih]
    have hc : ((n + 1 : ℕ) : ℤ) = (n : ℤ) + 1 := by push_cast; ring
    rw [hc]
    have hs := hF (A + n)
    have e1 : A + (↑n + 1) = A + ↑n + 1 := by ring
    rw [e1]
    rcases hs with h | h <;> rw [h] <;> split_ifs <;> omega

theorem count_identity (F : ℤ → ℤ) (hF : StepOK F) (A B : ℤ) (hAB : A ≤ B)
    (hA : A < F A) (hB : F B < B) :
    V F A (B - A).toNat - E F A (B - A).toNat = 1 := by
  rw [VE_step F hF A hA]
  have : A + ((B - A).toNat : ℤ) = B := by rw [Int.toNat_of_nonneg (by omega)]; ring
  rw [this]; simp; omega

/-- fixed points of a step-{0,1} map lie strictly between A and B -/
theorem fix_outside (F : ℤ → ℤ) (hF : StepOK F) (A B : ℤ) (hA : A < F A) (hB : F B < B) (k : ℤ)
    (hk : F k = k) : A < k ∧ k < B := by
  -- g k = F k - k is antitone
  have anti : ∀ a b : ℤ, a ≤ b → F b - b ≤ F a - a := by
    intro a b hab
    obtain ⟨d, rfl⟩ : ∃ d : ℕ, b = a + d := ⟨(b - a).toNat, by rw [Int.toNat_of_nonneg (by omega)]; ring⟩
    induction d with
    | zero => simp
    | succ d ih =>
      have := hF (a + d)
      have e1 : a + ((d + 1 : ℕ) : ℤ) = a + d + 1 := by push_cast; ring
      rw [e1]; have := ih (by omega); rcases hF (a + d) with h | h <;> omega
  constructor
  · by_contra h; push Not at h; have := anti k A h; omega
  · by_contra h; push Not at h; have := anti B k h; omega

/-- existence of A, B: eventually-below / eventually-above are preserved by composition of monotone maps -/
def EvBelow (f : ℤ → ℤ) : Prop := ∃ M, ∀ k, M ≤ k → f k < k
def EvAbove (f : ℤ → ℤ) : Prop := ∃ M, ∀ k, k ≤ M → k < f k

theorem evBelow_comp {f g : ℤ → ℤ} (hf : EvBelow f) (hg : EvBelow g) (gm : Monotone g) :
    EvBelow (g ∘ f) := by
  obtain ⟨M1, h1⟩ := hf; obtain ⟨M2, h2⟩ := hg
  refine ⟨max M1 (g M2 + 1), fun k hk => ?_⟩
  simp only [Function.comp]
  have hk1 : M1 ≤ k := le_trans (le_max_left _ _) hk
  have hk2 : g M2 + 1 ≤ k := le_trans (le_max_right _ _) hk
  by_cases hc : M2 ≤ f k
  · have := h2 (f k) hc; have := h1 k hk1; omega
  · push Not at hc; have := gm hc.le; omega

theorem evAbove_comp {f g : ℤ → ℤ} (hf : EvAbove f) (hg : EvAbove g) (gm : Monotone g) :
    EvAbove (g ∘ f) := by
  obtain ⟨M1, h1⟩ := hf; obtain ⟨M2, h2⟩ := hg
  refine ⟨min M1 (g M2 - 1), fun k hk => ?_⟩
  simp only [Function.comp]
  have hk1 : k ≤ M1 := le_trans hk (min_le_left _ _)
  have hk2 : k ≤ g M2 - 1 := le_trans hk (min_le_right _ _)
  by_cases hc : f k ≤ M2
  · have := h2 (f k) hc; have := h1 k hk1; omega
  · push Not at hc; have := gm hc.le; omega

theorem round_below (n : ℝ) (μ : ℝ) (h0 : 0 ≤ μ) (h1 : μ < 1) :
    EvBelow (fun k : ℤ => ⌊((k : ℝ) + n) * μ + 1 / 2⌋) := by
  -- for k ≥ M: (k+n)μ + 1/2 < k  ⇐  k(1-μ) > nμ + 1/2
  obtain ⟨M, hM⟩ := exists_int_gt ((|(n : ℝ)| * μ + 1) / (1 - μ))
  refine ⟨max M 0, fun k hk => ?_⟩
  rw [Int.floor_lt]
  have hk' : (M : ℝ) ≤ k := by exact_mod_cast le_trans (le_max_left _ _) hk
  have hpos : 0 < 1 - μ := by linarith
  have h2 : (|(n : ℝ)| * μ + 1) < (k : ℝ) * (1 - μ) := by
    have := (div_lt_iff₀ hpos).mp (lt_of_lt_of_le hM hk'); linarith
  have h3 : (n : ℝ) * μ ≤ |(n : ℝ)| * μ := mul_le_mul_of_nonneg_right (le_abs_self _) h0
  nlinarith

theorem round_above (n : ℝ) (μ : ℝ) (h0 : 0 ≤ μ) (h1 : μ < 1) :
    EvAbove (fun k : ℤ => ⌊((k : ℝ) + n) * μ + 1 / 2⌋) := by
  obtain ⟨M, hM⟩ := exists_int_gt ((|(n : ℝ)| * μ + 1) / (1 - μ))
  refine ⟨min (-M) 0, fun k hk => ?_⟩
  rw [Int.lt_floor_iff]
  have hk' : (k : ℝ) ≤ -(M : ℝ) := by exact_mod_cast le_trans hk (min_le_left _ _)
  have hpos : 0 < 1 - μ := by linarith
  have h2 : (|(n : ℝ)| * μ + 1) < (-(k : ℝ)) * (1 - μ) := by
    have hm : (M : ℝ) ≤ -(k : ℝ) := by linarith
    have := (div_lt_iff₀ hpos).mp (lt_of_lt_of_le hM hm); linarith
  have h3 : -(|(n : ℝ)| * μ) ≤ (n : ℝ) * μ := by
    have := mul_le_mul_of_nonneg_right (neg_abs_le (n : ℝ)) h0; linarith
  push_cast; nlinarith

/-! ### Assembly for words of rounding maps -/
def EvLe (f : ℤ → ℤ) : Prop := ∃ M, ∀ k, M ≤ k → f k ≤ k
def EvGe (f : ℤ → ℤ) : Prop := ∃ M, ∀ k, k ≤ M → k ≤ f k

theorem evLe_comp {f g : ℤ → ℤ} (hf : EvLe f) (hg : EvLe g) (gm : Monotone g) : EvLe (g ∘ f) := by
  obtain ⟨M1, h1⟩ := hf; obtain ⟨M2, h2⟩ := hg
  refine ⟨max M1 (g M2), fun k hk => ?_⟩
  simp only [Function.comp]
  have hk1 : M1 ≤ k := le_trans (le_max_left _ _) hk
  have hk2 : g M2 ≤ k := le_trans (le_max_right _ _) hk
  by_cases hc : M2 ≤ f k
  · have := h2 (f k) hc; have := h1 k hk1; omega
  · push Not at hc; have := gm hc.le; omega

theorem evGe_comp {f g : ℤ → ℤ} (hf : EvGe f) (hg : EvGe g) (gm : Monotone g) : EvGe (g ∘ f) := by
  obtain ⟨M1, h1⟩ := hf; obtain ⟨M2, h2⟩ := hg
  refine ⟨min M1 (g M2), fun k hk => ?_⟩
  simp only [Function.comp]
  have hk1 : k ≤ M1 := le_trans hk (min_le_left _ _)
  have hk2 : k ≤ g M2 := le_trans hk (min_le_right _ _)
  by_cases hc : f k ≤ M2
  · have := h2 (f k) hc; have := h1 k hk1; omega
  · push Not at hc; have := gm hc.le; omega

theorem evBelow_comp' {f g : ℤ → ℤ} (hf : EvBelow f) (hg : EvLe g) (gm : Monotone g) : EvBelow (g ∘ f) := by
  obtain ⟨M1, h1⟩ := hf; obtain ⟨M2, h2⟩ := hg
  refine ⟨max M1 (g M2 + 1), fun k hk => ?_⟩
  simp only [Function.comp]
  have hk1 : M1 ≤ k := le_trans (le_max_left _ _) hk
  have hk2 : g M2 + 1 ≤ k := le_trans (le_max_right _ _) hk
  by_cases hc : M2 ≤ f k
  · have := h2 (f k) hc; have := h1 k hk1; omega
  · push Not at hc; have := gm hc.le; omega

theorem evAbove_comp' {f g : ℤ → ℤ} (hf : EvAbove f) (hg : EvGe g) (gm : Monotone g) : EvAbove (g ∘ f) := by
  obtain ⟨M1, h1⟩ := hf; obtain ⟨M2, h2⟩ := hg
  refine ⟨min M1 (g M2 - 1), fun k hk => ?_⟩
  simp only [Function.comp]
  have hk1 : k ≤ M1 := le_trans hk (min_le_left _ _)
  have hk2 : k ≤ g M2 - 1 := le_trans hk (min_le_right _ _)
  by_cases hc : f k ≤ M2
  · have := h2 (f k) hc; have := h1 k hk1; omega
  · push Not at hc; have := gm hc.le; omega

/-- the rounding map k ↦ ⌊(k+n)μ + 1/2⌋ (μ = 1/λ) -/
noncomputable def roundMap (μ : ℝ) (n : ℝ) : ℤ → ℤ := fun k => ⌊((k : ℝ) + n) * μ + 1 / 2⌋

theorem allStep_round (μ : ℝ) (h0 : 0 ≤ μ) (h1 : μ < 1) : ∀ ns : List ℝ, AllStep (ns.map (roundMap μ))
  | [] => trivial
  | n :: ns => ⟨step_round n μ h0 h1, allStep_round μ h0 h1 ns⟩

theorem evLe_round (μ : ℝ) (h0 : 0 ≤ μ) (h1 : μ < 1) : ∀ ns : List ℝ, EvLe (comp (ns.map (roundMap μ)))
  | [] => ⟨0, fun k _ => le_refl _⟩
  | n :: ns => by
      have hb := round_below n μ h0 h1
      obtain ⟨M, hM⟩ := hb
      have hf : EvLe (roundMap μ n) := ⟨M, fun k hk => (hM k hk).le⟩
      have := evLe_comp hf (evLe_round μ h0 h1 ns)
        (StepOK.mono (comp_step _ (allStep_round μ h0 h1 ns)))
      exact this

theorem evGe_round (μ : ℝ) (h0 : 0 ≤ μ) (h1 : μ < 1) : ∀ ns : List ℝ, EvGe (comp (ns.map (roundMap μ)))
  | [] => ⟨0, fun k _ => le_refl _⟩
  | n :: ns => by
      obtain ⟨M, hM⟩ := round_above n μ h0 h1
      have hf : EvGe (roundMap μ n) := ⟨M, fun k hk => (hM k hk).le⟩
      exact evGe_comp hf (evGe_round μ h0 h1 ns)
        (StepOK.mono (comp_step _ (allStep_round μ h0 h1 ns)))

/-- **Main combinatorial theorem.** For every nonempty word `n₀ … n_{m-1}` and `0 ≤ μ < 1`, the composite rounding map
`F` has finitely many fixed points, all in `(A,B)`, and
(#fixed points) − (#adjacent fixed pairs) = 1, i.e. (#closed vertex chains) − (#closed edge chains) = 1. -/
theorem vertex_minus_edge (μ : ℝ) (h0 : 0 ≤ μ) (h1 : μ < 1) (n : ℝ) (ns : List ℝ) :
    ∃ A B : ℤ, A ≤ B ∧
      (∀ k, comp ((n :: ns).map (roundMap μ)) k = k → A < k ∧ k < B) ∧
      V (comp ((n :: ns).map (roundMap μ))) A (B - A).toNat
        - E (comp ((n :: ns).map (roundMap μ))) A (B - A).toNat = 1 := by
  set F := comp ((n :: ns).map (roundMap μ)) with hFdef
  have hS : StepOK F := comp_step _ (allStep_round μ h0 h1 (n :: ns))
  have hcomp : F = comp (ns.map (roundMap μ)) ∘ roundMap μ n := by
    funext k; simp [hFdef, comp, List.map]
  have hmono := StepOK.mono (comp_step _ (allStep_round μ h0 h1 ns))
  have hB : EvBelow F := by rw [hcomp]; exact evBelow_comp' (round_below n μ h0 h1) (evLe_round μ h0 h1 ns) hmono
  have hA : EvAbove F := by rw [hcomp]; exact evAbove_comp' (round_above n μ h0 h1) (evGe_round μ h0 h1 ns) hmono
  obtain ⟨Mb, hMb⟩ := hB; obtain ⟨Ma, hMa⟩ := hA
  set A := min Ma Mb with hAd
  set B := max Mb Ma with hBd
  have hA' : A < F A := hMa A (min_le_left _ _)
  have hB' : F B < B := hMb B (le_max_left _ _)
  refine ⟨A, B, le_trans (min_le_right _ _) (le_max_left _ _), fun k hk => fix_outside F hS A B hA' hB' k hk,
    count_identity F hS A B (le_trans (min_le_right _ _) (le_max_left _ _)) hA' hB'⟩

#print axioms step_round
#print axioms StepOK.mono
#print axioms StepOK.comp
#print axioms comp_step
#print axioms edgeOK_iff
#print axioms edge_closed_iff
#print axioms VE_step
#print axioms count_identity
#print axioms fix_outside
#print axioms evBelow_comp
#print axioms evAbove_comp
#print axioms round_below
#print axioms round_above
#print axioms evLe_comp
#print axioms evGe_comp
#print axioms evBelow_comp'
#print axioms evAbove_comp'
#print axioms allStep_round
#print axioms evLe_round
#print axioms evGe_round
#print axioms vertex_minus_edge

end Bgs.LineF
