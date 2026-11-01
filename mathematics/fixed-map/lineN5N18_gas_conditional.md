# Lines N5–N19b: the polymer-gas route to frozen R′ along m = 3p — a conditional reduction (Theorem R♯-mod v4 = v3 after lineN16 edits E1–E7)

**Status: frozen R′ (BGS-TRACE-206) is not refuted.** This note registers the conditional Theorem R♯-mod v4 (= v3 after lineN16 edits E1–E7; BGS-TRACE-299). The
theorem reduces a refutation along m = 3p to explicit open inputs H1–H8 (BGS-TRACE-300..306). The note also registers the proved
ingredients of the reduction and the ingredients that are still pending verification. The labels follow THEOREM_DRAFT_v4 §8
(`computations/verification/lineN_theorem_draft/THEOREM_DRAFT_v4.md`), which is the **canonical statement**; v1–v3 are kept as history.

**Referee status.** The final referee `lineN16` (`computations/verification/lineN16/referee/REPORT.md`) gives THEOREM_DRAFT_v3 GO once
its edits E1–E7 are made. v4 (Line N19b) applies them verbatim, and the owner diff check passed. The repo copy of v4 carries one owner
wording fix in the file references of the p₁ and crossover rows (the note under its header records it).

**How the labels are mapped to registry states.**

| draft label | registry state |
|---|---|
| [P], refereed, all dependencies proved | proved |
| [CA] (arb/interval) or [CA-fp] (IEEE binary64 with derived a-priori rounding bounds, standard model + libm ≤ 1 ulp), refereed | proved |
| [P mod inputs] | conditional (BGS-TRACE-299 only) |
| [H] or OPEN | open |
| [P-sketch], [P] pending a referee, [CA-fp] not yet refereed, [P-arith] with an unrefereed step | verification-pending |
| [N] numerics, superseded or withdrawn items (draft §6) | not registered |

No proved claim depends on a non-proved claim, except on BGS-TRACE-206 through its frozen definition. The gate for this is
`computations/verification/lineN_theorem_draft/integration_checks/proved_deps_gate_Ngas.py`, strict for 244..324.

## Sources
* **Author packets.** These are `computations/verification/lineN5 … lineN19b` (N5, N6, N7, N7b, N8, N8b, N9, N9b, N10, N10b, N11,
  N11b, N12, N12b, N13, N13b, N14, N14b, N15, N15b, N16, N16b, N17b, N18b, N19b). The drafts THEOREM_DRAFT v1–v4 are in
  `computations/verification/lineN_theorem_draft/`.
* **Referee reports.** These are `computations/verification/lineN{5,6,7,8,10,11,11b,12,13,14,15,16}/referee/`. Some reports cover
  several packets:

| referee | packets covered |
|---|---|
| lineN5 | N5 v1 (NOT READY; sign error) |
| lineN6 | N5 v2 (READY), N6 (READY after fixes, conditional) |
| lineN7 | N6 v2, N7 |
| lineN8 | N8, N8b |
| lineN10 | N9, N10 (+ the N7_v2 and N8_v2 fix checks) |
| lineN11 | N11, N9b |
| lineN11b | N11b |
| lineN12 | N12 (+ N11_v2) |
| lineN13 | N12b, N13 |
| lineN14 | N13b, N14b, N14 |
| lineN15 | N15, N17b, THEOREM_DRAFT_v2 (NOT READY; v3 applies its §3 items 1–20) |
| lineN16 | N16, N18b / REPORT_N17b_v2 (R1 robin() fix, applied in N19b), THEOREM_DRAFT_v3 (GO after E1–E7, applied in v4) |

* **Packets without a referee report of their own:** N7b, N10b, N15b and N16b (author notes); N19b and v4 got the owner diff check.
* **Large files.** Files over 5 MiB and the regenerable `.lake` directory are not committed. They are listed with sha256 in
  `evidence/executions/20261101/lineNgas/EXCLUDED.md`.

