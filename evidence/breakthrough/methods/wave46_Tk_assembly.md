# Wave 46, task 9 — Assembly of T_k = 5(k−4)

## Verdict

T_k is assembled conditional on exactly ONE statement on top of Gap G:
the (2-part) U-lemma. The defect identification is PROVED here as a
reduction: assuming Gap G at level j, the support defect at step
j→j+1 equals the U-lemma statement, and nothing else. The U-lemma
itself is NOT proved. New exact check: the U-lemma holds at the
128→256 step, 15/15 on-support split fibers, 0 bad.

Name warning: this "U-lemma" is wave 38(b)'s defect-sum lemma
(U ≡ (Q/4)·pat_z mod Q/2). It is NOT wave 45's "Lemma U"
(full-cycle ℘-rigidity). Different statements, same letter.

## 0. What T_k is (wave 36)

Level k: m = 2^k, Q = 2^{2k+3}, kernel sequences y_{i+1} = 6y_i − y_{i−1}
mod Q, Γ = dihedral. T_k = number of on-support split fibers at level
k. Census: T_5 = 5, T_6 = 10, T_7 = 15, T_8 = 20. Claim: T_k = 5(k−4)
for all k ≥ 5. Dynamics (wave 36 §6, proved given P, S, B): 10 NEW
fibers born per level, exactly one 5-cohort expires per level
(lifespan k ≤ 2b−6 for o_0 = 4, k ≤ 2b−5 for o_0 = 2), net +5.

## 1. Lemma P: complete under Gap G

P (preimage of a fiber is a fiber, type (o,s) ↦ (4o,16s)) was proved
modulo the Drift Lemma (wave 37). The Drift Lemma (wave 38(a)):
split ⟺ ν = (1,1) for p ≥ 8. Its two directions now split:
- ν = (1,1) ⟹ split: was "modulo reversal", now UNCONDITIONAL by
  wave 41: E_alt ∈ {0,±2,±4,±6} for every ν = (1,1) point, so
  |E_alt| ≤ 6 < 8 ≤ p rules out the reversal that would kill the
  odd-flip partner. No Gap G needed here.
- split ⟹ ν = (1,1): this IS the Split Bit Lemma, i.e. Gap G at
  that level (wave 42: Gap G at m ⟹ Split Bit unconditional at m).
Hence: under Gap G at level j, the Drift Lemma holds at level j,
and Lemma P holds at step j→j+1. No other gap in P.

## 2. Lemma B: complete under Gap G

B (exactly 10 NEW on-support split fibers per level k ≥ 6, fixed
profile) splits the same way (wave 38(c)):
- Period-≤4 part: proved UNCONDITIONALLY — exactly 10 fully-colliding
  orbits (sizes 8,8,8,4,4,2,2,2,1,1; periods 4,4,4,4,4,2,2,2,1,1),
  same Ŷ-types at every level (SNF diag(12,96), 128 points/level).
- The only remaining input: no p ≥ 8 non-split orbit fully collides.
  This is the Drift Lemma's converse (drift odd is what the
  drift-multiset theorem needs for p ≥ 8), i.e. Split Bit = Gap G.
Hence: under Gap G at level j, Lemma B holds at step j→j+1.

## 3. Lemma S: defect identification as a proved reduction

Theorem (proved modulo U-lemma + Gap G). Let y be in an on-support
split fiber F at level j, y' a lift at level j+1, z a torsion row.
Then the support defect d_z(y') = 2Q(z) − y'·z satisfies:
d_z ≡ 0 (mod 4Q) for non-max-period F, and d_z ≡ 2Q·pat_z (mod 4Q)
for max-period F, where pat_z = 1 iff z is non-constant mod 4.
Proof. Q_{j+1}(z) ≡ 0 mod 4Q (j ≥ 3), so d_z ≡ −y'·z. With
U = Σ_{i<p} y_i z_i and U' = (N/p)(U/Q) (integer by support):
y'·z = Q·[2U' + (N/2p)·W], W = Σ_{i<4p} δ_i z_i mod 2, using lift
period 4p (drift odd, by §1). W = 0: δ_{i+kp} ≡ δ_i + k (mod 2)
(drift odd) and z 4-periodic with 4 | p give, grouping
i, i+p, i+2p, i+3p, Σ_{k<4} δ_{i+kp} ≡ 4δ_i + 6 ≡ 0 mod 2.
So y'·z = 2Q·U' and d_z ≡ −2Q·U' (mod 4Q): defect ≠ 0 ⟺ U' odd.
Non-max p: U ≡ 0 (mod Q/4) gives U' = (N/4p)·k with N/4p ≥ 2 even,
so U' even, defect 0. Max p: U' odd ⟺ pat_z = 1 is exactly the
U-lemma below. ∎
So Lemma S (preimage on-support iff o(F) < max orbit count) follows
from this theorem plus max-period ⟺ max-orbit-count, which holds at
every checked level (at m = 128: the 5 max-period fibers are exactly
the 5 o = 8 fibers; §5). The defect dichotomy (0 vs (q_hi/2)·pat)
is wave 37's verified observation; the theorem above is its proof
modulo the U-lemma.

