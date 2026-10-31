# Referee report — BGS Lines N8 and N8b
Grok Bot, 2026-10-31 (Asia/Yekaterinburg, UTC+5). This is a read-only audit: nothing in /workspace/bgs-lineN was modified and nothing was pushed.

**Inputs.**
- N8/{REPORT_N8.md, NOTES_N8.md, code, logs}: SHA256_N8.txt verifies OK.
- N8b/{REPORT_N8b.md, NOTES_N8b.md, code, logs}: SHA256_N8b.txt verifies OK.

**My artifacts** (in /workspace/audit/lineN8):
- `code/rerun_q_propx2.py`: N8's q_propx2.py with the output path redirected.
- `code/ref_bases.py`: the fixed-point adjudication and the missing-bases test.
- `code/ref_Ic.py`: an exact check of identity (I_c).
- `logs/`: outputs of the above.
- `lean/LineN8Arith.lean`: builds clean. It uses norm_num and kernel `decide` on naturals; there is no sorry and no native_decide.
  - It is compiled read-only against the Mathlib build in /workspace/audit/pr66/wt_head, via LEAN_PATH.

**Environment note.** The usual build dir /workspace/audit/pr63/repo/formalization had lost its Mathlib build. My `lake env` call made lake re-clone the packages into that clone's untracked `.lake` directory. Tracked files are untouched (git status is clean), but the Mathlib build there is still missing. Rebuilding it needs `lake exe cache get`, which I did not run.

## Verdict
- **N8: READY-after-fixes.**
  - F6 is required: the claim "r₂ is not the bottleneck" overstates what the certificate covers.
  - F8 is required: stale p16.
  - F3 is hygiene.
- **N8b: READY-after-fixes.**
  - F7 is required: the numerical support for hypothesis G is narrower than stated.
  - F2 is required: prime powers in K_p.
- **The "4 fixed points, not 8" erratum is upheld** (N8b-F3). It shows my N7 audit missed an error.
- **Theorem R♯:** still conditional. The open inputs are listed in the status section at the end.

## N8
**Independent checks.**
- **Class certificates.**
  - I re-ran q_propx2 for fam, near0, z_7_2 and q_3_0 and reproduced the published E_e and p₀ exactly (near0: w0 = 320, L_e = 1, p0 = 1289, E = 7.37e-10).
  - The near-0 enclosure Re w₀ ∈ [2.3588e-5, 3.6143e-5] contains my independent TW values: 2.9866e-5 (L = 8/10; N6 audit) and Re 2.99e-5 at p = 29 (`ref_bases`, z = 0, e = 2√2).
  - The family check (z = ¼, e = 2, |r| = 3.955e-4) also reproduces.
- **Absolute-class total.** Σ|w| ≤ 1.2165e-6. With the Prop X′ errors this is ≤ 0.43% of Re w*_lo (Lean `abs_total`, `abs_share`). The 16-class count and the four positive classes check out.
  - The list is hand-picked (for example (5,¼), (5±√2,0) and (7±2√2,¼) are absent), not "all classes with |N| ≤ 41". This is harmless, because everything uncertified goes to the A∞-tail. But "0.42%" is a statement about the listed classes only.
- **Riesz bound sup_n‖Lⁿ(I−Π)‖ ≤ R₂′ = 3224.84: correct.**
  - Line F's certificates use r2 = 1 (top-level `r2` field).
  - Their resolvent bound is a Neumann-series bound, valid for all \|z\| ≥ 1. That rules out spectrum in \|z\| ≥ 1 apart from μ, so the Riesz–Dunford integral on \|z\| = 1 is legitimate.
  - This closes the "coll" justification gap I raised for N6.
- **Other sectors.**
  - The values R₂′(a) = 369.36 / 739.91 / 739.91 match my reconstruction from Line F's RA_r2 and ‖X‖, (RA+1)(1+‖X‖)+1, to 6 digits.
  - The set of non-dominant sector operators is the same for window twists 0 and ½, because L_{a,τ+½} = L_{a+4,τ}. One bound therefore serves both bases.
  - p ≥ 485 is verified exactly in Lean (`other_sector_485`, m = 1455, 6×39 core steps, rational bounds). Bop = 40.85 itself is taken from N8's r_other.json; it was not re-derived.
