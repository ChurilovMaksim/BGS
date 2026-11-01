"""Integrator script (no repo script regenerates these curated files; same procedure as the Line L/N integrations):
mirror record/claims.json into record/claim_verification_inventory.json (new rows 325-333, 335, 336; rebuilt rows for the state
changes 302, 322, 323; re-mirrored fields elsewhere; source_blob_sha) and append/annotate record/claim_integration_epochs.json."""
import json, hashlib
C = {c['id']: c for c in json.load(open('record/claims.json', encoding='utf-8'))['claims']}
T = lambda k: f'BGS-TRACE-{k}'
# ---------------- inventory ----------------
P = 'record/claim_verification_inventory.json'; raw = open(P, encoding='utf-8').read(); v = json.loads(raw)
dump = lambda o: json.dumps(o, indent=1, ensure_ascii=False, separators=(',', ': ')); assert dump(v) == raw
order = list([r for r in v['claims'] if r['id'] == 'BGS-TRACE-207'][0].keys()); EN = v['method_enumeration']
A, CC, IR, LF, CI = 'analytic_proof', 'computer_certificate', 'independent_review', 'lean_formalization', 'conditional_input'
UA, SV, NP, CU = 'unformalized_analytic_chain', 'single_verifier_implementation_only', 'no_proof_or_receipt_in_tree', 'conditional_on_unproved_input'
FC = 'finite_controls_separate_from_proof'
M = {
 302: ([A, CC, IR, LF], SV, "Closed by N21 v2 [P] + [CA-fp] (Lemmas C, Q, D^T; one implementation per window chain, referee reruns lineN21); standing-package constants taken as certified; Lean checks arithmetic only."),
 322: ([A, CC, IR, LF], SV, "Proved a fortiori via BGS-TRACE-335 (N21 Lemma C [P] + [CA-fp]); the N16 vector-chain method in the title is defective (F21-1/F21-3) and is not the proof."),
 323: ([CC, IR], FC, "[CA-fp] table (nh_table_rig.py) with an independent recomputation by a different method (lineN21b, SVD + residual certificate); only 20 cells are [CA] (arb)."),
 325: ([A, IR, LF, CI], CU, "Conditional assembly [P mod inputs H0, H1, H5-H8]; open inputs BGS-TRACE-336, 303..306; log -> modulus / background-interplay step [P-sketch]; refereed lineN22; Lean checks arithmetic only."),
 326: ([A, CC, IR, LF], SV, "[P] + [CA-fp] sum of four parts (N21 v2 section 5), not [CA]; standing-package constants taken as certified; refereed lineN21/lineN21b; Lean checks the sum."),
 327: ([A, CC, IR, LF], SV, "[P] (after F1/F2) + [CA-fp] anchors + arb sums (tail_DT.py v2); referee rerun (rerun_tail_DT.py, ref_DT.py)."),
 328: ([A, CC, IR, LF], SV, "[P] + [CA] constants; referee arb recomputation of every constant (lineN21); Lean checks the rational arithmetic."),
 329: ([A, IR], UA, "Lower bound [P mod N13 CA] only; the ratio statement is [N] (N14 float 3.45) and is not part of the claim; referee script ref_propF.py."),
 330: ([A, CC, IR, LF], UA, "Paper proofs (Lemma J, Lemma R) + exact BFS enumeration; Lean decides the 633-state graph facts and the closed-form carry arithmetic only."),
 331: ([CC, IR, LF], SV, "[CA-fp] core functional, shells j <= 14 only (shell_law.py v2); referee ref_shell.py; Lean checks the margin only."),
 332: ([A, CC, IR, LF, CI], CU, "Conditional on H1-shell (BGS-TRACE-336); span bound and background interplay [P-sketch]; arb bookkeeping (tail_kp.py v2) with referee ref_propk.py; Lean rational checks."),
 333: ([CC, IR, LF, CI], CU, "[P-arith] float + exact big-int K_p + monotonicity (crossover_v5.py), referee mpmath replay (xover22.py); conditional on H1 through A_bad^KP; additive budgets idealised."),
 335: ([A, CC, IR, LF], SV, "[P] (verified line by line, lineN21) + [CA-fp] window numerics (conv_c.py, f_postC.py v2); referee spot reruns bit-identical; Lean checks tau and the denominator."),
 336: ([IR], NP, "state is open"),
}
spofs = {r['spof'] for r in v['claims']}
def row(i, meth, sp, det):
    c = C[i]; op = c['state'] == 'open'; assert sp in spofs and all(x in EN for x in meth), i
    meth = [x for x in EN if x in meth]
    if not op: assert bool(c['formalization']) == (LF in meth), i
    r = {'id': i, 'title': c['title'], 'state': c['state'], 'methods': ['unevidenced'] if op else meth,
         'ledger_claimed_methods': [x for x in meth if x != LF], 'unevidenced': op or not any(c[k] for k in ('evidence', 'verifiers', 'formalization')),
         'adverse_receipt': False, 'receipt_counts': {x: len(c[x]) for x in ('evidence', 'verifiers', 'formalization')},
         'evidence': c['evidence'], 'verifiers': c['verifiers'], 'formalization': c['formalization'], 'ledger_status': c['ledger_status'],
         'boundary': c['boundary'], 'spof': sp, 'spof_detail': det, 'other_weaknesses': [],
         'risk_reassessment': 'OPEN_CONJECTURE' if op else 'PENDING_INDEPENDENT_PROOF_REVIEW'}
    return {x: r[x] for x in order}
