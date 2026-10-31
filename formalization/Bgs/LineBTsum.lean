import Bgs.LineBExpand
import Mathlib.Topology.Algebra.InfiniteSum.Order
import Mathlib.Topology.Algebra.InfiniteSum.Real
import Mathlib.Topology.Algebra.InfiniteSum.Ring

/-!
# BGS Line B, tsum step: from the finite trace formula to infinite mode sums

No `sorry`, no `axiom`, no `native_decide` anywhere in this file.

## What this module does

The chain `TraceFormula → Gauss → Expand` proves Theorem 1(a) of 163 for
trigonometric polynomials: a *finite* Fourier datum `(ĝ, supp)`. This module
passes to a *general* `ĝ : ℤ → ℂ` with `∑ n² |ĝ n| < ∞`, i.e. to `tsum` mode
sums over `Fin m → ℤ`. The key simplification, which is the whole point of
this step, is that the matrices are finite-dimensional (`N × N`): the trace
is continuous, so the trace of the `tsum`-kick is the limit of the traces of
the finite kicks, and the finite mode sums exhaust the `tsum` over all modes.
No infinite-dimensional operator theory is needed anywhere.

## Exact formulation (stage 1 of the brief)

For `ĝ : ℤ → ℂ` with `Summable fun k : ℤ => (k : ℝ) ^ 2 * ‖ĝ k‖` (the source's
`∑ n² |ĝ n| < ∞`), put:

* `kickValInf N ĝ x = ∑' k : ℤ, ĝ k * chi N (k * x)` — the infinite Fourier
  series of the kick at `x`. It is well defined by absolute summability:
  `∑ n² |ĝ n| < ∞` implies `∑ |ĝ n| < ∞` (`summable_norm_of_summable_sq`),
  and `‖chi‖ = 1`.
* `kickMatInf N ĝ = Matrix.diagonal (kickValInf N ĝ)` — the infinite kick.
* `phaseFun m N b n` — exactly the phase of the finite theorem
  (`trace_formula_kick`): `e (Qnum / Dm / N) * e (-(b % gp) * yp * NmZ / gp)`.

The main theorem (`trace_formula_tsum`) is then, for `m ≥ 2`, `N ≥ 2`,
`gcd (Dm m, N) = 1`, `a` with `2 * a * (-4) = 1`:

  `∃ b : ℕ, ((kickMatInf N ĝ * catMat N a) ^ m).trace
      = (catMat N a ^ m).trace
        * ∑' n : Fin m → ℤ, phiFun m ĝ n * phaseFun m N b n`
  `∧ ‖(catMat N a ^ m).trace‖ = 1`.

The parameter `b` is the same one as in the finite theorem, and it is
*controlled*: it is any `b₀` with `(N * b₀ : ZMod (Dm m).toNat) = 1`
(obtained from `exists_inv_mod`), and the finite identity is re-derived for
this fixed `b₀` from `trace_formula_finite` + `hexpand` + `hg0def`
(`trace_formula_kick_b`), so the limit step does not have to chase an
existentially quantified `b` varying with the finite support.

## What is NOT proved here

* The case `m = 1` (the Gauss bridge needs `m ≥ 2`, as in the finite case).
* The equal-layers hypothesis `hfib` and the analytic identification of
  `kickMatInf` with the real quantum kick: the module works with the Fourier
  datum `ĝ` directly, exactly as `Expand` does.
* Theorem 1(c) IS proved here (§7): the `tsum` phase bound
  `‖Tr − TrM · Z‖ ≤ π·m·s2·s0^{m−1}/N`, via the `tsum` product identity
  `∑' n, (∑ j, (n j) ^ 2) * ∏ r, ‖ĝ (n r)‖ = m * s2 * s0 ^ (m - 1)`.
-/

open Filter Topology
open Bgs.LineB.TraceFormula Bgs.LineB.Gauss Bgs.LineB.Expand Bgs.LineB.Derand

namespace Bgs.LineB.Tsum

/-- The infinite kick value at `x`: the `tsum` Fourier series of the kick. -/
noncomputable def kickValInf (N : ℕ) (ĝ : ℤ → ℂ) (x : ZMod N) : ℂ :=
  ∑' k : ℤ, ĝ k * chi N ((k : ZMod N) * x)

/-- The infinite kick matrix (diagonal). -/
noncomputable def kickMatInf (N : ℕ) (ĝ : ℤ → ℂ) : Matrix (ZMod N) (ZMod N) ℂ :=
  Matrix.diagonal (kickValInf N ĝ)

/-- The mode phase, exactly as in the finite theorem `trace_formula_kick`. -/
noncomputable def phaseFun (m N : ℕ) (b : ℕ) (n : Fin m → ℤ) : ℂ :=
  e ((Qnum m n : ℚ) / (Dm m : ℚ) / (N : ℚ) : ℝ)
    * e (-((b % gp m : ℕ) : ℚ) * (yp m : ℚ) * (NmZ m n : ℚ) / (gp m : ℚ) : ℝ)

/-! ### §1. Summability from `∑ n² |ĝ n| < ∞` -/

/-- For a nonzero integer, `1 ≤ k ^ 2` over `ℝ`. -/
lemma one_le_sq_of_ne_zero (k : ℤ) (hk : k ≠ 0) : (1 : ℝ) ≤ (k : ℝ) ^ 2 := by
  have h1 : (1 : ℤ) ≤ |k| := Int.one_le_abs hk
  have h2 : (1 : ℝ) ≤ (|k| : ℝ) := by exact_mod_cast h1
  calc (1 : ℝ) = (1 : ℝ) ^ 2 := by norm_num
    _ ≤ (|k| : ℝ) ^ 2 := pow_le_pow_left₀ zero_le_one h2 2
    _ = (k : ℝ) ^ 2 := sq_abs _

