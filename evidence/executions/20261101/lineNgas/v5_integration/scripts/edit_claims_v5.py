"""Integrator script (THEOREM_DRAFT_v5 integration, 2026-11-01): applies V5/CLAIMS_PROPOSED_v5.md as corrected by
referee lineN22 edits E9-E12 to record/claims.json and record/errata.json. Run once from the repository root."""
import json, sys
CP = 'record/claims.json'; EP = 'record/errata.json'
raw = open(CP, encoding='utf-8').read(); d = json.loads(raw)
assert json.dumps(d, indent=2, ensure_ascii=False) + '\n' == raw
by = {c['id']: c for c in d['claims']}
T = lambda k: f'BGS-TRACE-{k}'
assert T(325) not in by and T(324) in by
SRC = 'mathematics/fixed-map/lineN5N18_gas_conditional.md'
V = 'computations/verification/lineN_theorem_draft'
E = 'evidence/executions/20261101/lineNgas'
R = E + '/referee'
RECEIPT = E + '/v5_integration/receipt.json'
b302 = by[T(302)]['boundary']; cut = "Re Lambda_lo' = 6.234e-4."
SCOPE = b302[:b302.index(cut) + len(cut)]
SCOPE5 = SCOPE.replace('THEOREM_DRAFT_v3 section 1', 'THEOREM_DRAFT_v5 section 1')
REF22 = ('INDEPENDENT REFEREE AUDIT (' + R + '/lineN22/REPORT.md; FINAL PASS ON THEOREM_DRAFT_v5: GO AFTER EDITS E1-E12; '
         'E1-E8 APPLIED IN THE REPO COPY, E9-E12 APPLIED IN THE REGISTRY)')
REF21 = 'INDEPENDENT REFEREE AUDIT (' + R + '/lineN21/REPORT.md; N21 READY AFTER FIXES F1-F9, APPLIED IN REPORT_N21_v2)'
REF21b = 'INDEPENDENT REFEREE AUDIT (' + R + '/lineN21b/REPORT.md; N_H TABLE INDEPENDENTLY RECOMPUTED; BUDGETS; CROSSOVER 1401/1409 REPRODUCED)'
REF20 = 'INDEPENDENT REFEREE AUDIT (' + R + '/lineN20/REPORT.md; N20 READY AFTER FIXES 1-7, APPLIED IN REPORT_N20_v2)'
def dep(*ks): return [T(k) for k in sorted(ks)]
def addledger(k, text):
    c = by[T(k)]; assert text not in c['ledger_status']; c['ledger_status'] += ' + ' + text

# ---- existing claims ----
c = by[T(299)]; assert c['state'] == 'conditional'
addledger(299, 'SUPERSEDED BY BGS-TRACE-325 (THEOREM R#-MOD v5, THEOREM_DRAFT_v5; H4 MET BY BGS-TRACE-326, H3 FOLLOWS FROM H1 BY BGS-TRACE-332); STATE UNCHANGED (CONDITIONAL)')
c = by[T(300)]; assert c['state'] == 'open'
addledger(300, 'RE-SCOPED AS BGS-TRACE-336 (N20 v2: JOINT (A,B) BAD-CLUSTER SECOND MOMENT ON THE EPS-CHAIN + H1-ALI; referee lineN20, lineN22); STATE UNCHANGED (OPEN)')
c = by[T(301)]; assert c['state'] == 'open'
addledger(301, 'SUPERSEDED IN SUBSTANCE BY BGS-TRACE-332 (KP WITH a = a(C), PROP. K); a = 5.93e-6 USED THE WITHDRAWN 1.56e-8 TAIL PLACEHOLDER; UNDER PROP K a = a(C) >= 6.49e-6 (C >= 4.4e-4); STAYS OPEN, NOT CONDITIONAL, NOT AN INPUT OF BGS-TRACE-325 (referee lineN22 E10)')

