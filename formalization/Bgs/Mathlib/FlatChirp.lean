module
public import Mathlib
@[expose] public section

/-!
# The flat Fourier chirp `V_p` and the four-dimensional core `H` (BGS-TRACE-081, §§2–3)

Source: `mathematics/spectral-obstructions/flat_spectrum_obstruction.md`, §2 and §3.

For an odd prime `p` write `ψ(x) = e^{2π i x / p}` on `ZMod p`, and put
`F_p = p^{-1/2} (ψ(ab))_{a,b}`, `D_p = diag(ψ(b²))`, `V_p = F_p^* D_p F_p`.

Formalized here:

* (O8) `chirp_sum_normSq`: `|∑_b ψ(a b² + d b)|² = p` for every `a ≠ 0` and every `d`;
* Fourier orthogonality: `fourier_unitary` (`F_p^* F_p = 1`) and `fourier_unitary'`;
* (O7) `chirpV_apply`: `(V_p)_{ij} = p⁻¹ ∑_b ψ(b² + (j - i) b)`;
* `chirpV_unitary`, `chirpV_transpose` (`V_pᵀ = V_p`), `chirpV_pow_p` (`V_p^p = 1`);
* flatness `chirpV_entry_normSq`: `|(V_p)_{ij}|² = 1/p`;
* (O9) `chirpV_trace_pow_normSq`: `|Tr V_p^q|² = p` whenever `p ∤ q`;
* (O6) the core `H = W/2`: `coreH_mul_transpose` (`H Hᵀ = 1`), `coreH_sq`
  (`H²` is the displayed permutation), `coreH_pow_six` (`H⁶ = 1`), flat entries
  `coreH_entry_normSq`, the reversal core `reversal_coreH` and
  `reversal_coreH_mul_conjTranspose` (`B(H) B(H)ᴴ = ¼ · 1`).
-/

open Finset Matrix

namespace Bgs.Mathlib

/-- The standard additive character `ψ(x) = e^{2π i x/p}` of `ZMod p`. -/
noncomputable abbrev ψp (p : ℕ) [NeZero p] : AddChar (ZMod p) ℂ := ZMod.stdAddChar

lemma two_ne_zero_zmod (p : ℕ) [hp : Fact p.Prime] (hp2 : p ≠ 2) : (2 : ZMod p) ≠ 0 := by
  intro h
  have := (ZMod.natCast_eq_zero_iff 2 p).mp (by exact_mod_cast h)
  exact hp2 ((Nat.prime_dvd_prime_iff_eq hp.out Nat.prime_two).mp this)

/-- Orthogonality of characters: `∑_c ψ(c u) = p·[u = 0]`. -/
lemma sum_psi_mul (p : ℕ) [NeZero p] (u : ZMod p) :
    ∑ c : ZMod p, ψp p (c * u) = if u = 0 then (p : ℂ) else 0 := by
  rw [AddChar.sum_mulShift _ (ZMod.isPrimitive_stdAddChar p)]
  by_cases hu : u = 0 <;> simp [hu, ZMod.card]

lemma psi_conj (p : ℕ) [NeZero p] (x : ZMod p) :
    (starRingEnd ℂ) (ψp p x) = ψp p (-x) := (AddChar.map_neg_eq_conj _ x).symm

