module
public import Mathlib
@[expose] public section

/-!
# Local jet obstruction to a purely fixed-point proof of resonance nondegeneracy
(BGS-RES-002, `mathematics/resonance-cohomology/local_jet_resonance_obstruction.md`)

Let `S(u,z) = (λu, λ⁻¹z)` with `λ > 1`, `a = √((λ² + λ⁻²)/2)` and
`G(u,z) = (u² − z² + a u z)² + u² z²`.  The Poisson bracket is
`{f,h} = f_u h_z − f_z h_u` (the convention of the resonance notes).

* `Gfun_nonneg`, `Gfun_eq_zero_iff`: `G ≥ 0`, and `G = 0` only at the origin
  (strict isolated minimum).
* `bracket_expansion`: `{G, G∘S}` is the explicit homogeneous sextic
  `∑_r c_r u^r z^{6-r}` (for an arbitrary real parameter `a`).
* `bracket_coeff_three`: the resonant coefficient is
  `c₃ = 16(λ² − λ⁻²)(2a² − λ² − λ⁻²)`; it vanishes exactly when
  `a² = (λ² + λ⁻²)/2` (relation (2)).
* `monomial_coboundary`: `V ↦ V − V∘S` multiplies `u^r z^s` by `1 − λ^{r−s}`.
* `bracket_is_coboundary`: with relation (2), `{G, G∘S} = V − V∘S` for the explicit
  polynomial `V = ∑_{r ≠ 3} c_r/(1 − λ^{2r−6}) u^r z^{6−r}`.
* `bracket_ne_zero`: the bracket is not identically zero; its `u⁶` coefficient is
  `8a(λ² − λ⁴) ≠ 0` (formula (3)).
* `project_a`: for `λ = 3 + 2√2`, `a = √17`.
-/

open Real

namespace Bgs.Mathlib

namespace LocalJet

/-- The local observable `G(u,z) = (u² − z² + a u z)² + u² z²`. -/
noncomputable def Gfun (a u z : ℝ) : ℝ := (u ^ 2 - z ^ 2 + a * u * z) ^ 2 + u ^ 2 * z ^ 2

/-- Its composition with the hyperbolic linear map `S(u,z) = (λu, λ⁻¹z)`. -/
noncomputable def GS (a L u z : ℝ) : ℝ := Gfun a (L * u) (z / L)

/-- The Poisson bracket `{f,h} = f_u h_z − f_z h_u` of two functions of `(u,z)`. -/
noncomputable def pbracket (f h : ℝ → ℝ → ℝ) (u z : ℝ) : ℝ :=
  deriv (fun t => f t z) u * deriv (fun t => h u t) z
    - deriv (fun t => f u t) z * deriv (fun t => h t z) u

/-- `∂G/∂u`. -/
noncomputable def Gu (a u z : ℝ) : ℝ :=
  4 * u ^ 3 + 6 * a * u ^ 2 * z + 2 * (a ^ 2 - 1) * u * z ^ 2 - 2 * a * z ^ 3

/-- `∂G/∂z`. -/
noncomputable def Gz (a u z : ℝ) : ℝ :=
  2 * a * u ^ 3 + 2 * (a ^ 2 - 1) * u ^ 2 * z - 6 * a * u * z ^ 2 + 4 * z ^ 3

lemma Gfun_expand (a u z : ℝ) :
    Gfun a u z = u ^ 4 + 2 * a * z * u ^ 3 + (a ^ 2 - 1) * z ^ 2 * u ^ 2
      - 2 * a * z ^ 3 * u + z ^ 4 := by
  unfold Gfun; ring

lemma hasDerivAt_Gu (a u z : ℝ) : HasDerivAt (fun t => Gfun a t z) (Gu a u z) u := by
  have h := ((((hasDerivAt_pow 4 u).add ((hasDerivAt_pow 3 u).const_mul (2 * a * z))).add
    ((hasDerivAt_pow 2 u).const_mul ((a ^ 2 - 1) * z ^ 2))).sub
    ((hasDerivAt_id u).const_mul (2 * a * z ^ 3))).add_const (z ^ 4)
  convert! h using 1
  · funext t; rw [Gfun_expand]; simp
  · simp [Gu]; ring

lemma hasDerivAt_Gz (a u z : ℝ) : HasDerivAt (fun t => Gfun a u t) (Gz a u z) z := by
  have e : ∀ t, Gfun a u t = t ^ 4 - 2 * a * u * t ^ 3 + (a ^ 2 - 1) * u ^ 2 * t ^ 2
      + 2 * a * u ^ 3 * t + u ^ 4 := fun t => by unfold Gfun; ring
  have h := ((((hasDerivAt_pow 4 z).sub ((hasDerivAt_pow 3 z).const_mul (2 * a * u))).add
    ((hasDerivAt_pow 2 z).const_mul ((a ^ 2 - 1) * u ^ 2))).add
    ((hasDerivAt_id z).const_mul (2 * a * u ^ 3))).add_const (u ^ 4)
  convert! h using 1
  · funext t; rw [e]; simp
  · simp [Gz]; ring