- **Prop X′ architecture.** Writing out the 6-block telescoping and rank-one collapse (Tr Π = 1, so ∏ r_kΠ has trace ∏ r_k) is enough for [P mod Line F + CA] *for certified classes*. The proof is still a paragraph; it should become a numbered lemma.

**Findings.**
- **N8-F1 (OK).** Certificates, q_propx2 constants and the near-0 positivity reproduce. Dropping near-0 is legitimate: the Lin weight (2n/q²)|Z|²·Re(Ẑ/Z) is ≥ 0, and Re is the same for both ρ.
- **N8-F2 (OK).** The R₂′ Riesz argument is valid, with r2 = 1 and Neumann exterior validity. The coll term is now justified.
- **N8-F3 (hygiene).** r_other.py obtains R₂(a) as F_R2/Pert_{n_cert}. That equals Line F's R₂ only if Line F's Pert equals n_cert's.
  - They agree numerically to 6 digits, but R₂ should be computed directly as full_R(RA_r2, 1).
  - The E-family (certE) absorption was not run, so it is [P-sketch]. Label it.
- **N8-F4 (labels).** Prop X′ → [P mod Line F certs + class CA], for certified classes only. The k-parity mechanism stays [P-sketch]; equal endpoints are [CA] for 16 classes.
- **N8-F5 (threshold, minor).** p ≥ 1289 is an artefact of τ = 1e-9.
  - Positivity of near-0 needs only E < 2.36e-5, so a much smaller p₀ suffices.
  - The family at τ = 1e-9 would need 1321; that value is not used, and the family keeps E ≤ Re w*_lo/2 at 1165.
  - State p₀ as a choice.
- **N8-F6 (exaggeration, required): "r₂ is not the bottleneck".**
  - The certified r₂(k) = R(k)^{1/k} contains the prefactor (Cpair = 25.8 for 8V; R(200) = 1.9e7). r₂(200) = 1.0874 therefore applies only to blocks of ≥ 200 steps, i.e. cores of ≥ 200 steps, i.e. N(e) ≳ λ^{100} ≈ 10^{76}.
  - "Shorter cores are finitely many classes (§1-type certificates)" is not workable: there are ≈ 0.23·N classes per shell, so roughly 10^{75} classes would need individual certificates.
  - At short blocks R(k)^{1/k} ≥ Cpair^{1/k}·r gives a heuristic estimate: k = 10 → about 1.45, k = 8 → about 1.50 > 1.481.
  - So r₂ *is* a constraint for cores shorter than about 10–20 steps, and it is uncertified between about 10 and 200.
  - Fix:
    - run N2's e_r2 at k = 10, 20, 50, 100 (cheap);
    - handle shells with core length < k_min by another route (the sup-norm majorant is finite there);
    - restate the claim.
- **N8-F7 (derivation missing).** The aliased family HS² mass "1.52^p" is μ*²/λ^{1/2} = 1.5198 per step, against the threshold μ*³λ^{−1/2}/Λ = 1.4810. It is labelled [P, N8 analysis] but no derivation is written. Add the two-line computation. The conclusion (apply the estimate shell by shell, family excluded) stands.
- **N8-F8 (stale, required).** §5 cites my *interim* `ref_robin16` (p ≥ 498). My final N7 report resolved this:
  - p16 = 339 is correct with N7's sharp two-term B16 (≈ 706·1.63541^m + 2.27e5·0.95^m);
  - 498 applies only to the crude single-constant form.
  
  N7-F1 asks N7 to state this; N8 should not replace 339 by 498.
- **N8-F9 (A∞ bookkeeping).** Because of N8b-F3, the class enumerations in N7 and N8 cover only the bases z ∈ {0, ¼}. They omit the genuine fixed points √2/8 and ¼+√2/8.
  - My p = 29 test (`ref_bases`, exact twists, TW) found the shallowest classes at those bases have N = 14 and \|r\| ≈ 8.6e-25. They are numerically negligible, and the A∞-tail covers them by definition.
  - State this explicitly. The base-0/¼ numerics (9.5% total, 0.6% tail) are unaffected.
- **N8-F10 (open, honest).** (R1) box-restricted shell lemma and (R4) deep points remain open. N8b's observation matters here: for short windows the true \|r\| is 10³–10⁴× above the w-limit. Deep-point bounds therefore cannot come from w(z,e).

