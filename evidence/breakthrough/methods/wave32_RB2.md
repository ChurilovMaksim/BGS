# Wave 32, task 2: RB2 is FALSE — on-support splits outside q₃

## RB2 as stated (wave 23, §4)

> The only on-support split component is the full 3-part
> q₃ = 3^{2v₃(m)+2} when 4 | m, and none otherwise. Split fibers
> there: sizes 4·9^{e/2−1} ≤ 4m², orbit counts 3^{e/2−1} ≤ m.

## Verdict: the exclusivity claim is false, with exact counterexamples

Census (same code path as wave 20, reproduced exactly: m=12 q=81 →
(36,3); m=24 q=81 → (36,3), q=512 → 5 splits off-support; m=36 q=729 →
(324,9),(36,3); m=48 q=81 → (36,3), q=289 → 27 fibers 0 split,
q=332929 → 10693 fibers 0 split; support constant on every component
fiber, 0 partial fibers, at every (m,q) tested):

- **m=30, q=625 = 5⁴: two on-support split fibers, 150 points, 5 orbits
  of 30 each.** m=30 has no 3-part at all (4 ∤ 30), so RB2's "none
  otherwise" fails outright. All 625 points are supported; the only
  partially supported component is q=32 (4/32).
- **m=32, q=8192 = 2¹³: five on-support split fibers** — (32,2) ×3 and
  (16,2) ×2. At m=16 (2¹¹) and m=24/m=40 (2⁹) and m=48 (2¹¹) all
  2-part splits were off-support; at 2¹³ they land on support.

No other violations in the completed census range (m = 6, 10, 12, 16,
18, 20, 24, 28, 30, 32, 36, 40, 44, 48; all prime powers ≤ 400000, plus
923521 at m=30; huge components skipped: 1329409 at m=24/48,
443365544449 at m=32, 32959081/131859289 at m=44, 188485441 at m=48).
m=60/64 censuses later completed (all prime powers ≤ 400000; skipped
only 923521/5202961 at m=60 and 1985281/443365544449/5996469615361 at
m=64; q=332929 at m=64 is clean, 10693 fibers, 0 split). So the "no
other" claim extends to m=60/64 as well, modulo the skipped huge
components.

## The new splits are phase-split, not just split

S_q phases computed by the wave-20 method, with the adjugate avoided
via the exact identity W X W'^T = (D/q)(W·y') for kernel points
H y = qW (X = adj(H) = D·H^{−1}, H^{−1}W' = y'/q). Correction mode
confirmed cleanly (m=30: raw_bad=289/300, corr_bad=0; m=32:
raw_bad=252/300, corr_bad=0). Γ-invariance validates the computation:
phase spread within every orbit ≤ 2×10⁻¹³.

- m=30, q=625: |S| = 25 = √625 on all 5 orbits of each fiber; phases
  are 5th roots of unity, 72° apart (2.010619, 0.753982, −3.015929,
  −0.502655, −1.759292) — coherent sum exactly 0.
- m=32, q=8192: |S| = 4√8192 ≈ 362.0387 on all orbits; the two orbits
  of each fiber are π apart, equal size — coherent sum exactly 0.

So these splits have the same full-cancellation signature as m=24's
contributing 81-split (120° apart), not the degenerate equal-phase
case that would leave Δ_F = 0.

## They lift to contributing global fibers: Δ(30) > 0 and Δ(32) > 0

Rigid lift: fix all other components to the zero sequence. Zero is
supported at every component of D_30 and D_32 (checked exactly via the
Qmod criterion 2·Qmod(z) ≡ 0 mod q, including the huge component
443365544449 at m=32 — no enumeration needed). The CRT idempotent
for q* is ≡ 1 mod q* and ≡ 0 mod every other component, so the global
value is an injective function of the q*-coordinate alone. Hence any
global point sharing the multiset reduces mod q' to {0} (so ≡ 0 mod
q') and mod q* to the component multiset (so lies in the q*-fiber):
the global fiber is exactly the CRT lift, 150 points at m=30 (resp.
32/16 at m=32). Global Γ-orbits correspond bijectively to component
orbits (zeros are Γ-fixed), sizes preserved, and φ̂ = ∏_q S_q differs
across the fiber only by the q*-phase, up to a common factor. The
coherent sums vanish (5th roots; π-pairs), so each rigid fiber has
deficit exactly |F|². Therefore, counting rigid fibers only:

- Δ(30) ≥ 2·150²/|supp| = 45000/(D_30/8) ≈ 3.9×10⁻¹⁸ > 0.
- Δ(32) ≥ (1024+1024+256+1024+256)/|supp| = 3584/(D_32/16)
  ≈ 1.8×10⁻¹⁷ > 0.

(|supp| = D/|V4|; validated: ∏_q supp_pts(q) = D/|V4| exactly at
m=12 (|V4|=16) and m=30 (|V4|=8).)

## Consequences

- **RB1' is false too.** It predicts no contributing fiber without a
  split 3-fiber; the rigid fibers above have a split 5-fiber (m=30)
  resp. split 2-fiber (m=32) and singletons elsewhere.
- **Wave 29's "Δ(m) = 0 unless 12 | m" is false as a conclusion**
  (30 ≡ 6, 32 ≡ 8 mod 12) — it was conditional on RB1', which falls.
- **Δ → 0 itself is NOT refuted.** The new contributions are
  ~10⁻¹⁷–10⁻¹⁸, vastly below Δ(12) ≈ 1.9×10⁻⁴. But the RB-route to
  Δ → 0 is broken: the counting must be redone without the
  3-part exclusivity, and the H12-poly result (twin sums at 12|m) is
  unaffected — it concerns a different mechanism.
- **What survives of RB2:** the 3-part exponent (3-adic LTE, proved,
  wave 24); no split at e ≤ 2 (Lemma 9-split, proved, wave 29); the
  size bound ≤ 4m², verified at q₃ (36 at e=4; 324, 36 at e=6) and
  also satisfied by the new splits (150 ≤ 3600; 32 ≤ 4096).

## The phenomenon is systematic, not a fluke (m=60, m=64)

- **m=60: the 5-part splits persist alongside the 3-part split.**
  q=81 → (36,3) on-support as expected, and q=625 → the same two
  on-support splits (150,5) ×2 as at m=30. So at m=60 (12 | 60) the
  contributing splits are 3-part AND 5-part together.
- **m=64: the 2-part splits grow with the exponent.** q=32768 = 2¹⁵:
  20 splits, 10 on-support — (32,2), (128,4) ×3, (64,4) ×2, (32,2),
  (16,2) ×2, plus one more (32,2) — sizes up to 128, up to 4 orbits,
  against 5 on-support fibers of size ≤ 32 at 2¹³ (m=32) and none at
  2⁹/2¹¹. So 2-part on-support splits appear at exponent 13 and grow
  at exponent 15; the size bound ≤ 4m² still holds (128 ≤ 16384).

## Replacement question (for wave 33)

RB2* must describe which p-power components can carry on-support
phase-splits. Data so far: 3^e splits on-support iff e ≥ 4; 5⁴ splits
at m=30 and m=60 (5 | m in both); 2^e splits on-support at e ≥ 13
(m=32, 64) but not at e ≤ 11. The natural next test is the threshold
law: does a p-part split on-support exactly when its exponent passes
a p-dependent threshold (4 for p=3, 4 for p=5, 13 for p=2)? — and a
re-count of Δ → 0 with all contributing components, not just q₃.

## Files

- This note: `wave32_RB2.md`.
- Census: `wave32_RB2_check.py` (m ≤ 48 + 6/10/18/30 runs above).
- Phases: `wave32_RB2_phases.py` (adjugate-free S_q, correction test).
- Repository untouched; no Lean built.
- Honest limit: the Δ lower bounds use the wave-20 S_q framework
  (Γ-invariance sketch, φ̂ = ∏_q S_q); the census skips prime powers
  above the cap, but the rigid-lift argument needs no enumeration at
  the skipped components (zero-supported there by the Qmod criterion).
