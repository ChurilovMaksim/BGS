# research1105c — unifying N11 adapted-norm / non-resonant activity estimate

Grok Bot, 2026-11-05 (CET). Repo ChurilovMaksim/BGS, main @ 6f69baa1 (clone in `repo/`).
Prior finding: `/workspace/research1105b/REPORT.md`. Referee corrections: `/workspace/research1105b/REFEREE.md`.
`lineNgas/repo` was on `final-p17-nd` @ 8d6deba7 (not current); fresh clone used. **Nothing pushed.**

**Labels.** [P] proof. [P-sketch] outline with named gaps. [CA] interval/exact. [CA-fp] IEEE with a-priori model.
[N] floating-point numerics. [H] heuristic. [C] conjecture / open.

**Code / logs.** `code/r_attack_v2.py`, `code/r_attack_fast.py`, `code/r_attack.py` (superseded slow variants).
Checkpoints: `logs/ckpt/01_*.json` … `08_arb_thresholds.json`. Run log: `logs/r_attack_rest.out`.
Venv: `/workspace/lineNgas/venv` (python-flint 0.9.0). Transfer ops from N12 `a_ops` + adapted H-norm npz (read-only).

---

## 0. Headline

1. **Precise unifying estimate** (§1). One per-site activity bound for non-resonant sites in the N11 polymer expansion discharges (parts of) H1/(I)/(T) and H5(b), **with referee-corrected constants**. It does **not** by itself give a uniform e^{−cp} on all cross lines: the Lemma S axis sub-line and the 2p+1 family force the bridged/γ* route down to min(d₊,d₋) = 2p+1.
2. **Attacked seriously; no certified proof of the needed r.** [N] spectral radii, cutoff second moments, and empirical cross/Binet ratios. Full arb certification of a uniform r < 0.418 was **not** reached.
3. **Numbers.** Against the bridged threshold r_ε < ε^{−0.99} ≈ 0.4179 [CA]:
   - C′ candidate (1.2744/μ*)³ → r_ε ≈ 0.543 **fails** [N].
   - Non-resonant cutoff second-moment r_ε(θ=1/20) ≈ 0.472 **fails**; only for θ ≥ 1/8 does r_ε drop below 0.418 [N].
   - Fixed-twist spectral radius at |t|≥0.25: ρ ∈ [0.28,0.46], r_ε=√ρ ∈ [0.53,0.68] **fails** [N].
   - Empirical cross/Binet (seam = log_λ D): p=11 → r_ε≈0.325 (OK); p=13 → r_ε≈0.480 (**fails** 0.418; also fails absolute 0.463) [N]. Borderline, as research1105b said.
4. **Still missing.** Adapted-norm O(1) prefactor for bump/non-resonant blocks (N11 §2); H1-bad joint second-moment certificate (TRACE-336); counting on the cross circle; uniform control at min = 2p+1.

---

## 1. The precise unifying estimate

### 1.1 Formulation [C / open target]

**Estimate U (N11 non-resonant activity / adapted-norm input).**
There exist C₀ < ∞ and r < 1 such that every polymer γ in the N11 expansion
(exact identity [P mod Line F], `computations/verification/lineN11/REPORT_N11.md` §1)
whose support contains a non-resonant λ-site satisfies

```
|z_γ| ≤ C₀ · r^{n_nr(γ)},
```

where n_nr(γ) = # of non-resonant λ-sites in γ.
Equivalently, in the adapted H-norm of TRACE-311 (N12/N13): ‖B‖_H / μ* ≤ r on every
non-resonant block B, with C₀ absorbing the (now O(1)) gap-contraction prefactors.

- **What r is.** The per-site activity rate of polymers that cover λ-sites with twist outside the resonant boxes.
- **Which norm.** Adapted H-norm: cond_H ≤ 21.103, κ̃ = 0.45 on Q̃, N_H(t) ≤ 1+1e-12+4260 t² for |t|≤1/256 [CA]+[P] (TRACE-311). Plain spectral radius of A(τ)/μ* is only a Gelfand-rate proxy and does not control C₀.
- **Which sites.** λ-sites with |τ − b| ≥ η (η ~ 1/20) at backgrounds b ∈ {0, ½}. For H1-bad: ε-chain letters with zero-run < g₀ (polymer-restricted).

### 1.2 N11 polymer expansion (exact location)