# 302 (H4): proved; title parenthetical; deps rewired (E9)
c = by[T(302)]; assert c['state'] == 'open' and '(open, no working route)' in c['title']
c['title'] = c['title'].replace('(open, no working route)', '(met: BGS-TRACE-326)')
c['dependencies'] = dep(307, 322, 326, 327, 328)
c['state'] = 'proved'
old_cc = c.pop('closure_condition')
c['boundary'] += (' H4 met (THEOREM_DRAFT_v5, 1 November 2026): the closure condition ("' + old_cc.rstrip('.') + '") is met by N21 v2 '
    '[P] + [CA-fp] (not [CA]): Lemma D^T (BGS-TRACE-327, difference form, G >= 37 tail <= 1.0843e-7, G > 60 <= 3.1e-13) with Lemma Q '
    '(BGS-TRACE-328), Lemma C (BGS-TRACE-335, delta_true(G <= 15) <= 2.2102e-6) and the all-G bound delta_true <= 5.0313e-6 '
    '(BGS-TRACE-326), refereed lineN21, lineN21b and lineN22. The vector-chain description above is the superseded N16 route (defects '
    'F21-1/F21-3, lineN21). Standing-package inputs are taken as certified as for BGS-TRACE-307 (N8 n_cert constants, N13 V1-V3b, '
    'Line F F2, N6 symmetry).')
c['ledger_status'] = ('CLOSED [P] + [CA-fp] (NOT [CA]) BY BGS-TRACE-326/327/328/335 (AND 322 A FORTIORI); STATE open -> proved ON '
    '2026-11-01 (referee lineN22 E9); TITLE PARENTHETICAL "(open, no working route)" REPLACED BY "(met: BGS-TRACE-326)", ID AND '
    'MATHEMATICAL STATEMENT UNCHANGED (LOGGED IN record/claim_ledger.md) + ' + REF21 + ' + ' + REF21b + ' + ' + REF22 +
    ' + PREVIOUSLY: ' + c['ledger_status'])
c['evidence'] = c['evidence'] + [RECEIPT]
c['verifiers'] = [E + '/N21/REPORT_N21_v2.md', E + '/N21/code/tail_DT.py', E + '/N21/logs/final_delta_v2.json', R + '/lineN21/code/ref_DT.py']
c['formalization'] = ['formalization/Bgs/LineN21Arith.lean']

# 318: stays proved; boundary/ledger fix
c = by[T(318)]; assert c['state'] == 'proved'
old = 'Whether delta_true(G <= 15) <= 2.470e-6 actually holds is BGS-TRACE-322 (verification-pending); this claim neither asserts nor depends on it.'
assert old in c['boundary']
c['boundary'] = c['boundary'].replace(old, 'Whether delta_true(G <= 15) <= 2.470e-6 actually holds is BGS-TRACE-322 (proved a fortiori since 1 November 2026 via BGS-TRACE-335: delta_true(G <= 15) <= 2.2102e-6); this claim neither asserts nor depends on it.')
c['boundary'] += (' Boundary (THEOREM_DRAFT_v5, referee lineN22): the values 1386/1390/1399 charge delta only (A_bad^KP = 0). They are NOT '
    "the theorem's p1: B_p carries e^{-p(delta + A_bad^KP)} (THEOREM_DRAFT_v5 section 2). With all rate budgets see BGS-TRACE-333: "
    'first prime 3307 (H1 at C <= 0.082) / 1409 (C <= 8.8e-4). At delta_true = 5.0313e-6 alone: 1397/1399 (N21 v2; referee lineN21 '
    'section 4). This claim remains a true arithmetic implication in the input delta.')
old = 'delta_true <= 2.470e-6 IS BGS-TRACE-322, PENDING'
assert old in c['ledger_status']
c['ledger_status'] = c['ledger_status'].replace(old, 'delta_true(G <= 15) <= 2.470e-6 HOLDS A FORTIORI: BGS-TRACE-322 PROVED VIA BGS-TRACE-335 (<= 2.2102e-6), NOT A DEPENDENCY; NOT THE THEOREM\'S p1 (A_bad^KP = 0), SEE BGS-TRACE-333')
c['ledger_status'] += ' + ' + REF22

# 322: proved a fortiori via 335 (E11)
c = by[T(322)]; assert c['state'] == 'verification-pending'
c['state'] = 'proved'; c['dependencies'] = dep(307, 335)
old_cc = c.pop('closure_condition')
c['boundary'] += (' Proved a fortiori (1 November 2026, referee lineN22 E11): the bound in the title holds because N21 Lemma C '
    '(BGS-TRACE-335, [P] + [CA-fp]) gives delta_true(G <= 15) <= 2.2102e-6 <= 2.470e-6. The N16 vector-chain lemma and conv_vec.py '
    'named in the title are NOT the proof: they had defects F21-1/F21-3 (sqrt(cond) used non-conservatively; lineN21). The former '
    'closure condition ("' + old_cc.rstrip('.') + '") is met by Lemma C.')
