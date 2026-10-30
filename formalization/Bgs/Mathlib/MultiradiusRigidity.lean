module
public import Bgs.Mathlib.DigitFUP
@[expose] public section

/-!
# Sharp multiradius rigidity for vector polynomials (BGS-RES-016)

Source: `mathematics/information-theory/multiradius_polynomial_rigidity.md`.

Let `E` be a complex inner product space, `v_0, …, v_n ∈ E` and
`P(z) = ∑_{j ≤ n} z^j v_j`.  Write `r = dim span{v_0, …, v_n}`.  A radius `ρ > 0` is
*flat* if `‖P(ρ e^{iθ})‖²` does not depend on `θ`.

* `sparse_pos_roots_card_le` — §2: a nonzero complex polynomial with `k` nonzero
  coefficients has at most `k - 1` distinct positive real zeros (via Descartes' rule of
  signs after a phase rotation).
* `flat_coeff_eq_zero` — flatness kills every angular Fourier coefficient:
  `∑_j ρ^{2j+L} ⟪v_j, v_{j+L}⟫ = 0` for `1 ≤ L ≤ n`.
* `orthogonal_isFlat`, `orthogonal_card_nonzero_le` — alternative (a).
* **`multiradius_rigidity`** — Theorem 1 (b): if the coefficient vectors are not
  pairwise orthogonal, any finite set of positive flat radii has at most `r - 1` elements.
* `flat_at_rank_radii_orthogonal` — flatness at `r` distinct positive radii forces
  pairwise orthogonality, independently of the degree `n`.
* `sharpExample_attains_bound` — §4: `P(z) = (2(1+z), √5 z(1-z), z²(1+z))` has rank 3, is
  not orthogonal, and its positive flat radii are exactly `{1, 2}`; so `r - 1` is sharp.
* `two_radius_quadrature_rigidity` — §5: if `|A|² + |B|²` (real/imaginary coefficient
  quadratures of `p = A + iB`) is radial on two distinct positive circles, then `p` has at
  most two nonzero coefficients and `Re(c_j \bar c_k) = 0` for `j ≠ k`.
-/

open Complex BigOperators Finset Polynomial

namespace Bgs.Mathlib

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℂ E]

local notation "⟪" x ", " y "⟫" => @inner ℂ _ _ x y

/-- The vector polynomial `P(z) = ∑_{j ≤ n} z^j v_j`. -/
noncomputable def vecPoly (v : ℕ → E) (n : ℕ) (z : ℂ) : E :=
  ∑ j ∈ range (n + 1), z ^ j • v j

/-- `ρ` is a flat radius: `‖P(ρ e^{iθ})‖²` is independent of `θ`. -/
def IsFlatRadius (v : ℕ → E) (n : ℕ) (ρ : ℝ) : Prop :=
  ∀ θ : ℝ, ‖vecPoly v n (ρ * Complex.exp (θ * Complex.I))‖ ^ 2 = ‖vecPoly v n ρ‖ ^ 2

/-- The coefficient vectors are pairwise Hermitian-orthogonal. -/
def CoeffOrthogonal (v : ℕ → E) (n : ℕ) : Prop :=
  ∀ j ∈ range (n + 1), ∀ l ∈ range (n + 1), j ≠ l → ⟪v j, v l⟫ = 0

/-- The rank `r = dim span{v_0, …, v_n}`. -/
noncomputable def coeffRank (v : ℕ → E) (n : ℕ) : ℕ :=
  Module.finrank ℂ (Submodule.span ℂ (v '' (range (n + 1) : Set ℕ)))

/-! ### Sparse positive zeros -/

lemma support_eq_filter_range (P : ℝ[X]) :
    P.support = (Finset.range P.degree.succ).filter (fun i => P.coeff i ≠ 0) := by
  by_cases hP : P = 0
  · subst hP; simp
  · rw [Polynomial.degree_eq_natDegree hP]
    ext i
    simp only [mem_support_iff, Finset.mem_filter, Finset.mem_range]
    constructor
    · intro h
      refine ⟨?_, h⟩
      have := Polynomial.le_natDegree_of_ne_zero h
      have e : (P.natDegree : WithBot ℕ).succ = P.natDegree + 1 := rfl
      rw [e]; omega
    · exact fun h => h.2

lemma list_range_countP (n : ℕ) (q : ℕ → Prop) [DecidablePred q] :
    (List.range n).countP (fun x => decide (q x)) = ((Finset.range n).filter q).card := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [List.range_succ, List.countP_append, ih, Finset.range_add_one, Finset.filter_insert]
    split_ifs with h
    · rw [Finset.card_insert_of_notMem (by simp)]; simp [h]
    · simp [h]

/-- The number of sign variations is at most `#support - 1`. -/
lemma signVariations_le_card_support (P : ℝ[X]) :
    P.signVariations ≤ P.support.card - 1 := by
  unfold Polynomial.signVariations
  have h1 := (List.destutter_sublist (· ≠ ·)
    ((P.coeffList.map SignType.sign).filter (· ≠ 0))).length_le
  have h2 : ((P.coeffList.map SignType.sign).filter (· ≠ 0)).length = P.support.card := by
    rw [List.filter_map, List.length_map, Polynomial.coeffList]
    rw [List.filter_map, List.length_map]
    rw [← List.countP_eq_length_filter, List.countP_reverse]
    rw [support_eq_filter_range]
    convert! list_range_countP P.degree.succ (fun i => P.coeff i ≠ 0) using 2
    ext i
    simp
  omega

