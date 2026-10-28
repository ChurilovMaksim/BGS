module
public import Mathlib
@[expose] public section

/-!
# Clock moment-channel obstruction: the root-of-unity character bound (BGS-TRACE-014)

Source: `mathematics/spectral-obstructions/isospectral_clock_moment_control.md`, §§2–4.

* **(C6)** `clock_alternant_ratio`: evaluate the Weyl alternants at the clock point
  `(1, ζ, …, ζ^{N-1})`, `ζ` a primitive `N`-th root of unity.  For arbitrary integer
  exponents `a_1, …, a_N` (negative allowed), the numerator alternant
  `det (ζ^{i a_j})` equals `s · det (ζ^{i (N-1-j)})` with `s ∈ {0, 1, -1}`, and the
  denominator (a Vandermonde determinant) is nonzero.  Hence every irreducible character
  of `U(N)` takes a value in `{0, ±1}` at `D_N` (via the Weyl character formula, which is
  not itself formalized).
* `clock_trace_pow_eq_zero`: `Tr D_N^q = 0` for `N ∤ q`; in particular `Tr D_N = Tr D_N² = 0`
  for `N ≥ 3`, so `χ_S(D_N) = χ_A(D_N) = 0` and `χ_{Ad₀}(D_N) = |Tr D_N|² - 1 = -1`.
* **(C3)/(C7) bookkeeping** `two_copy_dimensions`: the multiplicities in (C3) sum to `N⁴`;
  `d_s + d_a = N²(N²-3)/2`; constituent dimensions add up to `dim End(S)`, `dim End(A)`,
  `dim Hom(A,S)`; and `clock_two_copy_max`: `4/((N²-1)(N²-4)) < 1/(N²-1)` for `N ≥ 3`,
  so the maximum absolute nontrivial eigenvalue in (C2) is `1/(N²-1)`.
* `dim_ge_of_sq` : the integer step `N² - 1 ≤ d² → N ≤ d` (for `N ≥ 2`) used for (C1).
* **(C8), clock side** `clock_trace_pow_N`: `|Tr (e^{iΘ} Q D_N Q⁻¹)^N|² = N²`.
* **§4 counting** `lattice_count`: a half-open interval of integer length `L` contains
  exactly `L` points of a translated lattice `ℤ + η`.
-/

open Finset Matrix

namespace Bgs.Mathlib

section Alternant

variable {N : ℕ} [NeZero N] {ζ : ℂ}

