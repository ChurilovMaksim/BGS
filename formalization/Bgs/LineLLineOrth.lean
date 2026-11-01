import Mathlib.Analysis.SpecialFunctions.Complex.CircleAddChar
import Mathlib.NumberTheory.LegendreSymbol.AddCharacter
import Mathlib.Algebra.Order.Chebyshev
import Mathlib.Topology.Algebra.InfiniteSum.Ring

/-!
# BGS-TRACE-259 (Lemma A1) and BGS-TRACE-267 (Lemma Q) — orthogonality on the isotropic line `ℓ(𝔮)`

Source: `mathematics/fixed-map/lineL_op_open_range.md` §6–§8; registry boundaries of `BGS-TRACE-255`, `259`, `267`.

**Model.** `q` an odd prime, split in `O = ℤ[√2]`: `s ∈ 𝔽_q` with `s² = 2`.  `O/q` is modelled as `𝔽_q × 𝔽_q`
(`(a, b) ↔ a + b√2`), so `Tr(γβ) = 2(γ₁β₁ + 2γ₂β₂)` (`trmul`).  The degree-one prime `𝔮 = (q, √2 − s)…` is the kernel of
`φ(a, b) = a + s b` (`𝔮 mod q = {φ = 0}`, `O/𝔮 ≅ 𝔽_q` via `φ`), and `ℓ(𝔮) ⊂ O/q` is its annihilator under
`(β, x) ↦ e(Tr(βx)/q)` (`ell`, defined literally as the annihilator).  `ψ = ZMod.stdAddChar`, `ψ(t) = e(t/q)`.

* `mem_ell_iff` : `β ∈ ℓ(𝔮) ⇔ 2β₂ = sβ₁`, and `sum_ell` : `ℓ(𝔮)` is the line `{(c, cs/2)}` (`q` points);
* `line_orth` : `(1/q) ∑_{β∈ℓ(𝔮)} e(Tr(γβ)/q) = 1[γ ∈ 𝔮]`;
* **Lemma Q** `lemmaQ` : for **absolutely summable** `c : O → ℂ` (`O = ℤ × ℤ`) and `F(β/q) = ∑_γ c_γ e(Tr(γβ)/q)`,
  `(1/q) ∑_{β∈ℓ(𝔮)} F(β/q) = ∑_{γ∈𝔮} c_γ`; `norm_dvd_of_mem` : `γ ∈ 𝔮 ⇒ q ∣ Nm γ = a² − 2b²`;
* **Lemma A1** `lemmaA1_parseval` : with `Ẑ_β = ∑_x A(x) e(Tr(βx)/q)` (`A` on `O/q`),
  `∑_{β∈ℓ(𝔮)} |Ẑ_β|² = q ∑_{u∈O/𝔮} |A(u + 𝔮)|²`; `lemmaA1_CS` : with `D_𝔮 = (1/q)∑_{β∈ℓ(𝔮)∖0} Ẑ_β`, `Z = Ẑ_0`,
  `|D_𝔮|² ≤ (1 − 1/q) C_𝔮`, `C_𝔮 = ∑_u |A(u + 𝔮)|² − |Z|²/q`.

The identities hold for any `s`; `s² = 2` is what makes `𝔮` the degree-one prime above `q` (it is used in `norm_dvd_of_mem`).

**Partial coverage.**  `A` is taken on `O/q` (the reduction of the finitely supported `A` on `O`); the collision form
`C_𝔮 = 1 + ∑_{α_v∈𝔮∖0} R(v) − |Z|²/q` (which uses Theorem U, BGS-TRACE-254) is **not** formalized for TRACE-259.  For TRACE-267,
the step "average = c₀ when no frequency `γ ≠ 0` has `|Nm γ| ≥ q`" is covered only through `q ∣ Nm γ` (the nonvanishing
`Nm γ ≠ 0` for `γ ≠ 0` is not formalized), and the block-energy use for `F = f_k` (interval `[I_k − T_k(q), I_k + T_k(q)]`) is
**not** formalized.  All proofs are kernel-checked.
-/

namespace Bgs.LineLLineOrth

open Finset ComplexConjugate