/-- A nonzero real polynomial with `k` nonzero coefficients has at most `k - 1` distinct
positive zeros. -/
theorem real_sparse_pos_roots_card_le (P : ℝ[X]) (hP : P ≠ 0) (S : Finset ℝ)
    (hS : ∀ x ∈ S, 0 < x ∧ P.eval x = 0) : S.card ≤ P.support.card - 1 := by
  have hle : S.val ≤ P.roots.filter (0 < ·) := by
    rw [Multiset.le_iff_subset S.nodup]
    intro x hx
    obtain ⟨hx0, hxr⟩ := hS x hx
    rw [Multiset.mem_filter, Polynomial.mem_roots hP]
    exact ⟨hxr, hx0⟩
  have h1 := Multiset.card_le_card hle
  rw [← Multiset.countP_eq_card_filter] at h1
  have h2 := Polynomial.roots_countP_pos_le_signVariations P
  have h3 := signVariations_le_card_support P
  simp only [Finset.card_val] at h1
  omega

/-- **§2.**  A nonzero complex polynomial with `k` nonzero coefficients has at most `k - 1`
distinct positive real zeros. -/
theorem sparse_pos_roots_card_le (B : ℂ[X]) (hB : B ≠ 0) (S : Finset ℝ)
    (hS : ∀ x ∈ S, 0 < x ∧ B.eval (x : ℂ) = 0) : S.card ≤ B.support.card - 1 := by
  obtain ⟨i0, hi0⟩ := Polynomial.support_nonempty.2 hB
  set c := B.coeff i0 with hc
  have hc0 : c ≠ 0 := Polynomial.mem_support_iff.1 hi0
  set R : ℝ[X] := ∑ i ∈ B.support, Polynomial.monomial i ((starRingEnd ℂ c * B.coeff i).re)
    with hR
  have hRcoeff : ∀ i, R.coeff i =
      if i ∈ B.support then (starRingEnd ℂ c * B.coeff i).re else 0 := by
    intro i
    rw [hR, Polynomial.finsetSum_coeff]
    simp only [Polynomial.coeff_monomial]
    rw [Finset.sum_ite_eq']
  have hR0 : R ≠ 0 := by
    intro h
    have := hRcoeff i0
    rw [h, Polynomial.coeff_zero, if_pos hi0, ← hc, Complex.conj_mul'] at this
    have h2 : ((‖c‖ ^ 2 : ℝ) : ℂ).re = ‖c‖ ^ 2 := Complex.ofReal_re _
    push_cast at h2
    rw [h2] at this
    exact hc0 (norm_eq_zero.1 (pow_eq_zero_iff (n := 2) (by norm_num) |>.1 this.symm))
  have hRsupp : R.support ⊆ B.support := by
    intro i hi
    rw [Polynomial.mem_support_iff, hRcoeff] at hi
    by_contra h
    exact hi (if_neg h)
  have hReval : ∀ x : ℝ, R.eval x = (starRingEnd ℂ c * B.eval (x : ℂ)).re := by
    intro x
    rw [hR, Polynomial.eval_finsetSum, Polynomial.eval_eq_sum, Polynomial.sum_def,
      Finset.mul_sum, Complex.re_sum]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [Polynomial.eval_monomial, ← mul_assoc, ← Complex.ofReal_pow, Complex.re_mul_ofReal]
  have h := real_sparse_pos_roots_card_le R hR0 S (fun x hx => by
    refine ⟨(hS x hx).1, ?_⟩
    rw [hReval, (hS x hx).2, mul_zero, Complex.zero_re])
  have := Finset.card_le_card hRsupp
  omega

/-! ### Angular Fourier coefficients -/

/-- **Flatness kills the angular Fourier coefficients.**  If `ρ` is flat then for every
`1 ≤ L ≤ n`, `∑_{j ≤ n - L} ρ^{2j+L} ⟪v_j, v_{j+L}⟫ = 0`. -/
theorem flat_coeff_eq_zero (v : ℕ → E) (n : ℕ) {ρ : ℝ} (hflat : IsFlatRadius v n ρ)
    {L : ℕ} (hL1 : 1 ≤ L) (hLn : L ≤ n) :
    ∑ j ∈ range (n + 1 - L), (ρ : ℂ) ^ (2 * j + L) * ⟪v j, v (j + L)⟫ = 0 := by
  set K := 2 * n + 1 with hK
  have hK0 : 0 < K := by omega
  have hKc : (K : ℂ) ≠ 0 := by exact_mod_cast hK0.ne'
  -- angle grid
  set θ : ℕ → ℝ := fun m => 2 * Real.pi * m / K with hθ
  -- the averaged Fourier coefficient
  set A : ℂ := ∑ m ∈ range K, Complex.exp (-(L * θ m : ℝ) * Complex.I) *
      ((‖vecPoly v n (ρ * Complex.exp (θ m * Complex.I))‖ ^ 2 : ℝ) : ℂ) with hA
  -- (i) flatness makes `A` vanish
  have hA0 : A = 0 := by
    rw [hA, Finset.sum_congr rfl (fun m _ => by rw [hflat (θ m)]), ← Finset.sum_mul]
    have hsum : ∑ m ∈ range K, Complex.exp (-(L * θ m : ℝ) * Complex.I) =
        ∑ m ∈ range K, Complex.exp (2 * Real.pi * Complex.I * ((-(L : ℤ) : ℤ) : ℂ) / K) ^ m := by
      refine Finset.sum_congr rfl fun m _ => ?_
      rw [← Complex.exp_nat_mul]; congr 1; simp only [hθ]; push_cast; field_simp
    rw [hsum, geom_exp_sum hK0, if_neg, zero_mul]
    rintro ⟨q, hq⟩
    have : (L : ℤ) = -(K * q) := by linarith
    rcases lt_trichotomy q 0 with h | h | h
    · nlinarith
    · subst h; simp at this; omega
    · nlinarith
  -- (ii) expansion of `A`
  have hexpand : ∀ z : ℂ, ((‖vecPoly v n z‖ ^ 2 : ℝ) : ℂ) =
      ∑ j ∈ range (n + 1), ∑ l ∈ range (n + 1),
        (starRingEnd ℂ z) ^ j * z ^ l * ⟪v j, v l⟫ := by
    intro z
    have h0 := inner_self_eq_norm_sq_to_K (𝕜 := ℂ) (vecPoly v n z)
    rw [show ((‖vecPoly v n z‖ ^ 2 : ℝ) : ℂ) = ⟪vecPoly v n z, vecPoly v n z⟫ by
      rw [h0]; push_cast; rfl, vecPoly, sum_inner]
    refine Finset.sum_congr rfl fun j _ => ?_
    rw [inner_sum]
    refine Finset.sum_congr rfl fun l _ => ?_
    rw [inner_smul_left, inner_smul_right, map_pow]; ring
  have hterm : ∀ m j l : ℕ, Complex.exp (-(L * θ m : ℝ) * Complex.I) *
      ((starRingEnd ℂ (ρ * Complex.exp (θ m * Complex.I))) ^ j *
        (ρ * Complex.exp (θ m * Complex.I)) ^ l * ⟪v j, v l⟫) =
      (ρ : ℂ) ^ (j + l) * ⟪v j, v l⟫ *
        Complex.exp (2 * Real.pi * Complex.I * (((l : ℤ) - j - L : ℤ) : ℂ) / K) ^ m := by
    intro m j l
    rw [map_mul, Complex.conj_ofReal, ← Complex.exp_conj, map_mul, Complex.conj_ofReal,
      Complex.conj_I, mul_pow, mul_pow, ← Complex.exp_nat_mul, ← Complex.exp_nat_mul,
      ← Complex.exp_nat_mul, pow_add]
    have e : ∀ a b c d : ℂ, Complex.exp a * ((ρ : ℂ) ^ j * Complex.exp b *
        ((ρ : ℂ) ^ l * Complex.exp c) * d) = (ρ : ℂ) ^ j * (ρ : ℂ) ^ l * d *
        Complex.exp (a + b + c) := by
      intro a b c d; rw [Complex.exp_add, Complex.exp_add]; ring
    rw [e]
    congr 2
    simp only [hθ]; push_cast; field_simp; ring
  have hA1 : A = K * ∑ j ∈ range (n + 1 - L), (ρ : ℂ) ^ (2 * j + L) * ⟪v j, v (j + L)⟫ := by
    rw [hA]
    simp_rw [hexpand, Finset.mul_sum, hterm]
    rw [Finset.sum_comm]
    simp_rw [Finset.sum_comm (s := range K) (t := range (n + 1))]
    simp_rw [← Finset.mul_sum, geom_exp_sum hK0]
    -- only `l = j + L` survives
    have hdvd : ∀ j ∈ range (n + 1), ∀ l ∈ range (n + 1),
        ((K : ℤ) ∣ ((l : ℤ) - j - L) ↔ l = j + L) := by
      intro j hj l hl
      simp only [Finset.mem_range] at hj hl
      constructor
      · rintro ⟨q, hq⟩
        rcases lt_trichotomy q 0 with h | h | h
        · exfalso; nlinarith
        · subst h; omega
        · exfalso; nlinarith
      · rintro rfl; exact ⟨0, by push_cast; ring⟩
    rw [Finset.mul_sum]
    have hinner : ∀ j ∈ range (n + 1), ∑ l ∈ range (n + 1), (ρ : ℂ) ^ (j + l) * ⟪v j, v l⟫ *
        (if (K : ℤ) ∣ ((l : ℤ) - j - L) then (K : ℂ) else 0) =
        if j + L < n + 1 then (K : ℂ) * ((ρ : ℂ) ^ (2 * j + L) * ⟪v j, v (j + L)⟫) else 0 := by
      intro j hj
      by_cases hjL : j + L < n + 1
      · rw [Finset.sum_eq_single (j + L)]
        · rw [if_pos ((hdvd j hj (j + L) (Finset.mem_range.2 hjL)).2 rfl), if_pos hjL]
          ring_nf
        · intro l hl hne
          rw [if_neg (fun h => hne ((hdvd j hj l hl).1 h)), mul_zero]
        · intro h; exact absurd (Finset.mem_range.2 hjL) h
      · rw [if_neg hjL]
        refine Finset.sum_eq_zero fun l hl => ?_
        have hne : l ≠ j + L := by
          intro h; subst h; exact hjL (Finset.mem_range.1 hl)
        rw [if_neg (fun h => hne ((hdvd j hj l hl).1 h)), mul_zero]
    rw [Finset.sum_congr rfl hinner, ← Finset.sum_filter]
    congr 1
    ext j
    simp only [Finset.mem_filter, Finset.mem_range]
    omega
  have := hA1.symm.trans hA0
  rcases mul_eq_zero.1 this with h | h
  · exact absurd h hKc
  · exact h

/-! ### Rank bounds and the expansion of `‖P‖²` -/

lemma card_le_coeffRank_of_linearIndependent (v : ℕ → E) (n : ℕ) (J : Finset ℕ)
    (hJ : J ⊆ range (n + 1)) (hli : LinearIndependent ℂ (fun j : J => v j)) :
    J.card ≤ coeffRank v n := by
  have h1 := finrank_span_eq_card hli
  rw [Fintype.card_coe] at h1
  rw [← h1, coeffRank]
  have : FiniteDimensional ℂ (Submodule.span ℂ (v '' (range (n + 1) : Set ℕ))) :=
    FiniteDimensional.span_of_finite ℂ ((Finset.finite_toSet _).image v)
  apply Submodule.finrank_mono
  apply Submodule.span_mono
  rintro _ ⟨j, rfl⟩
  exact ⟨j, hJ j.2, rfl⟩

/-- `‖P(z)‖² = ∑_{j,l} \bar z^j z^l ⟪v_j, v_l⟫`. -/
lemma normSq_vecPoly_expand (v : ℕ → E) (n : ℕ) (z : ℂ) :
    ((‖vecPoly v n z‖ ^ 2 : ℝ) : ℂ) =
      ∑ j ∈ range (n + 1), ∑ l ∈ range (n + 1), (starRingEnd ℂ z) ^ j * z ^ l * ⟪v j, v l⟫ := by
  have h0 := inner_self_eq_norm_sq_to_K (𝕜 := ℂ) (vecPoly v n z)
  rw [show ((‖vecPoly v n z‖ ^ 2 : ℝ) : ℂ) = ⟪vecPoly v n z, vecPoly v n z⟫ by
    rw [h0]; push_cast; rfl, vecPoly, sum_inner]
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [inner_sum]
  refine Finset.sum_congr rfl fun l _ => ?_
  rw [inner_smul_left, inner_smul_right, map_pow]; ring

/-! ### Alternative (a) -/

theorem orthogonal_isFlat (v : ℕ → E) (n : ℕ) (h : CoeffOrthogonal v n) (ρ : ℝ) :
    IsFlatRadius v n ρ := by
  have key : ∀ z : ℂ, ((‖vecPoly v n z‖ ^ 2 : ℝ) : ℂ) =
      ∑ j ∈ range (n + 1), ((Complex.normSq z : ℝ) : ℂ) ^ j * ⟪v j, v j⟫ := by
    intro z
    rw [normSq_vecPoly_expand]
    refine Finset.sum_congr rfl fun j hj => ?_
    rw [Finset.sum_eq_single j]
    · rw [← mul_pow, Complex.normSq_eq_conj_mul_self]
    · intro l hl hne; rw [h j hj l hl (Ne.symm hne), mul_zero]
    · intro h'; exact absurd hj h'
  intro θ
  have e : Complex.normSq (ρ * Complex.exp (θ * Complex.I)) = Complex.normSq (ρ : ℂ) := by
    rw [Complex.normSq_mul, Complex.normSq_eq_norm_sq (Complex.exp _),
      Complex.norm_exp_ofReal_mul_I]; ring
  have h1 := key (ρ * Complex.exp (θ * Complex.I))
  have h2 := key (ρ : ℂ)
  rw [e] at h1
  exact_mod_cast h1.trans h2.symm

open Classical in
theorem orthogonal_card_nonzero_le (v : ℕ → E) (n : ℕ) (h : CoeffOrthogonal v n) :
    ((range (n + 1)).filter (fun j => v j ≠ 0)).card ≤ coeffRank v n := by
  apply card_le_coeffRank_of_linearIndependent v n _ (Finset.filter_subset _ _)
  apply linearIndependent_of_ne_zero_of_inner_eq_zero
  · intro j; exact (Finset.mem_filter.1 j.2).2
  · intro i j hij
    exact h i (Finset.mem_filter.1 i.2).1 j (Finset.mem_filter.1 j.2).1
      (fun e => hij (Subtype.ext e))

/-! ### Alternative (b) -/

/-- **BGS-RES-016, Theorem 1 (b).**  If the coefficient vectors are not pairwise orthogonal,
then every finite set of distinct positive flat radii has at most `r - 1` elements. -/
theorem multiradius_rigidity (v : ℕ → E) (n : ℕ) (hno : ¬ CoeffOrthogonal v n)
    (S : Finset ℝ) (hS : ∀ ρ ∈ S, 0 < ρ ∧ IsFlatRadius v n ρ) :
    S.card + 1 ≤ coeffRank v n := by
  classical
  -- some positive separation carries a nonzero inner product
  have hex : ∃ L ∈ Finset.Icc 1 n, ∃ j, j + L ≤ n ∧ ⟪v j, v (j + L)⟫ ≠ 0 := by
    unfold CoeffOrthogonal at hno
    push Not at hno
    obtain ⟨j, hj, l, hl, hjl, hne⟩ := hno
    simp only [Finset.mem_range] at hj hl
    rcases lt_or_gt_of_ne hjl with h | h
    · refine ⟨l - j, Finset.mem_Icc.2 ⟨by omega, by omega⟩, j, by omega, ?_⟩
      rwa [show j + (l - j) = l by omega]
    · refine ⟨j - l, Finset.mem_Icc.2 ⟨by omega, by omega⟩, l, by omega, ?_⟩
      rw [show l + (j - l) = j by omega, ← inner_conj_symm]
      exact (_root_.map_ne_zero _).2 hne
  -- the maximal such separation
  set T := (Finset.Icc 1 n).filter
    (fun L => ∃ j, j + L ≤ n ∧ ⟪v j, v (j + L)⟫ ≠ 0) with hTdef
  have hT : T.Nonempty := by
    obtain ⟨L, hL, hj⟩ := hex
    exact ⟨L, Finset.mem_filter.2 ⟨hL, hj⟩⟩
  set L := T.max' hT with hLdef
  have hLmem : L ∈ T := Finset.max'_mem T hT
  have hL1 : 1 ≤ L := (Finset.mem_Icc.1 (Finset.mem_filter.1 hLmem).1).1
  have hLn : L ≤ n := (Finset.mem_Icc.1 (Finset.mem_filter.1 hLmem).1).2
  have hmax : ∀ L' j : ℕ, L < L' → j + L' ≤ n → ⟪v j, v (j + L')⟫ = 0 := by
    intro L' j hL' hjn
    by_contra hne
    have hmem : L' ∈ T := Finset.mem_filter.2
      ⟨Finset.mem_Icc.2 ⟨by omega, by omega⟩, j, hjn, hne⟩
    have := T.le_max' L' hmem
    omega
  -- the polynomial `B(x) = ∑_j ⟪v_j, v_{j+L}⟫ x^j`
  set B : ℂ[X] := ∑ j ∈ range (n + 1 - L), Polynomial.C (⟪v j, v (j + L)⟫) * X ^ j with hBdef
  have hBcoeff : ∀ j, B.coeff j = if j < n + 1 - L then ⟪v j, v (j + L)⟫ else 0 := by
    intro j
    rw [hBdef, Polynomial.finsetSum_coeff]
    simp only [Polynomial.coeff_C_mul_X_pow]
    rw [Finset.sum_ite_eq]
    simp [Finset.mem_range]
  have hB0 : B ≠ 0 := by
    obtain ⟨j, hj, hne⟩ := (Finset.mem_filter.1 hLmem).2
    intro h
    have := hBcoeff j
    rw [h, Polynomial.coeff_zero, if_pos (by omega)] at this
    exact hne this.symm
  have hBeval : ∀ x : ℂ, B.eval x = ∑ j ∈ range (n + 1 - L), ⟪v j, v (j + L)⟫ * x ^ j := by
    intro x
    rw [hBdef, Polynomial.eval_finsetSum]
    simp
  -- flat radii give positive roots `ρ²` of `B`
  have hroot : ∀ ρ ∈ S, B.eval ((ρ ^ 2 : ℝ) : ℂ) = 0 := by
    intro ρ hρ
    obtain ⟨hρ0, hflat⟩ := hS ρ hρ
    have h := flat_coeff_eq_zero v n hflat hL1 hLn
    have e : ∑ j ∈ range (n + 1 - L), (ρ : ℂ) ^ (2 * j + L) * ⟪v j, v (j + L)⟫ =
        (ρ : ℂ) ^ L * B.eval ((ρ ^ 2 : ℝ) : ℂ) := by
      rw [hBeval, Finset.mul_sum]
      refine Finset.sum_congr rfl fun j _ => ?_
      push_cast; ring
    rw [e] at h
    rcases mul_eq_zero.1 h with h' | h'
    · exact absurd h' (pow_ne_zero _ (by exact_mod_cast hρ0.ne'))
    · exact h'
  have hcard1 : S.card ≤ B.support.card - 1 := by
    have hinj : Set.InjOn (fun ρ : ℝ => ρ ^ 2) S := by
      intro a ha b hb hab
      have := (hS a ha).1; have := (hS b hb).1
      simp only at hab
      nlinarith
    have := sparse_pos_roots_card_le B hB0 (S.image (fun ρ : ℝ => ρ ^ 2)) (by
      intro x hx
      obtain ⟨ρ, hρ, rfl⟩ := Finset.mem_image.1 hx
      exact ⟨pow_pos (hS ρ hρ).1 2, hroot ρ hρ⟩)
    rwa [Finset.card_image_of_injOn hinj] at this
  -- the coefficient vectors indexed by the support of `B` are independent
  have hsupp : ∀ j ∈ B.support, j + L ≤ n ∧ ⟪v j, v (j + L)⟫ ≠ 0 := by
    intro j hj
    rw [Polynomial.mem_support_iff, hBcoeff] at hj
    by_cases h : j < n + 1 - L
    · rw [if_pos h] at hj; exact ⟨by omega, hj⟩
    · rw [if_neg h] at hj; exact absurd rfl hj
  have hli : LinearIndependent ℂ (fun j : B.support => v j) := by
    rw [Fintype.linearIndependent_iff]
    intro g hg
    by_contra hcon
    push Not at hcon
    set s := Finset.univ.filter (fun i : B.support => g i ≠ 0) with hs
    have hsne : s.Nonempty := by
      obtain ⟨i, hi⟩ := hcon; exact ⟨i, Finset.mem_filter.2 ⟨Finset.mem_univ _, hi⟩⟩
    obtain ⟨i0, hi0s, hi0max⟩ := s.exists_max_image (fun i => (i : ℕ)) hsne
    have hgi0 : g i0 ≠ 0 := (Finset.mem_filter.1 hi0s).2
    obtain ⟨hi0n, hb⟩ := hsupp i0 i0.2
    have hzero : ⟪v ((i0 : ℕ) + L), ∑ i, g i • v i⟫ = 0 := by rw [hg, inner_zero_right]
    rw [inner_sum] at hzero
    simp_rw [inner_smul_right] at hzero
    rw [Finset.sum_eq_single i0] at hzero
    · rcases mul_eq_zero.1 hzero with h | h
      · exact hgi0 h
      · rw [← inner_conj_symm] at h
        exact hb ((_root_.map_eq_zero _).1 h)
    · intro i _ hne
      by_cases hgi : g i = 0
      · rw [hgi, zero_mul]
      · have hlt : (i : ℕ) < i0 := by
          have := hi0max i (Finset.mem_filter.2 ⟨Finset.mem_univ _, hgi⟩)
          rcases lt_or_eq_of_le this with h | h
          · exact h
          · exact absurd (Subtype.ext h) hne
        rw [← inner_conj_symm,
          show (i0 : ℕ) + L = (i : ℕ) + ((i0 : ℕ) + L - i) by omega,
          hmax _ _ (by omega) (by omega), map_zero, mul_zero]
    · intro h; exact absurd (Finset.mem_univ _) h
  have hcard2 := card_le_coeffRank_of_linearIndependent v n B.support (by
    intro j hj
    exact Finset.mem_range.2 (by have := (hsupp j hj).1; omega)) hli
  have hpos : 1 ≤ B.support.card := Finset.card_pos.2 (Polynomial.support_nonempty.2 hB0)
  omega