c['ledger_status'] = ('PROVED A FORTIORI VIA BGS-TRACE-335 (N21 LEMMA C, [P] + [CA-fp]); STATE verification-pending -> proved ON 2026-11-01 '
    '(referee lineN22 E11); THE N16 METHOD IN THE TITLE HAD DEFECTS F21-1/F21-3 (lineN21) AND IS NOT THE PROOF + ' + REF21 + ' + ' + REF22 +
    ' + PREVIOUSLY: ' + c['ledger_status'])
c['evidence'] = c['evidence'] + [RECEIPT]
c['verifiers'] = c['verifiers'] + [E + '/N21/code/conv_c.py', E + '/N21/code/f_postC.py', E + '/N21/logs/f_postC_v2.json']
c['formalization'] = ['formalization/Bgs/LineN21Arith.lean']

# 323: proved [CA-fp] (closure met by lineN21b)
c = by[T(323)]; assert c['state'] == 'verification-pending'
c['state'] = 'proved'; old_cc = c.pop('closure_condition')
c['boundary'] += (' Values independently recomputed (lineN21b, 1 November 2026): different method (SVD + residual certificate); max '
    "2.916448 <= 2.91656, every one of the 2048 cells <= N15's value, minimum margin 3.93e-5; 20 cells including the max cell [CA] (arb). "
    'The former closure condition ("' + old_cc.rstrip('.') + '") is met.')
c['ledger_status'] = ('PROVED [CA-fp] (VALUES INDEPENDENTLY RECOMPUTED BY lineN21b; 20 CELLS [CA]); STATE verification-pending -> proved ON '
    '2026-11-01 + ' + REF21b + ' + ' + REF22 + ' + PREVIOUSLY: ' + c['ledger_status'])
c['evidence'] = c['evidence'] + [RECEIPT]
c['verifiers'] = c['verifiers'] + [R + '/lineN21b/code/nh_fp.py', R + '/lineN21b/code/nh_arb.py', R + '/lineN21b/logs/post.json']

# ---- new claims ----
def new(k, title, deps, state, tag_boundary, ledger, verifiers, lean, closure=None):
    row = {'id': T(k), 'title': title, 'source': SRC, 'dependencies': dep(*deps),
           'boundary': SCOPE5 + ' ' + tag_boundary, 'state': state, 'ledger_status': ledger,
           'external_dependencies': [], 'evidence': [RECEIPT], 'verifiers': verifiers,
           'formalization': lean, 'manuscript': []}
    if closure: row['closure_condition'] = closure
    assert state == 'proved' or closure
    d['claims'].append(row); by[T(k)] = row
L21 = 'formalization/Bgs/LineN21Arith.lean'; L20 = 'formalization/Bgs/LineN20Arith.lean'; L20T = 'formalization/Bgs/LineN20TailArith.lean'
X = V + '/V5'
new(325, "Line N Theorem R#-mod v5 (conditional; THEOREM_DRAFT_v5 after lineN22 edits E1-E8): if H0, H1 (BGS-TRACE-336), H5-H8 (BGS-TRACE-303..306) hold at p (H2, H4 met; H3 follows from H1) and B_p >= kappa > 0 for infinitely many primes p >= p_thr, with B_p carrying e^{-p(delta + A_bad^KP)}, then W'_{3p}/m -> infinity and frozen R' is false along m = 3p (conditional; not a refutation)",
    (206, 213, 271, 273, 336, 303, 304, 305, 306, 307, 326, 332, 333), 'conditional',
    "[P mod inputs H0, H1, H5-H8; log -> modulus / background-interplay step P-sketch] (THEOREM_DRAFT_v5 section 2). B_p := (n/h_p)[(2(1 + Re Lambda_lo')^p e^{-p(delta + A_bad^KP)} - 1 - |X_tail| - |X_cross| - |Y| - e^{-0.28p})^2 - 1] - I_p - eps_16 - eps_fl - eps_other, delta = delta_true <= 5.0313e-6 (BGS-TRACE-326), A_bad^KP = S_0(a) of Prop. K (BGS-TRACE-332, depends on H1's constant C). Then W'_{3p}/m >= -4 + m^-1 sum_{rho=(+-2,8)} S_rho B_p with S_rho >= c 1.13287^m (BGS-TRACE-271). The A_bad^KP-in-exponent step (|ln Xi_bad| <= p S_0(a), anchored KP corollary, Ueltschi 2004 Thm 1, with model-background-renormalised activities) is [P-sketch], correct and necessary (referee lineN22). H0 is the standing package (BGS-TRACE-197/199/207/212/213/228, Prop X' BGS-TRACE-324, n_cert). H3 (BGS-TRACE-301) is not an input: it is replaced by Prop. K (332). Thresholds: p1 with all rate budgets (BGS-TRACE-333): first prime 3307 (C <= 0.082, fragile: +1% in S_0 gives 3359) / 1409 (C <= 8.8e-4, robust); additive budgets (tails, Y, X_cross, eps, n/h_p) not computed. Supersedes BGS-TRACE-299 (v4). Frozen R' (BGS-TRACE-206) is used only for its frozen definition and is NOT refuted.",
    'CONDITIONAL THEOREM [P MOD INPUTS H0, H1, H5-H8] (ASSEMBLY; LOG -> MODULUS / BACKGROUND-INTERPLAY STEP [P-sketch]; THE INPUTS H1 (BGS-TRACE-336), H5, H6, H7*, H8 ARE OPEN; FROZEN R\' IS NOT REFUTED) + ' + REF22,
    [V + '/THEOREM_DRAFT_v5.md', R + '/lineN22/REPORT.md'], [L20T, L21],
    'Close every open input H1 (BGS-TRACE-336), H5 (or infinitude of P), H6, H7*, H8 (BGS-TRACE-303..306), write out the log -> modulus / background-interplay step, compute p_thr with the additive budgets, and show B_p >= kappa > 0 for infinitely many p; or disprove an input in a way that kills the route.')
