# Referee report — BGS Line N7 (+ REPORT_N6_v2)
Grok Bot, 2026-10-31 (Asia/Yekaterinburg, UTC+5). Read-only audit: nothing in /workspace/bgs-lineN was modified and nothing was pushed.

**Inputs:**
- N7/REPORT_N7.md
- N7/REPORT_N6_v2.md
- N7/NOTES_N7.md
- code, logs, data

SHA256_N7.txt verifies OK.

**My artifacts** (under /workspace/audit/lineN7):
- `code/ref_robin16.py`
- `code/rerun_d_Z16.py`: a copy of N7's d_Z16.py with its output redirected.
- `code/ref_mixed2.py`
- `code/ref_crossline.py`
- `logs/`: their outputs.
- `lean/LineN7Arith.lean`: builds clean, with no sorry and no native_decide.

## Verdict
- **REPORT_N6_v2:** READY. It applies N6-F1..F9 correctly. F10 (my self-correction) needs no author action. F11 is partly addressed: h_rho16 has been run, and o_levels has been run at p = 7.
- **N7:** READY-after-fixes. The required fixes are F3 and F6; F1, F8 and F9 are recommended.
  - Claims (1) on (±2,16) and (2) on the exact identity hold.
  - The gap-(a) reduction is incomplete at composite h_p (F6).
  - The theorem stays conditional on (a), (b), (b′) and the [P-sketch] parts of Prop X.

## Checks of the key claims
**(1) (±2,16) at all levels.** The claim holds, with one clarification (F1).
- I re-ran N7's `d_Z16.py` read-only, writing output to my directory, against the dom/rest certificate JSONs. It reproduces the published numbers: C16 = 2.2726e5, m1 = 51, p16 = 339, and dominant contour radius |b11| + r1 = 1.6354130.
- **Split of the constant.** The bound actually used is the two-term bound B16(m) ≈ **706·1.63541^m + 2.27e5·0.95^m**. The quoted form "2.273e5·1.6355^m" is a valid but crude majorant.
  - With the crude form, the thresholds would be m ≥ 83 and p ≥ 498 (my recomputation, `ref_robin16`). Both are still below 1165, so this is harmless.
- **Logic of Theorem 16.** It is correct:
  - the Dev floor is per ρ;
  - Σ_d n_d/d² ≤ σ(h_m)/h_m;
  - Robin's 1984 bound is unconditional for n ≥ 3;
  - the factor 2 accounts for the two ρ;
  - the bounds h_m ≤ ε^{3p} and h_p ≤ ε^p are conservative.
- **Arithmetic (Lean):**
  - 1.6355² < 2.7350;
  - decay ratio ≤ 0.97802;
  - |b11| + r1 ≤ 1.6355.
- **Caveats:**
  - **Threshold scans.** The scans check only finitely many m and p (m to m+60, p to p+200) and then rely on monotonicity. With the crude constant I verified monotone decrease for 400 further p. The report should state the monotonicity argument explicitly.
  - **Spectral containment.** The 'dom' Cauchy formula needs the spectrum to lie inside the two disks. Contour bounds alone do not exclude eigenvalues in the annulus between them. N7 relies on J3's rig_spec exterior argument, so it inherits J3's [CA] standing. I did not re-run a_dom16 or J3.

**(2) Pattern lemma [P].** Proved.
- **Identity (I).** I proved it in Lean in abstract form (`identity_I`: field_simp plus linear_combination from P = 2q + 1/P).
- **Lemma P′(i).** I checked the argument: e = 2√2a − 8zγ̄ (+8oγ̄) ∈ O because 8z ∈ O.
- **Lemma P′(iii)–(iv).** Consistent with my exact twist test from N6 (residual ≤ λ^{−p/2} up to p = 1901 for e = 2).
- For e = 2, ζ_A ∈ {b, a} according to k mod 2.
- [P] is justified for (I), P, P′(i), and P′(iii)–(iv) as O-statements.

**(3) Composite weight.** The arithmetic holds:
- ω ≤ p·ln ε/ln(2p−1) ≈ 132.5 at p = 1165;
- loss ≤ 11.38%;
- 2.3344e-3·(1 − 0.1138) ≥ 2.06e-3 (Lean).

**Self-correction #2:** my N6-F5 bound 4/(2p−1) silently assumed ω(h_p) ≤ 2. N7's correction is right.

**(4) Dropping W/W⁺.** This is legitimate: W/W⁺ removed nothing.
- The inventory remains complete, but only because (b) is a catch-all: "all β at levels ≤ L* outside item 1". Completeness is therefore true by construction; the substance is the closed list in item 1.
- See F6 for a set the parenthetical descriptions of (a)/(b)/(b′) miss.

