/-! BREAKTHROUGH DRAFT — research record, not a theorem.
    Source: BGS breakthrough program (Nov 2026), wave notes in evidence/breakthrough/methods/.
    Status: draft; built counterpart LemmaYM3Fixed.lean (861 s, 0 errors, 6 sorry).
    Not imported by formalization/Bgs.lean. Registry status unchanged. -/

/-! DRAFT ONLY — NOT A PROOF, NOT FOR MAIN. Wave 17, task 4: third Lean
milestone draft for the Lemma Y chain (roadmap wave14_Lean_roadmap_LemmaY.md):
Stage 6 (Lemma S, π₂ = π₃ compatibility) + Stage 7 (mod-D assembly).
`lake build` was NOT run, no repository file touched, nothing pushed to
`main`. Every `sorry` is a placeholder; do not cite as proved, do not
enter `main` until every `sorry` is replaced and `sorryAx = 0`.
Self-contained in namespace `LemmaYM3` (milestone-1/2 defs restated).
No NEW main definition is used: `pellX`, `pellY`, `Dm`, `gp` are imported
from `Bgs.LineB.Derand` as in milestones 1–2 (GitHub connector only:
`ChurilovMaksim/BGS`, `main`, HEAD `d87dce0…`, `LineBDerand.lean` blob
`01fa6e63…`, unchanged). Mathlib API: VERIFIED (waves 6/10) — flat
Derand import, primeFactors form, `Finset.sum_fiberwise_of_maps_to`;
UNCHECKED — `Finset.sum` over `Multiset` values, `Fin`/`Multiset`
notation as in milestones 1–2, two-modulus bookkeeping in T6.3.
OUT of scope: exact Pcarry, G1 at f ≥ 3, general Lemma PC, G4b, 152,
BGS-BGS-001, TRACE-005, hEquidistUnits, RMT statistics. -/
import Bgs.LineBDerand
namespace Bgs.Breakthrough.LemmaYM3
open Bgs.LineB.Derand
/-- Recurrence sequence with initial values `a, b` over `ZMod q`. -/
def seqFrom {q : Nat} (a b : ZMod q) : ℕ → ZMod q
  | 0 => a | 1 => b | n + 2 => 6 * seqFrom a b (n + 1) - seqFrom a b n
/-- `Fix_m mod q`: a recurrence sequence that is `m`-periodic. -/
def IsFix {q : Nat} (m : Nat) (y : ℕ → ZMod q) : Prop :=
  ∃ a b : ZMod q, y = seqFrom a b ∧ ∀ i, y (i + m) = y i
/-- Class sums `Y_r(y)` over `range m`, class `i ≡ r (mod t)`. -/
def classSum {q : Nat} (m t : Nat) (y : ℕ → ZMod q) (r : ℕ) : ZMod q :=
  ∑ i ∈ (Finset.range m).filter (fun i => i % t = r), y i
/-- Global multiset of a sequence over one period. -/
def seqMultiset {q : Nat} (m : Nat) (y : ℕ → ZMod q) : Multiset (ZMod q) :=
  Multiset.ofList ((List.range m).map y)
/-- Per-class multiset `M_r` over one period, class `i ≡ r (mod 4)`. -/
def perClassMultiset {q : Nat} (m : Nat) (y : ℕ → ZMod q) (r : ℕ) :
    Multiset (ZMod q) :=
  Multiset.ofList (((List.range m).filter (fun i => i % 4 = r)).map y)
/-- Dihedral permutation of `t` classes. -/
def IsDihedral {t : Nat} (π : Fin t → Fin t) : Prop :=
  ∃ b : Fin t, (∀ r, π r = r + b) ∨ (∀ r, π r = -r + b)
/-- `δ` stabilises the per-class multisets of `p`. -/
def StabM {q : Nat} (m : Nat) (p : ℕ → ZMod q) (δ : Fin 4 → Fin 4) : Prop :=
  ∀ r, perClassMultiset m p (δ r).val = perClassMultiset m p r