/-- **(O8).** For an odd prime `p`, `a ≠ 0` and any `d`, `|∑_b ψ(a b² + d b)|² = p`. -/
theorem chirp_sum_normSq (p : ℕ) [hp : Fact p.Prime] (hp2 : p ≠ 2) (a d : ZMod p)
    (ha : a ≠ 0) :
    Complex.normSq (∑ b : ZMod p, ψp p (a * b ^ 2 + d * b)) = p := by
  have h2 := two_ne_zero_zmod p hp2
  suffices hC : ((Complex.normSq (∑ b : ZMod p, ψp p (a * b ^ 2 + d * b)) : ℝ) : ℂ) = p by
    exact_mod_cast hC
  rw [← Complex.mul_conj, mul_comm, map_sum, Finset.sum_mul_sum]
  have key : ∀ c u : ZMod p, (starRingEnd ℂ) (ψp p (a * c ^ 2 + d * c)) *
      ψp p (a * (c + u) ^ 2 + d * (c + u))
      = ψp p (u * (a * u + d)) * ψp p (c * (2 * a * u)) := by
    intro c u
    rw [← AddChar.map_neg_eq_conj, ← AddChar.map_add_eq_mul, ← AddChar.map_add_eq_mul]
    congr 1; ring
  have hshift : ∀ c : ZMod p,
      ∑ b : ZMod p, (starRingEnd ℂ) (ψp p (a * c ^ 2 + d * c)) * ψp p (a * b ^ 2 + d * b)
      = ∑ u : ZMod p, (starRingEnd ℂ) (ψp p (a * c ^ 2 + d * c)) *
          ψp p (a * (c + u) ^ 2 + d * (c + u)) := by
    intro c
    exact (Fintype.sum_equiv (Equiv.addLeft c) _ _ (fun u => rfl)).symm
  rw [Finset.sum_congr rfl (fun c _ => hshift c)]
  simp_rw [key]
  rw [Finset.sum_comm]
  simp_rw [← Finset.mul_sum]
  have hin : ∀ u : ZMod p, ∑ c : ZMod p, ψp p (c * (2 * a * u)) =
      if u = 0 then (p : ℂ) else 0 := by
    intro u
    rw [sum_psi_mul]
    by_cases hu : u = 0
    · simp [hu]
    · have : 2 * a * u ≠ 0 := mul_ne_zero (mul_ne_zero h2 ha) hu
      simp [hu, this]
  simp_rw [hin]
  simp

/-! ## The unitary Fourier matrix and the chirp `V_p` -/

/-- The unitary discrete Fourier matrix `(F_p)_{ab} = p^{-1/2} ψ(ab)`. -/
noncomputable def fourierF (p : ℕ) [NeZero p] : Matrix (ZMod p) (ZMod p) ℂ :=
  fun a b => ((Real.sqrt p : ℝ) : ℂ)⁻¹ * ψp p (a * b)

/-- The chirp diagonal `D_p = diag(ψ(b²))`. -/
noncomputable def chirpD (p : ℕ) [NeZero p] : Matrix (ZMod p) (ZMod p) ℂ :=
  Matrix.diagonal fun b => ψp p (b ^ 2)

/-- The flat chirp `V_p = F_p^* D_p F_p`. -/
noncomputable def chirpV (p : ℕ) [NeZero p] : Matrix (ZMod p) (ZMod p) ℂ :=
  (fourierF p)ᴴ * chirpD p * fourierF p

lemma sqrt_inv_sq (p : ℕ) [NeZero p] :
    ((Real.sqrt p : ℝ) : ℂ)⁻¹ * ((Real.sqrt p : ℝ) : ℂ)⁻¹ = (p : ℂ)⁻¹ := by
  rw [← mul_inv, ← Complex.ofReal_mul, Real.mul_self_sqrt (Nat.cast_nonneg _)]
  simp

lemma conj_sqrt_inv (p : ℕ) :
    (starRingEnd ℂ) (((Real.sqrt p : ℝ) : ℂ)⁻¹) = ((Real.sqrt p : ℝ) : ℂ)⁻¹ := by
  rw [map_inv₀, Complex.conj_ofReal]

lemma fourier_conj_mul (p : ℕ) [NeZero p] (b i j : ZMod p) :
    (starRingEnd ℂ) (fourierF p b i) * fourierF p b j = (p : ℂ)⁻¹ * ψp p (b * (j - i)) := by
  simp only [fourierF, map_mul, conj_sqrt_inv, psi_conj]
  rw [← sqrt_inv_sq p]
  have : ψp p (b * (j - i)) = ψp p (-(b * i)) * ψp p (b * j) := by
    rw [← AddChar.map_add_eq_mul]; congr 1; ring
  rw [this]; ring

