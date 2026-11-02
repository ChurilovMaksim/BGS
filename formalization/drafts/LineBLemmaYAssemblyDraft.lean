/-! BREAKTHROUGH DRAFT — research record, not a theorem.
    Source: BGS breakthrough program (Nov 2026), wave notes in evidence/breakthrough/methods/.
    Status: draft; assembly draft, not built in this form.
    Not imported by formalization/Bgs.lean. Registry status unchanged. -/

import Bgs.LineBDerand
/-! DRAFT ONLY — NOT A PROOF, NOT FOR MAIN. Wave 26, task 5: Lean
assembly draft for Lemma Y at mod-`D` level, composing the three
milestone drafts of the Lemma Y chain (roadmap wave14_Lean_roadmap_LemmaY.md):

  Milestone 1 (stages 0–2): Pell, setup, odd component.
    Fixed copy BUILDS (wave 19: 769 s, 8706 jobs, 0 errors, 13 sorry).
  Milestone 2 (stages 3–5): P3′, P2 uniform, pattern lemma.
    Fixed build RUNNING in wave 25 (diagnosis wave 20: import + `π r` ×4).
  Milestone 3 (stages 6–7): Lemma S, compatibility, mod-D assembly.
    Fixed copy BUILDS (wave 23: 861 s, 8706 jobs, 0 errors, 6 sorry).

Every proof below is `sorry`; this file states HOW the milestones
compose, it does not prove any of them. Do not cite as proved, do not
enter `main` until every `sorry` is replaced and `sorryAx = 0`.

## Dependency wiring (which theorem feeds which hypothesis)

  M1 T0.1 (pellC1) + T0.2 (lte_v2) + T0.4 (radical_eq)
      → prime-power inventory: every `q ‖ (Dm m).toNat` is `2^a`,
        `3^e`, or `p^e` with `p ∤ 24`; the exponents `a, e` are the
        ones in the component lemmas below.
  M1 T1.2 (classSum_dot) → T7.2 (support-union) dot step.
  M1 T2.1 (vanishing) → odd `q = p^e`, `p ∤ 24` branch: class sums
      are 0, so any `π` works there.
  M1 T2.3 (componentY_mod3) → M2 T3.3 input: the mod-3 classification
      (T2.2a–c) underlying the top-digit argument.
  M2 T3.1 (scaling_div, scaling_bij) + T3.2 (top_digit)
      → M2 T3.3 (componentY_mod3pow): the `q = 3^e` branch.
  M2 T4.1 (alpha_pow) + T4.2 (doubling) → M2 T4.3
      (componentY_mod2pow): the `q = 2^a` branch (exponent `a` from
      M1 T0.2).
  M2 T5.1–T5.3 (block_period, block_shift, pattern_mod32)
      → M2 T5.4 (pattern_lemma): input A (`π₂`) of M3 T6.4.
  M3 T6.1 (pair_lemma) → M3 T6.2 (lemmaS): input B of M3 T6.4.
  M3 T6.3 (bijective_tau) → the counting behind T6.4 (a per-`k`
      non-injective matching does NOT imply compatibility).
  M3 T6.4 (pi2_pi3) → the 2/3-compatibility step of T7.1: one
      `π ∈ Π₂ ∩ Π₃` for the `2^a` and `3^e` branches jointly.
  T7.1 (lemmaY_modD) = branches + T6.4 + CRT over class sums.
  T7.2 (support_union_fibers) = T7.1 + M1 T1.2.

## Namespace reconciliation (read before assembling for real)