/-- Flatness at `r` distinct positive radii forces pairwise orthogonality, regardless of the
degree. -/
theorem flat_at_rank_radii_orthogonal (v : ℕ → E) (n : ℕ) (S : Finset ℝ)
    (hcard : coeffRank v n ≤ S.card) (hS : ∀ ρ ∈ S, 0 < ρ ∧ IsFlatRadius v n ρ) :
    CoeffOrthogonal v n := by
  by_contra h
  have := multiradius_rigidity v n h S hS
  omega

end Bgs.Mathlib

/-! ### Sharpness (§4): the explicit three-component example with flat radii `1, 2` -/

namespace Bgs.Mathlib

/-- Coefficients of `P(z) = (2(1+z), √5 z(1-z), z²(1+z))`. -/
noncomputable def sharpExample : ℕ → EuclideanSpace ℂ (Fin 3)
  | 0 => !₂[2, 0, 0]
  | 1 => !₂[2, Real.sqrt 5, 0]
  | 2 => !₂[0, -Real.sqrt 5, 1]
  | 3 => !₂[0, 0, 1]
  | _ => 0

lemma sharpExample_poly (z : ℂ) :
    vecPoly sharpExample 3 z =
      !₂[2 * (1 + z), Real.sqrt 5 * z * (1 - z), z ^ 2 * (1 + z)] := by
  ext i
  fin_cases i <;>
  simp [vecPoly, sharpExample, Finset.sum_range_succ] <;> ring

