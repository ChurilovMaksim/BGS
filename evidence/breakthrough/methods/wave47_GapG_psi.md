# Wave 47, task 7 — ψ-analysis in general: PROVED

## Verdict

ψ-analysis is **proved in general** for j ≥ 7 (j ≤ 2K), for every
ν = (1,0) sequence — minimality of p is never used, as with DIV/PAR
(wave 46 §5). The only new ingredient is the pinning lemma (§4);
everything else is PAR + DIV (both proved in general, wave 46 —
**not** listed as open), the 34-recurrence for w, and Pell
valuations/residues (waves 44/46). Consequence: the rep structure
the mod-16 digit argument uses — 2^{j−6} reps, spaced exactly 4
apart, ψ alternating on parity classes — now holds unconditionally.

## 1. Setup

Q = 8m², m = 2^K, p = 2^j, w_k = y_{2k+1} (34-recurrence mod Q,
w_{k+1} = 34w_k − w_{k−1}), quarter indices k < p/8, pairs
(j, j+p/16), j < p/16. Quarter defect: w_{k+p/8} − w_k = (Q/2)ε_k;
φ_k = (w_{k+p/16} − w_k)/(Q/4) mod 4. Claims: (i) φ affine mod 4
with odd slope; (ii) φ_k ≡ ε_k (mod 2); (iii) φ_k + φ_{k+p/16}
≡ 2ε_k (mod 4); ψ_k := (φ_k − ε_k)/2 mod 2 alternates on each
parity class; reps {j < p/16 : ε_j = φ_j = 0} number 2^{j−6},
spaced 4 apart. (Wave 42 proved this only at m = 128, via
m-specific parametrisations; wave 43 stated it as input.)

## 2. Well-definedness: DIV at s = j−4 and s = j−3

Wave 46 §3 proves DIV for 2 ≤ s ≤ j−4, but its proof uses only
s ≥ 2 (shift identity with r = s+1 ≥ 3; L_n ≡ 0 mod 16 from ν
at odd n). Hence it extends verbatim to s = j−3 (j ≥ 5):
w_{k+2^{j−3}} − w_k divisible by Q/2, i.e. ε_k is well-defined
mod 2; and at s = j−4, φ_k is well-defined mod 4. (Checked:
DIVphi = DIVeps = 0 at all points in Checks.)

## 3. Recurrences: φ affine, ε 2-periodic

d_k = w_{k+p/16} − w_k satisfies the 34-recurrence, so dividing
by Q/4: φ_{k+1} ≡ 34φ_k − φ_{k−1} ≡ 2φ_k − φ_{k−1} (mod 4).
Hence differences are constant: φ_k ≡ φ_0 + k·d (mod 4),
d = φ_1 − φ_0. Similarly e_k = w_{k+p/8} − w_k satisfies the
recurrence, so dividing by Q/2: ε_{k+1} ≡ 34ε_k − ε_{k−1}
≡ ε_{k−1} (mod 2): the even and odd subsequences are each
constant. Alternation of ε is therefore equivalent to the
pinning ε_1 ≠ ε_0, proved next.

## 4. Pinning lemma: ε_1 ≡ ε_0 + 1 (mod 2) — NEW