lemma deriv_Gu (a u z : ℝ) : deriv (fun t => Gfun a t z) u = Gu a u z :=
  (hasDerivAt_Gu a u z).deriv

lemma deriv_Gz (a u z : ℝ) : deriv (fun t => Gfun a u t) z = Gz a u z :=
  (hasDerivAt_Gz a u z).deriv

lemma deriv_GSu (a L u z : ℝ) : deriv (fun t => GS a L t z) u = L * Gu a (L * u) (z / L) := by
  have h := (hasDerivAt_Gu a (L * u) (z / L)).comp u ((hasDerivAt_id u).const_mul L)
  simp only [mul_one] at h
  rw [show (fun t => GS a L t z) = (fun t => Gfun a t (z / L)) ∘ (HMul.hMul L) from rfl,
    h.deriv]
  ring

lemma deriv_GSz (a L u z : ℝ) :
    deriv (fun t => GS a L u t) z = L⁻¹ * Gz a (L * u) (z / L) := by
  have h := (hasDerivAt_Gz a (L * u) (z / L)).comp z ((hasDerivAt_id z).div_const L)
  rw [show (fun t => GS a L u t) = (fun t => Gfun a (L * u) t) ∘ (fun t => id t / L) from rfl,
    h.deriv]
  simp; ring

/-! ## Positivity and the strict minimum -/

theorem Gfun_nonneg (a u z : ℝ) : 0 ≤ Gfun a u z := by unfold Gfun; positivity

theorem Gfun_eq_zero_iff (a u z : ℝ) : Gfun a u z = 0 ↔ u = 0 ∧ z = 0 := by
  constructor
  · intro h
    unfold Gfun at h
    have h1 : (u ^ 2 - z ^ 2 + a * u * z) ^ 2 = 0 := by nlinarith [sq_nonneg (u * z)]
    have h2 : u * z = 0 := by nlinarith [sq_nonneg (u ^ 2 - z ^ 2 + a * u * z)]
    have h3 : u ^ 2 - z ^ 2 + a * u * z = 0 := pow_eq_zero_iff (n := 2) (by norm_num) |>.1 h1
    rcases mul_eq_zero.1 h2 with hu | hz
    · subst hu; refine ⟨rfl, ?_⟩; nlinarith
    · subst hz; refine ⟨?_, rfl⟩; nlinarith
  · rintro ⟨rfl, rfl⟩; simp [Gfun]

/-! ## The bracket as an explicit sextic -/

/-- Coefficient of `u^r z^{6−r}` in `{G, G∘S}` (here `L = λ`). -/
noncomputable def coeff (a L : ℝ) : ℕ → ℝ
  | 0 => 8 * a * (L⁻¹ ^ 2 - L⁻¹ ^ 4)
  | 1 => 8 * (1 - a ^ 2) * (1 - L⁻¹ ^ 4)
  | 2 => 8 * a * (3 * L⁻¹ ^ 4 + L⁻¹ ^ 2 - 1 - 3 * L ^ 2) + 8 * a ^ 3 * (1 - L⁻¹ ^ 2)
  | 3 => 16 * (L ^ 2 - L⁻¹ ^ 2) * (2 * a ^ 2 - L ^ 2 - L⁻¹ ^ 2)
  | 4 => 8 * a * (-3 * L⁻¹ ^ 2 - 1 + L ^ 2 + 3 * L ^ 4) + 8 * a ^ 3 * (1 - L ^ 2)
  | 5 => 8 * (1 - a ^ 2) * (L ^ 4 - 1)
  | 6 => 8 * a * (L ^ 2 - L ^ 4)
  | _ => 0

theorem bracket_expansion (a : ℝ) {L : ℝ} (hL : L ≠ 0) (u z : ℝ) :
    pbracket (Gfun a) (GS a L) u z = ∑ r ∈ Finset.range 7, coeff a L r * u ^ r * z ^ (6 - r) := by
  unfold pbracket
  rw [deriv_Gu, deriv_Gz, deriv_GSu, deriv_GSz]
  simp only [Finset.sum_range_succ, Finset.sum_range_zero, coeff, Gu, Gz]
  field_simp
  ring

/-- The resonant coefficient `c₃` vanishes exactly under relation (2). -/
theorem bracket_coeff_three {a L : ℝ} (hL : 1 < L) :
    coeff a L 3 = 0 ↔ a ^ 2 = (L ^ 2 + L⁻¹ ^ 2) / 2 := by
  have hL0 : 0 < L := by linarith
  have hne : L ^ 2 - L⁻¹ ^ 2 ≠ 0 := by
    have : L⁻¹ < L := by
      rw [inv_lt_comm₀ hL0 hL0]; exact lt_of_lt_of_le (inv_lt_one_of_one_lt₀ hL) hL.le
    have : L⁻¹ ^ 2 < L ^ 2 := pow_lt_pow_left₀ this (by positivity) (by norm_num)
    linarith
  simp only [coeff, mul_eq_zero, hne, false_or, OfNat.ofNat_ne_zero]
  constructor <;> intro h <;> linarith

