# Wave 47, task 6 — 2-part U-lemma: nonmax PROVED, max reduced to one lemma

## Verdict

The nonmax half of the U-lemma is PROVED unconditionally — for every
period-p sequence with 4 | p satisfying the recurrence, no support or
split hypothesis needed. The max half is reduced, by proved steps, to
exactly one named lemma (CSL-max below): two bits on (S_0, S_1).
Consequence: T_k = 5(k−4) now rests on Gap G + CSL-max only; the
U-lemma's nonmax half drops out of the assembly entirely.
No counterexample at any checked level. No Lean built, repo untouched.

## 0. Setup (wave 46 §4)

Level j: N = 2^j, Q = 2^{2j+3}. y has period p, 4 | p, and
y_{i+1} = 6y_i − y_{i−1} mod Q. Class sums S_r = Σ_{k<p/4} y_{4k+r}.
U = Σ_{i<p} y_i z_i = Σ_r z_r S_r for each 4-periodic torsion row z.
Max: p = N/4, claim U ≡ (Q/4)·pat_z (mod Q/2).
Nonmax: p < N/4, claim U ≡ 0 (mod Q/4). pat_z = 1 iff z non-constant
mod 4. The 16 patterns are fixed integers, level-independent
(script wave47_Ulemma_patterncheck.py recomputes them from
torsion_data; e.g. (−1,1,2,4), (1,1,1,1), (0,4,0,4)).

## 1. Class-sum recurrence (PROVED)

Lemma. For any such y, the class sums satisfy, cyclically in r mod 4,
S_{r+2} = 6S_{r+1} − S_r (mod Q).
Proof. Sum the y-recurrence over i ≡ r+1 (mod 4), i ∈ [0,p):
Σ y_{i+1} = S_{r+2}, 6Σ y_i = 6S_{r+1}, Σ y_{i−1} = S_r, using
periodicity and 4 | p so residue classes mod 4 are preserved. ∎
Hence S_2 = 6S_1 − S_0 and S_3 = 35S_1 − 6S_0 (mod Q), so for every z,
U = A_z·S_0 + B_z·S_1 (mod Q), where
A_z = z_0 − z_2 − 6z_3, B_z = z_1 + 6z_2 + 35z_3.

## 2. Two proved congruences

Lemma. S_r ≡ 0 (mod Q/32) for all r, and S_1 ≡ 3S_0 (mod Q/4).
Proof. Adding the r = 0 and r = 2 recurrences gives
2(S_0+S_2) = 6(S_1+S_3) (mod Q), and symmetrically
2(S_1+S_3) = 6(S_0+S_2). So with A = S_0+S_2: 8A ≡ 0 (mod Q/2),
i.e. A ≡ 0 (mod Q/16). But A = 6S_1 (from §1), so S_1 ≡ 0
(mod Q/32); likewise all S_r. Also 2A = 6B with A = 6S_1,
B = 6S_0 gives 12S_1 ≡ 36S_0 (mod Q), i.e. S_1 ≡ 3S_0 (mod Q/4)
since 3 is a unit mod 2^k. ∎
Remark (proved, via total sum T = 42S_1 − 6S_0 and 4T ≡ 0 mod Q):
S_0 ≡ 7S_1 (mod Q/8), so τ_0 ≡ τ_1 (mod 2) below.

## 3. Pattern facts (exact 16-row checks, scripted)

(a) A_z + 3B_z ≡ 0 (mod 8) for all 16 patterns.
(b) B_z ≡ pat_z (mod 2) for all 16 patterns (since
B_z ≡ z_1 + z_3 (mod 2) and pat_z = (z_1+z_3) mod 2, wave 38).

## 4. Nonmax: PROVED

Write S_1 = 3S_0 + (Q/4)·K (§2). Then mod Q/4:
U = (A_z + 3B_z)·S_0 + B_z·(S_1 − 3S_0) ≡ (A_z + 3B_z)·S_0.
By §3(a) and S_0 ≡ 0 (mod Q/32) (§2),
(A_z + 3B_z)·S_0 ≡ 0 (mod 8·Q/32) = 0 (mod Q/4). ∎
So U ≡ 0 (mod Q/4) for every pattern, every nonmax fiber — in fact
for every period-p sequence with 4 | p. No support/split used.

## 5. Max: reduction to CSL-max

Write S_0 = (Q/32)·τ_0′, τ_0 = τ_0′ mod 2, and
K = (S_1 − 3S_0)/(Q/4) (integer by §2), k = K mod 2. Then mod Q/2:
U ≡ (Q/4)·(c_z·τ_0 + B_z·k), where c_z = ((A_z+3B_z)/8) mod 2,
using §3(a) and S_0 ≡ 0 (mod Q/32). The 16-row bit table
(scripted) shows c_z·τ_0 + B_z·k ≡ pat_z (mod 2) for all patterns
iff τ_0 = 0 and k = 1: constant patterns force τ_0 = 0
(e.g. (1,1,1,1): c_z = 1, B_z even, pat_z = 0), permutation
patterns then force k = 1 (B_z odd = pat_z by §3(b)).

Lemma CSL-max (the single remaining statement). For every
max-period on-support split fiber: S_0 ≡ 0 (mod Q/16), and
S_1 ≡ 3S_0 + Q/4 (mod Q/2). (In σ-form, σ_r = 16S_r/Q:
σ_1 ≡ 3σ_0 + 4 (mod 8).) By §5, CSL-max ⟺ max U-lemma.

## 6. Verification (script wave47_Ulemma_classsum.py)

Checks on every on-support split fiber: recurrence §1 exact,
§2 congruences, nonmax U ≡ 0 mod Q/4, max τ_0 = 0, k = 1 and
U ≡ (Q/4)·pat_z mod Q/2, all 16 patterns.

| level | max (p, o) | nonmax | bad |
| m=32 | 5 (8, 2) | 0 | 0 |
| m=64 | 5 (16, 4) | 5 (p=8) | 0 |
| m=128 | 5 (32, 8) | 10 (p=16, 8) | 0 |

Max fibers at all three levels have S_0/(Q/32) ∈ {16,18,20,22,28}
(τ_0 = 0, k = 1 throughout). The 256→512 exact check
(wave47_Ulemma_256_check.py) was launched and is still running;
it tests CSL-max at one more level when it lands.

## 7. What remains

Only CSL-max (two bits: S_0 mod Q/16 and the Q/4-bit of
S_1 − 3S_0). Note the bits are not both free: τ_0 ≡ τ_1 (mod 2)
is proved (§2 remark), so CSL-max is really "τ_0 even, k odd".
Support gives nothing beyond §2 here (Q(z) ≡ 0 mod Q, so support
is U ≡ 0 mod Q/4, already implied by §4's argument); a proof of
CSL-max must use max-period + split structure beyond the class sums.
