# CERT — final summary (referee-revised)

Grok Bot, 2026-11-05 (Europe/Berlin).  
Repo BGS @ 6f69baa1. **Nothing pushed.**  
Follow-ups: `REPORT.md`, `BRIDGED.md`, `C0.md`, `REFEREE_CERT.md`.

**Label policy (post-referee).** A statement is **[CA]** only if the quantity Estimate U needs is interval-closed with no silent float-as-exact eigenpair, and spectral radii use a theorem (norm / Rump / Kato–Temple with certified gap)—not residual+Pert_H. Everything else is research notes: [CA-fp], [N], [P], [H].

---

## Registerable claims vs research notes

### A. Claims that may be registered (narrow)

| # | Claim | Tag | Evidence |
|---|---|---|---|
| A1 | On the 10 single types 𝒯∪𝒯ε, with Φ,ψ,s taken as stored binary64 eigen data (N13 convention) and B built from cert_core arb blocks, the **core activity** \|ψ̃BΦ/(ψ̃Φ)\| ≤ **0.30209** | **[CA-fp] / [N13-conv]** | `logs/cert/c0_types/arb_singles.json`; indep referee match. **Not** full [CA]: eigenpair not enclosed. **Not** ‖B‖_H. |
| A2 | On **all 1350** coded pairs (prec ≥ 96), core \|r̃\| ≤ **0.09375** under the same convention | **[CA-fp]** | creplay 587 + `logs/cert/c0_pairs/` 763. Referee confirmed method on partial; completed this run. |
| A3 | C_gap = 1 for the adapted-norm one-step gap (TRACE-311 / N13 V3b) | **project [CA]** | Inherited; not re-audited this run. |
| A4 | Shorts enumeration: the N13 list of **200** short windows is exactly \|𝒯\|²·2·2·2 for T×T with n=2G+h∈{1,2,3,4} | **[P]** | `logs/cert/shorts/01_enumeration.json` |

No stronger continuum / discrete r_ε ≤ 0.5 **[CA]** is registered. No Estimate U / H5(b) theorem is registered.

### B. Research notes (not claims)

| Note | Result | Tag |
|---|---|---|
| Forward scan pair max 0.1576 | **WRONG** — prec-64 twist bug for large \|e\|; discard | [C] / withdrawn |
| All 1350 pairs @ prec ≥ 96 | max ≤ 0.09375 (new ≤ 0.0375) | [CA-fp] complete |
| Shorts max\|z\|≤0.6 for all 200 | **fails** — 31 ε-relabel OK; 157/160 nonrel ≤0.119; **3 arb radius blows** | [N]+[CA-attempt] partial |
| Discrete ρ_mid ≈ 0.223037, √ρ ≈ 0.47227 | reproduced mid; residual+Pert_H **demoted** | [N] |
| Discrete HS majorant ρ ≤ ∑w‖M‖₂² ≈ 0.327 ⇒ r_ε ≤ **0.572** | theorem-shaped, float MH | [N] |
| Continuum Fourier Galerkin K on S | ρ ≈ 0.22509, r_ε ≈ **0.4744** | [N] |
| Continuum r_ε ≤ 0.5 [CA] | **not achieved** (timebox + float Mh/T) | honest failure |
| Eigenpair Rump / Bauer-Fike | residual arb ~1e-15; full BF fails (cond V~1e13); 2×2 Rump OK on projection | [CA-attempt] / not [CA] |
| U_cross transfer (C0,r) | p=11 OK, p=13 marginal, p=17 lemmaS-only, p=37 missing | [N]+[H] |
| Soft room (semiprime C0=1) | p=1409 needs r_ε < **0.600**; p=3307 needs r_ε < **0.527** | [P-arith] |

---

## 1. Estimate U quantity

Estimate U asks \|z_γ\| ≤ C0 · r^{n_nr(γ)} (equivalently a block-norm form with C_gap=1).

For a **fixed geometric seed**, z = (ψ̃ B Φ)/(ψ̃ Φ) **is** the polymer weight. Bounding max\|z\| on a finite typed list gives the **C0 piece for that class only**. It does **not** give ‖B‖_H for arbitrary non-resonant words, and does **not** discharge Estimate U on cross/sub-line polymers.

---

## 2. C0 activity

### 2.1 Singles — [CA-fp]

max \|z\| ≤ 0.3020893 with float-exact Φ,ψ,s. Referee: number OK as activity; GAP on eigenpair enclosure and on ‖B‖_H.

**Verifyeig attempt.** cert_core residual ‖A0Φ−sΦ‖₂ ≤ 9×10⁻¹⁶ [CA as a residual]. Gap-ball R_s ~ 10⁻¹⁵ [P]. Full Bauer-Fike on float-dense A0 fails (cond(V)~10¹³). 2×2 Rump on span{Φ, resid} isolates |s|≈1.915 with rad~10⁻¹⁵ [CA-fp on projection only]. **No full eigenpair [CA].**

### 2.2 Coded pairs — [CA-fp] **complete** (all 1350)

