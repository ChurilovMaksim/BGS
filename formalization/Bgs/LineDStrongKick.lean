/-
  Bgs/LineDStrongKick.lean — strong-kick limit for TRACE-152.

  TEST COPY ONLY — not pushed to the repository, registry untouched,
  `Bgs.lean` aggregator unchanged (this module is built by a direct
  `lake env lean` call, not imported by the aggregator).

  Boundary (BGS-TRACE-152, proved; source
  mathematics/fixed-map/band_limited_kick_bridge.md; dependency
  BGS-TRACE-151), verbatim from `record/claims.json` (base 347f):

  > If a_k != 0 for k in K and P_K(xi) = (S_k(xi))_{k in K} separates
  > dihedral (Gamma) classes on the support, then lim_{eta->inf}
  > Psi_m(t*) = B_m^sym = D_eff^{-1} sum_{supp}|Gamma xi| for every
  > residue. Iterated limit (N -> infinity first). Quenched-ensemble
  > analogue of Line B Theorem 4. At finite eta Psi_m(t*) is residue
  > dependent and takes values in a range containing 2m; the COE value
  > 2m is not obtained at any fixed m. Does not prove BGS-TRACE-005 or
  > BGS-BGS-001; says nothing about eigenvalue statistics beyond the
  > second moment of Tr U^m at fixed m.

  What is built here, from the 151 block (LineDDefs / LineDOrbitPair /
  LineDParity, copied unchanged):

  * `psiPair_eq_onOrbit_add_offOrbit` — the exact split of the 151
    pair sum into the Gamma-orbit part and the off-orbit part.
  * `onOrbit_eq` — the orbit part evaluates, under Gamma-invariance
    of the mode values and of the weights on the support, to
    `c * sum_{support} |Gamma xi|`, with `c` the common value of
    `phi * star phi` on the support (the 151 value `|V[4]| / D_m`).
  * `offOrbit_tendsto_zero` — the off-orbit part tends to 0 as
    `eta -> infinity`, under P_K-separation (off-orbit pairs differ
    in some mode value) and decay of the Kluyver/Gaussian factor at
    large argument. This is the analytic heart of 152.
  * `strong_kick_limit` — `lim_{eta->inf} Psi_m = B_m^sym` (as the
    cast of `Parity.Bsym` over the phi-support subtype), for every
    residue `s`, under the normalisation `c * D_eff = 1`.
  * `psiPair_eq_bsym_add_offOrbit` — the exact finite-eta remainder:
    `Psi_m(eta) - B_m^sym` IS the off-orbit sum (an identity, not an
    estimate; the estimate is the limit theorem above).
  * `strong_kick_limit_iterated` — the iterated limit in honest
    epsilon form: first `N -> infinity` (hypothesis `hN`: an
    N-family tending to the pair sum at each fixed `eta`), then
    `eta -> infinity` (the limit theorem above).

  What is deliberately NOT claimed (explicit hypotheses `h...`,
  never invented lemmas, never postulates):

  * The Gamma-action on `Fix_m`, its generators, and the mode values
    `S_k` — parameters; `hSInv` (mode values Gamma-invariant) and
    `hSep` (P_K separates Gamma classes) are hypotheses. The 151
    boundary does not spell out the generators, so none are invented.
  * The weights `phihat_s`, their Gamma-invariance on the support
    (`hφinv`), the common square value `c` on the support (`hSq`),
    and the support's Gamma-invariance (`hInv`) — the 151 content
    (Line B Prop R), kept as hypotheses.
  * `card (support) = D_eff` (`hDeff`) and the normalisation
    `c * D_eff = 1` (`hNorm`) — the 151 table content; in particular
    the `m = 7` row (`Deff 7 = 57121`) is NOT re-proved here: kernel
    `decide` for `m = 7` is OOM-killed (exit 137) on this VM, see the
    151+149 report. The support card is a parameter `D`, not a
    `decide` table.
  * The `N -> infinity` step itself (`hN`): it needs continuity of
    `Psi_m` in `t` (C^infinity, analytic infrastructure absent from
    the graph) and the 149 bridge at `t_N -> t*`; it is a hypothesis
    of the iterated-limit theorem only, never asserted.
  * The COE value `2m` at fixed `m` is NOT asserted (the boundary
    explicitly denies it); `B_m^sym < 2m` is the 154 content, proved
    in LineDParity and bridged in LineDOrbitPair, not re-proved here.
  * Nothing here proves BGS-TRACE-005 or BGS-BGS-001.

  No `sorry`, no `admit`, no `axiom`, no `native_decide`, no `decide`
  in this file. `#print axioms` for the main theorems is at the end.
