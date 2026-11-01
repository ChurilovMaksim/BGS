/-
# BGS-TRACE-149, properties of the mode sum that close from the tree

What is proved here, and what is NOT:

* Hermitian covariances from the bridge's own hypotheses
  (`psimode_hermitian_of_avg`): from `hAvg` and `hEconj` alone,
  `c n n' = star (c n' n)`. No ensemble is constructed here; this is
  the algebraic consequence of the two hypotheses.
* Reality of the mode sum (`psimode_star`, `psimode_im_eq_zero`):
  under Hermitian `c`, `star (PsiMode c Q t) = PsiMode c Q t`, hence
  its imaginary part is zero. This closes the "real-valuedness"
  gap named in the `LineDBridge` header. Positivity is NOT proved:
  it needs `c` positive-semidefinite, i.e. the ensemble picture
  (`Psi_m = E|T|² ≥ 0`), not mode-sum algebra.
* Smoothness (`psimode_contDiff`): `t ↦ PsiMode c Q t` is `C^∞`,
  with no hypotheses on `c` at all (a finite sum of exponentials).
  This is the boundary's "Psi_m C^infinity" for the model function.
  N-independence is definitional for `PsiMode` (it has no `N`
  parameter); the substantive N-independence of the boundary's
  `Psi_m` follows only after the `Psi_m = PsiMode` identification,
  which is NOT proved here.
* `t_N → t*` (`tN_sub_tStar`, `tendsto_one_div_mul_atTop`):
  `t_N - t* = 1/(N·D_m)` by the definition of `t*` in the phase
  module, and `1/(N·D_m) → 0`. Together these say `t_N` converges
  to `t*` along admissible `N` (the two lemmas are stated
  separately because the coprimality hypothesis depends on `N`,
  so there is no single `Tendsto` statement over all of `ℕ`).

What is deliberately NOT claimed (see the gap map in the report):

* `hTrace` (Boasman–Keating per `θ`), `hAvg` (the covariance
  computation), `hEadd`/`hEsmul`/`hEconj` for the TRUE `θ`-average,
  `hPair` (mode sum = pair sum), symmetric `c` for evenness
  (`V → -V` symmetry), and the `Psi_m = PsiMode` identification.
  All of these need the analytic layer (the `θ`-ensemble, the
  kick identification, the theta-inversion step) that is not in
  the tree. A finite toy average would satisfy `hEadd`/`hEsmul`/
  `hEconj` trivially, but it would NOT discharge them for the
  true ensemble, so no such toy is claimed here.

No sorry, no admit, no axiom, no native_decide, no decide.
-/

import Bgs.LineDPhaseLemma
import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.Calculus.ContDiff.Operations
import Mathlib.Analysis.SpecificLimits.Basic

namespace Bgs
namespace LineD
namespace Props149

open Bgs.LineD
open Finset Filter Topology

/-! ### Hermitian covariances from `hAvg` + `hEconj` -/

/-- From the averaged covariances and conjugation-linearity of the
    average, the covariances are Hermitian. This is pure algebra
    on the bridge's hypotheses, not a new analytic input. -/
