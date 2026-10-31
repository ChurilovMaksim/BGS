/-
# BGS-TRACE-152, concrete data: Gaussian factor, concrete mode sums,
# and equality of limits across residues

TEST COPY ONLY — not pushed to the repository, registry untouched,
`Bgs.lean` aggregator unchanged (built by a direct `lake build`
target, not imported by the aggregator).

What is proved here, and what is NOT:

* (G ensemble, ω) The Gaussian factor
  `gaussOmega a k z = exp (-(a k * z)^2 / 4)` satisfies the three
  ω-hypotheses of `StrongKickBridge.strong_kick_limit_phihatFix`
  (`gaussOmega_zero`, `gaussOmega_bound`, `gaussOmega_lim`), under
  `a k ≠ 0` for the limit. Hence `strong_kick_limit_gauss`: the
  strong-kick limit with the Gaussian factor, with ONLY the
  S-hypotheses (`hSInv`, `hSep`) remaining.
* (concrete S, hSInv) The source's mode sums
  `S_k(ξ) = Σ_j e(k ξ_j)` (band_limited_kick_bridge.md, D3 proof),
  on the finite model `Fix m` via `ξ_j = (ξ.1 j).val / D_m`,
  are Γ-invariant (`modeSum_smul`): Γ acts by coordinate
  precomposition (`gamma_smul_apply`) and `gammaPerm` is bijective,
  so this is reindexing.
* (limits across residues) For odd `s₁ s₂` coprime to `D_m`, the
  η → ∞ limits of `PsiPair` with `phihatFix` weights coincide
  (`strong_kick_limit_eq_of_odd`): the supports are equal
  (`phihatFix_support_odd_eq`) hence the `Bsym` values are equal
  (`bsym_phihatFix_eq_of_odd`, via `orbitSum_eq_bsym`).
* (G assembly) The complex G-ensemble pair sum equals the doubled
  real pair sum (`psiPairC_gauss_eq`: the Gaussian splits over
  real/imaginary parts, unlike J0), hence
  `strong_kick_limit_gaussC`: the G-ensemble limit with the
  concrete modes over a finite `𝒦`, under only complex separation
  (`hSepC`).

What is deliberately NOT claimed:

* The J0 ensemble: `ω = J0(a|z|)` (Kluyver average, recorded in
  BGS-TRACE-133). Mathlib has no Bessel `J0`, so the decay
  `J0(x) → 0` and the Kluyver average identity itself are analytic
  inputs, not proved here. The Gaussian case above is the ensemble
  for which the ω-hypotheses close from Mathlib alone.
* `hSep` for the concrete modes: the source (D5) proves
  power sums ⇒ point multiset [P] by Newton, but
  multiset ⇒ Γ-class only by exact check for `m ≤ 7` [CA].
  So separation stays an explicit hypothesis in general; the Newton
  step alone would not close it, and no Newton-identities lemma
  was found in Mathlib.
* The N-step (`hN` of `strong_kick_limit_iterated`): it needs the
  149 chain — `hTrace` (Boasman–Keating per θ), `hAvg`/`hE`
  (ensemble average), `hPair` (mode sum = pair sum) — plus
  C^∞-continuity of Ψ in `t` (explicitly absent infrastructure,
  see `LineDBridge` header) and `t_N → t*` (D2), and the 150 link
  needs `hcollapse` on top. None of that is attempted here.

No `sorry`, no `admit`, no `axiom`, no `native_decide`, no `decide`
in this file. `#print axioms` for the main theorems is at the end.
-/

import Bgs.LineDStrongKickBridge
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Exponential
import Mathlib.Analysis.Normed.Ring.Basic
import Mathlib.Topology.Order.Basic

namespace Bgs
namespace LineD
namespace StrongKickConc

open Bgs.LineD
open Finset Filter Topology
open scoped Matrix

/-! ### §1. The Gaussian factor (G ensemble): the ω-hypotheses -/

/-- The Gaussian factor of the G ensemble: `exp (-(a k * z)^2 / 4)`.
    The source's form is `exp (-a^2 |z|^2 / 4)` for complex `z`;
    this is its real restriction, which is what the block's `PsiPair`
    (real mode values) takes. -/