variable {q : ℕ} [hq : Fact q.Prime]

/-- `ψ(t) = e(t/q)`. -/
noncomputable abbrev ψ : AddChar (ZMod q) ℂ := ZMod.stdAddChar

/-- `Tr(γβ)` for `γ = γ₁ + γ₂√2`, `β = β₁ + β₂√2` modulo `q`. -/
def trmul (γ β : ZMod q × ZMod q) : ZMod q := 2 * (γ.1 * β.1 + 2 * (γ.2 * β.2))

/-- Reduction `O/q → O/𝔮 ≅ 𝔽_q`, `a + b√2 ↦ a + s b`; `𝔮 mod q = {φ = 0}`. -/
def φ (s : ZMod q) (x : ZMod q × ZMod q) : ZMod q := x.1 + s * x.2

/-- `ℓ(𝔮)`: the annihilator of `𝔮 mod q` under `(β, x) ↦ e(Tr(βx)/q)`. -/
noncomputable def ell (s : ZMod q) : Finset (ZMod q × ZMod q) :=
  univ.filter (fun β => ∀ γ : ZMod q × ZMod q, φ s γ = 0 → trmul γ β = 0)

theorem two_ne_zero' (hq2 : q ≠ 2) : (2 : ZMod q) ≠ 0 := by
  intro h
  have : ((2 : ℕ) : ZMod q) = 0 := by exact_mod_cast h
  rw [ZMod.natCast_eq_zero_iff] at this
  have := (Nat.prime_dvd_prime_iff_eq hq.out Nat.prime_two).mp this
  exact hq2 this