- N13 creplay 587 + rerun 763 @ prec ≥ 96 = **1350/1350**.
- Global max core \|r̃\| ≤ **0.09375** (worst remains creplay `odd+odd` G=4); new jobs max ≤ 0.0375.
- Forward 0.1576: **discard** (prec-64 bug).
- 91/763 new have rad ≥ 10⁻³ (still abs_up ≪ 0.094).
- Quantity: **core** \|r̃\| under N13 float-eigenpair convention; core→true open. **Not** full [CA] (referee GAP a).
- Evidence: `logs/cert/c0_pairs/00_summary.json`.

### 2.3 Shorts — not [CA] for all 200

- 200 = exhaustive T×T n<5 list [P].
- 31 ε-relabel inherit ≤ 0.30209 under N13-conv.
- 157/160 unique non-relabel tight, max ≤ 0.1188; **3 blow** (rad~10⁹).
- **max\|z\|≤0.6 [CA] for all 200: no.**

---

## 3. Continuum / discrete ρ_cut — honest failure for [CA]

### 3.1 Soft room requirement [P-arith]

From `BRIDGED.md` / recomputed (`logs/cert/continuum_ca/00_soft_room.json`), **semiprime TRACE-350, C0=1**:

| p | slack | γ_req | **r_ε_req** |
|---|---:|---:|---:|
| **1409** | 0.02011 | 0.579 | **0.600** |
| **3307** | 0.003347 | 0.727 | **0.527** |

Truncated ω≤20 at C0=1 still allows r_ε up to ~0.48–0.56. Greedy M at p=3307 needs ~0.418 (not soft).

### 3.2 What was tried

1. Lip·Nsum mesh — err ~32 at Nq=48; needs ~10⁵ cells — abandoned.  
2. Discrete residual+Pert_H — **demoted by referee**.  
3. Discrete HS majorant ∑w‖M‖₂² — r_ε ≤ 0.572 [N].  
4. Continuum Fourier-exact Galerkin ∫_S Ad — ρ≈0.225, r_ε≈0.474 [N].  
5. Verified recipe (float eig → ulp/Rump/Temple / ‖K^k‖^{1/k}) — not closed as [CA] (float Mh,T,s; Krylov enclosure not finished in timebox).

### 3.3 Continuum r_ε ≤ 0.5 [CA]

**Not achieved. Not registerable.**

**If** the Fourier mid r_ε≈0.474 were [CA], it would cover soft semiprime C0=1 at both p=1409 and p=3307 and soft 0.48–0.50, but **not** greedy 0.418.  
**If** only the HS majorant 0.572 were [CA], it would cover p=1409 semiprime C0=1 only—not p=3307 (0.527) and not soft 0.50.

---

## 4. Estimate U_cross

Statement [P-sketch] in `logs/cert/crossline/`. Numeric: p=11 r_eff≈0.325; p=13≈0.480; p=17 lemmaS geometric only; p=37 no data. **No transfer [CA].**

---

## 5. Conditional chain (status only)

| Input | Status |
|---|---|
| C_gap=1 | project [CA] |
| C0≤0.30209 singles | [CA-fp] |
| pairs ≤0.094 | **[CA-fp] all 1350** |
| shorts ≤0.6 | **open** (3 blows) |
| r_ε≤0.472 or ≤0.5 continuum | **not [CA]** |
| Soft room arithmetic | [P-arith] OK **if** Estimate U holds with small C0 and r in soft range |
| H5(b) / H1 | **not theorems** |

---

## 6. Bottom line

```
REGISTERABLE [CA] (narrow / project):
  — none new that meet full referee eigenpair + spectral-radius standards
  — project C_gap=1 (inherited)

REGISTERABLE [CA-fp] / [N13-conv]:
  — singles activity ≤ 0.30209
  — all 1350 coded pairs core |r̃| ≤ 0.09375

NOT REGISTERABLE (research notes):
  — continuum / discrete r_ε ≤ 0.5 [CA]          FAILED
  — shorts max|z|≤0.6 for all 200               FAILED (3 blows)
  — eigenpair full Rump enclosure               FAILED
  — U_cross (C0,r) transfer                     open
  — H5(b), H1                                   open

NUMERIC LANDSCAPE (not claims):
  — continuum Fourier mid r_ε ≈ 0.474
  — discrete HS majorant r_ε ≤ 0.572
  — soft semiprime C0=1: need r<0.600 (p=1409), r<0.527 (p=3307)
```

---

## 7. File index

| path | role |
|---|---|
| `REFEREE_CERT.md` | hostile audit (a GAP, b CONFIRM, c GAP) |
| `logs/cert/c0_types/arb_singles.json` | singles activity |
| `logs/cert/c0_pairs/` | remaining pairs prec96 + `00_summary.json` |
| `logs/cert/shorts/` | enumeration, relabel, nonrel arb |
| `logs/cert/continuum/30_fourierK.json` | continuum Fourier mid [N] |
| `logs/cert/continuum_ca/` | soft room + honest continuum failure |
| `logs/cert/rho_power/` | HS majorant, ‖MH^k‖^{1/k} |
| `logs/cert/verifyeig/` | eigenpair Rump/BF attempt |
| `logs/cert/crossline/` | U_cross statement + numerics |
| `code/cert_*.py` | drivers |
