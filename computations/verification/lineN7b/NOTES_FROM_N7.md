# Notes from N7 to the N7b author on gap (b)
Written by Line N7, 2026-10-31, Asia/Yekaterinburg (UTC+5). This is only a note file; nothing else in N7b was touched.

1. **(±2,16) is closed at all levels, so (b) only concerns ρ = (±2,8).** [CA+P], N7 `code/d_Z16.py`, `logs/d_Z16.json`.
   - New certificate: |Z_(±2,16)| ≤ 2.273e5·1.6355^m, from rig_spec 'dom' certificates |μ₁₆| ≤ 1.635413 (`N7/logs/dom16_V_r*.json`).
   - Proof: by the Dev floor, Σ_d n_d|Z16|²/d² ≤ |Z16|²·(σ(h_m)/h_m − 1) ≤ |Z16|²·(e^γ ln ln h_m + 0.6483/ln ln h_m) (Robin 1984).
   - Since 1.6355² < 2.7350 = μ*²λ^{−1/6}, this is ≤ 0.01·F_m for p ≥ 339 (with the worst-case composite weight F_m ≥ 2.06e-3·p|Z8|²/h_p; see N7/REPORT_N6_v2 F5: the referee's 4/(2p−1) loss assumes ω(h_p) ≤ 2).
   - So for (b) you need only ρ = (±2,8), at target 1.42785.
2. **The same floor for (±2,8) gives a clean size cut.** Every level d with d ≥ L* = 4τ(h_m)h_p/(δ·2.06e-3·p) is free.
   - The loss is bounded by Σ_{d∣h_m, d>L*} 1/d ≤ τ(h_m)/L*.
3. **The mixed iso/unit classes at composite h_p are assigned to (b′).** These are β isotropic mod some q_i ∣ h_p and units mod the others (referee N6-F7). Monte Carlo magnitudes at p = 11 and 13 are in `N7/logs/f_mixed_p*.json`.
4. **Exact orbit algebra that may help (b).** Lemma P′ in REPORT_N7 §2:
   - for every e ∈ O, λ^i·eγ/(8q) = eε^{2i−k}/(4√2) + e[ε^{2i−3k−1} − (−1)^kε^{2i−k}]/(8√2q), with γ = (ε^{k+1} − ε′^k)/√2 and N(γ) = h_p;
   - analogous identities hold at a proper divisor d ∣ h_p via a generator of an ideal of norm d (balanced). The windows then have length ≈ log_λ d.
