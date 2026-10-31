# REPORT_N5 v2: Line N5 with the referee fixes N5-F1 … N5-F10 applied

*v2, 2026-10-31, about 21:10 Asia/Yekaterinburg (UTC+5).*
- The referee report is `/workspace/audit/lineN5/REPORT.md` (verdict NOT READY). This v2 applies all ten fixes. The original REPORT_N5.md, its code and its logs are unchanged.
- The new computations are in Line N6 (`/workspace/bgs-lineN/N6`), which this report cites.

Labels:
- [P]: proved.
- [P-sketch]: argument complete in outline.
- [CA]: computer-assisted, rigorous.
- [N]: numerics without error control.
- [H]: heuristic.

## 0. Summary (corrected)
| item | result | label |
|---|---|---|
| Lemma H (half-period identity) | ε^pδ ≡ ε^{−p}δ (mod O^∨) for every δ with 4qδ ∈ O and q ∣ h_p. This holds for all such δ, isotropic or not, and at any level q ∣ h_m with p replaced by m. Consequences: two slow windows per period, and the "fast half" consists of two O(1) excursions. | [P] |
| **Sign (N5-F1)** | Ẑ(½,…,½) = **−Z_ρ**, because e(Σn_i/2) shifts ν₀ to ν₀ + h. Hence **Ẑ_fam/Z_ρ → −(r_A r_B)³ = c*·e^{±0.518i}**, with the sign + for ρ = (2,8) and − for (−2,8). **Re > 0.** The v1 statement "Re < 0, arg = π + 0.52" was wrong: v1 compared moduli only. | [N]; certified in N6 [CA] |
| c* | 3.954525e-4 (stable to 10 digits for p ≥ 29) [N]. [CA] enclosure from N6: c* ∈ [3.447e-4, 4.443e-4]; arg ∈ [0.337, 0.717] for (2,8), the conjugate for (−2,8); Re(−(r_A r_B)³) ∈ [2.89e-4, 3.98e-4]. | [N]; [CA] (N6 §2) |
| Prop X | Ẑ_β = −(r_A r_B)³·Z_ρ·(1+O(θ^p)) on the 16D = 1 family. Explicit constants are in N6 §3 (p ≥ 1165). | [P-sketch] here; N6 §3 for the explicit version |
| Family rate | μ*·λ^{−1/6} = **1.42785**. Cross rate μ*²·λ^{−1/6} = **2.7350** (N5-F8; v1 wrote 1.42775 and 2.7348). Constants use μ* = 1.9154712. | [P-sketch] + [N] |
| **Bookkeeping (N5-F2)** | The family belongs to the deviation Dev_{h_p} (TRACE-213), not to the frozen main term, which is exactly the β = 0 part (TRACE-212). Its cross part is **positive** and exponentially dominant. It is a **driver toward refuting R′**, not an obstruction. | [P] (bookkeeping) + [N] (size) |
| Size in W′/m units | Level h_p, both (±2,8): about +3 at m = 57, +125 at m = 87, +1.1e5 at m = 141 (referee). N6's lower-bound version (level h_p only, φ ≤ h) gives P_m/m = 2.4 (p = 19), 10.9 (p = 23), 103 (p = 29), 8.7e4 (p = 47). For comparison, D7 is about 1.0184^m/m ≤ 0.1 and the floor of W′_A is −4. | [N] |
| 7·h_p unit points | [P mod the Theorem C inputs], with the spacing constant made explicit (N5-F7): ν is supported on the 1/(7h_p) lattice, so the Bowen-ball spacing loses a p-independent factor of 7. Σ\|W₇\| ≤ 72/49 < 2, v₇(h_{3p}) = 1 for p ≠ 7, and 7 ∤ h_p for p > 3. | [P mod inputs] |

## 1. Corrections, fix by fix
- **N5-F1 (sign).**
  - Every "(r_A r_B)³ Z_ρ" in v1 becomes −(r_A r_B)³ Z_ρ.
  - "arg((r_A r_B)³) = π + 0.52, Re < 0" becomes: −(r_A r_B)³ has argument ±0.518 and Re > 0.
  - Checks:
    - N6 `g_sign.py`: Ẑ(½…½)/Ẑ(0) = −1 ± 1e-15 for p = 19, 29, 59 and both signs, complex values compared.
    - N6 `l_lineF_r.py` and `n_cert.py`: Line F representation, [CA].
  - The v1 scripts d_excursion.py and c_true.py compared moduli only. They are not changed (v1 is frozen); the phase checks live in N6.
