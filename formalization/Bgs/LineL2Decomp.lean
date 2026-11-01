import Bgs.LineLCollisionForm

/-!
# BGS-TRACE-255 — Line L2 decomposition of `D_𝔮` and `D_iso` at an open split prime level

Source: registry statement of `BGS-TRACE-255`.  Notation of `Bgs.LineLLineOrth`: `q` an odd prime, `qO = 𝔮 𝔮̄` split,
`𝔮 = ker φ_s`, `𝔮̄ = ker φ_{−s}` (`s² = 2`; here only `s ≠ 0` is used), `ℓ(𝔮) = ell s`, `ℓ(𝔮̄) = ell (−s)`,
`A : O/q → ℂ`, `Ẑ_β = ∑_x A(x) e(Tr(βx)/q)`, `A_tot = ∑_x A(x) = Ẑ_0`, `A(𝔞) = ∑_{x ∈ 𝔞/qO} A(x)`.

* `A_ideal_line` : `A(𝔮) = q⁻¹ ∑_{β∈ℓ(𝔮)} Ẑ_β` (orthogonality, `[O:𝔮] = q`);
* `A_qO` : `A(qO) = q⁻² ∑_{β ∈ O/q} Ẑ_β` (`[O:qO] = q²`);
* `Dq_eq` : `D_𝔮 := A(𝔮) − A_tot/q = q⁻¹ ∑_{β∈ℓ(𝔮)∖0} Ẑ_β`;
* `A_qO_sub` : `A(qO) − A_tot/q² = q⁻² ∑_{β≠0} Ẑ_β`;
* `inter_eq` : `𝔮 ∩ 𝔮̄ = qO`;
* `Diso_eq` : with `D_iso := A(𝔮 ∪ 𝔮̄) − ((2q − 1)/q²) A_tot`,
  `D_iso = D_𝔮 + D_𝔮̄ − (A(qO) − A_tot/q²)`; `Diso_fourier` : the same as Fourier averages.

**Partial coverage:** the use with Theorem K1 (BGS-TRACE-237), i.e. the level contribution
`2 Re(conj Z_ρ (D_iso − E_b/q))`, is **not** formalized.  All proofs are kernel-checked.
-/

namespace Bgs.LineL2Decomp

open Finset ComplexConjugate Bgs.LineLLineOrth

variable {q : ℕ} [hq : Fact q.Prime] (A : ZMod q × ZMod q → ℂ)

/-- `A(𝔞)` for an ideal given by a predicate on `O/q`. -/
noncomputable def Aid (P : ZMod q × ZMod q → Prop) [DecidablePred P] : ℂ := ∑ x ∈ univ.filter P, A x

noncomputable def Atot : ℂ := ∑ x, A x

noncomputable def Dq (s : ZMod q) : ℂ := Aid A (fun x => φ s x = 0) - Atot A / q

noncomputable def Diso (s : ZMod q) : ℂ :=
  Aid A (fun x => φ s x = 0 ∨ φ (-s) x = 0) - ((2 * q - 1) / (q : ℂ) ^ 2) * Atot A

theorem Zhat_zero : Zhat A 0 = Atot A := by
  unfold Zhat Atot trmul; simp

theorem A_ideal_line (hq2 : q ≠ 2) (s : ZMod q) :
    Aid A (fun x => φ s x = 0) = (1 / (q : ℂ)) * ∑ β ∈ ell s, Zhat A β := by
  unfold Zhat Aid
  rw [sum_comm, mul_sum, sum_filter]
  refine sum_congr rfl (fun x _ => ?_)
  rw [← mul_sum, mul_comm, mul_assoc]
  simp_rw [trmul_comm _ x]
  rw [mul_comm _ (1 / (q : ℂ)), line_orth hq2 s]
  split_ifs <;> simp

