# Wave 45, task 5 — Mod-16 digit rule for t-agreement at j ≥ 9: PROVED at j = 9

## Verdict

The mod-16 digit rule is proved at j = 9 (m = p = 512), and it corrects
wave 43: the size-4 class contributes 0, not ±4 — its t-values always
split 2–2 — and the Gap G witnesses are the two size-2 classes, each
contributing ±4 always. The general-j form of the rule is the single
congruence E_m + 4δ_E ≡ 0 (mod 2^{j−6}) for small-class reps (§7).

## 0. Setup and inputs

Q = 8m², m = 2^K, minimal period p = 2^j, ν = (1,0), w_k = y_{2k+1}
(34-recurrence, period p/4). Quarter indices k < p/8, classes
v_k = w_k mod (Q/2), t_k = top bit of w_k. Pairs (j, j + p/16),
j < p/16; a pair with ε_j = 0, φ_j = 0 contributes 2(1 − 2t_j) to
2B_c − A_c of its class, all other pairs contribute 0 (waves 41–43).
Shift-8 operator, normalized by μ_3 = Q/2^{j−5} (so μ_3 = Q/16 at
j = 9): E_k = (w_{k+8} − w_k)/μ_3 mod 2^{j−5}. Inputs, all from
waves 42–44 or verified below: (DIV) shift-8 divisibility by μ_3;
(PAR) y_0 = step0·t, y_1 = step0·u, step0 = Q/(8p), t odd, and
u ≡ 11t (mod 16) (wave 44, from DIV at s = 2); (ψ) φ = 0 pair
representatives ("reps") number 2^{j−6}, spaced 4 apart (wave 43
ψ-analysis); (B3) the mod-8 slope along reps alternates, i.e.
E_{r+4} − E_r ≡ 4 (mod 8) — proved as Lemma 1 below.

## 1. Slope lemma: δ_E is odd (all j)

E_k satisfies the 34-recurrence divided by μ_3, hence
E_k ≡ E_0 + kδ_E (mod 2^{j−5}) with δ_E = E_1 − E_0. Now
w_8 − w_0 = (P_{17} − 1)y_1 − P_{16}y_0 and
w_9 − w_1 = (P_{19} − 35)y_1 − (P_{18} − 6)y_0 (P_n the Pell
numbers, P_3 = 35, P_2 = 6), and μ_3 = 256·step0 for every j
(since Q = 8p·step0). Hence δ_E = (Xu − Yt)/256 with
X = P_{19} − P_{17} − 34 = 2^9·117667008189 and
Y = P_{18} − P_{16} − 6 = 2^8·40376933835 (wave 43 values,
recomputed exactly). So δ_E = 2·X_odd·u − Y_odd·t with X_odd,
Y_odd odd; u is odd (u ≡ 11t, t odd), so δ_E is odd.
Consequences used below: E_{k+8} − E_k = 8δ_E ≡ 8 (mod 16), and
E_{r+4} − E_r = 4δ_E ≡ 4 (mod 8) along reps. (Correction to an
earlier draft computation: δ_E mod 8 varies with t mod 8 —
values {1,3,5,7} observed — only oddness is claimed.)

## 2. Flip lemma (exact, all j)

Let w_k = (Q/2)t_k + ρ_k, 0 ≤ ρ_k < Q/2, and let the shift-8 step
from k use digit e = E_k mod 2^{j−5} (so w_{k+8} = (w_k + μ_3·e)
mod Q, 0 ≤ μ_3·e < Q). Put β = ρ_k/μ_3 ∈ [0, 2^{j−6}) (real).
Then t_{k+8} ⊕ t_k = 1 ⟺ Q/2 ≤ ρ_k + μ_3·e < Q, i.e.
⟺ 2^{j−6} − β ≤ e < 2^{j−5} − β. Proof: if t_k = 0, w_{k+8} =
(ρ_k + μ_3 e) mod Q is ≥ Q/2 exactly on that interval (the sum
is < 3Q/2, so at most one wrap); if t_k = 1, w_{k+8} =
(Q/2 + ρ_k + μ_3 e) mod Q flips exactly when the sum crosses
Q or 3Q/2, i.e. on the same interval. ∎
At j = 9 (μ_3 = Q/16, e ∈ {0,…,15}, β ∈ [0,8)): flip ⟺
8 − β ≤ e < 16 − β. In particular complementary digits e and
e + 8 (mod 16) with the same β always flip oppositely: if
e < 8, e flips ⟺ e ≥ 8 − β while e + 8 flips ⟺ e < 8 − β;
if e ≥ 8, e flips ⟺ e < 16 − β while e − 8 flips ⟺ e ≥ 16 − β.

## 3. Big class: digits alternate, t splits 2–2, contribution 0

