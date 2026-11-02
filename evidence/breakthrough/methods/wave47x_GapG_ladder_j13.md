# Wave 47x, task D — Gap G ladder at j = 13: prediction confirmed exactly

## Verdict

**Gap G at j = 13 holds via exactly two step-64 chains of 8 with
contribution ±16 per point — the wave-47 ladder prediction is
confirmed exactly, with no deviation.** Full census over
134,217,728 points: every point has exactly two nonzero classes,
and both are the predicted step-64 chains. The ladder law
s(j) = ⌈(j−2)/2⌉ needs no correction. The ladder is now
confirmed through j = 13 (j = 9: two ±4; j = 10: one ±8;
j = 11: two ±8; j = 12: one ±16; j = 13: two ±16).

## 1. Setup (j = 13, m = p = 8192)

Q = 2^29, step0 = Q/(8p) = 8192. Grid: t odd in [1, 65536),
u = (11t + 16·U0) mod 65536, U0 in [0, 4096): 32,768 × 4,096 =
134,217,728 = 2^27 points. W[k] = y_{2k+1}; E = shift-8 digit;
reps = indices with eps = 0, phi = 0 (expected 2^{j−6} = 128,
spaced 4).

## 2. Correction to the j = 12 setup: the digit is mod 256

Naive reuse of the j = 12 code fails B2 at j = 13: the shift-8
difference W[j+8] − W[j] is divisible by Q/256 = 2^21, not Q/128
(odd multiples of 2^21 occur, e.g. point (1,0), j = 1, 3, 5).
With E = diff / 2^21 (mod 256), B2 (E mod 4 == phi mod 4)
holds everywhere, and the rep AP is mod 256 with diff divisible
by 4 and δ_E = diff/4 mod 64 odd. The cond64 condition is
unaffected (it only uses E mod 32 and δ_E mod 8):
E + 28δ_E ≡ 0 (mod 32), giving ordinals i ≡ i* (mod 8);
the 16 such ordinals split into two step-64 chains
{i*, i*+16, …, i*+112} and {i*+8, i*+24, …, i*+120},
each of 8 members, each predicted to be exactly a class
with constant t and contribution ±16.

## 3. Full census results (exact)

Fast chain census, 134,217,728 points (log
wave47x_ladder_j13_fast.log, finished 12:00, ~62 min wall):

- npoints = valid = 134,217,728; all structural checks
  0-bad: D_nondiv, eps_non01, phi_nondiv, B2_bad, reps_bad,
  spacing_bad, ap_bad, diff_non4, delta_even, E_non0mod4.
- cond64_total = 268,435,456 = exactly 2 × npoints;
  cond64_class_const = 268,435,456 (every chain is exactly
  a class with constant t); nonzero_not_cond64 = 0.
- nonzero_2 = 134,217,728: exactly two nonzero classes
  per point, no exceptions, both cond64 chains.
- chain_pos = chain_neg = 134,217,728 (equal +16/−16 chains).
- Sign pairs exactly 1:2:1: pair_nn 33,554,432,
  pair_pn 67,108,864, pair_pp 33,554,432 (as at j = 11 for
  two independent classes).
- Class sizes everywhere: (4×16, 8×6, 16×1) — 16 classes
  of size 4, 6 of size 8, 1 of size 16, total 128.
- wit_4 and share_8 everywhere; witness class size 8,
  contribution 0 everywhere — the step-16 witness still
  cancels at j = 13, as at every j ≥ 11.

## 4. Method: two censuses, and what each covers

- Full-recurrence census (`wave47x_ladder_j13.cpp`, 8193-step
  6-recurrence): checks period, minimality, ν-pattern AND all
  W-derived structure. Smoke runs: NT = 16 (65,536 points) and
  NT = 256 (1,048,576 points), ALL valid, ALL structural checks
  0-bad, cond64 exact on every point. The full 2^27 run of this
  binary was launched but stopped (VM heavily loaded, ~0.37
  cores effective) once the fast census cross-validated
  exactly — its partial progress is NOT claimed.
- Fast chain census (`wave47x_ladder_j13_fast.cpp`): W via the
  34-recurrence (z_0 = y_1, z_1 = y_3, z_{j+1} = 34z_j − z_{j−1};
  1536 steps), checking ONLY W-derived structure (reps, AP,
  B2, cond64 chains, classes, contributions, wit/share).
  Period/minimality/ν are NOT checked in this binary: they
  were validated on 1,114,112 full-recurrence points (all
  valid) and follow the proved general theory (DIV/PAR,
  wave 46) for this grid family, whose form is identical to
  the j = 12 grid (33,554,432 points, all valid).
- Cross-validation: fast NT = 16 output agrees EXACTLY with
  the full version on every W-derived counter.

## 5. Remaining gaps

- The census is exhaustive over the (m = p = 8192, ν = (1,0))
  grid, not a general proof: class-identity of step-2^s
  witness chains is census-confirmed at j = 9–13 only.
- Next testable prediction, from the ladder table (wave 47,
  task 2, §5): j = 14 (s = 6, step-64): exactly one chain of
  16 with contribution ±32.
- No Lean built, repository untouched.

## Checks

- wave47x_ladder_j13_probe.py: 200/200 points ok (probe
  section asserts reps/AP/B2/chains/classes/contribs).
- wave47x_ladder_j13.cpp: smoke NT = 16, NT = 256 (see §4).
- wave47x_ladder_j13_fast.cpp: smoke NT = 16, exact
  agreement with the full version; full run
  (134,217,728 points) log: wave47x_ladder_j13_fast.log,
  finished 12:00.
