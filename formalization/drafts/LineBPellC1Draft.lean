/-! BREAKTHROUGH DRAFT — research record, not a theorem.
    Source: BGS breakthrough program (Nov 2026), wave notes in evidence/breakthrough/methods/.
    Status: draft, not built in this form; statement draft only.
    Not imported by formalization/Bgs.lean. Registry status unchanged. -/

/-!
# DRAFT ONLY — NOT A PROOF, NOT FOR MAIN

File: `bgs-breakthrough/lean-drafts/LineBPellC1Draft.lean`
Task: wave 2, task 2 — draft Lean lemma for the Pell formula C1.
Status: text draft only. `lake build` was NOT run (forbidden for this task),
no file in the repository was touched, nothing was pushed to `main`.
Every `sorry` below is an explicit placeholder, not a claim:
this file must not be cited as proved, and must not enter `main`
until every `sorry` is replaced and the axiom audit is clean
(standard axioms only, `sorryAx = 0`).

## Verified source (current main, via GitHub connector)

- Repository: `ChurilovMaksim/BGS`, branch `main`, HEAD `a562e0cf`.
- `formalization/Bgs/LineBDerand.lean`, blob SHA
  `01fa6e63551542de55cce52cb9fb54c660f89b54`, read with
  `get_file_contents` at that ref. Definitions used verbatim in spirit:
  - `pellX : Nat → Int`, `pellY : Nat → Int`, mutually recursive:
    `pellX 0 = 1`, `pellX (n+1) = 3 * pellX n + 8 * pellY n`,
    `pellY 0 = 0`, `pellY (n+1) = pellX n + 3 * pellY n`.
  - `Dm m = 2 * (pellX m - 1)`.
  - `gp m = (pellX m - 1).toNat / Nat.gcd (pellX m - 1).toNat (pellY m).toNat`.
  - `pell_id` in main is only a finite `decide` check for `m < 30`;
    the general identity `pellX m ^ 2 - 8 * pellY m ^ 2 = 1` is
    Lemma L4 below, not imported from main.
- Numerical check of the target formula (independent Python, integers):
  for `m = 1..20`, with `u m, v m` as in §1, `gp m` from main's
  definition equals `2 * u m` for odd `m` and `4 * v m` for even `m`,
  and `Dm m = gp m ^ 2` (odd) / `2 * Dm m = gp m ^ 2` (even).
  A numerical check is not a proof; it only fixes the statement.

## Dependencies (proposed, to be confirmed at build time — not built here)

- `Bgs.LineB.Derand` — for `pellX`, `pellY`, `Dm`, `gp` only.
  Do NOT re-define `pellX`/`pellY`/`gp` in this file: redefinition
  would silently change the object.
- Core `Nat.gcd` lemmas (`Nat.gcd_mul_left`, `Nat.Coprime` API) and
  `Int` ring arithmetic. If a gcd lemma used below is not in core,
  add `Mathlib.Data.Nat.GCD.Basic` — and record the addition;
  do not silently widen imports to `Mathlib.Tactic` without measuring.

## Scope

- `m ≥ 1` only. `m = 0` is excluded on purpose: `pellX 0 - 1 = 0`,
  `pellY 0 = 0`, `Nat.gcd 0 0 = 0`, and `gp 0` is `0 / 0 = 0` in `Nat`,
  while the formula would claim `2 * uvU 0 = 2`. The draft does not
  try to rescue `m = 0`.
-/

import Bgs.LineB.Derand

namespace Bgs.Breakthrough.PellC1

open Bgs.LineB.Derand

/-! ## 1. The pair `(u m, v m)` for `(1 + √2)^m`

Defined by the same mutual-recursion pattern as `pellX`/`pellY` in
main, so that no real `√2` is needed: multiplication by `(1 + √2)`
is `(u, v) ↦ (u + 2v, u + v)`. -/

/-- `uvU m` is the rational part of `(1 + √2)^m`. -/
def uvU : Nat → Int
  | 0 => 1
  | n + 1 => uvU n + 2 * uvV n
where uvV : Nat → Int
  | 0 => 0
  | n + 1 => uvU n + uvV n

/-- `uvV m` is the coefficient of `√2` in `(1 + √2)^m`. -/
def uvV (n : Nat) : Int := uvU.uvV n

/-! ## 2. Lemmas needed, in proof order