Reps r_i = j* + 4i, i < 2^{j−6}. By Lemma 1, E mod 8 alternates
along reps: one parity has E ≡ 0 (mod 8), the other E ≡ 4 (mod 8).
At j = 9, members of the E ≡ 0 (mod 8) parity chain by shift-8
into ONE class of size 4 (each step digit ≡ 0 mod 8, so
v_{k+8} = v_k); the E ≡ 4 (mod 8) parity splits into TWO classes
of size 2 (two Q/4 steps make Q/2 ≡ 0).
Along big-class members (spaced 8 apart), step digits are
E_m, E_m + 8δ_E, E_m + 8δ_E, … ≡ d, d + 8, d, d + 8 (mod 16)
since 8δ_E ≡ 8 (mod 16). By Lemma 2 with fixed β (same class),
consecutive flips are f, 1 − f, f, 1 − f, …, so each block of
4 consecutive members has t-pattern (t, t⊕f, t⊕1, t⊕1⊕f) —
a 2–2 split. The big class has size 4, hence total contribution
0. The observed patterns are exactly D = (8,0,8,0)/(0,8,0,8)
with t = (0,1,1,0)/(0,0,1,1)/(1,1,0,0)/(1,0,0,1).

## 4. Small classes at j = 9: equal t, contribution ±4

A small class is {m, m + 16} (m an E ≡ 4 mod 8 rep). Now
w_{m+16} − w_m = μ_3(E_m + E_{m+8}) = μ_3(2E_m + 8δ_E).
Since m, m + 16 share a class, t_{m+16} = t_m ⟺
w_{m+16} − w_m ≡ 0 (mod Q) ⟺ 2E_m + 8δ_E ≡ 0 (mod 16)
⟺ E_m + 4δ_E ≡ 0 (mod 8). But E_m ≡ 4 (mod 8) and
4δ_E ≡ 4 (mod 8) (δ_E odd), so the sum is 0 mod 8. ∎
Hence each small class contributes 2(1 − 2t_m) + 2(1 − 2t_m)
= ±4 always. At j = 9 the observed small-class patterns are
D = (4,4)/(12,12) with t = (0,0)/(1,1) — equal digits and
equal t, as proved. Every point therefore has two ±4
witnesses, so Gap G holds at j = 9.

## 5. Corrections to wave 43

Wave 43 §4 reported class values {0, +4, −4}; the exact census
(all 524288 points at (512,512)) gives (−4,−4,0), (−4,0,4),
(0,4,4) — i.e. one class 0 (the big class) and two classes
±4 independently (the small classes). Wave 43 §5's claim that
"the size-4 class contributes ±4, i.e. a 3–1 t-split" is false:
the size-4 class always splits 2–2 and contributes 0. The
conclusion (Gap G at j = 9, Split Bit Lemma unconditional at
m = 512) is unaffected — it now has two witnesses per point
instead of one.

## 6. j = 10: the mod-16 rule, proved (not just sampled)

Step-16 sharing at general j needs E_m + 4δ_E ≡ 0 (mod 2^{j−7})
(w_{m+16} − w_m = μ_3(2E_m + 8δ_E) ≡ 0 mod Q/2); t-equality
needs one more bit, E_m + 4δ_E ≡ 0 (mod 2^{j−6}). At j = 10:
sharing is automatic (E_m ≡ 4 mod 8, 4δ_E ≡ 4 mod 8), and
t-equality is the mod-16 condition E_m ≡ −4δ_E (mod 16).
The two step-16 classes have E mod 16 = 4 and 12 (they differ
by 8δ_E ≡ 8, since their rep-indices differ by 2), and
−4δ_E mod 16 is one of {4, 12} — so exactly one step-16
class has constant t (±8 witness), the other alternates (0).
The other two classes are mixed (spacings 8, 24, 8; E mod 16
alternating 0, 8; linked by step-8 digits ≡ 0 mod 16 and
step-24 digit-sums ≡ 0 mod 16); they always split 2–2
(contribution 0, full census), but that is not needed for Gap G.
Caution: §3's big-class block argument does NOT generalize —
at j ≥ 10 the step digits are not complementary pairs, so the
2–2 block split is a j = 9 fact; the j ≥ 10 witness is the
step-16 class above, not a big class.

## 7. General j: statement and remaining step

Theorem (modulo DIV, PAR, ψ-analysis, slope lemma): at every j ≥ 9,
Gap G follows from the step-16 witness condition E_m + 4δ_E ≡ 0
(mod 2^{j−6}), proved at j = 9 (both classes, ±4 each) and j = 10
(exactly one, ±8). Remaining step for j ≥ 11: existence of a
sharing step-16 class with E_m ≡ −4δ_E (mod 2^{j−6}) (at j = 10
the two classes take both lifts 4, 12; in general the E-orbit
over sharing classes must be shown to hit the witness lift).

## Checks

- wave45_mod16_explore.py: full census at (512,512) — 524288
  points, all valid, reps_8 everywhere, class sizes (2,2,4)
  everywhere, D_nondiv = eps_non01 = phi_nondiv = 0.
- wave45_mod16_verify.py (2048 sampled points): Pell formulas
  for E_0 and δ_E exact (0 violations mod 16); arithmetic
  progression mod 16 exact (0/262144); flip lemma exact
  (0/262144); small-class t-equality and big-class 2–2 exact.
- wave45_mod16_j10 full census at (1024,1024): 2097152 points,
  all valid, reps_16 everywhere, sizes (4,4,4,4), contributions
  (−8,0,0,0) × 1048576 and (0,0,0,8) × 1048576 — exactly one
  ±8 witness per point; mixed classes always 2–2 (0).
- wave45_mod16_j10_inspect.py: step-16 vs mixed structure verified
  point by point; no Lean built, repository untouched.
