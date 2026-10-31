# REPORT N13b — mixed classes (iso mod d, unit mod h_p/d) at composite h_p without G*_gas: routes R1–R3
Labels: [P] · [P-sketch] · [CA] · [CA*] · [N] · [H]. Nothing pushed. Earlier lines untouched.
Asia/Yekaterinburg (UTC+5), 2026-11-01 00:36 → 01:17 (`date`). Every job ran at nice 19, sequentially.

## 0. Verdict
- **No route closes unconditionally.**
- **R2 is the most promising, and it is the one I committed to.**
  - Numerically the mixed classes are harmless with a wide margin: the weighted mixed sum is ≤ 3e-3 at p=11, 6e-4 at p=13 and 6e-6 at p=17. That is decaying like ~e^{−0.8p}, while |X| grows like (1+ReΛ)^p.
  - The proof reduces to one precise missing lemma, the **subgroup-C′ lemma** with an index exponent c < 0.387 (§2). The data give c ≈ 0.1–0.27 for the large iso parts.
  - The naive proof of that lemma gives only c = 0.694.
- **R1 does not close on its own** [N + structural]. The slow fixed point sits exactly at the pressure threshold μ\*³/λ = 1.2061, so long stays cannot be absorbed and the route falls back to a stay gas.
- **R3:**
  - (i) Prime h_p (NSW primes) gives a clean **conditional** refutation, since there are no mixed classes at all. Infinitely many NSW primes is an open conjecture.
  - (ii) Re-weighting the CS bound cannot kill mixed classes [P-sketch].
  - (iii) Switching to a prime level q | h_p fails: X_q ≈ 0 there [N].

## 1. R1 — restricted pressure (a_press.py: Line-F 8V operator, all periodic points of F^n, n ≤ 7, closed 1/8 box) [N]
R₃(L) = (Σ_{orbits, all box runs < L} |O|·ρ(P_{|O|})^{3n/|O|})^{1/n}/λ at n = 7, against the threshold μ\*³/λ = 1.2061:

| L | 1 | 2 | 3 | 4 | 5 | 6 | all |
|---|---|---|---|---|---|---|---|
| R₃(L) | 0.745 | 0.950 | 1.077 | 1.153 | **1.217** | 1.324 | 1.4055 |

(For reference, R₁ = 0.896 and R₂ = 1.0002 over all orbits.) The values are stable over n = 5–7 to about ±0.03.
- Below the threshold for L ≤ 4; above it from L = 5.
- **Structural obstruction.** A stay of length ℓ at the slow point contributes exactly (μ\*³/λ)^ℓ = 1.2061^ℓ, so the threshold is the fixed point itself.
  - Long stays therefore have to be separated as a gas again.
  - For mixed points the stays come from the iso component and can last up to ~p steps. They are capped only near the unit component's zeros, at ≤ 2log_λ q_u + O(1) per stay [P-sketch].
  - With q_u small, the stays are short, but the outside pressure at L = 4–5 (1.15–1.22) has no margin.
- **Not a standalone route.**

## 2. R2 — arithmetic/averaged route (chosen)
**Structure** [P, bookkeeping]:
- A mixed point has Nβ ≡ 0 mod d and Nβ a unit mod h/d. By CRT its twist is τ^{(d)} + τ^{(h/d)}.
- Count: |H_d| ≈ 2h²/d.
- Weight: |κ|/n ≤ 2^{ω(h/d)}·2d/h (exact max at p=11, d=353: 695/7371).
- Hence |Y_mixed,d| ≤ 2^{ω}(2d/h)·Σ_{H_d}|r| = 2^{ω}·4h·E_{H_d}|r|.