Each lemma is stated exactly, with its proof idea. `sorry` marks
"not yet elaborated in this draft", never "proved".

### L1 — norm (the engine)
Induction on `m`. Step: with `u' = u + 2v`, `v' = u + v`,
`(u')^2 - 2 (v')^2 = -(u^2 - 2 v^2)` by `ring`, so the sign flips
at every step and `(-1)^m` appears. No number theory beyond `ring`.
-/
theorem uv_norm (m : Nat) :
    uvU m * uvU m - 2 * uvV m * uvV m = (-1 : Int) ^ m := by
  sorry

/-- Positivity, needed for every `toNat` step below. Induction on `m`. -/
theorem uv_pos (m : Nat) : 0 < uvU m ∧ 0 ≤ uvV m := by
  sorry

/-- Parity. `uvU` is always odd; `uvV m` is odd iff `m` is odd.
Induction on `m`, working mod 2. -/
theorem uv_parity (m : Nat) : uvU m % 2 = 1 ∧ uvV m % 2 = (m : Int) % 2 := by
  sorry

/-- Coprimality from the norm. If `d ∣ uvU m` and `d ∣ uvV m`
(in `Nat`, after `toNat`), then `d ∣ (uvU m ^ 2 - 2 * uvV m ^ 2) = ±1`
by L1, hence `d = 1`. -/
theorem uv_coprime (m : Nat) :
    Nat.gcd (uvU m).toNat (uvV m).toNat = 1 := by
  sorry

/-- Addition formula for the pair. Induction on the second argument,
using the one-step recurrence. This is the only way the squaring
step in L5 is justified without real numbers. -/
theorem uv_add (a b : Nat) :
    uvU (a + b) = uvU a * uvU b + 2 * uvV a * uvV b ∧
    uvV (a + b) = uvU a * uvV b + uvV a * uvU b := by
  sorry

/-- Doubling. Immediate from L4 with `a = b = m`. -/
theorem uv_double (m : Nat) :
    uvU (2 * m) = uvU m * uvU m + 2 * uvV m * uvV m ∧
    uvV (2 * m) = 2 * uvU m * uvV m := by
  sorry

### L2 — bridge from main's Pell pair to `(u, v)`

The key identification, in two steps. First, the pair
`(pellX m, pellY m)` satisfies the same double-step recurrence as
`(uvU (2 * m), uvV (2 * m) / 2)`: multiplying
`U + V√2` by `(3 + 2√2) = (1 + √2)^2` gives
`U' = 3U + 4V`, `V' = 2U + 3V`; with `V = 2 * pellY m` this is
exactly main's `pellX`/`pellY` recurrence. Prove by induction on `m`.
Second, square `(uvU m + uvV m √2)` via L5 to get the closed forms.
-/
theorem pellX_eq_uv (m : Nat) : pellX m = uvU (2 * m) := by
  sorry

theorem pellY_eq_uv (m : Nat) : 2 * pellY m = uvV (2 * m) := by
  sorry

/-- Closed forms. From L2 + L5 (squaring). -/
theorem pell_closed (m : Nat) :
    pellX m = uvU m * uvU m + 2 * uvV m * uvV m ∧
    pellY m = uvU m * uvV m := by
  sorry

/-- General Pell identity, for free from L2 + L1 with `2m` in place
of `m`: `(uvU (2m))^2 - 2 (uvV (2m))^2 = 1`, and
`pellX m ^ 2 - 8 * pellY m ^ 2 = 1` follows because
`pellY m = uvV (2m) / 2`. This replaces main's finite `pell_id`. -/
theorem pell_id_all (m : Nat) :
    pellX m * pellX m - 8 * pellY m * pellY m = 1 := by
  sorry

/-- Positivity of main's pair for `m ≥ 1`, from L2 + L1-positivity.
Needed before any `toNat` manipulation of `gp`. -/
theorem pell_pos {m : Nat} (hm : 1 ≤ m) : 1 ≤ pellX m ∧ 1 ≤ pellY m := by
  sorry

### L3 — the gcd computation (odd / even split)

Odd case, using L1 with norm `-1` and `pell_closed`:
`u^2 - 2v^2 = -1`, so `2v^2 = u^2 + 1`, hence
`pellX m - 1 = u^2 + 2v^2 - 1 = 2 * u^2`, and `pellY m = u * v`.
Then, in `Nat`,
`gcd (2u^2) (u v) = u * gcd (2u) v` by `Nat.gcd_mul_left`,
and `gcd (2u) v = 1` because `gcd u v = 1` (L3-coprime) and
`v` is odd (L3-parity), so `gcd 2 v = 1` and coprimality multiplies.