/-- The cohomological operator `V ↦ V − V∘S` acts on monomials by `1 − λ^{r−s}`. -/
theorem monomial_coboundary {L : ℝ} (hL : L ≠ 0) (r s : ℕ) (u z : ℝ) :
    u ^ r * z ^ s - (L * u) ^ r * (z / L) ^ s = (1 - L ^ ((r : ℤ) - s)) * (u ^ r * z ^ s) := by
  rw [zpow_sub₀ hL, zpow_natCast, zpow_natCast, mul_pow, div_pow]
  field_simp

/-- The explicit transfer polynomial `V = ∑_{r≠3} c_r/(1 − λ^{2r−6}) u^r z^{6−r}`. -/
noncomputable def transferV (a L u z : ℝ) : ℝ :=
  ∑ r ∈ (Finset.range 7).erase 3,
    coeff a L r / (1 - L ^ ((r : ℤ) - (6 - r : ℕ))) * (u ^ r * z ^ (6 - r))

/-- **BGS-RES-002.** Under relation (2), the bracket `{G, G∘S}` is the polynomial
coboundary `V − V∘S`. -/
theorem bracket_is_coboundary {a L : ℝ} (hL : 1 < L) (ha : a ^ 2 = (L ^ 2 + L⁻¹ ^ 2) / 2)
    (u z : ℝ) :
    pbracket (Gfun a) (GS a L) u z = transferV a L u z - transferV a L (L * u) (z / L) := by
  have hL0 : L ≠ 0 := by positivity
  have h3 : coeff a L 3 = 0 := (bracket_coeff_three hL).2 ha
  have hden : ∀ r ∈ (Finset.range 7).erase 3, (1 - L ^ ((r : ℤ) - (6 - r : ℕ))) ≠ 0 := by
    intro r hr
    simp only [Finset.mem_erase, Finset.mem_range] at hr
    intro h
    have h1 : L ^ ((r : ℤ) - (6 - r : ℕ)) = 1 := by linarith
    have hexp : ((r : ℤ) - (6 - r : ℕ)) ≠ 0 := by omega
    exact hexp ((zpow_eq_one_iff_right₀ (by linarith) hL.ne').1 h1)
  rw [bracket_expansion a hL0, transferV, transferV, ← Finset.sum_sub_distrib]
  rw [← Finset.add_sum_erase _ _ (show 3 ∈ Finset.range 7 by simp), h3, zero_mul, zero_mul,
    zero_add]
  refine Finset.sum_congr rfl fun r hr => ?_
  rw [← mul_sub, monomial_coboundary hL0, ← mul_assoc, div_mul_cancel₀ _ (hden r hr)]
  ring

/-- The bracket is not identically zero: its value at `(1,0)` is the `u⁶` coefficient
`8a(λ² − λ⁴)`, which is nonzero for `a ≠ 0`, `λ > 1` (formula (3)). -/
theorem bracket_ne_zero {a L : ℝ} (hL : 1 < L) (ha : a ≠ 0) :
    pbracket (Gfun a) (GS a L) 1 0 = 8 * a * (L ^ 2 - L ^ 4) ∧
      pbracket (Gfun a) (GS a L) 1 0 ≠ 0 := by
  have hL0 : L ≠ 0 := by positivity
  have hv : pbracket (Gfun a) (GS a L) 1 0 = 8 * a * (L ^ 2 - L ^ 4) := by
    rw [bracket_expansion a hL0]
    simp [Finset.sum_range_succ, coeff]
  refine ⟨hv, ?_⟩
  rw [hv]
  have : L ^ 2 < L ^ 4 := pow_lt_pow_right₀ hL (by norm_num)
  have : L ^ 2 - L ^ 4 ≠ 0 := by linarith
  exact mul_ne_zero (mul_ne_zero (by norm_num) ha) this

/-- The parameter `a = √((λ² + λ⁻²)/2)` is positive, so `bracket_ne_zero` applies. -/
theorem a_pos {L : ℝ} (hL : 1 < L) : 0 < Real.sqrt ((L ^ 2 + L⁻¹ ^ 2) / 2) :=
  Real.sqrt_pos.2 (by have : 0 < L := by linarith
                      positivity)

/-- For the project eigenvalue `λ = 3 + 2√2` one has `a = √17`. -/
theorem project_a : Real.sqrt (((3 + 2 * √2) ^ 2 + (3 + 2 * √2)⁻¹ ^ 2) / 2) = √17 := by
  have h2 : (√2) ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  have hinv : (3 + 2 * √2)⁻¹ = 3 - 2 * √2 := by
    apply inv_eq_of_mul_eq_one_right
    nlinarith
  rw [hinv]
  congr 1
  nlinarith

end LocalJet

end Bgs.Mathlib