From N11 §1 [P mod Line F]:
- Dominant sector: Tr ∏_i L_{τ_i}. Gap split G_j = μ^{g_j}(c_j Π + Ñ_j).
- Exact expansion of ∏(c_j Π + Ñ_j): coded rank-1 product + Ñ-linked polymer chains.
- Polymer activity bound: ∏ ‖B‖/μ^ℓ · ∏ R₂ κ^g, with inputs R₂, κ, N₁, ‖Π‖, Cpow [CA, Line F / n_cert].
- **Open (N11 §2):** proved rate κ = 0.41765, but prefactor G_b ~ 4e8 (from Cpow ≤ 3246.8). Needs adapted norm with C = O(1) so g₁ drops from ~64 to ~15.

H1 re-scoped (TRACE-336, THEOREM_DRAFT_v5): (H1-bad) polymer-restricted joint (A,B) second moment
Σ_{bad, shell j} |r_A r_B|² ≤ C · 2^{j(1−β(0.28))}, C ≤ 0.082 at J₀ = 12; + (H1-ali).
Prop. K: H1 ⇒ H3 (KP). Prop. F: unrestricted carry/torus bounds cannot give H1 [P].

### 1.3 Constants needed (referee-corrected)

| Target | Needed constant | Notes |
|---|---|---|
| **H1 / (I) / (T)** | r < 1 with **usable** C₀ so A_bad^KP + δ_true < Re Λ_lo′ ≈ 6.23e-4; or H1-bad with C ≤ 0.082 | TRACE-336; N11 §2/§5; N20 Prop. K. δ_true ≤ 5.0313e-6 [P]+[CA-fp] |
| **H5(b) vacuum (primitive)** | c = (ln(1/r_λ))/4 − ReΛ ≥ **0.058** (C ≤ 1) | **Referee:** old 0.048 wrong. Binding at p = 1409 (w_max = 112); at p = 3307 need only 0.0501. Lemma W caps ω. |
| **H5(b) bridged** | Polymer gap **K > log_ε min(d₊,d₋) − 2 log_ε A − 1.214** [P, referee]; γ = log(1/r_ε)/log ε > γ*_M ≈ 0.9909 ⇒ **r_ε < ε^{−0.99} ≈ 0.4179** | Absolute γ* = 0.8737 ⇒ r_ε < 0.463. Binding at p = 3307. |
| **H5(b) sub-line / 2p+1** | Same r must cover **min(d₊,d₋) down to 2p+1** | Lemma S on axis sub-line 0 ≠ c ∈ 𝔞̄_{−σ} only gives G ≥ √min [P, referee]. TRACE-350 family. Uniform e^{−cp} from max ≥ √h does **not** apply here. |

Thresholds [CA] (`logs/ckpt/08_arb_thresholds.json`):
ε = 1+√2, ε^{−0.99} ∈ [0.41788046713305305] (tight), gap const log_ε(ε²/2) = 1.21356… ≈ 1.214.

### 1.4 What Estimate U would and would not discharge

- **Would help:** N11 (I) interaction prefactor; (T) per-site A_bad form; H5(b) vacuum on primitive classes with max ≥ √h (c ≥ 0.058); H5(b) bridged power law if r_ε < 0.4179.
- **Would not alone discharge:** H5(b) uniformly on all cross lines (sub-line + 2p+1 need γ*); H5(a)/Y mixed; H1 in its stated joint-moment form (Prop. F); H7*, H6, H8.

---

## 2. Attack: methods tried

### 2.1 Transfer-operator / adapted-norm route [N]
Reuse N12/N13 H-norm (already [CA] for V1–V3, quadratic bound). Compute:
- spectral radius ρ(A(t)/μ*) and Gelfand rates for fixed twist t;
- i.i.d. second-moment ρ(𝒦) (N13 method);
- cutoff second-moment averaging over |t| outside resonant boxes.

Literature backdrop (not used as a black box): Gouëzel–Liverani anisotropic spaces, Baladi–Tsujii, Blank–Keller–Liverani give Lasota–Yorke / essential-radius bounds for Anosov maps; quantitative O(1) prefactors for this specific kick are not available off the shelf. The project's own adapted norm is the right object.

### 2.2 Cone / finite-matrix spectral radius [N, partial]
Fixed-twist A(t)/μ* is a 495×495 matrix; ρ is a genuine spectral radius. Full arb enclosure of ρ for many t was not completed (memory/time: Kronecker form of 𝒦 is 245025²). Float eigvals + Gelfand n=30 recorded.

### 2.3 Empirical cross-line rates [N]
From research1105b seam_profile max|u| on cross vs Binet lines, with seam length = log_λ D (matches their 0.33–0.48).