- **N5-F2 (bookkeeping).**
  - Members at level d are Z_t = (G_d(t)/d²)Σ_β e(t̄Nβ/d)Ẑ(β) (TRACE-212/204). The frozen main term |Z_ρ|²/d² is the β = 0 part.
  - At a prime level, Z_t = ω_t Z_ρ(1+X)/q + (non-isotropic part), where X = Σ_{β iso ≠ 0} Ẑ_β/Z_ρ.
  - So Dev_{h_p} = (q−2)|Z_ρ|²q⁻²(2Re X + |X|²) + (square part ≥ 0) + (non-isotropic cross part).
  - Member sets are disjoint (TRACE-213). Levels are odd d ∣ h, so there is no "level 4".
  - Levels containing h_p inherit positive copies (TRACE-228). Mixed classes are numerically negligible (N6 §4; referee: \|Ẑ/Z₀\| ≤ 4e-12).
  - v1 §0 rows 3 and 5 and v1 §4 ("cannot be refuted by per-level bounds; needs cancellation") are **withdrawn**. The correct reading: the per-level target for all **other** pieces relaxes from T = 1.28359 to 1.42785 for (±2,8), and to about 1.64 for (±2,16).
- **N5-F3 (completeness of X).**
  - X = 4p·c*·e^{±0.518i}·(1 + O(1e-3)) [N]. Exact or screened totals: p = 11: 0.016493 + 0.008231i; p = 13: 0.019429 + 0.009762i; p = 19: 0.028554 + 0.014250i (N6 `f_iso.py`, `i_screen.py`).
  - A second, "near-0" family (4p points, ratio 2.987e-5 − 6.60e-6i) contributes about 8% of Re X. It is positive as well.
  - All other depth classes together are < 0.6% (N6), resp. < 0.1% (referee depth-class sum). Generic line points are ≤ 5e-12 each (referee Monte Carlo).
- **N5-F4.** H_mean (TRACE-256) is numerically false at q = h_p for h_p prime and p ≥ 19: the isotropic part has rate 1.4279 > T. TRACE-257 is vacuous there. TRACE-232 and TRACE-239 are one-sided lower bounds, and the new term is positive, so they are unaffected.
- **N5-F5.** N4 §3.3 is **withdrawn**: the remainder rates 1.2426/1.0672/0.9165, the leading-term figure 1.4468, and the target "G ≤ 1.547". It rested on a single window of length ≈ p/2. The N4 gauge lemma and the 16D = 1 identification stand.
- **N5-F6.** The estimates missing from the v1 Prop X were (i) uniform rank-one errors and (ii) the continuation radius ρ + 0.83 for T_{−a/κ}Φ. N6 §3 removes the need for (ii): it uses exact products of twisted operators over the excursion core, not the gauge form, and supplies (i) with explicit constants.
- **N5-F7.** 7·h_p: the spacing constant 7 is stated in §0.
- **N5-F8.** The constants are corrected: 1.42785 and 2.7350.
- **N5-F9.** twlaw truncation: (L, K) = (6,24), (8,32) and (10,40) agree to 1e-6 (referee). The law becomes unstable at L = 12 because ρ grows with L. All N5 and N6 numerics use L = 8.
- **N5-F10.** Levels containing h_p carry positive inherited copies and cannot cancel the family term. The v1 §4 item 2 ("cancellation across levels containing h_p") is withdrawn.

## 2. Rigour ledger (v2)
- **[P]:**
  - Lemma H.
  - The bookkeeping, and that the frozen main term is the β = 0 part.
  - 16D = 1 ⇔ 4β − q generates the ideal (N4).
  - Theorem C′ at 7·h_p mod the Theorem C inputs.
- **[CA]:** c* and the phase (N6 §2).
- **[P-sketch]:** Prop X in this report. The explicit version is in N6 §3.
- **[N]:** the tables, X(p), and the W′/m sizes.
- **Superseded:** v1 §0 rows 3 and 5, v1 §4, and N4 §3.3.