-/

import Bgs.LineDOrbitPair
import Mathlib.Topology.Algebra.Monoid
import Mathlib.Analysis.Normed.Group.Continuity
import Mathlib.Analysis.Normed.Ring.Basic
import Mathlib.Topology.Order.Basic
import Mathlib.Analysis.Complex.Basic
import Mathlib.Data.Fintype.BigOperators

namespace Bgs
namespace LineD
namespace StrongKick

open Bgs.LineD
open Finset Filter Topology

/-- The pair-sum term of 151, as a function of `eta`, for fixed
    residues and mode values. This is the summand of `PsiPair`,
    unfolded so the limit arguments can rewrite it. -/
noncomputable def pairTerm (m : ℕ) [NeZero m] {K : Type*} [Fintype K]
    (φ : ℤ → OrbitPair.Fix m → ℂ) (S : OrbitPair.Fix m → K → ℝ)
    (ω : K → ℝ → ℂ) (s : ℤ)
    (ξ ξ' : OrbitPair.Fix m) (η : ℝ) : ℂ :=
  φ s ξ * star (φ s ξ') * ∏ k, ω k (η * (S ξ k - S ξ' k))

/-- The Gamma-orbit part of the pair sum at parameter `eta`. -/
noncomputable def onOrbitSum (m : ℕ) [NeZero m] {K : Type*} [Fintype K]
    (G : Type*) [Group G] [MulAction G (OrbitPair.Fix m)]
    (φ : ℤ → OrbitPair.Fix m → ℂ) (S : OrbitPair.Fix m → K → ℝ)
    (ω : K → ℝ → ℂ) (s : ℤ) (η : ℝ) : ℂ :=
  ∑ ξ : OrbitPair.Fix m, ∑ ξ' ∈ Parity.orbitFinset G ξ,
    pairTerm m φ S ω s ξ ξ' η

/-- The off-Gamma-orbit part of the pair sum at parameter `eta`. -/
noncomputable def offOrbitSum (m : ℕ) [NeZero m] {K : Type*} [Fintype K]
    (G : Type*) [Group G] [MulAction G (OrbitPair.Fix m)]
    (φ : ℤ → OrbitPair.Fix m → ℂ) (S : OrbitPair.Fix m → K → ℝ)
    (ω : K → ℝ → ℂ) (s : ℤ) (η : ℝ) : ℂ :=
  ∑ ξ : OrbitPair.Fix m, ∑ ξ' ∈ (Parity.orbitFinset G ξ)ᶜ,
    pairTerm m φ S ω s ξ ξ' η

/-- Membership in the phi-support, unfolded: `xi` is in the support
    exactly when its weight is nonzero. -/
theorem mem_support_iff (m : ℕ) [NeZero m] (φ : OrbitPair.Fix m → ℂ)
    (ξ : OrbitPair.Fix m) :
    ξ ∈ OrbitPair.support m φ ↔ φ ξ ≠ 0 := by
  simp [OrbitPair.support]

/-- Exact split of the 151 pair sum into its Gamma-orbit part and its
    off-orbit part. No hypotheses: this is `sum_add_sum_compl` applied
    to every inner sum. -/
