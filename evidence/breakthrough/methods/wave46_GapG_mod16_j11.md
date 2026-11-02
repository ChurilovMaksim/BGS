# Wave 46, task 4 — Mod-16 digit at j ≥ 11: step-16 witness proved, but it cancels; Gap G at j = 11 via step-32

## Verdict

- Step-16 witness existence (wave 45 §7's remaining step): **proved in general**,
  modulo DIV, PAR, ψ-analysis, slope lemma, B2 — exactly 4 witness ordinals
  per point; confirmed exhaustively at j = 11 (8,388,608 points, wit_4).
- **Obstruction**: the step-16 witness does **not** give Gap G at j = 11: the
  witness reps chain into the size-8 class with t-pattern
  (t,t,1−t,1−t,t,t,1−t,1−t), contribution 0 — exhaustive
  (wit_class_nonzero = 0). Wave 45 §7's implication "witness ⟹ Gap G"
  holds at j = 9, 10 only because the witness chain there is short.
- Gap G at j = 11: **holds via step-32 witnesses** — exactly two step-32
  chains per point satisfy E + 12δ_E ≡ 0 (mod 16); each is exactly a class
  of size 4 with constant t, contribution ±8, signs independent (1:2:1).
  Full census: every point has exactly two nonzero classes.
- Ladder conjecture (§4): operative witness step s(j) = ⌈(j−2)/2⌉;
  sharp prediction at j = 12: one step-32 chain of 8, contribution ±16.

## 1. Step-16 witness lemma (general j)

Setup (wave 45 §0–§1, §6): reps r_i = r_0 + 4i, i < 2^{j−6};
E = shift-8 digit mod 2^{j−5}; S_i := E_{r_i} + 4δ_E.
Sharing (step-16 pair in one class) ⟺ S_i ≡ 0 (mod 2^{j−7});
witness (t-equality) ⟺ S_i ≡ 0 (mod 2^{j−6}).
(a) E_{r_i} ≡ 0 (mod 4): B2 (E ≡ φ mod 4, φ = 0 on reps).
(b) Rep-AP: E_{r_{i+1}} − E_{r_i} = 4δ_E, δ_E odd (slope lemma).
(c) S_i = S_0 + 4iδ_E. Solve S_i ≡ 0 (mod 2^{j−6}): divide by 4
(valid by (a)): iδ_E ≡ −S_0/4 (mod 2^{j−8}); δ_E odd ⟹ invertible,
so i ≡ i* (mod 2^{j−8}): exactly 4 solutions in [0, 2^{j−6}). ∎
Each is a sharing pair with t-equality (witness ⟹ sharing).
Standing hypotheses: DIV, PAR, ψ-analysis (rep count/spacing),
slope lemma (δ_E odd), B2. No Lean built, repository untouched.

Correction to wave 45 §1: the AP E_k ≡ E_0 + kδ_E holds mod 2^{j−6},
not mod 2^{j−5}: consecutive diffs are δ_E or δ_E + 32 (dd32_bad = 0
exhaustively at j = 11, i.e. consecutive diffs mod 32 are constant).
The rep-AP mod 2^{j−5} is exact because the four 32-bits in each
block of 4 sum to an even number. Only the rep-AP is used above.

## 2. Why the witness cancels at j = 11

Along a step-16 chain (ordinals ≡ c mod 4), S_{i+4} = S_i + 16δ_E.
At j = 11 the witness modulus is 32 and 16δ_E ≡ 16 (mod 32), so
t-equality holds at every other 16-link only: the 8-chain has
t-pattern (t,t,1−t,1−t,t,t,1−t,1−t), contribution 0. The 4
witness reps of every point lie in this big class (size 8).
General moral: the lemma of §1 controls existence, not the class
contribution — at j ≥ 11 the witness chain is long enough for the
t-equality to alternate, so Gap G needs the step-2^s analysis, not
the step-16 witness alone. (At j ≥ 12 the 16-links themselves stop
sharing for most ℓ, so the chain structure changes again; §4.)

## 3. Step-32 witness at j = 11 (Gap G)

32-step: w_{k+32} − w_k = μ_3(4E_k + 48δ_E) (sum of 4 consecutive
8-steps). T-equality ⟺ 4E_k + 48δ_E ≡ 0 (mod 64)
⟺ E_k + 12δ_E ≡ 0 (mod 16). Along a 32-chain (ordinals ≡ c mod 8),
E + 12δ_E (mod 16) is constant (32-step changes E by 32δ_E ≡ 0
mod 16). Counting: E_i + 12δ_E = E_0 + 4(i+3)δ_E ≡ 0 (mod 16)
⟺ i ≡ i* (mod 4) (E_0 ≡ 0 mod 4, δ_E odd) ⟹ 8 ordinals =
exactly 2 chains of 4. Each such chain: consecutive 32-links share
(condition mod 16 ⟹ mod 8 sharing) and are t-equal, so it
contributes ±8. Census confirms each is exactly a class
(cond32_class_const = 16,777,216 = 2 per point;
nonzero_not_cond32 = 0). Hence every point has exactly two
nonzero classes: Gap G at j = 11. Signs independent, 1:2:1
(2,097,152 / 4,194,304 / 2,097,152).

## 4. Ladder conjecture for general j (open, testable)

General s-step: w_{k+2^s} − w_k = μ_3·n(E_k + 4(n−1)δ_E),
n = 2^{s−3}; t-equality ⟺ E_k + 4(n−1)δ_E ≡ 0 (mod 2^{j−s−2}).
The condition is constant along s-chains iff 2s ≥ j−2; the
minimal such s is s(j) = ⌈(j−2)/2⌉ (j = 9, 10 → 4; j = 11 → 5).
Counting as in §3, the number of t-equal s(j)-chains is
2^{2s−j+2} (1 or 2), each of length 2^{j−s−4}. Prediction at
j = 12 (s = 5): exactly one step-32 chain of 8 members,
contribution ±16. Open at general j: class-identity of witness
chains (census-confirmed at j = 11 only) and the standing
hypotheses DIV, PAR, ψ-analysis, B2 in general form.

## Checks

- wave46_mod16_j11_probe.py: 4096 sampled points, all valid;
  reps_32 spaced 4; rep-AP exact; δ_E odd; E ≡ 0 mod 4;
  wit_4, share_8; sizes (4,4,4,4,4,4,8); nonzero class always.
- wave46_mod16_j11.cpp + wave46_mod16_j11.log: full census,
  8,388,608 points, all valid (bad_period/bad_min/bad_nu = 0);
  D_nondiv = eps_non01 = phi_nondiv = B2_bad = 0; reps_bad =
  spacing_bad = ap_bad = diff_non4 = delta_even = E_non0mod4 =
  dd32_bad = 0; wit_4, share_8 everywhere; sizes
  (4,4,4,4,4,4,8) everywhere; contribs (−8,−8,0,0,0,0,0) ×
  2,097,152, (−8,0,0,0,0,0,8) × 4,194,304,
  (0,0,0,0,0,8,8) × 2,097,152; wit_class_nonzero = 0,
  wit_class_notsize8 = 0; cond32_total = cond32_class_const =
  16,777,216; nonzero_not_cond32 = 0.