theorem psimode_hermitian_of_avg {ι : Type*} [Fintype ι] (a : ι → ℂ)
    (c : ι → ι → ℂ) (Eavg : ℂ → ℂ)
    (hEconj : ∀ x, Eavg (star x) = star (Eavg x))
    (hAvg : ∀ n n', Eavg (a n * star (a n')) = c n n') :
    ∀ n n', c n n' = star (c n' n) := by
  intro n n'
  have h1 : c n n' = Eavg (a n * star (a n')) := (hAvg n n').symm
  have h2 : star (c n' n) = Eavg (a n * star (a n')) := by
    rw [← hAvg n' n, ← hEconj]
    congr 1
    rw [star_mul, star_star, mul_comm]
  rw [h1, h2]

/-! ### Reality of the mode sum -/

/-- The mode sum is real under Hermitian covariances: conjugation
    swaps the summation indices and negates the phases. -/
theorem psimode_star {ι : Type*} [Fintype ι] (c : ι → ι → ℂ) (Q : ι → ℤ)
    (t : ℝ) (hc : ∀ n n', c n n' = star (c n' n)) :
    star (Bridge.PsiMode c Q t) = Bridge.PsiMode c Q t := by
  have hterm : ∀ n n' : ι,
      star (c n n' * Complex.exp (2 * Real.pi * Complex.I * (t : ℂ)
          * (2 * (((Q n : ℝ) : ℂ) - (Q n' : ℂ)))))
        = star (c n n') * Complex.exp (2 * Real.pi * Complex.I * (t : ℂ)
          * (2 * (((Q n' : ℝ) : ℂ) - (Q n : ℂ)))) := by
    intro n n'
    have hph : (2 * Real.pi * Complex.I * (t : ℂ)
          * (2 * (((Q n : ℝ) : ℂ) - (Q n' : ℂ))))
        = (((2 * Real.pi * t * (2 * ((Q n : ℝ) - Q n')) : ℝ)) : ℂ)
          * Complex.I := by
      push_cast
      ring
    -- `star` is an anti-homomorphism: `star (a * b) = star b * star a`,
    -- so after `star_mul` the conjugated coefficient sits on the right.
    have hph2 : (((-(2 * Real.pi * t * (2 * ((Q n : ℝ) - Q n')) : ℝ)) : ℂ)
          * Complex.I
        = 2 * Real.pi * Complex.I * (t : ℂ)
          * (2 * (((Q n' : ℝ) : ℂ) - (Q n : ℂ)))) := by
      push_cast
      ring
    rw [star_mul, hph, Bridge.star_exp_phase, mul_comm, hph2]
  unfold Bridge.PsiMode
  simp only [star_sum]
  have hswap : (∑ n, ∑ n', star (c n n' * Complex.exp (2 * Real.pi
          * Complex.I * (t : ℂ) * (2 * (((Q n : ℝ) : ℂ) - (Q n' : ℂ))))))
      = ∑ n, ∑ n', star (c n n') * Complex.exp (2 * Real.pi
          * Complex.I * (t : ℂ) * (2 * (((Q n' : ℝ) : ℂ) - (Q n : ℂ)))) :=
    Finset.sum_congr rfl (fun n _ =>
      Finset.sum_congr rfl (fun n' _ => hterm n n'))
  rw [hswap]
  rw [Finset.sum_comm (s := Finset.univ) (t := Finset.univ)
    (f := fun n n' => star (c n n') * Complex.exp (2 * Real.pi
      * Complex.I * (t : ℂ) * (2 * (((Q n' : ℝ) : ℂ) - (Q n : ℂ)))))]
  apply Finset.sum_congr rfl
  intro a _
  apply Finset.sum_congr rfl
  intro b _
  congr 1
  exact (hc a b).symm

/-- The imaginary part of the mode sum vanishes under Hermitian
    covariances. -/
theorem psimode_im_eq_zero {ι : Type*} [Fintype ι] (c : ι → ι → ℂ)
    (Q : ι → ℤ) (t : ℝ) (hc : ∀ n n', c n n' = star (c n' n)) :
    (Bridge.PsiMode c Q t).im = 0 := by
  have h := psimode_star c Q t hc
  have h2 := congrArg Complex.im h
  rw [Complex.star_def, Complex.conj_im] at h2
  linarith

/-! ### Smoothness in `t` -/

/-- The mode sum is `C^∞` in `t`, with no hypotheses on `c`: a finite
    sum of exponentials of linear functions. -/
theorem psimode_contDiff {ι : Type*} [Fintype ι] (c : ι → ι → ℂ)
    (Q : ι → ℤ) :
    ContDiff ℝ ⊤ (fun t => Bridge.PsiMode c Q t) := by
  have hexp : ContDiff ℝ ⊤ Complex.exp :=
    (Complex.contDiff_exp (𝕜 := ℂ)).restrict_scalars ℝ
  have hphase : ∀ n n' : ι, ContDiff ℝ ⊤ (fun t : ℝ =>
      Complex.exp (2 * Real.pi * Complex.I * (t : ℂ)
        * (2 * (((Q n : ℝ) : ℂ) - (Q n' : ℂ))))) := by
    intro n n'
    apply hexp.comp
    have hg : ContDiff ℝ ⊤ (fun t : ℝ =>
        (2 * Real.pi * Complex.I * (2 * (((Q n : ℝ) : ℂ) - (Q n' : ℂ))))
          * (t : ℂ)) := by
      have hof : ContDiff ℝ ⊤ (Complex.ofRealCLM : ℝ → ℂ) :=
        Complex.ofRealCLM.contDiff
      simpa only [Complex.ofRealCLM_apply, smul_eq_mul] using
        hof.const_smul (2 * Real.pi * Complex.I
          * (2 * (((Q n : ℝ) : ℂ) - (Q n' : ℂ))))
    convert hg using 1
    ext t
    push_cast
    ring
  unfold Bridge.PsiMode
  apply ContDiff.sum
  intro n _
  apply ContDiff.sum
  intro n' _
  simpa only [smul_eq_mul] using ContDiff.const_smul (c n n') (hphase n n')

/-! ### `t_N → t*` -/

/-- `t_N - t* = 1/(N·D_m)`, by the definition of `t*`. -/
theorem tN_sub_tStar (m N : ℕ) [NeZero m] [NeZero N]
    (h : Nat.Coprime (LineD.Defs.Dm m).toNat N) :
    Bridge.tN m N h - PhaseLemma.tStar m N h
      = 1 / ((N : ℝ) * ((LineD.Defs.Dm m).toNat : ℝ)) := by
  unfold PhaseLemma.tStar
  rw [sub_sub_self]

/-- `1/(N·D) → 0` for `D ≠ 0`. Together with `tN_sub_tStar` this
    is the `t_N → t*` convergence (D2) along admissible `N`. -/
theorem tendsto_one_div_mul_atTop {D : ℝ} (hD : D ≠ 0) :
    Tendsto (fun N : ℕ => 1 / ((N : ℝ) * D)) atTop (𝓝 0) := by
  have h : (fun N : ℕ => 1 / ((N : ℝ) * D))
      = (fun N : ℕ => (1 / D) * (1 / (N : ℝ))) := by
    funext N
    rw [mul_comm ((N : ℝ)) D, div_mul_div_comm, one_mul]
  rw [h]
  simpa using Tendsto.const_mul (1 / D) tendsto_one_div_atTop_nhds_zero_nat

/- Axiom audit for all main theorems of this module. -/
#print axioms Bgs.LineD.Props149.psimode_hermitian_of_avg
#print axioms Bgs.LineD.Props149.psimode_star
#print axioms Bgs.LineD.Props149.psimode_im_eq_zero
#print axioms Bgs.LineD.Props149.psimode_contDiff
#print axioms Bgs.LineD.Props149.tN_sub_tStar
#print axioms Bgs.LineD.Props149.tendsto_one_div_mul_atTop

end Props149
end LineD
end Bgs