**What C′ gives** [P+CA mod C′'s e^{o(p)}, squarefree h_p]:
- Σ_{H_d}|r| ≤ Σ_G|r| ≤ e^{o(p)}h²(1.2744/μ\*)^{3p}, so |Y_mixed,d| ≤ e^{o(p)}·d·(ε·0.2945)^p = e^{o(p)}·d·0.711^p.
- This is fine **iff d ≤ 1.4065^p**.
- Every composite h_p has a mixed class with d ≥ √h_p ≈ 1.554^p > 1.4065^p. **So C′ alone controls mixed classes exactly when h_p is prime** [P].

**Missing lemma (subgroup C′)** [H; target]:
- Statement: E_{β∈H_d}|r(β)| ≤ e^{o(p)}·d^c·(1.2744/μ\*)^{3p} with **c < c\* = ln(1/0.2945)/ln ε − 1 = 0.387**.
- It would give |Y_mixed| ≤ e^{o(p)}(ε^{1+c}·0.2945)^p → 0, uniformly over all splittings, at squarefree h_p.
- The naive proof (H_d's sublattice is Bowen-separated only up to time p − log_λ d, with the remaining steps bounded by the sup) gives c = ln(sup g/avg g)/ln λ = 0.694 > c\* ✗.
  - So genuine equidistribution of the iso sublattice is required. This is exactly N3 §4 item 1 ("beyond-Ehrenfest").

**Numerics** (b_subgroup.py: unbiased samples of 1500 per set; means are heavy-tailed, dominated by single maxima, so c_est is noisy) [N]:

| p | h = d·(h/d) | E_G\|r\| | E_{H_d}\|r\| (c_est) | weighted bound 8h·E_H | \|X\| |
|---|---|---|---|---|---|
| 11 | 23·353 | 9.6e-9 | H₂₃ 1.5e-8 (0.14); H₃₅₃ 4.6e-8 (0.27; exact 1.8e-8 → 0.11) | 1.0e-3 / 3.0e-3 (exact signed: 4.1e-5) | 0.018 |
| 13 | 79·599 | 1.3e-9 | H₇₉ 1.6e-9 (0.06); H₅₉₉ 1.7e-10 (−0.31) | 6.1e-4 / 6.4e-5 | 0.022 |
| 17 | 103·15607 | 1.9e-14 | H₁₀₃ 4.8e-13 (0.70†); H₁₅₆₀₇ 1.4e-13 (0.21) | 6.2e-6 / 1.8e-6 | ~0.026 |

- † A single outlier dominates this mean. Since d = 103 ≤ 1.4065^17 = 330, the trivial index loss suffices there anyway.
- For every large d, c_est ≤ 0.27 < 0.387.
- E_G is far below the C′ rate: 6.6e-3, 1.0e-2 and 2.0e-5 times 0.2945^p.
- **Mixed growth exponent [N]:** the weighted mixed bound falls by ~e^{−0.6…−0.9} per unit p over p = 11→17, against +6.2e-4 per p for the main term. Mixed classes are no numerical threat.

## 3. R3 — reformulations
- **(i) Prime h_p** [P mod standing inputs].
  - With h_p prime there are no mixed classes. Unit points are covered by C′ (−0.341/p) and the iso tail by N11's theorem.
  - h_p is prime for p = 5, 7, 19, 29, 47, 59, 163, 257, … (NSW primes).
  - **The refutation along {p : h_p prime} is therefore conditional on infinitely many NSW primes** (open, Bateman–Horn-type heuristics predict it), plus the other standing gap-(a)/(b) inputs other than the mixed class.
  - Composite h_p with all prime factors > 1.716^p cannot exist (two such factors would exceed h_p), so there is no wider arithmetic subsequence via C′ alone.
- **(ii) Member re-weighting** [P-sketch].
  - Any weights w_t in Σ_t|Z_t|² ≥ |Σw_tZ_t|²/‖w‖² give mixed frequencies the relative weight κ_w(u)/κ_w(0).
  - A function on the units mod q_u whose Fourier transform vanishes at all nonzero frequencies would have to be constant including at 0, which is impossible.
  - So the 1/(q_u−1) suppression is intrinsic.
- **(iii) Prime-level switch** (c_levelq.py, exact, p=11, q=353, all 124,609 points) [N].
  - X_q = −4.4e-7 + 3.9e-7i and |1+X_q+Y_q| = 1.0000053, against |1+X_h| = 1.0165 at the full level.
  - The iso gas lives only at the full level h_p. **Dead.**
- **(iv) Averaging over p** [H]. Heuristically (Σ_{q≡±1 mod 2p} 1/q), a fraction ~log p/p of p have h_p with a factor below 1.716^p. But since composite already forces a factor ≤ √h_p, averaging gives nothing beyond (i).

## 4. Recommendation
Prove the subgroup-C′ lemma with c < 0.387. Natural attack: redo C′'s Bowen-ball step on the sublattice 𝔡/hO, using the O1 collision majorant restricted to differences in 𝔡; Prop E then becomes a carry automaton over a sublattice. That is a finite arb certificate, if the restriction can be encoded in the automaton. Until then, gap (b) mixed holds unconditionally only along prime h_p.

---
# REPORT_N12b_v2 (minor fixes from /workspace/audit/lineN13/REPORT.md)
- **θ-robustness.** The referee shows Γ_per(θ, L=3) ≥ 1.4296 for every θ ∈ [1/16, 1/4], and the union of the four boxes changes nothing. So D1 with L ≥ 3 is dead at every box size, not just at 1/8. REPORT_N12b §3 is to be read with this strengthening.
- **K at the most favourable Γ ≈ T′.** q = μ\*/(λT′) = 0.2302, giving z/K = 0.687 (L=1) and 0.227 (L=2).
  - Rank-p pieces then need **K < 2.9e-4 (L=1) and 8.8e-4 (L=2)**. The referee's 3.0e-4 / 9.2e-4 are the same to rounding of q.
- **Constant convention.** The per-stay constant is **K := C²·C_θ**, with C = C_out·K_box as in REPORT_N9b_v2 F2. N12b's "K = C·C_θ" is corrected to this.
- **"K ≳ 1" is [N/heuristic]**, based on N_H(1/8) = 2.84 and N12's K_stay ~ 10². It is not proved.
- **Witness orbits** (period 5 with run 2: 1.43362; period 4: 1.42956) are not arb-certified in this line; optional, left open.

## Files
- code: a_press.py, b_subgroup.py, c_levelq.py
- logs: a_press_a4.jsonl, a_press.out, b_subgroup_p{11,13,17}.{json,out}, c_levelq_p11_q353.json
- NOTES_N13b.md, REPORT_N13b.md, SHA256_N13b.txt (+ .sha256)