Even case, using L1 with norm `+1`:
`u^2 - 2v^2 = 1`, so `pellX m - 1 = 4 * v^2`, `pellY m = u * v`,
`gcd (4v^2) (u v) = v * gcd (4v) u`, and `gcd (4v) u = 1`
because `u` is odd and `gcd v u = 1`.

Both gcd steps are pure `Nat.gcd` algebra once L1–L2 are in place;
there is no analytic input here.
-/
theorem gcd_odd {m : Nat} (hm : 1 ≤ m) (hodd : m % 2 = 1) :
    Nat.gcd (pellX m - 1).toNat (pellY m).toNat = (uvU m).toNat := by
  sorry

theorem gcd_even {m : Nat} (hm : 1 ≤ m) (heven : m % 2 = 0) :
    Nat.gcd (pellX m - 1).toNat (pellY m).toNat = (uvV m).toNat := by
  sorry

### L4 — cast lemma (the only Lean-technical blocker)

`gp` is defined with `Int.toNat` and `Nat` division. Before the
gcd computation can be divided out, one needs, for `m ≥ 1`:
`(pellX m - 1).toNat` equals the `Nat` value of the closed form
(`2 * u^2` resp. `4 * v^2`), `(pellY m).toNat` equals `u * v` in `Nat`,
both gcd arguments are positive, and the gcd divides the numerator
so that `Nat.div` can be cancelled by `Nat.mul_div_cancel_left`
(or the corresponding `Nat.div_eq_of_lt_le`-free route).
This is bookkeeping with `Int.toNat_of_nonneg` and `Nat.cast_inj`;
it contains no new mathematics, but it is the step most likely to
need several attempts in Lean, because main's `gp` mixes `Int`
subtraction, `toNat`, and `Nat.gcd` in one definition.
-/
theorem gp_cast {m : Nat} (hm : 1 ≤ m) :
    (pellX m - 1).toNat =
      (if m % 2 = 1 then 2 * (uvU m).toNat ^ 2
       else 4 * (uvV m).toNat ^ 2) ∧
    (pellY m).toNat = (uvU m).toNat * (uvV m).toNat := by
  sorry

/-! ## 3. Main theorem (exact statement) -/

/-- Pell formula C1, for `m ≥ 1`, in main's own `gp`:
odd `m` gives `gp m = 2 * u m`, even `m` gives `gp m = 4 * v m`.
Proof assembly (once L1–L4 are proved): split on `m % 2`,
rewrite `gp` by its definition, rewrite numerator and gcd by
L4 + L3, cancel the gcd factor. No other input is used. -/
theorem pellC1 {m : Nat} (hm : 1 ≤ m) :
    (m % 2 = 1 → gp m = 2 * (uvU m).toNat) ∧
    (m % 2 = 0 → gp m = 4 * (uvV m).toNat) := by
  sorry

/-- Corollary, same scope. `Dm m = 2 * (pellX m - 1)` by main's
definition, so odd: `Dm m = (2u)^2 = gp m ^ 2`; even:
`Dm m = 8v^2`, hence `2 * Dm m = (4v)^2 = gp m ^ 2`.
Stated with `2 * Dm m` on the even side to stay in `Int`
without division. -/
theorem pellC1_Dm {m : Nat} (hm : 1 ≤ m) :
    (m % 2 = 1 → Dm m = (gp m : Int) ^ 2) ∧
    (m % 2 = 0 → 2 * Dm m = (gp m : Int) ^ 2) := by
  sorry

/-! ## 4. What is NOT in this draft

- No proof of any statement above is complete: every proof is `sorry`.
- No statement about `BGS-BGS-001`, `TRACE-005`, `hEquidistUnits`,
  `kickMatInf`, or RMT statistics. C1 is a finite Pell identity;
  it does not close any of those.
- No redefinition of main's objects, no change to `LineBDerand`,
  no import of the full `Bgs` aggregator (which would pull in
  unrelated modules and slow any future build).
- The `m = 0` case is deliberately excluded; see Scope.
-/

end Bgs.Breakthrough.PellC1