new(326, 'Line N21 H4 met [P] + [CA-fp] (not [CA]): true-functional interaction constant delta_true (all G) <= 5.0313e-6 = 2.2102e-6 (G <= 15) + 2.712658e-6 (16 <= G <= 36, box) + 1.0843e-7 (G >= 37, Lemma D^T) + 3.1e-13 (G > 60)',
    (198, 307, 311, 322, 323, 327, 328, 335), 'proved',
    '[P] + [CA-fp] (N21 v2 section 5; parts sum to 5.031288e-6 <= 5.0313e-6, Lean Bgs.LineN21.delta_true_sum). Not [CA]: the window chains are [CA-fp] (IEEE binary64, standard model + libm <= 1 ulp). Standing-package inputs taken as certified and not registered as dependencies (as for BGS-TRACE-307): the N8 n_cert constants (Pert/Xn/dPi/...), N13 V1-V3b, Line F F2 (BGS-TRACE-198) and the N6 symmetry. For comparison the core functional gives delta_int^core <= 5.14476e-7 (BGS-TRACE-307). Refereed lineN21 (bit-identical spot reruns, own aggregation), lineN21b (N_H table, budgets) and lineN22.',
    'PROVED [P] + [CA-fp] (NOT [CA]; STANDING-PACKAGE CONSTANTS TAKEN AS CERTIFIED) + LEAN ARITHMETIC (Bgs.LineN21) + ' + REF21 + ' + ' + REF21b + ' + ' + REF22,
    [E + '/N21/REPORT_N21_v2.md', E + '/N21/code/final_delta.py', E + '/N21/logs/final_delta_v2.json'], [L21])
new(327, 'Line N21 Lemma D^T [P] + [CA-fp]: true-operator difference form; G >= 37 tail of delta_true <= 1.0843e-7 (G = 37..60 <= 1.0842557e-7), remainder G > 60 <= 3.1e-13',
    (323, 328, 335), 'proved',
    '[P] (after referee fixes F1/F2; step 4 written out, N21 v2 section 4) + [CA-fp] anchors + arb sums (tail_DT.py v2). Refereed lineN21 (independent rerun of tail_DT, ref_DT.py).',
    'PROVED [P] + [CA-fp] ANCHORS + ARB SUMS + LEAN ARITHMETIC (Bgs.LineN21) + ' + REF21 + ' + ' + REF22,
    [E + '/N21/code/tail_DT.py', E + '/N21/logs/tail_DT_40_200_v2.json', R + '/lineN21/code/ref_DT.py', R + '/lineN21/code/rerun_tail_DT.py'], [L21])
