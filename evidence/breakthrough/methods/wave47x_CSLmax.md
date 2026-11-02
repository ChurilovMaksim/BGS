# Wave 47x, task C — CSL-max: PROVED modulo Gap G + one Tower-Base Lemma

## Verdict

CSL-max is proved modulo Gap G and exactly one named residual statement
(Tower-Base Lemma, §4). Hence T_k = 5(k−4) now rests on Gap G alone
(given the wave-46 assembly). No counterexample at any checked level.
No Lean built, repository untouched.

## 0. Setup (wave 47, task 6)

Level j: N = 2^j, Q = 2^{2j+3}. y has period p, 4 | p, recurrence
y_{i+1} = 6y_i − y_{i−1} mod Q. Class sums S_r = Σ_{k<p/4} y_{4k+r}.
S_{r+2} = 6S_{r+1} − S_r, S_r ≡ 0 mod Q/32, S_1 ≡ 3S_0 mod Q/4
(wave 47 §1–§2, proved). Write S_0 = (Q/32)·τ_0′, τ_0 = τ_0′ mod 2,
K = (S_1 − 3S_0)/(Q/4), k = K mod 2. CSL-max: for every max-period
(p = N/4) on-support split fiber, τ_0 = 0 and k = 1.

## 1. Lift-Bits Lemma (PROVED)

Let y′ at level j+1 (modulus Q′ = 4Q) be a drift-odd lift of y at
level j: period p′ = 4p, y′_i ≡ y_{i mod p} mod Q, drift
δ_i = (y′_i − y_{i mod p})/Q, δ_{i+p} ≡ δ_i + 1 mod 2.
Then S′_r = 4S_r + Q·Δ_r exactly, Δ_r = Σ_{k<p} δ_{4k+r}:
indeed Σ_{k<p} y_{(4k+r) mod p} = 4S_r (each index ≡ r mod 4
occurs 4 times, using 4 | p). Moreover Δ_r is EVEN: partition
{4k+r} by mod p into groups {i_0 + tp : t < 4} (needs 4 | p);
drift-odd gives Σ_{t<4} δ_{i_0+tp} ≡ 4δ_{i_0} + 6 ≡ 0 mod 2.
Consequences (Q′/16 = Q/4, Q′/4 = Q, Q′/2 = 2Q):
- τ_0′ = 0 ⟺ S′_0 ≡ 0 mod Q/4 ⟺ 4S_0 ≡ 0 mod Q/4
  ⟺ S_0 ≡ 0 mod Q/16 ⟺ τ_0 = 0 (no drift needed);
- S′_1 − 3S′_0 = 4(S_1 − 3S_0) + Q(Δ_1 − 3Δ_0)
  ≡ Q·k + Q(Δ_1 + Δ_0) mod 2Q, so with Δ even,
  k′ = 1 ⟺ k = 1.
So (τ_0, k) propagate unchanged up drift-odd 4× lifts.
Drift-odd is the Drift Lemma (split ⟺ ν = (1,1)): its
split⟹ν direction is Split Bit = Gap G (wave 46 §1); the
ν⟹split direction is unconditional (wave 41). Lemma P
(preimage of a fiber is a fiber) is likewise modulo Gap G.

## 2. Pred2 Lemma (PROVED)

Let the base have period 2, lift period 8. Period-2 system gives
a, b ≡ 0 mod Q/16; write a = (Q/16)v_a, b = (Q/16)v_b, with
v_b ≡ 3v_a mod 8. Define u = ((b − 3a) mod Q)/(Q/2) mod 2.
Lift bits: S′_0 = 2a + Q(δ_0 + δ_4), S′_1 = 2b + Q(δ_1 + δ_5).
- τ_0′ = 0 ⟺ 2a ≡ 0 mod Q/4 ⟺ v_a even.
- δ-recurrence mod 2 (from the lift recurrence, defects
  e_i = (y_{i+1} − 6y_i + y_{i−1})/Q): δ_{i+2} ≡ δ_i + e_{i+1}
  mod 2. Step2-odd (δ_{i+2} ≡ δ_i + 1) ⟺ e_0, e_1 odd
  ⟺ (u = 1 and v_a even), since e_0 = (v_b − 3v_a)/8 and
  e_1 = (v_a − 3v_b)/8, and e_0 odd ⟺ u = 1, e_1 odd (given
  u = 1) ⟺ v_a even. Step2-odd gives δ_4 ≡ δ_0, δ_5 ≡ δ_1
  mod 2, so δ_0 + δ_1 + δ_4 + δ_5 ≡ 0 mod 2, and
  S′_1 − 3S′_0 = Q·e_0 + Q(δ_1 + δ_5 − 3δ_0 − 3δ_4)
  ≡ Q·(e_0 + 0) mod 2Q, hence k′ = 1 ⟺ e_0 odd ⟺ u = 1.
Therefore (u = 1 and v_a even) ⟹ the lift has bits (0, 1).

## 3. Pred1 Lemma (PROVED)