The three milestone drafts each define their own copies of
`seqFrom`, `IsFix`, `classSum`, `seqMultiset`, `perClassMultiset`,
`IsDihedral` under `LemmaYM1` / `LemmaYM2` / `LemmaYM3`. This file
defines ONE shared copy below (bodies text-identical to the
milestones'). A real assembly must either refactor the milestones
onto this shared base (the bodies being text-identical, the
transport is expected to be `rfl` after the refactor, but that
is NOT proved here — see the transport note before Stage 7).

## What is NOT supplied by the milestones (remains as hypotheses)

The mod-`D` assembly needs nothing beyond the milestone theorems.
The step from mod-`D` class sums to EXACT per-class multisets —
the form 152's separation step needs — additionally needs, as
explicit open hypotheses of `exact_perclass_from_modD` below:
  G1 (odd lift, open at `f ≥ 3`; `f = 2` closed wave 25, `s = 0`
      hole closed by proof, not search),
  general Lemma PC (common `π` across components; only the
      `(3,17)` / `8 ∣ m` class is proved),
  Pcarry (exact-integer class sums; mod-`q` only is claimed here).
Also out of scope: G4b, 152, `BGS-BGS-001`, `TRACE-005`,
`hEquidistUnits`, RMT statistics; `m = 0` excluded.

Import note: flat `Bgs.LineBDerand` on line 1 (wave 20/21 resolution:
flat path, dotted namespace `Bgs.LineB.Derand` inside the file).
In the test copy, which has no Derand module, replace this import
with Mathlib plus stubs, as the M1/M3 fixed-copy probes did; the
assembly statements themselves do not depend on Derand's proofs.
-/
namespace Bgs.Breakthrough.LemmaYAssembly
open Bgs.LineB.Derand

/-- Recurrence sequence with initial values `a, b` over `ZMod q`
(shared copy; same body as in all three milestones). -/
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

/-! ## Stage 7 — the assembly theorem

NOTE on transport (no theorem stated for it): the milestone
theorems live in their own namespaces over their own copies of
the vocabulary, so they cannot be cited verbatim here. The
assembly hypotheses below are those theorems RESTATED over the
shared vocabulary. Discharging the restatement — i.e. proving
each milestone theorem implies its assembly hypothesis — is
future work, expected to go through a shared-base refactor (the
copies are text-identical, so `rfl` is plausible but NOT proved
here). Until then, the assembly is conditional on the restated
hypotheses, not on the milestone files themselves. -/

/-- T7.1-assembly (mod-`D` Lemma Y from the milestone interface
theorems). Hypotheses, each named after the milestone theorem
that supplies it:
  `hOdd`   = M1 T2.1 `vanishing` (odd `p ∤ 24` branch),
  `h3pow`  = M2 T3.3 `componentY_mod3pow` (`q = 3^e` branch),
  `h2pow`  = M2 T4.3 `componentY_mod2pow` (`q = 2^a` branch),
  `hCompat` = M3 T6.4 `pi2_pi3` (one `π` for the 2- and 3-branches
    jointly; `4 ∣ m` case — for `t = gcd(m, 4) < 4` the 4-class
    statements restrict to `t` classes, and `t = 1` is trivial
    since `Fin 1` has one element).
The `q ‖ (Dm m).toNat` hypothesis is the prime-power inventory
supplied by M1 T0.1/T0.2/T0.4; CRT over class sums combines the
branches into one `π ∈ D_t`. -/
theorem lemmaY_modD_assembly {m q : Nat} (hm : 1 ≤ m)
    (hq : ∃ p e : Nat, p.Prime ∧ q = p ^ e ∧ q ∣ (Dm m).toNat)
    (hOdd : ∀ {p e : Nat}, p.Prime → p ≠ 2 → p ≠ 3 → q = p ^ e →
      ∀ (y : ℕ → ZMod q), IsFix m y → ∀ r, classSum m (Nat.gcd m 4) y r = 0)
    (h3pow : ∀ {f₀ : Nat}, 4 ∣ m → f₀ = 1 + Nat.factorization (m / 4) 3 →
      q = 3 ^ (2 * f₀) →
      ∀ (y y' : ℕ → ZMod q), IsFix m y → IsFix m y' →
      seqMultiset m y = seqMultiset m y' →
      ∃ π : Fin 4 → Fin 4, IsDihedral π ∧
        ∀ r, classSum m 4 y' r = classSum m 4 y (π r).val)
    (h2pow : ∀ (y y' : ℕ → ZMod q), IsFix m y → IsFix m y' →
      seqMultiset m y = seqMultiset m y' →
      ∃ π : Fin (Nat.gcd m 4) → Fin (Nat.gcd m 4), IsDihedral π ∧
        ∀ r, classSum m (Nat.gcd m 4) y' r =
          classSum m (Nat.gcd m 4) y (π r).val)
    (hCompat : ∀ {L : Nat}, 2 ≤ L →
      ∀ (p p' : ℕ → ZMod (2 ^ (2 * L + 3))),
      IsFix (2 ^ L) p → IsFix (2 ^ L) p' →
      ∀ (v v' : Fin 4 → ZMod 3),
      v 2 = -v 0 → v 3 = -v 1 → v' 2 = -v' 0 → v' 3 = -v' 1 →
      (∃ π₂ : Fin 4 → Fin 4, IsDihedral π₂ ∧ ∀ r,
        perClassMultiset (2 ^ L) p' r =
          perClassMultiset (2 ^ L) p (π₂ r).val) →
      (∃ π₃ : Fin 4 → Fin 4, IsDihedral π₃ ∧ ∀ r, v' r = v (π₃ r)) →
      ∃ π : Fin 4 → Fin 4, IsDihedral π ∧ (∀ r,
        perClassMultiset (2 ^ L) p' r =
          perClassMultiset (2 ^ L) p (π r).val) ∧ (∀ r, v' r = v (π r)))
    (y y' : ℕ → ZMod q) (hfix : IsFix m y) (hfix' : IsFix m y')
    (hsame : seqMultiset m y = seqMultiset m y') :
    ∃ π : Fin (Nat.gcd m 4) → Fin (Nat.gcd m 4), IsDihedral π ∧
      ∀ r, classSum m (Nat.gcd m 4) y' r =
        classSum m (Nat.gcd m 4) y (π r).val := by
  sorry

/-- T7.2-assembly (support is a union of fibers, conditional form).
From T7.1-assembly plus M1 T1.2 (`classSum_dot`, stated here as
`hDot`): if a support predicate depends only on the pair-value
multiset (the `pair_sorted` data — main's `φ̂` support criterion
in `LineDOrbitPairFull`), then it is constant on fibers. The `φ̂`
criterion itself is NOT restated here. -/
theorem support_union_from_assembly {m q : Nat} (hm : 1 ≤ m)
    (hAssem : ∀ (y y' : ℕ → ZMod q), IsFix m y → IsFix m y' →
      seqMultiset m y = seqMultiset m y' →
      ∃ π : Fin (Nat.gcd m 4) → Fin (Nat.gcd m 4), IsDihedral π ∧
        ∀ r, classSum m (Nat.gcd m 4) y' r =
          classSum m (Nat.gcd m 4) y (π r).val)
    (hDot : ∀ {t : Nat}, t ∣ m → 0 < t →
      ∀ (y z : ℕ → ZMod q) (zbar : ℕ → ZMod q),
      (∀ i, z i = zbar (i % t)) →
      ∑ i ∈ Finset.range m, z i * y i =
        ∑ r ∈ Finset.range t, zbar r * classSum m t y r)
    (supp : (ℕ → ZMod q) → Prop)
    (hpair : ∀ y y' : ℕ → ZMod q, IsFix m y → IsFix m y' →
      seqMultiset m y = seqMultiset m y' → (supp y ↔ supp y'))
    (y y' : ℕ → ZMod q) (hfix : IsFix m y) (hfix' : IsFix m y')
    (hsame : seqMultiset m y = seqMultiset m y') :
    supp y ↔ supp y' := by
  sorry

/-! ## Beyond mod-`D`: what the exact lemma still needs -/

/-- Exact per-class lemma from the mod-`D` assembly, with the three
open gaps as EXPLICIT hypotheses (all unproved, all `sorry` here):
  `hG1`  : odd lift G1 at `f ≥ 3` (the `f = 2` case is closed);
  `hPC`  : general Lemma PC, one common `π` across all components;
  `hPcarry` : exact-integer class sums (Pcarry), lifting the
    mod-`q` statement to exact multisets.
This is the form 152's separation step needs; it is NOT claimed
as proved, and none of `hG1`, `hPC`, `hPcarry` is supplied by
milestones 1–3. -/
theorem exact_perclass_from_modD {m : Nat} (hm : 1 ≤ m)
    (hAssem : ∀ (q : Nat), (∃ p e : Nat, p.Prime ∧ q = p ^ e ∧
      q ∣ (Dm m).toNat) →
      ∀ (y y' : ℕ → ZMod q), IsFix m y → IsFix m y' →
      seqMultiset m y = seqMultiset m y' →
      ∃ π : Fin (Nat.gcd m 4) → Fin (Nat.gcd m 4), IsDihedral π ∧
        ∀ r, classSum m (Nat.gcd m 4) y' r =
          classSum m (Nat.gcd m 4) y (π r).val)
    (hG1 : True) (hPC : True) (hPcarry : True)
    (y y' : ℕ → ℤ) (hsame : True) :
    ∃ π : Fin (Nat.gcd m 4) → Fin (Nat.gcd m 4), IsDihedral π ∧ True := by
  sorry

/-! NOT in this draft: no complete proof (every proof is `sorry`);
no stages 0–6 proofs (see the milestone drafts), no redefinition of
main's objects, no change to `LineBDerand`, no full-`Bgs` import;
`m = 0` excluded. -/
end Bgs.Breakthrough.LemmaYAssembly
