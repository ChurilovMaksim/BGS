# REPORT_N17b v3: erratum to REPORT_N17b_v2 (N18b), referee lineN16 R1, L1-a, L1-b

*Line N19b, 2026-11-01 (Asia/Yekaterinburg, UTC+5).*
- N18b/REPORT_N17b_v2.md is unchanged. This file lists the replacements; everything not mentioned stands as in v2.
- Nothing pushed.

## R1: Robin term in the crossover script (required)
- **The bug.** N18b `a_crossover_v2.py` used `robin(L) = e^γ ln L + 0.6483/L − 1` with L = ln K_p. Robin (1984, Thm 2) has 0.6483/ln ln K_p = 0.6483/ln L.
- **Fix.** N19b `code/a_crossover_v3.py` uses `def robin(L): return math.exp(gam)*math.log(L)+0.6483/math.log(L)-1`.
- **Re-run** (logs/a_crossover_v3_d*.json) reproduces the lineN16 table:

| δ | first integer p (envelope) | first prime (exact K_p) | Robin bound at p = 1289 (G there) | G′(p*) | envelope slope bound 2e^γ/(2p*+1) |
|---|---|---|---|---|---|
| core 5.14476e-7 | **1386** | **1399** | **12.849** (10.992) | 0.02209 | 0.00128 |
| true, G ≤ 15 only, 2.470e-6 | **1390** | **1399** | 12.849 (10.914) | 0.02200 | 0.00128 |

- No violation at any prime 1399 ≤ p ≤ 5000 (exact K_p).
- **Replacements in REPORT_N17b_v2:**
  - §0 item 2: "12.77" → **12.85**. Delete "(v1 printed 12.85 from an approximate ln K_p.)". The value 12.85 was right, and **12.77 is withdrawn**: it came from the bug.
  - §2 crossover bullets:
    - r(L) = e^γ ln L + 0.6483/ln L − 1, increasing for L > e^{0.6033} ≈ 1.83 (not "L > 0.37");
    - core δ: first at p = **1386** (margin 0.0153);
    - true δ (G ≤ 15): first at p = **1390** (margin 0.0021);
    - **delete** "This agrees with the referee's 1386" (a coincidence of two ≈0.08–0.10 errors);
    - G′(p*) ≥ **0.0220**.
  - §2 monotonicity [P]: ρ′(L) = (e^γ − 0.6483/ln²L)/L ≤ e^γ/L, so g′(p) ≤ 2e^γ/(2p+1) still holds. Hence G(p) > I_p for all p ≥ 1386 (core) / 1390 (δ_true, G ≤ 15), so for every prime p ≥ 1399 under the stated idealization (Lean `env_slope_small`, lineN16).
  - **Caveat:** δ in B_p is the all-G true δ, whose G > 15 part is open (H4). So 1390 is a lower bound for the true p₁.
  - §2b Q2 and §9 B2: 1382/1386 → **1386/1390**.
- **Also (lineN16 §2a minor):**
  - §2 "Scale" 1.1329 → **1.13287** (μ²/ε^{4/3} = 1.1328794; TRACE-271).
  - T′ printed as 1.4279/1.428 → **1.42785** (T′ = 1.4278538; rounding a threshold up is non-conservative).

## Lemma 1 (REPORT_N17b_v2 §6): verdict [P] (lineN16 §2b)
- **L1-b.** Replace "admissibility: (γ) ⊂ 𝔡O^∨ ⇒ N𝔡·N(O^∨) divides N(γ)" with: **"(γ) = 𝔡·O^∨·𝔟 with 𝔟 integral, so |N(γ)| = N𝔡·N𝔟/8 ≥ d/8"**. Hence every nonzero z ∈ Λ_𝔡 has |z_u z_s| ≥ d/(8h²).
- **L1-a.** In "Use in Lemma 2", replace C = 16λδ²h²λ^{−p} with **C = 16λ²δ²h²λ^{−p}**. Since ⌈x⌉ < x + 1, λ^{n_*−n} < λ²·(16δ²h²/d)·λ^{−n} (Lean `lemma1_C`). C ≍ 1 still.
- **Status.** Lemma 1 (squarefree d, split prime factors) is **[P]** (refereed lineN16 §2b). Lemma 2 remains [P-sketch].
