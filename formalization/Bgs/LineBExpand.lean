import Bgs.LineBGauss

/-!
# Line B: the trace expansion step (`hExpand`) for Theorem 1(a) of 163

This module proves the trace-expansion hypothesis `hExpand` of the wrapper
`Bgs.LineB.Gauss.trace_formula_via_gauss` for a concrete finite-dimensional
model, and the companion identification `hG0def` for the un-kicked trace.

Conventions (exactly the source's, `phase1_trace_formula_src.md` §3):
- `N` is odd (in fact only `[NeZero N]` is used below), `m ≥ 1`.
- The un-kicked matrix is `M_N(x, y) = N^{-1/2} · e_N(a·(3x² − 2xy + 3y²))`
  with `a = −8̄`, i.e. `2 * a * (−4) = 1` in `ZMod N`.
- The kick is a diagonal matrix whose diagonal is the finite Fourier sum
  `∑ k ∈ supp, ĝ k · χ_N(k * x)` for finitely supported Fourier data `ĝ`.
  (For a general kick with `∑ n²|ĝ n| < ∞` the expansion is a `tsum`;
  the finite-support case proved here is exact, and the `tsum` passage
  remains open — see the report.)
- The path sum is over cycles `x : ZMod m → ZMod N`, matching the index
  type of `Bgs.LineB.Gauss.Gsum`.

No `sorry`, no `axiom`, no `native_decide` anywhere in this file.
-/

namespace Bgs.LineB.Expand

open Matrix Finset

/-- Square root of a power: `√(N^m) = (√N)^m` for `N : ℕ`, by induction
using `Real.sqrt_mul` (no positivity beyond `N ≥ 0` is needed). -/
lemma sqrt_pow_nat (N m : ℕ) : Real.sqrt ((N : ℝ) ^ m) = (Real.sqrt (N : ℝ)) ^ m := by
  induction m with
  | zero => simp
  | succ k ih =>
    rw [pow_succ, Real.sqrt_mul (by positivity : (0:ℝ) ≤ (N : ℝ) ^ k), ih, pow_succ]

/-- The normalisation in the wrapper equals the per-factor normalisation
raised to `m`. -/
lemma sqrt_pow_inv (N m : ℕ) :
    (((Real.sqrt ((N : ℝ) ^ m) : ℂ)))⁻¹ = (((Real.sqrt (N : ℝ))⁻¹ : ℂ)) ^ m := by
  rw [sqrt_pow_nat]
  push_cast
  rw [inv_pow]

/-- Additivity of the Gauss character over a finite sum. -/
lemma chi_sum (N : ℕ) [NeZero N] (s : Finset ι) (f : ι → ZMod N) :
    Bgs.LineB.Gauss.chi N (∑ i ∈ s, f i) = ∏ i ∈ s, Bgs.LineB.Gauss.chi N (f i) := by
  classical
  induction s using Finset.induction with
  | empty => simp [Bgs.LineB.Gauss.chi_zero]
  | insert a s ha ih =>
    rw [Finset.sum_insert ha, Bgs.LineB.Gauss.chi_add, ih, Finset.prod_insert ha]

/-- Entries of the frozen-map matrix over `ZMod N`, as a `mulVec` formula:
`(H_N *ᵥ x) i = 6 * x i − x (i+1) − x (i−1)`. -/
lemma H_N_mulVec_apply (m N : ℕ) [NeZero m] [NeZero N] (x : ZMod m → ZMod N)
    (i : ZMod m) :
    (Bgs.LineB.Gauss.H_N m N *ᵥ x) i = 6 * x i - x (i + 1) - x (i - 1) := by
  classical
  have hentry : ∀ j : ZMod m,
      Bgs.LineB.Gauss.H_N m N i j
        = (if i = j then (6 : ZMod N) else 0)
          - (if j = i + 1 then (1 : ZMod N) else 0)
          - (if i = j + 1 then (1 : ZMod N) else 0) := by
    intro j
    show ((Bgs.LineD.Defs.Hmat m ℤ).map ⇑(Bgs.LineB.Gauss.castHom N)) i j = _
    rw [Matrix.map_apply]
    show ((Bgs.LineD.Defs.Hmat m ℤ i j : ℤ) : ZMod N) = _
    have hH : Bgs.LineD.Defs.Hmat m ℤ i j
        = (if i = j then (6 : ℤ) else 0)
          - (if j = i + 1 then (1 : ℤ) else 0)
          - (if i = j + 1 then (1 : ℤ) else 0) := by
      show ((6 : ℤ) • (1 : Matrix (ZMod m) (ZMod m) ℤ)
        - Bgs.LineD.Defs.shiftMat m ℤ
        - (Bgs.LineD.Defs.shiftMat m ℤ)ᵀ) i j = _
      simp only [Matrix.sub_apply, Matrix.smul_apply, smul_eq_mul, Matrix.one_apply,
        Bgs.LineD.Defs.shiftMat, Matrix.of_apply, Matrix.transpose_apply,
        mul_ite, mul_one, mul_zero]
    rw [hH]
    push_cast
    split_ifs <;> simp
  have e0 : ∀ j (_ : j ∈ Finset.univ), Bgs.LineB.Gauss.H_N m N i j * x j
      = (((if i = j then (6 : ZMod N) else 0)
        - (if j = i + 1 then (1 : ZMod N) else 0)
        - (if i = j + 1 then (1 : ZMod N) else 0)) * x j) := by
    intro j _
    rw [hentry j]
  have h6 : ∑ j : ZMod m, (if i = j then (6 : ZMod N) else 0) * x j = 6 * x i := by
    simp only [ite_mul, zero_mul]
    rw [Finset.sum_ite_eq Finset.univ i (fun j => 6 * x j)]
    simp
  have hnext : ∑ j : ZMod m, (if j = i + 1 then (1 : ZMod N) else 0) * x j
      = x (i + 1) := by
    simp only [ite_mul, one_mul, zero_mul]
    rw [Finset.sum_ite_eq' Finset.univ (i + 1) x]
    simp
  have hprev : ∑ j : ZMod m, (if i = j + 1 then (1 : ZMod N) else 0) * x j
      = x (i - 1) := by
    have e : ∀ j (_ : j ∈ Finset.univ),
        (if i = j + 1 then (1 : ZMod N) else 0) * x j
        = (if j = i - 1 then x j else 0) := by
      intro j _
      by_cases h2 : i = j + 1
      · have h3 : j = i - 1 := by rw [h2]; simp
        rw [if_pos h2, if_pos h3]
        simp
      · have h3 : ¬ (j = i - 1) := by
          intro h
          apply h2
          rw [h]
          simp
        rw [if_neg h2, if_neg h3]
        simp
    rw [Finset.sum_congr rfl e, Finset.sum_ite_eq' Finset.univ (i - 1) x]
    simp
  simp only [Matrix.mulVec, dotProduct]
  rw [Finset.sum_congr rfl e0]
  simp only [sub_mul, Finset.sum_sub_distrib]
  rw [h6, hnext, hprev]

/-- Reindexing a sum over `ZMod m` by the successor `+1`. -/
lemma sum_add_one (m : ℕ) [NeZero m] {α : Type*} [AddCommMonoid α] (f : ZMod m → α) :
    ∑ j : ZMod m, f (j + 1) = ∑ j : ZMod m, f j :=
  Equiv.sum_comp (Equiv.addRight (1 : ZMod m)) f

/-- The quadratic form of `H_N` equals the cyclic sum of the cat-map
quadratic form `3x² − 2xy + 3y²` (the source's `M`-product phase). -/
lemma quad_form_eq (m N : ℕ) [NeZero m] [NeZero N] (x : ZMod m → ZMod N) :
    x ⬝ᵥ (Bgs.LineB.Gauss.H_N m N *ᵥ x)
      = ∑ j : ZMod m, (3 * x j ^ 2 - 2 * x j * x (j + 1) + 3 * x (j + 1) ^ 2) := by
  classical
  have hprev : ∑ i : ZMod m, x i * x (i - 1) = ∑ i : ZMod m, x i * x (i + 1) := by
    have h2 := Equiv.sum_comp (Equiv.addRight (1 : ZMod m))
      (fun i : ZMod m => x i * x (i - 1))
    have h : ∑ i : ZMod m, x (i + 1) * x (i + 1 - 1)
        = ∑ i : ZMod m, x i * x (i - 1) := h2
    simp only [add_sub_cancel_right] at h
    rw [← h]
    apply Finset.sum_congr rfl
    intro i _
    rw [mul_comm]
  have hsq3 : ∑ j : ZMod m, 3 * x (j + 1) ^ 2 = ∑ j : ZMod m, 3 * x j ^ 2 :=
    sum_add_one m (fun j => 3 * x j ^ 2)
  have step1 : x ⬝ᵥ (Bgs.LineB.Gauss.H_N m N *ᵥ x)
      = ∑ i, (6 * x i ^ 2 - x i * x (i + 1) - x i * x (i - 1)) := by
    simp only [dotProduct, H_N_mulVec_apply]
    apply Finset.sum_congr rfl
    intro i _
    ring
  have step2 : ∑ i, (6 * x i ^ 2 - x i * x (i + 1) - x i * x (i - 1))
      = (∑ i, 6 * x i ^ 2) - (∑ i, x i * x (i + 1)) - (∑ i, x i * x (i - 1)) := by
    rw [Finset.sum_sub_distrib, Finset.sum_sub_distrib]
  have step3 : ∑ j, (3 * x j ^ 2 - 2 * x j * x (j + 1) + 3 * x (j + 1) ^ 2)
      = (∑ j, 3 * x j ^ 2) - (∑ j, 2 * x j * x (j + 1))
        + (∑ j, 3 * x (j + 1) ^ 2) := by
    rw [Finset.sum_add_distrib, Finset.sum_sub_distrib]
  have h6 : (∑ i, 6 * x i ^ 2) = 2 * (∑ i, 3 * x i ^ 2) := by
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro i _
    ring
  have h2 : (∑ j, 2 * x j * x (j + 1)) = 2 * (∑ j, x j * x (j + 1)) := by
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro j _
    ring
  rw [step1, step2, step3, hprev, hsq3, h6, h2]
  ring

/-- The kick kernel value at `x : ZMod N`: the finite Fourier sum
`∑ k ∈ supp, ĝ k * χ_N(k * x)`. -/
noncomputable def kickVal (N : ℕ) (ĝ : ℤ → ℂ) (supp : Finset ℤ) (x : ZMod N) : ℂ :=
  ∑ k ∈ supp, ĝ k * Bgs.LineB.Gauss.chi N ((k : ZMod N) * x)

/-- The diagonal kick matrix. -/
noncomputable def kickMat (N : ℕ) (ĝ : ℤ → ℂ) (supp : Finset ℤ) :
    Matrix (ZMod N) (ZMod N) ℂ :=
  Matrix.diagonal (kickVal N ĝ supp)

/-- The un-kicked cat matrix `M_N(x, y) = N^{-1/2} · χ_N(a·(3x² − 2xy + 3y²))`. -/
noncomputable def catMat (N : ℕ) (a : ZMod N) : Matrix (ZMod N) (ZMod N) ℂ :=
  Matrix.of fun x y => ((Real.sqrt (N : ℝ) : ℂ))⁻¹ *
    Bgs.LineB.Gauss.chi N (a * (3 * x ^ 2 - 2 * x * y + 3 * y ^ 2))

/-- The Fourier weight of a mode `n : Fin m → ℤ`: the product of `ĝ`
over the cycle positions. -/
noncomputable def phiFun (m : ℕ) [NeZero m] (ĝ : ℤ → ℂ) (n : Fin m → ℤ) : ℂ :=
  ∏ r : ZMod m, ĝ (n (Bgs.LineB.TraceFormula.zmodFinEquiv m r))

/-- A pi-element as a function `Fin m → ℤ` (reindexing by `zmodFinEquiv`). -/
noncomputable def modeFun (m : ℕ) [NeZero m]
    (p : (a : ZMod m) → a ∈ Finset.univ → ℤ) (j : Fin m) : ℤ :=
  p ((Bgs.LineB.TraceFormula.zmodFinEquiv m).symm j) (Finset.mem_univ _)

/-- The finite set of modes `Fin m → ℤ` with values in `supp`. -/
noncomputable def modeSet (m : ℕ) [NeZero m] (supp : Finset ℤ) : Finset (Fin m → ℤ) := by
  classical
  exact (Finset.univ.pi (fun _ : ZMod m => supp)).image (modeFun m)

/-- The Fourier weight of a mode function is the product of `ĝ` over the
pi-element. -/
lemma phiFun_modeFun (m : ℕ) [NeZero m] (ĝ : ℤ → ℂ)
    (p : (a : ZMod m) → a ∈ Finset.univ → ℤ) :
    phiFun m ĝ (modeFun m p) = ∏ r : ZMod m, ĝ (p r (Finset.mem_univ r)) := by
  simp only [phiFun, modeFun]
  apply Finset.prod_congr rfl
  intro r _
  simp only [Equiv.symm_apply_apply]

/-- The Gauss-sum linear term of a mode function is the cast pi-element. -/
lemma nZN_modeFun (m N : ℕ) [NeZero m] [NeZero N]
    (p : (a : ZMod m) → a ∈ Finset.univ → ℤ) :
    Bgs.LineB.Gauss.nZN m N (modeFun m p)
      = fun r => ((p r (Finset.mem_univ r) : ℤ) : ZMod N) := by
  funext r
  simp only [Bgs.LineB.Gauss.nZN_apply, Bgs.LineB.Gauss.nZ_apply, modeFun]
  simp only [Equiv.symm_apply_apply]

/-- The mode function is injective (no pi-membership needed). -/
lemma modeFun_inj (m : ℕ) [NeZero m]
    (p p' : (a : ZMod m) → a ∈ Finset.univ → ℤ)
    (h : modeFun m p = modeFun m p') : p = p' := by
  funext r hr
  have hcongr := congrFun h (Bgs.LineB.TraceFormula.zmodFinEquiv m r)
  have e1 : modeFun m p (Bgs.LineB.TraceFormula.zmodFinEquiv m r) = p r hr := by
    simp only [modeFun]
    simp only [Equiv.symm_apply_apply]
  have e2 : modeFun m p' (Bgs.LineB.TraceFormula.zmodFinEquiv m r) = p' r hr := by
    simp only [modeFun]
    simp only [Equiv.symm_apply_apply]
  rw [← e1, hcongr, e2]

/-- `Fin.snoc` for a constant family, with the family pinned explicitly:
with the dependent `Fin.snoc`, elaboration of `Fin.snoc q b` for a constant
`q` has to guess the family and fails. -/
def snocC {n : ℕ} {β : Type*} (q : Fin n → β) (b : β) : Fin (n + 1) → β :=
  Fin.snoc (α := fun _ => β) q b

lemma snocC_castSucc {n : ℕ} {β : Type*} (q : Fin n → β) (b : β) (i : Fin n) :
    snocC q b i.castSucc = q i :=
  Fin.snoc_castSucc (α := fun _ => β) b q i

lemma snocC_last {n : ℕ} {β : Type*} (q : Fin n → β) (b : β) :
    snocC q b (Fin.last n) = b :=
  Fin.snoc_last (α := fun _ => β) b q

lemma snocC_zero {n : ℕ} {β : Type*} (q : Fin (n + 1) → β) (b : β) :
    snocC q b 0 = q 0 := by
  have h := Fin.snoc_castSucc (α := fun _ => β) b q (0 : Fin (n + 1))
  rwa [Fin.castSucc_zero] at h

/-- Path expansion of a matrix power: `(A ^ p) a b` is the sum over paths
`q : Fin (p + 1) → ZMod N` from `a` to `b` of the product of the entries
along the path. -/
lemma pow_apply_path (A : Matrix (ZMod N) (ZMod N) ℂ) (p : ℕ) [NeZero N] (a b : ZMod N) :
    (A ^ p) a b = ∑ q : Fin (p + 1) → ZMod N,
      (if q 0 = a ∧ q (Fin.last p) = b then
        ∏ j : Fin p, A (q j.castSucc) (q j.succ) else 0) := by
  induction p generalizing a b with
  | zero =>
    have h₀ : ∀ q ∈ (Finset.univ : Finset (Fin 1 → ZMod N)), q ≠ (fun _ => a) →
        (if q 0 = a ∧ q (Fin.last 0) = b then
          ∏ j : Fin 0, A (q j.castSucc) (q j.succ) else 0) = 0 := by
      intro q _ hq
      have hq0 : q 0 ≠ a := by
        intro h
        apply hq
        funext i
        have hi : i = 0 := Subsingleton.elim i 0
        rw [hi]
        exact h
      simp [hq0]
    have h₁ : (fun _ => a) ∉ (Finset.univ : Finset (Fin 1 → ZMod N)) →
        (if (fun _ => a) 0 = a ∧ (fun _ => a) (Fin.last 0) = b then
          ∏ j : Fin 0, A ((fun _ => a) j.castSucc) ((fun _ => a) j.succ) else 0) = 0 := by
      intro h
      simp at h
    simp only [pow_zero, Matrix.one_apply]
    rw [Finset.sum_eq_single (fun _ => a) h₀ h₁]
    by_cases hab : a = b
    · simp [hab]
    · simp [hab]
  | succ p ih =>
    rw [pow_succ, Matrix.mul_apply]
    have step1 : ∑ c, (A ^ p) a c * A c b
        = ∑ c, (∑ q : Fin (p + 1) → ZMod N,
            (if q 0 = a ∧ q (Fin.last p) = c then
              ∏ j : Fin p, A (q j.castSucc) (q j.succ) else 0)) * A c b := by
      apply Finset.sum_congr rfl
      intro c _
      rw [ih]
    have step1b : ∑ c, (∑ q : Fin (p + 1) → ZMod N,
            (if q 0 = a ∧ q (Fin.last p) = c then
              ∏ j : Fin p, A (q j.castSucc) (q j.succ) else 0)) * A c b
        = ∑ c, ∑ q : Fin (p + 1) → ZMod N,
            (if q 0 = a ∧ q (Fin.last p) = c then
              ∏ j : Fin p, A (q j.castSucc) (q j.succ) else 0) * A c b := by
      apply Finset.sum_congr rfl
      intro c _
      rw [Finset.sum_mul]
    rw [step1, step1b, Finset.sum_comm]
    have step2 : ∀ q : Fin (p + 1) → ZMod N,
        (∑ c, (if q 0 = a ∧ q (Fin.last p) = c then
          ∏ j : Fin p, A (q j.castSucc) (q j.succ) else 0) * A c b)
        = (if q 0 = a then
            (∏ j : Fin p, A (q j.castSucc) (q j.succ)) * A (q (Fin.last p)) b else 0) := by
      intro q
      by_cases hqa : q 0 = a
      · have e : ∀ c (_ : c ∈ Finset.univ),
            (if q 0 = a ∧ q (Fin.last p) = c then
              ∏ j : Fin p, A (q j.castSucc) (q j.succ) else 0) * A c b
            = (if q (Fin.last p) = c then
                (∏ j : Fin p, A (q j.castSucc) (q j.succ)) * A c b else 0) := by
          intro c _
          by_cases hqc : q (Fin.last p) = c
          · rw [if_pos ⟨hqa, hqc⟩, if_pos hqc]
          · rw [if_neg (by intro h; exact hqc h.2), if_neg hqc]
            simp
        rw [Finset.sum_congr rfl e,
          Finset.sum_ite_eq Finset.univ (q (Fin.last p))
            (fun c => (∏ j : Fin p, A (q j.castSucc) (q j.succ)) * A c b)]
        simp [hqa]
      · have e : ∀ c (_ : c ∈ Finset.univ),
            (if q 0 = a ∧ q (Fin.last p) = c then
              ∏ j : Fin p, A (q j.castSucc) (q j.succ) else 0) * A c b = 0 := by
          intro c _
          rw [if_neg (by intro h; exact hqa h.1)]
          simp
        rw [Finset.sum_congr rfl e]
        simp [hqa]
    rw [Finset.sum_congr rfl (fun q _ => step2 q)]
    have hsnoc : ∀ (q : Fin (p + 1) → ZMod N) (b' : ZMod N),
        (if (snocC q b') 0 = a ∧ (snocC q b') (Fin.last (p + 1)) = b then
          ∏ j : Fin (p + 1), A ((snocC q b') j.castSucc) ((snocC q b') j.succ) else 0)
        = (if q 0 = a ∧ b' = b then
            (∏ j : Fin p, A (q j.castSucc) (q j.succ)) * A (q (Fin.last p)) b' else 0) := by
      intro q b'
      have h0 : (snocC q b') 0 = q 0 := snocC_zero q b'
      have hlast : (snocC q b') (Fin.last (p + 1)) = b' := snocC_last q b'
      have hprod : ∏ j : Fin (p + 1), A ((snocC q b') j.castSucc) ((snocC q b') j.succ)
          = (∏ j : Fin p, A (q j.castSucc) (q j.succ)) * A (q (Fin.last p)) b' := by
        rw [Fin.prod_univ_castSucc]
        congr 1
        · apply Finset.prod_congr rfl
          intro j _
          have e1 : (snocC q b') j.castSucc.castSucc = q j.castSucc :=
            snocC_castSucc q b' j.castSucc
          have e2 : (snocC q b') j.castSucc.succ = q j.succ := by
            rw [Fin.succ_castSucc]
            exact snocC_castSucc q b' j.succ
          rw [e1, e2]
        · have e1 : (snocC q b') (Fin.last p).castSucc = q (Fin.last p) :=
            snocC_castSucc q b' (Fin.last p)
          have e2 : (snocC q b') (Fin.last p).succ = b' := by
            have hlastsucc : (Fin.last p).succ = Fin.last (p + 1) := rfl
            rw [hlastsucc]
            exact snocC_last q b'
          rw [e1, e2]
      rw [h0, hlast, hprod]
    have hsum : (∑ q' : Fin (p + 2) → ZMod N,
          (if q' 0 = a ∧ q' (Fin.last (p + 1)) = b then
            ∏ j : Fin (p + 1), A (q' j.castSucc) (q' j.succ) else 0))
        = ∑ x : ZMod N × (Fin (p + 1) → ZMod N),
          (if x.2 0 = a ∧ x.1 = b then
            (∏ j : Fin p, A (x.2 j.castSucc) (x.2 j.succ)) * A (x.2 (Fin.last p)) x.1 else 0) :=
      (Fintype.sum_equiv (Fin.snocEquiv (fun _ => ZMod N)) _ _
        (fun ⟨b', q⟩ => (hsnoc q b').symm)).symm
    have hprod : (∑ x : ZMod N × (Fin (p + 1) → ZMod N),
          (if x.2 0 = a ∧ x.1 = b then
            (∏ j : Fin p, A (x.2 j.castSucc) (x.2 j.succ)) * A (x.2 (Fin.last p)) x.1 else 0))
        = ∑ q : Fin (p + 1) → ZMod N,
          (if q 0 = a then
            (∏ j : Fin p, A (q j.castSucc) (q j.succ)) * A (q (Fin.last p)) b else 0) := by
      rw [Fintype.sum_prod_type, Finset.sum_comm]
      apply Finset.sum_congr rfl
      intro q _
      by_cases hqa : q 0 = a
      · have e : ∀ b' (_ : b' ∈ Finset.univ),
            (if q 0 = a ∧ b' = b then
              (∏ j : Fin p, A (q j.castSucc) (q j.succ)) * A (q (Fin.last p)) b' else 0)
            = (if b' = b then
              (∏ j : Fin p, A (q j.castSucc) (q j.succ)) * A (q (Fin.last p)) b' else 0) := by
          intro b' _
          by_cases hbb : b' = b
          · rw [if_pos ⟨hqa, hbb⟩, if_pos hbb]
          · rw [if_neg (by intro h; exact hbb h.2), if_neg hbb]
        rw [Finset.sum_congr rfl e, Finset.sum_ite_eq' Finset.univ b
          (fun b' => (∏ j : Fin p, A (q j.castSucc) (q j.succ)) * A (q (Fin.last p)) b')]
        simp [hqa]
      · have e : ∀ b' (_ : b' ∈ Finset.univ),
            (if q 0 = a ∧ b' = b then
              (∏ j : Fin p, A (q j.castSucc) (q j.succ)) * A (q (Fin.last p)) b' else 0) = 0 := by
          intro b' _
          rw [if_neg (by intro h; exact hqa h.1)]
        rw [Finset.sum_congr rfl e]
        simp [hqa]
    exact hprod.symm.trans hsum.symm

/-- Value of `r + 1` in `ZMod m`, as a natural number. -/
lemma zmod_add_one_val (m : ℕ) [NeZero m] (r : ZMod m) :
    (r + 1).val = (r.val + 1) % m := by
  have h : (r + 1 : ZMod m) = (((r.val + 1 : ℕ)) : ZMod m) := by
    conv_lhs => rw [← ZMod.natCast_zmod_val r]
    push_cast
    ring
  rw [h]
  exact ZMod.val_natCast m (r.val + 1)

/-- The value of `zmodFinEquiv m s` is `s.val` (definitional). -/
lemma zmodFinEquiv_val (m : ℕ) [NeZero m] (s : ZMod m) :
    (Bgs.LineB.TraceFormula.zmodFinEquiv m s).val = s.val := rfl

/-- Closed paths of length `m` (paths `q : Fin (m+1) → ZMod N` with
`q (last) = q 0`) are the same as cycles `ZMod m → ZMod N`. -/
def closedPathEquiv (m N : ℕ) [NeZero m] [NeZero N] :
    {q : Fin (m + 1) → ZMod N // q (Fin.last m) = q 0} ≃ (ZMod m → ZMod N) where
  toFun q r := q.1 ((Bgs.LineB.TraceFormula.zmodFinEquiv m r).castSucc)
  invFun x := ⟨fun i => x ((i.val : ℕ) : ZMod m), by
    show x (((Fin.last m).val : ℕ) : ZMod m) = x (((0 : Fin (m + 1)).val : ℕ) : ZMod m)
    simp⟩
  left_inv q := by
    apply Subtype.ext
    funext i
    show q.1 ((Bgs.LineB.TraceFormula.zmodFinEquiv m ((i.val : ℕ) : ZMod m)).castSucc)
      = q.1 i
    have hval : (Bgs.LineB.TraceFormula.zmodFinEquiv m ((i.val : ℕ) : ZMod m)).val
        = i.val % m := by
      show ((i.val : ℕ) : ZMod m).val = i.val % m
      exact ZMod.val_natCast m i.val
    by_cases hi : i.val < m
    · have heq : (Bgs.LineB.TraceFormula.zmodFinEquiv m ((i.val : ℕ) : ZMod m)).castSucc
          = i := by
        apply Fin.ext
        simp [Fin.val_castSucc, hval, Nat.mod_eq_of_lt hi]
      rw [heq]
    · have him : i.val = m := by
        have hle : i.val ≤ m := Nat.le_of_lt_succ i.isLt
        omega
      have hi2 : i = Fin.last m := by
        apply Fin.ext
        simp [him]
      have hmod : i.val % m = 0 := by rw [him]; exact Nat.mod_self m
      have hidx : (Bgs.LineB.TraceFormula.zmodFinEquiv m ((i.val : ℕ) : ZMod m)).castSucc
          = 0 := by
        apply Fin.ext
        simp [Fin.val_castSucc, hval, hmod]
      rw [hidx, hi2]
      exact q.2.symm
  right_inv x := by
    funext r
    show x ((((Bgs.LineB.TraceFormula.zmodFinEquiv m r).castSucc).val : ℕ) : ZMod m)
      = x r
    rw [Fin.val_castSucc]
    congr 1
    show (((Bgs.LineB.TraceFormula.zmodFinEquiv m r).val : ℕ) : ZMod m) = r
    have hval : (Bgs.LineB.TraceFormula.zmodFinEquiv m r).val = r.val := rfl
    rw [hval]
    exact ZMod.natCast_zmod_val r

/-- The trace of a matrix power is the sum over cycles of the product of
the entries along the cycle. -/
lemma trace_pow_cycle (A : Matrix (ZMod N) (ZMod N) ℂ) (m : ℕ) [NeZero m] [NeZero N] :
    Matrix.trace (A ^ m)
      = ∑ x : ZMod m → ZMod N, ∏ j : ZMod m, A (x j) (x (j + 1)) := by
  classical
  have htrace : Matrix.trace (A ^ m) = ∑ a, (A ^ m) a a := by
    simp [Matrix.trace, Matrix.diag]
  rw [htrace]
  have step1 : (∑ a, (A ^ m) a a)
      = ∑ a, ∑ q : Fin (m + 1) → ZMod N,
          (if q 0 = a ∧ q (Fin.last m) = a then
            ∏ j : Fin m, A (q j.castSucc) (q j.succ) else 0) := by
    apply Finset.sum_congr rfl
    intro a _
    rw [pow_apply_path]
  rw [step1, Finset.sum_comm]
  have inner : ∀ q : Fin (m + 1) → ZMod N,
      (∑ a, (if q 0 = a ∧ q (Fin.last m) = a then
        ∏ j : Fin m, A (q j.castSucc) (q j.succ) else 0))
      = (if q (Fin.last m) = q 0 then
          ∏ j : Fin m, A (q j.castSucc) (q j.succ) else 0) := by
    intro q
    by_cases h : q (Fin.last m) = q 0
    · have e : ∀ a (_ : a ∈ Finset.univ),
          (if q 0 = a ∧ q (Fin.last m) = a then
            ∏ j : Fin m, A (q j.castSucc) (q j.succ) else 0)
          = (if q 0 = a then
              ∏ j : Fin m, A (q j.castSucc) (q j.succ) else 0) := by
        intro a _
        by_cases ha : q 0 = a
        · rw [if_pos ⟨ha, by rw [h]; exact ha⟩, if_pos ha]
        · rw [if_neg (by intro hh; exact ha hh.1), if_neg ha]
      rw [Finset.sum_congr rfl e,
        Finset.sum_ite_eq Finset.univ (q 0)
          (fun _ => ∏ j : Fin m, A (q j.castSucc) (q j.succ))]
      simp [h]
    · have e : ∀ a (_ : a ∈ Finset.univ),
          (if q 0 = a ∧ q (Fin.last m) = a then
            ∏ j : Fin m, A (q j.castSucc) (q j.succ) else 0) = 0 := by
        intro a _
        rw [if_neg (by intro hh; exact h (hh.2.trans hh.1.symm))]
      rw [Finset.sum_congr rfl e]
      simp [h]
  rw [Finset.sum_congr rfl (fun q _ => inner q)]
  have hsub : (∑ q : Fin (m + 1) → ZMod N,
        (if q (Fin.last m) = q 0 then
          ∏ j : Fin m, A (q j.castSucc) (q j.succ) else 0))
      = ∑ q : {q : Fin (m + 1) → ZMod N // q (Fin.last m) = q 0},
          ∏ j : Fin m, A (q.1 j.castSucc) (q.1 j.succ) := by
    have hfilter : (∑ q : Fin (m + 1) → ZMod N,
          (if q (Fin.last m) = q 0 then
            ∏ j : Fin m, A (q j.castSucc) (q j.succ) else 0))
        = ∑ q ∈ Finset.univ.filter (fun q : Fin (m + 1) → ZMod N => q (Fin.last m) = q 0),
            ∏ j : Fin m, A (q j.castSucc) (q j.succ) := by
      rw [Finset.sum_filter]
    rw [hfilter]
    have hmem : ∀ q : Fin (m + 1) → ZMod N,
        q ∈ Finset.univ.filter (fun q : Fin (m + 1) → ZMod N => q (Fin.last m) = q 0)
          ↔ q (Fin.last m) = q 0 := by
      intro q
      simp [Finset.mem_filter]
    exact Finset.sum_subtype _ hmem _
  rw [hsub]
  rw [← Fintype.sum_equiv (closedPathEquiv m N)
    (fun q : {q : Fin (m + 1) → ZMod N // q (Fin.last m) = q 0} =>
      ∏ j : Fin m, A (q.1 j.castSucc) (q.1 j.succ))
    (fun x : ZMod m → ZMod N => ∏ r : ZMod m, A (x r) (x (r + 1))) ?_]
  intro q
  have hsucc : ∀ r : ZMod m,
      q.1 ((Bgs.LineB.TraceFormula.zmodFinEquiv m (r + 1)).castSucc)
        = q.1 ((Bgs.LineB.TraceFormula.zmodFinEquiv m r).succ) := by
    intro r
    by_cases hr : r.val + 1 < m
    · have heq : (Bgs.LineB.TraceFormula.zmodFinEquiv m (r + 1)).castSucc
          = (Bgs.LineB.TraceFormula.zmodFinEquiv m r).succ := by
        apply Fin.ext
        simp [Fin.val_castSucc, Fin.val_succ, zmodFinEquiv_val, zmod_add_one_val,
          Nat.mod_eq_of_lt hr]
      rw [heq]
    · have hr2 : r.val + 1 = m := by
        have hlt : r.val < m := ZMod.val_lt r
        omega
      have e1 : (Bgs.LineB.TraceFormula.zmodFinEquiv m (r + 1)).castSucc = 0 := by
        apply Fin.ext
        simp [Fin.val_castSucc, zmodFinEquiv_val, zmod_add_one_val, hr2]
      have e2 : (Bgs.LineB.TraceFormula.zmodFinEquiv m r).succ = Fin.last m := by
        apply Fin.ext
        simp [Fin.val_succ, zmodFinEquiv_val, hr2]
      rw [e1, e2]
      exact q.2.symm
  have hprod : (∏ r : ZMod m, A ((closedPathEquiv m N q) r) ((closedPathEquiv m N q) (r + 1)))
      = ∏ j : Fin m, A (q.1 j.castSucc) (q.1 j.succ) := by
    have h1 : (∏ r : ZMod m, A ((closedPathEquiv m N q) r) ((closedPathEquiv m N q) (r + 1)))
        = ∏ r : ZMod m,
            A (q.1 ((Bgs.LineB.TraceFormula.zmodFinEquiv m r).castSucc))
              (q.1 ((Bgs.LineB.TraceFormula.zmodFinEquiv m r).succ)) := by
      apply Finset.prod_congr rfl
      intro r _
      show A (q.1 ((Bgs.LineB.TraceFormula.zmodFinEquiv m r).castSucc))
              (q.1 ((Bgs.LineB.TraceFormula.zmodFinEquiv m (r + 1)).castSucc))
          = A (q.1 ((Bgs.LineB.TraceFormula.zmodFinEquiv m r).castSucc))
              (q.1 ((Bgs.LineB.TraceFormula.zmodFinEquiv m r).succ))
      rw [hsucc]
    rw [h1]
    exact Fintype.prod_equiv (Bgs.LineB.TraceFormula.zmodFinEquiv m)
      (fun r => A (q.1 ((Bgs.LineB.TraceFormula.zmodFinEquiv m r).castSucc))
        (q.1 ((Bgs.LineB.TraceFormula.zmodFinEquiv m r).succ)))
      (fun j => A (q.1 j.castSucc) (q.1 j.succ))
      (fun r => rfl)
  exact hprod.symm

/-- The kicked matrix acts as kick times cat on each entry. -/
lemma kick_cat_apply (N : ℕ) [NeZero N] (ĝ : ℤ → ℂ) (supp : Finset ℤ) (a : ZMod N)
    (x y : ZMod N) :
    (kickMat N ĝ supp * catMat N a) x y
      = kickVal N ĝ supp x * catMat N a x y := by
  simp only [kickMat, Matrix.mul_apply]
  rw [Finset.sum_eq_single x]
  · rw [Matrix.diagonal_apply_eq]
  · intro k _ hkx
    rw [Matrix.diagonal_apply_ne (kickVal N ĝ supp) (fun h => hkx h.symm)]
    simp
  · intro h
    simp at h

/-- The product of the cat entries along a cycle is the normalisation
times the character of the quadratic form (via `quad_form_eq`). -/
lemma catMat_prod (m N : ℕ) [NeZero m] [NeZero N] (a : ZMod N) (x : ZMod m → ZMod N) :
    ∏ j : ZMod m, catMat N a (x j) (x (j + 1))
      = (((Real.sqrt (N : ℝ) : ℂ))⁻¹) ^ m *
        Bgs.LineB.Gauss.chi N
          (a * Bgs.LineB.Gauss.Qform (Bgs.LineB.Gauss.H_N m N) x) := by
  have hentry : ∀ j : ZMod m, catMat N a (x j) (x (j + 1))
      = ((Real.sqrt (N : ℝ) : ℂ))⁻¹ *
        Bgs.LineB.Gauss.chi N
          (a * (3 * x j ^ 2 - 2 * x j * x (j + 1) + 3 * x (j + 1) ^ 2)) := by
    intro j
    rfl
  have hsum : (∑ j : ZMod m,
        a * (3 * x j ^ 2 - 2 * x j * x (j + 1) + 3 * x (j + 1) ^ 2))
      = a * Bgs.LineB.Gauss.Qform (Bgs.LineB.Gauss.H_N m N) x := by
    rw [← Finset.mul_sum]
    congr 1
    exact (quad_form_eq m N x).symm
  rw [Finset.prod_congr rfl (fun j _ => hentry j), Finset.prod_mul_distrib,
    Finset.prod_const, Finset.card_univ, ZMod.card, ← chi_sum, hsum]

/-- The product of the kick values along a cycle expands into the sum
over Fourier modes (`Finset.prod_sum` + proof-irrelevance for the
`attach` product). -/
lemma kickVal_prod (m N : ℕ) [NeZero m] [NeZero N] (ĝ : ℤ → ℂ) (supp : Finset ℤ)
    (x : ZMod m → ZMod N) :
    ∏ j : ZMod m, kickVal N ĝ supp (x j)
      = ∑ p ∈ Finset.univ.pi (fun _ : ZMod m => supp),
          (∏ j : ZMod m, ĝ (p j (Finset.mem_univ j))) *
            Bgs.LineB.Gauss.chi N
              (∑ j : ZMod m, ((p j (Finset.mem_univ j) : ℤ) : ZMod N) * x j) := by
  simp only [kickVal]
  rw [Finset.prod_sum]
  apply Finset.sum_congr rfl
  intro p _
  have hconv : (∏ x_1 ∈ (Finset.univ : Finset (ZMod m)).attach,
        (ĝ (p ↑x_1 x_1.2) *
          Bgs.LineB.Gauss.chi N (((p ↑x_1 x_1.2 : ℤ) : ZMod N) * x ↑x_1)))
      = ∏ j : ZMod m, (ĝ (p j (Finset.mem_univ j)) *
          Bgs.LineB.Gauss.chi N (((p j (Finset.mem_univ j) : ℤ) : ZMod N) * x j)) := by
    rw [show (∏ x_1 ∈ (Finset.univ : Finset (ZMod m)).attach,
          (ĝ (p ↑x_1 x_1.2) *
            Bgs.LineB.Gauss.chi N (((p ↑x_1 x_1.2 : ℤ) : ZMod N) * x ↑x_1)))
        = ∏ x_1 ∈ (Finset.univ : Finset (ZMod m)).attach,
          (fun j : ZMod m => ĝ (p j (Finset.mem_univ j)) *
            Bgs.LineB.Gauss.chi N (((p j (Finset.mem_univ j) : ℤ) : ZMod N) * x j)) ↑x_1
        from Finset.prod_congr rfl (fun x_1 _ => rfl)]
    rw [Finset.prod_attach (Finset.univ : Finset (ZMod m))
      (fun j : ZMod m => ĝ (p j (Finset.mem_univ j)) *
        Bgs.LineB.Gauss.chi N (((p j (Finset.mem_univ j) : ℤ) : ZMod N) * x j))]
  rw [hconv, Finset.prod_mul_distrib, ← chi_sum]

/-- The trace of the kicked matrix, expanded: normalisation times the
sum over Fourier modes of the weight times the Gauss sum. -/
lemma trace_expand (m N : ℕ) [NeZero m] [NeZero N] (ĝ : ℤ → ℂ) (supp : Finset ℤ)
    (a : ZMod N) :
    Matrix.trace ((kickMat N ĝ supp * catMat N a) ^ m)
      = (((Real.sqrt (N : ℝ) : ℂ))⁻¹) ^ m *
        ∑ p ∈ Finset.univ.pi (fun _ : ZMod m => supp),
          (∏ j : ZMod m, ĝ (p j (Finset.mem_univ j))) *
            Bgs.LineB.Gauss.Gsum (Bgs.LineB.Gauss.H_N m N) a
              (Bgs.LineB.Gauss.nZN m N (modeFun m p)) := by
  rw [trace_pow_cycle]
  have step1 : (∑ x : ZMod m → ZMod N, ∏ j : ZMod m,
        (kickMat N ĝ supp * catMat N a) (x j) (x (j + 1)))
      = ∑ x : ZMod m → ZMod N, (∏ j : ZMod m, kickVal N ĝ supp (x j)) *
          (∏ j : ZMod m, catMat N a (x j) (x (j + 1))) := by
    apply Finset.sum_congr rfl
    intro x _
    rw [Finset.prod_congr rfl (fun j _ => kick_cat_apply N ĝ supp a (x j) (x (j + 1)))]
    rw [Finset.prod_mul_distrib]
  rw [step1]
  have step2 : (∑ x : ZMod m → ZMod N, (∏ j : ZMod m, kickVal N ĝ supp (x j)) *
        (∏ j : ZMod m, catMat N a (x j) (x (j + 1))))
      = ∑ x : ZMod m → ZMod N, (∏ j : ZMod m, kickVal N ĝ supp (x j)) *
          ((((Real.sqrt (N : ℝ) : ℂ))⁻¹) ^ m *
            Bgs.LineB.Gauss.chi N (a * Bgs.LineB.Gauss.Qform (Bgs.LineB.Gauss.H_N m N) x)) := by
    apply Finset.sum_congr rfl
    intro x _
    rw [catMat_prod]
  rw [step2]
  have step3 : (∑ x : ZMod m → ZMod N, (∏ j : ZMod m, kickVal N ĝ supp (x j)) *
        ((((Real.sqrt (N : ℝ) : ℂ))⁻¹) ^ m *
          Bgs.LineB.Gauss.chi N (a * Bgs.LineB.Gauss.Qform (Bgs.LineB.Gauss.H_N m N) x)))
      = ∑ x : ZMod m → ZMod N,
          (∑ p ∈ Finset.univ.pi (fun _ : ZMod m => supp),
            (∏ j : ZMod m, ĝ (p j (Finset.mem_univ j))) *
              Bgs.LineB.Gauss.chi N
                (∑ j : ZMod m, ((p j (Finset.mem_univ j) : ℤ) : ZMod N) * x j)) *
          ((((Real.sqrt (N : ℝ) : ℂ))⁻¹) ^ m *
            Bgs.LineB.Gauss.chi N (a * Bgs.LineB.Gauss.Qform (Bgs.LineB.Gauss.H_N m N) x)) := by
    apply Finset.sum_congr rfl
    intro x _
    rw [kickVal_prod]
  rw [step3]
  have step4 : (∑ x : ZMod m → ZMod N,
        (∑ p ∈ Finset.univ.pi (fun _ : ZMod m => supp),
          (∏ j : ZMod m, ĝ (p j (Finset.mem_univ j))) *
            Bgs.LineB.Gauss.chi N
              (∑ j : ZMod m, ((p j (Finset.mem_univ j) : ℤ) : ZMod N) * x j)) *
        ((((Real.sqrt (N : ℝ) : ℂ))⁻¹) ^ m *
          Bgs.LineB.Gauss.chi N (a * Bgs.LineB.Gauss.Qform (Bgs.LineB.Gauss.H_N m N) x)))
      = ∑ p ∈ Finset.univ.pi (fun _ : ZMod m => supp), ∑ x : ZMod m → ZMod N,
          ((∏ j : ZMod m, ĝ (p j (Finset.mem_univ j))) *
            Bgs.LineB.Gauss.chi N
              (∑ j : ZMod m, ((p j (Finset.mem_univ j) : ℤ) : ZMod N) * x j)) *
          ((((Real.sqrt (N : ℝ) : ℂ))⁻¹) ^ m *
            Bgs.LineB.Gauss.chi N (a * Bgs.LineB.Gauss.Qform (Bgs.LineB.Gauss.H_N m N) x)) := by
    have e : ∀ x : ZMod m → ZMod N,
        (∑ p ∈ Finset.univ.pi (fun _ : ZMod m => supp),
          (∏ j : ZMod m, ĝ (p j (Finset.mem_univ j))) *
            Bgs.LineB.Gauss.chi N
              (∑ j : ZMod m, ((p j (Finset.mem_univ j) : ℤ) : ZMod N) * x j)) *
        ((((Real.sqrt (N : ℝ) : ℂ))⁻¹) ^ m *
          Bgs.LineB.Gauss.chi N (a * Bgs.LineB.Gauss.Qform (Bgs.LineB.Gauss.H_N m N) x))
        = ∑ p ∈ Finset.univ.pi (fun _ : ZMod m => supp),
          ((∏ j : ZMod m, ĝ (p j (Finset.mem_univ j))) *
            Bgs.LineB.Gauss.chi N
              (∑ j : ZMod m, ((p j (Finset.mem_univ j) : ℤ) : ZMod N) * x j)) *
          ((((Real.sqrt (N : ℝ) : ℂ))⁻¹) ^ m *
            Bgs.LineB.Gauss.chi N (a * Bgs.LineB.Gauss.Qform (Bgs.LineB.Gauss.H_N m N) x)) := by
      intro x
      rw [Finset.sum_mul]
    rw [Finset.sum_congr rfl (fun x _ => e x), Finset.sum_comm]
  rw [step4]
  have step5 : ∀ p ∈ Finset.univ.pi (fun _ : ZMod m => supp),
      (∑ x : ZMod m → ZMod N,
        ((∏ j : ZMod m, ĝ (p j (Finset.mem_univ j))) *
          Bgs.LineB.Gauss.chi N
            (∑ j : ZMod m, ((p j (Finset.mem_univ j) : ℤ) : ZMod N) * x j)) *
        ((((Real.sqrt (N : ℝ) : ℂ))⁻¹) ^ m *
          Bgs.LineB.Gauss.chi N (a * Bgs.LineB.Gauss.Qform (Bgs.LineB.Gauss.H_N m N) x)))
      = (((Real.sqrt (N : ℝ) : ℂ))⁻¹) ^ m *
        ((∏ j : ZMod m, ĝ (p j (Finset.mem_univ j))) *
          Bgs.LineB.Gauss.Gsum (Bgs.LineB.Gauss.H_N m N) a
            (Bgs.LineB.Gauss.nZN m N (modeFun m p))) := by
    intro p _
    have hdot : ∀ x : ZMod m → ZMod N,
        (∑ j : ZMod m, ((p j (Finset.mem_univ j) : ℤ) : ZMod N) * x j)
          = (Bgs.LineB.Gauss.nZN m N (modeFun m p)) ⬝ᵥ x := by
      intro x
      rw [nZN_modeFun]
      simp only [dotProduct]
    have esum : (∑ x : ZMod m → ZMod N,
          ((∏ j : ZMod m, ĝ (p j (Finset.mem_univ j))) *
            Bgs.LineB.Gauss.chi N
              (∑ j : ZMod m, ((p j (Finset.mem_univ j) : ℤ) : ZMod N) * x j)) *
          ((((Real.sqrt (N : ℝ) : ℂ))⁻¹) ^ m *
            Bgs.LineB.Gauss.chi N (a * Bgs.LineB.Gauss.Qform (Bgs.LineB.Gauss.H_N m N) x)))
        = ((((Real.sqrt (N : ℝ) : ℂ))⁻¹) ^ m *
            (∏ j : ZMod m, ĝ (p j (Finset.mem_univ j)))) *
          ∑ x : ZMod m → ZMod N,
            Bgs.LineB.Gauss.chi N
              (a * Bgs.LineB.Gauss.Qform (Bgs.LineB.Gauss.H_N m N) x +
                (Bgs.LineB.Gauss.nZN m N (modeFun m p)) ⬝ᵥ x) := by
      have e : ∀ x : ZMod m → ZMod N,
          ((∏ j : ZMod m, ĝ (p j (Finset.mem_univ j))) *
            Bgs.LineB.Gauss.chi N
              (∑ j : ZMod m, ((p j (Finset.mem_univ j) : ℤ) : ZMod N) * x j)) *
          ((((Real.sqrt (N : ℝ) : ℂ))⁻¹) ^ m *
            Bgs.LineB.Gauss.chi N (a * Bgs.LineB.Gauss.Qform (Bgs.LineB.Gauss.H_N m N) x))
          = ((((Real.sqrt (N : ℝ) : ℂ))⁻¹) ^ m *
              (∏ j : ZMod m, ĝ (p j (Finset.mem_univ j)))) *
            Bgs.LineB.Gauss.chi N
              (a * Bgs.LineB.Gauss.Qform (Bgs.LineB.Gauss.H_N m N) x +
                (Bgs.LineB.Gauss.nZN m N (modeFun m p)) ⬝ᵥ x) := by
        intro x
        rw [hdot]
        have hchi : Bgs.LineB.Gauss.chi N
              (a * Bgs.LineB.Gauss.Qform (Bgs.LineB.Gauss.H_N m N) x +
                (Bgs.LineB.Gauss.nZN m N (modeFun m p)) ⬝ᵥ x)
            = Bgs.LineB.Gauss.chi N (a * Bgs.LineB.Gauss.Qform (Bgs.LineB.Gauss.H_N m N) x) *
              Bgs.LineB.Gauss.chi N ((Bgs.LineB.Gauss.nZN m N (modeFun m p)) ⬝ᵥ x) := by
          rw [Bgs.LineB.Gauss.chi_add]
        rw [hchi]
        ring
      rw [Finset.sum_congr rfl (fun x _ => e x), Finset.mul_sum]
    rw [esum]
    simp only [Bgs.LineB.Gauss.Gsum]
    ring
  rw [Finset.sum_congr rfl step5, Finset.mul_sum]

/-- `hExpand` for the wrapper, for the concrete kicked trace. -/
lemma hexpand (m N : ℕ) [NeZero m] [NeZero N] (ĝ : ℤ → ℂ) (supp : Finset ℤ)
    (a : ZMod N) :
    Matrix.trace ((kickMat N ĝ supp * catMat N a) ^ m)
      = (((Real.sqrt ((N : ℝ) ^ m) : ℂ)))⁻¹ *
        ∑ n ∈ modeSet m supp, phiFun m ĝ n *
          Bgs.LineB.Gauss.Gsum (Bgs.LineB.Gauss.H_N m N) a
            (Bgs.LineB.Gauss.nZN m N n) := by
  rw [trace_expand, sqrt_pow_inv]
  congr 1
  rw [show modeSet m supp
      = (Finset.univ.pi (fun _ : ZMod m => supp)).image (modeFun m) from rfl,
    Finset.sum_image (fun p _ p' _ h => modeFun_inj m p p' h)]
  apply Finset.sum_congr rfl
  intro p _
  rw [phiFun_modeFun]

/-- `hG0def` for the wrapper: the un-kicked trace is the normalised Gauss
sum at zero. -/
lemma hg0def (m N : ℕ) [NeZero m] [NeZero N] (a : ZMod N) :
    Matrix.trace (catMat N a ^ m)
      = (((Real.sqrt ((N : ℝ) ^ m) : ℂ)))⁻¹ *
        Bgs.LineB.Gauss.Gsum (Bgs.LineB.Gauss.H_N m N) a 0 := by
  rw [trace_pow_cycle]
  have step : (∑ x : ZMod m → ZMod N, ∏ j : ZMod m, catMat N a (x j) (x (j + 1)))
      = ∑ x : ZMod m → ZMod N, (((Real.sqrt (N : ℝ) : ℂ))⁻¹) ^ m *
          Bgs.LineB.Gauss.chi N (a * Bgs.LineB.Gauss.Qform (Bgs.LineB.Gauss.H_N m N) x) := by
    apply Finset.sum_congr rfl
    intro x _
    rw [catMat_prod]
  rw [step, sqrt_pow_inv]
  simp only [Bgs.LineB.Gauss.Gsum]
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro x _
  simp only [zero_dotProduct, add_zero]

/-- The finite-sum trace formula (Theorem 1(a) of 163) for
trigonometric-polynomial kicks: the wrapper applied to the concrete
expansion. -/
theorem trace_formula_kick (m N : ℕ) [NeZero m] [NeZero N] (ĝ : ℤ → ℂ)
    (supp : Finset ℤ) (a : ZMod N) (hm : 2 ≤ m)
    (hcop : Nat.Coprime (Bgs.LineB.Derand.Dm m).toNat N)
    (hN : 2 ≤ N) (ht0 : 2 * a * (-4) = 1) :
    ∃ b : ℕ, Matrix.trace ((kickMat N ĝ supp * catMat N a) ^ m)
      = Matrix.trace (catMat N a ^ m) *
        ∑ n ∈ modeSet m supp, phiFun m ĝ n *
          (Bgs.LineB.TraceFormula.e
            ((Bgs.LineB.TraceFormula.Qnum m n : ℚ) / (Bgs.LineB.Derand.Dm m : ℚ)
              / (N : ℚ) : ℝ) *
            Bgs.LineB.TraceFormula.e
              (-((b % Bgs.LineB.Derand.gp m : ℕ) : ℚ) * (Bgs.LineB.Derand.yp m : ℚ)
                * (Bgs.LineB.TraceFormula.NmZ m n : ℚ)
                / (Bgs.LineB.Derand.gp m : ℚ) : ℝ)) ∧
      ‖Matrix.trace (catMat N a ^ m)‖ = 1 := by
  have hcoef : a * (-4) ^ 2 - (-4) = 2 := by
    have h16 : 16 * a = -2 * (2 * a * (-4)) := by ring
    calc a * (-4) ^ 2 - (-4) = 16 * a + 4 := by ring
      _ = -2 * (2 * a * (-4)) + 4 := by rw [h16]
      _ = -2 * 1 + 4 := by rw [ht0]
      _ = 2 := by ring
  exact Bgs.LineB.Gauss.trace_formula_via_gauss m N hm hcop (phiFun m ĝ) (modeSet m supp)
    (Matrix.trace ((kickMat N ĝ supp * catMat N a) ^ m))
    (Matrix.trace (catMat N a ^ m)) hN a ht0 hcoef
    (hexpand m N ĝ supp a) (hg0def m N a)

/- Axiom audit for all main theorems of this module. -/
#print axioms Bgs.LineB.Expand.sqrt_pow_nat
#print axioms Bgs.LineB.Expand.sqrt_pow_inv
#print axioms Bgs.LineB.Expand.chi_sum
#print axioms Bgs.LineB.Expand.H_N_mulVec_apply
#print axioms Bgs.LineB.Expand.sum_add_one
#print axioms Bgs.LineB.Expand.quad_form_eq
#print axioms Bgs.LineB.Expand.pow_apply_path
#print axioms Bgs.LineB.Expand.trace_pow_cycle
#print axioms Bgs.LineB.Expand.kick_cat_apply
#print axioms Bgs.LineB.Expand.catMat_prod
#print axioms Bgs.LineB.Expand.kickVal_prod
#print axioms Bgs.LineB.Expand.trace_expand
#print axioms Bgs.LineB.Expand.hexpand
#print axioms Bgs.LineB.Expand.hg0def
#print axioms Bgs.LineB.Expand.trace_formula_kick

end Bgs.LineB.Expand
