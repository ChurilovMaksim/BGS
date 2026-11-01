import Bgs.LineLLineOrth

/-!
# BGS-TRACE-254 / BGS-TRACE-259 — collision form, level-`h` Parseval, and the `C_𝔮` collision closure

Sources: registry statements of `BGS-TRACE-254` (Line L Theorem U) and `BGS-TRACE-259` (Lemma A1, collision form).
Generic finite model: the frequencies `n` range over a finite set `s` of an additive group `N` (for the claims
`N = ℤ^k`, `s ⊇ supp w`), `w : N → ℂ` vanishes off `s`, `f : N →+ M` is the (reduced) embedding `n ↦ α_n`,
`A(u) = ∑_{f n = u} w(n)` and the autocorrelation is `R(v) = ∑_n w(n) conj w(n − v)` (BGS-TRACE-206).

* `collision_form` : `∑_u |A(u)|² = ∑_{v ∈ s − s, f v = 0} R(v)` (exact for any target finset of `u` containing `f(s)`);
* `R_zero` : `R(0) = ∑_n |w(n)|²`;
* `theoremU_consequence` : if `R(v) = 0` at every collision `v ≠ 0`, `f v = 0`, then `∑_u |A(u)|² = ∑_n |w(n)|²`;
* `parseval_level` : for odd `h` (`2` a unit in `ℤ/h`), `∑_{β ∈ O/h} |Ẑ_β|² = h² ∑_{x∈O/h} |A(x)|²`, with
  `Ẑ_β = ∑_x A(x) e(Tr(βx)/h)` on `O/h = (ℤ/h)²`, `Tr((a + b√2)(c + d√2)) = 2(ac + 2bd)`;
* `theoremU_level` : under the vanishing of `R` at every collision mod `h` and `∑|w|² = 1`:
  `∑_x |A(x)|² = 1` and `∑_β |Ẑ_β|² = h²` — the two displayed consequences of Theorem U;
* `Cq_collision` / `Cq_collision_exact` (BGS-TRACE-259) : `∑_u |A(u + 𝔮)|² = ∑|w|² + ∑_{v≠0, α_v ∈ 𝔮} R(v)`, and when the
  exact collisions `α_v = 0`, `v ≠ 0` have `R(v) = 0`, the sum runs over `α_v ∈ 𝔮 ∖ 0`; hence with `∑|w|² = 1`,
  `C_𝔮 = 1 + ∑_{α_v ∈ 𝔮∖0} R(v) − |Z|²/q`.

**Partial coverage:** Theorem U itself — the vanishing of `R(v)` (Lemma U1 `R(v) = e(ν₀P(v)/2h) ∏ κ(v_j, θ_j)` and the
Bessel/Neumann addition theorem making `κ` vanish) and `∑_n |ĝ(n)|² = 1` (`∑ J_n(1.8)² = 1`) — is **not** formalized;
it enters as the hypotheses above.  The infinite-support version is reduced to a finite support set `s`.
All proofs are kernel-checked.
-/

namespace Bgs.LineLCollisionForm

open Finset ComplexConjugate
open scoped Pointwise

variable {N M : Type*} [AddCommGroup N] [DecidableEq N] [AddCommGroup M] [DecidableEq M]

/-- `A(u) = ∑_{n ∈ s, f n = u} w(n)`. -/
noncomputable def Aw (s : Finset N) (w : N → ℂ) (f : N →+ M) (u : M) : ℂ := ∑ n ∈ s.filter (fun n => f n = u), w n

/-- `R(v) = ∑_n w(n) conj w(n − v)`. -/
noncomputable def R (s : Finset N) (w : N → ℂ) (v : N) : ℂ := ∑ n ∈ s, w n * conj (w (n - v))

omit [DecidableEq N] in
theorem R_zero (s : Finset N) (w : N → ℂ) : R s w 0 = ((∑ n ∈ s, ‖w n‖ ^ 2 : ℝ) : ℂ) := by
  unfold R; push_cast
  refine sum_congr rfl (fun n _ => ?_)
  rw [sub_zero, Complex.mul_conj']

theorem inner_reindex (s : Finset N) (w : N → ℂ) (hw : ∀ n ∉ s, w n = 0) (f : N →+ M) (n : N) (hn : n ∈ s) :
    ∑ v ∈ (s - s).filter (fun v => f v = 0), conj (w (n - v))
      = ∑ n' ∈ s.filter (fun n' => f n' = f n), conj (w n') := by
  rw [← sum_filter_of_ne (p := fun v => n - v ∈ s)]
  · rw [filter_filter]
    refine sum_nbij' (fun v => n - v) (fun n' => n - n') (fun v hv => ?_) (fun n' hn' => ?_)
      (fun v _ => sub_sub_cancel n v) (fun n' _ => sub_sub_cancel n n') (fun v _ => rfl)
    · simp only [mem_filter] at hv ⊢
      refine ⟨hv.2.2, ?_⟩
      rw [map_sub, hv.2.1, sub_zero]
    · simp only [mem_filter] at hn' ⊢
      exact ⟨sub_mem_sub hn hn'.1, by rw [map_sub, hn'.2, sub_self], by rw [sub_sub_cancel]; exact hn'.1⟩
  · intro v _ hne
    by_contra hc
    exact hne (by rw [hw _ hc, map_zero])