**(5) Gap (a) and the sup-norm barrier.** The reduction is fine [P mod Prop X′], with three provisos:
- several inputs are only [N]: the 2p multiplicity, the ε-symmetry, and the class counts for j > 14;
- the Lemma P′ machinery covers only the (γ)/(γ̄) lines (F6);
- the budget needs splitting (F3).

The barrier arithmetic is right:
- 6·ln(Λ/μ*)/ln λ = 0.0879 with Λ = 1.9656;
- μ*³λ^{−1/2}/Λ = 1.48100 (Lean).

But "a sup-norm bound provably fails" overstates the result (F9).

## (6) The mixed-class conflict, resolved: the two checks used different class sets
| | N5 referee (mine) | N7 f_mixed |
|---|---|---|
| level | e·h_p with e = 7, 457; **h_p prime** (p = 19) | d = h_p **composite** (p = 11: 23·353; p = 13: 79·599) |
| class | **family point** mod h_p × unit mod e (all 48 units mod 7; 12 samples mod 457) | **any** iso-or-0 point mod q1 × random unit mod q2 (and the reverse) |
| quantity | per-point \|Ẑ/Z₀\| ≤ 4.4e-12 / 6e-18 | **aggregate** absolute majorant: count × \|κ\| × E\|Ẑ/Z\|, relative to 4p·n_d·Re w |

- **Both results are right for their own sets.**
  - Family × unit at e·h_p is negligible: at most 48·4p points of size ≤ 4.4e-12.
  - Generic mixed classes at composite h_p are an index-loss-type aggregate. They are heavy-tailed and not negligible at small p.
- **Scope correction to my N5 report.** "Mixed classes are negligible" applies only to family × unit at e·h_p, not to generic mixed classes.
- **My independent replicate** (p = 11, seed 777, 3000 samples per class):
  - S_A/fam = **0.021 ± 0.005** (max point 5.6e-6), against N7's 0.149 ± 0.098 (max point 1.4e-4);
  - S_B/fam = 0.027 ± 0.006, against N7's 0.022 ± 0.006.
  - K = 16 against K = 32 truncation on 40 points per class agrees to 3e-4 relative, so this is not truncation noise.
  - The outliers are not the β ≡ 0 mod q_i (proper-divisor-level) points.
- **Interpretation.** N7's 15% comes from one rare near-slow sample. The p = 11 aggregate is plausibly about 2–15%, and only exhaustive orbit enumeration would settle it. p = 13 (≈ 0.3%) supports the 0.892^m decay heuristic. Neither figure is a proof.

## Findings
- **N7-F1 (clarity).** State B16(m) = Σ C_i R_i^m in its two-term form (≈ 706·1.63541^m + 2.27e5·0.95^m) as the bound behind m1 = 51 and p16 = 339. The 2.273e5·1.6355^m form gives only m ≥ 83 and p ≥ 498. Also write out the monotonicity step after the finite scans.
- **N7-F2 (inherited [CA]).** The dom certificates rely on J3 rig_spec for spectral containment between the contours. The linear algebra is float with γ_n bounds. Say so in the ledger.
- **N7-F3 (budget bookkeeping, required).** Theorem 16 consumes 0.01·F_m and the trivial floor consumes δ·F_m, so:
  - Ω♯ must become Σ|Lin♯| ≤ (1 − 2δ − 0.01)·F_m;
  - L* should be recomputed with 2.06e-3;
  - A∞'s θ < 0.9 leaves only 0.09 − 2δ for (b) + (b′). State the split.
- **N7-F4 (OK).** Identity (I), Lemma P and Lemma P′ are [P]. Lean checks identity (I).
- **N7-F5 (OK; referee self-correction).** The composite loss is 11.4%, so F_m ≥ 2.06e-3·p|Z₈|²/h_p.
- **N7-F6 (inventory/reduction gap, required).** At composite h_p (ω ≥ 2) there are 2^ω − 2 further *fully isotropic* lines, for ideals such as 𝔮₁𝔮̄₂.
  - These lines carry the full weight n_d.
  - Their generator is not the Binet γ, so identity (I) and Lemma P′ do not apply.
  - They are not "iso-or-0 × unit", so they are not in (b′).
  - A∞ ("all iso x at h_p") silently includes them, but the P′ reduction does not cover them.
  - [N] at p = 11 (`ref_crossline`): cross-line ratios are **0.0014 ± 0.0003** and **0.0009 ± 0.0001** of the family term, small but not zero. On the γ lines themselves the sampler hit family points (max 3.956e-4 = c*).
  - Fix: route cross lines (and prime-power analogues) explicitly to (b′), and restrict A∞ to the (γ)/(γ̄) lines.
  - All N7 numerics for (a) are at prime h_p (p = 29, 47), where cross lines do not exist.
