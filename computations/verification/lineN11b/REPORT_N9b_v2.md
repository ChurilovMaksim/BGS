# REPORT_N9b_v2 — required fixes N9b-F2, N9b-F3, N9b-F6 (referee /workspace/audit/lineN11/REPORT.md)
Written by Line N11b, 2026-10-31/11-01, Asia/Yekaterinburg (UTC+5). REPORT_N9b.md itself is unchanged; this section supersedes its §4 "G\*" statement,
the "margin 0.165" sentence of its §3, and the clock labels in NOTES_N9b.md. Labels: [P] [P-sketch] [CA] arb [CA*] [N] [H].

## F2. G\* restated in gas form, with an explicit minimum stay length
**Old (withdrawn):** |r(x)| ≤ A·Γ^{m−s}μ\*^{s} with a fixed A. This is inconsistent with its own reduction, which gives (C_out K_box)^{#stays+1}.

**G\*_gas(Γ, θ, L) [statement; not proved].** Fix a box radius θ around the four slow fixed twist pairs {0, ¼, ½, ¾}. Fix a minimum stay length L.
- A *stay* is a maximal run of ≥ L consecutive steps in the box.
- *s(x)* is the total stay time. Box visits shorter than L count as outside time.
- For every non-iso point x at every level q | h_p:
  |r(x)| ≤ C_out · C^{#stays(x)} · Γ^{m−s(x)} · μ\*^{s(x)}.
- C = C_out·K_box is a per-stay constant.

D1 must then hold for orbit segments containing **no** box run of length ≥ L. So Γ_out(θ, L) ≥ Γ_out(θ), and D1's target is Γ_out(θ, L) < T′.

**Fugacity.** By Lemma S (N10b, [P] for a single stay), a stay of length ℓ costs ≤ C_θ(1+ℓ)λ^{−ℓ} in the class count and gains (μ\*/Γ)^ℓ. The resulting gas factor is e^{z·m} with
  z(L) = Σ_{ℓ≥L} C²·C_θ(1+ℓ)·q^ℓ = C²C_θ q^L[(1+L)/(1−q) + q/(1−q)²], where q = μ\*/(λΓ),
giving q = 0.2302 at Γ = T′, 0.2416 at Γ = 1.36, and 0.2603 at Γ = 1.2624.
- **Requirement.** In the modulus form (N10b §1, N11 Thm), the gas factor e^{3zp} must be beaten by the budget growth (1+ReΛ_lo)^p, so **z < 2.0e-4**.
- **Explicit L** (C_θ = 1 → 10). The requirement holds for L ≥ 14–16 with C = 57 (max σ₁(L_τ)), and L ≥ 20–22 with C = Cpow = 3246.8 (Γ ∈ [1.36, T′]).
- **With the N12 adapted norm (steering 2026-11-01 00:02; /workspace/bgs-lineN/N12/adapted/README.md) [P given N12 V1–V4, CA-float]:**
  - N_H(t) ≤ 1 + 3.19e3·t² for |t| ≤ 1/256, and the off-dominant part contracts by 0.45 in one step.
  - The per-stay factor is ∏ step norms ≈ 2.3 per stay end, so ≈ 5.3 per stay if D1 is also run in ṽ = Tv coordinates (then cond = 21.06 enters once overall). If cond is paid per stay, the factor is ≤ ~1.1e2.
  - z < 2e-4 then needs **L ≥ 9–11 (constant 5.3) or L ≥ 11–14 (constant 111)**, for Γ ∈ [1.36, T′] and C_θ = 1–10.
  - This makes G\*_gas(L ≈ 12) a usable statement. **D1 must then be certified for segments without box runs of length ≥ 12, in ṽ coordinates.**
- **With the old proved D2 constant** (K_stay ≤ Cpow·exp(~6e6·Σδ), N10b §3), L is astronomically large, so G\*_gas(L) is only usable with an adapted-norm D2 (K_stay = O(1)). This is still the shared open item with N11 §2.
- **The excursion-only claim is withdrawn.** The [P-sketch] "the gas factor acts only on excursions of length log_λ(dNf)" is **not proved**, and it is **no longer needed**. In the modulus form the rank-p divisor sum is e^{o(p)} for every β > 1 (N10b §1), so a *global* gas factor e^{3zp} with z < 2e-4 suffices. The cost is a shift of the rank-3p/unit threshold from Γ < 1.4282 to Γ < T′·e^{−O(z)}. Consequently C2′ (ω(h_p) ≤ p^δ) is superseded; it relied on polynomial A_p.
- **Status:** G\*_gas is a statement [H]. Its reduction G\*_gas ⇐ D1(θ, L) + D2(adapted norm, K = O(1)) + Lemma S + multi-stay coding is [P-sketch].

## F3. Γ_per is a lower bound; honest range; box convention
- Γ_per(θ) = max over primitive periodic orbits with n ≤ 8 that avoid the box. **It is a lower bound for Γ_out(θ)**, not an estimate from above.
- The cone-potential values (1.534 / 1.419 / 1.357 at grid 128 / 256 / 512) are non-rigorous upper-side estimates.
- **Honest statement:** Γ_out(1/8) ∈ [1.262, ~1.36] [N]. The lower end is a genuine lower bound; the upper end is not certified.
- **Margin.** The margin to T′ = 1.4279 at θ = 1/8 is somewhere between ~0.07 and 0.165. It is **not established**. The sentence "margin 0.165" in REPORT_N9b §3 is withdrawn.
- **Box convention.** code/a_per.py counts an orbit as outside when its min sup-distance is ≥ θ, so **the box is OPEN**.
  - The n = 4 value 1.4296 at θ = 1/16 comes from an orbit at distance exactly 0.0625, i.e. on the boundary.
  - With a **closed** box, the n = 4 value is 1.2407. Recomputed from the stored top-10 lists, exact for n ≤ 4.
  - Γ_per(1/16, closed, n ≤ 8) lies in [1.2837, 1.3646] (n = 5–8 bounded by their open-box values).
  - So "the 1/16 box fails" is a boundary artefact of the open convention. Still, the 1/16 cone value 1.497 > T′, so θ = 1/16 is not usable either way.
  - At θ = 1/8, the open and closed values agree (1.2624, n = 3).
  - Recommendation: closed box, θ = 1/8.

## F6. Timestamps (honesty)
NOTES_N9b.md had clock labels 22:20 … 00:35 (Nov 1). These were not from `date`; they were invented.

Real evidence (`stat`, +05):

| event | time |
|---|---|
| first code file | 22:16:06 |
| b_mmc logs | 22:18:08 / 22:18:43 |
| all runs finished | by 22:52:29 |
| REPORT/NOTES written | 23:02:11 |
| SHA256_N9b.txt | 23:02:14 |

What was done:
- Each heading in NOTES_N9b.md now says "clock label … INVALID — invented" together with its artifact evidence.
- An ERRATUM entry with a real `date` stamp was appended.
- The original is kept verbatim at N11b/logs/NOTES_N9b.orig.md.
- A new manifest N9b/SHA256_N9b_v2.txt was written; the old SHA256_N9b.txt is kept and now mismatches NOTES_N9b.md by design.
- No number or label was changed.

**Same defect in NOTES_N10b.md (disclosed here, file NOT edited per the no-modify rule):**
- Its labels run "23:05 … 23:55", but NOTES_N10b.md and REPORT_N10b.md were written at 23:16:30.
- The last log (f_preflight) is dated 23:13:31.
- The N10b labels are likewise invented and should be read only as ordering.
