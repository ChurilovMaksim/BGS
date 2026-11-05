# REFEREE_CERT — hostile independent check of CERT.md CA claims

Referee: Grok Bot executor (independent of the CERT authoring run).
Date: 2026-11-05 (Europe/Berlin).
Target: `/workspace/research1105c/CERT.md` (+ C0.md, BRIDGED.md, REPORT.md, `logs/cert/`, `code/`).
Repo scope requested: ChurilovMaksim/BGS `main` @ `4487e66a`. Local clone is at parent `6f69baa1` (CERT’s pin); `4487e66a` is the later merge of PR #92 (Lemma S / TRACE-352..355) and was **not** checked out. CA artefacts under `research1105c/` do not depend on that merge for (a)–(c).
Nothing pushed.

**Labels used here.** CONFIRMED / GAP / WRONG. Hostility = demand that [CA] mean interval-closed quantities Estimate U actually needs, with no silent float-as-exact.

Venv: `/workspace/lineNgas/venv` (python-flint). Independent drivers: `referee_cert/indep_a_singles.py`, `referee_cert/indep_c_rho_fast.py`. Logs: `logs/cert/referee/`.

---

## Verdict table

| item | CERT claim | verdict |
|---|---|---|
| **(a)** C0 ≤ 0.30209 [CA] on singles 𝒯 ∪ 𝒯ε | number reproduces; quantity is activity \|ψ̃BΦ/(ψ̃Φ)\|, not ‖B‖_H | **GAP** (narrow: number OK as activity; not full Estimate-U C0 / ‖B‖_H) |
| **(b)** max\|z\| ≤ 0.094 [CA] on 587/1350 coded pairs | number true on N13 `c_replay` partial; unfinished list larger in corrupt float scan | **CONFIRMED** for the stated partial core-\|r̃\| claim; see caveats |
| **(c)** r_ε ≤ 0.472269 [CA] discrete K_g (η=1/20, Nq=48) + Pert_H | mid ρ reproduces; enclosure logic not a theorem; continuum honestly open | **GAP** |
| Conditional chain §3 | mostly careful; some soft overreach | **GAP** (not WRONG) |

---

## Definitions (Estimate U / TRACE-311)

From `REPORT.md` §1.1 (N11 / TRACE-311):

```
|z_γ| ≤ C₀ · r^{n_nr(γ)}
```

Equivalently: ‖B‖_H / μ* ≤ r on non-resonant blocks, with C₀ absorbing O(1) gap prefactors after TRACE-311 V3b (‖(A0/s)Q̃‖_H ≤ κ=0.45 **in one step, constant 1** ⇒ C_gap = 1).

So Estimate U needs **both** a usable C₀ and a rate r. CERT’s (a)/(b) attack C₀-like activities on the N13 typed list; (c) attacks a discrete second-moment rate.

---

## (a) C0 ≤ 0.30209 [CA] for singles 𝒯 ∪ 𝒯ε

### What was certified
`code/cert_C0_arb_singles.py` → `logs/cert/c0_types/arb_singles.json`:
- max \|ψ̃ B Φ / (ψ̃ Φ)\| ≤ **0.302087097762** (arb upper)
- max ‖B Φ‖_H (via float T·mid + c_hi·rad pad) ≤ 0.302087127745
- with ad hoc Pert_H pad: **C0_certified_for_activity = 0.3020893 ≤ 0.30209**

### Independent rerun
`referee_cert/indep_a_singles.py` at flint prec 96, same cert_core blocks, own driver:

| type | indep abs_sc_up | CERT |
|---|---:|---:|
| single odd | 0.302087097760 | match |
| single_eps odd | **0.302087097762** | match |
| others | ≤ 0.18 | match |

Indep max = **0.3020870977621713**, C0_pad = max·(1+10·2.1e-8) = 0.30208716 ≤ 0.30209.
(CERT’s slightly larger 0.3020893 uses the ‖BΦ‖_H branch + looser pad; still ≤ 0.30209.)

### Is it the Estimate-U quantity?
**Partially.** For these fixed finite geometric singles, activity z = ψ̃BΦ/(ψ̃Φ) **is** the polymer weight Estimate U bounds. Taking C₀ ≥ max\|z\| on this finite list is the right C₀-piece **for this class**, with C_gap=1 already [CA] in TRACE-311 / N12 V3b.

It is **not** the equivalent form ‖B‖_H (operator). CERT’s own note admits that. Scalar path \|z\| ≤ ‖BΦ‖_H with ‖Φ‖_H=1 is fine for activity; it does not give a uniform block norm for arbitrary non-resonant words.

### Arb rigor
| issue | severity |
|---|---|
| Φ, ψ, s from binary64 npz → `acb(..., rad=0)` (float-as-exact eigenpair) | **structural** — same N13 `c_replay` convention; not an enclosure of the true eigenpair |
| cert_core block radii used in the chain | OK (entry rads ~1e-20) |
| L1/L2 via `float(ceil(log))` | minor for small singles; see (b) for large seeds |
| ‖BΦ‖_H via float T + hardcoded c_hi=15.1962 (npz has ~15.181) | only affects tiny rad pad |
| Pert_H=2.1e-8 ×10 pad | ad hoc, numerically negligible here |