idx = {r['id']: n for n, r in enumerate(v['claims'])}
rebuilt, added = [], []
for k, (meth, sp, det) in M.items():
    i = T(k); r = row(i, meth, sp, det)
    if i in idx: v['claims'][idx[i]] = r; rebuilt.append(k)
    else: v['claims'].append(r); added.append(k)
F = ('title', 'state', 'ledger_status', 'boundary', 'evidence', 'verifiers', 'formalization'); remir = []
for r in v['claims']:
    c = C[r['id']]; diff = [x for x in F if r[x] != c[x]]
    if diff:
        assert 'state' not in diff, r['id']
        remir.append((r['id'], diff)); [r.__setitem__(x, c[x]) for x in F]
        r['receipt_counts'] = {x: len(c[x]) for x in ('evidence', 'verifiers', 'formalization')}
        if r['formalization'] and not r['unevidenced']: assert LF in r['methods'], r['id']
assert {r['id'] for r in v['claims']} == set(C) and len(v['claims']) == len(C)
v['caveats'].append('1 November 2026 (THEOREM_DRAFT_v5 integration, referee lineN22): rows BGS-TRACE-325..333, 335, 336 appended; rows 302 '
    '(open -> proved), 322 and 323 (verification-pending -> proved) rebuilt with new method tags; 299, 300, 301, 318 re-mirrored (ledger/boundary text only). '
    'New and rebuilt rows are provisional (PENDING_INDEPENDENT_PROOF_REVIEW); Lean links certify finite arithmetic only.')
