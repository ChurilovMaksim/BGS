/-! BREAKTHROUGH DRAFT — research record, not a theorem.
    Source: BGS breakthrough program (Nov 2026), wave notes in evidence/breakthrough/methods/.
    Status: draft, not built in this form; statement draft only.
    Not imported by formalization/Bgs.lean. Registry status unchanged. -/

/-!
# DRAFT ONLY — NOT A PROOF, NOT FOR MAIN

File: `bgs-breakthrough/lean-drafts/LineBRadicalDraft.lean`
Task: wave 4, task 2 — draft Lean lemma for the full radical lemma
`rad (D_m) = rad (g'_m)`, `m ≥ 1`.
Revision (wave 8, task 4): Mathlib API fixes applied from
`MathlibAPIVerification_Radical.md` (wave 6, task 4, Mathlib v4.33.1);
pre-fix version kept as `LineBRadicalDraft_v1_preAPIfix.lean`.
The mathematical content is unchanged; only statements, names,
and imports were corrected to the API actually present.

Status: text draft only. `lake build` was NOT run (forbidden for this task),
no file in the repository was touched, nothing was pushed to `main`.
Every `sorry` below is an explicit placeholder, not a claim:
this file must not be cited as proved, and must not enter `main`
until every `sorry` is replaced and the axiom audit is clean
(standard axioms only, `sorryAx = 0`).

## Verified source (current main, via GitHub connector only)