theorem mem_ell_iff (hq2 : q ≠ 2) (s : ZMod q) (β : ZMod q × ZMod q) :
    β ∈ ell s ↔ 2 * β.2 = s * β.1 := by
  have h2 := two_ne_zero' (q := q) hq2
  unfold ell; rw [mem_filter]
  constructor
  · rintro ⟨-, h⟩
    have := h (-s, 1) (by simp [φ])
    unfold trmul at this
    have h' : 2 * (2 * β.2 - s * β.1) = 0 := by linear_combination this
    have := (mul_eq_zero.mp h').resolve_left h2
    linear_combination this
  · intro h
    refine ⟨mem_univ _, fun γ hγ => ?_⟩
    unfold φ at hγ; unfold trmul
    have : γ.1 = -s * γ.2 := by linear_combination hγ
    rw [this]; linear_combination (2 * γ.2) * h

/-- `ℓ(𝔮)` is the line `{(c, c s/2) : c ∈ 𝔽_q}`. -/
theorem sum_ell (hq2 : q ≠ 2) (s : ZMod q) (f : ZMod q × ZMod q → ℂ) :
    ∑ β ∈ ell s, f β = ∑ c : ZMod q, f (c, c * s * 2⁻¹) := by
  have h2 := two_ne_zero' (q := q) hq2
  symm
  refine sum_bij' (fun c _ => (c, c * s * 2⁻¹)) (fun β _ => β.1) (fun c _ => ?_) (fun β _ => mem_univ _)
    (fun c _ => rfl) (fun β hβ => ?_) (fun c _ => rfl)
  · rw [mem_ell_iff hq2]; field_simp
  · rw [mem_ell_iff hq2] at hβ
    ext
    · rfl
    · simp only; field_simp; linear_combination -hβ

theorem trmul_line (hq2 : q ≠ 2) (s : ZMod q) (γ : ZMod q × ZMod q) (c : ZMod q) :
    trmul γ (c, c * s * 2⁻¹) = c * (2 * φ s γ) := by
  have h2 := two_ne_zero' (q := q) hq2
  unfold trmul φ; simp only
  field_simp

theorem psi_primitive : (ψ : AddChar (ZMod q) ℂ).IsPrimitive := ZMod.isPrimitive_stdAddChar q

/-- Orthogonality on the line: `∑_{β∈ℓ(𝔮)} e(Tr(γβ)/q) = q·1[γ ∈ 𝔮]`. -/
theorem line_sum (hq2 : q ≠ 2) (s : ZMod q) (γ : ZMod q × ZMod q) :
    ∑ β ∈ ell s, (ψ : AddChar (ZMod q) ℂ) (trmul γ β) = if φ s γ = 0 then (q : ℂ) else 0 := by
  have h2 := two_ne_zero' (q := q) hq2
  rw [sum_ell hq2]
  simp_rw [trmul_line hq2 s]
  rw [AddChar.sum_mulShift _ psi_primitive, ZMod.card]
  simp [h2]

theorem line_orth (hq2 : q ≠ 2) (s : ZMod q) (γ : ZMod q × ZMod q) :
    (1 / (q : ℂ)) * ∑ β ∈ ell s, (ψ : AddChar (ZMod q) ℂ) (trmul γ β) = if φ s γ = 0 then 1 else 0 := by
  have hq0 : (q : ℂ) ≠ 0 := by exact_mod_cast hq.out.ne_zero
  rw [line_sum hq2 s]; split_ifs
  · field_simp
  · simp

/-- Reduction `O = ℤ × ℤ → O/q`. -/
def red (γ : ℤ × ℤ) : ZMod q × ZMod q := ((γ.1 : ZMod q), (γ.2 : ZMod q))

/-- **Lemma Q:** `(1/q) ∑_{β∈ℓ(𝔮)} F(β/q) = ∑_{γ∈𝔮} c_γ` for absolutely summable `c`. -/
theorem lemmaQ (hq2 : q ≠ 2) (s : ZMod q) (c : ℤ × ℤ → ℂ) (hc : Summable c) :
    (1 / (q : ℂ)) * ∑ β ∈ ell s, (∑' γ : ℤ × ℤ, c γ * (ψ : AddChar (ZMod q) ℂ) (trmul (red γ) β))
      = ∑' γ : ℤ × ℤ, (if φ s (red γ) = 0 then c γ else 0) := by
  have hsum : ∀ β ∈ ell s, Summable (fun γ : ℤ × ℤ => c γ * (ψ : AddChar (ZMod q) ℂ) (trmul (red γ) β)) := by
    intro β _
    refine Summable.of_norm_bounded hc.norm (fun γ => ?_)
    rw [norm_mul]
    have : ‖(ψ : AddChar (ZMod q) ℂ) (trmul (red γ) β)‖ = 1 := by
      rw [ZMod.stdAddChar_apply]; exact Circle.norm_coe _
    rw [this, mul_one]
  rw [← Summable.tsum_finsetSum hsum, ← tsum_mul_left]
  congr 1; funext γ
  rw [← mul_sum, ← mul_assoc, mul_comm (1 / (q : ℂ)), mul_assoc, line_orth hq2 s]
  split_ifs <;> simp

/-- `γ ∈ 𝔮 ⇒ q ∣ Nm γ = a² − 2b²`. -/
theorem norm_dvd_of_mem (s : ZMod q) (hs : s ^ 2 = 2) (γ : ℤ × ℤ) (h : φ s (red γ) = 0) :
    (q : ℤ) ∣ γ.1 ^ 2 - 2 * γ.2 ^ 2 := by
  rw [← ZMod.intCast_zmod_eq_zero_iff_dvd]
  unfold φ red at h; simp only at h
  push_cast
  have : (γ.1 : ZMod q) = -s * γ.2 := by linear_combination h
  rw [this]; linear_combination (γ.2 : ZMod q) ^ 2 * hs

variable (A : ZMod q × ZMod q → ℂ)

/-- `Ẑ_β = ∑_x A(x) e(Tr(βx)/q)`. -/
noncomputable def Zhat (β : ZMod q × ZMod q) : ℂ := ∑ x, A x * (ψ : AddChar (ZMod q) ℂ) (trmul β x)

/-- `A(u + 𝔮) = ∑_{x ≡ u mod 𝔮} A(x)`, `u ∈ O/𝔮 ≅ 𝔽_q`. -/
noncomputable def Acoset (s u : ZMod q) : ℂ := ∑ x ∈ univ.filter (fun x => φ s x = u), A x

theorem trmul_comm (γ β : ZMod q × ZMod q) : trmul γ β = trmul β γ := by unfold trmul; ring

/-- **Lemma A1 (Parseval):** `∑_{β∈ℓ(𝔮)} |Ẑ_β|² = q ∑_u |A(u + 𝔮)|²`. -/
theorem lemmaA1_parseval (hq2 : q ≠ 2) (s : ZMod q) :
    ∑ β ∈ ell s, ‖Zhat A β‖ ^ 2 = (q : ℝ) * ∑ u : ZMod q, ‖Acoset A s u‖ ^ 2 := by
  have h2 := two_ne_zero' (q := q) hq2
  -- Ẑ on the line is the DFT of the coset sums at frequency 2c
  have hZ : ∀ c : ZMod q, Zhat A (c, c * s * 2⁻¹)
      = ∑ u : ZMod q, Acoset A s u * (ψ : AddChar (ZMod q) ℂ) (u * (2 * c)) := by
    intro c
    unfold Zhat Acoset
    simp_rw [sum_mul]
    have : ∀ u : ZMod q, ∑ i ∈ univ.filter (fun x => φ s x = u), A i * (ψ : AddChar (ZMod q) ℂ) (u * (2 * c))
        = ∑ i ∈ univ.filter (fun x => φ s x = u), A i * (ψ : AddChar (ZMod q) ℂ) (φ s i * (2 * c)) := by
      intro u
      refine sum_congr rfl (fun i hi => ?_)
      rw [(mem_filter.mp hi).2]
    simp_rw [this]
    rw [sum_fiberwise univ (φ s) (fun i => A i * (ψ : AddChar (ZMod q) ℂ) (φ s i * (2 * c)))]
    refine sum_congr rfl (fun x _ => ?_)
    rw [trmul_comm, trmul_line hq2 s]; ring_nf
  -- orthogonality in c
  have horth : ∀ u u' : ZMod q,
      ∑ c : ZMod q, (ψ : AddChar (ZMod q) ℂ) (u * (2 * c)) * conj ((ψ : AddChar (ZMod q) ℂ) (u' * (2 * c)))
        = if u = u' then (q : ℂ) else 0 := by
    intro u u'
    have : ∀ c : ZMod q, (ψ : AddChar (ZMod q) ℂ) (u * (2 * c)) * conj ((ψ : AddChar (ZMod q) ℂ) (u' * (2 * c)))
        = (ψ : AddChar (ZMod q) ℂ) (c * (2 * (u - u'))) := by
      intro c
      rw [← AddChar.map_neg_eq_conj, ← AddChar.map_add_eq_mul]; congr 1; ring
    simp_rw [this]
    rw [AddChar.sum_mulShift _ psi_primitive, ZMod.card]
    by_cases h : u = u'
    · simp [h]
    · have : 2 * (u - u') ≠ 0 := mul_ne_zero h2 (sub_ne_zero.mpr h)
      simp [h, this]
  have key : ((∑ β ∈ ell s, ‖Zhat A β‖ ^ 2 : ℝ) : ℂ) = (((q : ℝ) * ∑ u : ZMod q, ‖Acoset A s u‖ ^ 2 : ℝ) : ℂ) := by
    push_cast
    simp_rw [← Complex.mul_conj']
    rw [sum_ell hq2]
    simp_rw [hZ, map_sum, map_mul, sum_mul_sum]
    have hr : ∀ (x i j : ZMod q), Acoset A s i * (ψ : AddChar (ZMod q) ℂ) (i * (2 * x))
        * (conj (Acoset A s j) * conj ((ψ : AddChar (ZMod q) ℂ) (j * (2 * x))))
        = (Acoset A s i * conj (Acoset A s j)) * ((ψ : AddChar (ZMod q) ℂ) (i * (2 * x))
            * conj ((ψ : AddChar (ZMod q) ℂ) (j * (2 * x)))) := by intros; ring
    simp_rw [hr]
    rw [sum_comm, mul_sum]
    refine sum_congr rfl (fun i _ => ?_)
    rw [sum_comm]
    simp_rw [← mul_sum, horth]
    simp only [mul_ite, mul_zero, sum_ite_eq, mem_univ, if_true]
    ring
  exact_mod_cast key

theorem zero_mem_ell (hq2 : q ≠ 2) (s : ZMod q) : (0 : ZMod q × ZMod q) ∈ ell s := by
  rw [mem_ell_iff hq2]; simp

theorem card_ell (hq2 : q ≠ 2) (s : ZMod q) : (ell s).card = q := by
  have h : ((ell s).card : ℂ) = q := by
    rw [card_eq_sum_ones, Nat.cast_sum, sum_ell hq2 s (fun _ => ((1 : ℕ) : ℂ))]
    simp [ZMod.card]
  exact_mod_cast h

/-- **Lemma A1 (Cauchy–Schwarz):** `|D_𝔮|² ≤ (1 − 1/q) C_𝔮`, `D_𝔮 = (1/q)∑_{β∈ℓ(𝔮)∖0} Ẑ_β`,
`C_𝔮 = ∑_u |A(u + 𝔮)|² − |Z|²/q`, `Z = Ẑ_0 = ∑_x A(x)`. -/
theorem lemmaA1_CS (hq2 : q ≠ 2) (s : ZMod q) :
    ‖(1 / (q : ℂ)) * ∑ β ∈ (ell s).erase 0, Zhat A β‖ ^ 2
      ≤ (1 - 1 / (q : ℝ)) * (∑ u : ZMod q, ‖Acoset A s u‖ ^ 2 - ‖Zhat A 0‖ ^ 2 / q) := by
  have hq0 : (0 : ℝ) < q := by exact_mod_cast hq.out.pos
  have hP := lemmaA1_parseval A hq2 s
  rw [← add_sum_erase _ _ (zero_mem_ell hq2 s)] at hP
  have hcard : (((ell s).erase 0).card : ℝ) = q - 1 := by
    rw [card_erase_of_mem (zero_mem_ell hq2 s), card_ell hq2 s]
    have : 1 ≤ q := hq.out.one_lt.le
    push_cast [Nat.cast_sub this]; ring
  set T := ∑ β ∈ (ell s).erase 0, ‖Zhat A β‖ ^ 2 with hT
  have hCS : (∑ β ∈ (ell s).erase 0, ‖Zhat A β‖) ^ 2 ≤ (q - 1) * T := by
    rw [← hcard]; exact sq_sum_le_card_mul_sum_sq
  have hnorm : ‖(1 / (q : ℂ)) * ∑ β ∈ (ell s).erase 0, Zhat A β‖
      ≤ (1 / (q : ℝ)) * ∑ β ∈ (ell s).erase 0, ‖Zhat A β‖ := by
    rw [norm_mul]
    have : ‖(1 / (q : ℂ))‖ = 1 / (q : ℝ) := by simp
    rw [this]
    exact mul_le_mul_of_nonneg_left (norm_sum_le _ _) (by positivity)
  have h0 : 0 ≤ ‖(1 / (q : ℂ)) * ∑ β ∈ (ell s).erase 0, Zhat A β‖ := norm_nonneg _
  calc ‖(1 / (q : ℂ)) * ∑ β ∈ (ell s).erase 0, Zhat A β‖ ^ 2
      ≤ ((1 / (q : ℝ)) * ∑ β ∈ (ell s).erase 0, ‖Zhat A β‖) ^ 2 := pow_le_pow_left₀ h0 hnorm 2
    _ = (1 / (q : ℝ)) ^ 2 * (∑ β ∈ (ell s).erase 0, ‖Zhat A β‖) ^ 2 := by ring
    _ ≤ (1 / (q : ℝ)) ^ 2 * ((q - 1) * T) := mul_le_mul_of_nonneg_left hCS (by positivity)
    _ = (1 - 1 / (q : ℝ)) * (∑ u : ZMod q, ‖Acoset A s u‖ ^ 2 - ‖Zhat A 0‖ ^ 2 / q) := by
      have hT' : T = (q : ℝ) * ∑ u : ZMod q, ‖Acoset A s u‖ ^ 2 - ‖Zhat A 0‖ ^ 2 := by linarith
      rw [hT']; field_simp

end Bgs.LineLLineOrth
