# Wave 37, task 1 (retry): blind product B(60) — exact, m = 60 only

## Correction of wave 36 (important, do not reuse)
The wave-36 note's 81-column is WRONG: verbatim rerun of `wave36_pin_test2.py`
gives blind81 = 0 at 361 and 841 (not ALL 360/360, 840/840). Hence "free set
{81} may carry any sequence at 361/841" and "B(m) ≥ 361·841 for T={81}" are
FALSE under the triple test. The 625-column of wave 36 stands.

## Blindness table (exact; triple test, all sequences, all locked reps)
Test: fix a locked rep, vary the free fiber over its orbit reps, compare
sorted triple multisets (a_i, b_i, o_i); a collision = o does not pin the move.
"Blind625/81" = # sequences (incl. zero) colliding for ≥1 locked rep/fiber.

| q0 | blind625 | blind81 |
|----|----------|---------|
| 49 | all 49 | 0 |
| 121 | all 121 | 0 |
| 361, 841 | zero only (1) | 0 |
| 1681, 3481, 72361, 361201, 5202961 (p²) | zero only (p+1 direction reps, exact: kernel = p·(Z/p²)², unit scaling preserves blindness) | 0 |
| 923521 (31⁴) | zero only (batched exhaustive over all 923,521 seeds) | 0 |

Zero is blind for 625-moves everywhere and pins 81-moves everywhere.

## 81 is always locked (slice proof, no blindness needed)
Per 625-fiber the slice has exactly 12 joint fibers, each spanning exactly one
81-orbit (part 2). A full-space joint fiber's points project to pairs (a,b)
sharing the pair multiset, hence lie in one slice fiber, hence span exactly
one 81-orbit. So N_{81} = 0 and N_{81,625} = 0 rigorously. Only T={625} feeds C.

## B(60) exactly
B(60) = 49 × 121 = **5929** blind sequence combinations (wave-36 convention);
the joint test confirms all 5929 collide for every 81-orbit rep and 625-fiber.
As orbit pairs: 12 (at 49) × 11 (at 121) = 132. 2-part at (60,128): Q₂ = 5
supported 2-fibers, 8 supported points, max size 2 (exact, not RB3′'s 28800).

## Joint total at m = 60: polynomial, c_J = 8; c_J = 5 undecided
Lower: per (orbit pair, 2-fiber) section ≥ 6 fibers (3 a-reps × 2 625-fibers,
distinct by locked orbit / 625-fiber / marginal argument: no splits at 49/121
force all points of a fiber into one 49- and one 121-orbit). Each has ≥ 2
diagonal orbits of size ≥ 60 (stabilizer ⊆ Stab(a)∩Stab(b), |·| ≤ 2 from the
zero-section orbit sizes 60/120) with distinct 5th-root 625-phases (both 625
fibers verified: 5 distinct phases each, spreads ~1e-14; 2nd fiber = negatives
of the 1st). So Δ_F ≥ 2·60·60·(1−cos72°) = 4975.08, and total ≥ 660×6×4975 ≈
1.97×10⁷.
Upper (tightened): |F| ≤ 600 (slice pairs) × 144 (≤6·12·2 per-pair multiplicity)
= 86,400; total section points = 5929·36·150·2·8 = 5.12×10⁸; total ≤ 86,400 ×
5.12×10⁸ = 4.43×10¹³ < 60⁸ (1.68×10¹⁴). Wave-36 formula as written:
3600·28800·11137·5929 = 6.85×10¹⁵ ≈ 60^8.91 (c_J = 9).
Verdict: the m=60 joint total is polynomial in the wave-35 sense with c_J = 8
rigorously. c_J = 5 is NEITHER proved NOR refuted for the true total: the
interval [1.97×10⁷, 4.43×10¹³] straddles 60⁵ = 7.78×10⁸. Wave-35's 60⁵ covered
only the rigid (zero-rest, single-2-fiber) section. One m proves nothing about
SCJ in general — the Blindness Law for all m remains open.

## Scripts / scope
`wave37_Blindness_m60.py`, `wave37_Blindness_m60_part2.py`,
`wave37_Blindness_m60_part3.py`, `wave37_Blindness_m60_phases625.py` (logs alongside).
m = 60 only. Repository untouched; no Lean built.
