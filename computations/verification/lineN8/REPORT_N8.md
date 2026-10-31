# REPORT N8 — Lemma A∞ (gap (a)), Prop X′, Prop X constants
Labels: [P] proved, [P-sketch], [CA] computer-assisted (arb ball arithmetic), [N] numerical, [H] heuristic.
Code/logs in N8/code, N8/logs. Earlier lines unmodified.

## 0. Summary
| # | Item | Status |
|---|---|---|
| 1 | Generalised certificate `n8_cert.py` (any isotropic class (z,e), either k-parity, Lemma P′ seeds). Family rerun reproduces N6 (r_A, r_B to all digits). | [CA] |
| 2 | **Near-0 family is positive**: Re w₀ ∈ [2.3588e-5, 3.6143e-5]; with Prop X′ error ≤ 7.4e-10 for p ≥ 1289, Re(Ẑ/Z_ρ) ≥ 2.358e-5 > 0. **Dropped** (one-sidedness). | [CA] + [P mod §2] |
| 3 | 14 further small-depth classes (norms 7, 9, 17, 23, 25, 41; both bases) certified: 4 positive (dropped), 10 with absolute bounds, total Σ\|w\| ≤ 1.215e-6 = **0.42% of Re w*_lo**. | [CA] |
| 4 | k-parity independence: all 16 classes give identical endpoints for k even/odd (diff ≤ 2e-16). | [CA]; mechanism [P-sketch] |
| 5 | **sup_n‖L₄ⁿ(I−Π)‖ ≤ R₂′ = 3224.84** via Riesz–Dunford on \|z\| = 1 (Line F r₂ = 1). This closes the "coll" η-term gap. | [P mod Line F cert] |
| 6 | **Other-sector absorption explicit**: sectors 0, 2, 6 have sup_n‖L_aⁿ‖ ≤ 369.4, 739.9, 739.9 and twist-independent ‖L_{a,τ}‖ ≤ 40.85. Their contribution is ≤ 1e-6·Re w*_lo for p ≥ 485 (family windows). | [P + CA] |
| 7 | **Prop X′ explicit** (`q_propx2.py`): for a class (z,e) with certificate, \|Ẑ_x/Z_ρ − w(z,e)\| ≤ E_e(w), with p₀(e, τ) tabulated. | [P mod Prop X architecture, now written §2] |
| 8 | **Lemma A∞**: NOT proved. Reduced to the uncertified-class tail (A∞-tail). The restricted Theorem C route is analysed in §4: the r₂ input is fine (≤ 1.0874 at k = 200, ≤ 1.0529 at k = 4000 [CA, N2]); the missing piece is a box-restricted shell estimate. | open |
| 9 | N7 referee report: not yet landed (only interim scripts in /workspace/audit/lineN7). See §5. | pending |

## 1. Certificates of classes (A1′) [CA]
`n8_cert.py tag t0 e_a e_b` with env KPAR∈{0,1}.
- Seeds (Lemma P′):
  - k even: ζ_A = e/(4√2), ζ_B = −eε⁻¹/(4√2);
  - k odd: ζ_A = eε⁻¹/(4√2), ζ_B = +e/(4√2).
- Core d_j = emb₁(λʲζ) for j ≤ 0 and −emb₂(λ⁻ʲζ) for j ≥ 1, reduced mod 1 in arb.
  - A ball straddling a half-integer would only widen the enclosure, so this step is rigorous as written.
- Windows: KK = 18 plus the shift L = ⌈log_λ(\|e_i\|+1)⌉. The tail is |e_i|λ^{−(KK+L+1)}/(1−1/λ).
- All other machinery is N6 n_cert verbatim (resolvent on \|z−s\| = 0.6, C_pow = 3246.8, etc.).
- Base ¼: t0 = ½, e = 2α, sign −1. Base 0: t0 = 0, e = 2√2α, sign +1.
- Convention: the certificate's ρ corresponds to e_isodepth sg = −1, i.e. the conjugate. Re is the same for both ρ.

