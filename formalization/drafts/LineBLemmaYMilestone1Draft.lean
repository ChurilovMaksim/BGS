/-! BREAKTHROUGH DRAFT — research record, not a theorem.
    Source: BGS breakthrough program (Nov 2026), wave notes in evidence/breakthrough/methods/.
    Status: draft; built counterpart LemmaYM1Fixed.lean (769 s, 0 errors, 13 sorry).
    Not imported by formalization/Bgs.lean. Registry status unchanged. -/

/-!
# DRAFT ONLY — NOT A PROOF, NOT FOR MAIN

File: `bgs-breakthrough/lean-drafts/LineBLemmaYMilestone1Draft.lean`
Task: wave 15, task 4 — first Lean milestone draft for the Lemma Y chain
(roadmap `methods/wave14_Lean_roadmap_LemmaY.md`): Stage 0 (Pell / LTE /
radical inputs) + Stage 1 (Fix / class-sum setup) + Stage 2 (odd
component). Status: text draft only. `lake build` was NOT run
(forbidden for this task), no file in the repository was touched,
nothing was pushed to `main`. Every `sorry` below is an explicit
placeholder, not a claim: this file must not be cited as proved, and
must not enter `main` until every `sorry` is replaced and the axiom
audit is clean (standard axioms only, `sorryAx = 0`).

## Verified source (current main, via GitHub connector only)

- Repository: `ChurilovMaksim/BGS`, branch `main`,
  HEAD `d87dce0d9277579568edfee6cffecbc96ea61024`.
