/-
  Bgs/LineBNAverage.lean — N-average for TRACE-175 (Thm U).

  TEST COPY ONLY — not pushed to the repository, registry untouched,
  `Bgs.lean` aggregator unchanged (this module is built by a direct
  `lake env lean` call, not imported by the aggregator).

  Boundaries, verbatim from `record/claims.json` (base 347f):

  BGS-TRACE-175 (proved; source
  mathematics/fixed-map/derandomized_fixed_kick.md; dependency
  BGS-TRACE-163):

  > Averaging over N in (X, 2X], gcd(N, D_m) = 1:
  > <|Tr U_N^m|^2>_N = F_m(eta) + O(m s2 s0^{2m-1}/X +
  > D_m min(s0^{2m}, D_eff)/X), s0 = sum|ghat|, s2 = sum n^2|ghat|;
  > uniform for m <= (1-eps) c(eta) log X,
  > c(eta) = 1/(log lambda + 2 log s0(eta)). Fixed eta;
  > logarithmic window only (below Ehrenfest).

  BGS-TRACE-163 (proved; the trace formula used here, Theorem 1):

  > U = K_eta M_N with K_eta = diag e^{i eta f(q/N)}, f the fixed
  > real 32-mode trigonometric position kick, S=[[3,4],[2,3]], odd N
  > with gcd(N,D_m)=1, fixed m. Theorem 1: Tr(K_eta M)^m = Tr M^m *
  > sum_n Phihat(n) e(Q(n)/N) e(-nu_N y'_m Nm(alpha_n)/g'_m),
  > nu_N = N^{-1} mod g'_m, alpha_n in Z[lambda], lambda=3+2sqrt2;
  > hence Tr U^m / Tr M^m = Z_m(nu_N; eta) + O(1/N). [...] Pointwise
  > self-averaging in one N is false (|Tr U_N^m|^2 is asymptotically
  > a non-constant function of N^{-1} mod g'_m). Fixed m only;
  > diagonal (l=0) kick only; nothing at tau = m/N = O(1).

  What is built here, and what is honestly left as hypotheses:

  * `window`, `winAvg`, `nuAvg`, `Zfun`, `Bprof` — the language of
    175: the window (X, 2X] with the gcd condition, the window
    average, the uniform nu-average, the nu-profile Z_m(nu; eta)
    (the nu-part of the 163 sum, with e(t) := exp (2*pi*i*t)),
    and the squared profile B(nu) = |Tr M^m|^2 * |Z(nu)|^2.
    eta is FIXED throughout and suppressed: every quantity here is
    at that fixed eta (so s0 = s0(eta), F = F_m(eta)).
  * `traceHence` — DERIVED (no analysis): from the exact 163 sum
    (`hSum`) and an explicit O(1/N) phase-difference bound
    (`hPhase`), the "hence" form Tr U_N^m = Tr M^m * (Z(nu_N) + R_N)
    with |R_N| <= C / N. The phase bound is a hypothesis: it is
    the explicit-constant form of 163's O(1/N) remainder, whose
    constant is fixed by `hC` so that the squared passage below
    lands exactly on 175's first error term. Supplying that
    constant is analytic content, not proved here.
  * `pointwise_bound` — DERIVED (algebra + norms): from the hence
    form, the l1-bound |Z| <= s0^m (`hZ`), and C <= X (so that
    |R_N| <= 1 on the window and |R_N|^2 <= |R_N|), the squared
    pointwise bound | |Tr U_N^m|^2 - B(nu_N) | <= m s2 s0^{2m-1} / N.
  * `nAverage` — DERIVED (averaging lemmas + triangle inequality):
    the window average of |Tr U_N^m|^2 differs from the nu-average
    F_m(eta) by at most m s2 s0^{2m-1}/X + D_m min(s0^{2m}, D_eff)/X,
    under the equidistribution hypothesis `hEquidist` (the
    window-average of B(nu_N) against the uniform nu-average; the
    residue-equidistribution lemma is the remaining analytic heart
    and is NOT proved here) and the interpretation hypothesis
    `hNu` (nu_N is the inverse of N mod g'_m).
  * `window_pow_le` — DERIVED: the logarithmic window
    m <= (1-eps) c(eta) log X implies s0^{2m} <= X^{1-eps}
    (so both error terms decay like X^{-eps} up to the stated
    prefactors; see `window_error_decay`).
  * NOT claimed: the trace formula 163 itself as a theorem (it is
    hypothesis `hSum`); the phase bound, the l1-bound, and the
    equidistribution bound as theorems; pointwise self-averaging
    at a single N (false by 163, and not stated); anything about
    BGS-TRACE-005 or BGS-BGS-001; anything above the logarithmic
    window (the window hypothesis is used only as stated).
-/

import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Finset.Card
import Mathlib.Data.Finset.Interval
import Mathlib.Order.Interval.Finset.Nat
import Mathlib.Algebra.Order.Floor.Defs
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Order.GroupWithZero.Basic
import Mathlib.Algebra.Order.Group.Abs
import Mathlib.Analysis.Complex.Exponential
import Mathlib.Analysis.Complex.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.Real.Sqrt
import Mathlib.Data.ZMod.Basic

namespace Bgs.LineB.NAverage

open Finset

/-- The Pell unit lambda = 3 + 2*sqrt 2 from the 163 boundary. -/
noncomputable def lam : ℝ := 3 + 2 * Real.sqrt 2

/-- c(eta) = 1 / (log lambda + 2 log s0(eta)), at fixed eta. -/
noncomputable def cEta (s0 : ℝ) : ℝ := 1 / (Real.log lam + 2 * Real.log s0)

/-- The averaging window: N in (X, 2X] with gcd(N, D_m) = 1.
    As a Finset of naturals this is (floor X, floor (2X)] filtered
    by coprimality; `mem_window` proves it is exactly the window. -/
noncomputable def window (X : ℝ) (D : ℕ) : Finset ℕ :=
  (Finset.Ioc ⌊X⌋₊ ⌊2 * X⌋₊).filter (fun N => Nat.Coprime N D)

/-- Average of `f` over a finite window. -/
noncomputable def winAvg (W : Finset ℕ) (f : ℕ → ℝ) : ℝ :=
  (∑ N ∈ W, f N) / W.card

/-- The phase factor e(-nu * y' * Nm(alpha_n) / g'_m) for one mode,
    with e(t) := exp (2*pi*i*t). `nu.val` is the representative of
    the residue in {0, ..., g'-1}. -/
noncomputable def phase {g' : ℕ} [NeZero g'] (Nm : ℤ → ℤ) (yp : ℤ) (ν : ZMod g') (n : ℤ) : ℂ :=
  Complex.exp (2 * Real.pi * Complex.I *
    (((-(ν.val : ℂ)) * (yp : ℂ) * (Nm n : ℂ)) / (g' : ℂ)))

/-- The nu-profile Z_m(nu; eta): the nu-part of the 163 sum,
    Z(nu) = sum_n Phihat(n) e(-nu y' Nm(alpha_n)/g'_m). -/
noncomputable def Zfun {g' : ℕ} [NeZero g'] (S : Finset ℤ) (Phi : ℤ → ℂ)
    (Nm : ℤ → ℤ) (yp : ℤ) (ν : ZMod g') : ℂ :=
  ∑ n ∈ S, Phi n * phase Nm yp ν n

/-- The squared profile B(nu) = |Tr M^m|^2 * |Z(nu)|^2. -/
noncomputable def Bprof (TrM : ℂ) {g' : ℕ} (Z : ZMod g' → ℂ) (ν : ZMod g') : ℝ :=
  ‖TrM‖ ^ 2 * ‖Z ν‖ ^ 2

/-- The uniform nu-average F_m(eta): average of B over all residues
    mod g'_m. -/
noncomputable def nuAvg {g' : ℕ} [NeZero g'] (B : ZMod g' → ℝ) : ℝ :=
  (∑ ν : ZMod g', B ν) / g'

/-- Membership in the window, in analytic form. -/
theorem mem_window {X : ℝ} {D : ℕ} (hX : 0 ≤ X) {N : ℕ}
    (hN : N ∈ window X D) : X < N ∧ (N : ℝ) ≤ 2 * X ∧ Nat.Coprime N D := by
  rw [window, Finset.mem_filter, Finset.mem_Ioc] at hN
  obtain ⟨⟨h1, h2⟩, h3⟩ := hN
  have hN1 : X < (N : ℝ) := by
    have h := Nat.lt_floor_add_one X
    have hle : (⌊X⌋₊ : ℝ) + 1 ≤ (N : ℝ) := by exact_mod_cast h1
    linarith [h, hle]
  have hN2 : (N : ℝ) ≤ 2 * X := by
    have h := Nat.floor_le (show 0 ≤ 2 * X by linarith)
    have hle : (N : ℝ) ≤ (⌊2 * X⌋₊ : ℝ) := by exact_mod_cast h2
    linarith [h, hle]
  exact ⟨hN1, hN2, h3⟩

/-- Averaging lemma: the average of a difference is bounded by the
    average of the absolute differences. -/
theorem avg_sub_abs_le (W : Finset ℕ) (f g : ℕ → ℝ) (hW : W.Nonempty) :
    |winAvg W f - winAvg W g| ≤ winAvg W (fun N => |f N - g N|) := by
  have hcard : (0 : ℝ) < W.card := by
    exact_mod_cast Finset.card_pos.mpr hW
  unfold winAvg
  rw [div_sub_div_same, ← Finset.sum_sub_distrib]
  rw [abs_div]
  have hcard' : |(W.card : ℝ)| = W.card := abs_of_nonneg (Nat.cast_nonneg _)
  rw [hcard', div_le_div_iff_of_pos_right hcard]
  exact Finset.abs_sum_le_sum_abs _ _

/-- Averaging lemma: averages are monotone in the integrand. -/
theorem avg_mono (W : Finset ℕ) (f g : ℕ → ℝ) (hW : W.Nonempty)
    (h : ∀ N ∈ W, f N ≤ g N) : winAvg W f ≤ winAvg W g := by
  have hcard : (0 : ℝ) < W.card := by
    exact_mod_cast Finset.card_pos.mpr hW
  unfold winAvg
  rw [div_le_div_iff_of_pos_right hcard]
  exact Finset.sum_le_sum h

/-- Averaging lemma: a pointwise bound passes to the average. -/
theorem avg_le_of_forall_le (W : Finset ℕ) (f : ℕ → ℝ) (e : ℝ)
    (hW : W.Nonempty) (h : ∀ N ∈ W, f N ≤ e) : winAvg W f ≤ e := by
  have hcard : (0 : ℝ) < W.card := by
    exact_mod_cast Finset.card_pos.mpr hW
  unfold winAvg
  rw [div_le_iff₀ hcard]
  calc ∑ N ∈ W, f N ≤ W.card • e := Finset.sum_le_card_nsmul _ _ _ h
    _ = e * W.card := by rw [nsmul_eq_mul, mul_comm]

/-- From the exact 163 sum and the phase-difference bound, the
    "hence" form Tr U_N^m = Tr M^m * (Z(nu_N) + R_N). -/
theorem traceHence {g' : ℕ} [NeZero g'] {S : Finset ℤ} {Phi : ℤ → ℂ}
    {Q Nm : ℤ → ℤ} {yp : ℤ} {TrU : ℕ → ℂ} {TrM : ℂ}
    {nu : ℕ → ZMod g'} {W : Finset ℕ} {C : ℝ}
    (hSum : ∀ N ∈ W, TrU N = TrM * ∑ n ∈ S,
      Phi n * Complex.exp (2 * Real.pi * Complex.I * ((Q n : ℂ) / (N : ℂ))) *
        phase Nm yp (nu N) n)
    (hPhase : ∀ N ∈ W, ‖∑ n ∈ S, Phi n *
      (Complex.exp (2 * Real.pi * Complex.I * ((Q n : ℂ) / (N : ℂ))) - 1) *
        phase Nm yp (nu N) n‖ ≤ C / (N : ℝ)) :
    ∀ N ∈ W, TrU N = TrM * (Zfun S Phi Nm yp (nu N) +
      ∑ n ∈ S, Phi n *
        (Complex.exp (2 * Real.pi * Complex.I * ((Q n : ℂ) / (N : ℂ))) - 1) *
          phase Nm yp (nu N) n) ∧
      ‖∑ n ∈ S, Phi n *
        (Complex.exp (2 * Real.pi * Complex.I * ((Q n : ℂ) / (N : ℂ))) - 1) *
          phase Nm yp (nu N) n‖ ≤ C / (N : ℝ) := by
  intro N hN
  have hsplit : (∑ n ∈ S, Phi n *
      Complex.exp (2 * Real.pi * Complex.I * ((Q n : ℂ) / (N : ℂ))) *
        phase Nm yp (nu N) n)
      = Zfun S Phi Nm yp (nu N) + ∑ n ∈ S, Phi n *
        (Complex.exp (2 * Real.pi * Complex.I * ((Q n : ℂ) / (N : ℂ))) - 1) *
          phase Nm yp (nu N) n := by
    rw [Zfun, ← Finset.sum_add_distrib]
    apply Finset.sum_congr rfl
    intro n _
    ring
  rw [hSum N hN, hsplit]
  exact ⟨rfl, hPhase N hN⟩

/-- Squared pointwise bound from the hence form. The constant
    relation `hC` fixes C so that the bound lands exactly on 175's
    first error term; `hXbig` (C <= X) gives |R_N| <= 1 on the
    window, hence |R_N|^2 <= |R_N|. -/
theorem pointwise_bound {g' : ℕ} [NeZero g'] {S : Finset ℤ} {Phi : ℤ → ℂ}
    {Nm : ℤ → ℤ} {yp : ℤ} {TrU : ℕ → ℂ} {TrM : ℂ}
    {nu : ℕ → ZMod g'} {R : ℕ → ℂ} {W : Finset ℕ}
    {m : ℕ} {X s0 s2 C : ℝ}
    (hX : 0 < X) (_hm : 0 < m) (hs0 : 0 ≤ s0) (hs2 : 0 ≤ s2)
    (hC0 : 0 ≤ C)
    (hC : ‖TrM‖ ^ 2 * (2 * s0 ^ m + 1) * C = m * s2 * s0 ^ (2 * m - 1))
    (hXbig : C ≤ X)
    (hZ : ∀ ν : ZMod g', ‖Zfun S Phi Nm yp ν‖ ≤ s0 ^ m)
    (hTrace : ∀ N ∈ W, TrU N = TrM * (Zfun S Phi Nm yp (nu N) + R N) ∧
      ‖R N‖ ≤ C / (N : ℝ))
    (hW : ∀ N ∈ W, X < N) :
    ∀ N ∈ W, |‖TrU N‖ ^ 2 - Bprof TrM (Zfun S Phi Nm yp) (nu N)| ≤
      (m * s2 * s0 ^ (2 * m - 1)) / (N : ℝ) := by
  intro N hN
  obtain ⟨hTr, hR⟩ := hTrace N hN
  have hNpos : (0 : ℝ) < N := lt_trans hX (hW N hN)
  have hNne : (N : ℝ) ≠ 0 := ne_of_gt hNpos
  set z := ‖Zfun S Phi Nm yp (nu N)‖ with hz_def
  set r := ‖R N‖ with hr_def
  set w := ‖Zfun S Phi Nm yp (nu N) + R N‖ with hw_def
  have hz0 : 0 ≤ z := norm_nonneg _
  have hr0 : 0 ≤ r := norm_nonneg _
  have hw0 : 0 ≤ w := norm_nonneg _
  have hzle : z ≤ s0 ^ m := hZ _
  have hs0m : 0 ≤ s0 ^ m := pow_nonneg hs0 _
  have hRle : r ≤ C / (N : ℝ) := hR
  have hCN : C / (N : ℝ) ≤ 1 := by
    rw [div_le_one hNpos]
    exact le_trans hXbig (le_of_lt (hW N hN))
  have hr1 : r ≤ 1 := le_trans hRle hCN
  have hCN0 : 0 ≤ C / (N : ℝ) := div_nonneg hC0 (le_of_lt hNpos)
  -- |w^2 - z^2| <= 2*z*r + r^2
  have hw_le : w ≤ z + r := norm_add_le _ _
  have hw_ge : z - r ≤ w := by
    have h := norm_sub_norm_le (Zfun S Phi Nm yp (nu N)) (-(R N))
    rw [sub_neg_eq_add, norm_neg] at h
    exact h
  have habs : |w ^ 2 - z ^ 2| ≤ 2 * z * r + r ^ 2 := by
    rw [sq_sub_sq, abs_mul]
    have hwz : |w - z| ≤ r := by
      rw [abs_le]
      constructor <;> linarith [hw_le, hw_ge]
    have hwz2 : |w + z| ≤ 2 * z + r := by
      rw [abs_le]
      constructor
      · have : -(w + z) ≤ 0 := by linarith [hw0, hz0]
        linarith [this]
      · linarith [hw_le]
    calc |w + z| * |w - z| ≤ (2 * z + r) * r :=
          mul_le_mul hwz2 hwz (abs_nonneg _) (by linarith [hz0, hr0])
      _ = 2 * z * r + r ^ 2 := by ring
  -- Norm of the trace value.
  have hnorm : ‖TrU N‖ = ‖TrM‖ * w := by
    rw [hTr, norm_mul]
  have hA : ‖TrU N‖ ^ 2 - Bprof TrM (Zfun S Phi Nm yp) (nu N)
      = ‖TrM‖ ^ 2 * (w ^ 2 - z ^ 2) := by
    rw [hnorm, Bprof, mul_pow]
    ring
  have htM0 : 0 ≤ ‖TrM‖ ^ 2 := sq_nonneg _
  have hK0 : 0 ≤ (m : ℝ) * s2 * s0 ^ (2 * m - 1) := by
    apply mul_nonneg
    apply mul_nonneg
    · exact_mod_cast Nat.zero_le m
    · exact hs2
    · exact pow_nonneg hs0 _
  rw [hA, abs_mul, abs_of_nonneg htM0]
  -- Chain: tM2 * |w^2 - z^2| <= tM2 * (2 z r + r^2) <= ... <= K / N
  have step1 : ‖TrM‖ ^ 2 * |w ^ 2 - z ^ 2|
      ≤ ‖TrM‖ ^ 2 * (2 * z * r + r ^ 2) :=
    mul_le_mul_of_nonneg_left habs htM0
  have step2 : ‖TrM‖ ^ 2 * (2 * z * r + r ^ 2)
      ≤ ‖TrM‖ ^ 2 * (2 * s0 ^ m * (C / (N : ℝ)) + (C / (N : ℝ)) ^ 2) := by
    apply mul_le_mul_of_nonneg_left _ htM0
    have h1 : 2 * z * r ≤ 2 * s0 ^ m * (C / (N : ℝ)) := by
      have := mul_le_mul hzle hRle hr0 hs0m
      linarith [this]
    have h2 : r ^ 2 ≤ (C / (N : ℝ)) ^ 2 :=
      pow_le_pow_left₀ hr0 hRle 2
    linarith [h1, h2]
  have step3 : ‖TrM‖ ^ 2 * (2 * s0 ^ m * (C / (N : ℝ)) + (C / (N : ℝ)) ^ 2)
      ≤ ‖TrM‖ ^ 2 * ((2 * s0 ^ m + 1) * (C / (N : ℝ))) := by
    apply mul_le_mul_of_nonneg_left _ htM0
    have hsq : (C / (N : ℝ)) ^ 2 ≤ C / (N : ℝ) := by
      rw [pow_two]
      calc (C / (N : ℝ)) * (C / (N : ℝ)) ≤ (C / (N : ℝ)) * 1 :=
            mul_le_mul_of_nonneg_left hCN hCN0
        _ = C / (N : ℝ) := mul_one _
    linarith [hsq]
  have step4 : ‖TrM‖ ^ 2 * ((2 * s0 ^ m + 1) * (C / (N : ℝ)))
      = ((m : ℝ) * s2 * s0 ^ (2 * m - 1)) / (N : ℝ) := by
    have heq : ‖TrM‖ ^ 2 * ((2 * s0 ^ m + 1) * (C / (N : ℝ)))
        = (‖TrM‖ ^ 2 * (2 * s0 ^ m + 1) * C) / (N : ℝ) := by
      rw [show ‖TrM‖ ^ 2 * ((2 * s0 ^ m + 1) * (C / (N : ℝ)))
          = (‖TrM‖ ^ 2 * (2 * s0 ^ m + 1)) * (C / (N : ℝ)) by ring,
        ← mul_div_assoc]
    rw [heq, hC]
  exact le_trans step1 (le_trans step2 (le_trans step3 (le_of_eq step4)))

/-- The main averaging theorem (175): the window average of
    |Tr U_N^m|^2 differs from the nu-average F_m(eta) by at most
    the claimed error. `hEquidist` is the residue-equidistribution
    bound (analytic, not proved here); `_hNu` pins nu_N as the
    inverse of N mod g'_m (interpretation, from 163). -/
theorem nAverage {g' : ℕ} [NeZero g'] {S : Finset ℤ} {Phi : ℤ → ℂ}
    {Nm : ℤ → ℤ} {yp : ℤ} {TrU : ℕ → ℂ} {TrM : ℂ}
    {nu : ℕ → ZMod g'} {R : ℕ → ℂ}
    {m D : ℕ} {X s0 s2 Deff C : ℝ}
    (hX : 0 < X) (hm : 0 < m) (hs0 : 0 ≤ s0) (hs2 : 0 ≤ s2)
    (hC0 : 0 ≤ C)
    (hC : ‖TrM‖ ^ 2 * (2 * s0 ^ m + 1) * C = m * s2 * s0 ^ (2 * m - 1))
    (hXbig : C ≤ X)
    (hZ : ∀ ν : ZMod g', ‖Zfun S Phi Nm yp ν‖ ≤ s0 ^ m)
    (hTrace : ∀ N ∈ window X D, TrU N = TrM * (Zfun S Phi Nm yp (nu N) + R N) ∧
      ‖R N‖ ≤ C / (N : ℝ))
    (hW : (window X D).Nonempty)
    (hEquidist : |winAvg (window X D) (fun N => Bprof TrM (Zfun S Phi Nm yp) (nu N))
        - nuAvg (Bprof TrM (Zfun (g' := g') S Phi Nm yp))|
        ≤ (D : ℝ) * min (s0 ^ (2 * m)) Deff / X)
    (_hNu : ∀ N ∈ window X D, (nu N) * (N : ZMod g') = 1) :
    |winAvg (window X D) (fun N => ‖TrU N‖ ^ 2)
        - nuAvg (Bprof TrM (Zfun (g' := g') S Phi Nm yp))|
      ≤ (m * s2 * s0 ^ (2 * m - 1)) / X
        + (D : ℝ) * min (s0 ^ (2 * m)) Deff / X := by
  have hmem : ∀ N ∈ window X D, X < N := by
    intro N hN
    exact (mem_window (le_of_lt hX) hN).1
  have hpt := pointwise_bound hX hm hs0 hs2 hC0 hC hXbig hZ hTrace hmem
  have hK0 : 0 ≤ (m : ℝ) * s2 * s0 ^ (2 * m - 1) := by
    apply mul_nonneg
    apply mul_nonneg
    · exact_mod_cast Nat.zero_le m
    · exact hs2
    · exact pow_nonneg hs0 _
  have havg1 : |winAvg (window X D) (fun N => ‖TrU N‖ ^ 2)
      - winAvg (window X D) (fun N => Bprof TrM (Zfun S Phi Nm yp) (nu N))|
      ≤ winAvg (window X D) (fun N => ((m : ℝ) * s2 * s0 ^ (2 * m - 1)) / (N : ℝ)) := by
    apply le_trans (avg_sub_abs_le _ _ _ hW)
    exact avg_mono _ _ _ hW (fun N hN => hpt N hN)
  have havg2 : winAvg (window X D) (fun N => ((m : ℝ) * s2 * s0 ^ (2 * m - 1)) / (N : ℝ))
      ≤ ((m : ℝ) * s2 * s0 ^ (2 * m - 1)) / X := by
    apply avg_le_of_forall_le _ _ _ hW
    intro N hN
    have hNX : X < (N : ℝ) := hmem N hN
    have h1 : (1 : ℝ) / (N : ℝ) ≤ 1 / X := one_div_le_one_div_of_le hX (le_of_lt hNX)
    calc ((m : ℝ) * s2 * s0 ^ (2 * m - 1)) / (N : ℝ)
        = ((m : ℝ) * s2 * s0 ^ (2 * m - 1)) * (1 / (N : ℝ)) :=
        div_eq_mul_one_div _ _
      _ ≤ ((m : ℝ) * s2 * s0 ^ (2 * m - 1)) * (1 / X) :=
        mul_le_mul_of_nonneg_left h1 hK0
      _ = ((m : ℝ) * s2 * s0 ^ (2 * m - 1)) / X :=
        (div_eq_mul_one_div _ _).symm
  have havg : |winAvg (window X D) (fun N => ‖TrU N‖ ^ 2)
        - winAvg (window X D) (fun N => Bprof TrM (Zfun S Phi Nm yp) (nu N))|
        + |winAvg (window X D) (fun N => Bprof TrM (Zfun S Phi Nm yp) (nu N))
        - nuAvg (Bprof TrM (Zfun (g' := g') S Phi Nm yp))|
      ≤ ((m : ℝ) * s2 * s0 ^ (2 * m - 1)) / X
        + (D : ℝ) * min (s0 ^ (2 * m)) Deff / X :=
    add_le_add (le_trans havg1 havg2) hEquidist
  exact le_trans (abs_sub_le _ _ _) havg

/-- The Pell unit exceeds 1. -/
theorem one_lt_lam : 1 < lam := by
  unfold lam
  have h : (0 : ℝ) < Real.sqrt 2 := by positivity
  linarith [h]

/-- The logarithmic window implies the power bound s0^{2m} <= X^{1-eps}.
    If the denominator log lambda + 2 log s0 is <= 0, the window
    hypothesis forces m = 0 and the bound is 1 <= X^{1-eps};
    otherwise multiply the window hypothesis by the denominator
    and use 2 log s0 <= log lambda + 2 log s0. -/
theorem window_pow_le {m : ℕ} {X ε s0 : ℝ}
    (hX1 : 1 < X) (_hε0 : 0 < ε) (hε1 : ε < 1) (hs0 : 0 < s0)
    (hWin : (m : ℝ) ≤ (1 - ε) * cEta s0 * Real.log X) :
    s0 ^ (2 * m) ≤ X ^ ((1 : ℝ) - ε) := by
  have hlam : 0 < Real.log lam := Real.log_pos one_lt_lam
  have hlogX : 0 ≤ Real.log X := Real.log_nonneg (le_of_lt hX1)
  by_cases hden : 0 < Real.log lam + 2 * Real.log s0
  · -- Positive denominator: multiply the window hypothesis by it.
    have hmul : (m : ℝ) * (Real.log lam + 2 * Real.log s0)
        ≤ (1 - ε) * Real.log X := by
      have h := mul_le_mul_of_nonneg_right hWin (le_of_lt hden)
      unfold cEta at h
      have h2 : (1 - ε) * (1 / (Real.log lam + 2 * Real.log s0)) * Real.log X *
          (Real.log lam + 2 * Real.log s0) = (1 - ε) * Real.log X := by
        field_simp
      linarith [h, h2]
    have h3 : (2 * (m : ℝ)) * Real.log s0
        ≤ (m : ℝ) * (Real.log lam + 2 * Real.log s0) := by
      have h4 : (2 : ℝ) * Real.log s0 ≤ Real.log lam + 2 * Real.log s0 := by
        linarith [le_of_lt hlam]
      have h5 : (2 * (m : ℝ)) * Real.log s0 = (m : ℝ) * (2 * Real.log s0) := by
        ring
      rw [h5]
      exact mul_le_mul_of_nonneg_left h4 (Nat.cast_nonneg m)
    have hlog : (2 * (m : ℝ)) * Real.log s0 ≤ (1 - ε) * Real.log X :=
      le_trans h3 hmul
    have e1 : s0 ^ (2 * m) = Real.exp (((2 * m : ℕ) : ℝ) * Real.log s0) := by
      rw [← Real.rpow_natCast, Real.rpow_def_of_pos hs0, mul_comm]
    have e2 : X ^ ((1 : ℝ) - ε) = Real.exp (Real.log X * (1 - ε)) :=
      Real.rpow_def_of_pos (lt_trans zero_lt_one hX1) _
    rw [e1, e2]
    apply Real.exp_le_exp.mpr
    rw [mul_comm (Real.log X) (1 - ε)]
    push_cast
    linarith [hlog]
  · -- Non-positive denominator: the window forces m = 0.
    push Not at hden
    have hm0 : m = 0 := by
      have h1 : (m : ℝ) ≤ 0 := by
        unfold cEta at hWin
        have h2 : (1 - ε) * (1 / (Real.log lam + 2 * Real.log s0)) ≤ 0 :=
          mul_nonpos_of_nonneg_of_nonpos (by linarith [hε1])
            (one_div_nonpos.mpr hden)
        have h3 : (1 - ε) * (1 / (Real.log lam + 2 * Real.log s0)) * Real.log X ≤ 0 :=
          mul_nonpos_of_nonpos_of_nonneg h2 hlogX
        linarith [hWin, h3]
      have h2 : (0 : ℝ) ≤ (m : ℝ) := Nat.cast_nonneg m
      have h3 : (m : ℝ) = 0 := le_antisymm h1 h2
      exact_mod_cast h3
    rw [hm0]
    simp only [Nat.mul_zero, pow_zero]
    exact Real.one_le_rpow (le_of_lt hX1) (by linarith [hε1])

/-- Decay form of the window bound: both 175 error terms are at most
    their prefactors times X^{-eps}. -/
theorem window_error_decay {m : ℕ} {X ε s0 s2 Deff D : ℝ}
    (hX1 : 1 < X) (hε0 : 0 < ε) (hε1 : ε < 1) (hs0 : 0 < s0) (hs2 : 0 ≤ s2)
    (hm : 0 < m) (hD : 0 ≤ D) (_hDeff : 0 ≤ Deff)
    (hWin : (m : ℝ) ≤ (1 - ε) * cEta s0 * Real.log X) :
    (m : ℝ) * s2 * s0 ^ (2 * m - 1) / X ≤ ((m : ℝ) * s2 / s0) * X ^ (-ε) ∧
    D * min (s0 ^ (2 * m)) Deff / X ≤ D * X ^ (-ε) := by
  have hpow : s0 ^ (2 * m) ≤ X ^ ((1 : ℝ) - ε) :=
    window_pow_le hX1 hε0 hε1 hs0 hWin
  have hXpos : (0 : ℝ) < X := lt_trans zero_lt_one hX1
  have hrw : X ^ ((1 : ℝ) - ε) / X = X ^ (-ε) := by
    have h1 : X ^ ((1 : ℝ) - ε) = X * X ^ (-ε) := by
      have h2 : ((1 : ℝ) - ε) = 1 + (-ε) := by ring
      rw [h2, Real.rpow_add hXpos]
      simp
    rw [h1]
    field_simp
  have hpow2 : s0 ^ (2 * m - 1) ≤ X ^ ((1 : ℝ) - ε) / s0 := by
    have hsplit : s0 ^ (2 * m) = s0 ^ (2 * m - 1) * s0 := by
      conv_lhs => rw [← Nat.sub_add_cancel (show 1 ≤ 2 * m by omega)]
      rw [pow_add, pow_one]
    rw [le_div_iff₀ hs0, ← hsplit]
    exact hpow
  constructor
  · have h1 : (m : ℝ) * s2 * s0 ^ (2 * m - 1) / X
        ≤ (m : ℝ) * s2 * (X ^ ((1 : ℝ) - ε) / s0) / X := by
      apply (div_le_div_iff_of_pos_right hXpos).mpr
      exact mul_le_mul_of_nonneg_left hpow2 (by positivity)
    have h2 : (m : ℝ) * s2 * (X ^ ((1 : ℝ) - ε) / s0) / X
        = ((m : ℝ) * s2 / s0) * X ^ (-ε) := by
      rw [← hrw]
      ring
    exact le_trans h1 (le_of_eq h2)
  · have h1 : D * min (s0 ^ (2 * m)) Deff / X ≤ D * X ^ ((1 : ℝ) - ε) / X := by
      apply (div_le_div_iff_of_pos_right hXpos).mpr
      apply mul_le_mul_of_nonneg_left _ hD
      exact le_trans (min_le_left _ _) hpow
    have h2 : D * X ^ ((1 : ℝ) - ε) / X = D * X ^ (-ε) := by
      rw [← hrw]
      ring
    exact le_trans h1 (le_of_eq h2)

#print axioms nAverage
#print axioms traceHence
#print axioms pointwise_bound
#print axioms window_pow_le
#print axioms window_error_decay

end Bgs.LineB.NAverage
