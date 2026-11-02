# Wave 38, task 4: the three gaps behind the 2-part lemmas

Wave 37 proved Lemmas P, S, B modulo one gap each. No gap is refuted;
each is now either proved, or reduced to one exactly-stated lemma.
Notation: level j has m = 2^j, Q = 2^{2j+3}, length N = 2^j; y has
period p; z is a torsion row (4-periodic pattern); Γ = dihedral.

## (a) Drift Lemma — proved modulo two named sub-points

Setup (wave 37): half-period defect v = (M^{p/2}−I)(seed) = (Q/2)·ν,
ν ∈ (ℤ/2)²; V = (I−M^p)(seed)/Q satisfies V mod 2 = ν (since
L = (M^{p/2}+I)/2 ≡ I mod 2 for p ≥ 8); drift odd ⟺ ν = (1,1).
Data: split ⟺ ν = (1,1), nonsplit (p ≥ 8) ⟺ ν ∈ {(1,0),(0,1)}.

- PROVED: ν = (0,0) impossible for minimal p ≥ 8 (φ_p(seed) = 0 forces
  v into Ker(M^{p/2}+I mod 2Q), whose 4 elements are ≡ 0 mod Q, so
  period divides p/2).
- PROVED (modulo reversal): ν = (1,1) ⟹ split. Partner
  z_i = y_i + (Q/2)·(i odd) is a kernel sequence in the same fiber
  (verified: all split points at m = 32, 64; z same fiber, new orbit).
  Shift exclusion proved: k even forces k = p/2, but the p/2-shift adds
  Q/2 everywhere, not only on odd positions; k odd forces
  k ∈ {p/4, 3p/4}, both even — contradiction.
- OPEN sub-point 1 (reversal exclusion): a reversal would force
  A = pQ/8 for the alternating sum A = Σ_{i<p}(−1)^i y_i. The recurrence
  gives A = (Q/8)·E_alt, E_alt = −Σ(−1)^i e_i ∈ ℤ, so this needs
  |E_alt| < 8. Computational only: A ∈ {0, ±Q/4, ±Q/2, ±3Q/4} at
  m = 32, 64, hence A ≠ pQ/8 ≥ Q. Orbit-canon checks agree (0 reversals).
- OPEN sub-point 2 (Split Bit Lemma, the converse): split ⟹ ν = (1,1).
  Off-diagonal flips provably fail as partners (ν = (1,0): odd-flip
  leaves the fiber, even-flip = p/2-shift; ν = (0,1) symmetric). The
  remaining route is descent: for ν = (1,0) the odd subsequence has
  period dividing p/4, and its sub-multiset is never Q/2-symmetric
  (data only). Not completed.

Verdict (a): proved except reversal exclusion + Split Bit Lemma.

## (b) Defect identification — proved modulo the U-lemma and (a)

For y ∈ on-support split fiber, lift y′ at level j+1, defect
d_z = 2Q_{j+1}(z) − y′·z mod 4Q. Q_{j+1}(z) ≡ 0 mod 4Q (j ≥ 3), so
d_z ≡ −y′·z. With U = Σ_{i<p} y_i z_i, support gives
U = (Qp/N)·U′, and the lift period is 4p (drift odd), so
y′·z = Q·[2U′ + (N/2p)·W], W = Σ_{i<4p} δ_i z_i mod 2.

- PROVED: W = 0, using (a). δ_{i+kp} ≡ δ_i + k (mod 2) since drift is
  odd; z is 4-periodic and 4 | p, so grouping i, i+p, i+2p, i+3p gives
  Σ_{k<4} δ_{i+kp} ≡ 4δ_i + 6 ≡ 0 mod 2. Hence W ≡ 0 for every z.
- PROVED: pat_z = (z_0+z_2) mod 2 = (z_1+z_3) mod 2, i.e. 1 iff z is
  non-constant mod 4 (direct check on all 16 patterns).
- VERIFIED (exact, all on-support split fibers, 32→64 and 64→128):
  max p (= N/4): U′ = pat_z, W = 0; non-max p: U′ = 0, W = 0.
  U′ here equals wave 37's pat exactly, in the same row order.
