# REPORT_N5: Line N5 — the slow isotropic family at q = h_p is an exact aliased copy of the primary sum; the T-target fails there

Labels: **[P]** proved; **[P-sketch]** argument complete in outline, not every estimate written; **[CA]** ball arithmetic; **[N]** numerics; **[H]** heuristic.
Times are Asia/Yekaterinburg (UTC+5). N2–N4 files were only read. Nothing was pushed.

## 0. Summary

| item | result | label |
|---|---|---|
| Premise of the task | **Wrong in N4.** The 16D = 1 orbit is *not* "half slow, half fast". By a half-period identity every isotropic orbit at q ∣ h_p has **two** slow windows per period. For the 16D = 1 family they cover p − O(1) of the p steps; the "fast half" is two excursions of O(1) length. | [P] identity + [N] |
| Leading term | **Closed form:** Ẑ_β = (r_A r_B)³·Z_ρ·(1 + O(θ^p)) on the family, where r_A, r_B are two p-independent excursion factors (single gauge matrix elements). c* := \|r_A r_B\|³ = **3.954525469821·10⁻⁴** (10 digits stable from p = 29 to 257, both signs ±2, true TRACE-206 law). | [P-sketch] + [N] |
| Consequence | The family's isotropic rate tends to **μ*·λ^{−1/6} = 1.42775 > T = 1.28359**. True-law values: 1.3427 (p = 19), 1.3782 (29), 1.4018 (47), 1.4089 (59), 1.4239 (163), 1.4262 (257). The same constant c* and the same excess appear at the full level h_p for **composite squarefree** h_p (p = 11 … 43; > T from p = 11). **No bound G ≤ 1.547 can exist: the target T is unattainable at level h_p.** | [N] (exact-law numerics), asymptotics [P-sketch] |
| 7·h_p unit points | Theorem C′ extends to the mixed level 7·h_p with the same rate. | [P mod the standing inputs of Theorem C] |
| Reassessment | The per-level absolute strategy of N2–N4 (bound every open level's cross part by T^m) **cannot** refute R′ along m = 3p for any p ≥ 11 with h_p squarefree, because the cross part at level h_p alone is ≍ (μ*²λ^{−1/6})^m = **2.7348^m > ξ_lo^m = 2.4587^m**, coherently. A refutation along m = 3p would need this aliased term to be cancelled across levels or to be part of the main term; see §4. | assessment |

## 1. Half-period identity and the shape of the slow orbits

**Lemma H [P].** Let q ∣ h_p (p odd), ε = 1+√2, ε^p = h_p + y_p√2. For every δ with 4qδ ∈ O: ε^p δ ≡ ε^{−p} δ (mod O^∨).
*Proof.* ε^p + ε′^p = 2h_p and ε′^p = (−1/ε)^p = −ε^{−p}, so ε^p = 2h_p + ε^{−p}. 2h_pδ = (h_p/q)·(4qδ)/2 ∈ ½O ⊂ O^∨. ∎
- Hence λ^{(p+1)/2}δ = ε·ε^pδ ≡ λ^{−(p−1)/2}·εδ: the orbit returns near the fixed point z₄ = ¼ at time (p+1)/2 with deviation εδ, which has the same norm as δ.
- So each isotropic orbit of sector-4 depth D has **two** windows of length ≈ log_λ(16ε₀²q/D)·(1/2)·2 per period. At q = h_p ≈ λ^{p/2}/2 and 16D = 1 the two windows have total length p − O(1).
- [N] (`code/b_family.py`): steps within 0.05 of ½ per period: 14/19, 24/29, 42/47, 54/59 (always p − 5).
- **Correction to N4 §3.** N4 assumed one window of length ≈ p/2 and a fast half of length ≈ p/2. That was wrong. The N4 numbers that depend on it (the "G ≤ 1.548" requirement, the worst-case leading rate 1.4468 and the remainder rates 1.2426/1.0672/0.9165) are superseded by this report. The gauge lemma and the identification of the dominant family (16D = 1) in N4 stand.

## 2. The closed form for the dominant family

**Excursions [N, exact pattern].** Between the windows the twist deviation d_k = τ_k − ½ follows a fixed two-sided pattern (`logs/d_excursion_p59.json`):
- A: d_k = +a λ^{−k} (k ≥ 0), d_{−1−k} = −a λ^{−k}, with **a = (2−√2)/4 = 0.1464466**;
- B: d_k = −b λ^{−|k|}, with **b = √2/4 = 0.3535534**.
These are exactly Tr(λ^k·) of the two half-period images, reduced mod 1; they do not depend on p.

**Proposition X (closed form) [P-sketch].** On the 16D = 1 family at q ∣ h_p with 16D = 1 (in particular q = h_p):
  Ẑ_β = (r_A r_B)³·Ẑ(½,…,½)·(1 + O(θ^{p})),  Ẑ(½,…,½) = Z_ρ·(1 + O(θ^{p})),
with θ < 1 from the sector-4 spectral gap (complement radius ≤ 0.76905 vs μ* ≥ 1.91447, Line F [CA]) and
  r_A = ⟨ψ, G_{λa} T_{−a/κ} Φ⟩/⟨ψ, Φ⟩,  r_B = ⟨ψ, G_{−λb} T_{−b/(κλ)} Φ⟩/⟨ψ, Φ⟩,
where Φ, ψ are the right/left sector-4 Perron eigenvectors, κ = |C| = c₀ the multiplier coefficient, T_σ = translation and G_ν = modulation e(νs).
- *Derivation.* Each excursion is a contracting geometric run on one side and an expanding one on the other. By the gauge lemma (N4 §3.1) the contracting side is G-conjugate and the expanding side T-conjugate to powers of L_{½}. Inserting the rank-one decomposition of L_{½}^n on each long window leaves exactly one gauge matrix element per excursion. Three windings give the cube.
- What is not written: the uniform constants in the rank-one error on the twlaw (MC ⊗ automaton) realisation, and the analytic-continuation domain of Φ under T_{−a/κ} (|a/κ| = 0.83, which needs Φ on a disc of radius ρ + 0.83; the eigen-equation continues Φ there).
- [N] check (`code/d_excursion.py`, p = 59): the factorisation Ẑ_β = (r_A r_B)³·Ẑ(½…½) holds to **1e-14**; \|r_A\| = 0.2429773, \|r_B\| = 0.3020873, arg((r_A r_B)³) = π + 0.52 (so Re < 0); Ẑ(½…½)/Z_ρ = 1 − 1e-15.
- [N] (`code/c_true.py`, true TRACE-206 law, L = 8, K = 32): Ẑ_β/Z_ρ = 3.3502e-4 (p=5), 4.0797e-4 (7), 3.954524e-4 (19), **3.954525469821e-4** (29, 47, 59, 163, 257). Same for the (−2,8) sign. The model was validated against N2's arrays (2.872 at p = 5 and 172.740 at p = 7, exact).
- Not [CA]: certifying c* > 0 in arb is feasible (two matrix elements plus a gap bound) but was not done. It would make the *lower* bound on this family's term [P + CA].

**Rate [N + P-sketch].** Family weight: 2 lines × 2p points × (q−2)/q² (TRACE-229). So the iso part of the family is ≈ 4p·c*·|Z_ρ|/q, and with |Z_ρ|^{1/m} → μ* and q ≈ λ^{m/6}/2 its rate tends to **μ*·λ^{−1/6} = 1.42775**:

| p | q = h_p | rate (true law) | > T? |
|---|---|---|---|
| 5 | 41 | 1.0193 | no |
| 7 | 239 | 1.1535 | no |
| 19 | 9369319 | **1.3427** | yes |
| 29 | 6.3e10 | 1.3782 | yes |
| 47 | 4.9e17 | 1.4018 | yes |
| 59 | 1.9e22 | 1.4089 | yes |
| 163 | — | 1.4239 | yes |
| 257 | — | 1.4262 | yes |

**Composite squarefree h_p [N]** (`code/e_composite.py`): at the full level d = h_p, β = (d+γ)/4 with |N(γ)| = d is isotropic at every prime. For one of the 2^{ω−1} ideal classes (up to conjugation) of norm d the ratio is again c* (to 10 digits from p = 23). Rates (counting all 2^ω ideals, which only overcounts): 1.2859 (p=11, 23·353), 1.3147 (13), 1.3478 (17), 1.3738 (23), 1.3927 (31), 1.4092 (37, ω = 3), 1.4123 (41), 1.4135 (43). Weights are the CRT products of TRACE-229 prime-level weights (squarefree).

## 3. Theorem C′ at the mixed level 7·h_p (unit points) [P mod the standing inputs of Theorem C]
- Setting: p > 7 prime, h_p squarefree. Then 7 ∤ h_p (7 ∣ h_p ⇔ ord₇λ = 3 ∣ p), and 7 ∥ h_{3p} (λ³ ≢ 1 mod 49). 7 splits (3² ≡ 2 mod 7).
- A unit β at 7h_p is y = y₇ + y_p by CRT, with τ_i(y) = τ_i(y₇) + τ_i(y_p), and the unit weight factors: |W(y)| ≤ |W₇(y₇)|·|W_p(y_p)| (TRACE-229, squarefree). Σ over unit y₇ of |W₇| ≤ 36·2/49 < 2.
- Fix y₇. Let ν be the uniform measure on ∪_{j<3}(T^j y₇ + G_p). It is T-invariant, since T permutes the three cosets (period of y₇ is 3) and preserves G_p. Now rerun the proof of Theorem C (N2 §4) with ν in place of the uniform measure on G_p:
  - steps 1–2: Λ is a sup over **all** y ∈ T² of the cat-map products (the free-family certificate covers it a fortiori), so shifted points are included;
  - step 3 (Bowen-ball lemma) and step 4 (Hölder over residue classes) use only T-invariance of ν and the spacing of the support, which equals that of G_p;
  - step 5: ∫e(⟨α_v, y⟩)dν = e(⟨α_v, y₇⟩)·(average over the T-orbit)·1[α_v ≡ 0 mod h_p]. Its modulus is ≤ the G_p value, and the collision majorant has nonnegative coefficients, so the same bound R^Q holds;
  - step 6 (Prop E) is unchanged.
- Since Ẑ is constant on T-orbits, the ν-average over the three cosets equals the average for y₇. Hence E_{y_p∈G_p}|Ẑ(y₇ + y_p)| ≤ e^{o(p)}(Λ r₂)^p for every unit y₇, and the unit-point part at 7·h_p has the **same rates as Theorem C′**: 1.27438 (8V), 0.80266 (8E), 1.45789 (16V, vs 1.4742), 0.77812 (16E), with all Λ [CA] from N4.
- This upgrades N3-F9's [P-sketch] to [P mod the Theorem C inputs]. The isotropic part at 7·h_p is **not** covered, and §2 suggests it carries the same aliased term.

## 4. Reassessment: what remains for refuting R′ along m = 3p (h_p squarefree)
- **Proved or certified** (mod standing inputs):
  - unit points at h_p and at 7·h_p for all four families (Theorem C′ with N4's [CA] Λ);
  - levels > L_m (Prop K2);
  - the Weil range and small conductors (TRACE-245/246).
- **New negative finding [N, with P-sketch asymptotics].**
  - At level h_p the isotropic part contains the 16D = 1 family. Its term is an exact multiple c*·Z_ρ of the primary sum, which is an aliased copy of the sector-4 (¼-character) structure.
  - Its rate is μ*λ^{−1/6} = 1.42775 > T, so the cross part at this one level is ≈ 2·Re((r_Ar_B)³)·4p·|Z_ρ|²/h_p, of size **(μ*²λ^{−1/6})^m = 2.7348^m ≫ ξ_lo^m**. It has a definite sign (Re < 0), and within the level it is coherent (N3: signed/absolute 0.948 at (21,239)).
  - Therefore **no argument that bounds each open level's cross part in absolute value by T^m (N2–N4's route through H♮_mid) can work along m = 3p**, for any squarefree h_p with p ≥ 11. The obstacle is not a missing estimate: the term is genuinely large.
- **What a refutation along m = 3p would now need** [assessment]:
  1. **Accounting.** Decide whether the aliased family belongs to the main term. It is β/h_p = ¼ + γ/(4h_p): the level-4 character modulated by a small level-h_p twist, i.e. the Line L TRACE-218 aliasing. If the frozen R′ main term already contains the ¼-character (sector-4) contribution at its own level, this is a double count to be moved and subtracted exactly (Prop X gives the closed form). If not, it is a real secondary term of size 2.73^m.
  2. **Cancellation.** If it is not in the main term, R′'s fate along m = 3p depends on whether the same aliased term at the other levels containing h_p (7·h_p, and divisors via the depth-1 families at q ∣ h_p, whose windows are shorter) cancels it. Signs are explicit (Prop X), so this is a finite computation per level type, but it was not done.
  3. The previous open items remain: generic isotropic points (beyond-Ehrenfest averaging), index loss at proper divisors d ∣ h_p, K_p-levels, and the h_p-squarefree hypothesis.
- Net: R′ is **not** refuted along m = 3p. N5 shows that the route via per-level absolute bounds is closed there; the decisive question is now item 1 (main-term accounting of the aliased ¼-character family), which is a bookkeeping question about R′'s definition rather than an estimate.

## 5. Rigour ledger
- [P]: Lemma H (half-period identity); 16D = 1 ⇔ 4β − q generates the ideal (N4); Theorem C′ at 7·h_p mod Theorem C inputs (§3).
- [P-sketch]: Prop X (closed form via gauge lemma + rank-one windows); its asymptotic rate μ*λ^{−1/6}.
- [CA] (inherited): Line F sector-4 data; N4 Λ certificates; N2 Prop E.
- [N]: everything in the tables; c* to 10 digits; factorisation to 1e-14; composite levels.
- [H]: the aliasing interpretation in §4.1.

## 6. Files (`/workspace/bgs-lineN/N5`)
- code: `a_model.py`, `b_family.py`, `c_true.py`, `d_excursion.py`, `e_composite.py`.
- logs: `b_family.json`, `b_family.out`, `c_true_s1.json`, `c_true_s-1.json`, `c_true.out`, `d_excursion_p59.json`, `e_composite.json`.
- `NOTES_N5.md`, `SHA256_N5.txt` (+ `.sha256`).