### 2.4 O1 restricted periodic census [N, reused]
`research1104/O1`: periodic ε-words; R = (g_A g_B)^{1/|w|}. H1-refutation threshold R > ε·0.28 ≈ 0.676.

---

## 3. Numerical results

### 3.1 Fixed-twist spectral radii [N] (`ckpt/01_power_rates.json`, `01b_power_rates_n30.json`)

| t | N_H(t) | ρ(A/μ*) | Gelfand₃₀ | r_ε := √ρ |
|---|---:|---:|---:|---:|
| 0 | 1.000 | 1.000 | 1.000 | 1.000 |
| 0.05 | 1.828 | 0.956 | 0.976 | 0.978 |
| 0.10 | 2.657 | 0.844 | 0.873 | 0.919 |
| 0.15 | 2.872 | 0.707 | 0.735 | 0.841 |
| 0.20 | 2.623 | 0.575 | 0.599 | 0.758 |
| 0.25 | 2.178 | 0.458 | 0.479 | 0.677 |
| 0.30 | 1.769 | 0.359 | 0.378 | 0.599 |
| 0.40 | 1.425 | 0.348 | 0.367 | 0.590 |
| 0.50 | 1.470 | 0.300 | 0.317 | 0.548 |

**Vs 0.418:** every fixed-twist r_ε above is **> 0.418**. The one-step adapted norm N_H(t) ≥ 1 always (prefactor problem of N11 §2). Asymptotic rate ρ < 1 for |t| ≳ 0.05, but not below the bridged threshold under √-conversion.

C′ candidate: (1.2744/1.91547)³ ≈ 0.2945 per λ-site → r_ε ≈ 0.543 > 0.4179 [N/CA*].
Crude vacuum for c ≥ 0.058: need only r_λ ≤ e^{−0.232} ≈ 0.793, which ρ meets for |t| ≳ 0.05 — but this is **irrelevant for sub-lines** (seam O(log p)).

### 3.2 Second-moment rates [N]

- **i.i.d. ρ(𝒦) = 0.27255** (N13 `g_K.json`, reused; √ρ ≈ 0.522). Below λ^{−1/2} = 0.414 as a λ-site second-moment rate, but √ρ as r_ε is still > 0.418.
- **Cutoff** (twists with dist to {0,½} ≥ θ; H-coords; Nq=48) [`ckpt/03_rhoK_cutoff.json`]:

| θ | ρ_cut | r_ε = √ρ | < 0.4179? |
|---|---:|---:|---|
| 1/20 | 0.2230 | **0.472** | no |
| 1/12 | 0.1976 | **0.445** | no |
| 1/8 | 0.1737 | **0.417** | yes (barely) |
| 1/6 | 0.1499 | **0.387** | yes |

So the natural coding threshold η = 1/20 does **not** give r_ε < 0.418 in this averaged model. Only a harsher non-resonant cut does. [N], quadrature coarse (Nq=48); not [CA].

### 3.3 Constant-twist scalar products [N] (`ckpt/04_seams.json`)

| t | n=10, r_sc | r_ε |
|---|---:|---:|
| 0.05 | 0.950 | 0.975 |
| 0.10 | 0.821 | 0.906 |
| 0.15 | 0.664 | 0.815 |
| 0.25 | 0.372 | 0.610 |
| 0.50 | 0.297 | 0.545 |

Consistent with §3.1: no margin under 0.418.

### 3.4 Empirical cross/Binet [N] (`ckpt/05b_empirical_corrected.json`)