## 4. The U-lemma (the single remaining statement for T_k)

For y in an on-support split fiber at level j, p its period,
N = 2^j, Q = 2^{2j+3}, z any of the 16 torsion rows:
- (U-max) if p = N/4: U ≡ (Q/4)·pat_z (mod Q/2);
- (U-nonmax) if p < N/4: U ≡ 0 (mod Q/4).
σ-form of (U-max): with class sums S_r = Σ_{k<p/4} y_{4k+r} and
σ_r = 16S_r/Q, Σ_r z_r σ_r ≡ 4·pat_z (mod 8) for all 16 patterns.
Note: no descent from (U-max) to (U-nonmax) is established; the
lemma is the conjunction. Both parts are exact integer statements
at each fixed level — no analysis, no asymptotics.

## 5. New check: U-lemma at 128→256 (exact, 0 bad)

Script wave46_Tk_Ulemma_check.py (same logic as wave38_explore_b.py,
level pair (128, 131072, 256, 524288); ~7 s). Results:
- 131,072 kernel points at m = 128; 15 on-support split fibers,
  matching wave 36's T_7 = 15.
- 5 MAX fibers (o = 8, p = 32 = N/4): U' = pat_z exactly
  ([0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0]), W = 0, match = True.
- 10 non-max fibers (o = 2, p = 8; o = 4, p = 16): U' = 0, W = 0.
- TOTAL: max = 5, nonmax = 10, bad = 0.
Verified steps now: 32→64, 64→128 (wave 38), 128→256 (this wave).
At every step W = 0 empirically, as §3 proves it must be.

## 6. Assembly theorem (conditional)

Assume (i) Gap G at every level j ≥ 5 and (ii) the U-lemma at every
level j ≥ 5. Then T_k = 5(k−4) for all k ≥ 5.
Proof. Base T_5 = 5 (census). Step: P by §1, B by §2, S by §3, all
under the assumptions; counting by wave 36 §6 (net +5/level). ∎
Gap G is needed only through Split Bit (one direction of the Drift
Lemma); reversal exclusion is already unconditional (wave 41).

## 7. Exactly what remains open, and at which levels

1. U-lemma (§4): OPEN at every level j ≥ 5. Verified at steps
   32→64, 64→128, 128→256 (§5); proved at no level. This is the only
   gap for T_k once Gap G is assumed.
2. Gap G (Split Bit side): proved for period 2^j with j ≤ 8 (direct
   censuses, m ≤ 256 all periods); j = 9 (m = p = 512: mod-16 rule,
   census 524,288 points) and j = 10 (m = p = 1024: census 2,097,152
   points, exactly one ±8 witness per point) by wave 45. DIV proved
   at j = 7 modulo PAR (wave 45); pinning (B1),(B2) for j ≥ 7 modulo
   DIV + PAR (wave 44). OPEN for j ≥ 11 modulo three named inputs:
   DIV in general form, PAR in general (verified to m = 512,
   unproved), and existence of a sharing step-16 class with
   E_m ≡ −4δ_E (mod 2^{j−6}) (wave 45 §7).
3. Minor, used by P and by the max-period definition: on-support
   split fibers have periods 4 | p with 8 ≤ p ≤ N/4 (so max split
   period is N/4). Verified to m = 256 (periods 8, 16, 32, 64); not
   proved in general. If a split fiber of period N/2 existed, the
   max-period/max-orbit identification in §3 would need restating.

## 8. What would close T_k

A level-independent proof of the σ-form (§4) plus completion of the
Gap G tower (gap 2 above). The two are independent: the U-lemma is
a fixed-level class-sum identity; Gap G is a tower/pinning problem.
No Lean built, repository untouched.