## N8b
**Independent checks.**
- **(E1)/(E2).** Verified by hand from γ = (ε^{k+1} − ε′^k)/√2.
- **Identity (I_c).** Exact check (`ref_Ic`): **54,810 checks, 0 failures**. It covers c ∈ {23, 353, 79, 599, 103, 15607, 47}, both consistent lines with the stated σ, s ≤ 29, and three t shifts.
- **r ≡ 1 (mod 2p).** The proof is correct:
  - x_p² − 2y_p² = −1, so 2 is a QR and r splits;
  - 2x_p = ε^p − ε^{−p}, so ε^{2p} ≡ 1 mod 𝔯 and ord ∈ {p, 2p};
  - therefore p ∣ r−1, and since r is odd, 2p ∣ r−1.
  
  On all 16 factorisations (p < 62): every r ∣ h_p is ≡ 1 mod 2p, and every r ∣ K_p (r ≠ 7) is ≡ 1 mod 6p. **But K_5 has 31² and K_7 has 7².**
- **κ floor.** κ = (½ln λ)/(2ln μ* − ln r₂) ∈ [0.7060, 0.7062] (Lean `kappa_floor`, `kappa_upper`, exact). The monotonicity in Λ holds because 2ln T′ > ln r₂.
  - μ*²/λ ∈ [0.6294, 0.6296] and μ*³/λ ∈ [1.2057, 1.2059] (Lean).
  - κ₃ at the floor is 0.5211 and the R₃ ≤ 1.3284 threshold reproduces (by hand).
- **The "inconsistent lines at h_p" flag.** This is the same gap as my N7-F6, and N8b's rel_abs 2.7e-3 at p = 11 matches my 0.14% + 0.09%.

**Findings.**
- **N8b-F1 (OK, [P]).** Lemma P′_c (i)–(v) and identity (I_c) hold, and the consistent/inconsistent dichotomy is correct.
- **N8b-F2 (required, small).** r ≡ 1 (2p) for r ∣ h_p is [P].
  - Lemma Σ and the K_p route must allow **prime-power** factors: 31² ∣ K_5 and 7² ∣ K_7 occur, and nothing excludes them for large p.
  - **Bonus:** apply it to N7-F5. Since the j-th prime factor of h_p is ≥ 2pj+1, Σ2/r_i ≤ H_ω/p ≤ 6/1165 < 0.52% at p = 1165, instead of 11.4%. So **F_m ≥ 2.32e-3·p\|Z₈\|²/h_p** (Lean `harmonic132`, `loss_improved`, `fm_improved`). Recommend adopting it.
- **N8b-F3 (erratum for N7 Lemma P′(i): UPHELD).**
  - λ−1 = 2ε, so the λ-fixed set on K/O^∨ is ½O^∨/O^∨ = (√2/8)O/O^∨, which has 4 points: {0, √2/8, ¼, ¼+√2/8}.
  - (1/8)O/O^∨ has 8 points, and 4 of them are not fixed: there λz − z ∉ O^∨, and the twist shifts by ½. My `ref_bases` enumeration confirms 8 representatives and 4 fixed points.
  - **Consequences:**
    - The representation x = z + eγ/(8q), e ∈ O, holds for any z with 8z ∈ O. The twist formula in (ii) and the window structure need z fixed, so restrict to the 4.
    - N7 §3's window twist values "{0, ¼, ½, ¾}" are wrong. Only {0, ½} occur (Tr z ∈ {0, ½}).
    - N7's checks used z ∈ {0, ¼}, both genuine, so no numerical result is wrong. Bases √2/8 and ¼+√2/8 were not enumerated (N8-F9).
  - **Referee self-correction #3:** I passed this in N7.
