# Wave 25, task 2: RB1 repaired — twin identity mechanism proved, RB1 restated

## Verdict

The wave-24 refutation is explained, not patched over. The (6,7)-twin
identity has an exact mechanism: a **β-order criterion**. RB1 is
restated as RB1' with multi-point twin-qt fibers, and the corrected
bound is proved **conditionally on one named lemma** (Twin Sum).
Unconditional polynomiality of the corrected count is open, with the
obstruction stated exactly. Repository untouched; no Lean build.

## 1. Twin data (verified from wave-24 files)

Split 81-fiber: 3 orbits of 12, gam labels 5, 6, 7. Reps a6, a7 are
12-periodic; a7 = a6 ∘ σ where σ fixes odd positions and rotates
even positions by 8 within 12-blocks (so σ(i) ≡ i+8 mod 12 for even
i, σ(i) = i for odd i). a7 − a6 is divisible by 27, zero on odds.
a6 evens: [9,45,63,72,36,18] repeating (6-periodic in j).

## 2. Mechanism theorem (proved)

Let β = α² = 17+12√2, and let y = CRT(p0, a, t) over components
(2048, 81, qt), other components 0, with a ∈ {a6, a7}.

**Theorem.** If there is N = 6k+4 such that the β-shift S^N is the
identity on the even subsequences of all p0 and all t, then
sorted CRT(p0, a6, t) = sorted CRT(p0, a7, t) for all p0, t.

*Proof.* Odd coordinates: σ fixes odds, so a7 = a6 there and
y' = y on all odd positions exactly. Evens: write j for even index
(i = 2j, j ∈ Z_24). Since a6 is 12-periodic, a7's even subsequence
is a^{ev}_{j+4}. So y'^{ev}_j = CRT(p^{ev}_j, a^{ev}_{j+4}, t^{ev}_j).
Substituting j' = j+4, multiset(y'^{ev}) =
multiset_{j'} CRT(p^{ev}_{j'−4}, a^{ev}_{j'}, t^{ev}_{j'−4}).
If S^N = id with N = 6k+4, then p^{ev}_{j'−4} = p^{ev}_{j'+6k} and
t^{ev}_{j'−4} = t^{ev}_{j'+6k} (since p_{j'+6k} = p_{j'+6k−N}).
The map φ(j') = j'+6k permutes Z_24 and preserves j' mod 6, hence
preserves a^{ev}; so the two multisets coincide. ∎

Shift lemma used: for a β-sequence (e_{j+1} = 34e_j − e_{j−1}),
write S^N = A_N + B_N S in (Z/q)[S]/(S²−34S+1). Then S^N = id on a
set E iff (A_N−1)e_j + B_N e_{j+1} = 0 for all e ∈ E, j. If
gcd(12,q) = 1, then (A_N,B_N) = (1,0) ⟺ β^N = 1 in R_q, since
β^N = (A_N+17B_N) + 12B_N√2.

**Criterion.** Multiples N of ord_q(β) with N ≡ 4 mod 6 exist iff
gcd(ord_q(β), 6) | 4 iff 3 ∤ ord_q(β). So the twin identity is
available at qt exactly when 3 ∤ ord_qt(β) (plus the 2-part
condition, which holds at m = 48, see §3).

## 3. Order table and side verifications (exact)

ord(β) in R_q, computed exactly:

| q | ord(β) | 3 \| ord | twin? |
| 2048 | 512 | no | (2-part, see below) |
| 289 = 17² | 68 | no | YES |
| 332929 = 577² | 4616 | no | YES |
| 25, 49, 121, 9409, 1329409 | 15, 21, 66, 2328, 13836 | yes | no |
| 13729² (big comp.) | 24 mod 13729 | yes | no |

Joint N values: (2048, 289): N = 8704 = lcm(512, 68), 8704 ≡ 4
mod 6. (2048, 332929): N = 590848 = 2·lcm(512, 4616), ≡ 4 mod 6.
qt-side: (A_N, B_N) = (1, 0) mod qt in both cases, so S^N = id on
all t-sequences; verified directly: shift identity holds for
289/289 and 332929/332929 t-sequences.
2048-side: every mod-2048 Fix sequence is 16-periodic in i
(verified exactly on all 2048 points; seeds p0, p1 are even), so
p_{j−4} = p_{j+12} on even subsequences, and 6k ≡ 12 mod 24 in
both cases (1450 ≡ 98474 ≡ 2 mod 4). Hence the theorem applies.
Exact CRT check: sorted equality holds 6/6 at qt = 289, 332929.

## 4. Failure direction

If 3 | ord_qt(β), no N ≡ 4 mod 6 has β^N = 1 (ord | N would force
3 | N, but N ≡ 4 mod 6 gives N ≡ 1 mod 3), so the shift argument
cannot work. This matches the sweep exactly: 0 survivors at every
non-twin qt. The twin set at m = 48 is therefore exactly
{17², 577²} — by the orders, not by luck of sampling.

## 5. RB1' (corrected restatement)

**RB1'.** Every contributing global fiber is a product of one
split 3-component fiber, one supported 2-component fiber, one
fiber f_qt of a single other component qt with 3 ∤ ord_qt(β)
(a *twin* component; singletons are the degenerate case f_qt = 1
point), and singletons elsewhere. Joint-nonzero families (two
non-singleton other components) remain excluded only by the
CRT-injectivity sketch, as before.

## 6. Corrected counting and conditional theorem

At m = 48: twin fibers number 27 (qt = 289, sizes ≤ 16) and 10693
(qt = 332929, sizes ≤ 32); products 39 × (27+10693) = 418080;
max global fiber size ≤ 36 × 8 × 32 = 9216; twin-product points
≤ 128 × 36 × (289+332929) ≈ 1.54×10⁹; hence ΣΔ_F ≤ 1.41×10¹³
against the actual ≈ 4.44×10¹¹ (32× slack).

**Conditional theorem.** Assume RB2, RB3, RB1', a bound
max |f_qt| ≤ m^b over twin qt, and the **Twin Sum Lemma**
Σ_{twin qt | D_m} qt = o(D_m). Then ΣΔ_F ≤
(8m² · m · Σ qt) · (4m² · 8 · m^b) = o(D_m), so Δ(m) → 0.

**Why unconditional polynomiality is open.** F(qt) ≈ qt/31 at
m = 48 (10693 fibers over 332929 points), so the corrected count
is controlled by Σ qt over twin qt, and twin qt are a priori
unbounded: the mechanism bounds no twin prime power. The worst
case — one twin qt comparable to D_m — is not ruled out
elementarily. Near-misses: D_m = 2p² is impossible (p odd gives
p² − 8Z² = −2, impossible mod 8), and at m = 48 the largest
component 13729² is not twin (ord 24), so the twin sum there is
tiny by the orders, not by a general theorem.

## 7. Status (independent of the enumeration)

The full (1,2) enumeration is running (relaunched 17:40, now
14000/418080 pairs, partial deficit 14833080288, mean/pair
≈ 1.06×10⁶, consistent with the wave-24 estimate 4.44×10¹¹).
The mechanism proved here does not depend on its outcome: the
identity holds for every product regardless of the total.