### Scope caveats in CERT
Honest: singles∪pairs only; not shorts; not full ‖B‖_H; not arbitrary non-res words; not core→true for composites. **Acceptable.**

### Verdict: **GAP**
Number and activity interpretation **confirmed** by independent arb rerun. Tag [CA] is overstated relative to a hostile reading (float eigenpair; not ‖B‖_H). As “N13-style [CA] activity on the 10 singles”, the bound ≤ 0.30209 stands. Not enough alone for Estimate U.

---

## (b) max\|z\| ≤ 0.094 [CA] on 587 of 1350 coded pairs

### What was certified
`creplay_partial.json`: 597 N13 `c_replay.jsonl` lines = 10 singles + **587 pairs**, pair max abs_up = **0.093752532066** ≤ 0.094.
Worst pair: `odd+odd`, G=4, h=0, k=11.

Independent check of the jsonl: all 587 pair rows have max(A.abs_up,B.abs_up) ≤ 0.093752532066; expected coded-pair count is 1350; k=10..596 contiguous, none missing.

### Is it the Estimate-U quantity?
Same as (a): core functional r̃ = ψ̃v/(ψ̃Φ), **not** true window weight. N13 REPORT explicitly leaves core→true for composites open (cost involves Γ_X and Pert_H). So this is a **core-activity** bound on a partial typed list, not full Estimate-U C₀ on pairs.

### Critical cross-check: forward [N] vs arb [CA]
CERT also quotes float forward max on all 1350 pairs ≤ **0.1576** [N]. For the same job k=291 (`sq2+odd`, G=14, e≈5e10):

| source | ctx.prec | \|r\| |
|---|---:|---:|
| N13 `c_replay` arb | 96 | **0.05309** (abs_up) |
| forward / a_ops recompute | **64** | **0.15764** |
| a_ops recompute | **96** | **0.05254** |

**Root cause:** `core_floats` / `red(e1·λ^j)` at flint **prec 64** loses fractional accuracy for \|e\|≳1e10; twists are wrong; products inflate. At prec 96 they match arb. Forward (`cert_C0_forward.py` line 11: `ctx.prec=64`) therefore **corrupts large-G pair activities**. About 188/587 creplay pairs have \|e\|>1e9.

So:
- CERT’s **[CA] ≤ 0.094 on 587/1350** is the trustworthy figure for those jobs.
- CERT’s **[N] ≤ 0.1576 on 1350** is a **precision artifact**, not evidence that unfinished pairs exceed 0.094.
- Shorts’ worst seed has tiny e=[4,−2]; the float 0.5218 is **not** explained by this bug (arb still radius-blows as CERT says).

### Arb rigor
Same float-eigenpair issue as (a). Some large-G creplay rows have rad ~1e-3; abs_up still a valid upper for the enclosure. Core→true open.

### Scope caveats
CERT correctly says 587/1350 and separates [CA] from [N]. Incomplete list is honest. It does **not** warn that forward pair maxima are prec-64-corrupt — that omission is a GAP in the writeup, not in the [CA] claim itself.

### Verdict: **CONFIRMED**
for the literal claim “max \|r̃\| ≤ 0.094 [CA] on the 587 finished coded pairs”.  
Companion note: forward 0.1576 [N] should be treated as **WRONG/unreliable**; do not use it against soft room.

---

## (c) r_ε ≤ 0.472269 [CA] for discrete K_g (η=1/20, Nq=48) + Pert_H

### What was certified
`logs/cert/rho_cut/03_discrete_CA.json`:
- K_g = (1/\|I\|) Σ_{i∈I} Ad_MH(t_i), I = {t_i = −1/2+i/48 : dist(t_i,{0,½}) ≥ 1/20}, \|I\|=38
- ρ_mid = 0.22303697137851128, eps_res ~ 6.8e-17
- MH_rad from cert_core entry rads ~ 0 at prec 64; pad uses N13 **Pert_H = 2.1e-8** as MH op-radius
- ρ_ub = 0.223037321 ⇒ r_ε = √ρ_ub ≤ **0.47226827 ≤ 0.472269**
- Continuum Lip·Nsum·δ ≈ 32: **not certified** (honest)

### Independent rerun
`referee_cert/indep_c_rho_fast.py`:
- ρ_mid = **0.22303697137851128** (exact match)
- eps_res = 6.79e-17 (match)
- claim-style pad with Pert_H and measured ‖MH‖_F ∈ [2.39, 3.16] → ray_rad_pert ≈ 1.13e-7 → r_eps_claim ≈ **0.47226802 ≤ 0.472269**
- CERT’s ray_rad 3.50e-7 is a slightly looser Mf estimate; same conclusion
- crude F-norm majorant √(Σ w ‖M‖_F²) ≈ 2.71 — useless
- numeric Kato–Temple with random Y-orthogonal probes: gap_est ≈ ρ (probes ~0), kato_r ≈ 0.47226790 — **[N] only**

