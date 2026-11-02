# Wave 39, task 4 (retry) — Reversal exclusion at minimal p = 8: PROVED under "split"

Verdict: |E_alt| < 8 is FALSE unconditionally (exact counterexample, §2),
but TRUE for split points at every level (theorem, §3). Split is the
operative hypothesis: reversal exclusion is needed for the ν=(1,1) ⟹ split
argument, and ν=(1,1) points are the split points (wave-38 data).

Setup: level j ≥ 3, m = 2^j, Q = 2^{2j+3}. y is a kernel point of minimal
period 8 (so 8 | N); A = Σ_{i<8}(−1)^i y_i (canonical reps), A = (Q/8)·E_alt.

## 1. Reduction to mod 64 (proved)

M = [[6,−1],[1,0]], M^8 − I = 408·K, K = [[3363,−577],[577,−99]], det K = −8.
Period 8 gives K·(y_1,y_0) ≡ 0 mod 2^{2j} (408 = 8·51, 51 odd), hence
(y_1,y_0) = 2^{2j−3}·[[99,−577],[577,−3363]]·t. So y_0, y_1, and by the
recurrence every y_i, are divisible by 2^{2j−3}. Write y_i = 2^{2j−3}·z_i,
z_i ∈ [0,64). Then z satisfies the recurrence mod 64 cyclically, has
minimal period 8, and E_alt(y) = A_z/8 with A_z = Σ(−1)^i z_i (so
|E_alt| < 8 ⟺ |A_z| < 64). Splitness also descends exactly: the fiber of
y is the 8-multiset of z repeated N/8 times (scaling is injective), and
Γ-orbits of y are dihedral orbits of z (shifts/reversals act mod 8).

## 2. Unconditional claim is FALSE

Seed (z_0,z_1) = (1,11) mod 64 gives z = (1,11,1,59,33,11,33,59),
A_z = −72, E_alt = −9. It lifts to every level j ≥ 3 (y = 2^{2j−3}z);
at m = 32 it is a genuine kernel point, nonsplit (1 orbit), E_alt = −9.
Consistent with m = 32 data: nonsplit-onsup p = 8 points reach E_alt = ±15.

## 3. Theorem: split p = 8 points have |E_alt| ≤ 6

(a) Exact classification (384 minimal-period-8 z-sequences, 37 multisets):
exactly 5 multisets are split, all even-valued; split ⟺ all z_i even
(128 sequences each). The two orbits in each split multiset are odd-flip
partners (z ↦ z + 32·[i odd]), as in wave 38.
(b) Bound for all-even z (structural). Write z = 2w, w mod 32, minimal
period 8. Even/odd subsequences of w are APs mod 32 with differences
d, d' ≡ 0 mod 8 (from w_{k+1} = 34w_k − w_{k−1}, i.e. 2w_k − w_{k−1} mod 32,
cyclic over 4 terms). If d = 0 then o_1 = o_3 (from o_k = 6e_0 − o_{k−1}),
so 2d' ≡ 0 mod 32, d' ∈ {0,16}, and w has period 4 — contradiction;
symmetrically d' ≠ 0. Hence d, d' ∈ {8,24}. The four even values are
{r, r+8, r+16, r+24}, r = e_0 mod 8, summing to 4r + 48; likewise odds sum
to 4r' + 48. So A_w = 4(r − r'), |A_w| ≤ 28. Mod 8, w is 2-periodic
(w_2 ≡ w_0, w_3 ≡ w_1, using w_0 + w_1 ≡ 0 mod 4 from K·state ≡ 0 mod 4),
so A_w ≡ 4(w_0 − w_1) ≡ 0 mod 8. Hence A_w ∈ {0,±8,±16,±24},
A_z = 2A_w ∈ {0,±16,±32,±48}, E_alt ∈ {0,±2,±4,±6}, |E_alt| ≤ 6 < 8.

## 4. Verification

m = 32 and m = 64: exactly 128 split-onsup p = 8 points each, with
E_alt ∈ {0,±2,±4,±6} — identical, as the reduction predicts.

Caveat: this proves |E_alt| < 8 (E_alt ≠ 8), the form wave 38 uses for
reversal exclusion. A residue-only reading of the reversal constraint
(A ≡ pQ/8 mod Q/2, i.e. E_alt ≡ 0 mod 4 at p = 8) is not excluded by this
alone for the E_alt = ±4 cases, and c-even reversals need a separate
argument; those are outside this task's statement.

Check script: wave39_ReversalExclusion_p8_check.py. No Lean, repo untouched.