/-- Fourier orthogonality: `F_p^* F_p = 1`. -/
theorem fourier_unitary (p : ℕ) [NeZero p] : (fourierF p)ᴴ * fourierF p = 1 := by
  ext i j
  simp only [mul_apply, conjTranspose_apply, RCLike.star_def, fourier_conj_mul]
  rw [← Finset.mul_sum, sum_psi_mul]
  by_cases hij : i = j
  · subst hij; simp [NeZero.ne]
  · have : j - i ≠ 0 := sub_ne_zero.mpr (Ne.symm hij)
    simp [this, one_apply_ne hij]

/-- The Fourier matrix is symmetric. -/
lemma fourierF_transpose (p : ℕ) [NeZero p] : (fourierF p)ᵀ = fourierF p := by
  ext a b; simp [fourierF, mul_comm]

/-- `F_p F_p^* = 1`. -/
theorem fourier_unitary' (p : ℕ) [NeZero p] : fourierF p * (fourierF p)ᴴ = 1 :=
  (mul_eq_one_comm_of_card_eq _ _ ℂ rfl).mp (fourier_unitary p)

/-- **(O7).** Entry formula `(V_p)_{ij} = p⁻¹ ∑_b ψ(b² + (j-i) b)`. -/
theorem chirpV_apply (p : ℕ) [NeZero p] (i j : ZMod p) :
    chirpV p i j = (p : ℂ)⁻¹ * ∑ b : ZMod p, ψp p (b ^ 2 + (j - i) * b) := by
  rw [chirpV, chirpD, mul_apply, Finset.mul_sum]
  refine Finset.sum_congr rfl fun b _ => ?_
  rw [mul_diagonal, conjTranspose_apply, RCLike.star_def, mul_right_comm,
    fourier_conj_mul, mul_assoc]
  congr 1
  rw [← AddChar.map_add_eq_mul]; congr 1; ring

/-- `V_p` is unitary. -/
theorem chirpV_unitary (p : ℕ) [NeZero p] : (chirpV p)ᴴ * chirpV p = 1 := by
  have hD : (chirpD p)ᴴ * chirpD p = 1 := by
    rw [chirpD, diagonal_conjTranspose, diagonal_mul_diagonal, ← diagonal_one]
    congr 1; funext b
    simp only [Pi.star_apply, RCLike.star_def]
    rw [psi_conj, ← AddChar.map_add_eq_mul]; simp
  simp only [chirpV, conjTranspose_mul, conjTranspose_conjTranspose, Matrix.mul_assoc]
  rw [← Matrix.mul_assoc (fourierF p) (fourierF p)ᴴ, fourier_unitary', Matrix.one_mul,
    ← Matrix.mul_assoc (chirpD p)ᴴ, hD, Matrix.one_mul, fourier_unitary]

/-- `V_p` is symmetric: `V_pᵀ = V_p` (replace `b` by `-b` in (O7)). -/
theorem chirpV_transpose (p : ℕ) [NeZero p] : (chirpV p)ᵀ = chirpV p := by
  ext i j
  rw [transpose_apply, chirpV_apply, chirpV_apply]
  congr 1
  exact Fintype.sum_equiv (Equiv.neg _) _ _ (fun b => by
    simp only [Equiv.neg_apply]; congr 1; ring)