Let the base be constant c = (Q/4)·t, t ∈ {0,1,2,3}, lift
period 8. τ_0′ = 0 is automatic (2c ≡ 0 mod Q/4). Mod-2Q
recurrence for ε_i = δ_i mod 2: ε_{i+1} ≡ ε_{i−1} + t mod 2.
If t is odd, ε has period 4, so δ_0 + δ_1 + δ_4 + δ_5
≡ 0 mod 2, and S′_1 − 3S′_0 = −Qt + Q(δ_1 + δ_5 − 3δ_0
− 3δ_4) ≡ Q·t mod 2Q, hence k′ = 1 ⟺ t odd.
If t is even, ε has period 2, the same four-term sum is
≡ 0 mod 2, and k′ = 0.
Hence an 8× lift of a period-1 base has bits (0, 1) ⟺ t odd.

## 4. Tower-Base Lemma (ONE named residual; census-verified, §5)

Reduction chains of split fibers strictly decrease period
(factor 4, or 8 from period-1) until period ≤ 4. The bases are
exactly, level-independently:
- period-4: 5 types, values scaling by 4 per level (at Q = 8192:
  [0,2048,4096,6144], [512,3584,4608,7680], [1024,5120,5120,1024],
  [1536,6656,5632,2560], [3072,3072,7168,7168]); bits (0, 1) by
  direct computation (S_0/(Q/32) ∈ {0,2,4,6,12}; S_1 − 3S_0
  ≡ Q/4 mod Q/2 in all 5 cases; scaling preserves both bits).
  Their lifts are drift-odd (checked on the 5 types).
- period-2: exactly (v_a, v_b) = (0,8), (2,14), (6,10)
  (u = 1, v_a even, in both phases).
- period-1: exactly t ∈ {1, 3}.
General proof of this classification (splitness ⟹ base data) is
open; it is the only remaining gap for CSL-max.

## 5. Assembly (induction on level)

Claim H(j): every tower fiber at level j with 4 | p has bits
(0, 1), where tower(j) = split fibers at level j plus all their
reductions. Base j = 5 (m = 32): 5 max fibers, bits (0, 1)
(wave 47 classsum), plus the 5 period-4 tower singletons (§4).
Step: a split fiber F′ at level j+1 reduces to F at level j.
If 4 | p_F, bits(F′) = bits(F) = (0, 1) by Lemma 1 + H(j).
If p_F = 2, bits(F′) = (0, 1) by Lemma 2 + §4. If p_F = 1,
bits(F′) = (0, 1) by Lemma 3 + §4. (Reductions of split fibers
at levels 64/128/256 are all of these three kinds; no same-period
or factor-2 reductions occur.) Max fibers are split, hence in
the tower, so CSL-max follows. T_k = 5(k−4) then rests on Gap G
alone (wave-46 assembly + wave-47 §6 nonmax proof).

## 6. Verification (exact)

- Bits table, all on-support fibers with 4 | p: at m = 32:
  (split, 0, 1): 5, (singleton, 0, 1): 5, (singleton, 1, 0): 48;
  m = 64: 10 / 5 / 112; m = 128: 15 / 5 / 240;
  m = 256: 20 / 5 / 496. So (0, 1) ⟺
  tower membership among on-support fibers, and every split
  fiber has (0, 1). (Support is vacuous for p ≤ m/4: the support
  sum is (m/p)·U_z with U_z = (Q/4)·W_z, so (m/p) ≥ 4 kills it;
  the (0, 1)/(1, 0) dichotomy is a tower phenomenon, not support.)
- Lift checks at 64/128/256 (all on-support split fibers): lift
  property True everywhere; 4× identity S′ = 4S + QΔ True
  wherever 4 | p_base; Δ even everywhere; bits equal to the
  reduction everywhere; drift-odd True everywhere checked.
  Max chains: max(128) ← split (2, 8)@64 ← period-2 (u = 1) /
  period-1 (t odd) @32; max(64) ← period-4 tower @32.
  At 256: 20 split fibers — max (16, 64) ← (4, 16)@128 with
  Δ = [24, 24, 24, 24]; (8, 32) ← (2, 8)@128 with Δ = [12, 12,
  12, 12]; (4, 16) ← period-4 tower @128 with Δ = [6, 6, 6, 6];
  (2, 8) ← 3 pred2 (u = 1) + 2 pred1 (t = 1, 3) @128.
- CSL-max itself: verified at m = 32, 64, 128 (wave 47) and m = 256
  (wave-47 256-check: 5 max, 15 nonmax, 0 bad; this note's
  Table A/B at 256 independently confirms the same structure).
- Scripts: wave47x_CSLmax_lift.py, wave47x_CSLmax_all.py,
  wave47x_CSLmax_base.py.

## 7. What remains

1. Tower-Base Lemma in general (§4): why splitness forces exactly
   these base types. Census-verified at m = 32, 64, 128, 256
   (Table A/B counts in §6); no counterexample at any level.
2. Lean formalization (none built). Gap G tower (j ≥ 13 ladder)
   is separate and untouched by this argument.
