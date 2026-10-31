# Referee report — Line N (/workspace/bgs-lineN)

Referee: Grok Bot · 2026-10-31 (Asia/Yekaterinburg, UTC+5) · read-only on repo/clones, nothing pushed.

## Verdict: **READY-after-fixes (N-F1 … N-F10)**

No mathematical error that invalidates a headline claim. One wrong number (N4 index 32 → **4**), one
mis-stated hypothesis (N1.2(b) q ≥ τ²), a hypothesis of N3 that must be sourced to a proved registry item
rather than a "standing input", missing credit to L2 Prop S, a wrong file in logs/, and wording fixes.
N3 is **correct** and its main corollary (K2′'s conclusion is unconditionally true for all large p; L §6 target false)
**stands**. It contradicts no claim registered as proved; it upgrades two [H] caveats in PR #64 (§6 below).

## Independent numerics (code/ref_n.py → logs/ref_n.log; author reruns logs/rerun_*.log)

| Check | Result |
|---|---|
| ε_F = η/(3A_k) from Line L final_constants.jsonl | 8V: 10^−12.507, c_W 10^−25.615 (= L); 8E −10.165; 16V −10.964; 16E −10.118 ✔ |
| c_N = ε⁹/17.31 | 8V 10^−113.798; crossover with Weil p ≥ 10^264.55 ✔; (2,3) c 10^−75.81; isotropic (CP) 10^−101.51 ✔ |
| 4·3^{4/3} | 17.30699 < 17.31 ✔ (n2's C_F = 17.3087 also < 17.31) |
| J₃ constant across the whole W⁺ range (q from c_W p² to c_N p^{7/3}, τ ∈ {p,3p}, p 10^264.6…10^400) | ratio J₃-bound/τ^{11/3} = 17.30699 everywhere ✔ — **but q < τ² throughout p < 10^{344}** (see N-F4) |
| θ_F | 8V 5.3901e-6, 8E 6.0057e-6 ✔ |
| Fix(T^p) and conductor-h_p points, brute force p=3,5,7 | #Fix = 4h_p² (196, 6724, 228484); cond. points h_p² all fixed; **index 4** (not 32) |
| J₂, J₃, max|S|, isotropic sum on 17 real levels q \| h_{3p}, q ≤ 4700 (direct count/matrix, no FFT) | J₂ = 2τ²−τ exactly in 17/17; J₃ ≤ bound (ratio 0.015–0.07); max|S| ≤ min(b22,b23,b33); iso ≤ min(CP, Weil); all ok, values identical to n3_check |
| Author scripts n2_constants, n3_check, n6_theta rerun | byte-identical to saved logs ✔ |
| Lean (lean/LineNArith.lean, logs/lean.log, toolchain v4.33.1, `decide +kernel`, no native_decide) | |det(S^p−1)| = 4h_p² for p=3,5,7; 32/8=4; 3⁴ < (17.31/4)³; J₂ equalities — compiles clean |

n5 (toy slow rates) and n1/n4 factor runs were not rerun (cost); their logs are internally consistent (0 congruence failures).

## Item-by-item

**(1) Reduction to binomial orbit sums over H = ⟨λ mod q⟩ [P] — confirmed.** The kick phase enters only through
β ↦ γβ in the Fourier expansion of f_k; the frozen average is I_k + Σ c_γ S(γβ) with S a sum over H of
e_q(Tr-type binomial). No residual phase survives. Proved.

**(2) ε_F = 10^−12.51 independent of m [P] — confirmed, checked against L Theorem W.** In L's proof the per-level
bound is C′((1−δ/2)target)^m; the τ(h_m) = e^{O(m/log m)} conductor count is absorbed by (1−δ/2)^m
(δ/2 ≈ 0.004 for 8V) for m ≥ m₁, and the per-level threshold ε_F = η/(3A_k) never sees the count. m₁ is
effective but **not computed** — N must say so wherever "for all large m" appears (N-F7).

**(3) Theorem W⁺ — correct with fixes.**
- OSV moment inequality |S|^{2kl} ≤ q²τ^{2kl−2k−2l}J_kJ_l: re-derivation correct; J₂ ≤ 2τ²−τ proof correct (−1 ∉ H, τ odd).
- J₃: degenerate ≤ 12τ³ ✔; curve (X^s+Y^s+a)(X^s+Y^s+bX^sY^s) − X^sY^s, abs. irreducible for ab(ab−1)≠0, gcd(s,q)=1
  (OSV Lemma 4.3) ✔ — the ab=1 / a=0 / b=0 cases are exactly those counted as degenerate ✔. OSV Cor 2.9 independence
  hypothesis is not needed in the diagonal form used ✔.
- Voloch count 4d^{4/3}p^{2/3}+3p: hypothesis d > p^{1/4} holds (d = 3(q−1)/τ, q ≥ τ^{4/3}). Original not retrievable
  (matwbn/impan errors); keep label **[P-cite via OSV]**. logs/voloch.pdf is an unrelated paper (N-F5).
- **N-F4:** N1.2(b) says "for q ≥ τ² and τ ≥ 10²⁵ this gives J₃ ≤ 17.31τ^{11/3}". In the range where W⁺ beats Weil
  (10^{264.5} ≤ p < 10^{344}) one has q ≤ c_N p^{7/3} < τ², so the stated hypothesis fails there. The constant is
  nevertheless valid: the 3qτ²/(q−1)² term is ≤ 3τ^{2/3}·τ^{4/3}/q, negligible as soon as q ≥ τ^{4/3}·τ^{δ}; replace by
  "q ≥ c_W p² and τ ≥ 10^{45}" (or q ≥ τ^{4/3+}) — verified numerically over the whole range.
- Cochrane–Pinner Thm 1.1 (any subgroup, λ = 2/3^{1/4}) used correctly for the isotropic range 10^{−101.5}p³ ✔.
- Minor: §1 table says "J₂ ≤ 2τ², J₃ ≤ 17.32τ^{11/3}" vs body 2τ²−τ, 17.31 — harmonise (N-F9).

**(4) Bourgain JAMS 18 (2005) Cor 1.21 + BGK.** Statement as quoted is accurate (complete sum s=1..p−1, all a_i ≠ 0,
ord θ_i and ord θ_iθ_j^{−1} > p^ε, δ = δ(ε)). Bourgain §5(1) gives δ_r > exp(−C₃ r(ε^{−C₂}+log r)): the bound is
**effective in form, constants not computed**. So "not explicit" is right and "ineffective" is wrong
(N-F6; amend lineK_harg_removal.md:249 and K2/REPORT_K2_v2.md:20). Qualitative BGK extension: [P-cite], fine.

**(5) Theorem N3 — scrutinised; correct, with sourcing fixes.**
- Logic: for β=1, Tr(λⁿ)/c is tiny for |n| ≤ log_λc − t, f_k ≥ 0, f_k(0) = ‖L₀^k‖²_HS ≥ ρ^{2k}, so the average is
  ≥ (2(log_λ c − t − k)/r)μ^{2k} > threshold iff log_λ c ≥ θ_F r/2 + t + k. Sound. log_λ c ≤ r/2 always (c² | N(λ^r−1)),
  so the theorem is non-vacuous only because θ_F ≈ 5·10⁻⁶ ≪ 1; for c = h_p, r = p, λ^p−1 = 2h_pε^p (Lean lam_pow_eq,
  Line M) gives log_λ h_p = p/2 − O(1) ✔.
- **N-F2 (dependence):** step 4 rests on "Line F |Z_ρ| ≥ (½−o(1))|μ*|^m standing input" + Lidskii, and then "take F to be the
  family containing it" — but θ_F is computed for a *fixed* F (8V/8E). Replace by the proved per-family spectral-radius
  bound of TRACE-198 [CA] (ρ(L₀^F) ≥ μ* for the family in question); then N3 is [P] with no standing input and the
  family-switching sentence goes. State also the needed r > 2(N + k) (min(r,·) truncation).
- **N-F3 (t_F):** "O(k), explicit but not computed". Rough estimate from A_k and the λ^{|n|+k} Lipschitz factor:
  t_F ≈ 25 + k ≈ 40, so c = h_p is covered for p ≳ 110 [H, estimate]; say so, or compute it.
- **N-F1 (credit):** N3 is the extension of L2 Prop S (TRACE-258, proved, prime/inherited levels) to composite c, chiefly h_p,
  with an explicit θ. Cite it.
- Compatibility: L2 Prop S (same mechanism) ✔; Theorem U ✔ (U is a conditional bound for β-weighted sums, N3 only shows the
  unweighted "no slow orbit" target false); Lemma E (TRACE-268, excursion ≤ 264ε²q² for β≠0) ✔ — not contradicted;
  H_mean (TRACE-256, incl. composite levels) unaffected since it is a mean over β. TRACE-245 (Theorem W) is unaffected
  (h_p is beyond its range). **No proved claim is contradicted.**
- Toy illustration (β=1 rates 1.43–1.71 > 1.28359 threshold, random β 0.81–1.18) consistent; [N] label correct.

**(6) N4 index — wrong number (N-F8).** Fix(T^p) = (4√2 h_pε^p)⁻¹O/O^∨ has 4h_p² points ✔, but the
conductor-h_p points are ((1/h_p)O + O^∨)/O^∨ with h_p² points: index **4**, not 32. The error is forgetting
[O^∨ : O] = N(2√2) = 8 (32/8 = 4). Brute-forced p = 3,5,7 and Lean-checked. The correction to K2 §3 should use 4; n6_theta.py's
"N(4√2) = 32" printout is true but is not the index. Downstream statements of N4 using the index should be rechecked.

## Fix list
- **N-F1** Credit L2 Prop S (TRACE-258); present N3 as its composite-c / h_p extension with explicit θ.
- **N-F2** N3 step 4: replace the Line F |Z_ρ| standing input + family switch by TRACE-198 [CA] per family; add r > 2(N+k).
- **N-F3** Give t_F (or an explicit bound; estimate ≈ 40, p ≳ 110) and mark m₀ for Corollary N3′ effective-not-computed.
- **N-F4** N1.2(b)/N1.3: hypothesis q ≥ τ² → q ≥ c_W p², τ ≥ 10^{45} (constant 17.31 holds; verified).
- **N-F5** logs/voloch.pdf is an unrelated paper (certificateless signatures) — remove/relabel; Voloch stays [P-cite via OSV].
- **N-F6** "ineffective" → "effective, constants not computed" (N §4; lineK_harg_removal.md:249; REPORT_K2_v2.md:20).
- **N-F7** State m₁ (Theorem W) as effective-not-computed wherever "all large m" is used in N0/N2/§5.
- **N-F8** N4: index 4 (not 32); fix K2 §3 correction accordingly.
- **N-F9** Harmonise table vs body (2τ²−τ; 17.31).
- **N-F10** Note N1′ supersedes REPORT_K2_v2.md:134–137 ("explicit versions do not help for the binomial sums").

## Suggested registry states
| Item | State |
|---|---|
| N0 reduction / ε_F independent of m | proved |
| N1.1 (J₂), N1.2 (J₃, after N-F4), N1.3, Theorem W⁺ | proved (P + P-cite: OSV Lemma 4.3, Voloch via OSV, Cochrane–Pinner) |
| N1′ Bourgain/BGK qualitative extension | proved-cite, "not explicit" |
| Composite c ≤ p^C via Bourgain finite-ring | open [H] |
| N3 + Corollary N3′ (after N-F2/F3) | proved (effective, p₀ not computed) |
| N4 index-4 identification | proved; size estimates [H] |
| N5 toy rates | numerical |

## PR #64 (branch line-L-op) / merged claims in light of N3
- **TRACE-246 (K2′) CAVEAT** — amend: replace "That this covers all or most m is [H]" with "By N3 [P], for every p ≥ p₀
  (effective, not computed) the conductor c = h_p in K2′'s open set carries the slow orbit β = 1; hence K2′'s conclusion
  holds unconditionally and K2′ is never a refutation route."
- **TRACE-258 (Prop S)** — same [H] sentence is superseded by N3; add cross-reference.
- **TRACE-247 (open)** and REPORT_L_v2 §6 target ("exclude slow λ-orbits at c ∈ (c_W p², L_m)") — mark the unweighted
  target **false** (for c ≥ λ^{θr/2+t}) and restate as a β-weighted target. §6 was labelled [assessment], so this is a
  correction of a target, not of a proved claim.
- TRACE-245, 256, 266, 268: no change needed. Stale "ineffective" wording (N-F6) should be fixed in the same PR.

## Cheap Lean targets
Done (lean/LineNArith.lean): Fix(T^p) counts p=3,5,7; 32/8 = 4; 4·3^{4/3} < 17.31; J₂ equalities.
Next: general `|det(S^p−1)| = 4h_p²` via lam_pow_eq; [O^∨:O]=8 as a lattice index; θ_F rational bound
((1−δ/2)·1.28359/1.91547)^{30} < 5.4·10⁻⁶; J₂ ≤ 2τ²−τ for a finite cyclic subgroup with −1 ∉ H (pure algebra, feasible);
log_λ h_p ≥ p/2 − 1 from h_p ≥ ε^p/2.