/-! ## Stage 6 — Lemma S and compatibility (4 ∣ m; P = 2^L, a = 2L+3) -/
/-- T6.1 (pair lemma PL). For a pattern `p ∈ Fix_P mod 2^a`, equal
pair-unions imply equal pair-profiles: if `M_r + M_s = M_{r'} + M_{s'}`
for distinct classes, then `{M_r, M_s} = {M_{r'}, M_{s'}}` (wave 12
lemmaS §1; induction on level `t` via milestone-2 T5.2, cases A/B/C).
PL is FALSE for arbitrary multisets (wave-11 §5 counterexample); the
segment structure (cases A/B/C) is the Fix input. The naive
"first-half top bits constant per class" sub-claim is FALSE and is
not used: δ = 1 classes give both lifts, case B scales, case C
splits mod 16. -/
theorem pair_lemma {L : Nat} (hL : 2 ≤ L)
    (p : ℕ → ZMod (2 ^ (2 * L + 3))) (hfix : IsFix (2 ^ L) p)
    {r s r' s' : ℕ} (hrs : r ≠ s) (hr's' : r' ≠ s')
    (hunion : perClassMultiset (2 ^ L) p r + perClassMultiset (2 ^ L) p s =
      perClassMultiset (2 ^ L) p r' + perClassMultiset (2 ^ L) p s') :
    (perClassMultiset (2 ^ L) p r = perClassMultiset (2 ^ L) p r' ∧
      perClassMultiset (2 ^ L) p s = perClassMultiset (2 ^ L) p s') ∨
    (perClassMultiset (2 ^ L) p r = perClassMultiset (2 ^ L) p s' ∧
      perClassMultiset (2 ^ L) p s = perClassMultiset (2 ^ L) p r') := by
  sorry
/-- T6.2 (Lemma S, stabiliser adjustment). If `γ ∈ D₄` satisfies the
union equalities `(*)` over every `v`-fiber block
(`v = (a, b, -a, -b)` mod 3), then some `δ ∈ Stab(M)` maps every
`γ(F_a)` back to `F_a` (stated as: `δ ∘ γ` preserves each fiber
block; set equality follows by finiteness). Proof (wave 12 lemmaS
§§2–3): T6.1 gives profile preservation for pair blocks, then finite
`D₄` case analysis on the three block shapes (size 4; opposite pair
+ two singletons; two adjacent pairs), with explicit `δ` per case. -/
theorem lemmaS {L : Nat} (hL : 2 ≤ L)
    (p : ℕ → ZMod (2 ^ (2 * L + 3))) (hfix : IsFix (2 ^ L) p)
    (v : Fin 4 → ZMod 3) (hv2 : v 2 = -v 0) (hv3 : v 3 = -v 1)
    (γ : Fin 4 → Fin 4) (hγ : IsDihedral γ)
    (hstar : ∀ a : ZMod 3,
      (∑ r ∈ Finset.univ.filter (fun r : Fin 4 => v r = a),
        perClassMultiset (2 ^ L) p r.val) =
      (∑ r ∈ Finset.univ.filter (fun r : Fin 4 => v r = a),
        perClassMultiset (2 ^ L) p (γ r).val)) :
    ∃ δ : Fin 4 → Fin 4, IsDihedral δ ∧ StabM (2 ^ L) p δ ∧
      ∀ a : ZMod 3, ∀ r : Fin 4, v r = a → v (δ (γ r)) = a := by
  sorry
/-- T6.3 (bijective `τ′` from global `σ`). If `y' = y ∘ σ` for a
bijection `σ` on `ℤ/m` and the class vectors match under `σ`, then
the joint values `J(k) = (p_k, v_{k mod 4})` over pattern positions
`k ∈ ℤ/P` have a bijective matching `τ′` with `J′ = J ∘ τ′`
(wave 11 task 3 §1; counting with multiplicity `m/P`, using
`P ∣ m` and `4 ∣ P`). Bijectivity is load-bearing: a per-`k`
non-injective matching does NOT imply compatibility (abstract
counterexample in the wave-11 note). NOTE: stated over one modulus;
the two-modulus version is the same counting with casts, UNCHECKED. -/
theorem bijective_tau {m P : Nat} (hPm : P ∣ m) (hP4 : 4 ∣ P)
    (y y' : ℕ → ZMod (2 ^ 6)) (v v' : ℕ → ZMod 3)
    (σ : ℕ → ℕ) (hσbij : Function.Bijective (fun i : Fin m => ⟨σ i % m, by omega⟩))
    (hσ : ∀ i, y' i = y (σ i)) (hσv : ∀ i, v' (i % 4) = v (σ i % 4)) :
    ∃ τ' : Fin P → Fin P, Function.Bijective τ' ∧ ∀ k : Fin P,
      y' k.val = y (τ' k).val ∧ v' (k.val % 4) = v ((τ' k).val % 4) := by
  sorry