### Is it the Estimate-U quantity?
**Related, not identical.** Estimate U’s r is a per-site activity rate on non-resonant **blocks** in H-norm. ρ(K_g) is the HS spectral radius of the equal-weight average of Ad_MH over a discrete non-res grid — an i.i.d. second-moment model for digit twists. CERT’s note that digit twists are discrete (so K_g may be the intended object) is fair. It is **not** a theorem that Estimate U may take r = √ρ(K_g).

### Arb / enclosure rigor — main objections
1. **MH assembled from float `a_ops`**, not cert_core arb A(t). Entry-rad MH_rad_op ~ 1e-34 at prec 64 is “mids are exact relative to those rads”, not “float MH = true MH”.
2. **Pert_H = 2.1e-8** is Galerkin→true for **A0** (resonant) in N12/N13. Using it as a uniform op-radius for **all** MH(t) on the grid is unjustified without a twist-uniform perturbation bound.
3. **ρ_ub = ρ_mid + eps_res + ray_rad is not a theorem.** For Hermitian K, a residual ‖KY−ρY‖ ≤ ε‖Y‖ proves *existence* of some eigenvalue in [ρ−ε,ρ+ε], not ρ_max ≤ ρ+ε. Upper bounds need a spectral gap (Kato–Temple), a norm bound, or a validated eigensolver. CERT does not supply a certified gap.
4. Float power iteration / residual themselves are [CA-fp] at best.
5. Continuum open: CERT is **honest** (Lip mesh ~32). Good.

Code/json mismatch: on-disk `cert_rho_cut.py` still computes MH_rad_op from entry rads (~0) and would give r_eps_ub≈0.47226790; the saved `03_discrete_CA.json` was produced by a Pert_H-patched run (label says so). Numbers are consistent with that patch; provenance is slightly messy.

### Scope caveats
Continuum denial: honest. Discrete-only: honest. Soft-room use of 0.472: depends on C₀=O(1) and divisor hypotheses — deferred to chain.

### Verdict: **GAP**
The discrete mid-value ρ≈0.223037 and the numerical claim r_ε≈0.472268 are **reproduced**. A hostile [CA] stamp is **not** earned: float MH, Pert_H misuse, and residual≠ρ_max. Accept as strong [CA-fp]/[N] for the **discrete** operator only.

---

## Conditional chain (CERT §3) — overstatement check

| CERT statement | Referee |
|---|---|
| C_gap=1 [CA] TRACE-311 | Inherited from N12/N13 V3b [CA-float] verify_adapted; not re-audited here. Accept as project [CA]. |
| C0≤0.30209 (coded singles; pairs smaller) [CA] | Singles GAP as above; “pairs smaller” true on finished arb (≤0.094) and likely true in general once prec-64 forward is discarded. |
| C0≤0.522 (all types, float shorts) [N] | Shorts e small ⇒ 0.5218 not the large-e bug; arb still fails (rad blowup). OK as [N]. |
| r_ε≤0.47227 (discrete ρ_cut) [CA] | **Over-tagged**; see (c) GAP. |
| Soft room r_ε\<0.48–0.60 at C0=1 [P-arith] | As in BRIDGED.md; not re-derived; no overclaim that H5(b) is closed. |
| H5(b) vacuum “conditionally OK” with r_λ=(0.47227)² | Arithmetic OK **if** Estimate U holds on those polymers with this (C0,r). CERT marks identification of seam polymers / sub-line as open — **honest**. |
| H5(b) bridged “arithmetic closes” for ω≤20 / semiprime / hybrid | Conditional on C0 and Estimate U on cross-line defects; listed opens are appropriate. Soft overreach: “sit inside soft room” reads stronger than “arithmetic of the idealised slack closes”. |
| H1 not proved; (T) open; TRACE-336 open | **Honest.** |
| Bottom line: “H5(b) is not a theorem” / “H1 is not proved” | Correct; no overstatement. |

**Chain verdict: GAP** — conclusions are mostly carefully conditional; the main overstatement is carrying (c) as full [CA] into the chain inputs table.

---

## Bottom line for the parent agent

```
(a) GAP       — activity ≤ 0.30209 on 10 singles reproduced [arb]; not ‖B‖_H; float eigenpair
(b) CONFIRMED — core |r̃| ≤ 0.094 on 587/1350 pairs; forward 0.1576 [N] is prec-64 WRONG
(c) GAP       — discrete ρ mid reproduced; residual+Pert_H enclosure is not [CA]
chain GAP     — honest on H5(b)/H1 open; over-tags (c) as [CA]
```

Usable positive residue: singles activity ≤ 0.30209 and discrete ρ_mid ≈ 0.223037 are real numerical facts under the N13 float-eigenpair convention. They do **not** discharge Estimate U or H5(b).

### Files written
- `/workspace/research1105c/REFEREE_CERT.md` (this file)
- `/workspace/research1105c/referee_cert/indep_a_singles.py`
- `/workspace/research1105c/referee_cert/indep_c_rho_fast.py`
- `/workspace/research1105c/logs/cert/referee/indep_a_singles.json`
- `/workspace/research1105c/logs/cert/referee/indep_c_rho.json`
