# Lines M and N: conductor structure along m = 3p, the explicit range beyond Weil, and scarred conductors

**Status.** Each result below is labelled:
* paper proofs [P], proofs from cited theorems [P-cite];
* computer-assisted inputs [CA] (only through the Line F certificate BGS-TRACE-198/199 and the Line L constants);
* kernel-checked finite statements in Lean (§8; `decide`/`norm_num`, no `native_decide`, no `sorry`);
* floating-point numerics [N], heuristics [H], [constant arithmetic] and opinions on strategy [assessment]. **[N], [H] and [assessment]
  items are notes only (§7); they are not registered as claims.**

**Independent referee audits.**
* Line M: `computations/verification/lineM/referee/REPORT.md`, **READY after fixes M-F1–M-F12**. The author applied them in
  `computations/verification/lineM/REPORT_M_v2.md` (errata §10, claims table §11); v1 `REPORT_M.md` is kept.
* Line N: `computations/verification/lineN/referee/REPORT.md`, **READY after fixes N-F1–N-F10**. The fixes were applied at integration
  as `computations/verification/lineN/REPORT_N_v2.md` (errata §12, with integration notes I-1–I-4); the author's `REPORT_N.md` is kept
  unchanged (sha256 b740bc39…, listed in `SHA256_N.txt`).

The integration record is `evidence/executions/20261031/lineMN/INTEGRATION.md`.

**Standing inputs.** As in the Line L note (`lineL_op_open_range.md`): BGS-TRACE-197, 225, 226, 227, 238, 241, all proved; of Theorem J3
(BGS-TRACE-231, conditional) only the notation and its proved parts are used. Theorem W+ (BGS-TRACE-280) and the qualitative extension
(BGS-TRACE-281) are relative to the standing inputs of Theorem W (BGS-TRACE-245), with m ≥ m₁ effective, not computed. H♮
(BGS-TRACE-232, open) appears in M2 only as the form of a statement, and the Line F per-family bound is the proved [CA] claim
BGS-TRACE-198. No proved claim of this note depends on a non-proved claim, except on BGS-TRACE-206 through its frozen definition
(gate: `computations/verification/lineN/integration_checks/proved_deps_gate_MN.py`, strict for 244..285). **No explicit p₀ is claimed
anywhere: every threshold (m₁, p₀(C), t_F, p₀ of N3) is effective, not computed.**

**Registered claims** (`record/claims.json`):

| § | claim | content | label | state |
|---|---|---|---|---|
| §1 | BGS-TRACE-269 | M1: gcd(h_m, h_n) = h_gcd(m,n) (odd m, n); open conductors at distinct m = 3p disjoint (only 7 shared) | [P] + Lean | proved |
| §1 | BGS-TRACE-270 | M2: positive-weight averaged H♮ ⇒ H♮ with δ/2 | [P] | proved |
| §2 | BGS-TRACE-271 | M3: m = 3p ≥ 495, (±2,8): h_p included and open; Prop K2 floor ≥ c·1.13287^m, beats D7 by > 1.11238^m (no-go for positivity) | [P on CA] | proved |
| §2 | BGS-TRACE-272 | M4a: the four P* families are disjoint (odd m) | [P] + Lean | proved |
| §2 | BGS-TRACE-273 | M4b: (±2,8) rule includes every d \| h, 1 < d ≤ √h, odd m ≥ 15 | [P on CA] | proved |
| §2 | BGS-TRACE-274 | M4c: (±2,16) rule degenerates for m ≳ 85 | [N] | **open** |
| §2 | BGS-TRACE-275 | M5: squares offset a cross deficit X only if d ≳ 4\|Z\|²/X; Prop K2 sharp within the quadratic relaxation | [P] | proved |
| §2 | BGS-TRACE-276 | M6: ±ρ pairing law at all levels (conditional on C1–C4) | [H] | **open** |
| §1 | BGS-TRACE-277 | M7a: ord_c λ \| 3p; λ^p = 1 + 2h_pε^p; p = 2log_λ h_p + O(1); M7b literature as annotation | [P] + Lean | proved |
| §3 | BGS-TRACE-278 | N0: reduction to binomial sums over ⟨λ mod q⟩; budget ε_F = η_F/(3A_k) independent of m | [P] | proved |
| §3 | BGS-TRACE-279 | N1.1–N1.3: moment inequality, J₂ ≤ 2τ² − τ, J₃ ≤ 17.31τ^{11/3} (q ≥ c_W p², τ ≥ 10⁴⁵), binomial and isotropic bounds | [P + P-cite] | proved |
| §3 | BGS-TRACE-280 | Theorem W⁺: q ≤ max(c_W p², c_N p^{7/3}), c_N = 10^{−113.80}; beyond Weil only for p ≥ 10^{264.5} | [P + P-cite + CA] | proved |
| §4 | BGS-TRACE-281 | N2: prime q, 7q ≤ p^C via Bourgain (JAMS 2005); p₀(C) effective, constants not computed | [P-cite] | proved |
| §4 | BGS-TRACE-282 | composite c ≤ p^C via Bourgain's finite-ring theorem | [H] | **open** |
| §5 | BGS-TRACE-283 | Theorem N3: scarred conductors carry the slow β = 1 (F = (±2,8)V, θ_F = 5.39·10⁻⁶, r > 2(N + k)) | [P on CA] + Lean | proved |
| §5 | BGS-TRACE-284 | Corollary N3′: K2′'s conclusion holds without assuming frozen R′ for p ≥ p₀; the unweighted slow-orbit target is false | [P on CA] | proved |
| §6 | BGS-TRACE-285 | N4: conductor-h_p points are a subgroup of index 4 in Fix(T^p) | [P] + Lean | proved |