- `formalization/Bgs/LineBDerand.lean`, blob SHA
  `01fa6e63551542de55cce52cb9fb54c660f89b54`, read with
  `get_file_contents` at that ref. Definitions used verbatim:
  - `pellX : Nat → Int`, `pellY : Nat → Int`, mutually recursive:
    `pellX 0 = 1`, `pellX (n+1) = 3 * pellX n + 8 * pellY n`,
    `pellY 0 = 0`, `pellY (n+1) = pellX n + 3 * pellY n`.
  - `Dm m = 2 * (pellX m - 1)`.
  - `gp m = (pellX m - 1).toNat / Nat.gcd (pellX m - 1).toNat (pellY m).toNat`.
  - `pellQ`, `pellP` (companion Pell numbers) with main's finite
    `D_closed`: `Dm m = pellQ m ^ 2` (m odd), `Dm m = 8 * pellP m ^ 2`
    (m even), checked in main for `1 ≤ m ≤ 20`.
  - `Hm`, `Lpow`, `d1`, `d2`, `radSize` (not used by this milestone
    beyond the radical statement's source).
- No object from main is re-defined here: `pellX`, `pellY`, `Dm`,
  `gp`, `pellQ`, `pellP` are imported from `Bgs.LineB.Derand`.

## Roadmap mapping (exact)

- T0.1 (Pell identity + C1, via main's `pellQ`/`pellP` form, proof
  route = `lean-drafts/LineBPellC1Draft.lean` L1–L4).
- T0.2 (LTE `v₂(D_m)` formula, proof = `methods/wave11_task3_LTE_v2Dm.md`).
- T0.4 (radical as primeFactors equality, proof sketch wave 3,
  `lean-drafts/LineBRadicalDraft.lean`).
- T1.1 (Fix setup), T1.2 (class sums + class-sum dot identity,
  proof = `methods/pair_sorted_identity_note.md` §§1–3).
- T2.1 (vanishing for `p ∤ 24`, proof = `methods/wave8_lemmaY_proof_attempt.md` §2).
- T2.2 (mod-3 classification, proof = wave 8 §3 / wave 9 Lemma 6).
- T2.3 (mod-3 component Lemma Y, assembly of T2.2; wave 8 §3).
- OUT of this milestone (deferred, see roadmap): T0.3 (`v₃` formula,
  stage 3 input), T0.5 (SNF of `M^m − I`), all of stages 3–7
  (P3′, P2 uniform, pattern lemma, Lemma S, compatibility, assembly),
  exact Pcarry, G1 at `f ≥ 3`, general Lemma PC, G4b Lean, 152.

## Mathlib API status (waves 6 / 10 verified, or flagged UNCHECKED)

- VERIFIED (wave 6 grep): flat import `import Bgs.LineBDerand`
  (namespace `Bgs.LineB.Derand` opened below);
  `Nat.mem_primeFactors_of_ne_zero` form for primeFactors arguments;
  `Nat.Prime.dvd_iff_one_le_factorization` (not needed below, noted
  for T0.4's proof); `Nat.radical` does NOT exist — hence the
  primeFactors restatement of T0.4.
- VERIFIED (wave 10 grep): `Finset.sum_fiberwise_of_maps_to` (the
  regrouping behind T1.2's proof); `Finset.sum_image`,
  `Finset.sum_le_sum_of_subset_of_nonneg` (not needed below).
- UNCHECKED (not covered by the wave 6 / 10 grep passes; to confirm
  at elaboration): `Finset.sum` / `Finset.filter` / `Finset.range`
  notation, `Multiset.ofList` and Multiset literals, `Fin` arithmetic
  (`+`, `-` on `Fin t`), `Nat.factorization`, `ZMod` numeral
  literals. No proof below depends on an unchecked name's exact
  signature — every proof is `sorry` — but the statements must be
  re-checked against the elaborator before any claim is made.
-/

import Bgs.LineBDerand

namespace Bgs.Breakthrough.LemmaYM1

open Bgs.LineB.Derand

/-! ## Stage 0 — Pell / valuation inputs -/

/-- T0.1a (Pell identity, general form of main's finite `pell_id`).
Proof route: Pell draft L1–L2 (norm of `(1 + √2)^{2m}`). -/
theorem pell_id_all (m : Nat) :
    pellX m * pellX m - 8 * pellY m * pellY m = 1 := by
  sorry

/-- T0.1b (factored form). Immediate from T0.1a by `ring`-style
rearrangement once T0.1a is proved; used by the radical argument. -/
theorem pell_factor (m : Nat) :
    (pellX m - 1) * (pellX m + 1) = 8 * pellY m * pellY m := by
  sorry

/-- T0.1c (positivity, needed before any `toNat` step). From the
Pell draft's `pell_pos`. -/
theorem pell_pos {m : Nat} (hm : 1 ≤ m) : 1 ≤ pellX m ∧ 1 ≤ pellY m := by
  sorry

/-- T0.1d (Pell formula C1, in main's own `pellQ` / `pellP` form).
This is the Pell draft's C1 restated without its private `(u, v)`:
odd `m` gives `gp m = pellQ m` (check: m = 1: 2 = 2; m = 3: 14 = 14),
even `m` gives `gp m = 4 * pellP m` (m = 2: 8 = 4·2; m = 4: 48 = 4·12),
using main's `gprime_values` / `D_closed` as the finite sanity check.
Proof route: Pell draft L1–L4 (the `(u, v)` identification
`pellX m = uvU (2m)`, `2 * pellY m = uvV (2m)` plus the gcd
computation); the only Lean-technical blocker is the draft's L4
`gp` cast lemma (`Int.toNat` / `Nat` division bookkeeping). -/
theorem pellC1 {m : Nat} (hm : 1 ≤ m) :
    (m % 2 = 1 → gp m = (pellQ m).toNat) ∧
    (m % 2 = 0 → gp m = 4 * (pellP m).toNat) := by
  sorry

/-- T0.2 (LTE: `v₂(D_m)` depends only on `v₂(m)`).
Proof: `methods/wave11_task3_LTE_v2Dm.md` (proved there):
in `R = ℤ[√2]`, `D_m = α^{-m}(α^m − 1)²`, so
`v₂(D_m) = v_𝔭(α^m − 1)` for `𝔭 = (√2)`; base valuations
`v_𝔭(α − 1) = 2`, `v_𝔭(α + 1) = 3`, and the cofactor argument
for odd `m` / the `2^j`-tower for even `m`.
`Nat.factorization` is UNCHECKED (see header). -/
theorem lte_v2 {m : Nat} (hm : 1 ≤ m) :
    Nat.factorization (Dm m).toNat 2 =
      if m % 2 = 1 then 2 else 2 * Nat.factorization m 2 + 3 := by
  sorry

/-- T0.4 (radical lemma, primeFactors restatement).
`Nat.radical` does not exist in Mathlib v4.33.1 (wave 6 grep), so
the wave-3 sketch `rad(D_m) = rad(gp)` is stated as equality of
prime-factor lists. Proof route: odd primes from
`(x − 1)(x + 1) = 8y²` (T0.1b); `p = 2` via T0.2 and the
`v₂(gp)` values (1 for odd `m`, `2 + v₂(y_m)` for even `m`).
API for the proof's factorization lemmas: VERIFIED wave 6. -/
theorem radical_eq {m : Nat} (hm : 1 ≤ m) :
    (Dm m).toNat.primeFactors = (gp m).primeFactors := by
  sorry

/-! ## Stage 1 — Fix / class-sum setup -/

/-- The recurrence sequence with initial values `a, b` over `ZMod q`.
Definitional: `seqFrom a b (n + 2) = 6 * seqFrom a b (n + 1) - seqFrom a b n`. -/
def seqFrom {q : Nat} (a b : ZMod q) : ℕ → ZMod q
  | 0 => a
  | 1 => b
  | n + 2 => 6 * seqFrom a b (n + 1) - seqFrom a b n

/-- T1.1 (Fix setup). A sequence is in `Fix_m mod q` iff it is a
recurrence sequence (some `seqFrom a b`) that is `m`-periodic.
This is the wave 8/9 setup: `Fix_m mod q = ker(M^m − I)` with
`M = [[6, -1], [1, 0]]`, stated here without Matrix API (UNCHECKED
for the kernel form; the sequence form below is what stages 2+
actually use). -/
def IsFix {q : Nat} (m : Nat) (y : ℕ → ZMod q) : Prop :=
  ∃ a b : ZMod q, y = seqFrom a b ∧ ∀ i, y (i + m) = y i

/-- T1.1b (determination by initial values). Any sequence satisfying
the recurrence and `m`-periodicity is `seqFrom (y 0) (y 1)`. -/
theorem fix_eq_seqFrom {q m : Nat} (y : ℕ → ZMod q)
    (hrec : ∀ n, y (n + 2) = 6 * y (n + 1) - y n)
    (hper : ∀ i, y (i + m) = y i) :
    y = seqFrom (y 0) (y 1) := by
  sorry

/-- Class sums. `classSum m t y r` is the sum of `y i` over the
`+t`-orbit class `i ≡ r (mod t)` inside `range m` — the wave-8
`Y_r(y)`. Exact-integer lifts (needed later for Pcarry) are a
refinement; the mod-`q` version here is what T2.1 / T2.2 need.
`Finset` notation is UNCHECKED (see header). -/
def classSum {q : Nat} (m t : Nat) (y : ℕ → ZMod q) (r : ℕ) : ZMod q :=
  ∑ i ∈ (Finset.range m).filter (fun i => i % t = r), y i

/-- The global multiset of a sequence over one period. `Multiset`
notation is UNCHECKED (see header). -/
def seqMultiset {q : Nat} (m : Nat) (y : ℕ → ZMod q) : Multiset (ZMod q) :=
  Multiset.ofList ((List.range m).map y)

/-- T1.2 (class-sum dot identity, the `(*)` of the pair note).
If `z` is constant on each `+t`-class (with class values `zbar`),
then the full dot product splits as a dot product of `zbar` with
the class-sum vector `Y`. Proof route: fiber regrouping of the
sum over `range m` by `i ↦ i % t` (needs `t ∣ m`); the regrouping
lemma `Finset.sum_fiberwise_of_maps_to` is VERIFIED (wave 10).
This is the unconditional step behind `pairNum(z, w_y) = z · y =
z̄ · Y(y)`; the adjugate step `Xw = y` (main's `Hmat_mul_Xmat`,
`Xmat_transpose` in `LineDOrbitPairFull`) is the bridge to the
`φ̂` support criterion and belongs to the 152 assembly, not to
the Lemma Y chain core. -/
theorem classSum_dot {q m t : Nat} (ht : t ∣ m) (ht0 : 0 < t)
    (y z : ℕ → ZMod q) (zbar : ℕ → ZMod q)
    (hconst : ∀ i, z i = zbar (i % t)) :
    ∑ i ∈ Finset.range m, z i * y i =
      ∑ r ∈ Finset.range t, zbar r * classSum m t y r := by
  sorry

/-! ## Stage 2 — Odd component -/

/-- A dihedral permutation of the `t` classes: a shift, or a
reflection followed by a shift. `Fin` arithmetic is UNCHECKED
(see header). -/
def IsDihedral {t : Nat} (π : Fin t → Fin t) : Prop :=
  ∃ b : Fin t, (∀ r, π r = r + b) ∨ (∀ r, π r = -r + b)

/-- T2.1 (vanishing for `p ∤ 24`: component Lemma Y is trivial there).
Proof (wave 8 §2): in `R/qR`, `q` odd, `α − β = 4√2` has norm `−32`,
a unit mod `q`, so every recurrence sequence is `y_i = Aα^i + Āβ^i`
and `(α^4 − 1)Y_r = 0`; since `α^4 − 1 = 576 + 408√2` and
`gcd(576, 408) = 24`, `p ∤ 24` forces `Y_r ≡ 0 (mod q)`. The
`ℤ[√2]`-mod-`q` representation is a NEW argument for Lean
(roadmap stage-2 note); it is not proved by this draft. -/
theorem vanishing {m p e : Nat} (hm : 1 ≤ m) (hp : p.Prime)
    (hp2 : p ≠ 2) (hp3 : p ≠ 3)
    (y : ℕ → ZMod (p ^ e)) (hfix : IsFix m y) :
    ∀ r, classSum m (Nat.gcd m 4) y r = 0 := by
  sorry

/-- T2.2a (mod-3 period-4 form). For `4 ∣ m`, every `Fix_m mod 3`
sequence satisfies `y (i + 2) = -y i` (the recurrence mod 3 is
`y_{i+1} = -y_{i-1}` since `6 ≡ 0`), hence is 4-periodic of the
form `(a, b, -a, -b)` repeated. Proof: wave 8 §3 / wave 9 Lemma 6
setup; finite check, no enumeration of `Fix` needed. -/
theorem mod3_period4 {m : Nat} (hm : 4 ∣ m)
    (y : ℕ → ZMod 3) (hfix : IsFix m y) :
    ∀ i, y (i + 2) = -y i := by
  sorry

/-- T2.2b (mod-3 classification into 3 types). A 4-vector of the
form `(a, b, -a, -b)` over `𝔽₃` has multiset `{0⁴}`, `{0², 1, 2}`,
or `{1², 2²}`. Proof: exhaustive over the 9 pairs `(a, b) ∈ 𝔽₃²`
(wave 9 Lemma 6). Multiset literals are UNCHECKED (see header). -/
theorem mod3_types (v : Fin 4 → ZMod 3) (h2 : v 2 = -v 0) (h3 : v 3 = -v 1) :
    Multiset.ofList [v 0, v 1, v 2, v 3] = {0, 0, 0, 0} ∨
    Multiset.ofList [v 0, v 1, v 2, v 3] = {0, 0, 1, 2} ∨
    Multiset.ofList [v 0, v 1, v 2, v 3] = {1, 1, 2, 2} := by
  sorry

/-- T2.2c (equal mod-3 multisets ⇒ `D₄`-related). Within each of
the 3 types of T2.2b, the rotation `(a, b) ↦ (b, -a)` cycles the
whole type, so each type is a single `D₄`-orbit. Finite case split
(roadmap: easiest step of the chain). -/
theorem mod3_D4 (v w : Fin 4 → ZMod 3)
    (hv2 : v 2 = -v 0) (hv3 : v 3 = -v 1)
    (hw2 : w 2 = -w 0) (hw3 : w 3 = -w 1)
    (h : Multiset.ofList [v 0, v 1, v 2, v 3] =
      Multiset.ofList [w 0, w 1, w 2, w 3]) :
    ∃ π : Fin 4 → Fin 4, IsDihedral π ∧ ∀ r, w r = v (π r) := by
  sorry

/-- T2.3 (mod-3 component Lemma Y: stage-2 assembly).
For `4 ∣ m`, two `Fix_m mod 3` points with the same global multiset
have `D₄`-related class-sum vectors. Proof: T2.2a gives the
`(a, b, -a, -b)` form; class sums are `(m/4) • (a, b, -a, -b)`
mod 3, so equal global multisets give equal 4-vector multisets
(the factor `m/4` is common), and T2.2c applies. Note the
degenerate subcase `3 ∣ m/4` (i.e. `12 ∣ m`): then class sums
vanish mod 3 and the claim is trivial — this is exactly why
stage 3 (P3′) needs the top digit, not the mod-3 class sum. -/
theorem componentY_mod3 {m : Nat} (hm : 4 ∣ m)
    (y y' : ℕ → ZMod 3) (hfix : IsFix m y) (hfix' : IsFix m y')
    (hsame : seqMultiset m y = seqMultiset m y') :
    ∃ π : Fin 4 → Fin 4, IsDihedral π ∧
      ∀ r, classSum m 4 y' r = classSum m 4 y (π r).val := by
  sorry

/-! ## What is NOT in this draft

- No proof of any statement above is complete: every proof is `sorry`.
- No statement about stages 3–7 (P3′, P2 uniform, pattern lemma,
  Lemma S, compatibility, mod-D assembly), exact Pcarry, G1 at
  `f ≥ 3`, general Lemma PC, G4b, 152, `BGS-BGS-001`, `TRACE-005`,
  `hEquidistUnits`, or RMT statistics.
- No redefinition of main's objects, no change to `LineBDerand`,
  no import of the full `Bgs` aggregator.
- The `m = 0` case is deliberately excluded throughout (see the
  Pell draft's Scope note: `gp 0` is degenerate).
-/

end Bgs.Breakthrough.LemmaYM1
