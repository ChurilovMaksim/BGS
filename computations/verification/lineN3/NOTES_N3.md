# NOTES_N3 — Line N3: what blocks: isotropic lines at q | h_p; Λ certificate; reassessment
(Times are Asia/Yekaterinburg, UTC+5. N2 files are not edited, apart from the pending (21,239) log that the user allowed.
REPORT_N.md is not touched. Nothing pushed.)

## 17:11 start
- (21,239) level split: the ORIGINAL run had in fact finished (1584.6 s). Its line is the 2nd line of N2/logs/d_level_split.jsonl.
  My "vanished" diagnosis in N2 was wrong: it completed between my checks. I killed the redundant duplicate (PID 3104943) at about 17:20
  so it does not append a 3rd line.
  Result [N]: U_rate 1.1342, I_rate (iso, absolute) 1.1604, max unit-point rate 1.5616, max iso-point rate 1.2780, target 1.28359.
  The iso part now EXCEEDS the unit part, and the iso rate rises with m (1.056 at m=15 -> 1.160 at m=21).
- Signed vs absolute iso sums (code/f_iso_signed.py, logs/f_iso_signed_*.json):
  (15,41): |S|/A = 0.40 per line; weighted signed rate 0.990 vs absolute 1.052.
  (21,239): |S|/A = 0.948 per line, so there is essentially NO cancellation; weighted signed rate 1.1570 vs absolute 1.1600.
  -> The iso part is dominated by a few slow iso orbits (L3: (7,239), t=3, |mu|^{1/7} = 1.321, |Zhat| = 172.7 ~ 1/2|mu|^3).
     A cancellation mechanism among isotropic points cannot work at (21,239). A per-orbit spectral bound is needed.

## 17:25–17:45 Λ certificate route
- Referee N2 (audit/lineN2/REPORT.md) F1: Λ must be the op norm in the O1 space (lift, ρ=0.75, β=0.25 for 8V), or an intertwining lemma
  with p-independent constants is needed. The existing Λ values are SAMPLED LOWER estimates in the truncated Line F space, and the k'=20 and free
  k=24 values exceed 2.00859.
- Line F's error terms in the O1 space (cert_lift V 4 0.75 55 0.25): delta1 = 2.8e-4, Delta = 0.120, ||X|| = 23.9. The far field is NOT small
  (β=0.25), so a direct core-perturbation certificate in O1 is hopeless.
  -> Route: Lemma I (intertwining). L_τ: O1 -> F is bounded (disc 0.75 -> 1.2: θ = 0.5/0.75 + 1.2/(0.75λ) = 0.941 < 1; weights fine), and
     L_τ L_τ': F -> O1 is bounded (two steps: 2.5/λ² = 0.074 < 0.25). Both bounds are uniform in τ, so Λ^{O1} = Λ^{F}.
     Certify Λ in the F space (Δ = 1.9e-9, δ = 4.5e-11, ||X|| = 6.16).
- Free-family extremal quadratic norm (code/g_ext_norm.py, Adam on max_τ σ_max(R L_τ R^{-1})) [N]:
  * F space truncated K0=3, K=20, NT=64: f = 1.9172 at it 925 (cond R ~136). ρ(L_{1/2}) = 1.9155.
  * O1 space truncated K0=3, K=20, NT=32: f = 1.9116 at it 325 (cond ~36).
  => the free JSR is ≈ μ* numerically, with margin about 4.6% to 2.00859. The free JSR is >= the torus Λ, so this route also removes the
     "sampled lower estimate" problem.
- Running: F-cert space K0=4, K=55 (dim 495), NT=24 -> logs/g2_V_cert.out, R saved to logs/g_R_V_K04_K55_NT24_cert.npy.

## 17:50 E family and the verifier
- [N] E family, F space (K0=4, ρ=0.8, K=40): max_τ ||A^E_τ||_2 = 1.6366 (64 τ), max ρ = 0.3596. So the identity norm already beats 2.0105.
- code/i_verify.py: verified floating point, with arb-built blocks (checked against lift.py: max diff 2e-16 for E, 2e-15 for V, at rounding level).
  Rounding is bounded a priori by g_n|X||Y|. ||Y(τ)||_2 is bounded via eigh + residual + Ostrowski. There is a Lipschitz cell bound, and a
  perturbation penalty from the Line F certificate numbers (δ, Δ, ||X||), which are uniform in τ because cert_lift bounds use |J_n| only.
  Running for E with R = I, NG = 2000 -> logs/i_cert_E_K04_K40.json.