lemma zpow_eq_of_intCast_eq (hζ : IsPrimitiveRoot ζ N) {k k' : ℤ}
    (h : (k : ZMod N) = (k' : ZMod N)) : ζ ^ k = ζ ^ k' := by
  rw [ZMod.intCast_eq_intCast_iff_dvd_sub] at h
  obtain ⟨c, hc⟩ := h
  have hζ0 : ζ ≠ 0 := hζ.ne_zero (NeZero.ne N)
  have : k' = k + N * c := by linarith
  rw [this, zpow_add₀ hζ0, _root_.zpow_mul, zpow_natCast, hζ.pow_eq_one, _root_.one_zpow, mul_one]

/-- The clock alternant with integer exponents `a_j`: `det (ζ^{i a_j})_{i,j}`. -/
noncomputable def clockAlternant (ζ : ℂ) (a : Fin N → ℤ) : ℂ :=
  Matrix.det (fun i j : Fin N => ζ ^ ((i : ℤ) * a j))

/-- The base matrix `(ζ^{i r})` indexed by residues `r ∈ ZMod N`. -/
noncomputable def clockBase (ζ : ℂ) : Matrix (Fin N) (ZMod N) ℂ :=
  fun i r => ζ ^ ((i : ℤ) * (r.val : ℤ))

lemma clock_entry_eq (hζ : IsPrimitiveRoot ζ N) (i : Fin N) (a : ℤ) :
    ζ ^ ((i : ℤ) * a) = clockBase ζ i (a : ZMod N) := by
  unfold clockBase
  apply zpow_eq_of_intCast_eq hζ
  push_cast
  rw [ZMod.natCast_zmod_val]

omit [NeZero N] in
/-- The denominator exponents `N - 1 - j`, as residues, are pairwise distinct. -/
lemma den_residue_injective : Function.Injective
    (fun j : Fin N => (((N - 1 - (j : ℕ) : ℕ) : ℤ) : ZMod N)) := by
  intro j j' h
  simp only [Int.cast_natCast] at h
  have hj := j.isLt; have hj' := j'.isLt
  rw [ZMod.natCast_eq_natCast_iff'] at h
  rw [Nat.mod_eq_of_lt (by omega), Nat.mod_eq_of_lt (by omega)] at h
  exact Fin.ext (by omega)

omit [NeZero N] in
/-- The denominator alternant (a Vandermonde determinant) is nonzero. -/
theorem clock_den_ne_zero (hζ : IsPrimitiveRoot ζ N) :
    clockAlternant ζ (fun j : Fin N => ((N - 1 - (j : ℕ) : ℕ) : ℤ)) ≠ 0 := by
  set y : Fin N → ℂ := fun j => ζ ^ (N - 1 - (j : ℕ))
  have hM : (fun i j : Fin N => ζ ^ ((i : ℤ) * (((N - 1 - (j : ℕ) : ℕ) : ℤ)))) =
      (Matrix.vandermonde y)ᵀ := by
    ext i j
    simp only [transpose_apply, vandermonde_apply, y]
    rw [← pow_mul, mul_comm, ← zpow_natCast]
    push_cast; ring_nf
  unfold clockAlternant
  rw [hM, det_transpose, det_vandermonde]
  refine Finset.prod_ne_zero_iff.mpr fun i _ => Finset.prod_ne_zero_iff.mpr fun j hj => ?_
  rw [sub_ne_zero]
  intro hyij
  have hlt : i < j := by simpa using hj
  have hi := i.isLt; have hj' := j.isLt
  have := (hζ.pow_inj (by omega : N - 1 - (j : ℕ) < N) (by omega : N - 1 - (i : ℕ) < N)) hyij
  have : (i : ℕ) = j := by omega
  exact absurd (Fin.ext this) (ne_of_lt hlt)

/-- **(C6).**  At the clock point, the Weyl alternant quotient lies in `{0, +1, -1}`:
`det(ζ^{i a_j}) = s · det(ζ^{i (N-1-j)})` for some `s ∈ {0, 1, -1}`, for every integer
exponent vector `a`. -/
theorem clock_alternant_ratio (hζ : IsPrimitiveRoot ζ N) (a : Fin N → ℤ) :
    ∃ s : ℤ, (s = 0 ∨ s = 1 ∨ s = -1) ∧
      clockAlternant ζ a =
        s * clockAlternant ζ (fun j : Fin N => ((N - 1 - (j : ℕ) : ℕ) : ℤ)) := by
  set f : Fin N → ZMod N := fun j => (a j : ZMod N)
  set f0 : Fin N → ZMod N := fun j => (((N - 1 - (j : ℕ) : ℕ) : ℤ) : ZMod N)
  have hcard : Fintype.card (Fin N) = Fintype.card (ZMod N) := by simp [ZMod.card]
  have hnum : clockAlternant ζ a = ((clockBase ζ).submatrix id f).det := by
    unfold clockAlternant; congr 1; ext i j; exact clock_entry_eq hζ i (a j)
  have hden : clockAlternant ζ (fun j : Fin N => ((N - 1 - (j : ℕ) : ℕ) : ℤ)) =
      ((clockBase ζ).submatrix id f0).det := by
    unfold clockAlternant; congr 1; ext i j; exact clock_entry_eq hζ i _
  by_cases hinj : Function.Injective f
  · have hbij : Function.Bijective f := (Fintype.bijective_iff_injective_and_card f).mpr
      ⟨hinj, hcard⟩
    have hbij0 : Function.Bijective f0 := (Fintype.bijective_iff_injective_and_card f0).mpr
      ⟨den_residue_injective, hcard⟩
    set e := Equiv.ofBijective f hbij
    set e0 := Equiv.ofBijective f0 hbij0
    set σ : Equiv.Perm (Fin N) := e.trans e0.symm
    have hsub : (clockBase ζ).submatrix id f =
        ((clockBase ζ).submatrix id f0).submatrix id σ := by
      ext i j
      simp only [submatrix_apply, id, σ, Equiv.trans_apply]
      congr 1
      have : f0 (e0.symm (e j)) = e j := e0.apply_symm_apply (e j)
      rw [this]; rfl
    refine ⟨(Equiv.Perm.sign σ : ℤ), ?_, ?_⟩
    · rcases Int.units_eq_one_or (Equiv.Perm.sign σ) with h | h <;> simp [h]
    · rw [hnum, hden, hsub, det_permute']
  · refine ⟨0, Or.inl rfl, ?_⟩
    rw [hnum, Int.cast_zero, zero_mul]
    simp only [Function.Injective, not_forall] at hinj
    obtain ⟨j, j', hjj', hne⟩ := hinj
    exact det_zero_of_column_eq hne fun k => by simp [hjj']

end Alternant

/-! ## Traces of the clock matrix -/

/-- `Tr D_N^q = ∑_j ζ^{jq} = 0` whenever `N ∤ q`. -/
theorem clock_trace_pow_eq_zero {N : ℕ} {ζ : ℂ} (hζ : IsPrimitiveRoot ζ N) (q : ℕ)
    (hq : ¬ N ∣ q) : ∑ j ∈ range N, (ζ ^ j) ^ q = 0 := by
  have hw : ζ ^ q ≠ 1 := fun h => hq (hζ.dvd_of_pow_eq_one q h)
  have hwN : (ζ ^ q) ^ N = 1 := by rw [← pow_mul, mul_comm, pow_mul, hζ.pow_eq_one, one_pow]
  have : ∑ j ∈ range N, (ζ ^ j) ^ q = ∑ j ∈ range N, (ζ ^ q) ^ j :=
    Finset.sum_congr rfl fun j _ => by rw [← pow_mul, ← pow_mul, mul_comm]
  rw [this, geom_sum_eq hw, hwN, sub_self, zero_div]

/-- For `N ≥ 3`: `Tr D_N = 0`, `Tr D_N² = 0`, hence `χ_S(D_N) = χ_A(D_N) = 0` and
`χ_{Ad₀}(D_N) = |Tr D_N|² - 1 = -1`. -/
theorem clock_low_characters {N : ℕ} (hN : 3 ≤ N) {ζ : ℂ} (hζ : IsPrimitiveRoot ζ N) :
    let t1 := ∑ j ∈ range N, ζ ^ j
    let t2 := ∑ j ∈ range N, (ζ ^ j) ^ 2
    t1 = 0 ∧ t2 = 0 ∧ (t1 ^ 2 + t2) / 2 = 0 ∧ (t1 ^ 2 - t2) / 2 = 0 ∧
      Complex.normSq t1 - 1 = -1 := by
  intro t1 t2
  have h1 : t1 = 0 := by
    have := clock_trace_pow_eq_zero hζ 1 (by
      intro h; have := Nat.le_of_dvd one_pos h; omega)
    simpa [t1] using this
  have h2 : t2 = 0 := clock_trace_pow_eq_zero hζ 2 (by
      intro h; have := Nat.le_of_dvd two_pos h; omega)
  refine ⟨h1, h2, ?_, ?_, ?_⟩ <;> simp [h1, h2]

/-! ## Dimension bookkeeping for (C2), (C3), (C7) -/

/-- **(C3)/(C7).**  The two-copy dimension identities (as polynomial identities in `N`):
the multiplicities of (C3) add up to `N⁴`; `d_s + d_a = N²(N²-3)/2`; and the constituent
dimensions fill `End(S)`, `End(A)` and `Hom(A,S)`. -/
theorem two_copy_dimensions (N : ℚ) :
    let ds := N ^ 2 * (N - 1) * (N + 3) / 4
    let da := N ^ 2 * (N + 1) * (N - 3) / 4
    let dc := (N ^ 2 - 1) * (N ^ 2 - 4) / 4
    2 + 4 * (N ^ 2 - 1) + N ^ 2 * (N ^ 2 - 3) / 2 + (N ^ 2 - 1) * (N ^ 2 - 4) / 2 = N ^ 4 ∧
    ds + da = N ^ 2 * (N ^ 2 - 3) / 2 ∧
    1 + (N ^ 2 - 1) + ds = (N * (N + 1) / 2) ^ 2 ∧
    1 + (N ^ 2 - 1) + da = (N * (N - 1) / 2) ^ 2 ∧
    (N ^ 2 - 1) + dc = (N * (N + 1) / 2) * (N * (N - 1) / 2) ∧
    2 * dc = (N ^ 2 - 1) * (N ^ 2 - 4) / 2 := by
  intro ds da dc
  refine ⟨by ring, by simp only [ds, da]; ring, by simp only [ds]; ring,
    by simp only [da]; ring, by simp only [dc]; ring, by simp only [dc]; ring⟩

/-- **(C2).**  For `N ≥ 3`, `4/((N²-1)(N²-4)) < 1/(N²-1)`; so among the nontrivial channel
eigenvalues `-1/(N²-1)`, `0`, `4/((N²-1)(N²-4))` the largest in absolute value is
`1/(N²-1)`. -/
theorem clock_two_copy_max {N : ℝ} (hN : 3 ≤ N) :
    4 / ((N ^ 2 - 1) * (N ^ 2 - 4)) < 1 / (N ^ 2 - 1) := by
  have h1 : 0 < N ^ 2 - 1 := by nlinarith
  have h4 : 5 ≤ N ^ 2 - 4 := by nlinarith
  rw [div_lt_div_iff₀ (by positivity) h1]
  nlinarith

/-- The integer step in (C1): `N² - 1 ≤ d²` with `N ≥ 2` forces `N ≤ d`. -/
theorem dim_ge_of_sq {N d : ℕ} (hN : 2 ≤ N) (h : N ^ 2 - 1 ≤ d ^ 2) : N ≤ d := by
  by_contra hlt
  push Not at hlt
  have hN2 : 1 ≤ N ^ 2 := Nat.one_le_pow _ _ (by omega)
  zify [hN2] at h
  have hd : (d : ℤ) ≤ N - 1 := by omega
  have hd0 : (0 : ℤ) ≤ d := by positivity
  nlinarith

/-- **(C8), clock side.**  For `V = e^{iΘ} Q D_N Q⁻¹` the `N`-th trace has
`|Tr V^N|² = N²`, i.e. `N⁻² |Tr V^N|² = 1`, for every realization. -/
theorem clock_trace_pow_N {N : ℕ} {ζ : ℂ} (hζ : IsPrimitiveRoot ζ N) (θ : ℝ) :
    Complex.normSq ((Complex.exp (θ * Complex.I)) ^ N * ∑ j ∈ range N, (ζ ^ j) ^ N) =
      (N : ℝ) ^ 2 := by
  have : ∑ j ∈ range N, (ζ ^ j) ^ N = N := by
    rw [Finset.sum_congr rfl fun j _ => by rw [← pow_mul, mul_comm, pow_mul, hζ.pow_eq_one,
      one_pow]]
    simp
  rw [this, Complex.normSq_mul, Complex.normSq_natCast, ← Complex.exp_nat_mul,
    Complex.normSq_eq_norm_sq, show (N : ℂ) * (θ * Complex.I) = ((N * θ : ℝ) : ℂ) * Complex.I
      by push_cast; ring, Complex.norm_exp_ofReal_mul_I]
  ring

/-! ## §4: exact lattice counts -/

/-- **§4.**  A half-open interval `[x, x + L)` of integer length `L` contains exactly `L`
points of the translated lattice `ℤ + η`. -/
theorem lattice_count (η x : ℝ) (L : ℕ) :
    ((Finset.Ico (⌈x - η⌉) (⌈x - η⌉ + L)).filter
      (fun n : ℤ => x ≤ n + η ∧ (n : ℝ) + η < x + L)).card = L := by
  rw [Finset.filter_true_of_mem]
  · simp
  · intro n hn
    rw [Finset.mem_Ico] at hn
    have h1 : x - η ≤ (n : ℝ) := (Int.ceil_le.mp hn.1)
    have h2 : (n : ℝ) < x - η + L := by
      have h3 : n < ⌈x - η⌉ + L := hn.2
      have h4 : (⌈x - η⌉ : ℝ) < x - η + 1 := Int.ceil_lt_add_one _
      have h5 : (n : ℝ) + 1 ≤ ⌈x - η⌉ + L := by exact_mod_cast h3
      linarith
    constructor <;> linarith

/-- Every point of `ℤ + η` in `[x, x + L)` lies in the enumerated window, so the count is
exactly `L`. -/
theorem lattice_points_in_window (η x : ℝ) (L : ℕ) (n : ℤ)
    (h : x ≤ n + η ∧ (n : ℝ) + η < x + L) :
    n ∈ Finset.Ico (⌈x - η⌉) (⌈x - η⌉ + L) := by
  rw [Finset.mem_Ico]
  constructor
  · exact Int.ceil_le.mpr (by linarith [h.1])
  · have h1 : ((⌈x - η⌉ : ℤ) : ℝ) ≥ x - η := Int.le_ceil _
    have : (n : ℝ) < ⌈x - η⌉ + L := by linarith [h.2]
    exact_mod_cast this

end Bgs.Mathlib