lemma sharpExample_normSq (ρ θ : ℝ) :
    ‖vecPoly sharpExample 3 (ρ * Complex.exp (θ * Complex.I))‖ ^ 2 =
      (1 + ρ ^ 2) * (4 + 5 * ρ ^ 2 + ρ ^ 4) +
        2 * ρ * Real.cos θ * (ρ ^ 4 - 5 * ρ ^ 2 + 4) := by
  rw [sharpExample_poly, EuclideanSpace.norm_sq_eq, Fin.sum_univ_three]
  have hz : (ρ : ℂ) * Complex.exp (θ * Complex.I) =
      ((ρ * Real.cos θ : ℝ) : ℂ) + ((ρ * Real.sin θ : ℝ) : ℂ) * Complex.I := by
    rw [Complex.exp_mul_I]; push_cast
    rw [← Complex.ofReal_cos, ← Complex.ofReal_sin]; ring
  rw [hz]
  simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
    Matrix.head_cons, Matrix.tail_cons, Complex.sq_norm, Complex.normSq_apply]
  simp only [Complex.mul_re, Complex.mul_im, Complex.add_re, Complex.add_im, Complex.ofReal_re,
    Complex.ofReal_im, Complex.I_re, Complex.I_im, Complex.one_re, Complex.one_im,
    Complex.sub_re, Complex.sub_im, pow_two, Complex.re_ofNat, Complex.im_ofNat]
  have h5 : Real.sqrt 5 * Real.sqrt 5 = 5 := Real.mul_self_sqrt (by norm_num)
  have hsc := Real.sin_sq_add_cos_sq θ
  set c := Real.cos θ
  set sn := Real.sin θ
  have hsn : sn * sn = 1 - c * c := by nlinarith
  ring_nf
  rw [show Real.sqrt 5 ^ 2 = 5 by rw [sq]; exact h5]
  have hsn2 : sn ^ 2 = 1 - c ^ 2 := by nlinarith
  rw [show sn ^ 4 = (sn ^ 2) ^ 2 by ring, show sn ^ 6 = (sn ^ 2) ^ 3 by ring, hsn2]
  ring