- **N8b-F4 (OK).** The classification table and the amplification A_c ≈ h_p/c are consistent with TRACE-228 inheritance. I did not re-derive I(c) ∈ [1, 1.2].
- **N8b-F5 (OK, honest).** Prop X′_c is [P-sketch]. The short-window caveat (w underestimates \|r\| by 10³–10⁴) is important and correctly stated.
- **N8b-F6 ("mixed-gap impossibility": scope).** The 0.7060 floor is a theorem *about the two-block op·HS² method*: any Λ ≥ μ* gives κ ≥ 0.7060 with the certified r₂. It is not an impossibility statement about the mixed gap. §7 says this; the summary row and the brief's wording should say it too.
- **N8b-F7 (evidence for G, required).** Hypothesis G(Γ, A) with Γ < 1.2329 is required for **all** residual points, including unit and partially isotropic points (Lemma Σ(d)). The "Γ_eff ≤ 1.069, wide margin" evidence covers isotropic residual lines only.
  - On the inconsistent line at h_13, Γ_eff = 1.267 > 1.2329.
  - For mixed points at p = 11 (N7 and my replicate), \|r\| reaches 1.4e-4 at m = 33, which is Γ_eff = 1.46 with A = 1. G then needs A ≳ 300.
  - There is no numerical evidence on unit or mixed patterns at large p. G must be labelled as unsupported for those pattern types.
- **N8b-F8 (C2 scope).**
  - C2 needs infinitely many prime h_p. That is open, a Mersenne-type conjecture; the census has 13 BPSW-PRPs for p ≤ 3989, and only p = 1493 and 1901 are ≥ 1289.
  - If frozen R′ (TRACE-206) is an *explicit* inequality at each m rather than an o(m) statement, a single verified p would suffice. The authors should state which form R′ takes. That decides whether "infinitude of 𝒫" is needed at all.

## Overall status of Theorem R♯
**Proved or certified now:**
- **[P]:**
  - the positivity lemma;
  - the trivial floor;
  - Theorem 16 ((±2,16) at all levels, mod J3 dom [CA]);
  - Lemma P, P′ (with 4 fixed points) and P′_c;
  - r ≡ 1 (2p);
  - the composite weight (F_m ≥ 2.32e-3·p\|Z₈\|²/h_p with the N8b improvement).
- **[P mod Line F + CA]:**
  - Prop X/X′ for the family and the 16 certified classes;
  - the coll term (Riesz);
  - the other sectors for the V family.
- **[CA]:** the family term w*, near-0 positivity, and 10 small absolute classes (0.43%).

**What still stands between R♯ and an unconditional refutation:**
1. **Gap (a), the A∞-tail.** A one-sided bound on all uncertified isotropic classes on the (γ)/(γ̄) lines at h_p.
   - This includes the bases √2/8 and ¼+√2/8.
   - It needs (R1) the box-restricted shell lemma, a short-block r₂ certificate for cores of about 10–200 steps (N8-F6), and (R4) deep points.
   - Numerically the tail is ≈ 0.6% against a budget of ≈ 89%.
2. **Gap (b)/(b′).**
   - The isotropic residual classes (consistent at c ∣ h_p, which are deep (a)-classes amplified by h_p/c; consistent rank-3p; inconsistent lines including those at h_p itself) all reduce to the single pointwise input G(Γ < 1.2329, A independent of p).
   - Unit and mixed patterns at λ^{0.5p} ≤ ι < λ^{0.7376p} need G or a certified R₃ ≤ 1.33 / R₄ ≤ 2.61. The two-block method provably cannot do it (κ ≥ 0.706).
3. **Standing certified inputs** (float-BLAS-with-γ_n [CA]):
   - n_cert;
   - Line F (V sectors; E sectors only sketched);
   - J3 dom;
   - TRACE-199/212/213/228 as registered.
   - The E-family other-sector absorption has not been run.
4. **Form of R′:** a single verified p could suffice if TRACE-206 is explicit (N8b-F8). Otherwise infinitely many p are needed, and C2 additionally needs infinitely many prime h_p.

**Honest summary.** Every remaining gap is a statement about *uniform pointwise or shell-averaged decay of excursion products*: G for (b), and R1/R4 for (a). All numerics are favourable by wide margins on isotropic patterns. Evidence for unit and mixed patterns at large p is absent. No route is yet more than a well-posed target. The most leveraged next step is a certified short-block r₂(k), k ∈ [10, 200], plus a box-restricted shell lemma. That step serves (a), and via G on consistent lines, much of (b).

## Lean (`lean/LineN8Arith.lean`)
- `abs_total`, `abs_share`
- `p0_near0`
- `other_sector_485` (exact naturals, m = 1455)
- `kappa_floor`, `kappa_upper`
- `fp_r2`, `fp_R3`
- `harmonic132`, `loss_improved`, `fm_improved`

Uses `set_option exponentiation.threshold` / `maxRecDepth`; no sorry, no native_decide.