| class (α, base) | N(α) | Re w enclosure | \|w\| ≤ | use |
|---|---|---|---|---|
| family (1, ¼) | 1 | [2.884e-4, 3.988e-4] | 4.72e-4 | main term (N6 box [2.8896e-4, 3.9820e-4] kept) |
| near-0 (1, 0) | 1 | [2.3588e-5, 3.6143e-5] | 3.84e-5 | **positive → drop** |
| (1±2√2, ¼) | −7 | [2.2e-9, 3.31e-8] | 4.23e-8 | positive → drop |
| (1±2√2, 0) | −7 | [5.52e-8, 1.77e-7] | 1.98e-7 | positive → drop |
| (3, ¼) | 9 | [−6.16e-8, 2.42e-7] | 4.467e-7 | absolute |
| (5±√2, ¼) | 23 | [−4.91e-8, 7.2e-9] | 6.16e-8 (each) | absolute |
| (1±3√2, ¼) | −17 | [−4.36e-8, 6.4e-9] | 5.12e-8 (each) | absolute |
| (7±2√2, 0) | 41 | [−2.55e-8, 1.39e-7] | 2.636e-7 (each) | absolute |
| (3, 0) | 9 | [−5.8e-9, 5.0e-9] | 1.14e-8 | absolute |
| (5, 0) | 25 | [−1.8e-9, 2.0e-9] | 3.2e-9 | absolute |
| (1+3√2, 0) | −17 | [−1.2e-9, 9.5e-10] | 1.9e-9 | absolute |

- Absolute-class total ≤ 1.215e-6, plus Prop X′ errors 10 × 1e-9. That is ≤ 0.43% of Re w*_lo = 2.8895e-4.
- Each class contributes its 4p orbit points per ρ, exactly like the family, so the comparison with the 4p·Re w* budget is per class.
- These match the p = 47 numerics (`N7/logs/e_isodepth_p47_K60_*`) within the enclosure widths.
- k-parity: all k1 runs equal the k0 runs (`logs/n8_cert_*_k1.json`).
  - Mechanism [P-sketch]: the odd-k seeds are the even-k seeds with A↔B swapped and one core negated. w = (r_A r_B)³ is swap-symmetric, and r(−ζ) = r(ζ) follows from the per-step parity symmetry behind Ẑ(−β) = Ẑ(β) (N6 t_sym).

## 2. Prop X / X′ constants
**(i) Riesz bound [P mod Line F cert].**
- Line F certifies, for sector 4: a resolvent bound R₂′ = R₂/(1−F·R₂) ≤ 3224.84 on \|z\| = 1, and exactly one spectral point μ outside it.
- Then Lⁿ(I−Π) = (2πi)⁻¹∮_{\|z\|=1} zⁿ(z−L)⁻¹dz, so ‖Lⁿ(I−Π)‖ ≤ R₂′ for all n ≥ 0.
- Hence ‖Lⁿ‖/\|μ\|ⁿ ≤ ‖Π‖ + R₂′ = C_pow.
- This is exactly what the q_propx terms use:
  - coll = 2G_b²R₂′μ^{−⌊w/2⌋} (rank-one collapse);
  - the Gronwall constant C_pow in cont/outer/rtail, through the expansion ‖∏(L+E_j) − Lⁿ‖ ≤ \|μ\|ⁿ C(exp(CΣ‖E_j‖/\|μ\|) − 1);
  - ‖E_j‖ ≤ 2πN₁\|d_j\| (N₁ includes all rows and the far tail, N6 n_cert).
- The final telescoping ‖∏(A_k+B_k) − ∏A_k‖ ≤ 6η(x+η)⁵ over the 6 blocks, with \|Tr\| ≤ (T₁G_b+1)·‖·‖, gives E(w). The architecture is therefore [P], given the Line F certificate and the [CA] core constants.

**(ii) Other sectors [P+CA]** (`r_other.py`, `logs/r_other.json`).
- Sectors a = 0, 2, 6 have no outer spectrum (Ap_root < 1). Riesz then gives sup_n‖L_aⁿ‖ ≤ R₂′(a) = 369.4 / 739.9 / 739.9.
- Twist-independent bound: ‖L_{a,τ}‖ ≤ ‖A‖ + ‖X‖ + ‖Δ‖ ≤ 40.85, with ‖A‖ from the block-Frobenius bound with \|w(n)\|.
- Resulting bound: \|Ẑ_a\| ≤ TN·40.85^{6·39}·(C_a e^{C_a·2πN₁S})⁷.
- Against \|Z₈\| ≥ ½(1−λ^{−m})(μ^m − 3012.3) (TRACE-199), the ratio for 3 sectors is ≤ 1e-6·Re w*_lo for p ≥ 485.
- For a class with core length n_e the exponent becomes 6n_e. It stays absorbed while 6n_e·ln 40.85 ≪ 3p·ln μ, i.e. for any fixed finite class list. **It does not give a bound uniform over all deep points** (needed in A∞; see §4).
- certE_eta2 (the E-family) has smaller constants (R ≤ 4.67·(1+‖X‖)…). The same argument applies [P-sketch: not run separately].

**(iii) Prop X′ [P mod (i), Lemma P′ [P], class certificate [CA]].** For the class (z,e) with certificate:
- \|Ẑ_x/Z_ρ − w(z,e)\| ≤ E_e(w) for all 4p orbit points. Here w ≥ ⌊((p−1)/2−1)/2⌋ − L_e.
- E_e is q_propx's E with:
  - b → b_e = \|e\|_∞ε/(4√2), a conservative bound on \|ζ\| (Lemma P′ tails are ±ζλ^{−\|j\|} with O(\|e\|λ^{−k}) error);
  - G_c, r_max taken from the class certificate.
