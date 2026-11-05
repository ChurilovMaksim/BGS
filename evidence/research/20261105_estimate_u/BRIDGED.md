# BRIDGED — is r_ε < 0.418 necessary?

Grok Bot, 2026-11-05 (CET). Follow-up to `REPORT.md`. Repo BGS @ 6f69baa1.
Grok47 sources: `grok47/h5_xline.md`, `h5_factor.md` (from `research-grok46-1104`).
Referee gap constant 1.214 from `/workspace/research1105b/REFEREE.md`. **Nothing pushed.**

**Labels.** [P] / [P-sketch] / [CA] / [N] / [H] / [C] as in REPORT.md.

**Code / logs.** `code/bridged_rereq.py`, `logs/bridged/r_req_table.json`, `hybrid.json`,
`entropy_table.json`, `arb_r_thresholds.json`.

---

## 0. Answer in one paragraph

**No: 0.418 is not forced by the bridged mechanism.** It is the r-translation of grok47's
γ*_M = 0.9909, which is the exponent that makes the **greedy many-prime majorant**
2(∏(1+q_j^{−γ})−1) fit the idealised slack/M at p = 3307. That majorant packs ~203 of the
smallest primes ≡ ±1 (mod 2p) allowed by Lemma W. For every divisor structure that is
actually small-ω (semiprime 2p+1, or ω ≤ 20), and for the hybrid that sends large-min
lines to the vacuum bound e^{−0.058 p}, the bridged requirement softens to

```
r_ε < 0.48 … 0.60   (C₀ = 1)
```

against which the [N] cutoff value 0.472 (η = 1/20) and C′ proxy 0.54 become **plausible**.
They are **not** certified, and they fail as soon as C₀ ≳ 10 or the per-site type entropy
B ≳ 2. Full greedy still needs ≈ 0.418. Arb certification of the cutoff spectral radius
was **not** achieved and would not discharge the O(1)-prefactor issue in any case.

---

## 1. Where 0.418 came from [P-arith, grok47]

Grok47 `proofs/h5_xline.md` Prop. 1:
- Rooms: slack(1409, δ_rob) ≈ 0.02011, slack(3307, δ_frag) ≈ 0.003347 [P-arith].
- Majorant [P]: Σ_{cross lines} min(d,h/d)^{−γ} ≤ 2(∏_j (1+q_j^{−γ}) − 1), with {q_j} the
  shortest primes ≡ ±1 (mod 2p) of product ≤ h_p (greedy).
- γ*_abs = 0.8737, γ*_M = 0.9909, both binding at p = 3307.

research1105b then set γ = log(1/r_ε)/log ε from the polymer gap
K > log_ε min − 2 log_ε A − 1.214 [P, referee], and demanded γ > γ*_M, i.e.

```
r_ε < ε^{−0.9909} ≈ 0.4179.   [CA]
```

That chain is valid as an implication **from the greedy majorant**. It is not the only
implication the bridged mechanism allows.

---

## 2. (i) Bridged polymers with entropy [P-sketch]

**Gap.** A bridging defect of coefficient size A and ε-span K that is not in (η₊η₋) obeys
[P, referee]

```
K > log_ε min(d₊,d₋) − 2 log_ε A − 1.214.
```

**Activity.** Under Estimate U, |z| ≤ C₀ r^K on such a polymer.

**Counting.** Let N(K) be the number of bridging types of span K.
- If the types are a **finite list** independent of K (N11 short clusters, N12-F1: ~200
  short types), then N(K) ≤ N_* and
  Σ_{K≥Kmin} N(K) C₀ r^K ≤ N_* C₀ r^{Kmin}/(1−r) for r < 1.
  Absorbing N_*/(1−r) into C₀ leaves the same γ = log(1/r)/log ε. **Entropy B = 1.**
- If types grow as B^K (digit alphabet of size B per ε-site, or (2A+1) coefficient
  choices), the geometric sum is C₀ (B r)^{Kmin}/(1−B r), and the effective rate is B r:
  γ_eff = log(1/(B r))/log ε. Then the r-budget shrinks by 1/B.