new(328, 'Line N21 Lemma Q [P] + [CA] constants: ||(L_0/mu)^k Q|| <= m(k) with K_0 < 56.78 and Rem < 1.591e-3',
    (310, 311), 'proved',
    '[P] + [CA] constants (N21 v2 section 4); the referee recomputed every constant independently in arb, agreement >= 11 digits (lineN21). Lean checks the rational arithmetic (Bgs.LineN21.Rem_up, m1_up, m2_up, K0_up).',
    'PROVED [P] + [CA] CONSTANTS (REFEREE ARB RECOMPUTATION) + LEAN ARITHMETIC (Bgs.LineN21) + ' + REF21 + ' + ' + REF22,
    [E + '/N21/REPORT_N21_v2.md', R + '/lineN21/code/ref_post.py', R + '/lineN21/logs/ref_post.json'], [L21])
new(329, "Line N20 Prop. F [P mod N13 CA]: the unrestricted joint torus mean is >= 5.1e-7 * lambda^{-n} for 1 <= n <= 10^10 (fixed-point shadowing)",
    (311, 312), 'proved',
    "Lower bound only [P mod N13 CA] (N20 v2 section 2; referee lineN20 fix 4). [N], not part of this claim: the ratio to the i.i.d. value is > 1 for 22 <= n <= 10^10 and therefore no unrestricted carry/Bohr-mean method can give H1; this ratio statement uses the N14 float 3.45 [N] (and N15 rhobar = 0.28 [CA-fp]); '-> infinity' is withdrawn. A negative result: it rules out a route to H1 (BGS-TRACE-336), it does not bound a gas quantity.",
    'PROVED [P MOD N13 CA] (LOWER BOUND ONLY; RATIO STATEMENT [N] IN THE BOUNDARY; referee lineN22 E12) + ' + REF20 + ' + ' + REF22,
    [E + '/N20/REPORT_N20_v2.md', R + '/lineN20/code/ref_propF.py', R + '/lineN20/logs/ref_propF.out'], [])
new(330, "Line N20 Lemma J [P]: joint (A,B) collisions are eps-adic (mu_B = -eps^{-1} mu_A); eps-carries |e| <= 51 (sharp), 6145 pair states; the lambda-carry graph (633 states, rho >= 20) and the renewal Lemma R",
    (312,), 'proved',
    '[P] (N20 v2 sections 2-3) + exact BFS (carry_graph.py, carry_graph_eps.py). Lean: Bgs.LineN20 (reachable sets, |FW cap BW| = 633, max |e| = 14, Collatz-Wielandt A x >= 20 x, by decide +kernel; no native_decide) and Bgs.LineN20Tail (renewal lemma, eps-carry closed-form arithmetic |e| <= 51; eps_green_l1 only equates two closed forms, the Green l1 evaluation and the 6145-state count are Python/exact-integer, not Lean). Refereed lineN20 (carries.py, green.py).',
    'PROVED [P] + EXACT ENUMERATION + LEAN (Bgs.LineN20, Bgs.LineN20Tail) + ' + REF20 + ' + ' + REF22,
    [E + '/N20/code/carry_graph_eps.py', E + '/N20/logs/carry_graph_eps.json', E + '/N20/code/carry_graph.py', E + '/N20/logs/carry_graph_cert.json', R + '/lineN20/code/carries.py'], [L20, L20T])
new(331, 'Line N20 Thm A [CA-fp]: the H1 shell law holds for every shell j <= 14 for the core functional, C_cert(j) <= 4.36e-4 (<= 5.9e-5 for j >= 8)',
    (307, 311, 321), 'proved',
    '[CA-fp] core functional only (c3_mid radii, IEEE standard model + libm <= 1 ulp; exponent factors in arb); the H4 conversion was not run on these shells (N20 v2 section 3.1, referee lineN20 fix 3). By Prop. F (BGS-TRACE-329) the finite shells are not evidence for the tail j > 14 (H1, BGS-TRACE-336). Margin 0.082/4.36e-4 > 188 (Lean Bgs.LineN20Tail.shell_margin).',
    'PROVED [CA-fp] (CORE FUNCTIONAL, FINITE SHELLS j <= 14) + LEAN ARITHMETIC (Bgs.LineN20Tail) + ' + REF20 + ' + ' + REF22,
    [E + '/N20/code/shell_law.py', E + '/N20/logs/shell_law_v2.json', E + '/N20/code/a_cert_ext.py', R + '/lineN20/code/ref_shell.py', R + '/lineN20/logs/ref_shell.json'], [L20T])