**Changed earlier claims (annotations; no state changes):**
* **BGS-TRACE-246 (K2′, proved)** and **BGS-TRACE-258 (Prop S, proved):** the [H] caveat "that this covers all or most m" is replaced by
  the proved statement of Theorem N3 (BGS-TRACE-283), which is added as a dependency of both. For every p ≥ p₀ (effective, not computed)
  the conductor c = h_p, which lies in K2′'s open set, carries the slow orbit β = 1. So K2′'s conclusion holds without assuming frozen R′,
  and K2′ is never a refutation route for such m (Corollary N3′, BGS-TRACE-284). To keep the graph acyclic, N3 credits Prop S in its
  text only and does not depend on 246, 258 or M3.
* **BGS-TRACE-247 (Conjecture C1, open) and the Line L §6 target.** The unweighted target "exclude slow λ-orbits at conductors
  c ∈ (c_W p², L_m)" (REPORT_L_v2 §6) is **false** on c ≥ λ^{θr/2+t} (by N3). It is restated as a **β-weighted** target: bound the
  β-weighted mean of the twisted orbit sums at the scarred conductors, h_p first. Examples are H_mean (BGS-TRACE-256) and the
  periodic-orbit pressure form of N4 ([H]). C1 itself is unaffected.
* **BGS-TRACE-238 (Prop K2, proved):** M5 (BGS-TRACE-275) is recorded as its refinement (sharp within the quadratic relaxation), and M3
  as its consequence at h_p.
* **BGS-TRACE-206 (frozen R′) stays OPEN.** Nothing here refutes it.
* Wording (N-F6): the Line K "ineffective" for the Bourgain extension now reads **"effective, constants not computed"**. The places are
  `lineK_harg_removal.md` (the K2 paragraph) and `computations/verification/lineK/K2/REPORT_K2_v2.md` (§9 errata, lines 20 and 132).

## 1. Arithmetic of h_m along m = 3p (BGS-TRACE-269, 270, 277)

Notation: ε = 1 + √2 and λ = ε² = 3 + 2√2. For odd m, ε^{2m} − 1 = 2h_mε^m, so h_3 = 7, h_5 = 41, h_7 = 239, …

**M1 [P] (BGS-TRACE-269).**
- By the r(q) lemma (BGS-TRACE-230), q | h_m ⇔ r(q) | m.
- Lifting the exponent (q odd, unramified) gives v_q(h_m) = v_q(h_r) + v_q(m/r), and 2 ∤ h_m.
- Hence gcd(h_m, h_n) = h_gcd(m,n).
- On m = 3p every prime q ≠ 7 dividing h_m has r(q) ∈ {p, 3p}. So open conductors at distinct m are disjoint, and only 7 is shared
  (49 | h_21 is the exception at p = 7).

**M2 [P] (BGS-TRACE-270).** For c_m ≥ 0 with Σc_m D̃7_m = ∞: if Σ_{m≤M} c_m(Õ_m + (1−δ)D̃7_m) ≥ 0 for infinitely many M, then
Õ_m ≥ −(1−δ/2)D̃7_m for infinitely many m ∈ S⁺. So averaged H♮ is never weaker than H♮.