/-- **Collision form:** `∑_u |A(u)|² = ∑_{v ∈ s−s, f v = 0} R(v)`. -/
theorem collision_form (s : Finset N) (w : N → ℂ) (hw : ∀ n ∉ s, w n = 0) (f : N →+ M) (t : Finset M)
    (ht : ∀ n ∈ s, f n ∈ t) :
    ((∑ u ∈ t, ‖Aw s w f u‖ ^ 2 : ℝ) : ℂ) = ∑ v ∈ (s - s).filter (fun v => f v = 0), R s w v := by
  push_cast
  have h1 : ∀ u ∈ t, ((‖Aw s w f u‖ : ℝ) : ℂ) ^ 2
      = ∑ n ∈ s.filter (fun n => f n = u), w n * ∑ n' ∈ s.filter (fun n' => f n' = f n), conj (w n') := by
    intro u _
    rw [← Complex.mul_conj', Aw, map_sum, sum_mul]
    refine sum_congr rfl (fun n hn => ?_)
    rw [(mem_filter.mp hn).2]
  rw [sum_congr rfl h1, sum_fiberwise_of_maps_to ht (fun n => w n * ∑ n' ∈ s.filter (fun n' => f n' = f n), conj (w n'))]
  unfold R
  rw [sum_comm]
  refine sum_congr rfl (fun n hn => ?_)
  rw [← mul_sum, inner_reindex s w hw f n hn]

theorem zero_mem_sub (s : Finset N) (hs : s.Nonempty) : (0 : N) ∈ s - s := by
  obtain ⟨n, hn⟩ := hs
  have := sub_mem_sub hn hn
  rwa [sub_self] at this

/-- Collision form with the diagonal split off. -/
theorem collision_split (s : Finset N) (hs : s.Nonempty) (w : N → ℂ) (hw : ∀ n ∉ s, w n = 0) (f : N →+ M)
    (t : Finset M) (ht : ∀ n ∈ s, f n ∈ t) :
    ((∑ u ∈ t, ‖Aw s w f u‖ ^ 2 : ℝ) : ℂ)
      = ((∑ n ∈ s, ‖w n‖ ^ 2 : ℝ) : ℂ) + ∑ v ∈ ((s - s).filter (fun v => f v = 0)).erase 0, R s w v := by
  rw [collision_form s w hw f t ht, ← add_sum_erase _ _ (mem_filter.mpr ⟨zero_mem_sub s hs, map_zero f⟩), R_zero]

/-- **Theorem U consequence (any level):** vanishing of `R` at every collision `v ≠ 0` gives `∑|A|² = ∑|w|²`. -/
theorem theoremU_consequence (s : Finset N) (hs : s.Nonempty) (w : N → ℂ) (hw : ∀ n ∉ s, w n = 0) (f : N →+ M)
    (t : Finset M) (ht : ∀ n ∈ s, f n ∈ t) (hR : ∀ v ∈ s - s, v ≠ 0 → f v = 0 → R s w v = 0) :
    ∑ u ∈ t, ‖Aw s w f u‖ ^ 2 = ∑ n ∈ s, ‖w n‖ ^ 2 := by
  have h := collision_split s hs w hw f t ht
  have hz : ∑ v ∈ ((s - s).filter (fun v => f v = 0)).erase 0, R s w v = 0 := sum_eq_zero (fun v hv => by
    obtain ⟨hv0, hv⟩ := mem_erase.mp hv
    exact hR v (mem_filter.mp hv).1 hv0 (mem_filter.mp hv).2)
  rw [hz, add_zero] at h
  exact_mod_cast h

/-! ### Parseval on `O/h = (ℤ/h)²`, `h` odd -/

section level

variable {h : ℕ} [NeZero h]

local notation "ψh" => (ZMod.stdAddChar : AddChar (ZMod h) ℂ)

/-- `Tr((a + b√2)(c + d√2)) = 2(ac + 2bd)` on `O/h`. -/
def trmul (β x : ZMod h × ZMod h) : ZMod h := 2 * (β.1 * x.1 + 2 * (β.2 * x.2))