b = open('record/claims.json', 'rb').read(); v['source_blob_sha'] = hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()
open(P, 'w', encoding='utf-8').write(dump(v)); print('inventory', v['source_blob_sha'], 'added', added, 'rebuilt', rebuilt, 'remirrored', remir)
# ---------------- epochs ----------------
P = 'record/claim_integration_epochs.json'; raw = open(P, encoding='utf-8').read(); d = json.loads(raw)
assert json.dumps(d, indent=2, ensure_ascii=False) + '\n' == raw
S = 'mathematics/fixed-map/lineN5N18_gas_conditional.md'; TAIL = " Does not close TRACE-206, TRACE-148 or BGS-001; frozen R' is not refuted."
H = '1 November 2026 (THEOREM_DRAFT_v5; Lines N20, N21; referee lineN22 GO after E1-E12): '
lab = {
 325: "conditional theorem [P mod inputs H0, H1 (TRACE-336), H5-H8] (Theorem R#-mod v5, canonical statement THEOREM_DRAFT_v5; B_p with e^{-p(delta + A_bad^KP)}, A_bad step [P-sketch]; supersedes TRACE-299)",
 326: "proved [P] + [CA-fp] (H4 met: delta_true <= 5.0313e-6, all G; not [CA])",
 327: "proved [P] + [CA-fp] (Lemma D^T, G >= 37 tail)", 328: "proved [P] + [CA] constants (Lemma Q)",
 329: "proved [P mod N13 CA] (Prop. F, lower bound only; ratio statement [N])", 330: "proved [P] (Lemma J, eps-carries, lambda-carry graph, Lemma R)",
 331: "proved [CA-fp] (Thm A, shells j <= 14, core functional)", 332: "conditional on H1 (Prop. K: H1-shell => H3 with a = a(C); span bound and background interplay P-sketch)",
 333: "conditional on H1 [P-arith] (crossover with all rate budgets: 3307 fragile at C <= 0.082, 1409 robust at C <= 8.8e-4; additive budgets open)",
 335: "proved [P] + [CA-fp] (Lemma C, delta_true(G <= 15) <= 2.2102e-6)", 336: "open hypothesis H1 [H] (re-scoped by N20: H1-bad joint (A,B) second moment + H1-ali)"}
ids = {r['id'] for r in d['after_wave3']}
for k, t in lab.items():
    i = T(k); assert i not in ids and C[i]['source'] == S
    st = C[i]['state']; assert t.split()[0] == st, (i, st, t)
    d['after_wave3'].append({'id': i, 'state': st, 'source': S, 'disposition': H + t + '.' + TAIL})
upd = {
 302: ('proved', "explicit state review open -> proved [P] + [CA-fp] (H4 met by TRACE-326/327/328/335; dependencies 307, 322, 326, 327, 328; title parenthetical '(open, no working route)' -> '(met: BGS-TRACE-326)', ID and statement unchanged; lineN22 E9)."),
 322: ('proved', "explicit state review verification-pending -> proved a fortiori via TRACE-335 (N21 Lemma C, delta_true(G <= 15) <= 2.2102e-6); the N16 method in the title had defects F21-1/F21-3 (lineN22 E11)."),
 323: ('proved', "explicit state review verification-pending -> proved [CA-fp] (values independently recomputed by lineN21b; 20 cells [CA])."),
 299: ('conditional', "state unchanged (conditional); superseded by TRACE-325 (Theorem R#-mod v5)."),
 300: ('open', "state unchanged (open); re-scoped as TRACE-336."),
 301: ('open', "state unchanged (open, not conditional); superseded in substance by TRACE-332 (a = a(C)); not an input of TRACE-325 (lineN22 E10)."),
 318: ('proved', "state unchanged (proved, arithmetic implication in the input delta); 1386/1390/1399 charge delta only and are not the theorem's p1 (see TRACE-333)."),
 206: ('open', "state unchanged (open); Theorem R#-mod v5 (TRACE-325) is a conditional reduction to the open inputs TRACE-336 and TRACE-303..306; no refutation claimed.")}
seen = set()
for r in d['after_wave3']:
    k = int(r['id'][-3:]) if r['id'].startswith('BGS-TRACE-') else None
    if k in upd:
        st, txt = upd[k]; assert C[r['id']]['state'] == st, r['id']
        r['state'] = st; r['disposition'] += ' ' + H + txt; seen.add(k)
assert seen == set(upd), set(upd) - seen
open(P, 'w', encoding='utf-8').write(json.dumps(d, indent=2, ensure_ascii=False) + '\n'); print('epochs', len(d['after_wave3']))