**M7a [P] (BGS-TRACE-277).**
- ord_c λ | 3p for c | h_{3p}.
- λ^p = 1 + 2h_pε^p (Lean `lam_pow_eq`), so λ^p ≡ 1 mod 2h_p and p = 2log_λ h_p + 2log_λ 2 + o(1).
- M7b (annotation) concerns the unkicked cat map:
  - Kurlberg–Rudnick, *Commun. Math. Phys.* **222** (2001) 201–227, DOI 10.1007/s002200100501. The volume was checked against the
    publisher's page at integration; the referee's "221" is a slip.
  - Bourgain (LNM 1910), BGK (JLMS 2006) and Bourgain (JAMS 2005) cover prime q ≤ p^C only (BGS-TRACE-281).
  - Faure–Nonnenmacher–De Bièvre (CMP 239, 2003): h_p is a minimal-period modulus (an analogy only).

## 2. The frozen inclusion rule and positivity (BGS-TRACE-271..276)

**M4a [P] (BGS-TRACE-272).**
- The congruences force gcd(h/d, h/d′) | 3, and 3 ∤ h_m (Lean `three_not_dvd_nsw`).
- So (h/d)(h/d′) | h (Lean `coprime_core`), which gives d = d′ = √h and then h = 1, a contradiction.
- Exact enumeration for m = 5…19 agrees.

**M4b [P on Line F [CA]] (BGS-TRACE-273).**
- Line F F3 gives |Z_ρ| ≥ ½(1 − λ^{−m})(μ_lo^m − 3012.4). With it, |Z_ρ|² ≥ 4mh_m for odd m ≥ 15 (checked to 20001, monotone beyond).
- So every d | h with 1 < d ≤ √h is included for (±2,8). **M4c (open, BGS-TRACE-274):** for (±2,16) only float evidence exists.

**M5 [P] (BGS-TRACE-275).**
- Dev_d = 2Re(conj Z_ρ·S)/d + Σ|X_ν|².
- With Cauchy–Schwarz, squares offset a cross deficit X only if d ≳ 4|Z_ρ|²/X.
- The minimum over S is Prop K2's per-level bound −n_d|Z_ρ|²/d². This is sharp within the quadratic relaxation.

**M3 [P on Line F [CA]] (BGS-TRACE-271).**
- Scope: m = 3p ≥ 495, ρ = (±2,8).
- h_p is included (M1, M4b) and open (K2′ definition).
- Its Prop K2 floor is ≥ c·(μ_lo²/λ^{2/3})^m ≥ c·1.13287^m, more than 1.11238^m times the D7 demand. The report's 1.13288 and 1.11239
  are rounded to nearest.
- This is a no-go for positivity methods, not a refutation.

**M6 (open, BGS-TRACE-276).** The ±ρ pairing law is [H], conditional on C1–C4. Its closure condition is C1–C3 for (±2,8) at squarefree
levels.

## 3. Line N: reduction and Theorem W⁺ (BGS-TRACE-278..280)

**N0 [P] (BGS-TRACE-278).**
- The orbit average at a prime conductor is I_k + Σc_γS(γβ), where S is a binomial sum over H = ⟨λ mod q⟩. No quadratic phase survives.
- The per-level threshold is ε_F = η_F/(3A_k) = 10^{−12.51} for (±2,8)V. It does not depend on m, for m ≥ m₁ (effective, not computed).

**N1.1–N1.3 [P + P-cite] (BGS-TRACE-279).**
- The moment inequality: |S|^{2kl} ≤ q²τ^{2kl−2k−2l}J_kJ_l.
- J₂ ≤ 2τ² − τ.
- J₃ ≤ 17.31τ^{11/3} for q ≥ c_W p², τ ≥ 10⁴⁵ (N-F4). This uses OSV Lemma 4.3 (absolute irreducibility) and Voloch's point count, cited
  via OSV, Math. Proc. Camb. Lemma 2.1.
- Isotropic sums: Cochrane–Pinner Thm 1.1, constant 2/3^{1/4} = 1.519671…, range (1/3)q^{1/3} < τ ≤ q^{1/2} (integration note I-1).

**Theorem W⁺ (BGS-TRACE-280).**
- Under the standing inputs of Theorem W, Theorem W holds for q ≤ max(c_W p², c_N p^{7/3}), with c_N = 10^{−113.80}.
- The part beyond Weil is non-empty only for p ≥ 10^{264.5}, where τ ≥ p ≥ 10⁴⁵ and q ≥ c_W p².

## 4. Line N: qualitative range (BGS-TRACE-281, 282)

**N2 [P-cite] (BGS-TRACE-281).**
- Bourgain, JAMS 18 (2005), Theorem 1 / Corollary (1.21): non-isotropic sums use the complete-sum form with both a_i ≠ 0; isotropic
  sums use r = 1.
- So Theorem W holds for prime q, 7q ≤ p^C and p ≥ p₀(C) = ε_F^{−1/δ(C)}. **p₀(C) is effective, constants not computed.**