## v5 update: THEOREM_DRAFT_v5, N20 v2, N21 v2 and referee lineN22 (1 November 2026)
**Canonical statement now:** `computations/verification/lineN_theorem_draft/THEOREM_DRAFT_v5.md` (repo copy with referee lineN22 edits
E1–E8 applied verbatim; author original, the author v4 → v5 diff and the edit diff are next to it). v1–v4 are kept as history.
**Theorem R♯-mod v5 is BGS-TRACE-325 (conditional)**; it supersedes BGS-TRACE-299 (v4, still conditional, ledger "superseded").
Frozen R′ (BGS-TRACE-206) is **not** refuted.

* **Sources.** The N20 v2 and N21 v2 author packets and the referee reports lineN20, lineN21, lineN21b and lineN22 are in
  `evidence/executions/20261101/lineNgas/` (`N20/`, `N21/`, `referee/lineN2*/`), byte-identical to the box originals, with their SHA256
  manifests. Final referee: lineN22, GO after E1–E12 (E1–E8 in the draft, E9–E12 in the registry).
* **Exponent correction (v5 §2).** B_p carries e^{−p(δ + A_bad^KP)}: the KP log → modulus step charges the weighted S₀(a), not a
  [P-sketch, background interplay as for H3]; lineN22 found it correct and necessary.
* **State changes.**
  * BGS-TRACE-302 (H4) open → **proved** [P] + [CA-fp]; dependencies 307, 322, 326, 327, 328; the title parenthetical
    "(open, no working route)" now reads "(met: BGS-TRACE-326)" (ID and statement unchanged).
  * BGS-TRACE-322 verification-pending → **proved a fortiori** via BGS-TRACE-335 (N21 Lemma C, δ_true(G ≤ 15) ≤ 2.2102e-6); the N16
    method named in its title had defects F21-1/F21-3 and is not the proof.
  * BGS-TRACE-323 verification-pending → **proved** [CA-fp] (values recomputed independently by lineN21b).
* **Unchanged states, new ledger/boundary text.** BGS-TRACE-301 (H3) stays **open** (superseded in substance by 332; its a = 5.93e-6
  used the withdrawn tail placeholder). BGS-TRACE-300 (H1) stays open, re-scoped as BGS-TRACE-336. BGS-TRACE-318 stays proved as an
  arithmetic implication in the input δ; its 1386/1390/1399 charge δ only and are not the theorem's p₁.
* **New claims.**
  * Conditional: BGS-TRACE-325 (Theorem R♯-mod v5; inputs H0, H1 = 336, H5–H8 = 303..306; uses 326, 332, 333), BGS-TRACE-332
    (Prop. K: H1-shell ⇒ H3 with a = a(C)), BGS-TRACE-333 (crossover with all rate budgets: first prime 3307 at C ≤ 0.082, fragile;
    1409 at C ≤ 8.8e-4, robust; additive budgets open).
  * Proved: BGS-TRACE-326 (δ_true ≤ 5.0313e-6, all G), 327 (Lemma D^T), 328 (Lemma Q), 329 (Prop. F, lower bound only; the ratio
    statement is [N]), 330 (Lemma J, ε-carries, λ-carry graph, Lemma R), 331 (Thm A, shells j ≤ 14, core functional), 335 (Lemma C).
  * Open: BGS-TRACE-336 (H1 re-scoped: H1-bad joint (A,B) second moment + H1-ali).
  * The proposed claim 334 (N14 digits.py mp.dps = 34 erratum, N21 F21-2) is recorded as erratum ERR-065, not as a claim; no ID 334 is
    registered.
* **Lean.** `formalization/Bgs/LineN20Arith.lean`, `LineN20TailArith.lean` and `LineN21Arith.lean` (namespaces `Bgs.LineN20`,
  `Bgs.LineN20Tail`, `Bgs.LineN21`): the author/referee files verbatim, 54 theorems with `#print axioms`, `norm_num`/`decide +kernel`
  only, no `sorry`, no `native_decide`. Finite arithmetic and finite graph facts only.
* **Gate.** `computations/verification/lineN_theorem_draft/integration_checks/proved_deps_gate_v5.py`, strict for 244..336.