new(332, 'Line N20 Prop. K (conditional on H1): H1-shell(C <= 0.082, J0 = 12) implies H3 with KP weight a = a(C) <= 2.70e-3 and budget left >= 2.738e-4 (with delta_true <= 5.0313e-6)',
    (336, 321, 326, 331), 'conditional',
    "[P + CA mod H1-shell; span bound l <= 2j + g0 P-sketch; background interplay P-sketch] (N20 v2 section 3.4; tail_kp.py v2, tail_kp_v2.json; Lean rational checks Bgs.LineN20Tail.kp_*). A_bad^KP = S_0(a) per C at J0 = 12: <= 3.4457e-4 (C = 0.082, a = 2.69e-3), 1.1182e-4 (0.04), 2.3798e-6 (8.8e-4, a = 8.25e-6), 2.1548e-6 (4.4e-4); a >= 6.49e-6 for C >= 4.4e-4. The withdrawn 1.56e-8 tail placeholder of N15 (BGS-TRACE-301) is not used. Background interplay: the bad activities must be renormalised by the model background before KP is applied (referee lineN22 section 1, estimate not proof). Replaces H3 (BGS-TRACE-301) as input of BGS-TRACE-325.",
    'CONDITIONAL ON H1 (BGS-TRACE-336) [P + CA MOD H1-SHELL; SPAN BOUND AND BACKGROUND INTERPLAY P-sketch] + LEAN ARITHMETIC (Bgs.LineN20Tail) + ' + REF20 + ' + ' + REF22,
    [E + '/N20/code/tail_kp.py', E + '/N20/logs/tail_kp_v2.json', R + '/lineN20/code/ref_propk.py'], [L20T],
    'A proof of H1-shell (BGS-TRACE-336) and written proofs of the span bound l <= 2j + g0 and of the background-interplay normalisation.')
new(333, 'Line N v5 gas vs Robin crossover with all rate budgets (delta_true + A_bad^KP), additive terms idealised [P-arith], conditional on H1 via A_bad^KP: C <= 0.082 -> all p >= 3305, first prime 3307; C <= 0.04 -> 1726/1733; C <= 8.8e-4 -> 1402/1409; C <= 4.4e-4 -> 1402/1409',
    (336, 318, 326, 332), 'conditional',
    "[P-arith: float + exact big-int K_p + monotonicity, N19b logic verbatim (V5/code/crossover_v5.py); independently reproduced in mpmath by referee lineN22 (xover22.py)], under the idealisation tails = Y = X_cross = eps = 0, n/h_p := 1; no violation among primes <= 5000. delta_eff = delta_true + A_bad^KP: 3.4962e-4 (C = 0.082), 1.1691e-4 (0.04; the unrounded input 1.16848e-4 gives 1725/1733), 7.4115e-6 (8.8e-4), 7.1864e-6 (4.4e-4); v4-style 7.0944e-6 (withdrawn placeholder) -> 1401/1409. Sensitivity (referee lineN22, sens22.json): 3307 is fragile (A_bad^KP x 1.01 -> 3359, x 1.03 -> 3449, x 1.10 -> 3821), 1409 is robust (unchanged up to A_bad^KP x 2). Charging a instead of S_0 would be wrong (no crossover at C >= 0.04). The p1 with the additive budgets is open.",
    'CONDITIONAL ON H1 (BGS-TRACE-336) THROUGH A_bad^KP [P-arith] (FLOAT + EXACT BIG-INT K_p + MONOTONICITY; REFEREE MPMATH REPLAY) + ' + REF21b + ' + ' + REF22,
    [X + '/code/crossover_v5.py', X + '/logs/crossover_v5_d3.496200e-04.json', X + '/logs/crossover_v5_d1.169100e-04.json', X + '/logs/crossover_v5_d7.411500e-06.json', X + '/logs/crossover_v5_d7.186400e-06.json', R + '/lineN22/code/xover22.py', R + '/lineN22/logs/xover22.json', R + '/lineN22/code/sens22.py', R + '/lineN22/logs/sens22.json'], [L21],
    'A proof of H1 (BGS-TRACE-336) at the stated constant, and the threshold recomputed with the additive budgets (tails, Y, X_cross, eps, n/h_p).')