theorem A_qO (hq2 : q ≠ 2) : A 0 = (1 / (q : ℂ) ^ 2) * ∑ β, Zhat A β := by
  have h2 : IsUnit (2 : ZMod q) := (two_ne_zero' (q := q) hq2).isUnit
  have hq0 : (q : ℂ) ≠ 0 := by exact_mod_cast hq.out.ne_zero
  unfold Zhat
  rw [sum_comm]
  have : ∀ x : ZMod q × ZMod q, ∑ β, A x * (ψ : AddChar (ZMod q) ℂ) (trmul β x)
      = A x * (if x = 0 then (q : ℂ) ^ 2 else 0) := by
    intro x
    rw [← mul_sum]
    congr 1
    exact Bgs.LineLCollisionForm.orth (h := q) h2 x
  simp_rw [this, mul_ite, mul_zero, sum_ite_eq', mem_univ, if_true]
  field_simp

theorem Dq_eq (hq2 : q ≠ 2) (s : ZMod q) :
    Dq A s = (1 / (q : ℂ)) * ∑ β ∈ (ell s).erase 0, Zhat A β := by
  unfold Dq
  rw [A_ideal_line A hq2 s, ← add_sum_erase _ _ (zero_mem_ell hq2 s), Zhat_zero]
  ring

theorem A_qO_sub (hq2 : q ≠ 2) :
    A 0 - Atot A / (q : ℂ) ^ 2 = (1 / (q : ℂ) ^ 2) * ∑ β ∈ univ.erase 0, Zhat A β := by
  rw [A_qO A hq2, ← add_sum_erase _ _ (mem_univ 0), Zhat_zero]
  ring

theorem inter_eq (hq2 : q ≠ 2) (s : ZMod q) (hs : s ≠ 0) (x : ZMod q × ZMod q) :
    (φ s x = 0 ∧ φ (-s) x = 0) ↔ x = 0 := by
  have h2 := two_ne_zero' (q := q) hq2
  unfold φ
  constructor
  · rintro ⟨h1, h3⟩
    have hx2 : x.2 = 0 := by
      have : 2 * s * x.2 = 0 := by linear_combination h1 - h3
      rcases mul_eq_zero.mp this with h | h
      · exact absurd h (mul_ne_zero h2 hs)
      · exact h
    have hx1 : x.1 = 0 := by rw [hx2, mul_zero, add_zero] at h1; exact h1
    exact Prod.ext hx1 hx2
  · rintro rfl; simp

theorem Diso_eq (hq2 : q ≠ 2) (s : ZMod q) (hs : s ≠ 0) :
    Diso A s = Dq A s + Dq A (-s) - (A 0 - Atot A / (q : ℂ) ^ 2) := by
  have hq0 : (q : ℂ) ≠ 0 := by exact_mod_cast hq.out.ne_zero
  have hU := sum_union_inter (s₁ := univ.filter (fun x : ZMod q × ZMod q => φ s x = 0))
    (s₂ := univ.filter (fun x : ZMod q × ZMod q => φ (-s) x = 0)) (f := A)
  rw [← filter_or, ← filter_and] at hU
  have hI : univ.filter (fun x : ZMod q × ZMod q => φ s x = 0 ∧ φ (-s) x = 0) = {0} := by
    ext x; simp only [mem_filter, mem_univ, true_and, mem_singleton]; exact inter_eq hq2 s hs x
  rw [hI, sum_singleton] at hU
  unfold Diso Dq Aid
  have : ∑ x ∈ univ.filter (fun x => φ s x = 0 ∨ φ (-s) x = 0), A x
      = ∑ x ∈ univ.filter (fun x => φ s x = 0), A x + ∑ x ∈ univ.filter (fun x => φ (-s) x = 0), A x - A 0 := by
    rw [← hU]; ring
  rw [this]
  field_simp
  ring

theorem Diso_fourier (hq2 : q ≠ 2) (s : ZMod q) (hs : s ≠ 0) :
    Diso A s = (1 / (q : ℂ)) * ∑ β ∈ (ell s).erase 0, Zhat A β + (1 / (q : ℂ)) * ∑ β ∈ (ell (-s)).erase 0, Zhat A β
      - (1 / (q : ℂ) ^ 2) * ∑ β ∈ univ.erase 0, Zhat A β := by
  rw [Diso_eq A hq2 s hs, Dq_eq A hq2, Dq_eq A hq2, A_qO_sub A hq2]

end Bgs.LineL2Decomp