**Composite c ≤ p^C (open [H], BGS-TRACE-282).** Bourgain's finite-ring theorem (J. Anal. Math. 101, 2007) plausibly applies, but it was
not read. Its closure condition is to verify its hypotheses for R = O/c.

## 5. Line N: scarred conductors (BGS-TRACE-283, 284)

**Theorem N3 [P on BGS-TRACE-198 [CA]] (BGS-TRACE-283).** This is the composite-conductor extension of L2 Prop S (BGS-TRACE-258, credited).
- F = (±2,8)V, k = 15, μ = 1.9154712 (certified per family, N-F2), θ_F = ((1−δ_F/2)·1.28359/μ)^{30} = 5.39·10⁻⁶.
- Lean `theta8V` checks θ_F < 5.4·10⁻⁶.
- Suppose r = ord_c λ > 2(N + k) with N = log_λ c − t_F, and log_λ c ≥ θ_F(1+κ)r/2 + t_F + k. Then β = 1 is slow at c.
- t_F = O(k) is effective, not computed. The rough estimate ≈ 40, i.e. p ≳ 110, is [H] (N-F3).
- c = h_p qualifies for every p ≥ p₀ (effective, not computed).
- Only F = (±2,8)V is used. The author's (8E) value is dropped because the spectrum of L_E lies in |z| < 1 (I-3).

**Corollary N3′ (BGS-TRACE-284).**
- For m = 3p ∈ S⁺ with p ≥ p₀, c = h_p is open (M3) and slow.
- So K2′'s conclusion holds without assuming frozen R′, and no strengthening of the exponential-sum input can turn K2′ into a refutation.
- **The unweighted target "exclude slow λ-orbits" is false on c ≥ λ^{θr/2+t}; the open-range target must be β-weighted.**

## 6. Line N: the inherited level (BGS-TRACE-285)

**N4 [P].**
- Fix(T^p) has 4h_p² points, and the conductor-h_p points ((1/h_p)O + O^∨)/O^∨ form a subgroup of index **4** (N-F8; not 32).
- With L3 S4 (BGS-TRACE-266), the level-h_p twisted sums are periodic-orbit sums Tr(M_y³) of the cat map.
- Lean `fix3/fix5/fix7` checks |det(S^p − 1)| = 4h_p², and `idx` checks 32/8 = 4.

## 7. Notes only (not registered)

* [N] M4b at m = 11, 13 (float ratios 1.13, 2.22); M4c float data (|Z_16|² < 4mh for m ≤ 29, crossover ≈ 85).
* [N] M3 n_{h_p}/h_p ∈ [0.908, 1] for p ≤ 61; M1 checks to m, n ≤ 601 (referee).
* [assessment] Line M: "every refutation needs a signed equidistribution theorem at h_p"; the signed-weight and Tauberian remarks of M2;
  §3 (m and 3m, 9m) and §7(b)–(e) of REPORT_M_v2 (other fixed conductors, kick averaging, quantum dictionary [P-sketch], norm-one form).
* [assessment] REPORT_M_v2 §6 M7b and §8.3 say "ineffectively" for Bourgain/BGK; after Line N (N-F6) read "effective, constants not computed".
* [H] N3: t_F ≈ 40, p ≳ 110. N4: weighted margin (μ*³/λ)^{1/3} = 1.0644 and the pressure target
  limsup_p (1/p) log Σ_{y∈Fix T^p}|Tr M_y³| < 2.512.
* [N] N5: PARI factorisations of h_p, K_p (p ≤ 173) and the p³-smooth survey (p ≤ 2000); no level is covered by Theorem W or W⁺ at any
  computable m. K2 single-disc toy slow rates at h_p (n5_slow_toy).
* [assessment] REPORT_N_v2 §9–§10 (what remains open; recommended next step).

## 8. Lean

* `formalization/Bgs/LineMArith.lean` (namespace `Bgs.LineM`, referee file): `three_not_dvd_nsw`, `pp_eq`, `strong_div_small`,
  `three_small`, `triple_small`, `nsw_three_mul`, `coprime_core`, `lam_pow_eq`.
* `formalization/Bgs/LineNArith.lean` (namespace `Bgs.LineN`, referee file plus `theta8V`): `fix3`, `fix5`, `fix7`, `idx`, `c17`, `j2a`,
  `theta8V`.
* Both are in `lake build Bgs`; `#print axioms` lists only propext, Classical.choice and Quot.sound, or no axioms at all.
* The Line F certificate, the cited theorems and the analytic arguments are not formalised.