noncomputable def Zhat (A : ZMod h × ZMod h → ℂ) (β : ZMod h × ZMod h) : ℂ := ∑ x, A x * ψh (trmul β x)

theorem orth (h2 : IsUnit (2 : ZMod h)) (z : ZMod h × ZMod h) :
    ∑ β : ZMod h × ZMod h, ψh (trmul β z) = if z = 0 then ((h : ℂ) ^ 2) else 0 := by
  have hp := ZMod.isPrimitive_stdAddChar h
  have hsplit : ∑ β : ZMod h × ZMod h, ψh (trmul β z)
      = (∑ a : ZMod h, ψh (a * (2 * z.1))) * ∑ b : ZMod h, ψh (b * (4 * z.2)) := by
    rw [Fintype.sum_prod_type, sum_mul_sum]
    refine sum_congr rfl (fun a _ => sum_congr rfl (fun b _ => ?_))
    rw [← AddChar.map_add_eq_mul]; unfold trmul; congr 1; ring
  rw [hsplit, AddChar.sum_mulShift _ hp, AddChar.sum_mulShift _ hp, ZMod.card]
  have h4 : IsUnit (4 : ZMod h) := by
    have : (4 : ZMod h) = 2 * 2 := by norm_num
    rw [this]; exact h2.mul h2
  by_cases hz : z = 0
  · simp [hz, sq]
  · have : 2 * z.1 ≠ 0 ∨ 4 * z.2 ≠ 0 := by
      by_contra hc
      push Not at hc
      apply hz
      exact Prod.ext ((h2.mul_right_eq_zero).mp hc.1) ((h4.mul_right_eq_zero).mp hc.2)
    rcases this with h' | h' <;> simp [h', hz]

/-- **Parseval on `O/h`:** `∑_β |Ẑ_β|² = h² ∑_x |A(x)|²` (`h` odd). -/
theorem parseval_level (h2 : IsUnit (2 : ZMod h)) (A : ZMod h × ZMod h → ℂ) :
    ∑ β, ‖Zhat A β‖ ^ 2 = (h : ℝ) ^ 2 * ∑ x, ‖A x‖ ^ 2 := by
  have key : ((∑ β, ‖Zhat A β‖ ^ 2 : ℝ) : ℂ) = (((h : ℝ) ^ 2 * ∑ x, ‖A x‖ ^ 2 : ℝ) : ℂ) := by
    push_cast
    simp_rw [← Complex.mul_conj']
    unfold Zhat
    simp_rw [map_sum, map_mul, sum_mul_sum]
    have hr : ∀ β x y : ZMod h × ZMod h, A x * ψh (trmul β x) * (conj (A y) * conj (ψh (trmul β y)))
        = A x * conj (A y) * ψh (trmul β (x - y)) := by
      intro β x y
      rw [← AddChar.map_neg_eq_conj, mul_mul_mul_comm, ← AddChar.map_add_eq_mul]
      unfold trmul; congr 2; simp only [Prod.fst_sub, Prod.snd_sub]; ring
    simp_rw [hr]
    rw [sum_comm, mul_sum]
    refine sum_congr rfl (fun x _ => ?_)
    rw [sum_comm]
    simp_rw [← mul_sum, orth h2, sub_eq_zero]
    simp only [mul_ite, mul_zero, sum_ite_eq, mem_univ, if_true]
    rw [Complex.mul_conj']; ring
  exact_mod_cast key

/-- **Theorem U, displayed consequences:** `∑_x |A(x)|² = 1` and `∑_β |Ẑ_β|² = h²`. -/
theorem theoremU_level (h2 : IsUnit (2 : ZMod h)) (s : Finset N) (hs : s.Nonempty) (w : N → ℂ)
    (hw : ∀ n ∉ s, w n = 0) (f : N →+ ZMod h × ZMod h)
    (hR : ∀ v ∈ s - s, v ≠ 0 → f v = 0 → R s w v = 0) (hnorm : ∑ n ∈ s, ‖w n‖ ^ 2 = 1) :
    ∑ x, ‖Aw s w f x‖ ^ 2 = 1 ∧ ∑ β, ‖Zhat (Aw s w f) β‖ ^ 2 = (h : ℝ) ^ 2 := by
  have h1 : ∑ x, ‖Aw s w f x‖ ^ 2 = 1 := by
    rw [theoremU_consequence s hs w hw f univ (fun _ _ => mem_univ _) hR, hnorm]
  exact ⟨h1, by rw [parseval_level h2, h1, mul_one]⟩

end level

/-! ### BGS-TRACE-259: `C_𝔮` in collision form -/

section Cq

variable {q : ℕ} [Fact q.Prime]

open Bgs.LineLLineOrth

/-- `φ_s` as an additive map `O/q → O/𝔮 ≅ 𝔽_q`. -/
def phiHom (s : ZMod q) : ZMod q × ZMod q →+ ZMod q where
  toFun := φ s
  map_zero' := by unfold φ; simp
  map_add' x y := by unfold φ; simp only [Prod.fst_add, Prod.snd_add]; ring

omit [DecidableEq N] in
/-- The coset sums of `A = Aw` are the fibre sums of `φ_s ∘ g`. -/
theorem Acoset_Aw (S : Finset N) (w : N → ℂ) (g : N →+ ZMod q × ZMod q) (s u : ZMod q) :
    Acoset (Aw S w g) s u = Aw S w ((phiHom s).comp g) u := by
  unfold Acoset Aw
  have hmaps : ∀ n ∈ S.filter (fun n => (phiHom s).comp g n = u), g n ∈ univ.filter (fun x => φ s x = u) := by
    intro n hn
    simp only [mem_filter, mem_univ, true_and] at hn ⊢
    exact hn.2
  rw [← sum_fiberwise_of_maps_to hmaps]
  refine sum_congr rfl (fun x hx => ?_)
  rw [filter_filter]
  refine sum_congr (filter_congr (fun n _ => ?_)) (fun _ _ => rfl)
  have hx' : φ s x = u := (mem_filter.mp hx).2
  constructor
  · intro h; exact ⟨by show φ s (g n) = u; rw [h]; exact hx', h⟩
  · intro h; exact h.2

/-- **Lemma A1, collision form:** `∑_u |A(u + 𝔮)|² = ∑|w|² + ∑_{v ≠ 0, α_v ∈ 𝔮} R(v)`. -/
theorem Cq_collision (S : Finset N) (hS : S.Nonempty) (w : N → ℂ) (hw : ∀ n ∉ S, w n = 0)
    (g : N →+ ZMod q × ZMod q) (s : ZMod q) :
    ((∑ u : ZMod q, ‖Acoset (Aw S w g) s u‖ ^ 2 : ℝ) : ℂ)
      = ((∑ n ∈ S, ‖w n‖ ^ 2 : ℝ) : ℂ) + ∑ v ∈ ((S - S).filter (fun v => φ s (g v) = 0)).erase 0, R S w v := by
  simp_rw [Acoset_Aw]
  exact collision_split S hS w hw ((phiHom s).comp g) univ (fun _ _ => mem_univ _)

/-- With `α : N →+ O` and `g = red ∘ α`: if the exact collisions (`α_v = 0`, `v ≠ 0`) have `R(v) = 0`, then
`C_𝔮 = ∑|w|² + ∑_{α_v ∈ 𝔮 ∖ 0} R(v) − |Z|²/q`; with `∑|w|² = 1` this is `1 + ∑_{α_v∈𝔮∖0} R(v) − |Z|²/q`. -/
theorem Cq_collision_exact {P : Type*} [AddCommGroup P] [DecidableEq P] (S : Finset N) (hS : S.Nonempty)
    (w : N → ℂ) (hw : ∀ n ∉ S, w n = 0) (α : N →+ P) (red : P →+ ZMod q × ZMod q) (s : ZMod q)
    (hexact : ∀ v ∈ S - S, v ≠ 0 → α v = 0 → R S w v = 0) (hnorm : ∑ n ∈ S, ‖w n‖ ^ 2 = 1) :
    ((∑ u : ZMod q, ‖Acoset (Aw S w (red.comp α)) s u‖ ^ 2 - ‖Zhat (Aw S w (red.comp α)) 0‖ ^ 2 / q : ℝ) : ℂ)
      = 1 + ∑ v ∈ (S - S).filter (fun v => φ s (red (α v)) = 0 ∧ α v ≠ 0), R S w v
          - ((‖Zhat (Aw S w (red.comp α)) 0‖ ^ 2 / q : ℝ) : ℂ) := by
  rw [Complex.ofReal_sub, Cq_collision S hS w hw (red.comp α) s, hnorm]
  congr 2
  rw [← sum_filter_of_ne (p := fun v => α v ≠ 0)]
  · rw [filter_erase, filter_filter]
    refine sum_congr ?_ (fun _ _ => rfl)
    ext v
    have key : α v ≠ 0 → v ≠ 0 := fun h h0 => h (by rw [h0, map_zero])
    simp only [mem_erase, mem_filter, AddMonoidHom.coe_comp, Function.comp_apply]
    tauto
  · intro v hv hne
    by_contra hc
    have hc' : α v = 0 := hc
    obtain ⟨hv0, hv⟩ := mem_erase.mp hv
    exact hne (hexact v (mem_filter.mp hv).1 hv0 hc')

end Cq

end Bgs.LineLCollisionForm