new(335, 'Line N21 Lemma C [P] + [CA-fp]: two-sided core -> true vector conversion including the second-order dPi^2 term; delta_true(G <= 15) <= 2.2102e-6',
    (198, 307, 311, 323), 'proved',
    '[P] (N21 v2 section 2, verified line by line by referee lineN21) + [CA-fp] window numerics (conv_c.py, f_postC.py v2; IEEE standard model + libm <= 1 ulp), conditional on the certified inputs of N21 v2 section 7 (N8 n_cert constants, N13 V1-V3b, Line F F2, N6 symmetry), taken as certified as for BGS-TRACE-307. tau = dPi ||psi_T|| ||Phi_T|| < 6.1374e-4 (Lean Bgs.LineN21.tau_lt, den_tau_pos). Proves BGS-TRACE-322 a fortiori; does not use the N16 vector-chain code (defects F21-1/F21-3).',
    'PROVED [P] + [CA-fp] + LEAN ARITHMETIC (Bgs.LineN21) + ' + REF21 + ' + ' + REF22,
    [E + '/N21/code/conv_c.py', E + '/N21/code/f_postC.py', E + '/N21/logs/f_postC_v2.json', R + '/lineN21/code/rerun_convC_spot.py', R + '/lineN21/logs/rerun_convC_spot.json'], [L21])
new(336, 'Line N hypothesis H1, re-scoped by N20 (open [H]): (H1-bad) bad-cluster (polymer-restricted) joint (A,B) second moment on the eps-chain, sum_{bad, shell j} |r_A r_B|^2 <= C 2^{j(1 - beta(0.28))} for j > J0 = 12 with C <= 0.082, plus (H1-ali) the near-collision/box constants',
    (309, 312, 330, 331), 'open',
    "[H] (N20 v2 sections 1, 4; THEOREM_DRAFT_v5 section 2). Re-scoping of BGS-TRACE-300: the object changed from the single-window collision sum to the joint (A,B) pair on one eps-chain (Lemma J, BGS-TRACE-330) and gained H1-ali. Finite part j <= 14 certified for the core functional (Thm A, BGS-TRACE-331, C_cert <= 4.36e-4). By Prop. F (BGS-TRACE-329) no unrestricted carry/torus bound can close it; the 633-state lambda-carry certificate and single-window [N] are not evidence for it. The constant C enters the threshold through A_bad^KP (BGS-TRACE-332, 333).",
    'OPEN HYPOTHESIS [H] (INPUT H1 OF BGS-TRACE-325; RE-SCOPED FROM BGS-TRACE-300) + ' + REF20 + ' + ' + REF22,
    [], [],
    '(H1-bad) a phase-keeping certificate for the bad-restricted joint (A,B) excursion system (eps-carries |e| <= 51, 6145 pair states) giving the shell rate with C <= 0.082 at J0 = 12 for all j > 12, and (H1-ali) the Beurling-Selberg box constants of the near-collision cells.')
assert T(334) not in by
open(CP, 'w', encoding='utf-8').write(json.dumps(d, indent=2, ensure_ascii=False) + '\n')

# ---- errata: 334 -> ERR-065 (E12) ----
raw = open(EP, encoding='utf-8').read(); e = json.loads(raw)
assert json.dumps(e, indent=2, ensure_ascii=False) + '\n' == raw
ids = {x['id'] for x in e['entries']}; assert 'ERR-065' not in ids and 'ERR-064' in ids
e['entries'].append({'id': 'ERR-065',
  'title': 'Line N14 digits.py twists at mp.dps = 34 (N21 F21-2)',
  'disposition': 'corrected: N14 digits.py with mp.dps = 34 corrupts the twists for G >= 21 at the ulp level, material from G >~ 25 (4.4e-15 at G = 25, 1.2e-3 at G = 40) (N21 F21-2, refereed lineN21). Proposed as claim BGS-TRACE-334 in V5/CLAIMS_PROPOSED_v5.md and recorded here instead (referee lineN22 E12); no claim ID 334 is registered.',
  'downstream': 'G <= 20 is exact, so the v4 numbers (G <= 15) are unaffected. All N21 G >= 16 data behind BGS-TRACE-326/327 use dps = 160; the dps-34 runs are kept only under N21/logs/discarded_dps34.',
  'authority': E + '/N21/REPORT_N21_v2.md'})
e['updated'] = '2026-11-01'
open(EP, 'w', encoding='utf-8').write(json.dumps(e, indent=2, ensure_ascii=False) + '\n')
print('ok', len(d['claims']))