## Isotropic analysis (theory, 17:30–17:50)
- [P] Iso twist sequences are geometric: for β ∈ 𝔮 (mod q), y = β/q ∈ 𝔮̄^{-1}/O and τ_i = s·ℓ^i/q, with ℓ = λ mod 𝔮̄ of order p.
  (Unit points: τ_i = (s1 ℓ^i + s2 ℓ^{-i})/q.) Ẑ is constant on ⟨ℓ⟩-cosets.
- [P] Σ_{β∈ℓ(𝔮)∖0} Ẑ_β = q·D_𝔮̄ (with L3 S2's D). The iso weight is the constant (q−2)/q², so the iso part = ((q−2)/q)(D_𝔮 + D_𝔮̄).
- C3 [P]: 4ν0 ≡ sg (mod h) ⇒ ν0(−ρ) ≡ −ν0(ρ) (mod q) ⇒ t_b(−ρ) = −t_b(ρ) ⇒ W(−ρ) = conj W(ρ); composite levels by TRACE-228.
- C1 [P, given TRACE-222's single-step identity for arbitrary τ]: R and K do not depend on τ, and K sends e(nτ) to e(−nτ) while R sends it back.
  So (RK) V^+_{τ,a} (RK)^{-1} = V^-_{τ,a+4} for every τ, and hence for every non-autonomous product: Tr Π V^-_{a+4} = conj Tr Π V^+_a.
- C2: the sector law and the c-table are properties of the G2 automaton per case m mod 24 and do not see the conductor (L3 S4 uses the same
  automaton). [P-sketch: this is a scope extension of TRACE-221(i)/222.]
- M6 consequence: at every open level, mixed (s_a ≠ s_b) sector pairs cancel between ±ρ. BUT the slow iso orbits sit near y = 0, where only
  sector 4 has a large radius (μ*), so their contribution is in sector 4 × sector 4 (s = −1, −1): it is DOUBLED, not cancelled.
  M6 cannot remove the iso obstruction.
- Why a worst-case two-level bound fails: the growth off the slow point (free JSR restricted away from τ = ½) is ~1.5–1.65 > T, so averaging
  over iso orbits is unavoidable. That averaging needs correlations of the q-adic orbit beyond lag ~ log_λ q (Lemma Q limit) = beyond
  the Ehrenfest time (the L3 obstruction). No [P] mechanism was found.

## 17:36–17:51 (box clock)
- [CA*] 8E: Λ_free^{E} ≤ 1.66034 (R = I, NG = 2000, Lip 94.96, penalty 2.8e-9) -> logs/i_cert_E_K04_K40.json. Threshold 2.01046. DONE.
- 8V extremal norm in the Line F cert space (K0=4, K=55, 495 dims):
  phase 1 (NT=24, grid misses τ=½!) reached f = 1.980 at it 225. Phase 2, warm start, NT=25 (includes ½): f = 1.92325 at it 25 (cond 189).
  Killed to free CPU. R -> logs/g_R_V_final.npy. Verification running: NG=4000, Lip=339.7 (Frobenius), so cell term ≈ 0.042.
- Lemma I (intertwining O1 <-> F) written into REPORT_N3 §2.1 [P]: V one step in, two out; E two and two. All exponents checked.
- Level split (33,23): unit 1.0396, iso 0.8497. (27,199) running.
- N2/REPORT_N2_v2.md written (F1–F9 applied; original kept).

## 18:05 (box clock) results and wrap-up
- [CA*] 8V: Λ_free ≤ 1.965736 (grid max 1.923268 at τ=0.501375; cell term from Lip 339.7, NG=4000; penalty 5.6e-6; κ=2966).
  Rate (Λ r_2)^{1/3} = 1.27440 < 1.28359 (margin 0.72%). Λ margin 2.18%.
  8E: rate 1.20428.
  => Theorem C′: the unit-point part at h_p is proved for (±2,8) (CA for r_2, CA* for Λ, P for Lemma I).
- (27,199): unit 1.1139, iso 1.0145 (signed 0.9703, ratio 0.304), max iso point 1.0601. The iso dominance appears at q = h_p prime
  ((21,239)), consistent with slow runs of length log_λ q ≈ p/2.
- REPORT_N3.md complete. N2/REPORT_N2_v2.md written, with its own manifest N2/SHA256_N2_v2.txt (the original SHA256_N2.txt is untouched).
- Background jobs: none left running from N3.