Let D = 2^{j−2} = p/4. Then w_{p/8} = y_{D+1}, w_0 = y_1,
w_{1+p/8} = y_{D+3}, w_1 = y_3, so e_0 = y_{D+1} − y_1,
e_1 = y_{D+3} − y_3. Pell matrix T^D =
[[P_{D+1}, −P_D], [P_D, −P_{D−1}]] gives
y_{n+D} − y_n = P_D·y_{n+1} − (P_{D−1}+1)·y_n.
At n = 1, 3: e_0 = P_D·y_2 − (P_{D−1}+1)·y_1,
e_1 = P_D·y_4 − (P_{D−1}+1)·y_3.
PAR (wave 46): y_i = step0·ỹ_i, ỹ_0 = t odd, ỹ_1 = u,
u ≡ 11t (mod 16); ỹ_2 = 6u − t, ỹ_3 = 35u − 6t,
ỹ_4 = 204u − 35t. Valuations (waves 44/46): v_2(P_D) =
v_2(P_{D−1}+1) = j−2; write e_2 = P_D/2^{j−2} ≡ 3 (mod 16),
f = (P_{D−1}+1)/2^{j−2} odd. Then e_i = step0·2^{j−2}·L_i with
L_0 = e_2·ỹ_2 − f·u, L_1 = e_2·ỹ_4 − f·ỹ_3; DIV (§2) gives
L_i ≡ 0 (mod 16) and ε_i = L_i/16 mod 2 (Q/2 = step0·2^{j+2}).
Difference: L_1 − L_0 = e_2(198u − 34t) − f(34u − 6t).
Mod 32: e_2(198u − 34t) ≡ 3(198u − 34t) ≡ 18u + 26t ≡ 0,
using u ≡ 11t (mod 16) (18u ≡ 6t, 6t + 26t ≡ 0); and
f(34u − 6t) = 2f(17u − 3t) with 17u − 3t ≡ u − 3t ≡ 8t
(mod 16), so f(34u − 6t) ≡ 16ft ≡ 16 (f, t odd).
Hence L_1 − L_0 ≡ −16 ≡ 16 (mod 32), so (L_1 − L_0)/16 is
odd: ε_1 − ε_0 ≡ 1 (mod 2). ∎
Corollary: ε alternates, ε_k ≡ ε_0 + k (mod 2).

## 5. (ii), odd slope, rep structure, ψ

(iii): w_{k+p/8} − w_k = d_k + d_{k+p/16} gives, dividing by
Q/4, 2ε_k ≡ φ_k + φ_{k+p/16} (mod 4). By §3,
φ_{k+p/16} ≡ φ_k + (p/16)d ≡ φ_k (mod 4) for j ≥ 6
(p/16 ≡ 0 mod 4), so 2φ_k ≡ 2ε_k (mod 4): (ii) holds.
Then d = φ_1 − φ_0 ≡ ε_1 − ε_0 ≡ 1 (mod 2) by §4: d odd.
So φ_k ≡ 0 (mod 4) ⟺ k ≡ k* (mod 4) for a unique k* (d
invertible mod 4); φ_k = 0 ⟹ ε_k = 0 by (ii). Reps:
{j < p/16 : φ_j = 0} = {j < p/16 : j ≡ k* (mod 4)},
count (p/16)/4 = 2^{j−6}, consecutive diffs exactly 4. ∎
ψ: ψ_{k+2} = (φ_{k+2} − ε_{k+2})/2 = ψ_k + d ≡ ψ_k + 1
(mod 2), using φ_{k+2} = φ_k + 2d and ε_{k+2} = ε_k. ∎

## 6. What this closes, what remains

Wave 46 §4 listed as open for the mod-16 witness argument:
DIV, PAR, ψ-analysis, B2 in general form. DIV and PAR were
proved in wave 46; B2 is unconditional by wave 46 §4 (pinning
from DIV + PAR); the slope lemma (δ_E odd) is wave 45 §1; and
ψ-analysis is proved here. All five inputs are now closed.
Remaining for Gap G: the ladder conjecture (wave 46 §4) at
j ≥ 12 — class-identity of step-2^s witness chains and the
s(j)-chain analysis beyond the j = 11 census. Sharp next test:
j = 12 prediction (one step-32 chain of 8, contribution ±16).

## Checks

wave47_GapG_psi_check.py (ALL CHECKS PASS): Part A — Pell
valuations/residues exact for r = 3..12 (e = 3, c = 9, f = 9
mod 16; note f ≡ 9 is also the consistency value implied by
DIV, §4). Part B — full census (128,128): 32768/32768 valid,
reps exactly 2; sampled (256,256), (512,512), (1024,1024),
off-diagonal (2048,1024), (2048,2048): DIVphi = DIVeps = 0,
ε-alternation, φ-affine, (ii), (iii), ψ-alternation, rep
count 2^{j−6} with spacing exactly 4, pinning algebra
(L_1 − L_0 ≡ 16 mod 32; ε_i = L_i/16 mod 2) — 0 violations
throughout. No Lean built, repository untouched.