## Registered claims
* **Conditional theorem.** BGS-TRACE-299 (Theorem R♯-mod, v4 statement) is conditional on H0–H8:
  * H0 is the standing package: BGS-TRACE-197/199/207/212/213/228, Prop X′ (BGS-TRACE-324) and n_cert;
  * H2 is met: BGS-TRACE-307;
  * H1, H3, H4, H5, H6, H7* and H8 are open: BGS-TRACE-300, 301, 302, 303, 304, 305 and 306.
  * The subsequence version on 𝒫 = {h_p prime} also needs 𝒫 to be infinite. That is equivalent to ¬R_NSW (BGS-TRACE-210) and is open.
* **Proved.**
  * 307: δ_int^core ≤ 5.14476e-7 [CA-fp].
  * 308: ρ̄ ≤ 0.28 [CA-fp].
  * 309: the coding lemma [P].
  * 310: Re Λ_lo ≥ 6.238e-4 [CA].
  * 311: the adapted norm, and the quadratic step bound for |t| ≤ 1/256 [CA]+[P].
  * 312: the carry reduction (|e| ≤ 14, 633 states) and the torus identity [P].
  * 313: Lemmas P, P′, P′_c and A_c [P].
  * 314: (±2,16) closed for p ≥ 339 [CA]+[P]. It inherits the J3 rig_spec standing (N7-F2).
  * 315: the K_p identity [P].
  * 316: the CRT count n = 7371 [P].
  * 317: the level bookkeeping [P].
  * 318: the gas-vs-Robin crossover [P-arith], an arithmetic implication in the input δ: p ≥ 1386 at the core δ, and **p ≥ 1390 for
    the input value δ = 2.470e-6**, first prime 1399, under the stated idealisation. Whether δ_true(G ≤ 15) ≤ 2.470e-6 holds is
    BGS-TRACE-322 (verification-pending); 318 does not depend on it, but 299 depends on both. It uses N19b's `a_crossover_v3.py` (robin() corrected) and is refereed in lineN16 §2a. 1390 is a lower
    bound for the true p₁.
  * 319: Lemma 1 (sublattice separation) [P], refereed in lineN16 §2b with L1-a/L1-b.
  * 321: A_bad j ≤ 12 [CA-fp], checked in lineN14, lineN15 §1a and lineN16 §1e.
* **Verification-pending.**
  * 320: Lemma 2, c_B = 0.7375, and p = 31 [P-sketch].
  * 322: δ_true(G ≤ 15) ≤ 2.470e-6. The numerics are reproduced (lineN16); the conversion lemma is [P-sketch]. *(Since v5: proved
    a fortiori via BGS-TRACE-335; see the v5 update.)*
  * 323: the step-norm table for |t| > 1/256. The method is refereed, but the values were not recomputed. *(Since v5: proved,
    values recomputed by lineN21b.)*
  * 324: Prop X′ (it has [P-sketch] parts).

## Lean
* **Files.** `formalization/Bgs/LineN{5,6,7,8,10,11,12,13,14,15,16}Arith.lean` are the referee arithmetic files, integrated verbatim inside
  the namespaces `Bgs.LineN*`. They contain 168 theorems, each with `#print axioms`. They use `norm_num` and `decide` only: no
  `sorry` and no `native_decide`.
* **What they check.** Finite arithmetic only, namely the rate comparisons, the KP inequalities, the rounding constants, the K_p
  identities for p = 5..13, and the CRT counts. They do not formalise the analytic arguments.

## Not registered
* **[N] numerics.**
  * Small-p W′ tables (m ≤ 17).
  * The level data at m = 21, 33, 39, and Dev_7.
  * The TW-law estimate "+2.95 at m = 57", which is not an exact W′/m.
  * The carry correction ≤ 2e-9.
  * The NSW primes ≤ 300 (FLINT).
  * The non-h_p Dev numerics.
  * The collision margin of 186×.
  * The (R-mix) majorant runs of N16b §2, and the exact-mode run p = 17, q = 103 (h₁₇ = 103·15607, 2.51e10 points, finished
    1 November 2026): E_M = 0.72637, W0 = 2.08247, E_M/W0 = 0.349, c_coll = −0.227. Like every earlier exact row (p = 11, 13 and
    p = 17, q = 15607; c_coll between −0.58 and −0.40) it has E_M < W0, so it is consistent with the [N] remark "c ≤ 0" in H5; it is
    the c_coll closest to 0 so far, and the N16b sampled estimate for this case (ratio 0.065) was ≈ 5× low. One prime, float, no
    error control; not evidence for (R-mix) uniformly in d or for large p
    ([evidence](../../evidence/executions/20261101/lineNgas/p17_q103_exact/README.md)).