noncomputable def gaussOmega {K : Type*} (a : K → ℝ) (k : K) (z : ℝ) : ℂ :=
  Complex.exp (((-(a k * z) ^ 2 / 4 : ℝ) : ℂ))

/-- `ω k 0 = 1` for the Gaussian factor. No hypothesis on `a`. -/
theorem gaussOmega_zero {K : Type*} (a : K → ℝ) (k : K) :
    gaussOmega a k 0 = 1 := by
  simp [gaussOmega]

/-- Norm of the Gaussian factor, in real form. -/
theorem gaussOmega_norm {K : Type*} (a : K → ℝ) (k : K) (z : ℝ) :
    ‖gaussOmega a k z‖ = Real.exp (-(a k * z) ^ 2 / 4) := by
  unfold gaussOmega
  rw [Complex.norm_exp, Complex.ofReal_re]

/-- `‖ω k z‖ ≤ 1` for the Gaussian factor. No hypothesis on `a`. -/
theorem gaussOmega_bound {K : Type*} (a : K → ℝ) (k : K) (z : ℝ) :
    ‖gaussOmega a k z‖ ≤ 1 := by
  rw [gaussOmega_norm]
  rw [Real.exp_le_one_iff]
  have h : (0:ℝ) ≤ (a k * z) ^ 2 := sq_nonneg _
  linarith

/-- The quadratic `η^2` tends to `atTop` (elementary, no lemma-name
    dependence). -/
theorem tendsto_sq_atTop : Tendsto (fun η : ℝ => η ^ 2) atTop atTop := by
  apply tendsto_atTop_mono' atTop _ tendsto_id
  filter_upwards [eventually_ge_atTop (1:ℝ)] with η hη
  calc η = η * 1 := (mul_one η).symm
    _ ≤ η * η := mul_le_mul_of_nonneg_left hη (by linarith)
    _ = η ^ 2 := by ring