/-- T6.4 (π₂ = π₃ compatibility). Given the pattern lemma (input A:
`π₂` with `M′_r = M_{π₂(r)}`) and Lemma S (input B: T6.2), there is
`π ∈ Π₂ ∩ Π₃`: `π` relates the per-class multisets AND the mod-3
vectors (wave 11 task 3 §3, with `γ = π₂ ∘ π₃⁻¹` and
`π = δ ∘ π₂`). This is the mod-`D` compatibility step; odd prime
powers `q ≠ 3` vanish (milestone-1 T2.1), so no further prime
needs a compatibility argument. -/
theorem pi2_pi3 {L : Nat} (hL : 2 ≤ L)
    (p p' : ℕ → ZMod (2 ^ (2 * L + 3)))
    (hfix : IsFix (2 ^ L) p) (hfix' : IsFix (2 ^ L) p')
    (v v' : Fin 4 → ZMod 3) (hv2 : v 2 = -v 0) (hv3 : v 3 = -v 1)
    (hv2' : v' 2 = -v' 0) (hv3' : v' 3 = -v' 1)
    (hπ₂ : ∃ π₂ : Fin 4 → Fin 4, IsDihedral π₂ ∧ ∀ r, perClassMultiset (2 ^ L) p' r = perClassMultiset (2 ^ L) p (π₂ r).val)
    (hπ₃ : ∃ π₃ : Fin 4 → Fin 4, IsDihedral π₃ ∧ ∀ r, v' r = v (π₃ r))
    (hS : ∀ γ : Fin 4 → Fin 4, IsDihedral γ → (∀ a : ZMod 3, (∑ r ∈ Finset.univ.filter (fun r : Fin 4 => v r = a), perClassMultiset (2 ^ L) p r.val) = (∑ r ∈ Finset.univ.filter (fun r : Fin 4 => v r = a), perClassMultiset (2 ^ L) p (γ r).val)) → ∃ δ : Fin 4 → Fin 4, IsDihedral δ ∧ StabM (2 ^ L) p δ ∧ ∀ a : ZMod 3, ∀ r : Fin 4, v r = a → v (δ (γ r)) = a) :
    ∃ π : Fin 4 → Fin 4, IsDihedral π ∧ (∀ r, perClassMultiset (2 ^ L) p' r = perClassMultiset (2 ^ L) p (π r).val) ∧ (∀ r, v' r = v (π r)) := by
  sorry
/-! ## Stage 7 — Assembly -/
/-- T7.1 (mod-`D` Lemma Y — the chain's target). For `q ‖ D_m`
(`q` a prime power dividing `(Dm m).toNat`), two `Fix_m mod q`
points with the same global multiset have `D_t`-related class-sum
vectors, `t = gcd(m, 4)` (roadmap T7.1). Assembly: odd `q ≠ 3` by
milestone-1 T2.1; `q = 3^e` by milestone-2 T3.3; `q = 2^a` by
milestone-2 T4.3; 2/3-compatibility by T6.4; CRT over class sums.
Exact-integer class sums (Pcarry) are NOT claimed — mod-`q` only. -/
theorem lemmaY_modD {m q : Nat} (hm : 1 ≤ m)
    (hq : ∃ p e : Nat, p.Prime ∧ q = p ^ e ∧ q ∣ (Dm m).toNat)
    (y y' : ℕ → ZMod q) (hfix : IsFix m y) (hfix' : IsFix m y')
    (hsame : seqMultiset m y = seqMultiset m y') :
    ∃ π : Fin (Nat.gcd m 4) → Fin (Nat.gcd m 4), IsDihedral π ∧ ∀ r, classSum m (Nat.gcd m 4) y' r = classSum m (Nat.gcd m 4) y (π r).val := by
  sorry
/-- T7.2 (support is a union of fibers, conditional form). If a
support predicate on `Fix` points depends only on the pair-value
multiset `{z · y : z ∈ Z}` (the `pair_sorted` data — the content of
main's `φ̂` support criterion in `LineDOrbitPairFull`, via
milestone-1 T1.2's dot identity `z · y = z̄ · Y(y)` and the
`D_t`-invariance of `z̄`), then T7.1 implies it is constant on
fibers. The `φ̂` criterion itself is NOT restated here. -/
theorem support_union_fibers {m q : Nat} (hm : 1 ≤ m)
    (supp : (ℕ → ZMod q) → Prop)
    (hpair : ∀ y y' : ℕ → ZMod q, IsFix m y → IsFix m y' →
      seqMultiset m y = seqMultiset m y' → (supp y ↔ supp y'))
    (y y' : ℕ → ZMod q) (hfix : IsFix m y) (hfix' : IsFix m y')
    (hsame : seqMultiset m y = seqMultiset m y') :
    supp y ↔ supp y' := by
  sorry
/-! NOT in this draft: no complete proof (every proof is `sorry`); no
stages 0–5 (see milestones 1–2), exact Pcarry, G1 at f ≥ 3, general
Lemma PC, G4b, 152, BGS-BGS-001, TRACE-005, hEquidistUnits, or RMT
statistics; no redefinition of main's objects, no change to
`LineBDerand`, no full-`Bgs` import; `m = 0` excluded. -/
end Bgs.Breakthrough.LemmaYM3