* **Negative results.**
  * The D1 + G*_gas route is dead (θ ∈ [1/16, 1/4]).
  * The 4-fold automaton gives ≥ 5.41151 > 2.611 ([CA] for the author, [CA*] for the referee).
  * The letterwise CP bound diverges.
  * The H-product conversion is vacuous.
  * These are recorded in the packets (N12b, N10b, N14 §2.3, N15 §5) and are not registered, because they mix [N] with [P] and do
    not bound any registered quantity.
* **Superseded and withdrawn items of THEOREM_DRAFT_v3 §6.** These include:
  * Lemma A∞;
  * hypothesis G;
  * c2_mid and 5.14415e-7 / 5.14416e-7;
  * the (1 + Re Λ − δ)^p form;
  * "0.97·ℓ₀/log_λ d";
  * N17b §5(b) "372 = hp-div".
* **Line N5 v1.** Its sign error is superseded by N5 v2. The N5 v2 family-rate statement (rate 1.42785 > T, positive cross part)
  enters only as the threshold T′ = 1.42785 in H7* (BGS-TRACE-305). It is not a separate claim.

## Claim index

| id | state | claim |
|---|---|---|
| BGS-TRACE-299 | conditional | Line N Theorem R#-mod v4 (= v3 after lineN16 edits E1-E7) (conditional): if H0-H8 (BGS-TRACE-300..306 and the standing package) hold at p and B_p >= kappa > 0 for infinitely many primes p >= p_thr, then W'_{3p}/m -> infinity and frozen R' is false along m = 3p (conditional; not a refutation) |
| BGS-TRACE-300 | open | Line N hypothesis H1 (open [H]): collision lemma - lattice-to-collision reduction for shell sums with constant C <= 0.082 at J0 = 12, plus the A_bad tail j > 12 |
| BGS-TRACE-301 | open | Line N hypothesis H3 (open): Kotecky-Preiss polymer weight e^{a\|gamma\|} with a = 5.93e-6 at g0 = 4 (log -> modulus), finite part certified, tail j > 12 = H1 |
| BGS-TRACE-302 | proved | Line N hypothesis H4 (met: BGS-TRACE-326): core -> true conversion of the interaction constant, now = difference-form (pair-minus-product) conversion + the G > 15 true-functional tail |
| BGS-TRACE-303 | open | Line N hypothesis H5 (open): composite h_p - (a) mixed classes (R-mix) E_{mixed,d} F_p <= e^{o(p)} d^c r_2^p with c < 0.387 uniformly in d \| h_p; (b) the 2^omega - 2 cross lines; (c) partially isotropic points; or p in P = {h_p prime} |
| BGS-TRACE-304 | open | Line N hypothesis H6 (open): inputs of Theorem C' - an explicit p0 and squarefreeness of h_p (or conductor-q^a weights) |
| BGS-TRACE-305 | open | Line N hypothesis H7* (open): for included levels d not in {h_p} u {e h_p}, d < L_fl = h_p^{1+o(1)}: \|Lin_d\| <= eps_d \|Z_rho\|^2/h_p with sum eps_d <= kappa0, i.e. cross-correlation growth < T' = 1.42785; needed even for prime h_p |
| BGS-TRACE-306 | open | Line N hypothesis H8 (open): deep wrap-around points of gap (a) at composite h_p - free if per-point weights are not d-amplified, otherwise need c < 1.1718 l0 / ln d (= 0.6647 l0 / log_lambda d) |
| BGS-TRACE-307 | proved | Line N H2 met [CA-fp]: core interaction constant delta_int^core <= 5.14476e-7 (c3_mid, closed F14.1; referee arb 5.1447502e-7) |
| BGS-TRACE-308 | proved | Line N [CA-fp]: rhobar <= 0.28 by an eigen-solver-free residual certificate (N15 b_cp3) |
| BGS-TRACE-309 | proved | Line N11 coding lemma [P]: the isotropic sum at q = h_p is coded by the gas, X_coded = 2[(1 + Lambda)^p e^{p Delta} - 1] - (dense part), and \|1 + X_gas\| >= 2(1 + Re Lambda)^p e^{-p delta} - 1 given the model form |
| BGS-TRACE-310 | proved | Line N [CA]: Re Lambda_lo >= 6.238e-4 (Re Lambda_lo' = 6.234e-4 after charges) |
| BGS-TRACE-311 | proved | Line N13 adapted norm [CA] (cond_H 21.103, Lip_H 167.213, Qtilde 0.45) and quadratic step bound N_H <= 1 + 1.01e-12 + 4260 t^2 for \|t\| <= 1/256 [CA]+[P] |
| BGS-TRACE-312 | proved | Line N15 exact carry reduction [P]: \|e\| <= 15 (sharp \|e\| <= 14, 29 values, 633 reachable pair states) and the torus-mean identity [P] |
| BGS-TRACE-313 | proved | Line N7/N8b Lemmas P, P' (all isotropic points at q = h_p, with the 4-fixed-point correction N8b-F3), P'_c, the classification and the weight amplification A_c [P] |
| BGS-TRACE-314 | proved | Line N7: the (+-2,16) contribution is closed at all levels for p >= 339 (two-term B16 form; crude form p >= 498) [CA]+[P] |
| BGS-TRACE-315 | proved | Line N17b K_p arithmetic [P]: h_{3p} = h_p K_p with K_p = 4 h_p^2 + 3, 7 \| K_p, gcd(h_p, K_p) \| 3; h_15 = 7 * 31^2 * 41 |
| BGS-TRACE-316 | proved | Line N17b CRT count [P]: at h = 8119 = 23 * 353 (m = 33) S = CRT and n = 7371 = 21 * 351; 7743 - 7371 = 372 are the non-unit nu excluded by BGS-TRACE-206 |
| BGS-TRACE-317 | proved | Line N17b level bookkeeping [P]: W'_m = NR part + phi^-1 sum Dev_d(rho) (BGS-TRACE-213), NR >= -RMT >= -4m, level floor -(h_p/d) S_rho, inclusion m0 = 15 |
| BGS-TRACE-318 | proved | Line N18b/N19b gas vs Robin crossover [P-arith], an arithmetic implication: under the idealisation tails = Y = X_cross = eps = 0 and n/h_p := 1, the gas lower bound exceeds the Robin bound on inherited levels for all p >= 1386 at the core value delta = 5.14476e-7 (BGS-TRACE-307) and, for the INPUT value delta = 2.470e-6, for all p >= 1390; first prime 1399 |
| BGS-TRACE-319 | proved | Line N14b/N18b Lemma 1 (sublattice separation) [P]: for squarefree d with split prime factors, delta-close pairs of the conductor-d components H_d separate after n_* steps, with delta0 = 1/(4 sqrt2 (lambda+1)) = 0.025888 and constant C = 16 lambda^2 delta^2 h^2 lambda^{-p} |
| BGS-TRACE-320 | verification-pending | Line N14b Lemma 2 (subgroup C', c_B = 0.7375) [P-sketch, asymptotic, constants ignored], covering iso parts d <= 1.588^p; p = 31 covered (H5, not P) |
| BGS-TRACE-321 | proved | Line N15 [CA-fp]: A_bad finite part j <= 12 = 2.031569e-6 at g0 = 4 (c3 radii) and short types sum \|w\| = 9.970e-7 (173 rows incl. alpha = 4) |
| BGS-TRACE-322 | proved | Line N16 [CA-fp]+[P-sketch]: delta_true(G <= 15) <= 2.470e-6 (vector-chain conversion per window, E/\|r\| ~ 1.7e-3) |
| BGS-TRACE-323 | proved | Line N15 [CA-fp]: SVD-free step-norm table for \|t\| > 1/256, max 2.91656 |
| BGS-TRACE-324 | verification-pending | Line N8 Prop X' (explicit error, p >= 1289) with the 15 small-depth classes [CA]: [P mod Line F certificates + class CA] for the certified classes; k-parity mechanism and E-family absorption [P-sketch] |
| BGS-TRACE-325 | conditional | Line N Theorem R#-mod v5 (conditional; THEOREM_DRAFT_v5 after lineN22 edits E1-E8): if H0, H1 (BGS-TRACE-336), H5-H8 (BGS-TRACE-303..306) hold at p (H2, H4 met; H3 follows from H1) and B_p >= kappa > 0 for infinitely many primes p >= p_thr, with B_p carrying e^{-p(delta + A_bad^KP)}, then W'_{3p}/m -> infinity and frozen R' is false along m = 3p (conditional; not a refutation) |
| BGS-TRACE-326 | proved | Line N21 H4 met [P] + [CA-fp] (not [CA]): true-functional interaction constant delta_true (all G) <= 5.0313e-6 = 2.2102e-6 (G <= 15) + 2.712658e-6 (16 <= G <= 36, box) + 1.0843e-7 (G >= 37, Lemma D^T) + 3.1e-13 (G > 60) |
| BGS-TRACE-327 | proved | Line N21 Lemma D^T [P] + [CA-fp]: true-operator difference form; G >= 37 tail of delta_true <= 1.0843e-7 (G = 37..60 <= 1.0842557e-7), remainder G > 60 <= 3.1e-13 |
| BGS-TRACE-328 | proved | Line N21 Lemma Q [P] + [CA] constants: \|\|(L_0/mu)^k Q\|\| <= m(k) with K_0 < 56.78 and Rem < 1.591e-3 |
| BGS-TRACE-329 | proved | Line N20 Prop. F [P mod N13 CA]: the unrestricted joint torus mean is >= 5.1e-7 * lambda^{-n} for 1 <= n <= 10^10 (fixed-point shadowing) |
| BGS-TRACE-330 | proved | Line N20 Lemma J [P]: joint (A,B) collisions are eps-adic (mu_B = -eps^{-1} mu_A); eps-carries \|e\| <= 51 (sharp), 6145 pair states; the lambda-carry graph (633 states, rho >= 20) and the renewal Lemma R |
| BGS-TRACE-331 | proved | Line N20 Thm A [CA-fp]: the H1 shell law holds for every shell j <= 14 for the core functional, C_cert(j) <= 4.36e-4 (<= 5.9e-5 for j >= 8) |
| BGS-TRACE-332 | conditional | Line N20 Prop. K (conditional on H1): H1-shell(C <= 0.082, J0 = 12) implies H3 with KP weight a = a(C) <= 2.70e-3 and budget left >= 2.738e-4 (with delta_true <= 5.0313e-6) |
| BGS-TRACE-333 | conditional | Line N v5 gas vs Robin crossover with all rate budgets (delta_true + A_bad^KP), additive terms idealised [P-arith], conditional on H1 via A_bad^KP: C <= 0.082 -> all p >= 3305, first prime 3307; C <= 0.04 -> 1726/1733; C <= 8.8e-4 -> 1402/1409; C <= 4.4e-4 -> 1402/1409 |
| BGS-TRACE-335 | proved | Line N21 Lemma C [P] + [CA-fp]: two-sided core -> true vector conversion including the second-order dPi^2 term; delta_true(G <= 15) <= 2.2102e-6 |
| BGS-TRACE-336 | open | Line N hypothesis H1, re-scoped by N20 (open [H]): (H1-bad) bad-cluster (polymer-restricted) joint (A,B) second moment on the eps-chain, sum_{bad, shell j} \|r_A r_B\|^2 <= C 2^{j(1 - beta(0.28))} for j > J0 = 12 with C <= 0.082, plus (H1-ali) the near-collision/box constants |