**N11 alphabet.** Single-bump types 𝒯 = {±1,±√2,±2,±2√2,±4} have |𝒯| = 10 and span ≤ 3.
Long bridging defects are not yet reduced to a finite list; the honest entropy is [C].
Using B = 1 (finite-list hope) keeps the soft thresholds below; B ≥ 2 already forces
r < 0.30 for the semiprime room at p = 1409, below every [N] candidate.

---

## 3. (ii) Requirement vs divisor structure [P-arith]

Write L_line ≤ C₀ · min(d₊,d₋)^{−γ} for the bridged contribution on one line, and demand
Σ_{cross} L_line < slack (idealised, tails/Y zeroed as in grok47).

### 3.1 Semiprime / TRACE-350 (ω = 2, min = 2p+1) [P-arith]

Two cross lines, min = q = 2p+1. Need 2 C₀ q^{−γ} < slack.

| p | slack | C₀ | γ_req | r_ε_req | 0.472 fits? |
|---|---:|---:|---:|---:|---|
| 1409 | 0.02011 | 1 | 0.579 | **0.600** | yes |
| 1409 | 0.02011 | 10 | 0.869 | 0.465 | no |
| 1409 | 0.02011 | 100 | 1.159 | 0.360 | no |
| 3307 | 0.003347 | 1 | 0.727 | **0.527** | yes |
| 3307 | 0.003347 | 10 | 0.984 | 0.420 | no |

### 3.2 Truncated ω, exact / majorant, C₀ = 1 [P-arith]

Worst-case primes = greedy shortest. Exact line sum for ω ≤ 16; majorant for ω ≤ 20.

| p | ω | γ_req | r_ε_req | 0.472 fits? |
|---|---:|---:|---:|---|
| 1409 | 3 | 0.645 | 0.566 | yes |
| 1409 | 8 | 0.695 | 0.542 | yes |
| 1409 | 12 | 0.710 | 0.535 | yes |
| 1409 | 16 | 0.721 | 0.530 | yes |
| 3307 | 2 | 0.727 | 0.527 | yes |
| 3307 | 8 | 0.808 | 0.491 | yes |
| 3307 | 16 | 0.825 | 0.483 | yes |
| 3307 | 20 | 0.830 | 0.481 | yes |

Margin over 0.472 shrinks with ω but stays positive through ω = 20 at C₀ = 1.

### 3.3 Full greedy (the 0.418 source) [P-arith]

| p | γ*_abs | r_abs | γ*_M | r_M |
|---|---:|---:|---:|---:|
| 1409 | 0.771 | 0.507 | 0.896 | 0.455 |
| 3307 | 0.874 | 0.463 | **0.991** | **0.418** |

Only the M-reading at p = 3307 forces 0.418. It assumes the divisor set can be the full
greedy pack of length 203. Lemma W **permits** that cardinality (w_max = 231); it does
not assert that any h_p attains it. [H]: actual ω(h_p) is small; [P]: no theorem caps ω
below ~20.

### 3.4 Hybrid vacuum + bridged [P-arith / P-sketch]

Charge lines with min > Q to the vacuum bound |X| ≤ e^{−0.058 p} (Estimate U at the
referee c ≥ 0.058, C = 1). Charge min ≤ Q to C₀ min^{−γ}.

At both conditional primes, with Q ∈ {(2p+1)^2, (2p+1)^3, 10^6…10^{12}} and ω ≤ 20:
- C₀ = 1 ⇒ r_ε_req ∈ **0.50–0.60**, and 0.472 fits.
- C₀ = 10 ⇒ r_ε_req ∈ **0.41–0.47**, and 0.472 fails.

Vacuum budget n_vac · e^{−0.058 p} is negligible against slack at these p (e^{−0.058·1409} ≈ 10^{−35}).
The hybrid does **not** remove C₀-sensitivity. Scope gap: vacuum e^{−cp} on axis sub-lines
is [P-sketch] (needs Estimate U on those classes); the arithmetic of the split is [P-arith].

---

## 4. (iii) Comparison with [N] candidates