Convention: r_λ = (max|u|_cross / max|u|_Binet)^{1/(log_λ D)}, r_ε = √r_λ.
(This matches research1105b's 0.33–0.48; the half-seam convention is optimistically small and was discarded.)

| p | D | ratio | r_λ | r_ε | γ | vs 0.418 | vs 0.463 |
|---|---:|---:|---:|---:|---:|---|---|
| 11 | 353 | 5.67e-4 | 0.106 | **0.325** | 1.27 | OK | OK |
| 13 | 599 | 4.87e-3 | 0.231 | **0.480** | 0.83 | **fail** | **fail** |

**Not uniform, not a proof.** Small-p, top-|u| only, seam-length convention sensitive. Agrees with research1105b: borderline / no claimed margin. [N]

### 3.5 O1 restricted rates [N] (`ckpt/06_O1_summary.json`)

| census | best R | best restr. R (mz<4) | vs H1-thr 0.676 |
|---|---:|---:|---|
| p≤8 periodic | 0.524 (mz=7) | 0.335 | no refute |
| p=10 | 0.302 | 0.302 | no |
| p=12 | 0.283–0.288 | same | no |

No periodic word in the census refutes H1 as stated. Does not prove H1. [N]

---

## 4. What was proved or certified here

| item | label | content |
|---|---|---|
| Estimate U statement + constant table | [C] formulation; inputs [P] from N11/TRACE | §1 |
| Referee c ≥ 0.058, gap 1.214, sub-line scope | adopted from REFEREE.md [P there] | §1.3 |
| ε^{−0.99}, gap const log_ε(ε²/2) | [CA] flint arb | `08_arb_thresholds.json` |
| Spectral radii / cutoff / empirical / O1 | [N] | §3 |
| Certified r < 0.418 uniformly | **not obtained** | — |
| Adapted-norm O(1) bump prefactor | **still open** (TRACE-311 gives the norm; N11 §2 prefactor open) | — |
| H1-bad joint moment | **still open** (TRACE-336) | — |

---

## 5. What is still missing

1. **Usable C₀ in Estimate U.** The H-norm exists [CA], but bump-block norms and the conversion from core to true window still leave large prefactors (N15 H-product vacuous; N21 closed δ_true by a different route). Estimate U needs C₀ = O(1) for non-resonant blocks.
2. **Uniform r_ε < 0.4179** (or a weaker γ* with the M-factor bookkeeping). Data do not support a clean margin; p=13 empirical and η=1/20 cutoff both sit at or above the line.
3. **Sub-line / 2p+1.** Even a good r only gives poly(p)·min^{−γ}. Must verify the γ*-sum closes at min = 2p+1 for the TRACE-350 family and axis classes — not done here beyond restating the referee's scope gap.
4. **H1-bad as stated.** A one-sided activity r is necessary but not the joint (A,B) second-moment certificate; Prop. F blocks unrestricted methods.
5. **Counting on the cross circle** (N11 coding lemma extends from Binet; research1105b §5 item 2, [C]).

---

## 6. Files

- `code/r_attack_v2.py` — main attack (eigvals / cutoff / seams / empirical / O1).
- `code/r_attack_fast.py`, `code/r_attack.py` — slower superseded variants.
- `notes/unifying_estimate.md` — short statement draft.
- `logs/ckpt/01_power_rates.json`, `01b_power_rates_n30.json`
- `logs/ckpt/02_rhoK.json` (N13 value)
- `logs/ckpt/03_rhoK_cutoff.json`
- `logs/ckpt/04_seams.json`
- `logs/ckpt/05_empirical_cross.json`, `05b_empirical_corrected.json`
- `logs/ckpt/06_O1_summary.json`
- `logs/ckpt/07_unifying_estimate.json`
- `logs/ckpt/08_arb_thresholds.json` [CA]
- `logs/r_attack_rest.out`
- `repo/` — BGS @ 6f69baa1 (read-only for this report)

**Reproduce.** `/workspace/lineNgas/venv/bin/python code/r_attack_v2.py` (expects N12 `a_ops` cache and adapted_norm npz; research1105b seam logs; research1104/O1 logs).

---

## 7. Bottom line (no exaggeration)

The single missing analytic input identified in research1105b is real and precisely the N11 adapted-norm / non-resonant activity bound (Estimate U). Referee corrections raise the H5(b) vacuum bar to c ≥ 0.058 and force the bridged route to cover min down to 2p+1 with gap constant 1.214.

**This pass did not prove Estimate U.** Numerics say r_ε < 0.418 is **not** plainly true for the natural η = 1/20 cut or for the C′ rate, and is **borderline** on small-p cross/Binet data (OK at p=11, fail at p=13). A certified interval proof was not reached. The estimate remains the right target; the constants are now the referee's; the proof is still open.

---

**Follow-up.** Bridged r_ε requirement re-derived in [`BRIDGED.md`](BRIDGED.md) (2026-11-05): 0.418 is greedy-M only; soft room r_ε < 0.48–0.60 at C₀=1 / ω≤20; cutoff 0.472 plausible but C₀ / entropy still block certification.

**C0 follow-up.** Adapted-norm bump prefactor analysed in [`C0.md`](C0.md): C0≤3 plausible for geometric N11 bumps [N]; ρ_cut r_ε≤0.47227 [CA-fp]; not certified.

**CERT follow-up.** [`CERT.md`](CERT.md): C0_activity≤0.30209 [CA] on singles; r_ε≤0.47227 [CA] discrete ρ_cut; H5(b)/H1 not discharged.
