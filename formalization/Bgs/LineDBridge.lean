/-
  Bgs/LineDBridge.lean — the 149 bridge: theta-average = mode sum = pair sum.

  What this module is
  -------------------
  The analytic-computation core of TRACE-149:

  * `tN` — the 149 parameter t_N = (D_m⁻¹ mod N)/N, with `tN_spec`
    (D_m · D_m⁻¹ = 1 in ZMod N, from gcd(D_m, N) = 1; primality of N
    is never used, exactly as in the boundary).
  * `PsiMode` — the finite mode sum
    `∑_{n,n'} c n n' · exp(2πi t · 2(Qn − Qn'))` (Q integral because
    X_m is integral as an adjugate — no fractions appear), with
    `psiMode_periodic` (1-periodicity, from integrality of Q) and
    `psiMode_even` (evenness, from symmetry of c).
  * `bridge` — the genuine computation: from the trace formula
    (hypothesis `hTrace`, the Boasman–Keating mechanism) and the
    averaged covariances (hypothesis `hAvg`), the theta-average of
    |T|² is the mode sum. The expansion of |T|², the conjugation of
    the phases, the termwise averaging and the reassembly are all
    proved, not postulated.
  * `bridge_pair` — the landing on the 151 pair sum: if the mode sum
    at t equals the pair sum (hypothesis `hPair`, the reindexing /
    theta-inversion identity), the bridge lands on `PsiPair`.

  What is deliberately NOT claimed (explicit hypotheses, not theorems)
  --------------------------------------------------------------------
  * `hTrace` — the formula Tr U^m = Tr M_N^m · ∑_n Ghat(n) e(t_N·2Qn)
    (Boasman–Keating 1995 §5 mechanism; not claimed as new, per 149).
  * `hAvg` — the averaged covariances E[a n · star (a n')] = c n n'
    (theta-averaging; "sites iid up to a global phase that cancels"
    is analytic input, not proved here).
  * `hTr1` — |Tr M_N^m| = 1.
  * `hPair` — the identification of the mode sum with the pair sum.
  * The linearity/conjugation properties of the averaging functional
    (`hEadd`, `hEsmul`, `hEconj`) — properties of the ensemble average,
    kept as hypotheses on the functional.
  * Smoothness (C^∞) of Psi_m and its independence from N as a
    function: the mode sum is manifestly N-independent as a finite
    sum (its only N-dependence is through the parameter t), but C^∞
    needs analytic infrastructure that is not in the graph.
  * Real-valuedness / positivity of the mode sum under Hermitian c:
    a reindexing argument of the same shape as `psiMode_even`, left
    as an explicit gap (in the ensemble picture reality is immediate
    since the averaged object is |T|²).
  * The 150 link `E = Psi(t*)` needs, in addition, the lattice
    collapse (`hcollapse` in LineDExpansion): periodicity (proved
    here) plus collapse gives Psi_m(t_N) = Psi_m(t*).
-/

import Bgs.LineDOrbitPair
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Exponential
import Mathlib.Analysis.Normed.Algebra.Exponential
import Mathlib.Data.ZMod.Basic

namespace Bgs
namespace LineD
namespace Bridge

open Finset
open Bgs.LineD.Defs

/-- t_N = (D_m⁻¹ mod N)/N as a real number (149). Primality of N is
    never used; only gcd(D_m, N) = 1. -/
noncomputable def tN (m N : ℕ) [NeZero m] [NeZero N]
    (h : Nat.Coprime (Dm m).toNat N) : ℝ :=
  ((((Dm m).toNat : ZMod N)⁻¹).val : ℝ) / N

/-- The defining property of the modular inverse: D_m · D_m⁻¹ = 1
    in ZMod N. Together with the definition of `tN`, this is the
    whole content of "t_N is the modular inverse over N". -/
theorem tN_spec (m N : ℕ) [NeZero m] (h : Nat.Coprime (Dm m).toNat N) :
    ((Dm m).toNat : ZMod N) * (((Dm m).toNat : ZMod N))⁻¹ = 1 :=
  ZMod.mul_inv_of_unit _ ((ZMod.isUnit_iff_coprime _ _).mpr h)

/-- Mode sum (149): ∑_{n,n'} c n n' · exp(2πi t · 2(Qn − Qn')).
    Q : ι → ℤ is the quadratic-form value (X_m is integral, so the
    form is integral — no fractions appear). The boundary's Psi_m is
    this sum with c the averaged covariances and Q n = nᵀ X_m n. -/
noncomputable def PsiMode {ι : Type*} [Fintype ι] (c : ι → ι → ℂ)
    (Q : ι → ℤ) (t : ℝ) : ℂ :=
  ∑ n, ∑ n', c n n' * Complex.exp (2 * Real.pi * Complex.I * t * (2 * ((Q n : ℝ) - Q n')))

/-- 1-periodicity of the mode sum (149: Psi_m is 1-periodic).
    Uses only integrality of Q: exp(2πi · 2(Qn − Qn')) = 1. -/
theorem psiMode_periodic {ι : Type*} [Fintype ι] (c : ι → ι → ℂ)
    (Q : ι → ℤ) (t : ℝ) :
    PsiMode c Q (t + 1) = PsiMode c Q t := by
  unfold PsiMode
  apply Finset.sum_congr rfl
  intro n _
  apply Finset.sum_congr rfl
  intro n' _
  congr 1
  rw [show 2 * Real.pi * Complex.I * ((t + 1 : ℝ) : ℂ) * (2 * ((Q n : ℝ) - Q n'))
      = 2 * Real.pi * Complex.I * t * (2 * ((Q n : ℝ) - Q n'))
        + (2 * (Q n - Q n') : ℤ) * (2 * Real.pi * Complex.I) by push_cast; ring]
  rw [Complex.exp_add, Complex.exp_int_mul_two_pi_mul_I, mul_one]

/-- Evenness of the mode sum (149: Psi_m is even), under symmetry of
    the covariances. The argument is reindexing (n, n') ↦ (n', n). -/
theorem psiMode_even {ι : Type*} [Fintype ι] (c : ι → ι → ℂ) (Q : ι → ℤ)
    (t : ℝ) (hc : ∀ n n', c n n' = c n' n) :
    PsiMode c Q (-t) = PsiMode c Q t := by
  unfold PsiMode
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro n' _
  apply Finset.sum_congr rfl
  intro n _
  rw [hc n n']
  congr 1
  congr 1
  rw [Complex.ofReal_neg]
  push_cast
  ring

/-- Conjugation of a purely imaginary exponential (Euler form).
    This is the exact step that turns star (exp (phase)) into
    exp (−phase) in the bridge computation. -/
theorem star_exp_phase (y : ℝ) :
    star (Complex.exp (y * Complex.I)) = Complex.exp ((-y) * Complex.I) := by
  rw [Complex.exp_mul_I, Complex.exp_mul_I, Complex.cos_neg, Complex.sin_neg,
    star_add, star_mul]
  have hc : star (Complex.cos (y : ℂ)) = Complex.cos (y : ℂ) := by
    rw [← Complex.ofReal_cos]
    exact Complex.conj_ofReal _
  have hs : star (Complex.sin (y : ℂ)) = Complex.sin (y : ℂ) := by
    rw [← Complex.ofReal_sin]
    exact Complex.conj_ofReal _
  have hI : star (Complex.I : ℂ) = -Complex.I := by simp
  rw [hc, hs, hI]
  ring

/-- Bridge (149): the theta-average of |T|² is the mode sum.

    Hypotheses (analytic inputs, not theorems):
    * `hTrace` — the trace formula (Boasman–Keating mechanism);
    * `hAvg` — the averaged covariances;
    * `hTr1` — |Tr M_N^m| = 1;
    * `hEadd`, `hEsmul`, `hEconj` — linearity/conjugation of the
      averaging functional.
    Everything else — expansion of |T|², conjugation of phases,
    termwise averaging, reassembly as `PsiMode` — is proved. -/
theorem bridge {ι : Type*} [Fintype ι] (a : ι → ℂ) (Q : ι → ℤ)
    (c : ι → ι → ℂ) (t : ℝ) (TrM : ℂ)
    (Eavg : ℂ → ℂ)
    (hEadd : ∀ x y, Eavg (x + y) = Eavg x + Eavg y)
    (hEsmul : ∀ (r : ℂ) (x : ℂ), Eavg (r * x) = r * Eavg x)
    (hEconj : ∀ x, Eavg (star x) = star (Eavg x))
    (hAvg : ∀ n n', Eavg (a n * star (a n')) = c n n')
    (hTr1 : TrM * star TrM = 1)
    (T : ℂ)
    (hTrace : T = TrM * ∑ n, a n * Complex.exp (2 * Real.pi * Complex.I * t * (2 * (Q n : ℝ)))) :
    Eavg (T * star T) = PsiMode c Q t := by
  classical
  have hE0 : Eavg 0 = 0 := by
    have h := hEadd 0 0
    rw [add_zero] at h
    have h2 := congrArg (· - Eavg 0) h
    simpa using h2.symm
  have hEsum : ∀ (s : Finset ι) (f : ι → ℂ),
      Eavg (∑ i ∈ s, f i) = ∑ i ∈ s, Eavg (f i) := by
    intro s f
    induction s using Finset.induction with
    | empty => simp [hE0]
    | insert a s ha ih =>
      rw [Finset.sum_insert ha, Finset.sum_insert ha, hEadd, ih]
  have hstarT : star T = star TrM * ∑ n,
      star (a n) * Complex.exp (-(2 * Real.pi * Complex.I * t * (2 * (Q n : ℝ)))) := by
    rw [hTrace, star_mul, mul_comm]
    congr 1
    rw [star_sum]
    apply Finset.sum_congr rfl
    intro n _
    rw [star_mul, mul_comm (star (Complex.exp (2 * Real.pi * Complex.I * t * (2 * (Q n : ℝ)))))
      (star (a n))]
    congr 1
    have hph : 2 * Real.pi * Complex.I * t * (2 * (Q n : ℝ))
        = ((2 * Real.pi * t * (2 * (Q n : ℝ)) : ℝ) : ℂ) * Complex.I := by
      push_cast
      ring
    rw [hph, star_exp_phase, neg_mul]
  have hexpand : T * star T
      = ∑ n, ∑ n', (a n * star (a n')) * (TrM * star TrM)
          * (Complex.exp (2 * Real.pi * Complex.I * t * (2 * (Q n : ℝ)))
             * Complex.exp (-(2 * Real.pi * Complex.I * t * (2 * (Q n' : ℝ))))) := by
    rw [hstarT, hTrace, mul_assoc, Finset.sum_mul, Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro n _
    rw [Finset.mul_sum, Finset.mul_sum, Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro n' _
    ring
  have hterm : ∀ n n',
      Eavg ((a n * star (a n')) * (TrM * star TrM)
          * (Complex.exp (2 * Real.pi * Complex.I * t * (2 * (Q n : ℝ)))
             * Complex.exp (-(2 * Real.pi * Complex.I * t * (2 * (Q n' : ℝ))))))
        = (TrM * star TrM) * c n n'
          * (Complex.exp (2 * Real.pi * Complex.I * t * (2 * (Q n : ℝ)))
             * Complex.exp (-(2 * Real.pi * Complex.I * t * (2 * (Q n' : ℝ))))) := by
    intro n n'
    have hrw : (a n * star (a n')) * (TrM * star TrM)
          * (Complex.exp (2 * Real.pi * Complex.I * t * (2 * (Q n : ℝ)))
             * Complex.exp (-(2 * Real.pi * Complex.I * t * (2 * (Q n' : ℝ)))))
        = ((TrM * star TrM)
          * (Complex.exp (2 * Real.pi * Complex.I * t * (2 * (Q n : ℝ)))
             * Complex.exp (-(2 * Real.pi * Complex.I * t * (2 * (Q n' : ℝ))))))
          * (a n * star (a n')) := by ring
    rw [hrw, hEsmul, hAvg]
    ring
  have havg : Eavg (T * star T)
      = ∑ n, ∑ n', (TrM * star TrM) * c n n'
          * (Complex.exp (2 * Real.pi * Complex.I * t * (2 * (Q n : ℝ)))
             * Complex.exp (-(2 * Real.pi * Complex.I * t * (2 * (Q n' : ℝ))))) := by
    rw [hexpand, hEsum]
    refine Finset.sum_congr rfl (fun n _ => ?_)
    rw [hEsum]
    refine Finset.sum_congr rfl (fun n' _ => ?_)
    exact hterm n n'
  calc Eavg (T * star T)
      = ∑ n, ∑ n', (TrM * star TrM) * c n n'
          * (Complex.exp (2 * Real.pi * Complex.I * t * (2 * (Q n : ℝ)))
             * Complex.exp (-(2 * Real.pi * Complex.I * t * (2 * (Q n' : ℝ))))) := havg
    _ = ∑ n, ∑ n', c n n'
          * Complex.exp (2 * Real.pi * Complex.I * t * (2 * ((Q n : ℝ) - Q n'))) := by
        apply Finset.sum_congr rfl
        intro n _
        apply Finset.sum_congr rfl
        intro n' _
        rw [hTr1, one_mul, ← Complex.exp_add]
        congr 1
        congr 1
        push_cast
        ring
    _ = PsiMode c Q t := rfl

/-- From the mode sum to the pair sum (151): if the mode sum at t
    equals the pair sum (hypothesis `hPair`, the reindexing /
    theta-inversion identity — analytic input), the bridge lands
    exactly on `PsiPair`. -/
theorem bridge_pair {ι : Type*} [Fintype ι] (a : ι → ℂ) (Q : ι → ℤ)
    (c : ι → ι → ℂ) (t : ℝ) (TrM : ℂ)
    (Eavg : ℂ → ℂ)
    (hEadd : ∀ x y, Eavg (x + y) = Eavg x + Eavg y)
    (hEsmul : ∀ (r : ℂ) (x : ℂ), Eavg (r * x) = r * Eavg x)
    (hEconj : ∀ x, Eavg (star x) = star (Eavg x))
    (hAvg : ∀ n n', Eavg (a n * star (a n')) = c n n')
    (hTr1 : TrM * star TrM = 1)
    (T : ℂ)
    (hTrace : T = TrM * ∑ n, a n * Complex.exp (2 * Real.pi * Complex.I * t * (2 * (Q n : ℝ))))
    (m : ℕ) [NeZero m] {K : Type*} [Fintype K]
    (φ : ℤ → Bgs.LineD.OrbitPair.Fix m → ℂ)
    (S : Bgs.LineD.OrbitPair.Fix m → K → ℝ) (ω : K → ℝ → ℂ) (η : ℝ)
    (s : ℤ)
    (hPair : PsiMode c Q t = Bgs.LineD.OrbitPair.PsiPair m φ S ω η s) :
    Eavg (T * star T) = Bgs.LineD.OrbitPair.PsiPair m φ S ω η s := by
  rw [bridge a Q c t TrM Eavg hEadd hEsmul hEconj hAvg hTr1 T hTrace, hPair]

#print axioms tN_spec
#print axioms psiMode_periodic
#print axioms psiMode_even
#print axioms star_exp_phase
#print axioms bridge
#print axioms bridge_pair

end Bridge
end LineD
end Bgs