/-- The positive flat radii of the example are exactly `1` and `2`. -/
theorem sharpExample_isFlat_iff {ρ : ℝ} (hρ : 0 < ρ) :
    IsFlatRadius sharpExample 3 ρ ↔ ρ = 1 ∨ ρ = 2 := by
  have h0 : ‖vecPoly sharpExample 3 (ρ : ℂ)‖ ^ 2 =
      (1 + ρ ^ 2) * (4 + 5 * ρ ^ 2 + ρ ^ 4) + 2 * ρ * 1 * (ρ ^ 4 - 5 * ρ ^ 2 + 4) := by
    have := sharpExample_normSq ρ 0
    simpa using this
  have hfac : ρ ^ 4 - 5 * ρ ^ 2 + 4 = (ρ - 1) * (ρ - 2) * (ρ + 1) * (ρ + 2) := by ring
  constructor
  · intro hflat
    have hπ := hflat Real.pi
    rw [sharpExample_normSq, h0, Real.cos_pi] at hπ
    have hB : ρ ^ 4 - 5 * ρ ^ 2 + 4 = 0 := by nlinarith
    rw [hfac] at hB
    rcases mul_eq_zero.1 hB with h | h
    · rcases mul_eq_zero.1 h with h | h
      · rcases mul_eq_zero.1 h with h | h
        · left; linarith
        · right; linarith
      · linarith
    · linarith
  · intro h θ
    have hB : ρ ^ 4 - 5 * ρ ^ 2 + 4 = 0 := by
      rw [hfac]; rcases h with rfl | rfl <;> ring
    rw [sharpExample_normSq, h0, hB]; ring