- Repository: `ChurilovMaksim/BGS`, branch `main`,
  HEAD `d87dce0d9277579568edfee6cffecbc96ea61024` (PR #76),
  re-verified in wave 8, task 4 via the GitHub connector
  (previously pinned at `6dbcc7a0ed38d780ff7643bdb55917a9bc5efed1`,
  PR #75; the file is byte-identical between the two HEADs).
- `formalization/Bgs/LineBDerand.lean`, blob SHA
  `01fa6e63551542de55cce52cb9fb54c660f89b54`, read with
  `get_file_contents` at the new ref. Definitions used verbatim:
  - `pellX : Nat → Int`, `pellY : Nat → Int`, mutually recursive:
    `pellX 0 = 1`, `pellX (n+1) = 3 * pellX n + 8 * pellY n`,
    `pellY 0 = 0`, `pellY (n+1) = pellX n + 3 * pellY n`.
  - `Dm m = 2 * (pellX m - 1)` (an `Int`).
  - `gp m = (pellX m - 1).toNat / Nat.gcd (pellX m - 1).toNat (pellY m).toNat`.
  - `pell_id` in main is only a finite `decide` check for `m < 30`;
    the general norm identity is Lemma `pell_norm` below, proved
    (in the intended proof) by induction, not imported from main.
- Numerical grounding (exact integers, NOT a proof; it only fixes
  the statement): `rad (D_m) = rad (g'_m)` and the `v2` formulas of
  §4 were checked for `m = 1..30` before this draft was written.
  A numerical check never replaces the lemmas below.

## Relation to the Pell C1 draft

This draft does NOT import or reuse
`bgs-breakthrough/lean-drafts/LineBPellC1Draft.lean`, and it must
not be made to depend on it:
- That draft is not in main and not on any lake import path, so an
  `import` of it would not elaborate in the project at all.
- Mathematically it is unnecessary here. C1 introduces the pair
  `(u, v)` for `(1 + √2)^m` and proves closed forms
  `pellX = u^2 + 2v^2`, `pellY = u * v` in order to compute the
  VALUE of `gp` (`2u` / `4v`). The radical lemma needs only the
  PRIME SUPPORT of `gp`, and that follows from the `pellX`/`pellY`
  recurrence plus the norm alone — strictly weaker input.
- The one shared statement is the norm `pellX^2 - 8 * pellY^2 = 1`
  (C1's `pell_id_all`). This draft re-proves it directly by a
  3-line induction + `ring`, so that the two drafts stay
  independent; if C1 is ever completed, its norm lemma could
  replace §2 here, but nothing else from C1 is needed.
- C1's `gp_cast` lemma (the `Int.toNat` / division bookkeeping for
  the value of `gp`) is also not reused: §1 below proves its own,
  smaller cast lemmas, only for `A = (x-1).toNat`, `B = y.toNat`,
  `C = (x+1).toNat` and for `(Dm m).toNat`. The cast bridge is
  still the fiddliest part of this draft (see §6), but it is a
  different, smaller bridge than C1's.

## Scope

- `m ≥ 1` only. `m = 0` is excluded on purpose: `pellY 0 = 0`,
  `pellX 0 - 1 = 0`, `gp 0 = 0 / 0 = 0` in `Nat`, and the radical
  statement degenerates. The draft does not try to rescue `m = 0`.
- `Nat.radical` does NOT exist in Mathlib v4.33.1 (whole-Mathlib
  grep in wave 6, task 4: only `Ideal.radical`,
  `QuadraticForm.radical`, etc.). The main theorem is therefore
  stated in §5 as the primeFactors equality `primeFactors_eq`
  (equivalent content, not weaker), plus a locally defined
  product `rad` and its corollary `rad_eq`. The mathematical
  content is the prime-divisor equivalence `prime_dvd_iff` of §5,
  from which any reasonable `rad` definition follows by the same
  `Finset` argument. Do not silently change the statement to a
  weaker one (e.g. only one divisibility direction) to fit an API.

## Notation in this draft

Throughout, for fixed `m`:
- `x := pellX m`, `y := pellY m` (in `Int`).
- `A := (pellX m - 1).toNat`, `B := (pellY m).toNat`,
  `C := (pellX m + 1).toNat` (in `Nat`).
- `Dnat := (Dm m).toNat`; §1 proves `Dnat = 2 * A`.
- `v p n` abbreviates `Nat.factorization n p` in comments; in code
  it is written out.
-/

-- Import path (verified against main at d87dce0, wave 8, task 4):
-- the aggregator line is `import Bgs.LineBDerand` (flat module
-- name, file `formalization/Bgs/LineBDerand.lean`), while the
-- NAMESPACE inside that file is `Bgs.LineB.Derand` — so the
-- `open` line below keeps the dotted form. The v1 draft wrote
-- `import Bgs.LineB.Derand`, which is not a module path and
-- would not elaborate. `LineBDerand` itself imports nothing
-- (core Lean only), so the factorization / primeFactors
-- imports below are NOT transitive and must be explicit.
import Bgs.LineBDerand
import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Data.Nat.PrimeFin

namespace Bgs.Breakthrough.Radical

open Bgs.LineB.Derand

/-! ## 1. Positivity and the Int → Nat cast bridge

Everything in `LineBDerand` is stated in `Int`, everything about
factorization and `rad` lives in `Nat`. The lemmas of this section
are the bridge, and they are the first place elaboration is
expected to need several attempts (see §6, point 1). No new
mathematics happens here: only `Int.toNat_of_nonneg`,
`Int.toNat_mul` / `Int.toNat_add` under nonnegativity,
`Int.toNat_pow_of_nonneg` (note: NOT plain `Int.toNat_pow`)
for the `B ^ 2` cast, and `Nat.cast_inj` (with explicit
`R := ℤ`) in the reverse direction. All names verified
against Lean core v4.33.1 in wave 6, task 4.
-/

/-- For `m ≥ 1` the Pell pair is strictly positive in the sense
needed below. Induction on `m`, using the recurrence; the step
preserves `x ≥ 3` and `y ≥ 1` once they hold at `m = 1`. -/
theorem pell_pos_ge {m : Nat} (hm : 1 ≤ m) : 3 ≤ pellX m ∧ 1 ≤ pellY m := by
  sorry

/-- Immediate consequences: `x - 1 ≥ 2`, `x + 1 ≥ 4`, `y ≥ 1`. -/
theorem pell_pos_aux {m : Nat} (hm : 1 ≤ m) :
    2 ≤ pellX m - 1 ∧ 4 ≤ pellX m + 1 ∧ 1 ≤ pellY m := by
  sorry

/-- The `Nat` shadows satisfy the same multiplicative identity as
the `Int` pair. This is the cast of `factor_eq` (§2) to `Nat`:
`A * C = 8 * B ^ 2`, with `A + 2 = C` as a `Nat` identity.
Proof idea: rewrite `A`, `B`, `C` by `Int.toNat` of the `Int`
identity, using nonnegativity from `pell_pos_aux` to push `toNat`
through multiplication and addition; `A + 2 = C` because
`(x + 1) - (x - 1) = 2` in `Int` and both sides are nonnegative. -/
theorem factor_eq_nat {m : Nat} (hm : 1 ≤ m) :
    (pellX m - 1).toNat * (pellX m + 1).toNat
      = 8 * (pellY m).toNat ^ 2 ∧
    (pellX m - 1).toNat + 2 = (pellX m + 1).toNat := by
  sorry

/-- `(Dm m).toNat = 2 * A`. From `Dm m = 2 * (pellX m - 1)` and
`pellX m - 1 ≥ 0`, by `Int.toNat_mul` / `Int.toNat_ofNat`. -/
theorem Dm_toNat {m : Nat} (hm : 1 ≤ m) :
    (Dm m).toNat = 2 * (pellX m - 1).toNat := by
  sorry

/-- Positivity in `Nat`: `A ≥ 2`, `B ≥ 1`, `C ≥ 4`, hence
`A ≠ 0`, `B ≠ 0`, `C ≠ 0`, `gp m ≠ 0`, `(Dm m).toNat ≠ 0`.
`gp m ≠ 0` needs `Nat.div_pos`: `gcd A B ≤ A` and `A > 0`, so
`A / gcd A B > 0`. Shorter verified shortcut (core v4.33.1):
`Nat.div_gcd_pos_of_pos_left` gives `0 < A / A.gcd B`
directly from `0 < A`. These nonvanishing facts are side conditions
for every `Nat.factorization_*` lemma used later (except
`Nat.factorization_div`, which needs only `d ∣ n` — see §5);
they must be discharged explicitly, not left implicit. -/
theorem nat_pos {m : Nat} (hm : 1 ≤ m) :
    2 ≤ (pellX m - 1).toNat ∧ 1 ≤ (pellY m).toNat ∧
    4 ≤ (pellX m + 1).toNat ∧ 0 < gp m ∧ 0 < (Dm m).toNat := by
  sorry

/-! ## 2. Norm and parity / mod-4 facts (in `Int`)

These are the only genuinely arithmetic inputs. All of them are
one-step inductions; none of them needs the `(u, v)` pair.
-/

/-- Norm. Induction on `m`. Step, with `x' = 3x + 8y`,
`y' = x + 3y`: `(x')^2 - 8 (y')^2 = x^2 - 8 y^2` by `ring`,
so the induction hypothesis gives `1`. Base `m = 0`: `1 - 0 = 1`. -/
theorem pell_norm (m : Nat) :
    pellX m * pellX m - 8 * pellY m * pellY m = 1 := by
  sorry

/-- Factored form of the norm, in `Int`. Immediate from
`pell_norm` by `ring`-normalisation:
`(x - 1)(x + 1) = x^2 - 1 = 8 y^2`. -/
theorem factor_eq {m : Nat} :
    (pellX m - 1) * (pellX m + 1) = 8 * pellY m * pellY m := by
  sorry

/-- `x` is always odd. Induction: base `x 0 = 1`; step
`3x + 8y` is odd when `x` is odd, since `8y` is even.
Stated with `Odd` so that `Int.ModEq` steps below can use it. -/
theorem pellX_odd (m : Nat) : Odd (pellX m) := by
  sorry

/-- Parity of `y`: `y_m ≡ m (mod 2)`. Induction: the step is
`y' = x + 3y ≡ 1 + y (mod 2)` because `x` is odd (by
`pellX_odd`) and `3 ≡ 1 (mod 2)`. In particular `y` is odd
iff `m` is odd, and even iff `m` is even. -/
theorem pellY_parity (m : Nat) :
    pellY m % 2 = (m : Int) % 2 := by
  sorry

/-- `x` mod 4. Induction: `x' = 3x + 8y ≡ 3x (mod 4)` since
`8y ≡ 0 (mod 4)`, so `x_m ≡ 3^m (mod 4)` by induction.
Stated as `Int.ModEq` so the corollaries can be read off
without redoing the induction. -/
theorem pellX_mod4 (m : Nat) : pellX m ≡ 3 ^ m [ZMOD 4] := by
  sorry

/-- Corollaries of `pellX_mod4`, split by parity of `m`.
Odd `m`: `3^m ≡ 3 (mod 4)`; even `m`: `3^m ≡ 1 (mod 4)`.
Both are inductions on the parity form of `m` (or a two-step
induction on `m`); do not prove them by `decide` for fixed `m`. -/
theorem pellX_mod4_odd {m : Nat} (hodd : m % 2 = 1) :
    pellX m % 4 = 3 := by
  sorry

theorem pellX_mod4_even {m : Nat} (heven : m % 2 = 0) :
    pellX m % 4 = 1 := by
  sorry

/-! ## 3. Factorization of the norm identity at a prime

Fix a prime `p`. Write `a := (A).factorization p`,
`b := (C).factorization p`, `t := (B).factorization p`,
where `A, B, C` are the `Nat` shadows of §1. The point of this
section is that the norm identity becomes an additive identity
of exponents, and that `a` and `b` cannot both be positive when
`p` is odd.
-/

/-- Exponent form of `factor_eq_nat`. For every prime `p`,
`a + b = (if p = 2 then 3 else 0) + 2 * t`.
Proof idea: apply `Nat.factorization` to both sides of
`A * C = 8 * B^2`, using `Nat.factorization_mul` (needs
`A ≠ 0`, `C ≠ 0`, `B ≠ 0` from `nat_pos`) and
`Nat.factorization_pow` (no side conditions). Both names
verified in Mathlib v4.33.1 (wave 6, task 4); they are
`Finsupp` equalities, so the pointwise form at `p` needs
`Finsupp.add_apply` and `Finsupp.smul_apply` + `smul_eq_mul`.
The factorization of `8` at `p` is `3` at `p = 2` and `0`
elsewhere, via `8 = 2^3`: at `p = 2`,
`Nat.factorization_pow_self`; at `p ≠ 2`,
`Nat.factorization_eq_zero_of_not_dvd` (since `p ∣ 2^3`
would give `p ∣ 2`, hence `p = 2`). -/
theorem factor_exponents {m : Nat} (hm : 1 ≤ m) {p : Nat} (hp : p.Prime) :
    Nat.factorization (pellX m - 1).toNat p +
      Nat.factorization (pellX m + 1).toNat p
    = (if p = 2 then 3 else 0) +
      2 * Nat.factorization (pellY m).toNat p := by
  sorry

/-- For odd `p`, `a` and `b` are not both positive.
Proof idea: if `p ∣ A` and `p ∣ C`, then `p ∣ C - A` in `Nat`,
and `C - A = 2` by `factor_eq_nat` (`C = A + 2`), so `p ∣ 2`,
contradicting `p` odd prime (hence `p ≥ 3`); the step
`p ∣ 2 → p = 2` is `Nat.prime_dvd_prime_iff_eq` with
`Nat.prime_two`. In factorization language: `min a b = 0`.
The `Nat` subtraction here is safe because `C = A + 2 ≥ A`;
do not write it as an `Int` subtraction without the cast.
Flag (wave 6, task 4): the name `Nat.dvd_sub'` for the
`p ∣ C - A` step was NOT re-grepped line-by-line; if it
fails, use the fully confirmed alternative route via
`Nat.factorization_le_iff_dvd` instead. -/
theorem not_both_pos {m : Nat} (hm : 1 ≤ m) {p : Nat}
    (hp : p.Prime) (hp2 : p ≠ 2) :
    Nat.factorization (pellX m - 1).toNat p = 0 ∨
    Nat.factorization (pellX m + 1).toNat p = 0 := by
  sorry

/-- Consequence for odd `p`: the exponent identity collapses.
If `a > 0` then `b = 0` by `not_both_pos`, so
`a = 2 * t` from `factor_exponents`. If `a = 0` nothing is
claimed here (the case `b = 2 * t` is symmetric and is not
needed for the radical lemma, since only `a` feeds `gp`). -/
theorem odd_exponent {m : Nat} (hm : 1 ≤ m) {p : Nat}
    (hp : p.Prime) (hp2 : p ≠ 2)
    (ha : 0 < Nat.factorization (pellX m - 1).toNat p) :
    Nat.factorization (pellX m - 1).toNat p
      = 2 * Nat.factorization (pellY m).toNat p := by
  sorry

/-! ## 4. The 2-adic computation

This is the part of the wave-3 sketch that was new (the odd-prime
case was already known). It is also the part where a `Nat`
factorization value has to be extracted from a congruence, which
is a real Lean step, not bookkeeping (see §6, point 3).
-/

/-- The minimum of the two 2-adic exponents is exactly 1.
Proof idea: `x` is odd, so exactly one of `x - 1`, `x + 1` is
`≡ 2 (mod 4)` and the other is `≡ 0 (mod 4)`. In `Nat` terms:
from `pellX_mod4_odd` / `pellX_mod4_even`, one of `A, C` is
`2 mod 4` (hence has 2-adic exponent exactly 1) and the other
is `0 mod 4` (hence has exponent `≥ 2`, in particular `≥ 1`).
The congruence-to-exponent conversion is the hard step here:
a number `≡ 2 (mod 4)` is `2 * (odd)`, so its factorization
at `2` is `1`; a number `≡ 0 (mod 4)` is divisible by `4`,
so its factorization at `2` is `≥ 2`. State these two
conversions as separate helper lemmas when elaborating, rather
than burying them in this proof. Verified routes (wave 6,
task 4): the `Int` congruences of §2 reach `Nat` via
`Int.natCast_mod` (`((m % n : ℕ) : ℤ) = (m : ℤ) % (n : ℤ)`).
Route A (as above): `n % 4 = 2` gives `n = 2 * k` with `k`
odd, then `Nat.factorization_mul` + `Nat.Prime.factorization`
for `2` + `Nat.factorization_eq_zero_of_not_dvd` for `k`.
Route B (shorter, recommended): `Nat.Prime.pow_dvd_iff_le_factorization`
gives `2 ∣ n → 1 ≤ factorization n 2` and
`¬ 4 ∣ n → ¬ 2 ≤ factorization n 2`, hence `= 1` by
antisymmetry; likewise `n % 4 = 0` gives `4 ∣ n`, hence
`2 ≤ factorization n 2`. -/
theorem v2_min {m : Nat} (hm : 1 ≤ m) :
    min (Nat.factorization (pellX m - 1).toNat 2)
        (Nat.factorization (pellX m + 1).toNat 2) = 1 := by
  sorry

/-- Exact 2-adic exponent of `A`, by parity of `m`.
Odd `m`: `x ≡ 3 (mod 4)`, so `A = x - 1 ≡ 2 (mod 4)`,
hence `a = 1` (and, from §2, `y` is odd, so `t = 0`).
Even `m`: `x ≡ 1 (mod 4)`, so `C ≡ 2 (mod 4)`, hence
`b = 1`; the exponent identity at `p = 2` gives
`a + 1 = 3 + 2 * t`, i.e. `a = 2 + 2 * t`.
In both cases the conclusion is stated uniformly as an
equation for `a` in terms of `t`, so §5 can use it without
re-splitting on parity. -/
theorem v2_A {m : Nat} (hm : 1 ≤ m) :
    (m % 2 = 1 →
      Nat.factorization (pellX m - 1).toNat 2 = 1 ∧
      Nat.factorization (pellY m).toNat 2 = 0) ∧
    (m % 2 = 0 →
      Nat.factorization (pellX m - 1).toNat 2
        = 2 + 2 * Nat.factorization (pellY m).toNat 2) := by
  sorry

/-- Corollary used in §5: in all cases `a > t`, i.e. the
2-adic exponent of `A` strictly exceeds that of `B`.
Odd `m`: `1 > 0`. Even `m`: `2 + 2t > t` for all `t ≥ 0`.
This strict inequality is exactly what makes `2 ∣ gp`. -/
theorem v2_A_gt {m : Nat} (hm : 1 ≤ m) :
    Nat.factorization (pellY m).toNat 2 <
    Nat.factorization (pellX m - 1).toNat 2 := by
  sorry

/-! ## 5. From exponents to `gp` to `rad`

The bridge from §3–§4 to `gp` is one factorization lemma:
factorization commutes with `gcd` (as `min`) and with division
by a divisor (as subtraction of exponents). After that, the
prime-divisor equivalence is a case split on `p = 2` vs `p`
odd, and `rad` equality is a `Finset` argument on
`primeFactors`.
-/

/-- Factorization of `gp` at any prime.
`gp m = A / Nat.gcd A B`, `Nat.gcd A B ∣ A`, so factorization
of the quotient is factorization of `A` minus factorization
of the gcd, and factorization of the gcd is the pointwise
`min` of the factorizations. Hence, for every prime `p`,
`factorization (gp m) p = a - min a t` (Nat subtraction,
which is exact here because `min a t ≤ a`).
Verified names (Mathlib v4.33.1, wave 6, task 4):
`Nat.factorization_div` needs ONLY `Nat.gcd_dvd_left A B`
(no nonvanishing hypotheses at all — the v1 comment claiming
otherwise was inaccurate); `Nat.factorization_gcd` needs
`A ≠ 0`, `B ≠ 0` from `nat_pos`; pointwise steps are
`Finsupp.tsub_apply` and `Finsupp.inf_apply`, with `⊓` on
`ℕ` definitionally `min` (close with `simp`/`rfl`; no
standalone `⊓ = min` lemma was verified, so do not cite
one unchecked). -/
theorem gp_factorization {m : Nat} (hm : 1 ≤ m) {p : Nat} (hp : p.Prime) :
    Nat.factorization (gp m) p
      = Nat.factorization (pellX m - 1).toNat p -
        min (Nat.factorization (pellX m - 1).toNat p)
            (Nat.factorization (pellY m).toNat p) := by
  sorry

/-- Prime-divisor equivalence: the mathematical heart of the
radical lemma. For every prime `p`,
`p ∣ gp m ↔ p ∣ (Dm m).toNat`.
Proof idea, using `Nat.Prime.dvd_iff_one_le_factorization`
(`p.Prime → n ≠ 0 → (p ∣ n ↔ 1 ≤ factorization n p)`,
Mathlib v4.33.1 — there is NO lemma called
`Nat.factorization_pos`; `1 ≤ _` is `0 < _` by `omega`)
for `n ≠ 0` (both sides are nonzero by `nat_pos`),
together with `Dm_toNat`
(`(Dm m).toNat = 2 * A`, so for `p ≠ 2`, `p ∣ Dnat ↔ p ∣ A`,
and for `p = 2`, `2 ∣ Dnat` trivially):
- Forward: if `p ∣ gp m` then `factorization (gp m) p > 0`,
  so by `gp_factorization`, `a > min a t`, hence `a > 0`,
  hence `p ∣ A`, hence `p ∣ Dnat`.
- Backward, `p` odd: if `p ∣ Dnat` then `p ∣ A`, so `a > 0`,
  so by `odd_exponent`, `a = 2 * t`, hence `t > 0` (else
  `a = 0`) and `a - min a t = t > 0`, so `p ∣ gp m`.
- Backward, `p = 2`: `2 ∣ Dnat` always; `v2_A_gt` gives
  `a > t`, so `a - min a t > 0`, so `2 ∣ gp m`.
No other case is needed. Note the asymmetry: the forward
direction is uniform in `p`; the backward direction is where
the Pell input (`odd_exponent`, `v2_A_gt`) enters. -/
theorem prime_dvd_iff {m : Nat} (hm : 1 ≤ m) {p : Nat} (hp : p.Prime) :
    p ∣ gp m ↔ p ∣ (Dm m).toNat := by
  sorry

/-- Main theorem (restated, wave 8, task 4): primeFactors
equality, for `m ≥ 1`. This is the exact content of the v1
`radical_eq`, with `Nat.radical` — which does not exist in
Mathlib v4.33.1 — removed, not weakened: the two numbers
have the same prime divisors, hence the same primeFactors
finset, hence the same product over it.
Proof idea: for `n ≠ 0`,
`p ∈ n.primeFactors ↔ p.Prime ∧ p ∣ n` via
`Nat.mem_primeFactors_of_ne_zero` (use this form, not
`Nat.mem_primeFactors`, whose statement carries an extra
`n ≠ 0` conjunct). So `primeFactors (gp m)` and
`primeFactors (Dm m).toNat` are equal as finsets by
`Finset.ext` plus `prime_dvd_iff` (both numbers are nonzero
by `nat_pos`). -/
theorem primeFactors_eq {m : Nat} (hm : 1 ≤ m) :
    (gp m).primeFactors = (Dm m).toNat.primeFactors := by
  sorry

/-- Local radical: product over primeFactors, written
notation-free (`Finset.prod ... id`) so no `BigOperators`
scope question arises at elaboration. This is the definition
the v1 `radical_eq` proof idea assumed for `Nat.radical`. -/
def rad (n : Nat) : Nat := n.primeFactors.prod id

/-- Corollary of `primeFactors_eq`: the local radicals agree.
By `congrArg` from `primeFactors_eq` (products over equal
finsets are equal). -/
theorem rad_eq {m : Nat} (hm : 1 ≤ m) :
    rad (Dm m).toNat = rad (gp m) := by
  sorry

/-! ## 6. What is genuinely hard in Lean (not just tedious)

1. **The Int → Nat cast bridge (§1).** `gp` mixes `Int`
   subtraction, `Int.toNat`, and `Nat.gcd` / `Nat` division in a
   single definition, and every factorization lemma lives in
   `Nat` while every recurrence lives in `Int`. The bridge
   lemmas `factor_eq_nat`, `Dm_toNat`, `nat_pos` contain no new
   mathematics, but they are the step most likely to need
   several elaboration attempts — the same class of blocker as
   the `gp_cast` lemma in the Pell C1 draft, though smaller in
   scope (only `A, B, C` and `Dnat`, not the value of `gp`).
2. **Factorization API names and side conditions (§3, §5) —
   RESOLVED in wave 6, task 4, applied in wave 8, task 4.**
   `Nat.factorization_mul` (needs `A ≠ 0`, `C ≠ 0`),
   `Nat.factorization_pow` (no side conditions),
   `Nat.factorization_gcd` (needs `A ≠ 0`, `B ≠ 0`),
   `Nat.factorization_div` (needs ONLY `d ∣ n`, via
   `Nat.gcd_dvd_left` — no nonvanishing hypotheses),
   `Nat.Prime.dvd_iff_one_le_factorization` (replacing the
   nonexistent `Nat.factorization_pos`), `Nat.mem_primeFactors_of_ne_zero`,
   and the pointwise steps `Finsupp.add_apply`,
   `Finsupp.smul_apply`, `Finsupp.inf_apply`,
   `Finsupp.tsub_apply` all exist in Mathlib v4.33.1 with
   exactly these statements. Remaining micro-flags, not
   mathematical gaps: `⊓` on `ℕ` is definitionally `min`
   (close with `simp`/`rfl`; no standalone lemma verified),
   and `Nat.dvd_sub'` in `not_both_pos` was not re-grepped
   line-by-line (confirmed alternative via
   `Nat.factorization_le_iff_dvd` exists).
3. **Congruence → factorization value (§4) — helper
   RESOLVED to a few lines in wave 6, task 4.** Converting
   "`A ≡ 2 (mod 4)`" into "`factorization A 2 = 1`" (and
   "`C ≡ 0 (mod 4)`" into "`factorization C 2 ≥ 2`") still
   needs a helper lemma, but it is short: either the
   `2 * odd` factorisation route, or the shorter route via
   `Nat.Prime.pow_dvd_iff_le_factorization` (see the `v2_min`
   comment). No new mathematical input is needed.
4. **Not hard, only tedious:** the norm and parity/mod-4
   inductions (§2, `induction` + `ring` / `Int.ModEq`); the
   `not_both_pos` argument (a common divisor of `A` and `C`
   divides `2`); the final `Finset.ext` assembly for `rad`
   (§5, standard once `prime_dvd_iff` is in place).

## 7. What is NOT in this draft

- No proof of any statement above is complete: every proof is
  `sorry`.
- No statement about `BGS-BGS-001`, `TRACE-005`, `hEquidistUnits`,
  `kickMatInf`, or RMT statistics. The radical lemma is a finite
  Pell / divisor statement; it is one input to `hEquidistUnits`
  (it gives `hCoprime`: `N` coprime to `D_m` iff coprime to
  `g'_m`), not a closure of any of those claims.
- No redefinition of main's objects, no change to `LineBDerand`,
  no import of the full `Bgs` aggregator, no import of the
  Pell C1 draft (see the header: that would not elaborate and
  is mathematically unnecessary).
- The `m = 0` case is deliberately excluded; see Scope.
-/

end Bgs.Breakthrough.Radical
