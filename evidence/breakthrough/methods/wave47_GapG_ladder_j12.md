# Wave 47, task 2 — Gap G ladder at j = 12: prediction confirmed, no correction

## Verdict

**Gap G at j = 12 holds via exactly one step-32 chain of 8 with
contribution ±16 per point — the wave-46 ladder prediction is
confirmed exactly, with no deviation.** Full census over
33,554,432 points: every point has exactly one nonzero class,
and it is the predicted step-32 chain. The ladder law
s(j) = ⌈(j−2)/2⌉ needs no correction. DIV and PAR are proved
in general (wave 46, task 3) and are not open here.

## 1. Setup (j = 12, m = p = 4096)

Q = 2^27, step0 = Q/(8p) = 4096. Grid: t odd in [1, 32768),
u = (11t + 16·U0) mod 32768, U0 in [0, 2048): 16,384 × 2,048 =
33,554,432 = 2^25 points. W[k] = y_{2k+1} (k < 1024); E = shift-8
digit mod 128; reps = indices with eps = 0, phi = 0. Per point:
64 reps spaced 4; E along reps is an AP with diff 4δ_E,
δ_E odd; E ≡ 0 mod 4 on reps (B2). All structural checks
(period, minimality, ν-pattern, divisibility, B2, rep-AP)
are 0-bad over the whole census.

## 2. Why one chain of 8 is predicted

Step-32 (s = 5, n = 4): t-equality ⟺ 4(E_k + 12δ_E) ≡ 0
(mod 128) ⟺ E_k + 12δ_E ≡ 0 (mod 32). The condition is
constant along 32-chains: a 32-step changes E by 32δ_E ≡ 0
mod 32 (boundary case 2s = 10 = j−2). Along reps,
E_i + 12δ_E = E_0 + 4(i+3)δ_E ≡ 0 (mod 32) ⟺
E_0/4 + (i+3)δ_E ≡ 0 (mod 8) ⟺ i ≡ i* (mod 8)
(δ_E odd, E_0 ≡ 0 mod 4). Among 64 ordinals this gives
exactly 8 solutions — one residue class mod 8, i.e. one
chain of 8 members. The census tests the two things the
counting does not give: the chain is exactly a class, and
its t is constant (so the contribution is ±16, not 0).

## 3. Census results (exact)

- npoints = valid = 33,554,432; bad_period = bad_min =
  bad_nu = D_nondiv = eps_non01 = phi_nondiv = B2_bad = 0;
  reps_bad = spacing_bad = ap_bad = diff_non4 =
  delta_even = E_non0mod4 = 0.
- cond32_total = 33,554,432 (exactly one chain per point);
  cond32_class_const = 33,554,432 (every chain is exactly
  a class with constant t); nonzero_not_cond32 = 0.
- nonzero_1 = 33,554,432: exactly one nonzero class
  per point, no exceptions.
- Contributions: (−16, 0×11) × 16,777,216 and
  (0×11, +16) × 16,777,216 — signs exactly 1:1, as
  expected for a single class (contrast j = 11's 1:2:1
  for two independent classes).
- Class sizes everywhere: (4×8, 8×4) — 8 classes of
  size 4, 4 classes of size 8, total 64.
- Step-16 witness: wit_4 and share_8 everywhere, and
  witclass_size_8_contrib_0 everywhere — the witness
  still cancels (see §4).

## 4. Witness anatomy at j = 12 (sampled detail)

The 4 step-16 witness reps (ordinals ≡ w mod 16) sit in
one size-8 class with t-pattern
(t,t,1−t,1−t,t,t,1−t,1−t), contribution 0 — the same
cancellation pattern as at j = 11. The other two
non-witness size-8 classes also have balanced
t-patterns and contribute 0; all size-4 classes
contribute 0. So at j = 12, as at j = 11, Gap G comes
solely from the operative-step chain, never from the
step-16 witness. The step-16 witness is a red herring
at every j ≥ 11.

## 5. Ladder table (confirmed through j = 12)

| j | s(j) | chains | length | contribution |
|---|------|--------|--------|--------------|
| 9 | 4 | 2 | 2 | ±4 |
| 10 | 4 | 1 | 4 | ±8 |
| 11 | 5 | 2 | 4 | ±8 |
| 12 | 5 | 1 | 8 | ±16 (this task) |
| 13 | 6 | 2 | 8 | ±16 (predicted) |
| 14 | 6 | 1 | 16 | ±32 (predicted) |

Next testable prediction, j = 13 (s = 6, step-64):
exactly two step-64 chains of 8, each contributing
±16; t-equality ⟺ E + 28δ_E ≡ 0 (mod 32), constant
along chains since 2s = 12 ≥ j−2 = 11.

## 6. Remaining gaps

- The census is exhaustive over the (m = p = 4096,
  ν = (1,0)) grid, not a proof: class-identity of
  witness chains is census-confirmed at j = 9–12
  only, and the general-j ladder argument still
  needs ψ-analysis in general form (rep structure,
  slope lemma, B2 beyond the verified cases).
- DIV and PAR are NOT gaps: proved in general in
  wave 46, task 3.
- No Lean built, repository untouched.

## Checks

- wave47_ladder_j12_probe.py: 4096 sampled points,
  all valid; cond32_1, chain_exact_class_const_t
  everywhere; contribs exactly one ±16 per point.
- wave47_ladder_j12_detail.py: class anatomy of 3
  points (witness class size 8, contrib 0; COND32
  class constant t, ±16).
- wave47_ladder_j12.cpp + wave47_ladder_j12.log:
  full census, 33,554,432 points, exit 0 (OpenMP,
  4 threads, ~12.5 min wall under load).