theorem sharpExample_not_orthogonal : ¬ CoeffOrthogonal sharpExample 3 := by
  intro h
  have := h 0 (by simp) 1 (by simp) (by norm_num)
  simp [sharpExample, EuclideanSpace.inner_eq_star_dotProduct, dotProduct,
    Fin.sum_univ_three] at this

theorem sharpExample_rank : coeffRank sharpExample 3 = 3 := by
  apply le_antisymm
  · rw [coeffRank]
    have := Submodule.finrank_le (Submodule.span ℂ (sharpExample '' (range (3 + 1) : Set ℕ)))
    rwa [finrank_euclideanSpace, Fintype.card_fin] at this
  · have hJ : ({0, 2, 3} : Finset ℕ) ⊆ range (3 + 1) := by decide
    have := card_le_coeffRank_of_linearIndependent sharpExample 3 {0, 2, 3} hJ (by
      rw [Fintype.linearIndependent_iff]
      intro g hg
      set g' : ℕ → ℂ := fun i => if h : i ∈ ({0, 2, 3} : Finset ℕ) then g ⟨i, h⟩ else 0
        with hg'
      have hgg : ∀ i : ({0, 2, 3} : Finset ℕ), g i = g' i := by
        intro i; simp only [hg', Subtype.coe_eta, Finset.coe_mem, dite_true]
      have hsum : ∑ i ∈ ({0, 2, 3} : Finset ℕ), g' i • sharpExample i = 0 := by
        rw [← Finset.sum_coe_sort]; simp_rw [← hgg]; exact hg
      rw [Finset.sum_insert (by decide), Finset.sum_insert (by decide),
        Finset.sum_singleton] at hsum
      have c0 := congrArg (fun x : EuclideanSpace ℂ (Fin 3) => x 0) hsum
      have c1 := congrArg (fun x : EuclideanSpace ℂ (Fin 3) => x 1) hsum
      have c2 := congrArg (fun x : EuclideanSpace ℂ (Fin 3) => x 2) hsum
      simp [sharpExample] at c0 c1 c2
      have e3 : g' 3 = 0 := by rw [c1, zero_add] at c2; exact c2
      intro i
      rw [hgg]
      have hi := i.2
      simp only [Finset.mem_insert, Finset.mem_singleton] at hi
      rcases hi with h | h | h <;> rw [h]
      · exact c0
      · exact c1
      · exact e3)
    simpa using this

/-- **Sharpness of Theorem 1 at `d = r = 3`.**  The example is not orthogonal, has rank `3`,
and is flat on exactly the `r - 1 = 2` radii `{1, 2}`. -/
theorem sharpExample_attains_bound :
    ¬ CoeffOrthogonal sharpExample 3 ∧ coeffRank sharpExample 3 = 3 ∧
      (∀ ρ : ℝ, 0 < ρ → (IsFlatRadius sharpExample 3 ρ ↔ ρ ∈ ({1, 2} : Finset ℝ))) ∧
      ({1, 2} : Finset ℝ).card + 1 = coeffRank sharpExample 3 := by
  refine ⟨sharpExample_not_orthogonal, sharpExample_rank, fun ρ hρ => ?_, ?_⟩
  · rw [sharpExample_isFlat_iff hρ]; simp
  · rw [sharpExample_rank, Finset.card_pair (by norm_num)]

end Bgs.Mathlib

/-! ### §5: the two-quadrature consequence -/

namespace Bgs.Mathlib

/-- Real and imaginary coefficient parts as a two-component vector. -/
noncomputable def quadVec (c : ℕ → ℂ) (j : ℕ) : EuclideanSpace ℂ (Fin 2) :=
  !₂[((c j).re : ℂ), ((c j).im : ℂ)]

/-- The two quadrature polynomials `A(z) = ∑ Re(c_j) z^j`, `B(z) = ∑ Im(c_j) z^j`. -/
noncomputable def quadA (c : ℕ → ℂ) (n : ℕ) (z : ℂ) : ℂ := ∑ j ∈ range (n + 1), ((c j).re : ℂ) * z ^ j
noncomputable def quadB (c : ℕ → ℂ) (n : ℕ) (z : ℂ) : ℂ := ∑ j ∈ range (n + 1), ((c j).im : ℂ) * z ^ j

lemma norm_vecPoly_quadVec (c : ℕ → ℂ) (n : ℕ) (z : ℂ) :
    ‖vecPoly (quadVec c) n z‖ ^ 2 = ‖quadA c n z‖ ^ 2 + ‖quadB c n z‖ ^ 2 := by
  rw [EuclideanSpace.norm_sq_eq, Fin.sum_univ_two]
  congr 2
  · simp [vecPoly, quadVec, quadA, mul_comm]
  · simp [vecPoly, quadVec, quadB, mul_comm]

/-- **BGS-RES-016, §5 (two-quadrature rigidity).**  If `|A|² + |B|²` is radial on two distinct
positive circles, then `p = A + iB` has at most two nonzero coefficients and any two of its
coefficients satisfy `Re(c_j \bar c_k) = 0`. -/
theorem two_radius_quadrature_rigidity (c : ℕ → ℂ) (n : ℕ) {ρ₁ ρ₂ : ℝ} (h₁ : 0 < ρ₁)
    (h₂ : 0 < ρ₂) (hne : ρ₁ ≠ ρ₂)
    (hflat : ∀ ρ ∈ ({ρ₁, ρ₂} : Finset ℝ), ∀ θ : ℝ,
      ‖quadA c n (ρ * Complex.exp (θ * Complex.I))‖ ^ 2 +
          ‖quadB c n (ρ * Complex.exp (θ * Complex.I))‖ ^ 2 =
        ‖quadA c n ρ‖ ^ 2 + ‖quadB c n ρ‖ ^ 2) :
    (∀ j ∈ range (n + 1), ∀ k ∈ range (n + 1), j ≠ k →
        (c j * (starRingEnd ℂ) (c k)).re = 0) ∧
      ((range (n + 1)).filter (fun j => c j ≠ 0)).card ≤ 2 := by
  classical
  have hrank : coeffRank (quadVec c) n ≤ 2 := by
    rw [coeffRank]
    have := Submodule.finrank_le (Submodule.span ℂ (quadVec c '' (range (n + 1) : Set ℕ)))
    rwa [finrank_euclideanSpace, Fintype.card_fin] at this
  have hS : ∀ ρ ∈ ({ρ₁, ρ₂} : Finset ℝ), 0 < ρ ∧ IsFlatRadius (quadVec c) n ρ := by
    intro ρ hρ
    refine ⟨?_, fun θ => ?_⟩
    · simp only [Finset.mem_insert, Finset.mem_singleton] at hρ
      rcases hρ with rfl | rfl <;> assumption
    · rw [norm_vecPoly_quadVec, norm_vecPoly_quadVec]; exact hflat ρ hρ θ
  have horth : CoeffOrthogonal (quadVec c) n := by
    by_contra h
    have := multiradius_rigidity (quadVec c) n h _ hS
    rw [Finset.card_pair hne] at this
    omega
  refine ⟨fun j hj k hk hjk => ?_, ?_⟩
  · have := horth j hj k hk hjk
    simp [quadVec, EuclideanSpace.inner_eq_star_dotProduct, dotProduct, Fin.sum_univ_two] at this
    simp only [Complex.mul_re, Complex.conj_re, Complex.conj_im]
    have h' := congrArg Complex.re this
    simp at h'
    linarith
  · have h1 := orthogonal_card_nonzero_le (quadVec c) n horth
    have h2 : (range (n + 1)).filter (fun j => c j ≠ 0) =
        (range (n + 1)).filter (fun j => quadVec c j ≠ 0) := by
      ext j
      simp only [Finset.mem_filter]
      constructor
      · rintro ⟨hj, hc⟩
        refine ⟨hj, fun h0 => hc ?_⟩
        have e0 := congrArg (fun x : EuclideanSpace ℂ (Fin 2) => x 0) h0
        have e1 := congrArg (fun x : EuclideanSpace ℂ (Fin 2) => x 1) h0
        simp [quadVec] at e0 e1
        exact Complex.ext e0 e1
      · rintro ⟨hj, hv⟩
        refine ⟨hj, fun h0 => hv ?_⟩
        ext i; fin_cases i <;> simp [quadVec, h0]
    rw [h2]
    convert! h1.trans hrank using 2
    ext j; simp

#print axioms support_eq_filter_range
#print axioms list_range_countP
#print axioms signVariations_le_card_support
#print axioms real_sparse_pos_roots_card_le
#print axioms sparse_pos_roots_card_le
#print axioms flat_coeff_eq_zero
#print axioms card_le_coeffRank_of_linearIndependent
#print axioms normSq_vecPoly_expand
#print axioms orthogonal_isFlat
#print axioms orthogonal_card_nonzero_le
#print axioms multiradius_rigidity
#print axioms flat_at_rank_radii_orthogonal
#print axioms sharpExample_poly
#print axioms sharpExample_normSq
#print axioms sharpExample_isFlat_iff
#print axioms sharpExample_not_orthogonal
#print axioms sharpExample_rank
#print axioms sharpExample_attains_bound
#print axioms norm_vecPoly_quadVec
#print axioms two_radius_quadrature_rigidity
end Bgs.Mathlib