- Table (`logs/q_propx2_all.out`, τ = 1e-9): p₀ ranges over 1197–1289, the near-0 class gives 1289, and w(z,e) is uniform in p.
- **This upgrades Prop X′ from [P-sketch] to [P mod the Line F certificate and the [CA] class certificates] for every certified class.**
- The conservative b_e makes p₀(fam) = 1169 instead of 1165. Keep N6's exact-b value 1165 for the family.
- **Consequence for Theorem R♯:** with the near-0 class dropped and the 10 absolute classes charged, the threshold becomes p ≥ 1289.

## 3. What A∞ now requires
- Positive classes are dropped and the certified negative or indeterminate classes are charged 1.23e-6. A∞ (θ < 0.9) then follows from:
- **(A∞-tail)** For p ≥ p₂: Σ over all *uncertified* non-family isotropic points x at level h_p of max(0, −Re Ẑ_x/Z_ρ) ≤ 0.895·4p·Re w*_lo·(1 − o(1)).
  - "Uncertified" means: all classes except the 16 in §1, and all deep points.
- [N] evidence (p = 47, N7 i_shells): total non-family excluding near-0 ≈ 0.6% of Re w_fam, so the slack is about 150×. This is not a proof.

## 4. Restricted Theorem C route — status
- **r₂ input [CA, cited].** N2 Prop E gives r₂(200) ≤ 1.0874041 and r₂(4000) ≤ 1.0529012 (8V; `N2/logs/e_r2_cert.jsonl`, sha256 26d54504…3f83).
  - r₂(k) = R^{1/k} with R a Collatz–Wielandt bound, so it is a certified per-step HS² rate on blocks of length k.
  - Both values are far below the needed 1.481 (slack ≥ 1.36 per step). **No new r₂ certificate is needed.** Its uniformity at shorter block lengths (core lengths 2D) is covered by the k = 200 value once 2D ≥ 200; shorter cores are finitely many classes (§1-type certificates).
- **What is missing (precise):**
  - (R1) A box-restricted Bowen-ball lemma. The core twist vectors (d_j)_{\|j\|≤D} of classes in shell \|N(e)\| ∈ [2^j, 2^{j+1}) must be ε-dense with bounded multiplicity in the Bowen D-balls of the toral map. That would turn Σ_{shell}\|r_A\|² into the k-block HS² sum with r₂ rate.
  - (R2) The op-norm factor: \|r_A r_B\|³ ≤ \|r_A\|²·sup\|r_A\|·\|r_B\|³ needs sup‖core‖ growth. The sup barrier N^{1.088} [P, N7] gives op rate λ^{0.088D}·…. Combined with (R1), the shell sum is ~2^{j(1.088 − 2δ₂)} with δ₂ = 1 − log r₂/log λ^{…}. [H] It decays iff r₂-rate·op-rate < 1.481, as computed in N7.
  - (R3) The family aliasing obstruction [P, N8 analysis]: the full line-Parseval identity contains the family's aliased HS² mass ~1.52^p > 1.481^p. So (R1) must be applied *shell by shell* (cores of length ~2D, family = shell 0 excluded), never to the whole line.
  - (R4) Deep points (D ≳ k/2, no clean windows): the other-sector and Prop X′ constants are not uniform there. They need either the full-torus Theorem C bound at level h_p (index-loss barrier, N2) or a separate argument.
- Conclusion: **Lemma A∞ remains open.** It is reduced to (R1)+(R4). The finite part (A1′ for 16 classes, near-0 positivity) is done.

## 5. N7 referee
- /workspace/audit/lineN7/REPORT.md had not appeared when this report was written. Only interim scripts and logs exist.
- One interim log, `logs/ref_robin16.json`, reads first_p_ratio_le_1 = 498 (m1 = 83) for a Robin-bound check. That may conflict with N7's p16 = 339 for the (±2,16) all-levels statement.
  - This is irrelevant for Theorem R♯ (p ≥ 1165).
  - If confirmed, replace 339 by 498 in N7 row "(±2,16) closed for p ≥ 339".
- Not otherwise incorporated.

## 6. Files
- code: n8_cert.py, run_batch.sh, batch1.txt, r_other.py, q_propx2.py
- logs: n8_cert_*.{out,json} (32 runs), class_table.out, r_other.json, q_propx2_*.json, q_propx2_all.out, batch1.log
- Hashes: SHA256_N8.txt (+ SHA256_N8.txt.sha256)