/-- Decay of the Gaussian factor: `ω k (η * Δ) → 0` for `Δ ≠ 0`,
    under `a k ≠ 0` (the boundary's `a_k ≠ 0`). -/
theorem gaussOmega_lim {K : Type*} (a : K → ℝ) (ha : ∀ k, a k ≠ 0)
    (k : K) (Δ : ℝ) (hΔ : Δ ≠ 0) :
    Tendsto (fun η : ℝ => gaussOmega a k (η * Δ)) atTop (𝓝 0) := by
  have haΔ : (a k * Δ) ≠ 0 := mul_ne_zero (ha k) hΔ
  have hC : (0:ℝ) < (a k * Δ) ^ 2 / 4 := by positivity
  have hX : Tendsto (fun η : ℝ => (a k * Δ) ^ 2 / 4 * η ^ 2) atTop atTop :=
    Filter.Tendsto.const_mul_atTop hC tendsto_sq_atTop
  have hexp : Tendsto (fun η : ℝ => Real.exp ((a k * Δ) ^ 2 / 4 * η ^ 2))
      atTop atTop :=
    Real.tendsto_exp_atTop.comp hX
  have hlim : Tendsto
      (fun η : ℝ => Real.exp (-((a k * Δ) ^ 2 / 4 * η ^ 2))) atTop (𝓝 0) := by
    simp only [Real.exp_neg]
    exact tendsto_inv_atTop_zero.comp hexp
  rw [tendsto_zero_iff_norm_tendsto_zero]
  have hnorm : ∀ η : ℝ, ‖gaussOmega a k (η * Δ)‖
      = Real.exp (-((a k * Δ) ^ 2 / 4 * η ^ 2)) := by
    intro η
    rw [gaussOmega_norm]
    congr 1
    ring
  simpa only [hnorm] using hlim

/-- The strong-kick limit with the Gaussian factor: the ω-hypotheses
    are discharged, only `hSInv`/`hSep` remain. The `Bsym` target is
    copied verbatim from `strong_kick_limit_phihatFix`. -/
theorem strong_kick_limit_gauss (m : ℕ) [NeZero m] {K : Type*}
    [Fintype K] (S : OrbitPair.Fix m → K → ℝ) (a : K → ℝ)
    (ha : ∀ k, a k ≠ 0) (s : ℤ)
    (_hodd : Odd s) (hs : IsCoprime s (Defs.Dm m))
    (hSInv : ∀ (g : DihedralGroup m) (ξ : OrbitPair.Fix m) (k : K),
      S (g • ξ) k = S ξ k)
    (hSep : ∀ (ξ ξ' : OrbitPair.Fix m),
      (∀ k, S ξ k = S ξ' k) → ξ' ∈ Parity.orbitFinset (DihedralGroup m) ξ) :
    Tendsto (fun η : ℝ => OrbitPair.PsiPair m (OrbitPairFull.phihatFix m) S
        (gaussOmega a) η s)
      atTop
      (𝓝 (((@Parity.Bsym (DihedralGroup m)
        ↥(OrbitPair.support m (OrbitPairFull.phihatFix m s))
        inferInstance
        (OrbitPair.supportMulAction m (OrbitPairFull.phihatFix m s)
          (fun g ξ hξ => StrongKickBridge.phihatFix_support_inv m s g ξ hξ))
        inferInstance : ℚ)) : ℂ)) :=
  StrongKickBridge.strong_kick_limit_phihatFix m S (gaussOmega a) s _hodd hs
    (gaussOmega_zero a) (gaussOmega_bound a) (gaussOmega_lim a ha)
    hSInv hSep

/-! ### §2. The concrete mode sums: Γ-invariance -/

/-- The source's mode sum `S_k(ξ) = Σ_j e(k ξ_j)` (D3 proof), on the
    finite model: `ξ_j` is `(ξ.1 j).val / D_m` mod 1, and `k` is an
    integer, so `e(k ξ_j)` depends only on `(ξ.1 j).val`. -/
noncomputable def modeSum (m : ℕ) [NeZero m] (k : ℤ)
    (ξ : OrbitPair.Fix m) : ℂ :=
  ∑ j : ZMod m, Complex.exp (2 * Real.pi * Complex.I *
    (((k * ((ξ.1 j).val : ℤ) : ℂ)) / (Defs.Dm m : ℂ)))

/-- Γ-invariance of the concrete mode sums: Γ acts by coordinate
    precomposition and `gammaPerm` is bijective, so this is
    reindexing. This discharges `hSInv` for the concrete modes. -/
theorem modeSum_smul (m : ℕ) [NeZero m] (k : ℤ)
    (g : DihedralGroup m) (ξ : OrbitPair.Fix m) :
    modeSum m k (g • ξ) = modeSum m k ξ := by
  unfold modeSum
  simp only [OrbitPairFull.gamma_smul_apply]
  exact Equiv.sum_comp
    (Equiv.ofBijective (OrbitPairFull.gammaPerm m g)
      (StrongKickBridge.gammaPerm_bijective m g))
    (fun j => Complex.exp (2 * Real.pi * Complex.I *
      (((k * ((ξ.1 j).val : ℤ) : ℂ)) / (Defs.Dm m : ℂ))))

/-! ### §3. Equality of limits across residues -/

/-- The `phihatFix` support is the same for odd `s₁ s₂` coprime to
    `D_m` (from `phihatFix_support_odd_eq`, pointwise). -/
theorem phihatFix_support_eq_of_odd (m : ℕ) [NeZero m] (s₁ s₂ : ℤ)
    (hs1 : IsCoprime s₁ (Defs.Dm m)) (hs2 : IsCoprime s₂ (Defs.Dm m))
    (hodd1 : Odd s₁) (hodd2 : Odd s₂) :
    OrbitPair.support m (OrbitPairFull.phihatFix m s₁)
      = OrbitPair.support m (OrbitPairFull.phihatFix m s₂) := by
  ext ξ
  rw [StrongKick.mem_support_iff, StrongKick.mem_support_iff]
  exact not_congr
    (OrbitPairFull.phihatFix_support_odd_eq m s₁ s₂ hs1 hs2 hodd1 hodd2 ξ)

/-- The `Bsym` limit value is the same for odd `s₁ s₂` coprime to
    `D_m`: both equal `c * Σ_{supp} |Γξ|` with the same support. -/
theorem bsym_phihatFix_eq_of_odd (m : ℕ) [NeZero m] (s₁ s₂ : ℤ)
    (hs1 : IsCoprime s₁ (Defs.Dm m)) (hs2 : IsCoprime s₂ (Defs.Dm m))
    (hodd1 : Odd s₁) (hodd2 : Odd s₂) :
    (((@Parity.Bsym (DihedralGroup m)
      ↥(OrbitPair.support m (OrbitPairFull.phihatFix m s₁))
      inferInstance
      (OrbitPair.supportMulAction m (OrbitPairFull.phihatFix m s₁)
        (fun g ξ hξ => StrongKickBridge.phihatFix_support_inv m s₁ g ξ hξ))
      inferInstance : ℚ)) : ℂ)
    = (((@Parity.Bsym (DihedralGroup m)
      ↥(OrbitPair.support m (OrbitPairFull.phihatFix m s₂))
      inferInstance
      (OrbitPair.supportMulAction m (OrbitPairFull.phihatFix m s₂)
        (fun g ξ hξ => StrongKickBridge.phihatFix_support_inv m s₂ g ξ hξ))
      inferInstance : ℚ)) : ℂ) := by
  have hsupp := phihatFix_support_eq_of_odd m s₁ s₂ hs1 hs2 hodd1 hodd2
  have e1 := @StrongKick.orbitSum_eq_bsym m _ (DihedralGroup m) _ _
    (OrbitPairFull.phihatFix m s₁)
    (fun g ξ hξ => StrongKickBridge.phihatFix_support_inv m s₁ g ξ hξ)
    (OrbitPair.supportMulAction m (OrbitPairFull.phihatFix m s₁)
      (fun g ξ hξ => StrongKickBridge.phihatFix_support_inv m s₁ g ξ hξ))
    (fun _ _ => rfl)
    ((Fintype.card (OrbitPair.V4 m) : ℂ) / (Defs.Dm m : ℂ))
    (OrbitPair.support m (OrbitPairFull.phihatFix m s₁)).card
    (StrongKickBridge.phihatFix_cardPos m s₁ hs1)
    rfl
    (StrongKickBridge.phihatFix_hNorm m s₁ hs1)
  have e2 := @StrongKick.orbitSum_eq_bsym m _ (DihedralGroup m) _ _
    (OrbitPairFull.phihatFix m s₂)
    (fun g ξ hξ => StrongKickBridge.phihatFix_support_inv m s₂ g ξ hξ)
    (OrbitPair.supportMulAction m (OrbitPairFull.phihatFix m s₂)
      (fun g ξ hξ => StrongKickBridge.phihatFix_support_inv m s₂ g ξ hξ))
    (fun _ _ => rfl)
    ((Fintype.card (OrbitPair.V4 m) : ℂ) / (Defs.Dm m : ℂ))
    (OrbitPair.support m (OrbitPairFull.phihatFix m s₂)).card
    (StrongKickBridge.phihatFix_cardPos m s₂ hs2)
    rfl
    (StrongKickBridge.phihatFix_hNorm m s₂ hs2)
  calc (((@Parity.Bsym (DihedralGroup m)
        ↥(OrbitPair.support m (OrbitPairFull.phihatFix m s₁))
        inferInstance
        (OrbitPair.supportMulAction m (OrbitPairFull.phihatFix m s₁)
          (fun g ξ hξ => StrongKickBridge.phihatFix_support_inv m s₁ g ξ hξ))
        inferInstance : ℚ)) : ℂ)
      = ((Fintype.card (OrbitPair.V4 m) : ℂ) / (Defs.Dm m : ℂ)) *
          ∑ ξ ∈ OrbitPair.support m (OrbitPairFull.phihatFix m s₁),
            ((Parity.orbitFinset (DihedralGroup m) ξ).card : ℂ) := e1.symm
    _ = ((Fintype.card (OrbitPair.V4 m) : ℂ) / (Defs.Dm m : ℂ)) *
          ∑ ξ ∈ OrbitPair.support m (OrbitPairFull.phihatFix m s₂),
            ((Parity.orbitFinset (DihedralGroup m) ξ).card : ℂ) := by
        rw [hsupp]
    _ = (((@Parity.Bsym (DihedralGroup m)
        ↥(OrbitPair.support m (OrbitPairFull.phihatFix m s₂))
        inferInstance
        (OrbitPair.supportMulAction m (OrbitPairFull.phihatFix m s₂)
          (fun g ξ hξ => StrongKickBridge.phihatFix_support_inv m s₂ g ξ hξ))
        inferInstance : ℚ)) : ℂ) := e2

/-- Equality of the η → ∞ limits across odd coprime residues: both
    `PsiPair` families tend to the same `Bsym` value. The `S`/`ω`
    hypotheses are the same for both residues; only the support
    equality is new. -/
theorem strong_kick_limit_eq_of_odd (m : ℕ) [NeZero m] {K : Type*}
    [Fintype K] (S : OrbitPair.Fix m → K → ℝ) (ω : K → ℝ → ℂ)
    (s₁ s₂ : ℤ)
    (_hodd1 : Odd s₁) (_hodd2 : Odd s₂)
    (hs1 : IsCoprime s₁ (Defs.Dm m)) (hs2 : IsCoprime s₂ (Defs.Dm m))
    (hω0 : ∀ k, ω k 0 = 1)
    (hωbound : ∀ k (z : ℝ), ‖ω k z‖ ≤ 1)
    (hωlim : ∀ (k : K) (Δ : ℝ), Δ ≠ 0 →
      Tendsto (fun η : ℝ => ω k (η * Δ)) atTop (𝓝 0))
    (hSInv : ∀ (g : DihedralGroup m) (ξ : OrbitPair.Fix m) (k : K),
      S (g • ξ) k = S ξ k)
    (hSep : ∀ (ξ ξ' : OrbitPair.Fix m),
      (∀ k, S ξ k = S ξ' k) → ξ' ∈ Parity.orbitFinset (DihedralGroup m) ξ) :
    Tendsto (fun η : ℝ => OrbitPair.PsiPair m (OrbitPairFull.phihatFix m) S ω
        η s₁)
      atTop
      (𝓝 (((@Parity.Bsym (DihedralGroup m)
        ↥(OrbitPair.support m (OrbitPairFull.phihatFix m s₁))
        inferInstance
        (OrbitPair.supportMulAction m (OrbitPairFull.phihatFix m s₁)
          (fun g ξ hξ => StrongKickBridge.phihatFix_support_inv m s₁ g ξ hξ))
        inferInstance : ℚ)) : ℂ))
    ∧ Tendsto (fun η : ℝ => OrbitPair.PsiPair m (OrbitPairFull.phihatFix m) S ω
        η s₂)
      atTop
      (𝓝 (((@Parity.Bsym (DihedralGroup m)
        ↥(OrbitPair.support m (OrbitPairFull.phihatFix m s₁))
        inferInstance
        (OrbitPair.supportMulAction m (OrbitPairFull.phihatFix m s₁)
          (fun g ξ hξ => StrongKickBridge.phihatFix_support_inv m s₁ g ξ hξ))
        inferInstance : ℚ)) : ℂ)) := by
  have hlim1 := StrongKickBridge.strong_kick_limit_phihatFix m S ω s₁
    _hodd1 hs1 hω0 hωbound hωlim hSInv hSep
  have hlim2 := StrongKickBridge.strong_kick_limit_phihatFix m S ω s₂
    _hodd2 hs2 hω0 hωbound hωlim hSInv hSep
  have hbsym := bsym_phihatFix_eq_of_odd m s₁ s₂ hs1 hs2 _hodd1 _hodd2
  refine ⟨hlim1, ?_⟩
  rw [← hbsym] at hlim2
  exact hlim2

/-! ### §4. G-ensemble assembly: the complex pair sum as a doubled real pair sum -/

/-- The concrete mode sums in `PsiPair` argument order. -/
noncomputable def modeSumF (m : ℕ) [NeZero m] (ξ : OrbitPair.Fix m)
    (k : ℤ) : ℂ :=
  modeSum m k ξ

/-- Γ-invariance of `modeSumF` (from `modeSum_smul`). -/
theorem modeSumF_smul (m : ℕ) [NeZero m]
    (g : DihedralGroup m) (ξ : OrbitPair.Fix m) (k : ℤ) :
    modeSumF m (g • ξ) k = modeSumF m ξ k :=
  modeSum_smul m k g ξ

/-- The G-ensemble factor on complex arguments: the source's
    `exp (-a^2 |z|^2 / 4)`, with `|z| = ‖z‖`. -/
noncomputable def gaussOmegaC {K : Type*} (a : K → ℝ) (k : K) (z : ℂ) : ℂ :=
  Complex.exp (((-(a k) ^ 2 * ‖z‖ ^ 2 / 4 : ℝ) : ℂ))

/-- Doubled real mode values from complex mode sums: real part on
    `true`, imaginary part on `false`. -/
noncomputable def doubledMode {m : ℕ} [NeZero m] {K : Type*}
    (S : OrbitPair.Fix m → K → ℂ) (ξ : OrbitPair.Fix m) : K × Bool → ℝ
  | (k, true) => (S ξ k).re
  | (k, false) => (S ξ k).im

/-- The G-ensemble complex pair sum equals the doubled real pair
    sum: `exp (-a^2 |Δ|^2 / 4)` splits over real and imaginary parts
    (this is why the Gaussian case, unlike J0, fits the block's real
    `PsiPair` exactly). -/
theorem psiPairC_gauss_eq {m : ℕ} [NeZero m] {K : Type*} [Fintype K]
    (φ : ℤ → OrbitPair.Fix m → ℂ) (S : OrbitPair.Fix m → K → ℂ)
    (a : K → ℝ) (η : ℝ) (s : ℤ) :
    OrbitPairFull.PsiPairC m φ S (gaussOmegaC a) ((η : ℝ) : ℂ) s
      = OrbitPair.PsiPair m φ (doubledMode S) (fun p => gaussOmega a p.1)
        η s := by
  unfold OrbitPairFull.PsiPairC OrbitPair.PsiPair
  apply Finset.sum_congr rfl; intro ξ _
  apply Finset.sum_congr rfl; intro ξ' _
  congr 1
  rw [Fintype.prod_prod_type]
  apply Finset.prod_congr rfl; intro k _
  rw [Fintype.prod_bool]
  dsimp only
  have hre : doubledMode S ξ (k, true) - doubledMode S ξ' (k, true)
      = (S ξ k - S ξ' k).re := by
    simp [doubledMode, Complex.sub_re]
  have him : doubledMode S ξ (k, false) - doubledMode S ξ' (k, false)
      = (S ξ k - S ξ' k).im := by
    simp [doubledMode, Complex.sub_im]
  rw [hre, him]
  unfold gaussOmegaC gaussOmega
  rw [← Complex.exp_add, ← Complex.ofReal_add]
  congr 1
  have hnorm : ‖((η : ℝ) : ℂ) * (S ξ k - S ξ' k)‖ ^ 2
      = η ^ 2 * ((S ξ k - S ξ' k).re ^ 2 + (S ξ k - S ξ' k).im ^ 2) := by
    rw [norm_mul, Complex.norm_real, mul_pow, Real.norm_eq_abs, sq_abs,
      ← Complex.normSq_eq_norm_sq, Complex.normSq_apply]
    ring
  rw [hnorm]
  ring

/-- The concrete mode sums restricted to a finite mode set `𝒦`
    (the source's `𝒦` is finite; the block's `PsiPair` needs
    `Fintype K`, so the subtype `{k // k ∈ 𝒦}` is the faithful
    formalization, not all of `ℤ`). -/
noncomputable def modeSumK (m : ℕ) [NeZero m] (𝒦 : Finset ℤ)
    (ξ : OrbitPair.Fix m) (k : {k // k ∈ 𝒦}) : ℂ :=
  modeSumF m ξ k.1

/-- Γ-invariance of `modeSumK` (from `modeSumF_smul`). -/
theorem modeSumK_smul (m : ℕ) [NeZero m] (𝒦 : Finset ℤ)
    (g : DihedralGroup m) (ξ : OrbitPair.Fix m) (k : {k // k ∈ 𝒦}) :
    modeSumK m 𝒦 (g • ξ) k = modeSumK m 𝒦 ξ k :=
  modeSumF_smul m g ξ k.1

/-- The strong-kick limit for the G ensemble with the concrete mode
    sums over a finite mode set `𝒦`: everything except complex
    separation (`hSepC`) is discharged — the Gaussian factor by §1,
    Γ-invariance of the modes by §2, and the complex/real pair-sum
    identification by the doubled-modes identity above. -/
theorem strong_kick_limit_gaussC (m : ℕ) [NeZero m] (𝒦 : Finset ℤ)
    (a : ℤ → ℝ) (ha : ∀ k ∈ 𝒦, a k ≠ 0) (s : ℤ)
    (_hodd : Odd s) (hs : IsCoprime s (Defs.Dm m))
    (hSepC : ∀ (ξ ξ' : OrbitPair.Fix m),
      (∀ k : {k // k ∈ 𝒦}, modeSumK m 𝒦 ξ k = modeSumK m 𝒦 ξ' k) →
        ξ' ∈ Parity.orbitFinset (DihedralGroup m) ξ) :
    Tendsto (fun η : ℝ => OrbitPairFull.PsiPairC m (OrbitPairFull.phihatFix m)
        (modeSumK m 𝒦) (gaussOmegaC (fun k : {k // k ∈ 𝒦} => a k.1))
        ((η : ℝ) : ℂ) s)
      atTop
      (𝓝 (((@Parity.Bsym (DihedralGroup m)
        ↥(OrbitPair.support m (OrbitPairFull.phihatFix m s))
        inferInstance
        (OrbitPair.supportMulAction m (OrbitPairFull.phihatFix m s)
          (fun g ξ hξ => StrongKickBridge.phihatFix_support_inv m s g ξ hξ))
        inferInstance : ℚ)) : ℂ)) := by
  have ha𝒦 : ∀ k : {k // k ∈ 𝒦}, (fun k => a k.1) k ≠ 0 :=
    fun k => ha k.1 k.2
  have hSInvD : ∀ (g : DihedralGroup m) (ξ : OrbitPair.Fix m)
      (p : {k // k ∈ 𝒦} × Bool),
      doubledMode (modeSumK m 𝒦) (g • ξ) p
        = doubledMode (modeSumK m 𝒦) ξ p := by
    intro g ξ ⟨k, b⟩
    cases b <;> simp [doubledMode, modeSumK_smul]
  have hSepD : ∀ (ξ ξ' : OrbitPair.Fix m),
      (∀ p, doubledMode (modeSumK m 𝒦) ξ p
          = doubledMode (modeSumK m 𝒦) ξ' p) →
        ξ' ∈ Parity.orbitFinset (DihedralGroup m) ξ := by
    intro ξ ξ' h
    apply hSepC
    intro k
    apply Complex.ext
    · have h1 := h (k, true)
      simpa [doubledMode] using h1
    · have h2 := h (k, false)
      simpa [doubledMode] using h2
  have hlim := StrongKickBridge.strong_kick_limit_phihatFix m
    (doubledMode (modeSumK m 𝒦))
    (fun p => gaussOmega (fun k : {k // k ∈ 𝒦} => a k.1) p.1) s _hodd hs
    (fun p => gaussOmega_zero _ p.1) (fun p => gaussOmega_bound _ p.1)
    (fun p Δ hΔ => gaussOmega_lim _ ha𝒦 p.1 Δ hΔ)
    hSInvD hSepD
  exact Filter.Tendsto.congr
    (fun η => (psiPairC_gauss_eq (OrbitPairFull.phihatFix m) (modeSumK m 𝒦)
      (fun k : {k // k ∈ 𝒦} => a k.1) η s).symm) hlim

/- Axiom audit for all main theorems of this module. -/
#print axioms StrongKickConc.gaussOmega_zero
#print axioms StrongKickConc.gaussOmega_norm
#print axioms StrongKickConc.gaussOmega_bound
#print axioms StrongKickConc.tendsto_sq_atTop
#print axioms StrongKickConc.gaussOmega_lim
#print axioms StrongKickConc.strong_kick_limit_gauss
#print axioms StrongKickConc.modeSum_smul
#print axioms StrongKickConc.phihatFix_support_eq_of_odd
#print axioms StrongKickConc.bsym_phihatFix_eq_of_odd
#print axioms StrongKickConc.strong_kick_limit_eq_of_odd
#print axioms StrongKickConc.modeSumF_smul
#print axioms StrongKickConc.modeSumK_smul
#print axioms StrongKickConc.psiPairC_gauss_eq
#print axioms StrongKickConc.strong_kick_limit_gaussC

end StrongKickConc
end LineD
end Bgs