- **N7-F7 (OK, with caveat).** Dropping W/W⁺ is legitimate. Inventory completeness holds by the catch-all definition of (b), so N7b's scope note must include the F6 cross lines.
- **N7-F8 (labels).** These are all [N] and should be labeled so:
  - the λ-orbit multiplicity 2p per line;
  - the ε-symmetry α ~ εα ~ −α;
  - the shell class counts beyond j = 14;
  - "(a) holds with ~10× margin".
  
  The heavy tails (max/mean up to 37; the j = 12 outlier) mean the 9.5% total has no error bar.
- **N7-F9 (exaggeration).** §4.4 should read "the worst-case (joint-spectral-radius) majorant diverges [P]", not "a sup-norm bound provably fails". Per-class cores are specific sequences, and their realised values decay (~N^{−1.3} [N]). Only that particular majorant is ruled out.
- **N7-F10 (mixed MC).** Report the p = 11 class-A figure as heavy-tailed (two seeds: 0.149 ± 0.098 and 0.021 ± 0.005). Do not quote 15% ± 10% as an estimate.
- **N7-F11 (scope fix, mine).** My N5 "≤ 4.4e-12" concerns family × unit at e·h_p (h_p prime) only. See §(6).

## How close is this?
The following are now closed: (±2,16), the pattern lemma, composite weights, and all explicit thresholds below 1165. What remains:
- (a): A∞ on the γ lines;
- (b) and (b′), now including the cross lines;
- Prop X/X′ [P-sketch];
- J3/Line F [CA] inputs.

Numerically every open piece is small: (a) ≈ 9.5% (mostly the positive near-0 family), and (b′) is ≤ a few % by p ≈ 13 and decaying. But (a) and (b)/(b′) are genuine index-loss problems. This is a solid conditional result, still roughly two hard lemmas away from unconditional.

## Most promising route to Lemma A∞
I recommend a **restricted Theorem C on depth shells, done on the Fourier side with a positive kernel.**
1. **Core twists as an exponential-sum problem.** By Lemma P′(iv), the core twists of class e are d_j = emb₁(λ^jζ_e) mod 1, with ζ_e ∈ (1/(4√2))O lying in the hyperbolic shell N ≤ |N(e)| < 2N (mod units). Expand ‖Q_e‖²_HS as a trigonometric polynomial in (d_j). Frequency vectors n give phases e(Σ_j n_j emb₁(λ^jζ)) = e(⟨ζ, w_n⟩), where w_n = Σ n_jλ^j ∈ O.
2. **Majorize the shell with a nonnegative kernel.** Replace the shell indicator by a Beurling–Selberg/Fejér majorant whose Fourier transform is nonnegative and supported in a ball of radius ~1/width. The shell sum of HS² is then ≤ Σ_n (kernel weight ≥ 0) × [near-collisions w_n ∈ dual lattice + ball]. This is exactly Theorem C's collision automaton, with an "η-near-collision" tolerance in place of exact collisions. Positivity replaces the missing T-invariance; this is the box-restricted Bowen step.
3. **Show near-collisions grow slowly.** The near-collision growth rate r₂(η) → r₂ ≈ 1.053 as η → 0. One needs h₂ = r₂(η) < 1.481, a margin of about 1.4. Choose the core sub-window so that the width gives η ≤ λ^{−c}. The few steps at the core ends, where the deviation is small, are absorbed by window rank-one collapse.
4. **Add a finite certificate and the deep points.**
   - Certify [CA] the finitely many classes with N ≤ N₀ (near-0 family first, as n_cert did for w*; one-sided, so Re ≥ 0 suffices).
   - Apply step 2 to the shells N > N₀.
   - Deep points (A2) are handled by the same estimate with D_p → q, since the shell bound is uniform in N.

The quantity to compute first is r₂(η) from Theorem C's automaton with tolerance: one transfer-matrix spectral radius.

## Lean (`lean/LineN7Arith.lean`, builds clean)
- `identity_I`
- `loss_1165`, `fm206`
- `r16_sq`, `r16_rate`, `contour`
- `thr1481` (≥ 1.4808 with Λ ≤ 1.9657)
- `supexp`