/-- The source's hypothesis `∑ n² |ĝ n| < ∞` implies absolute summability
`∑ |ĝ n| < ∞`. The only subtle point is `k = 0`, where `k ^ 2 = 0`, so the
comparison function carries the `k = 0` term separately. -/
lemma summable_norm_of_summable_sq (ĝ : ℤ → ℂ)
    (hs2 : Summable fun k : ℤ => (k : ℝ) ^ 2 * ‖ĝ k‖) :
    Summable fun k : ℤ => ‖ĝ k‖ := by
  apply summable_of_sum_le (fun k => norm_nonneg _)
    (c := ‖ĝ 0‖ + ∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖)
  intro u
  have hterm : ∀ k : ℤ, ‖ĝ k‖ ≤ (k : ℝ) ^ 2 * ‖ĝ k‖ + (if k = 0 then ‖ĝ 0‖ else 0) := by
    intro k
    by_cases hk : k = 0
    · simp [hk]
    · simp only [hk, if_false, add_zero]
      calc ‖ĝ k‖ = 1 * ‖ĝ k‖ := by rw [one_mul]
        _ ≤ (k : ℝ) ^ 2 * ‖ĝ k‖ :=
            mul_le_mul_of_nonneg_right (one_le_sq_of_ne_zero k hk) (norm_nonneg _)
  calc ∑ k ∈ u, ‖ĝ k‖
      ≤ ∑ k ∈ u, ((k : ℝ) ^ 2 * ‖ĝ k‖ + (if k = 0 then ‖ĝ 0‖ else 0)) :=
        Finset.sum_le_sum fun k _ => hterm k
    _ = (∑ k ∈ u, (k : ℝ) ^ 2 * ‖ĝ k‖) + ∑ k ∈ u, (if k = 0 then ‖ĝ 0‖ else 0) :=
        Finset.sum_add_distrib
    _ ≤ (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖) + ‖ĝ 0‖ := by
        apply add_le_add
        · exact hs2.sum_le_tsum u (fun k _ => by positivity)
        · by_cases h0 : (0 : ℤ) ∈ u
          · rw [Finset.sum_ite_eq' u 0 (fun _ => ‖ĝ 0‖)]
            simp [h0]
          · have hz : ∀ k ∈ u, (if k = 0 then ‖ĝ 0‖ else 0) = 0 := by
              intro k hk
              have hk0 : k ≠ 0 := fun h => h0 (h ▸ hk)
              simp [hk0]
            rw [Finset.sum_eq_zero hz]
            exact norm_nonneg _
    _ = ‖ĝ 0‖ + ∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖ := by rw [add_comm]

/-- The kick series at each `x` is summable: `‖chi‖ = 1`. -/
lemma summable_kick (ĝ : ℤ → ℂ) (hs0 : Summable fun k : ℤ => ‖ĝ k‖)
    (N : ℕ) (x : ZMod N) :
    Summable fun k : ℤ => ĝ k * chi N ((k : ZMod N) * x) := by
  apply Summable.of_norm_bounded hs0
  intro k
  rw [norm_mul, chi]
  simp [e_norm_one]

/-- The finite kick values tend to the infinite kick value along the
directed filter of finite supports: this is `HasSum` unfolded. -/
lemma kickVal_tendsto (ĝ : ℤ → ℂ) (hs0 : Summable fun k : ℤ => ‖ĝ k‖)
    (N : ℕ) (x : ZMod N) :
    Tendsto (fun S : Finset ℤ => kickVal N ĝ S x) atTop (nhds (kickValInf N ĝ x)) :=
  (summable_kick ĝ hs0 N x).hasSum

/-! ### §2. Summability over modes -/

/-- A function on `Fin 1` is its value at `0`. -/
noncomputable def finOneArrowEquiv : (Fin 1 → ℤ) ≃ ℤ where
  toFun n := n 0
  invFun k := fun _ => k
  left_inv n := by
    funext j
    have hj : j = 0 := Subsingleton.elim j 0
    rw [hj]
  right_inv _ := rfl

/-- Splitting off the first coordinate of a `Fin (m + 1)`-mode. -/
noncomputable def finSuccArrowEquiv (m : ℕ) : (Fin (m + 1) → ℤ) ≃ ℤ × (Fin m → ℤ) where
  toFun n := (n 0, Fin.tail n)
  invFun p := Fin.cons p.1 p.2
  left_inv n := Fin.cons_self_tail n
  right_inv p := by
    cases p
    simp [Fin.cons_zero, Fin.tail_cons]

/-- The product of `‖ĝ‖` over a mode is summable over all modes. Induction
from `m = 1` (via `finOneArrowEquiv`) with the `Fin.cons` step (via
`summable_prod_of_nonneg`). -/
lemma mode_norm_summable (ĝ : ℤ → ℂ) (hs0 : Summable fun k : ℤ => ‖ĝ k‖) :
    ∀ m : ℕ, 1 ≤ m → Summable fun n : Fin m → ℤ => ∏ j : Fin m, ‖ĝ (n j)‖ := by
  intro m hm
  induction m, hm using Nat.le_induction with
  | base =>
    have heq : (fun n : Fin 1 → ℤ => ∏ j : Fin 1, ‖ĝ (n j)‖)
        = (fun k : ℤ => ‖ĝ k‖) ∘ finOneArrowEquiv := by
      funext n
      show (∏ j : Fin 1, ‖ĝ (n j)‖) = ‖ĝ (n 0)‖
      exact Fin.prod_univ_one _
    rw [heq]
    exact finOneArrowEquiv.summable_iff.mpr hs0
  | succ m hm ih =>
    have heq : (fun n : Fin (m + 1) → ℤ => ∏ j : Fin (m + 1), ‖ĝ (n j)‖)
        = (fun p : ℤ × (Fin m → ℤ) => ‖ĝ p.1‖ * ∏ j : Fin m, ‖ĝ (p.2 j)‖)
          ∘ finSuccArrowEquiv m := by
      funext n
      show (∏ j : Fin (m + 1), ‖ĝ (n j)‖)
        = ‖ĝ (n 0)‖ * ∏ j : Fin m, ‖ĝ (Fin.tail n j)‖
      rw [Fin.prod_univ_succ]
      congr 1
    rw [heq]
    apply (finSuccArrowEquiv m).summable_iff.mpr
    rw [summable_prod_of_nonneg
      (fun p => mul_nonneg (norm_nonneg _) (Finset.prod_nonneg (fun j _ => norm_nonneg _)))]
    constructor
    · intro k
      show Summable fun y : Fin m → ℤ => ‖ĝ k‖ * ∏ j : Fin m, ‖ĝ (y j)‖
      exact Summable.mul_left _ ih
    · show Summable fun k : ℤ => ∑' n : Fin m → ℤ, ‖ĝ k‖ * ∏ j : Fin m, ‖ĝ (n j)‖
      have hts : (fun k : ℤ => ∑' n : Fin m → ℤ, ‖ĝ k‖ * ∏ j : Fin m, ‖ĝ (n j)‖)
          = fun k => ‖ĝ k‖ * ∑' n : Fin m → ℤ, ∏ j : Fin m, ‖ĝ (n j)‖ := by
        funext k
        exact tsum_mul_left
      rw [hts]
      exact Summable.mul_right _ hs0

/-- The norm of a mode term is the product of `‖ĝ‖` over the mode: the
phases have norm `1`, and the `ZMod m`-product reindexes to `Fin m`. -/
lemma norm_phiFun_mul_phase (m : ℕ) [NeZero m] (ĝ : ℤ → ℂ) (N b : ℕ)
    (n : Fin m → ℤ) :
    ‖phiFun m ĝ n * phaseFun m N b n‖ = ∏ j : Fin m, ‖ĝ (n j)‖ := by
  have h1 : ‖phaseFun m N b n‖ = 1 := by
    unfold phaseFun
    rw [norm_mul, e_norm_one, e_norm_one, mul_one]
  rw [norm_mul, h1, mul_one]
  show ‖∏ r : ZMod m, ĝ (n (zmodFinEquiv m r))‖ = ∏ j : Fin m, ‖ĝ (n j)‖
  rw [norm_prod]
  exact Fintype.prod_equiv (zmodFinEquiv m)
    (fun r => ‖ĝ (n (zmodFinEquiv m r))‖) (fun j => ‖ĝ (n j)‖) (fun _ => rfl)

/-- The mode terms of the `tsum` trace formula are summable. -/
lemma summable_mode (ĝ : ℤ → ℂ) (hs0 : Summable fun k : ℤ => ‖ĝ k‖)
    (m : ℕ) [NeZero m] (hm : 2 ≤ m) (N b : ℕ) :
    Summable fun n : Fin m → ℤ => phiFun m ĝ n * phaseFun m N b n := by
  apply Summable.of_norm
  have h := mode_norm_summable ĝ hs0 m (by omega : 1 ≤ m)
  have heq : (fun n : Fin m → ℤ => ‖phiFun m ĝ n * phaseFun m N b n‖)
      = (fun n => ∏ j : Fin m, ‖ĝ (n j)‖) := by
    funext n
    exact norm_phiFun_mul_phase m ĝ N b n
  rw [heq]
  exact h

/-! ### §3. The finite identity with a controlled `b₀` -/

/-- The finite trace formula, re-derived for a *fixed* `b₀` with
`(N * b₀ : ZMod (Dm m).toNat) = 1`, by replaying the Gauss wrapper's proof
(`trace_formula_finite` + `hexpand` + `hg0def`) instead of applying the
wrapper (whose `∃ b` is opaque). This fixed `b₀` is what survives the
limit step. -/
lemma trace_formula_kick_b (m N : ℕ) [NeZero m] [NeZero N] (ĝ : ℤ → ℂ)
    (supp : Finset ℤ) (a : ZMod N) (hm : 2 ≤ m)
    (hcop : (Dm m).toNat.Coprime N) (hN : 2 ≤ N) (ht0 : 2 * a * (-4) = 1)
    (b₀ : ℕ) (hb₀ : ((N * b₀ : ℕ) : ZMod (Dm m).toNat) = 1) :
    ((kickMat N ĝ supp * catMat N a) ^ m).trace
      = (catMat N a ^ m).trace
        * ∑ n ∈ modeSet m supp, phiFun m ĝ n * phaseFun m N b₀ n
      ∧ ‖(catMat N a ^ m).trace‖ = 1 := by
  obtain ⟨aDℕ, haD⟩ := exists_inv_mod (Dm m).toNat N hcop
  have hcoef : a * (-4) ^ 2 - (-4) = 2 := by
    have h16 : 16 * a = -2 * (2 * a * (-4)) := by ring
    calc a * (-4) ^ 2 - (-4) = 16 * a + 4 := by ring
      _ = -2 * (2 * a * (-4)) + 4 := by rw [h16]
      _ = -2 * 1 + 4 := by rw [ht0]
      _ = 2 := by ring
  have hGauss : ((kickMat N ĝ supp * catMat N a) ^ m).trace
      = (catMat N a ^ m).trace * ∑ n ∈ modeSet m supp, phiFun m ĝ n
        * e ((Qnum m n : ℚ) * (aDℕ : ℚ) / (N : ℚ) : ℝ) := by
    rw [hexpand m N ĝ supp a, hg0def m N a,
      gauss_bridge m N hm (phiFun m ĝ) (modeSet m supp) aDℕ haD a ht0 hcoef,
      mul_assoc]
  have hMod : ‖(catMat N a ^ m).trace‖ = 1 := by
    rw [hg0def m N a]
    exact norm_TrM m N hm aDℕ haD a ht0
  exact trace_formula_finite m N (by omega) hN hcop aDℕ b₀ haD hb₀
    (phiFun m ĝ) (catMat N a ^ m).trace
    ((kickMat N ĝ supp * catMat N a) ^ m).trace (modeSet m supp) hGauss hMod

/-! ### §4. Continuity of the trace in the finite support -/

/-- Entrywise convergence of powers of the kicked matrix: matrix
multiplication is a finite sum of products, so it preserves the
entrywise convergence of the kick values. -/
lemma pow_entry_tendsto (ĝ : ℤ → ℂ) (hs0 : Summable fun k : ℤ => ‖ĝ k‖)
    (N : ℕ) [NeZero N] (a : ZMod N) (p : ℕ) (i j : ZMod N) :
    Tendsto (fun S : Finset ℤ => ((kickMat N ĝ S * catMat N a) ^ p) i j) atTop
      (nhds (((kickMatInf N ĝ * catMat N a) ^ p) i j)) := by
  induction p generalizing i j with
  | zero =>
    simp only [pow_zero]
    exact tendsto_const_nhds
  | succ p ih =>
    have key : Tendsto (fun S : Finset ℤ => ∑ k : ZMod N,
        ((kickMat N ĝ S * catMat N a) ^ p) i k
          * (kickVal N ĝ S k * catMat N a k j))
        atTop (nhds (∑ k : ZMod N,
        ((kickMatInf N ĝ * catMat N a) ^ p) i k
          * (kickValInf N ĝ k * catMat N a k j))) := by
      apply tendsto_finsetSum Finset.univ
      intro k _
      exact (ih i k).mul ((kickVal_tendsto ĝ hs0 N k).mul tendsto_const_nhds)
    have e1 : (fun S : Finset ℤ => ((kickMat N ĝ S * catMat N a) ^ (p + 1)) i j)
        = (fun S : Finset ℤ => ∑ k : ZMod N,
          ((kickMat N ĝ S * catMat N a) ^ p) i k
            * (kickVal N ĝ S k * catMat N a k j)) := by
      funext S
      rw [pow_succ, Matrix.mul_apply]
      apply Finset.sum_congr rfl
      intro k _
      congr 1
      show (Matrix.diagonal (kickVal N ĝ S) * catMat N a) k j = _
      exact Matrix.diagonal_mul _ _ _ _
    have e2 : (((kickMatInf N ĝ * catMat N a) ^ (p + 1)) i j)
        = ∑ k : ZMod N,
          ((kickMatInf N ĝ * catMat N a) ^ p) i k
            * (kickValInf N ĝ k * catMat N a k j) := by
      rw [pow_succ, Matrix.mul_apply]
      apply Finset.sum_congr rfl
      intro k _
      congr 1
      show (Matrix.diagonal (kickValInf N ĝ) * catMat N a) k j = _
      exact Matrix.diagonal_mul _ _ _ _
    rw [e1, e2]
    exact key

/-- The trace is a finite sum of diagonal entries, hence continuous in
the finite support. -/
lemma trace_tendsto (ĝ : ℤ → ℂ) (hs0 : Summable fun k : ℤ => ‖ĝ k‖)
    (N : ℕ) [NeZero N] (a : ZMod N) (m : ℕ) :
    Tendsto (fun S : Finset ℤ => ((kickMat N ĝ S * catMat N a) ^ m).trace) atTop
      (nhds (((kickMatInf N ĝ * catMat N a) ^ m).trace)) := by
  have h : ∀ A : Matrix (ZMod N) (ZMod N) ℂ, A.trace = ∑ i : ZMod N, A i i := by
    intro A
    rfl
  rw [show (fun S : Finset ℤ => ((kickMat N ĝ S * catMat N a) ^ m).trace)
      = (fun S : Finset ℤ => ∑ i : ZMod N, ((kickMat N ĝ S * catMat N a) ^ m) i i) from
      funext fun S => h _]
  rw [show (((kickMatInf N ĝ * catMat N a) ^ m).trace)
      = ∑ i : ZMod N, ((kickMatInf N ĝ * catMat N a) ^ m) i i from h _]
  apply tendsto_finsetSum Finset.univ
  intro i _
  exact pow_entry_tendsto ĝ hs0 N a m i i

/-! ### §5. Exhaustion of modes by finite supports -/

/-- Membership in `modeSet`: a mode is in `modeSet m S` exactly when all
its values lie in `S`. -/
lemma modeSet_mem (m : ℕ) [NeZero m] (S : Finset ℤ) (n : Fin m → ℤ) :
    n ∈ modeSet m S ↔ ∀ j : Fin m, n j ∈ S := by
  constructor
  · intro hn j
    obtain ⟨p, hp, hpn⟩ := Finset.mem_image.mp hn
    have hmem := (Finset.mem_pi.mp hp) ((zmodFinEquiv m).symm j) (Finset.mem_univ _)
    rw [← hpn]
    exact hmem
  · intro hn
    apply Finset.mem_image.mpr
    refine ⟨fun r _ => n (zmodFinEquiv m r), ?_, ?_⟩
    · rw [Finset.mem_pi]
      intro r _
      exact hn (zmodFinEquiv m r)
    · funext j
      show n ((zmodFinEquiv m) ((zmodFinEquiv m).symm j)) = n j
      rw [Equiv.apply_symm_apply]

/-- `modeSet` is monotone in the support. -/
lemma modeSet_mono (m : ℕ) [NeZero m] : Monotone (modeSet m) := by
  intro S T hST n hn
  rw [modeSet_mem] at hn ⊢
  intro j
  exact hST (hn j)

/-- The finite mode sets exhaust all modes: `modeSet m S → atTop` along
`atTop` on finite supports. -/
lemma modeSet_tendsto_atTop (m : ℕ) [NeZero m] :
    Tendsto (modeSet m) atTop atTop := by
  rw [tendsto_atTop]
  intro T
  rw [Filter.eventually_atTop]
  refine ⟨T.biUnion (fun n => Finset.univ.image n), fun S hS => ?_⟩
  intro n hn
  rw [modeSet_mem]
  intro j
  apply hS
  apply Finset.mem_biUnion.mpr
  exact ⟨n, hn, Finset.mem_image.mpr ⟨j, Finset.mem_univ j, rfl⟩⟩

/-- The finite mode sums tend to the `tsum` over all modes. -/
lemma mode_sum_tendsto (ĝ : ℤ → ℂ) (hs0 : Summable fun k : ℤ => ‖ĝ k‖)
    (m : ℕ) [NeZero m] (hm : 2 ≤ m) (N b : ℕ) :
    Tendsto (fun S : Finset ℤ => ∑ n ∈ modeSet m S, phiFun m ĝ n * phaseFun m N b n)
      atTop (nhds (∑' n : Fin m → ℤ, phiFun m ĝ n * phaseFun m N b n)) :=
  (summable_mode ĝ hs0 m hm N b).hasSum.comp (modeSet_tendsto_atTop m)

/-! ### §6. The `tsum` trace formula -/

/-- Theorem 1(a) of 163 for a general kick with `∑ n² |ĝ n| < ∞`, plus
`‖TrM‖ = 1`: the trace of the infinite kick is `TrM` times the `tsum`
over all modes. Proved by taking limits in the finite identity with a
fixed `b₀`: the left side converges by continuity of the trace (§4),
the right side by exhaustion of modes (§5). -/
theorem trace_formula_tsum (m N : ℕ) [NeZero m] [NeZero N] (ĝ : ℤ → ℂ)
    (a : ZMod N) (hm : 2 ≤ m) (hcop : (Dm m).toNat.Coprime N) (hN : 2 ≤ N)
    (ht0 : 2 * a * (-4) = 1) (hs2 : Summable fun k : ℤ => (k : ℝ) ^ 2 * ‖ĝ k‖) :
    ∃ b : ℕ, ((kickMatInf N ĝ * catMat N a) ^ m).trace
      = (catMat N a ^ m).trace
        * ∑' n : Fin m → ℤ, phiFun m ĝ n * phaseFun m N b n
      ∧ ‖(catMat N a ^ m).trace‖ = 1 := by
  have hs0 := summable_norm_of_summable_sq ĝ hs2
  obtain ⟨b₀, hb₀⟩ := exists_inv_mod N (Dm m).toNat (Nat.Coprime.symm hcop)
  have hS : ∀ S : Finset ℤ,
      ((kickMat N ĝ S * catMat N a) ^ m).trace
        = (catMat N a ^ m).trace
          * ∑ n ∈ modeSet m S, phiFun m ĝ n * phaseFun m N b₀ n
        ∧ ‖(catMat N a ^ m).trace‖ = 1 :=
    fun S => trace_formula_kick_b m N ĝ S a hm hcop hN ht0 b₀ hb₀
  have hL1 := trace_tendsto ĝ hs0 N a m
  have hL2 := mode_sum_tendsto ĝ hs0 m hm N b₀
  have hL2' : Tendsto (fun S : Finset ℤ => (catMat N a ^ m).trace
      * ∑ n ∈ modeSet m S, phiFun m ĝ n * phaseFun m N b₀ n)
      atTop (nhds ((catMat N a ^ m).trace
        * ∑' n : Fin m → ℤ, phiFun m ĝ n * phaseFun m N b₀ n)) :=
    hL2.const_mul _
  have hEq : (fun S : Finset ℤ => ((kickMat N ĝ S * catMat N a) ^ m).trace)
      = (fun S : Finset ℤ => (catMat N a ^ m).trace
        * ∑ n ∈ modeSet m S, phiFun m ĝ n * phaseFun m N b₀ n) :=
    funext fun S => (hS S).1
  refine ⟨b₀, ?_, (hS ∅).2⟩
  exact (tendsto_nhds_unique (by rw [hEq]; exact hL2') hL1).symm

/-! ### §7. Theorem 1(c): the `tsum` phase bound -/

/-- A finite sum of summable functions is summable. -/
lemma summable_finset_sum {ι β α : Type*} [AddCommMonoid α] [TopologicalSpace α]
    [ContinuousAdd α] {s : Finset ι} {f : ι → β → α}
    (hf : ∀ j ∈ s, Summable (f j)) :
    Summable fun n => ∑ j ∈ s, f j n := by
  classical
  induction s using Finset.induction with
  | empty =>
    simp only [Finset.sum_empty]
    exact summable_zero
  | insert a s ha ih =>
    have ih' := ih (fun j hj => hf j (Finset.mem_insert_of_mem hj))
    rw [show (fun n => ∑ j ∈ insert a s, f j n) = fun n => f a n + ∑ j ∈ s, f j n from
      funext fun n => Finset.sum_insert ha]
    exact (hf a (Finset.mem_insert_self a s)).add ih'

/-- A product of nonnegative per-coordinate functions over modes is
summable. This generalizes `mode_norm_summable` (the case `f j k = ‖ĝ k‖`).
Induction from `m = 1` with the `Fin.cons` step. -/
lemma summable_mode_prod_nonneg :
    ∀ m : ℕ, 1 ≤ m → ∀ f : Fin m → ℤ → ℝ, (∀ j k, 0 ≤ f j k) →
      (∀ j, Summable (f j)) → Summable fun n : Fin m → ℤ => ∏ j : Fin m, f j (n j) := by
  intro m hm
  induction m, hm using Nat.le_induction with
  | base =>
    intro f _ hf
    have heq : (fun n : Fin 1 → ℤ => ∏ j : Fin 1, f j (n j))
        = (fun k : ℤ => f 0 k) ∘ finOneArrowEquiv := by
      funext n
      show (∏ j : Fin 1, f j (n j)) = f 0 (n 0)
      exact Fin.prod_univ_one _
    rw [heq]
    exact finOneArrowEquiv.summable_iff.mpr (hf 0)
  | succ m hm ih =>
    intro f hf0 hf
    have heq : (fun n : Fin (m + 1) → ℤ => ∏ j : Fin (m + 1), f j (n j))
        = (fun p : ℤ × (Fin m → ℤ) => f 0 p.1 * ∏ j : Fin m, f j.succ (p.2 j))
          ∘ finSuccArrowEquiv m := by
      funext n
      show (∏ j : Fin (m + 1), f j (n j))
        = f 0 (n 0) * ∏ j : Fin m, f j.succ (Fin.tail n j)
      rw [Fin.prod_univ_succ]
      congr 1
    rw [heq]
    apply (finSuccArrowEquiv m).summable_iff.mpr
    rw [summable_prod_of_nonneg
      (fun p => mul_nonneg (hf0 0 _) (Finset.prod_nonneg (fun j _ => hf0 _ _)))]
    constructor
    · intro k
      show Summable fun y : Fin m → ℤ => f 0 k * ∏ j : Fin m, f j.succ (y j)
      exact Summable.mul_left _ (ih _ (fun j k => hf0 _ _) (fun j => hf _))
    · show Summable fun k : ℤ => ∑' n : Fin m → ℤ, f 0 k * ∏ j : Fin m, f j.succ (n j)
      have hts : (fun k : ℤ => ∑' n : Fin m → ℤ, f 0 k * ∏ j : Fin m, f j.succ (n j))
          = fun k => f 0 k * ∑' n : Fin m → ℤ, ∏ j : Fin m, f j.succ (n j) := by
        funext k
        exact tsum_mul_left
      rw [hts]
      exact Summable.mul_right _ (hf 0)

/-- The `tsum` of a mode product is the product of the coordinate `tsum`s,
for nonnegative summable factors. Induction from `m = 1` with the
`Fin.cons` step and `Summable.tsum_mul_tsum`. -/
lemma tsum_mode_prod_value :
    ∀ m : ℕ, 1 ≤ m → ∀ f : Fin m → ℤ → ℝ, (∀ j k, 0 ≤ f j k) →
      (∀ j, Summable (f j)) →
      ∑' n : Fin m → ℤ, ∏ j : Fin m, f j (n j) = ∏ j : Fin m, ∑' k : ℤ, f j k := by
  intro m hm
  induction m, hm using Nat.le_induction with
  | base =>
    intro f _ _
    have h1 : (fun n : Fin 1 → ℤ => ∏ j : Fin 1, f j (n j))
        = fun n => f 0 (finOneArrowEquiv n) := by
      funext n
      show (∏ j : Fin 1, f j (n j)) = f 0 (n 0)
      exact Fin.prod_univ_one _
    rw [h1, Equiv.tsum_eq, Fin.prod_univ_one]
  | succ m hm ih =>
    intro f hf0 hf
    have ihsum : ∀ g : Fin m → ℤ → ℝ, (∀ j k, 0 ≤ g j k) → (∀ j, Summable (g j)) →
        Summable fun n : Fin m → ℤ => ∏ j : Fin m, g j (n j) :=
      fun g hg0 hg => summable_mode_prod_nonneg m hm g hg0 hg
    have hprod : Summable fun z : ℤ × (Fin m → ℤ) =>
        f 0 z.1 * ∏ j : Fin m, f j.succ (z.2 j) := by
      rw [summable_prod_of_nonneg
        (fun z => mul_nonneg (hf0 0 _) (Finset.prod_nonneg (fun j _ => hf0 _ _)))]
      constructor
      · intro k
        show Summable fun y : Fin m → ℤ => f 0 k * ∏ j : Fin m, f j.succ (y j)
        exact Summable.mul_left _
          (ihsum (fun j => f j.succ) (fun j k => hf0 _ _) (fun j => hf _))
      · show Summable fun k : ℤ => ∑' n : Fin m → ℤ, f 0 k * ∏ j : Fin m, f j.succ (n j)
        have hts : (fun k : ℤ => ∑' n : Fin m → ℤ, f 0 k * ∏ j : Fin m, f j.succ (n j))
            = fun k => f 0 k * ∑' n : Fin m → ℤ, ∏ j : Fin m, f j.succ (n j) := by
          funext k
          exact tsum_mul_left
        rw [hts]
        exact Summable.mul_right _ (hf 0)
    have hsplit : (fun n : Fin (m + 1) → ℤ => ∏ j : Fin (m + 1), f j (n j))
        = fun n => f 0 (n 0) * ∏ j : Fin m, f j.succ (n j.succ) := by
      funext n
      exact Fin.prod_univ_succ _
    calc ∑' n : Fin (m + 1) → ℤ, ∏ j : Fin (m + 1), f j (n j)
        = ∑' n : Fin (m + 1) → ℤ, f 0 (n 0) * ∏ j : Fin m, f j.succ (n j.succ) := by
          rw [hsplit]
      _ = ∑' p : ℤ × (Fin m → ℤ), f 0 p.1 * ∏ j : Fin m, f j.succ (p.2 j) := by
          rw [← Equiv.tsum_eq (finSuccArrowEquiv m)
            (fun p : ℤ × (Fin m → ℤ) => f 0 p.1 * ∏ j : Fin m, f j.succ (p.2 j))]
          apply tsum_congr
          intro n
          show f 0 (n 0) * ∏ j : Fin m, f j.succ (n j.succ)
            = f 0 (n 0) * ∏ j : Fin m, f j.succ (Fin.tail n j)
          congr 1
      _ = (∑' k : ℤ, f 0 k) * (∑' n : Fin m → ℤ, ∏ j : Fin m, f j.succ (n j)) :=
          (Summable.tsum_mul_tsum (hf 0)
            (ihsum (fun j => f j.succ) (fun j k => hf0 _ _) (fun j => hf _)) hprod).symm
      _ = (∑' k : ℤ, f 0 k) * ∏ j : Fin m, ∑' k : ℤ, f j.succ k := by
          rw [ih (fun j => f j.succ) (fun j k => hf0 _ _) (fun j => hf _)]
      _ = ∏ j : Fin (m + 1), ∑' k : ℤ, f j k :=
          (Fin.prod_univ_succ (fun j => ∑' k : ℤ, f j k)).symm

/-- The per-coordinate family with a squared factor at position `j`. -/
noncomputable def sqFamily {m : ℕ} (ĝ : ℤ → ℂ) (j : Fin m) (r : Fin m) (k : ℤ) : ℝ :=
  if r = j then (k : ℝ) ^ 2 * ‖ĝ k‖ else ‖ĝ k‖

/-- The squared family is nonnegative. -/
lemma sqFamily_nonneg {m : ℕ} (ĝ : ℤ → ℂ) (j r : Fin m) (k : ℤ) :
    0 ≤ sqFamily ĝ j r k := by
  by_cases hr : r = j
  · rw [show sqFamily ĝ j r k = (k : ℝ) ^ 2 * ‖ĝ k‖ from if_pos hr]
    positivity
  · rw [show sqFamily ĝ j r k = ‖ĝ k‖ from if_neg hr]
    exact norm_nonneg _

/-- The squared family is summable in each coordinate. -/
lemma sqFamily_summable {m : ℕ} (ĝ : ℤ → ℂ) (j r : Fin m)
    (hs0 : Summable fun k : ℤ => ‖ĝ k‖)
    (hs2 : Summable fun k : ℤ => (k : ℝ) ^ 2 * ‖ĝ k‖) :
    Summable (sqFamily ĝ j r) := by
  by_cases hr : r = j
  · rw [show sqFamily ĝ j r = (fun k : ℤ => (k : ℝ) ^ 2 * ‖ĝ k‖) from
      funext fun k => if_pos hr]
    exact hs2
  · rw [show sqFamily ĝ j r = (fun k : ℤ => ‖ĝ k‖) from funext fun k => if_neg hr]
    exact hs0

/-- The squared family product at a mode is the squared coordinate times
the plain product. -/
lemma sqFamily_prod {m : ℕ} (ĝ : ℤ → ℂ) (j : Fin m) (n : Fin m → ℤ) :
    ∏ r : Fin m, sqFamily ĝ j r (n r)
      = ((n j : ℝ)) ^ 2 * ∏ r : Fin m, ‖ĝ (n r)‖ := by
  rw [← Finset.mul_prod_erase Finset.univ (fun r => sqFamily ĝ j r (n r))
    (Finset.mem_univ j)]
  rw [← Finset.mul_prod_erase Finset.univ (fun r => ‖ĝ (n r)‖) (Finset.mem_univ j)]
  have hgj : sqFamily ĝ j j (n j) = ((n j : ℝ)) ^ 2 * ‖ĝ (n j)‖ := if_pos rfl
  have hger : ∏ r ∈ Finset.univ.erase j, sqFamily ĝ j r (n r)
      = ∏ r ∈ Finset.univ.erase j, ‖ĝ (n r)‖ := by
    apply Finset.prod_congr rfl
    intro r hr
    have hrj : r ≠ j := (Finset.mem_erase.mp hr).1
    exact if_neg hrj
  rw [hgj, hger]
  ring

/-- The coordinate `tsum`s of the squared family: `s2` at `j`, `s0`
elsewhere, giving `s2 * s0 ^ (m - 1)`. -/
lemma sqFamily_tsum_prod {m : ℕ} (ĝ : ℤ → ℂ) (j : Fin m) :
    ∏ r : Fin m, ∑' k : ℤ, sqFamily ĝ j r k
      = (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖) * (∑' k : ℤ, ‖ĝ k‖) ^ (m - 1) := by
  rw [← Finset.mul_prod_erase Finset.univ _ (Finset.mem_univ j)]
  have hsj : ∑' k : ℤ, sqFamily ĝ j j k = ∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖ :=
    tsum_congr fun k => if_pos rfl
  have hser : ∏ r ∈ Finset.univ.erase j, ∑' k, sqFamily ĝ j r k
      = (∑' k, ‖ĝ k‖) ^ (m - 1) := by
    have h1 : ∏ r ∈ Finset.univ.erase j, ∑' k, sqFamily ĝ j r k
        = ∏ r ∈ Finset.univ.erase j, ∑' k, ‖ĝ k‖ := by
      apply Finset.prod_congr rfl
      intro r hr
      have hrj : r ≠ j := (Finset.mem_erase.mp hr).1
      exact tsum_congr fun k => if_neg hrj
    rw [h1, Finset.prod_const]
    congr 1
    rw [Finset.card_erase_of_mem (Finset.mem_univ j), Finset.card_univ, Fintype.card_fin]
  rw [hsj, hser]

/-- The mode product times the squared norm is the sum over coordinates
of the squared-coordinate terms. -/
lemma prod_mul_sq_sum (ĝ : ℤ → ℂ) (m : ℕ) :
    (fun n : Fin m → ℤ => (∏ j : Fin m, ‖ĝ (n j)‖) * (∑ j, ((n j : ℝ)) ^ 2))
      = (fun n => ∑ j : Fin m, ((n j : ℝ)) ^ 2 * ∏ r : Fin m, ‖ĝ (n r)‖) := by
  funext n
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro j _
  rw [mul_comm]

/-- The weighted mode sum: `∑' n, (∏ ‖ĝ‖) * ‖n‖² = m * s2 * s0 ^ (m - 1)`. -/
lemma weighted_mode_tsum (m : ℕ) [NeZero m] (hm : 2 ≤ m) (ĝ : ℤ → ℂ)
    (hs0 : Summable fun k : ℤ => ‖ĝ k‖)
    (hs2 : Summable fun k : ℤ => (k : ℝ) ^ 2 * ‖ĝ k‖) :
    ∑' n : Fin m → ℤ, (∏ j : Fin m, ‖ĝ (n j)‖) * (∑ j, ((n j : ℝ)) ^ 2)
      = (m : ℝ) * ((∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖)
        * (∑' k : ℤ, ‖ĝ k‖) ^ (m - 1)) := by
  have hsum : ∀ j : Fin m, Summable fun n : Fin m → ℤ =>
      ((n j : ℝ)) ^ 2 * ∏ r : Fin m, ‖ĝ (n r)‖ := by
    intro j
    have h := summable_mode_prod_nonneg m (by omega) (sqFamily ĝ j)
      (fun r k => sqFamily_nonneg ĝ j r k) (fun r => sqFamily_summable ĝ j r hs0 hs2)
    have heq : (fun n : Fin m → ℤ => ∏ r : Fin m, sqFamily ĝ j r (n r))
        = (fun n => ((n j : ℝ)) ^ 2 * ∏ r : Fin m, ‖ĝ (n r)‖) :=
      funext fun n => sqFamily_prod ĝ j n
    rw [heq] at h
    exact h
  have hC : ∀ j : Fin m, ∑' n : Fin m → ℤ, ((n j : ℝ)) ^ 2 * ∏ r : Fin m, ‖ĝ (n r)‖
      = (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖) * (∑' k : ℤ, ‖ĝ k‖) ^ (m - 1) := by
    intro j
    have hval := tsum_mode_prod_value m (by omega) (sqFamily ĝ j)
      (fun r k => sqFamily_nonneg ĝ j r k) (fun r => sqFamily_summable ĝ j r hs0 hs2)
    have heq : (fun n : Fin m → ℤ => ∏ r : Fin m, sqFamily ĝ j r (n r))
        = (fun n => ((n j : ℝ)) ^ 2 * ∏ r : Fin m, ‖ĝ (n r)‖) :=
      funext fun n => sqFamily_prod ĝ j n
    rw [heq] at hval
    rw [hval]
    exact sqFamily_tsum_prod ĝ j
  rw [prod_mul_sq_sum ĝ m,
    Summable.tsum_finsetSum (s := Finset.univ)
      (f := fun j (n : Fin m → ℤ) => ((n j : ℝ)) ^ 2 * ∏ r : Fin m, ‖ĝ (n r)‖)
      (fun j _ => hsum j)]
  rw [show (∑ j : Fin m, ∑' n : Fin m → ℤ, ((n j : ℝ)) ^ 2 * ∏ r : Fin m, ‖ĝ (n r)‖)
      = ∑ j : Fin m, (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖)
        * (∑' k : ℤ, ‖ĝ k‖) ^ (m - 1) from
      Finset.sum_congr rfl (fun j _ => hC j)]
  rw [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]

/-- The zero-phase: the second factor of `phaseFun`, i.e. the phase with
the `Qnum` term removed. -/
noncomputable def phase0Fun (m _N : ℕ) (b : ℕ) (n : Fin m → ℤ) : ℂ :=
  e (-((b % gp m : ℕ) : ℚ) * (yp m : ℚ) * (NmZ m n : ℚ) / (gp m : ℚ) : ℝ)

/-- `phaseFun` splits as the `Q`-phase times the zero-phase. -/
lemma phaseFun_split (m N : ℕ) (b : ℕ) (n : Fin m → ℤ) :
    phaseFun m N b n
      = e ((Qnum m n : ℚ) / (Dm m : ℚ) / (N : ℚ) : ℝ) * phase0Fun m N b n := rfl

/-- The zero-phase has norm `1`. -/
lemma norm_phase0Fun (m N : ℕ) (b : ℕ) (n : Fin m → ℤ) :
    ‖phase0Fun m N b n‖ = 1 := by
  unfold phase0Fun
  exact e_norm_one _

/-- The norm of `phiFun` itself. -/
lemma norm_phiFun (m : ℕ) [NeZero m] (ĝ : ℤ → ℂ) (n : Fin m → ℤ) :
    ‖phiFun m ĝ n‖ = ∏ j : Fin m, ‖ĝ (n j)‖ := by
  show ‖∏ r : ZMod m, ĝ (n (zmodFinEquiv m r))‖ = ∏ j : Fin m, ‖ĝ (n j)‖
  rw [norm_prod]
  exact Fintype.prod_equiv (zmodFinEquiv m)
    (fun r => ‖ĝ (n (zmodFinEquiv m r))‖) (fun j => ‖ĝ (n j)‖) (fun _ => rfl)

/-- The norm of a mode term with the zero-phase. -/
lemma norm_phiFun_mul_phase0 (m : ℕ) [NeZero m] (ĝ : ℤ → ℂ) (N b : ℕ)
    (n : Fin m → ℤ) :
    ‖phiFun m ĝ n * phase0Fun m N b n‖ = ∏ j : Fin m, ‖ĝ (n j)‖ := by
  rw [norm_mul, norm_phase0Fun, mul_one]
  exact norm_phiFun m ĝ n

/-- The zero-phase mode terms are summable. -/
lemma summable_mode0 (ĝ : ℤ → ℂ) (hs0 : Summable fun k : ℤ => ‖ĝ k‖)
    (m : ℕ) [NeZero m] (hm : 2 ≤ m) (N b : ℕ) :
    Summable fun n : Fin m → ℤ => phiFun m ĝ n * phase0Fun m N b n := by
  apply Summable.of_norm
  have h := mode_norm_summable ĝ hs0 m (by omega : 1 ≤ m)
  have heq : (fun n : Fin m → ℤ => ‖phiFun m ĝ n * phase0Fun m N b n‖)
      = (fun n => ∏ j : Fin m, ‖ĝ (n j)‖) := by
    funext n
    exact norm_phiFun_mul_phase0 m ĝ N b n
  rw [heq]
  exact h

/-- The `Q`-phase argument is bounded by half the squared norm of the mode
over `N`. Note `Q_bound` itself is stated over `ℝ`; only the phase's
`ℚ`-cast needs converting. -/
lemma qphase_le (m N : ℕ) (hm : 1 ≤ m) (hN : 2 ≤ N) (n : Fin m → ℤ) :
    |((Qnum m n : ℚ) / (Dm m : ℚ) / (N : ℚ) : ℝ)|
      ≤ (∑ i, ((n i : ℝ)) ^ 2) / (2 * (N : ℝ)) := by
  have hNℝ : (0 : ℝ) < N := by exact_mod_cast (by omega : 0 < N)
  have hcast : ((Qnum m n : ℚ) / (Dm m : ℚ) / (N : ℚ) : ℝ)
      = (Qnum m n : ℝ) / (Dm m : ℝ) / (N : ℝ) := by
    simp only [Rat.cast_intCast, Rat.cast_natCast]
  rw [hcast, abs_of_nonneg (div_nonneg (Q_bound m hm n).1 hNℝ.le), ← div_div,
    div_le_iff₀ hNℝ, div_mul_cancel₀ _ (ne_of_gt hNℝ)]
  exact (Q_bound m hm n).2

/-- Per-mode bound for the difference between the `Q`-phase term and the
zero-phase term. -/
lemma diff_term_bound (m N : ℕ) [NeZero m] (hm : 1 ≤ m) (hN : 2 ≤ N)
    (ĝ : ℤ → ℂ) (b : ℕ) (n : Fin m → ℤ) :
    ‖phiFun m ĝ n * phaseFun m N b n - phiFun m ĝ n * phase0Fun m N b n‖
      ≤ (Real.pi / (N : ℝ))
        * ((∏ j : Fin m, ‖ĝ (n j)‖) * (∑ j, ((n j : ℝ)) ^ 2)) := by
  have hdiff : phiFun m ĝ n * phaseFun m N b n - phiFun m ĝ n * phase0Fun m N b n
      = phiFun m ĝ n * (e ((Qnum m n : ℚ) / (Dm m : ℚ) / (N : ℚ) : ℝ) - 1)
        * phase0Fun m N b n := by
    rw [phaseFun_split]
    ring
  have hNℝ : (0 : ℝ) < N := by exact_mod_cast (by omega : 0 < N)
  have hNe : (N : ℝ) ≠ 0 := ne_of_gt hNℝ
  rw [hdiff, norm_mul, norm_mul, norm_phiFun m ĝ n, norm_phase0Fun, mul_one]
  have hQ := qphase_le m N hm hN n
  have he := e_sub_one_le ((Qnum m n : ℚ) / (Dm m : ℚ) / (N : ℚ) : ℝ)
  calc (∏ j : Fin m, ‖ĝ (n j)‖)
        * ‖e ((Qnum m n : ℚ) / (Dm m : ℚ) / (N : ℚ) : ℝ) - 1‖
      ≤ (∏ j : Fin m, ‖ĝ (n j)‖)
        * (2 * Real.pi * ((∑ j, ((n j : ℝ)) ^ 2) / (2 * (N : ℝ)))) := by
          apply mul_le_mul_of_nonneg_left _ (Finset.prod_nonneg (fun j _ => norm_nonneg _))
          exact le_trans he (mul_le_mul_of_nonneg_left hQ (by positivity))
    _ = (Real.pi / (N : ℝ))
        * ((∏ j : Fin m, ‖ĝ (n j)‖) * (∑ j, ((n j : ℝ)) ^ 2)) := by
          field_simp

/-- Theorem 1(c) for the `tsum` version: the trace with the `Q`-phases
differs from the trace with zero phases by at most `π·m·s2·s0^{m-1}/N`. -/
theorem trace_formula_tsum_error (m N : ℕ) [NeZero m] [NeZero N] (ĝ : ℤ → ℂ)
    (a : ZMod N) (hm : 2 ≤ m) (hcop : (Dm m).toNat.Coprime N) (hN : 2 ≤ N)
    (ht0 : 2 * a * (-4) = 1) (hs2 : Summable fun k : ℤ => (k : ℝ) ^ 2 * ‖ĝ k‖) :
    ∃ b : ℕ, ((kickMatInf N ĝ * catMat N a) ^ m).trace
      = (catMat N a ^ m).trace
        * ∑' n : Fin m → ℤ, phiFun m ĝ n * phaseFun m N b n
      ∧ ‖(catMat N a ^ m).trace‖ = 1
      ∧ ‖((kickMatInf N ĝ * catMat N a) ^ m).trace
        - (catMat N a ^ m).trace
          * ∑' n : Fin m → ℤ, phiFun m ĝ n * phase0Fun m N b n‖
        ≤ Real.pi * (m : ℝ) * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖)
          * (∑' k : ℤ, ‖ĝ k‖) ^ (m - 1) / (N : ℝ) := by
  have hs0 := summable_norm_of_summable_sq ĝ hs2
  obtain ⟨b₀, hTr, hNorm⟩ := trace_formula_tsum m N ĝ a hm hcop hN ht0 hs2
  refine ⟨b₀, hTr, hNorm, ?_⟩
  have hsumQ := summable_mode ĝ hs0 m hm N b₀
  have hsum0 := summable_mode0 ĝ hs0 m hm N b₀
  have hdiff : (∑' n : Fin m → ℤ, phiFun m ĝ n * phaseFun m N b₀ n)
      - (∑' n : Fin m → ℤ, phiFun m ĝ n * phase0Fun m N b₀ n)
      = ∑' n : Fin m → ℤ, (phiFun m ĝ n * phaseFun m N b₀ n
        - phiFun m ĝ n * phase0Fun m N b₀ n) :=
    (Summable.tsum_sub hsumQ hsum0).symm
  have hsum : ∀ j : Fin m, Summable fun n : Fin m → ℤ =>
      ((n j : ℝ)) ^ 2 * ∏ r : Fin m, ‖ĝ (n r)‖ := by
    intro j
    have h := summable_mode_prod_nonneg m (by omega) (sqFamily ĝ j)
      (fun r k => sqFamily_nonneg ĝ j r k) (fun r => sqFamily_summable ĝ j r hs0 hs2)
    have heq : (fun n : Fin m → ℤ => ∏ r : Fin m, sqFamily ĝ j r (n r))
        = (fun n => ((n j : ℝ)) ^ 2 * ∏ r : Fin m, ‖ĝ (n r)‖) :=
      funext fun n => sqFamily_prod ĝ j n
    rw [heq] at h
    exact h
  have hbound : Summable fun n : Fin m → ℤ =>
      (Real.pi / (N : ℝ)) * ((∏ j : Fin m, ‖ĝ (n j)‖) * (∑ j, ((n j : ℝ)) ^ 2)) := by
    apply Summable.mul_left
    rw [prod_mul_sq_sum ĝ m]
    exact summable_finset_sum (s := Finset.univ)
      (f := fun j (n : Fin m → ℤ) => ((n j : ℝ)) ^ 2 * ∏ r : Fin m, ‖ĝ (n r)‖)
      (fun j _ => hsum j)
  have hnormdiff : Summable fun n : Fin m → ℤ =>
      ‖phiFun m ĝ n * phaseFun m N b₀ n - phiFun m ĝ n * phase0Fun m N b₀ n‖ := by
    refine Summable.of_nonneg_of_le (fun n => norm_nonneg _)
      (fun n => diff_term_bound m N (by omega) hN ĝ b₀ n) hbound
  rw [hTr, ← mul_sub, hdiff, norm_mul, hNorm, one_mul]
  calc ‖∑' n : Fin m → ℤ, (phiFun m ĝ n * phaseFun m N b₀ n
        - phiFun m ĝ n * phase0Fun m N b₀ n)‖
      ≤ ∑' n : Fin m → ℤ, ‖phiFun m ĝ n * phaseFun m N b₀ n
        - phiFun m ĝ n * phase0Fun m N b₀ n‖ :=
        norm_tsum_le_tsum_norm hnormdiff
    _ ≤ ∑' n : Fin m → ℤ, (Real.pi / (N : ℝ))
        * ((∏ j : Fin m, ‖ĝ (n j)‖) * (∑ j, ((n j : ℝ)) ^ 2)) :=
        Summable.tsum_le_tsum (fun n => diff_term_bound m N (by omega) hN ĝ b₀ n)
          hnormdiff hbound
    _ = (Real.pi / (N : ℝ)) * ((m : ℝ) * ((∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖)
        * (∑' k : ℤ, ‖ĝ k‖) ^ (m - 1))) := by
        rw [tsum_mul_left, weighted_mode_tsum m hm ĝ hs0 hs2]
    _ = Real.pi * (m : ℝ) * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖)
        * (∑' k : ℤ, ‖ĝ k‖) ^ (m - 1) / (N : ℝ) := by
        rw [div_mul_eq_mul_div]
        ring

/- Axiom audit for all theorems of this module. -/
#print axioms Bgs.LineB.Tsum.one_le_sq_of_ne_zero
#print axioms Bgs.LineB.Tsum.summable_norm_of_summable_sq
#print axioms Bgs.LineB.Tsum.summable_kick
#print axioms Bgs.LineB.Tsum.kickVal_tendsto
#print axioms Bgs.LineB.Tsum.mode_norm_summable
#print axioms Bgs.LineB.Tsum.norm_phiFun_mul_phase
#print axioms Bgs.LineB.Tsum.summable_mode
#print axioms Bgs.LineB.Tsum.trace_formula_kick_b
#print axioms Bgs.LineB.Tsum.pow_entry_tendsto
#print axioms Bgs.LineB.Tsum.trace_tendsto
#print axioms Bgs.LineB.Tsum.modeSet_mem
#print axioms Bgs.LineB.Tsum.modeSet_mono
#print axioms Bgs.LineB.Tsum.modeSet_tendsto_atTop
#print axioms Bgs.LineB.Tsum.mode_sum_tendsto
#print axioms Bgs.LineB.Tsum.trace_formula_tsum
#print axioms Bgs.LineB.Tsum.summable_finset_sum
#print axioms Bgs.LineB.Tsum.summable_mode_prod_nonneg
#print axioms Bgs.LineB.Tsum.tsum_mode_prod_value
#print axioms Bgs.LineB.Tsum.sqFamily_nonneg
#print axioms Bgs.LineB.Tsum.sqFamily_summable
#print axioms Bgs.LineB.Tsum.sqFamily_prod
#print axioms Bgs.LineB.Tsum.sqFamily_tsum_prod
#print axioms Bgs.LineB.Tsum.prod_mul_sq_sum
#print axioms Bgs.LineB.Tsum.weighted_mode_tsum
#print axioms Bgs.LineB.Tsum.norm_phase0Fun
#print axioms Bgs.LineB.Tsum.phaseFun_split
#print axioms Bgs.LineB.Tsum.norm_phiFun
#print axioms Bgs.LineB.Tsum.norm_phiFun_mul_phase0
#print axioms Bgs.LineB.Tsum.summable_mode0
#print axioms Bgs.LineB.Tsum.qphase_le
#print axioms Bgs.LineB.Tsum.diff_term_bound
#print axioms Bgs.LineB.Tsum.trace_formula_tsum_error

end Bgs.LineB.Tsum