/-- Powers of the chirp: `V_p^q = F_p^* D_p^q F_p`. -/
theorem chirpV_pow (p : ℕ) [NeZero p] (q : ℕ) :
    chirpV p ^ q = (fourierF p)ᴴ * (chirpD p) ^ q * fourierF p := by
  induction q with
  | zero => simp [fourier_unitary]
  | succ q ih =>
    rw [pow_succ, ih, pow_succ, chirpV]
    calc (fourierF p)ᴴ * chirpD p ^ q * fourierF p * ((fourierF p)ᴴ * chirpD p * fourierF p)
        = (fourierF p)ᴴ * chirpD p ^ q * (fourierF p * (fourierF p)ᴴ) * chirpD p *
            fourierF p := by simp only [Matrix.mul_assoc]
      _ = _ := by rw [fourier_unitary', Matrix.mul_one]; simp only [Matrix.mul_assoc]

lemma chirpD_pow (p : ℕ) [NeZero p] (q : ℕ) :
    (chirpD p) ^ q = Matrix.diagonal fun b => ψp p (q * b ^ 2) := by
  rw [chirpD, diagonal_pow]
  congr 1; funext b
  simp only [Pi.pow_apply]
  rw [← AddChar.map_nsmul_eq_pow, nsmul_eq_mul]

/-- Trace of a power of the chirp: `Tr V_p^q = ∑_b ψ(q b²)`. -/
theorem chirpV_trace_pow (p : ℕ) [NeZero p] (q : ℕ) :
    (chirpV p ^ q).trace = ∑ b : ZMod p, ψp p (q * b ^ 2) := by
  rw [chirpV_pow, Matrix.trace_mul_cycle, Matrix.mul_assoc, ← Matrix.mul_assoc _ _ (_ ^ q)]
  rw [fourier_unitary', Matrix.one_mul, chirpD_pow, trace_diagonal]

/-- `V_p^p = 1`: the spectrum consists of `p`-th roots of unity. -/
theorem chirpV_pow_p (p : ℕ) [NeZero p] : chirpV p ^ p = 1 := by
  rw [chirpV_pow, chirpD_pow]
  have : (fun b : ZMod p => ψp p ((p : ZMod p) * b ^ 2)) = fun _ => 1 := by
    funext b; simp
  rw [this, diagonal_one, Matrix.mul_one, fourier_unitary]

/-- **Flatness.** Every entry of `V_p` has squared modulus `1/p`. -/
theorem chirpV_entry_normSq (p : ℕ) [Fact p.Prime] (hp2 : p ≠ 2) (i j : ZMod p) :
    Complex.normSq (chirpV p i j) = 1 / p := by
  rw [chirpV_apply, Complex.normSq_mul]
  have := chirp_sum_normSq p hp2 1 (j - i) one_ne_zero
  simp only [one_mul] at this
  rw [this, Complex.normSq_inv, Complex.normSq_natCast]
  have hp : (p : ℝ) ≠ 0 := by exact_mod_cast (Fact.out : p.Prime).ne_zero
  field_simp

/-- **(O9).** If `p ∤ q`, then `|Tr V_p^q|² = p`, i.e. `|Tr V_p^q| = √p`. -/
theorem chirpV_trace_pow_normSq (p : ℕ) [Fact p.Prime] (hp2 : p ≠ 2) (q : ℕ)
    (hq : ¬ p ∣ q) : Complex.normSq ((chirpV p ^ q).trace) = p := by
  rw [chirpV_trace_pow]
  have hq' : (q : ZMod p) ≠ 0 := by
    rwa [Ne, ZMod.natCast_eq_zero_iff]
  have := chirp_sum_normSq p hp2 (q : ZMod p) 0 hq'
  simpa using this

/-- `|Tr V_p^q| = √p` whenever `p ∤ q`. -/
theorem chirpV_trace_pow_norm (p : ℕ) [Fact p.Prime] (hp2 : p ≠ 2) (q : ℕ)
    (hq : ¬ p ∣ q) : ‖(chirpV p ^ q).trace‖ = Real.sqrt p := by
  rw [← chirpV_trace_pow_normSq p hp2 q hq, Complex.normSq_eq_norm_sq,
    Real.sqrt_sq (norm_nonneg _)]

/-! ## The four-dimensional core `H = W/2` -/

/-- The sign matrix `W`. -/
def coreW : Matrix (Fin 4) (Fin 4) ℂ :=
  !![1, 1, 1, 1; 1, -1, -1, 1; 1, 1, -1, -1; 1, -1, 1, -1]

/-- The core `H = W/2`, a real orthogonal flat matrix. -/
noncomputable def coreH : Matrix (Fin 4) (Fin 4) ℂ := (1 / 2 : ℂ) • coreW

/-- The coordinate reversal matrix `B(U)_{ij} = U_{ij} \overline{U_{ji}}`. -/
noncomputable def reversalB {n : Type*} (U : Matrix n n ℂ) : Matrix n n ℂ :=
  fun i j => U i j * (starRingEnd ℂ) (U j i)

/-- The intensity matrix `P(U)_{ij} = |U_{ij}|²`. -/
noncomputable def intensityP {n : Type*} (U : Matrix n n ℂ) : Matrix n n ℝ :=
  fun i j => Complex.normSq (U i j)

/-- `H` is (real) orthogonal: `H Hᵀ = 1`. -/
theorem coreH_mul_transpose : coreH * coreHᵀ = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [coreH, coreW, mul_apply, Fin.sum_univ_four] <;> norm_num

/-- `H` is unitary: `Hᴴ H = 1`. -/
theorem coreH_unitary : coreHᴴ * coreH = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [coreH, coreW, mul_apply, Fin.sum_univ_four, map_ofNat] <;> norm_num

/-- **(O6).** `H²` is the displayed permutation matrix. -/
theorem coreH_sq :
    coreH ^ 2 = !![1, 0, 0, 0; 0, 0, 1, 0; 0, 0, 0, 1; 0, 1, 0, 0] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [pow_two, coreH, coreW, mul_apply, Fin.sum_univ_four] <;> norm_num

/-- **(O6).** `H⁶ = 1`. -/
theorem coreH_pow_six : coreH ^ 6 = 1 := by
  have : coreH ^ 6 = (coreH ^ 2) ^ 3 := by rw [← pow_mul]
  rw [this, coreH_sq]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [pow_succ, mul_apply, Fin.sum_univ_four]

/-- Every entry of `H` has squared modulus `1/4`. -/
theorem coreH_entry_normSq (i j : Fin 4) : Complex.normSq (coreH i j) = 1 / 4 := by
  fin_cases i <;> fin_cases j <;> simp [coreH, coreW, Complex.normSq_apply] <;> norm_num

/-- The reversal core `B(H) = ¼ · (sign matrix)`. -/
theorem reversal_coreH :
    reversalB coreH = (1 / 4 : ℂ) •
      !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [reversalB, coreH, coreW, map_ofNat] <;> norm_num

/-- `B(H) B(H)ᴴ = ¼ · 1`, so `2 B(H)` is unitary and `‖B(H)‖ = 1/2`. -/
theorem reversal_coreH_mul_conjTranspose :
    reversalB coreH * (reversalB coreH)ᴴ = (1 / 4 : ℂ) • 1 := by
  rw [reversal_coreH]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [mul_apply, Fin.sum_univ_four, map_ofNat] <;> norm_num

#print axioms two_ne_zero_zmod
#print axioms sum_psi_mul
#print axioms psi_conj
#print axioms chirp_sum_normSq
#print axioms sqrt_inv_sq
#print axioms conj_sqrt_inv
#print axioms fourier_conj_mul
#print axioms fourier_unitary
#print axioms fourierF_transpose
#print axioms fourier_unitary'
#print axioms chirpV_apply
#print axioms chirpV_unitary
#print axioms chirpV_transpose
#print axioms chirpV_pow
#print axioms chirpD_pow
#print axioms chirpV_trace_pow
#print axioms chirpV_pow_p
#print axioms chirpV_entry_normSq
#print axioms chirpV_trace_pow_normSq
#print axioms chirpV_trace_pow_norm
#print axioms coreH_mul_transpose
#print axioms coreH_unitary
#print axioms coreH_sq
#print axioms coreH_pow_six
#print axioms coreH_entry_normSq
#print axioms reversal_coreH
#print axioms reversal_coreH_mul_conjTranspose
end Bgs.Mathlib