theorem psiPair_eq_onOrbit_add_offOrbit (m : ℕ) [NeZero m]
    {K : Type*} [Fintype K]
    (G : Type*) [Group G] [MulAction G (OrbitPair.Fix m)]
    (φ : ℤ → OrbitPair.Fix m → ℂ) (S : OrbitPair.Fix m → K → ℝ)
    (ω : K → ℝ → ℂ) (s : ℤ) (η : ℝ) :
    OrbitPair.PsiPair m φ S ω η s
      = onOrbitSum m G φ S ω s η + offOrbitSum m G φ S ω s η := by
  classical
  unfold OrbitPair.PsiPair onOrbitSum offOrbitSum pairTerm
  rw [← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro ξ _
  exact (Finset.sum_add_sum_compl (Parity.orbitFinset G ξ) _).symm

/-- Orbit size in the phi-support subtype equals orbit size in the
    ambient `Fix_m`, for a support point: the ambient orbit of a
    support point stays inside the support (`hInv`), and the subtype
    action agrees with the ambient action (`hAct`). -/
theorem orbitFinset_card_subtype (m : ℕ) [NeZero m]
    (G : Type*) [Group G] [MulAction G (OrbitPair.Fix m)]
    (φ : OrbitPair.Fix m → ℂ)
    (hInv : ∀ (g : G) (ξ : OrbitPair.Fix m),
      ξ ∈ OrbitPair.support m φ → g • ξ ∈ OrbitPair.support m φ)
    [MulAction G ↥(OrbitPair.support m φ)]
    (hAct : ∀ (g : G) (x : ↥(OrbitPair.support m φ)),
      (g • x).1 = g • x.1)
    (x : ↥(OrbitPair.support m φ)) :
    (Parity.orbitFinset G x).card = (Parity.orbitFinset G x.1).card := by
  apply Finset.card_bij (fun y _ => y.1)
  · intro y hy
    simp only [Parity.orbitFinset, Finset.mem_filter, Finset.mem_univ,
      true_and] at hy ⊢
    obtain ⟨g, hg⟩ := MulAction.mem_orbit_iff.mp hy
    exact MulAction.mem_orbit_iff.mpr ⟨g, by rw [← hg]; exact (hAct g x).symm⟩
  · intro a _ b _ h
    exact Subtype.ext h
  · intro z hz
    simp only [Parity.orbitFinset, Finset.mem_filter, Finset.mem_univ,
      true_and] at hz
    obtain ⟨g, hg⟩ := MulAction.mem_orbit_iff.mp hz
    have hzs : z ∈ OrbitPair.support m φ := by
      rw [← hg]
      exact hInv g x.1 x.2
    refine ⟨⟨z, hzs⟩, ?_, rfl⟩
    simp only [Parity.orbitFinset, Finset.mem_filter, Finset.mem_univ,
      true_and]
    exact MulAction.mem_orbit_iff.mpr
      ⟨g, Subtype.ext (by rw [hAct]; exact hg)⟩

/-- The Gamma-orbit part evaluates to `c * sum_{support} |Gamma xi|`,
    under Gamma-invariance of the mode values (`hSInv`), of the
    weights on the support (`hφinv`), and the common square value
    `c` on the support (`hSq`). The diagonal `xi' = xi` is included:
    every point lies in its own orbit. -/
theorem onOrbit_eq (m : ℕ) [NeZero m] {K : Type*} [Fintype K]
    (G : Type*) [Group G] [MulAction G (OrbitPair.Fix m)]
    (φ : ℤ → OrbitPair.Fix m → ℂ) (S : OrbitPair.Fix m → K → ℝ)
    (ω : K → ℝ → ℂ) (s : ℤ) (η : ℝ) (c : ℂ)
    (hω0 : ∀ k, ω k 0 = 1)
    (hSInv : ∀ (g : G) (ξ : OrbitPair.Fix m) (k : K),
      S (g • ξ) k = S ξ k)
    (hφinv : ∀ (g : G) (ξ : OrbitPair.Fix m),
      ξ ∈ OrbitPair.support m (φ s) → φ s (g • ξ) = φ s ξ)
    (hSq : ∀ ξ ∈ OrbitPair.support m (φ s),
      φ s ξ * star (φ s ξ) = c) :
    onOrbitSum m G φ S ω s η
      = c * ∑ ξ ∈ OrbitPair.support m (φ s),
          ((Parity.orbitFinset G ξ).card : ℂ) := by
  classical
  have hterm : ∀ ξ : OrbitPair.Fix m, ∀ ξ' ∈ Parity.orbitFinset G ξ,
      pairTerm m φ S ω s ξ ξ' η = φ s ξ * star (φ s ξ') := by
    intro ξ ξ' hξ'
    simp only [Parity.orbitFinset, Finset.mem_filter, Finset.mem_univ,
      true_and] at hξ'
    obtain ⟨g, hg⟩ := MulAction.mem_orbit_iff.mp hξ'
    unfold pairTerm
    have hprod : ∏ k, ω k (η * (S ξ k - S ξ' k)) = 1 := by
      apply Finset.prod_eq_one
      intro k _
      rw [← hg, hSInv]
      simp [hω0]
    rw [hprod, mul_one]
  have hinner1 : ∀ ξ ∈ OrbitPair.support m (φ s),
      (∑ ξ' ∈ Parity.orbitFinset G ξ, pairTerm m φ S ω s ξ ξ' η)
        = c * ((Parity.orbitFinset G ξ).card : ℂ) := by
    intro ξ hξ
    have hsum : (∑ ξ' ∈ Parity.orbitFinset G ξ,
          pairTerm m φ S ω s ξ ξ' η)
        = φ s ξ * ∑ ξ' ∈ Parity.orbitFinset G ξ, star (φ s ξ') := by
      rw [Finset.mul_sum]
      exact Finset.sum_congr rfl (fun ξ' hξ' => hterm ξ ξ' hξ')
    have hstar : (∑ ξ' ∈ Parity.orbitFinset G ξ, star (φ s ξ'))
        = ((Parity.orbitFinset G ξ).card : ℂ) * star (φ s ξ) := by
      have h1 : (∑ ξ' ∈ Parity.orbitFinset G ξ, star (φ s ξ'))
          = ∑ ξ' ∈ Parity.orbitFinset G ξ, star (φ s ξ) := by
        apply Finset.sum_congr rfl
        intro ξ' hξ'
        simp only [Parity.orbitFinset, Finset.mem_filter,
          Finset.mem_univ, true_and] at hξ'
        obtain ⟨g, hg⟩ := MulAction.mem_orbit_iff.mp hξ'
        rw [← hg, hφinv g ξ hξ]
      rw [h1, Finset.sum_const, nsmul_eq_mul]
    rw [hsum, hstar]
    calc φ s ξ * (((Parity.orbitFinset G ξ).card : ℂ) * star (φ s ξ))
        = (φ s ξ * star (φ s ξ)) * ((Parity.orbitFinset G ξ).card : ℂ) := by
          ring
      _ = c * ((Parity.orbitFinset G ξ).card : ℂ) := by rw [hSq ξ hξ]
  have hinner0 : ∀ ξ : OrbitPair.Fix m,
      ξ ∉ OrbitPair.support m (φ s) →
      (∑ ξ' ∈ Parity.orbitFinset G ξ, pairTerm m φ S ω s ξ ξ' η) = 0 := by
    intro ξ hξ
    apply Finset.sum_eq_zero
    intro ξ' _
    have hφ0 : φ s ξ = 0 := by
      by_contra hne
      exact hξ ((mem_support_iff m (φ s) ξ).mpr hne)
    unfold pairTerm
    rw [hφ0]
    simp
  unfold onOrbitSum
  rw [← Finset.sum_subset (Finset.subset_univ (OrbitPair.support m (φ s)))
    (fun ξ _ hξ => hinner0 ξ hξ)]
  rw [Finset.sum_congr rfl (fun ξ hξ => hinner1 ξ hξ)]
  rw [← Finset.mul_sum]