| candidate | value | vs soft req 0.48–0.60 (C₀=1, ω≤20) | vs greedy 0.418 |
|---|---:|---|---|
| cutoff η=1/20 r_ε | 0.472 | **fits, thin margin** | fails |
| cutoff η=1/8 r_ε | 0.417 | fails soft? borderline at ω=20 | ≈ equals |
| C′ proxy √((1.2744/μ*)³) | 0.543 | fits comfortably at ω≲8 | fails |
| fixed-twist \|t\|≥0.25 | 0.53–0.68 | mixed | fails |
| empirical p=11 / p=13 | 0.325 / 0.480 | fits / borderline | p=11 only |

**Verdict on (iii).** Yes: under C₀ = 1 and either (a) ω(h_p) ≤ 20, or (b) hybrid with
Q ≳ (2p+1)^2, or (c) the TRACE-350 semiprime, the bridged requirement is r_ε < 0.48–0.60,
and the [N] value 0.472 is in range. It is **not** in range for C₀ ≥ 10, for type-entropy
B ≥ 2, or for the unrestricted greedy majorant.

---

## 5. (iv) Certified bound for the cutoff? [not obtained]

**What the cutoff 0.472 is.** Spectral radius of the H-relative second-moment operator
averaged over twists with dist({0,½}) ≥ 1/20, by float power iteration on a 48-point grid
(`REPORT.md` §3.2). It is a rate for i.i.d. non-resonant steps, not a polymer activity
with prefactor C₀.

**What Estimate U needs.** ‖B‖_H / μ* ≤ r on non-resonant **blocks**, with C₀ absorbing
gap-contraction and conversion. N11 §2: the existing Cpow ≤ 3246.8 makes C₀ ~ 10^8 before
the adapted norm; TRACE-311 gives the norm but not O(1) bump norms.

**Arb attempt.** Thresholds ε^{−γ} for the scenario γ's are [CA]
(`logs/bridged/arb_r_thresholds.json`). Full arb enclosure of ρ_cut would require interval
495×495 matrices on the quadrature grid and a validated power/PSD iteration. That was not
run: even a certified ρ_cut < 0.48 would leave C₀ open, and C₀ ≥ 10 already kills the soft
room. **(iv) is blocked by the prefactor, not by the missing interval spectral radius.**

---

## 6. What would make soft r enough for a theorem [C]

A proof of H5(b) along the bridged route with r_ε ≈ 0.47 needs **all** of:

1. Estimate U with **C₀ ≤ O(1)** (say ≤ 3) and r ≤ 0.47. [open]
2. Type entropy B = 1 (finite bridging list up to the gap length), or B r still < 0.48. [C]
3. Either
   - (3a) ω(h_p) ≤ 20 for all large p in the conditional range, **or**
   - (3b) hybrid: vacuum e^{−0.058 p} on lines with min > Q₀ (e.g. (2p+1)^2) proved for
     axis sub-lines too, **or**
   - (3c) restriction to 𝒫 ∪ {ω ≤ 20} ∪ TRACE-350.
4. The idealised slack of grok47 Prop. 4 replaced by the v5 additive budget (still open).

Without (1), softening the γ* target does not close H5(b). With (1) and (3a)/(3b), the
greedy 0.418 target is unnecessarily strong.

---

## 7. Bottom line

| claim | status |
|---|---|
| 0.418 is the greedy-M translation of γ*_M at p=3307 | [P-arith] |
| Soft requirement r_ε < 0.48–0.60 for C₀=1, ω≤20 / semiprime / hybrid | [P-arith] |
| [N] cutoff 0.472 fits the soft room | [N], thin margin |
| Soft room survives C₀ ≥ 10 or B ≥ 2 | **false** [P-arith] |
| Certified Estimate U at r ≤ 0.47 | **not obtained** |
| H5(b) discharged | **no** |

The right target for the next analytic push is **C₀ = O(1) in Estimate U**, not a better
spectral radius. Once C₀ is O(1), the bridged arithmetic of this note makes r_ε ≈ 0.47 a
usable constant for every Lemma W–realistic divisor pattern short of the full greedy pack.