- REDUCTION: non-max follows from U ≡ 0 mod Q/4, since then
  U′ = (N/p)(U/Q) = (N/4p)·k with N/4p ≥ 2 even. So (b) is exactly:
  U-LEMMA: for max-period y, U ≡ (Q/4)·pat_z (mod Q/2).
  Equivalent σ-form: with class sums S_r = Σ_{k<p/4} y_{4k+r} and
  σ_r = 16S_r/Q, Σ_r z_r σ_r ≡ 4·pat_z (mod 8) for all 16 patterns
  (e.g. fiber 3 at m = 32: σ ≡ (0,4,0,4) mod 8, so the sum is
  4(z_1+z_3); fiber 74: σ ≡ (1,7,1,7), sum ≡ 2a+6b with
  a+3b ≡ 2·pat_z mod 4 — the condition is on σ mod 8, not general).

Verdict (b): proved modulo the U-lemma (one exact statement) + (a).

## (c) Birth stability — proved modulo (a)'s converse

- PROVED: M⁴−I = [[1188,−204],[204,−36]], det = −1152, gcd of entries
  12, so SNF diag (12,96). Hence exactly 128 period-dividing-4 points
  at every level j ≥ 2 (gcd(12,Q) = 4, gcd(96,Q) = 32), all of the form
  y = (Q/32)·Ŷ, with the Ŷ-set fixed (M^i mod 32 is fixed). Verified:
  128 points and identical Ŷ-set at m = 32 and m = 64.
- PROVED (finite check on fixed data): all 128 Ŷ-types are on-support
  at every level. Support for y = (Q/32)Ŷ is y·z = NQ·ΣŶ_r z_r/128,
  so it is N·ΣŶ_r z_r ≡ 0 mod 128: automatic for j ≥ 7, a mod-4 check
  at j = 5, a mod-2 check at j = 6 — 0 violations in 2048 checks.
- PROVED: e is j-independent (Ŷ fixed integers, e_i = (Ŷ-diff)/32
  mod 4). A 4-periodic δ^part need NOT exist (112/200 period-≤4 points
  fail the image conditions e_0 ≡ e_2, e_1 ≡ e_3 mod 2 and alternating
  sum ≡ 0 mod 4) — instead δ has block drift δ_{r+4} = δ_r + C + D·r
  (mod 4), with (C,D) well-defined (ker L = {A+Bi} shifts C by 4B ≡ 0,
  leaves D). Along class r, δ_{4k+r} = δ_r + k(C+Dr) mod 4, so the lift
  multiset is (N/8) copies of a fixed multiset determined by
  (Ŷ, δ_r, C, D) — all j-independent. Full collision is therefore
  level-independent: it holds iff no class has C+Dr ≡ 0 and the
  "2-classes" have balanced parity.
- VERIFIED: exactly 10 fully-colliding period-≤4 orbits at m = 32 and
  m = 64, identical Ŷ-types, sizes 8,8,8,4,4,2,2,2,1,1, periods
  4,4,4,4,4,2,2,2,1,1 (matching wave 37's accounting):
  (0,8,16,24), (2,14,18,30), (6,26,22,10) [p = 4, size 8];
  (4,20,20,4), (12,12,28,28) [p = 4, size 4];
  (0,16,0,16), (4,28,4,28), (12,20,12,20) [p = 2, size 2];
  (8,8,8,8), (24,24,24,24) [p = 1, size 1].
  Their (C+Dr) are (3,1,3,1), (3,3,3,3), (2,2,2,2); all 29 other
  period-≤4 orbits have a 0-class and do not collide. The (2,2,2,2)
  cases collide by parity balance (2 even, 2 odd classes).
- The only non-period-≤4 input: no p ≥ 8 non-split orbit fully
  collides. This is (a)'s converse (non-split ⟹ drift even), since
  drift odd is what the drift-multiset theorem needs for p ≥ 8.

Verdict (c): the period-≤4 part (exactly 10 births, same types at
every level) is proved unconditionally; the full birth rule needs
(a)'s converse for the p ≥ 8 exclusion.

## Bottom line

No counterexample to any gap. T_k = 5(k−4) now rests on exactly three
named statements: reversal exclusion (|E_alt| < 8), the Split Bit
Lemma (split ⟹ ν = (1,1)), and the U-lemma
(U ≡ (Q/4)·pat_z mod Q/2 for max-period fibers). Everything else
behind P, S, B is proved above or was proved in wave 37.
Scripts: wave38_explore_b.py, wave38_explore_b2.py,
wave38_explore_c.py, wave38_explore_c2.py (exact integer checks).