/-- One off-orbit pair term tends to 0 as `eta -> infinity`: some
    mode value differs (`hSep`, contrapositive), so one Kluyver /
    Gaussian factor tends to 0 (`hωlim`) while all other factors are
    bounded (`hωbound`). -/
theorem pairTerm_tendsto_zero (m : ℕ) [NeZero m] {K : Type*} [Fintype K]
    (G : Type*) [Group G] [MulAction G (OrbitPair.Fix m)]
    (φ : ℤ → OrbitPair.Fix m → ℂ) (S : OrbitPair.Fix m → K → ℝ)
    (ω : K → ℝ → ℂ) (s : ℤ)
    (hωbound : ∀ k (z : ℝ), ‖ω k z‖ ≤ 1)
    (hωlim : ∀ (k : K) (Δ : ℝ), Δ ≠ 0 →
      Tendsto (fun η : ℝ => ω k (η * Δ)) atTop (𝓝 0))
    (hSep : ∀ (ξ ξ' : OrbitPair.Fix m),
      (∀ k, S ξ k = S ξ' k) → ξ' ∈ Parity.orbitFinset G ξ)
    (ξ ξ' : OrbitPair.Fix m) (hξ' : ξ' ∉ Parity.orbitFinset G ξ) :
    Tendsto (fun η : ℝ => pairTerm m φ S ω s ξ ξ' η) atTop (𝓝 0) := by
  classical
  obtain ⟨k₀, hk₀⟩ : ∃ k, S ξ k ≠ S ξ' k := by
    by_contra hcon
    apply hξ'
    apply hSep
    intro k
    by_contra hne
    exact hcon ⟨k, hne⟩
  set Δ : K → ℝ := fun k => S ξ k - S ξ' k with hΔ
  have hΔ0 : Δ k₀ ≠ 0 := sub_ne_zero.mpr hk₀
  have hprod : ∀ η : ℝ, ∏ k, ω k (η * Δ k)
      = ω k₀ (η * Δ k₀) * ∏ k ∈ Finset.univ.erase k₀, ω k (η * Δ k) := by
    intro η
    exact (Finset.mul_prod_erase Finset.univ _ (Finset.mem_univ k₀)).symm
  have hrest : ∀ η : ℝ,
      ‖∏ k ∈ Finset.univ.erase k₀, ω k (η * Δ k)‖ ≤ 1 := by
    intro η
    rw [norm_prod]
    exact Finset.prod_le_one (fun k _ => norm_nonneg _)
      (fun k _ => hωbound k _)
  have hbound : ∀ η : ℝ,
      ‖pairTerm m φ S ω s ξ ξ' η‖
        ≤ ‖φ s ξ‖ * ‖φ s ξ'‖ * ‖ω k₀ (η * Δ k₀)‖ := by
    intro η
    have hstar : ‖star (φ s ξ')‖ = ‖φ s ξ'‖ := by simp
    unfold pairTerm
    rw [hprod η]
    calc ‖φ s ξ * star (φ s ξ') * (ω k₀ (η * Δ k₀)
            * ∏ k ∈ Finset.univ.erase k₀, ω k (η * Δ k))‖
        ≤ ‖φ s ξ * star (φ s ξ')‖
            * ‖ω k₀ (η * Δ k₀) * ∏ k ∈ Finset.univ.erase k₀, ω k (η * Δ k)‖ :=
          norm_mul_le _ _
      _ ≤ (‖φ s ξ‖ * ‖star (φ s ξ')‖) * (‖ω k₀ (η * Δ k₀)‖ * 1) := by
          apply mul_le_mul
          · exact norm_mul_le _ _
          · exact (norm_mul_le _ _).trans
              (mul_le_mul_of_nonneg_left (hrest η) (norm_nonneg _))
          · exact norm_nonneg _
          · exact mul_nonneg (norm_nonneg _) (norm_nonneg _)
      _ = ‖φ s ξ‖ * ‖φ s ξ'‖ * ‖ω k₀ (η * Δ k₀)‖ := by
          rw [hstar, mul_one]
  have hlim : Tendsto
      (fun η : ℝ => ‖φ s ξ‖ * ‖φ s ξ'‖ * ‖ω k₀ (η * Δ k₀)‖)
      atTop (𝓝 0) := by
    have h0 := hωlim k₀ (Δ k₀) hΔ0
    have hnorm : Tendsto (fun η : ℝ => ‖ω k₀ (η * Δ k₀)‖) atTop (𝓝 0) := by
      have := h0.norm
      simpa using this
    have := hnorm.const_mul (‖φ s ξ‖ * ‖φ s ξ'‖)
    simpa using this
  exact squeeze_zero_norm hbound hlim

/-- A finite sum of functions each tending to 0 tends to 0. (The
    stock `tendsto_finsetSum` cannot unify `𝓝 0` with a sum limit,
    so the zero is first rewritten as a constant sum.) -/
theorem tendsto_finsetSum_zero {ι : Type*} {s : Finset ι} {f : ι → ℝ → ℂ}
    (hf : ∀ i ∈ s, Tendsto (f i) atTop (𝓝 0)) :
    Tendsto (fun η => ∑ i ∈ s, f i η) atTop (𝓝 0) := by
  have h0 : (0 : ℂ) = ∑ _i ∈ s, (0 : ℂ) := by simp
  rw [h0]
  exact tendsto_finsetSum s hf

/-- The off-orbit part tends to 0 as `eta -> infinity`: a finite sum
    of terms each tending to 0. -/
theorem offOrbit_tendsto_zero (m : ℕ) [NeZero m] {K : Type*} [Fintype K]
    (G : Type*) [Group G] [MulAction G (OrbitPair.Fix m)]
    (φ : ℤ → OrbitPair.Fix m → ℂ) (S : OrbitPair.Fix m → K → ℝ)
    (ω : K → ℝ → ℂ) (s : ℤ)
    (hωbound : ∀ k (z : ℝ), ‖ω k z‖ ≤ 1)
    (hωlim : ∀ (k : K) (Δ : ℝ), Δ ≠ 0 →
      Tendsto (fun η : ℝ => ω k (η * Δ)) atTop (𝓝 0))
    (hSep : ∀ (ξ ξ' : OrbitPair.Fix m),
      (∀ k, S ξ k = S ξ' k) → ξ' ∈ Parity.orbitFinset G ξ) :
    Tendsto (fun η : ℝ => offOrbitSum m G φ S ω s η) atTop (𝓝 0) := by
  classical
  unfold offOrbitSum
  apply tendsto_finsetSum_zero
  intro ξ _
  apply tendsto_finsetSum_zero
  intro ξ' hξ'
  simp only [Finset.mem_compl] at hξ'
  exact pairTerm_tendsto_zero m G φ S ω s hωbound hωlim hSep ξ ξ' hξ'

/-- The orbit-sum value equals the cast of `Parity.Bsym` over the
    phi-support subtype, under the support-card hypothesis `hDeff`
    and the normalisation `hNorm` (`c * D_eff = 1`, the 151 value
    `|V[4]| / D_m` times `D_m / |V[4]|`). -/
theorem orbitSum_eq_bsym (m : ℕ) [NeZero m]
    (G : Type*) [Group G] [MulAction G (OrbitPair.Fix m)]
    (φ : OrbitPair.Fix m → ℂ)
    (hInv : ∀ (g : G) (ξ : OrbitPair.Fix m),
      ξ ∈ OrbitPair.support m φ → g • ξ ∈ OrbitPair.support m φ)
    [MulAction G ↥(OrbitPair.support m φ)]
    (hAct : ∀ (g : G) (x : ↥(OrbitPair.support m φ)),
      (g • x).1 = g • x.1)
    (c : ℂ) (D : ℕ) (hcardPos : 0 < (OrbitPair.support m φ).card)
    (hDeff : (OrbitPair.support m φ).card = D)
    (hNorm : c * (D : ℂ) = 1) :
    c * ∑ ξ ∈ OrbitPair.support m φ,
        ((Parity.orbitFinset G ξ).card : ℂ)
      = ((Parity.Bsym G ↥(OrbitPair.support m φ) : ℚ) : ℂ) := by
  have hcard : (∑ x : ↥(OrbitPair.support m φ),
        ((Parity.orbitFinset G x).card : ℚ))
      = ∑ ξ ∈ OrbitPair.support m φ,
          ((Parity.orbitFinset G ξ).card : ℚ) := by
    rw [← Finset.sum_coe_sort (OrbitPair.support m φ)
      (fun ξ => ((Parity.orbitFinset G ξ).card : ℚ))]
    apply Finset.sum_congr rfl
    intro x _
    exact_mod_cast orbitFinset_card_subtype m G φ hInv hAct x
  have hDne : (D : ℂ) ≠ 0 := by
    have hpos : (D : ℕ) ≠ 0 := by
      rw [← hDeff]
      exact Nat.pos_iff_ne_zero.mp hcardPos
    exact_mod_cast hpos
  unfold Parity.Bsym
  rw [Fintype.card_coe, hDeff, hcard]
  push_cast
  rw [eq_div_iff hDne]
  calc c * (∑ ξ ∈ OrbitPair.support m φ,
          ((Parity.orbitFinset G ξ).card : ℂ)) * (D : ℂ)
      = (c * (D : ℂ)) * ∑ ξ ∈ OrbitPair.support m φ,
          ((Parity.orbitFinset G ξ).card : ℂ) := by ring
    _ = ∑ ξ ∈ OrbitPair.support m φ,
          ((Parity.orbitFinset G ξ).card : ℂ) := by rw [hNorm, one_mul]

/-- TRACE-152, strong-kick limit: for every residue `s`,
    `lim_{eta->inf} Psi_m = B_m^sym`, under P_K-separation, decay of
    the Kluyver/Gaussian factor, Gamma-invariance of mode values and
    weights on the support, the common square value `c` on the
    support, and the normalisation `c * D_eff = 1`. The COE value
    `2m` is NOT asserted here (the boundary denies it at fixed `m`). -/
theorem strong_kick_limit (m : ℕ) [NeZero m] {K : Type*} [Fintype K]
    (G : Type*) [Group G] [MulAction G (OrbitPair.Fix m)] [Fintype G]
    (φ : ℤ → OrbitPair.Fix m → ℂ) (S : OrbitPair.Fix m → K → ℝ)
    (ω : K → ℝ → ℂ) (s : ℤ) (c : ℂ) (D : ℕ)
    (hω0 : ∀ k, ω k 0 = 1)
    (hωbound : ∀ k (z : ℝ), ‖ω k z‖ ≤ 1)
    (hωlim : ∀ (k : K) (Δ : ℝ), Δ ≠ 0 →
      Tendsto (fun η : ℝ => ω k (η * Δ)) atTop (𝓝 0))
    (hSInv : ∀ (g : G) (ξ : OrbitPair.Fix m) (k : K),
      S (g • ξ) k = S ξ k)
    (hSep : ∀ (ξ ξ' : OrbitPair.Fix m),
      (∀ k, S ξ k = S ξ' k) → ξ' ∈ Parity.orbitFinset G ξ)
    (hφinv : ∀ (g : G) (ξ : OrbitPair.Fix m),
      ξ ∈ OrbitPair.support m (φ s) → φ s (g • ξ) = φ s ξ)
    (hSq : ∀ ξ ∈ OrbitPair.support m (φ s),
      φ s ξ * star (φ s ξ) = c)
    (hInv : ∀ (g : G) (ξ : OrbitPair.Fix m),
      ξ ∈ OrbitPair.support m (φ s) →
        g • ξ ∈ OrbitPair.support m (φ s))
    [MulAction G ↥(OrbitPair.support m (φ s))]
    (hAct : ∀ (g : G) (x : ↥(OrbitPair.support m (φ s))),
      (g • x).1 = g • x.1)
    (hcardPos : 0 < (OrbitPair.support m (φ s)).card)
    (hDeff : (OrbitPair.support m (φ s)).card = D)
    (hNorm : c * (D : ℂ) = 1) :
    Tendsto (fun η : ℝ => OrbitPair.PsiPair m φ S ω η s) atTop
      (𝓝 ((Parity.Bsym G ↥(OrbitPair.support m (φ s)) : ℚ) : ℂ)) := by
  classical
  have hsplit : ∀ η : ℝ, OrbitPair.PsiPair m φ S ω η s
      = (c * ∑ ξ ∈ OrbitPair.support m (φ s),
            ((Parity.orbitFinset G ξ).card : ℂ))
        + offOrbitSum m G φ S ω s η := by
    intro η
    rw [psiPair_eq_onOrbit_add_offOrbit m G φ S ω s η,
      onOrbit_eq m G φ S ω s η c hω0 hSInv hφinv hSq]
  have hbsym := orbitSum_eq_bsym m G (φ s) hInv hAct c D hcardPos hDeff hNorm
  have hlim : Tendsto
      (fun η : ℝ => (c * ∑ ξ ∈ OrbitPair.support m (φ s),
            ((Parity.orbitFinset G ξ).card : ℂ))
        + offOrbitSum m G φ S ω s η)
      atTop (𝓝 (((Parity.Bsym G ↥(OrbitPair.support m (φ s)) : ℚ) : ℂ))) := by
    rw [← hbsym]
    simpa using tendsto_const_nhds.add
      (offOrbit_tendsto_zero m G φ S ω s hωbound hωlim hSep)
  exact hlim.congr (fun η => (hsplit η).symm)

/-- Exact finite-eta remainder: `Psi_m(eta) - B_m^sym` IS the
    off-orbit sum. No estimate is claimed at finite `eta`; the
    estimate is the limit theorem `strong_kick_limit`. -/
theorem psiPair_eq_bsym_add_offOrbit (m : ℕ) [NeZero m]
    {K : Type*} [Fintype K]
    (G : Type*) [Group G] [MulAction G (OrbitPair.Fix m)] [Fintype G]
    (φ : ℤ → OrbitPair.Fix m → ℂ) (S : OrbitPair.Fix m → K → ℝ)
    (ω : K → ℝ → ℂ) (s : ℤ) (η : ℝ) (c : ℂ) (D : ℕ)
    (hω0 : ∀ k, ω k 0 = 1)
    (hSInv : ∀ (g : G) (ξ : OrbitPair.Fix m) (k : K),
      S (g • ξ) k = S ξ k)
    (hφinv : ∀ (g : G) (ξ : OrbitPair.Fix m),
      ξ ∈ OrbitPair.support m (φ s) → φ s (g • ξ) = φ s ξ)
    (hSq : ∀ ξ ∈ OrbitPair.support m (φ s),
      φ s ξ * star (φ s ξ) = c)
    (hInv : ∀ (g : G) (ξ : OrbitPair.Fix m),
      ξ ∈ OrbitPair.support m (φ s) →
        g • ξ ∈ OrbitPair.support m (φ s))
    [MulAction G ↥(OrbitPair.support m (φ s))]
    (hAct : ∀ (g : G) (x : ↥(OrbitPair.support m (φ s))),
      (g • x).1 = g • x.1)
    (hcardPos : 0 < (OrbitPair.support m (φ s)).card)
    (hDeff : (OrbitPair.support m (φ s)).card = D)
    (hNorm : c * (D : ℂ) = 1) :
    OrbitPair.PsiPair m φ S ω η s
      = ((Parity.Bsym G ↥(OrbitPair.support m (φ s)) : ℚ) : ℂ)
        + offOrbitSum m G φ S ω s η := by
  rw [psiPair_eq_onOrbit_add_offOrbit m G φ S ω s η,
    onOrbit_eq m G φ S ω s η c hω0 hSInv hφinv hSq,
    orbitSum_eq_bsym m G (φ s) hInv hAct c D hcardPos hDeff hNorm]

/-- Iterated limit, in honest epsilon form: first `N -> infinity`
    (hypothesis `hN`: an N-family tending to the pair sum at each
    fixed `eta` — the 149-bridge-plus-continuity step, NOT proved
    here), then `eta -> infinity` (the limit theorem above). -/
theorem strong_kick_limit_iterated (m : ℕ) [NeZero m]
    {K : Type*} [Fintype K]
    (G : Type*) [Group G] [MulAction G (OrbitPair.Fix m)] [Fintype G]
    (φ : ℤ → OrbitPair.Fix m → ℂ) (S : OrbitPair.Fix m → K → ℝ)
    (ω : K → ℝ → ℂ) (s : ℤ) (c : ℂ) (D : ℕ)
    (F : ℕ → ℝ → ℂ)
    (hω0 : ∀ k, ω k 0 = 1)
    (hωbound : ∀ k (z : ℝ), ‖ω k z‖ ≤ 1)
    (hωlim : ∀ (k : K) (Δ : ℝ), Δ ≠ 0 →
      Tendsto (fun η : ℝ => ω k (η * Δ)) atTop (𝓝 0))
    (hSInv : ∀ (g : G) (ξ : OrbitPair.Fix m) (k : K),
      S (g • ξ) k = S ξ k)
    (hSep : ∀ (ξ ξ' : OrbitPair.Fix m),
      (∀ k, S ξ k = S ξ' k) → ξ' ∈ Parity.orbitFinset G ξ)
    (hφinv : ∀ (g : G) (ξ : OrbitPair.Fix m),
      ξ ∈ OrbitPair.support m (φ s) → φ s (g • ξ) = φ s ξ)
    (hSq : ∀ ξ ∈ OrbitPair.support m (φ s),
      φ s ξ * star (φ s ξ) = c)
    (hInv : ∀ (g : G) (ξ : OrbitPair.Fix m),
      ξ ∈ OrbitPair.support m (φ s) →
        g • ξ ∈ OrbitPair.support m (φ s))
    [MulAction G ↥(OrbitPair.support m (φ s))]
    (hAct : ∀ (g : G) (x : ↥(OrbitPair.support m (φ s))),
      (g • x).1 = g • x.1)
    (hcardPos : 0 < (OrbitPair.support m (φ s)).card)
    (hDeff : (OrbitPair.support m (φ s)).card = D)
    (hNorm : c * (D : ℂ) = 1)
    (hN : ∀ η : ℝ, Tendsto (fun N => F N η) atTop
      (𝓝 (OrbitPair.PsiPair m φ S ω η s))) :
    ∀ ε > 0, ∃ η₀ : ℝ, ∀ η ≥ η₀, ∃ N₀ : ℕ, ∀ N ≥ N₀,
      ‖F N η - ((Parity.Bsym G ↥(OrbitPair.support m (φ s)) : ℚ) : ℂ)‖
        < ε := by
  classical
  have hlim := strong_kick_limit m G φ S ω s c D hω0 hωbound hωlim hSInv
    hSep hφinv hSq hInv hAct hcardPos hDeff hNorm
  intro ε hε
  have hε2 : (0:ℝ) < ε / 2 := by linarith
  obtain ⟨η₀, hη₀⟩ := (Metric.tendsto_atTop.mp hlim) (ε / 2) hε2
  refine ⟨η₀, fun η hη => ?_⟩
  obtain ⟨N₀, hN₀⟩ := (Metric.tendsto_atTop.mp (hN η)) (ε / 2) hε2
  refine ⟨N₀, fun N hN => ?_⟩
  have h1 := hN₀ N hN
  have h2 := hη₀ η hη
  rw [dist_eq_norm] at h1 h2
  calc ‖F N η - ((Parity.Bsym G ↥(OrbitPair.support m (φ s)) : ℚ) : ℂ)‖
      = ‖(F N η - OrbitPair.PsiPair m φ S ω η s)
        + (OrbitPair.PsiPair m φ S ω η s
          - ((Parity.Bsym G ↥(OrbitPair.support m (φ s)) : ℚ) : ℂ))‖ := by
        congr 1
        abel
    _ ≤ ‖F N η - OrbitPair.PsiPair m φ S ω η s‖
        + ‖OrbitPair.PsiPair m φ S ω η s
          - ((Parity.Bsym G ↥(OrbitPair.support m (φ s)) : ℚ) : ℂ)‖ :=
        norm_add_le _ _
    _ < ε / 2 + ε / 2 := by
        exact add_lt_add h1 h2
    _ = ε := by ring

#print axioms tendsto_finsetSum_zero
#print axioms mem_support_iff
#print axioms psiPair_eq_onOrbit_add_offOrbit
#print axioms orbitFinset_card_subtype
#print axioms onOrbit_eq
#print axioms pairTerm_tendsto_zero
#print axioms offOrbit_tendsto_zero
#print axioms orbitSum_eq_bsym
#print axioms strong_kick_limit
#print axioms psiPair_eq_bsym_add_offOrbit
#print axioms strong_kick_limit_iterated

end StrongKick
end LineD
end Bgs
