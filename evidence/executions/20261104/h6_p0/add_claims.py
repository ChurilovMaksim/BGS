#!/usr/bin/env python3
"""Hand-edit of record/claims.json for the H6 explicit-p0 / Lemma W integration (P4 v2 after referee audit/p4): new ids 342, 343 (renumbered from 337, 338: PR #88 owns BGS-TRACE-337..341)."""
import json, pathlib
P = pathlib.Path('record/claims.json'); raw = P.read_text(encoding='utf-8'); d = json.loads(raw); cl = d['claims']; by = {c['id']: c for c in cl}
assert json.dumps(d, indent=2, ensure_ascii=False) + '\n' == raw
assert 'BGS-TRACE-342' not in by and 'BGS-TRACE-343' not in by
V = 'computations/verification/h6_p0'; E = 'evidence/executions/20261104/h6_p0'
SRC = f'{V}/REPORT_P4_v2.md'; EV = [f'{E}/receipt.json']
REF = f'INDEPENDENT REFEREE AUDIT ({E}/referee/AUDIT.md; LEMMA W CONFIRMED; p0 NEEDS FIX (e^{{beta Rc}}, A_J <= 4/3), FIXES 1-6 APPLIED IN REPORT_P4_v2; CORRECTED p0 28,424,695 / 3,934 REPRODUCED BY THE v2 ARB RERUN)'
LEAN = 'formalization/Bgs/H6LemmaW.lean'
w = dict(id='BGS-TRACE-342',
 title="Lemma W [P]: for odd primes p and q with q | h_p = (eps^p + epsbar^p)/2, eps = 1 + sqrt2: q = +-1 (mod 2p); hence p does not divide h_p, the j-th smallest prime factor of h_p is >= pj - 1, and omega(h_p) <= w_max(p) := max{w : (p-1)^w w! <= eps^p}",
 source=SRC, dependencies=[],
 boundary="For odd primes p and q with q | h_p = (eps^p + epsbar^p)/2, eps = 1+sqrt2: q = +-1 (mod 2p). Hence p does not divide h_p, the j-th smallest prime factor of h_p is >= pj - 1, and omega(h_p) <= w_max(p) := max{w : (p-1)^w w! <= eps^p}. "
 "[P] REPORT_P4_v2 section 2.1 (h_n odd; O/q unramified; eps^{2p} = 1 and ord(eps) in {p, 2p} since N(eps - 1) = -2, N(eps^2 - 1) = -4; split p | q - 1, inert eps^{q+1} = -1 so p | q + 1; counting slots; h_p < eps^p), checked line by line by the referee. "
 "[N] 0 violations for all primes q < 10^8 dividing h_p, 3 <= p < 500 (P4, lemmaW_trial.py, no presieve). Complete factorisations (BPSW primality, uncertified for large factors) for 47 p <= 233 are squarefree with omega <= 6. "
 "Lean (Bgs.H6LemmaW, decide +kernel, no axioms): every divisor d > 1 of h_p is = +-1 (mod 2p) for p = 3, 5, 7, 11, 13, and p, 2 do not divide h_p for odd primes p < 100; finite check only. Does not prove that h_p is squarefree.",
 state='proved', ledger_status='PROVED [P] + [N] (TRIAL DIVISION q < 1e8, p < 500) + LEAN FINITE CHECK (Bgs.H6LemmaW) + ' + REF,
 external_dependencies=[], evidence=EV,
 verifiers=[f'{V}/code/lemmaW_trial.py', f'{V}/logs/lemmaW_trial.json', f'{V}/code/lemmaW_full.py', f'{V}/logs/lemmaW_full_partial.out', f'{E}/referee/code/lw.py'],
 formalization=[LEAN], manuscript=[])
h = dict(id='BGS-TRACE-343',
 title="H6 / Theorem C' explicit threshold [P + CA, mod inherited N4 Lambda, kappa_F and N2 r_2; given h_p squarefree and the torus normalisation u = 1]: for 8V (k = 4000) the unit-point cross part at c = h_p is < T^{3p} = 1.28359^{3p} for every prime p >= 28,424,695 with h_p squarefree; for 8E (k = 1000) for p >= 3,934",
 source=SRC, dependencies=['BGS-TRACE-289', 'BGS-TRACE-294', 'BGS-TRACE-296', 'BGS-TRACE-342'],
 boundary="For the 8V family (k = 4000), the unit-point cross part at c = h_p is < T^{3p} = 1.28359^{3p} for every prime p >= 28,424,695 with h_p squarefree. For 8E (k = 1000) this holds for p >= 3,934. "
 "Proof: interval cover of [p0, 10^10] plus an analytic tail (h6_p0.py certify, arb 128-bit balls, restart-on-failure since the pointwise test is not monotone near p0). The constants are C_I <= 5.2535e8, S <= 61.002, log L' <= 6909.80 and log K(p) <= 31804.6 + 2 log p, including e^{beta Rc} = e^{10} and A_J <= 4/3 (8E: e^{8.75}). "
 "Conditional on exactly: (i) the frequency normalisation u = 1 in (C1) (the image of e_q in O; its effect is O(1) in log K), assumed; (ii) h_p squarefree (open, Wieferich-type; Theorem C' assumes it); (iii) the inherited N4 [CA] constants Lambda^{8V} <= 1.9656353, kappa_F = 4036, Lambda^{8E} <= 0.4915932, kappa = 4.3e4 and the N2 r_2 certificate (r_2 rerun here); (iv) 8V/8E only. "
 "Lemma I one-step structure [P] from TRACE-197/249/294 and lineF/code/cert_lift.py. The threshold is for this bound only, not optimal; 16V/16E are not covered; the other additive budgets of p_thr are not included. Partially discharges the explicit-p0 part of H6 (BGS-TRACE-304, unchanged, still open).",
 state='conditional', ledger_status="CONDITIONAL [P + CA] (MOD u = 1 IN (C1), h_p SQUAREFREE, INHERITED N4 Lambda/kappa_F AND N2 r_2; 8V/8E ONLY) + " + REF,
 external_dependencies=[], evidence=EV,
 verifiers=[f'{V}/code/h6_p0.py', f'{V}/logs/h6_p0.json', f'{V}/code/h6_variants.py', f'{V}/logs/h6_variants.json', f'{V}/code/r2_cert_x0.py', f'{V}/logs/r2_cert_x0.jsonl', f'{E}/referee/code/indep.py', f'{E}/referee/code/indep.out'],
 formalization=[], manuscript=[],
 closure_condition="Verify the u = 1 normalisation of (C1), prove h_p squarefree for the p used (or extend C' to conductor-q^a weights), and extend to 16V/16E.")
i = max(k for k, c in enumerate(cl) if c['id'] == 'BGS-TRACE-336') + 1
cl[i:i] = [w, h]; d['updated'] = '2026-11-04'
P.write_text(json.dumps(d, indent=2, ensure_ascii=False) + '\n', encoding='utf-8'); print('ok', len(cl))
