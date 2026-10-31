# REPORT N7 v2 — fixes required by the N7 referee (/workspace/audit/lineN7/REPORT.md) and the N8b erratum
This file supersedes the affected statements of N7/REPORT_N7.md. The N7 files themselves are unchanged.

## F1 — (±2,16) bound, two-term form [CA, inherited J3 rig_spec]
- The bound behind m1 = 51 and p16 = 339 is the two-term form B16(m) = Σ_i C_iR_i^m ≈ 706·1.63541^m + 2.27e5·0.95^m (`N7/logs/d_Z16.json`).
- The single-term majorant 2.273e5·1.6355^m is valid but cruder. With it the thresholds become m ≥ 83 and p ≥ 498 (referee `ref_robin16`). Both are < 1165, so Theorem R♯ is unaffected.
- **Monotonicity after the finite scans [P].** The scanned ratio has the form (C·1.6355^m + C′·0.95^m)²·σ(h_m)/h_m·h_p/(c·p·μ*^{2m}).
  - Robin's bound gives σ(h_m)/h_m ≤ e^γ lnln h_m + 0.6483/lnln h_m = O(ln m).
  - The squared bracket over μ*^{2m} decays geometrically with ratio ≤ (1.6355/1.9154712)² = 0.729 per m.
  - h_p/p ≤ ε^p/p grows by at most ε^{1/3} per unit of m, and 0.729·ε^{1/3} < 0.98.
  - So the ratio is eventually decreasing at geometric rate ≤ 0.98·(1+O(1/m ln m)) and stays below 1 after the first m at which it is < 1. The referee checked numerically that it decreases for 400 further p.
- **F2 (ledger):** the dom certificates inherit spectral containment from J3 rig_spec [CA], with float linear algebra and γ_n bounds.

## F3 — budget split (required) [P bookkeeping]
- Constants:
  - F_m ≥ 2.06e-3·p|Z₈|²/h_p (worst composite case);
  - L*_m := 4τ(h_m)h_p/(δ·2.06e-3·p) (replaces 2.3e-3);
  - Theorem 16 ((±2,16) all levels) uses 0.01·F_m; the trivial floor d > L* uses δ·F_m.
- **Ω♯_m:** Σ_ρΣ_{d ≤ L*}|Lin♯_d(ρ)| ≤ (1 − 2δ − 0.01)·F_m.
- **Split.** Take δ = 0.01 (so 1 − 2δ − 0.01 = 0.97):
  - (a) Lemma A∞ (one-sided, γ/γ̄ lines only): θ_a = 0.25;
  - (b) + (b′) + cross lines (F6): θ_b = 0.72.
- In absolute units, A∞ reads: Σ_{x ∈ (γ)∪(γ̄), x ∉ fam} max(0, −Re Ẑ_x/Z_ρ) ≤ θ_a·4p·(Re w*_lo − E(290)) = 0.25·4p·1.4584e-4.
- [N] numerics at p = 29 and 47 put the negative part at ≲ 2e-6 per 4p, about 5% of the θ_a budget. The certified head (N8/N9) is ≤ 1.27e-6, about 3.5%.
- **Caution (N9 §3):** the θ_a budget is likely exceeded for p ≳ 6·10³ because of multi-bump classes [H]. See REPORT_N9.

## F6 — cross lines (required)
- At composite h_p (ω ≥ 2) there are 2^ω − 2 further fully isotropic lines (𝔮₁𝔮̄₂, …). Identity (I) does not apply to them, and neither do prime-power analogues.
- **They are routed to (b′)** and counted in θ_b.
- **Lemma A∞ is restricted to the lines (γ) and (γ̄).**
- [N] sizes:
  - referee: 0.0014 / 0.0009 of the family term at p = 11;
  - N8b: rel_abs 2.7e-3 (p = 11), 7.9e-3 (13), 5.9e-5 (17), ≤ 4.6e-14 (37), ≤ 1.5e-14 (41).
- Proper-divisor consistent classes (N8b Lemma P′_c) are deep classes in the N7 sense (N(e) ≥ h_p/c ≥ 2p+1). They stay in (b) under the N8b bookkeeping. Any deep-class bound for (a) is stated in N9 so that it applies verbatim to them (REPORT_N9 §4).

## Erratum to Lemma P′(i) (N8b) [P]
- λ − 1 = 2ε, so the λ-fixed points of K/O^∨ are (λ−1)⁻¹O^∨/O^∨ = (√2/8)O/O^∨, i.e. **4 points**: z ∈ {0, ¼, √2/8, ¼ + √2/8}, with Tr z ∈ {0, ½, 0, ½}. N7 said 8 points.
- **Corrected (i).** For each of the 4 fixed points z, every point of the line (γ) is x = z + eγ/(8q), with e ∈ −8zγ̄ + 2√2O, uniquely mod 2√2γ̄O. Each z thus gives a complete parametrisation, and every x has 4 representations.
  - The windows of x lie near the z whose e has small norm.
  - (ii)–(iv) need Tr(λ^iz) ≡ Tr z, i.e. z fixed, which now holds.
- **The cosets are:**
  - z = ¼: e = 2α, α odd norm (N7's base ¼ — correct and complete);
  - z = 0: e = 2√2α′ with **any** α′ ∈ O. N7 used only odd α′, so it **missed** e = 4β;
  - z = √2/8 and ¼ + √2/8: e ∈ −√2γ̄ + 2√2O and e ∈ −(2+√2)γ̄ + 2√2O. These are p-dependent cosets, not enumerated by N7.
- **Re-check of e_isodepth.** N7's points x = ¼ + γα/(4q) are genuine (z = ¼ is fixed), and so are its base-0 points. The class list was incomplete, not wrong.
- **N9 numerics (`N9/code/a_bases.py`, exact twists, all 4 z, |N(e)| ≤ 40, p = 29 and 47):**
  - z = 0, e = 4 (N = 16): w = 1.041e-6 − 3.116e-6i (sg = +1). This is 0.83% of |w*|, a **missed** class.
    - [CA] (n9_cert): Re w ∈ [3.55e-9, 2.079e-6] > 0, so it is **positive and droppable**, and identical for both parities of k.
  - z = 0, e = 4√2: |w| ≤ 4.24e-8 [CA]; Re indeterminate.
  - z ∈ {√2/8, ¼+√2/8}: every class has |Ẑ/Z| ≤ 1e-24 (p = 29) and ≤ 7e-39 (p = 47). These decay exponentially in p, with no p-independent limit [N]. The mechanism (vanishing overlap of leading projectors between the two fixed-point sectors) is [H].
  - The family and near-0 values reproduce N7 exactly.

## F8 — labels
These items are [N] and carry no proof:
- the λ-orbit multiplicity 2p per line;
- the ε-symmetry α ~ εα ~ −α (N9 adds [CA] k-parity independence for 18 classes);
- the shell class counts for j > 14;
- "(a) holds with ~10× margin".

Shell sums are heavy-tailed (max/mean up to 37; outlier at j = 12), so the 9.5% total has no error bar.

## F9
N7 §4.4 should read: "the worst-case (joint-spectral-radius) majorant diverges [P]". Realised per-class values decay (~N^{−1.3} [N]); only that majorant is ruled out.

## F10
- The p = 11 class-A mixed figure is heavy-tailed: 0.149 ± 0.098 and 0.021 ± 0.005 for two seeds.
- The plausible range is 2–15% [N].
- It is not an estimate with an error bar.

## F11
The N5 referee's "≤ 4.4e-12" concerns only family × unit at e·h_p (h_p prime). Generic mixed classes are (b′).
