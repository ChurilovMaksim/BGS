# Wave 34, task 2 — SC danger case: no ~D_m^δ split fiber exists

## Verdict

The danger case as stated — a single split fiber of size ~D_m^δ
at some huge prime power — is DEAD, unconditionally, by an
elementary pair argument (§1). What the new census does kill is
wave 33's constant: SC holds with c = 5, not c = 4 (§2). The
remaining gap for full SC is a bound on the NUMBER of split
fibers per component, not on their size (§5). Repository
untouched, no Lean built.

## 1. Theorem (proved): every component fiber has size ≤ m²

Let F be a fiber of kernel points mod q (any prime power, any
m ≥ 2): sequences y ∈ (ℤ/q)^m satisfying
y_{i+1} = 6y_i − y_{i−1} (mod q) and m-periodicity, grouped by
sorted multiset. A point y is determined by its first two
coordinates (y₀, y₁): forward recurrence gives y₂, …, y_{m−1}.
Both y₀ and y₁ occur among the values of y, hence in the sorted
multiset M of F, which has m entries and therefore at most m
distinct values. So (y₀, y₁) ranges over at most m² ordered
pairs, and distinct points have distinct pairs. Hence

    s_q ≤ m²   for every component fiber, split or not.

Corollary: for any fixed δ > 0, s_q = o(D_m^δ), since
D_m ≥ ρ^m − 2 with ρ = 3 + 2√2. No split fiber can have size
~D_m^δ for large m; small m are covered by direct census (§3–4).
The single-fiber danger case is impossible, for every q,
including huge prime powers.

## 2. SC with c = 4 is FALSE; SC with c = 5 holds on all data

Counterexample to c = 4, exact (wave34_SC_m21.py): m = 21,
q = 2401 = 7⁴, all points supported, FIVE on-support split
fibers of size 294 (7 orbits each), so

    Σ_q n_q s_q² = 5 · 294² = 432,180 > 21⁴ = 194,481  (2.22×).

Wave 33's c = 4 rested on censused m ≤ 64 selected values;
m = 21 was not censused. With c = 5 the same total has slack
21⁵ / 432,180 ≈ 9.4×, the tightest slack in the new data.
Everywhere else c = 5 slack is huge: m = 108, q = 6561:
8,609,328 vs 108⁵ (slack ~1700×); m = 150, q = 15625:
28,170,000 vs 150⁵ (slack ~2700×); m = 63: same 432,180 total,
slack ~2300×. So the repaired split-census hypothesis is SC
with c = 5 (constant left free for the count lemma in §5).

## 3. Scaling families: sizes are polynomial and saturate §1

3-part, m = 4·3^k (q = 3^{2k+2}): main split fiber size
4·9^k = m²/4 exactly — 36 (m = 12), 324 (m = 36), 2916
(m = 108, 27 orbits, depth 4), plus lifted fibers 324 (depth 5)
and 36 (depth 6) at m = 108. The pair bound §1 is sharp up
to the constant 4 here.
5-part, m = 6·5^k (q = 5^{2k+2}): main size 6·25^k = m²/6 —
150 (m = 30, 60), 3750 (m = 150, 25 orbits, depth 3), plus
150-fibers at depth 4. In general, main split fiber size =
c_p · p^{e/2} with c₃ = 4, c₅ = 6, c₇ = 6 (e = 4: 36, 150,
294; e = 6: 324, 3750). Size depends on q only, not on m:
the m = 21 and m = 63 fibers at q = 2401 are identical
(294 × 5), and m = 42 matches too.

## 4. Structural laws (verified, not yet proved in general)

- Split ⇒ p | m (odd p). Splits occur only at components whose
  prime divides m: (30, 923521 = 31⁴): 0 splits, 31265 fibers =
  31265 orbits, all supported; (14, 28561 = 13⁴): 0 splits;
  prime m = 5, 7, 11, 13: 0 splits at every component, including
  q = 57121, 124609, 358801 (all fully supported);
  (63, 16129 / 39601 / 57121): 0 splits (127, 199, 239 ∤ 63).
  Conversely p | m with exponent e ≥ 4 does split: (21, 2401)
  and (42, 2401) both give the same 5 × 294 fibers.
- Split ⇒ e ≥ 4 (odd p): consistent with square rigidity at
  e = 2 (wave 32 task 4) and e odd impossible (odd part of D_m
  is a square). LTE form e = e_d + 2·v_p(m/d), d = order of α
  mod p, verified for p = 3, 5, 7, 11, 13 to m ≤ 120 and for the
  high primes below to m ≤ 240.
- Depth law: in every censused on-support split fiber at odd
  q = p^e, every point has v_p(gcd of coordinates) ≥ e/2,
  constant across the fiber (depths: 2 at 81/625/2401; 3, 4 at
  729/15625; 4, 5, 6 at 6561). 2-part depths at 8192 are 8–10
  (e = 13). This law is the natural route to the count lemma.
- High primes are tame: base exponents e_d ≥ 4 occur only for
  (13, 14) and (31, 15) among all primes with d ≤ 120 (241
  primes seen); all others have e_d = 2. The dangerous-looking
  q = 923521 = 31⁴ at m = 30 does not split (31 ∤ 30), so the
  high-prime danger case needs p | m as well, hence p ≤ m.

## 5. What remains: the Split-Count Lemma (for full SC)

From §1, Σ_q n_q s_q² ≤ (Σ_q n_q) · m⁴. The number of
components ω(D_m) satisfies 2^ω ≤ D_m < ρ^m, so ω < 2.54m.
Hence SC with c = 5 follows from one named lemma:

    Split-Count Lemma: n_q ≤ 10 for every component q
    (then Σ_q n_q ≤ 26m and Σ n_q s_q² ≤ 26·m⁵).

Evidence: max observed n_q is 10 (m = 64, q = 32768, 2-part);
odd-p max is 5 (q = 2401); new censuses give 3 (m = 108),
4 (m = 150), 0 at every high prime tested. The depth law (§4)
is the proposed route: split fibers at q are classified by
depth t ≥ e/2, and division by p^t should biject them onto
split fibers mod p^{e−t} (checked: the 2916-fiber at 6561
reduces to a 2916-fiber mod 81, which is not deep, so the
recursion stops in one step).
Note: the sibling wave-34 result refuting RB1′′ (joint splits
F₈₁ × F₆₂₅ at m = 60) does not touch SC itself — SC is the
per-component census — but the wave-33 Δ → 0 theorem needs a
third joint-split mechanism on top of SC(c = 5); with two split
components, global sizes multiply (≤ m⁴) and counts multiply,
still polynomial under the count lemma.

## Files

- This note: `wave34_SC_danger.md`.
- `wave34_SC_census1.py` (prime m, 0 splits),
  `wave34_SC_inspect.py` (depths/periods),
  `wave34_SC_target.py` (m = 108, 150 scaling),
  `wave34_SC_923521.py` (m = 30, q = 923521, 0 splits),
  `wave34_SC_pdiv.py` (p | m rule: 21/42 vs 14),
  `wave34_SC_m21.py` (full m = 21, 63 census; c = 4 fails).
- Addendum: the broad census `wave34_SC_census2.py` (m = 72–150,
  q ≤ 400000) did complete after all and confirms every targeted
  number exactly: m = 72 total 106272 (= 324² + 36², same as m = 36);
  m = 96 total 4880; m = 108 total 8609328; m = 120 total 46296;
  m = 144 total 106272 (same as m = 72); m = 150 total 28170000.
  No new split component appears; all totals are consistent
  with SC(c = 5) and with size depending on q only.
