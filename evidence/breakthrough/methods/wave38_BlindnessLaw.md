# Wave 38, task 2 — Blindness Law in general

## Verdict

Two blindness mechanisms are proved with exact criteria, verified at m = 60, 120, 180.
Consequence for SCJ: the scaling move gives a polynomial B(m) bound, but the
top-digit move gives B(m) ≥ D_{3t} (t = 3-free part of m) — exponential in t.
The B(m) counting route to polynomial SCJ is therefore dead; polynomial SCJ
itself is NOT refuted (B(m) is an upper-bound device; most blind configurations
need not occur as joint fibers with Δ_F > 0).

## 1. Fiber criterion (proved, general)

Fix locked rep a, free orbit reps b, b′, sequence o at q0. Then o is blind for
b→b′ iff b, b′ agree as multisets on every fiber I_v of i ↦ (a_i, o_i):
grouping triples (a_i, b_i, o_i) by v = (a_i, o_i), equality of triple
multisets ⟺ {b_i : i ∈ I_v} = {b′_i : i ∈ I_v} for every v. Dihedral τ give
same-orbit b′, so blindness needs a non-dihedral agreement.

## 2. Scaling law (proved mechanism)

Setup: free orbits related by integer scalings w ↦ u·w mod p^f (625 at
m = 60/120/180: b = 25·w, w_j = u_j·w_0, u ∈ {1,4,6,9,11}).
Coset lemma: on each mod-d_a class (d_a = locked period), t takes a full
coset {c + p·j} (from α^{d_a} ≡ 1 + p·w mod p^f, w a unit √2-multiple, plus
the norm argument excluding x ≡ 0 mod p: −2y² ≡ 1 mod p impossible).
Hence u ≡ 1 mod p permutes every coset, so it is invisible on any union of
mod-d_a classes. Theorem: blind ⟺ period(o) | d_a and ratio ≡ 1 mod p
(the ⇐ direction is the coset argument; ⇒ for ratios is verified: ρ ≡ −1
swaps cosets 2↔3 and fails 4/6 a-fibers at m = 60).
Verified exactly: m = 60 (d_a = 12): 49: 48/48, 121: 120/120, 361: 0, 841: 0;
m = 120 identical (same C's); m = 180 (locked 729, d_a = 36): 49: 48/48,
121: 120/120, 361: 0 (20 ∤ 36), 841: 0 (10 ∤ 36).
Colliding ratios at m = 60 are exactly {6, 11, 21} (≡ 1 mod 5); {4, 9, 14}
(≡ −1 mod 5) never collide.

## 3. Top-digit law (proved mechanism, 3-adic)

Setup: free orbits related by ΔC divisible by 3^5 at 3^6 (729 at m = 180:
C = 27·(14 + k√2), colliding pairs exactly k ↦ k−9, i.e. C ↦ C − 243√2).
Key congruence: α^{12} ≡ 1 + 9√2 mod 27. Hence w_{j+12} ≡ w_j + 9L_j with
L_j = k·x_j + 2y_j mod 3, and L_{j+12} = L_j. Norm x² − 2y² = 1 mod 3 forces:
y ≢ 0 ⟹ x ≡ 0 ⟹ L = 2y ≢ 0; y ≡ 0 ⟹ shift is 0. So every 12-triple
{w_j, w_{j+12}, w_{j+24}} is a full mod-9 class (permuted by +9 shifts) or
constant with zero shift — invisible to the move. Theorem: blind ⟸ every
(a,o)-fiber is a union of 12-triples; for locked period d_a with
v_3(d_a) ≤ 1 this holds iff v_3(period(o)) ≤ 1 (via gcd(lcm(d_a,d_o),36) | 12).
Verified at m = 180 (locked 625, d_a = 30): blind for ALL nonzero o at
49 (48/48), 121 (120/120), 361 (360/360), 841 (840/840), 1681 (150/150 sampled),
3481 (150/150), 72361 (150/150) — periods 3, 12, 20, 10, 5, 20, 30, all | 60;
pinning at 5329 (0/5328 FULL), 38809 (0/38808 FULL), 32041, 39601 (0/40
sampled) — periods 36, 18, 9, all with v_3 = 2.

## 4. Mid-digit moves pin

81-orbits differ by 9-multiples in C (not top-digit 27); blind81 = 0 for all
o at all tested components (m = 60, 120). Mechanism sketch: (625,o)-fibers
have size ≤ 2 while 9-differences generically break pairs. General proof open.

## 5. Counting: scaling polynomial, top-digit exponential

Blind sequences at q0 = p^e for scaling: period | d_a ⟺ C(α^{d_a}−1) = 0
((Tr, Tr∘α) injective, p odd), count ≤ p^{v_p(D_{d_a})}; product over q0
≤ D_{d_a}; free sets ≤ 2^{ω(m)} ≤ m. So scaling-only B(m) ≤ m·D_{d_a}:
polynomial for bounded d_a (at m = 60: B = 49·121 = 5929 exactly).
Top-digit: blind count at q0 = |Ann(α^{3t}−1) mod p^e| = p^{v_p(D_{3t})}
(t = m/3^{v_3(m)}), product = D_{3t} ~ ρ^{3t}. Rigorous at m = 180:
seven confirmed non-split, confirmed all-blind components give
B(180) ≥ 49·121·361·841·1681·3481·72361 = 762185960484837066409
≈ 7.6×10^20 > 180^9, killing c_J ≤ 8 (wave-35 hope) and ≤ 9.
Full D_{60} ≈ 10^48 > 180^21 if 923521, 361201, 5202961 are also non-split
and all-blind (predicted by the annihilator count; 923521 not directly
tested — kernel enumeration over 923521 points too slow in Python).

## 6. Hypotheses and falsification

The polynomial-B(m) claim survives only under: (H1) every free move is
scaling, top-digit, or pinning mid-digit; (H2) locked periods d_a bounded
(or O(log m)); (H3) no scaling-blind sequence with period ∤ d_a;
(H4) no top-digit-blind sequence on non-triple fibers in bulk.
Falsification of the exponential-B conclusion would need: 729-type splits
with top-digit moves absent along m = 9t (splits verified at m = 36, 180
only), or the locked component having v_3(d_a) ≥ 2 (then the move pins
everywhere by the gcd criterion). What remains open for SCJ: a counting
argument not routed through B(m), or a proof that most blind configurations
do not occur as joint fibers with Δ_F > 0.

## Limits

No Lean built; repository untouched. Scaling law verified at m = 60, 120, 180;
top-digit law at m = 180 (8 blind + 4 pinning components). General proofs of
the ⇒ directions (ratios, triple-necessity) and of mid-digit pinning are open.
Scripts: wave38_blind_explore*.py, wave38_blind_m120.py, wave38_blind_m180.py,
wave38_blind_m180_invest.py, wave38_blind_m180_pairs.py,
wave38_blind_m180_med.py, wave38_blind_m180_full.py, wave38_blind_m180_splits.py,
wave38_blind_m180_D60.py (partial: 923521 unfinished).
