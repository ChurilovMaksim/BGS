"""Add BGS-TRACE-352..355 to record/claim_verification_inventory.json (same procedure as
evidence/executions/20261105/h5_ceiling/edit_inventory.py) and refresh its source blob sha. Run from the repository root."""
if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
import json, hashlib
P = 'record/claim_verification_inventory.json'; raw = open(P, encoding='utf-8').read(); v = json.loads(raw)
dump = lambda o: json.dumps(o, indent=1, ensure_ascii=False, separators=(',', ': ')); assert dump(v) == raw
C = {c['id']: c for c in json.load(open('record/claims.json', encoding='utf-8'))['claims']}
F = ('title', 'state', 'ledger_status', 'boundary', 'evidence', 'verifiers', 'formalization')
ids = {r['id'] for r in v['claims']}
R = 'independent internal referee research1105b (REFEREE.md, evidence/research/20261105_lemma_s/; not external)'
new = {
 'BGS-TRACE-352': dict(methods=['analytic_proof', 'independent_review', 'finite_control', 'lean_formalization'], ledger=['analytic_proof', 'independent_review', 'lean_formalization'],
   spof='unformalized_analytic_chain', detail='[P] paper proof confirmed by the ' + R + '; Lean covers only the height/norm inequalities (Bgs.LemmaSArith), not the ideal-theoretic steps; exhaustive check p = 11, 13, 17 (lemmaS_exact.py, float64 heights); max(d_+, d_-) >= sqrt(h_p) conditional on H6.'),
 'BGS-TRACE-353': dict(methods=['analytic_proof', 'independent_review', 'exact_identity', 'finite_control', 'lean_formalization'], ledger=['analytic_proof', 'independent_review', 'exact_identity', 'lean_formalization'],
   spof='unformalized_analytic_chain', detail='[P] paper proof confirmed by the ' + R + ' (constant made explicit there); Lean proves the norm bound, the logarithmic form and 1.213 < log_eps(eps^2/2) < 1.214, not the Gauss divisibility step; exhaustive small-(A, K) check (polymer_const.py).'),
 'BGS-TRACE-354': dict(methods=['analytic_proof', 'independent_review', 'exact_identity', 'finite_control', 'lean_formalization'], ledger=['analytic_proof', 'independent_review', 'exact_identity', 'lean_formalization'],
   spof='unformalized_analytic_chain', detail='[P] paper proof by the ' + R + '; Lean proves the norm as a product over all conjugates (every odd prime p), not its identification with Algebra.norm or the lattice/index argument; exact resultants p <= 73, all lines p <= 43 (eta_check.py).'),
 'BGS-TRACE-355': dict(methods=['analytic_proof', 'independent_review', 'exact_identity', 'float_numerics', 'conditional_input'], ledger=['independent_review', 'exact_identity', 'float_numerics', 'conditional_input'],
   spof='conditional_on_unproved_input', detail='Conditional on an open uniform cross-line bound |X_line| <= C e^{-cp}; room values copied from an unregistered research note (grok47 h5_factor Prop. 4, PR #85); exact w_max and mpmath thresholds (h5b_const.py), constant corrected by the ' + R + '.'),
}
for i, m in new.items():
    assert i not in ids; c = C[i]
    r = {'id': i, 'title': c['title'], 'state': c['state'], 'ledger_status': c['ledger_status'], 'boundary': c['boundary'], 'methods': m['methods'], 'ledger_claimed_methods': m['ledger'],
         'unevidenced': False, 'adverse_receipt': False, 'receipt_counts': {x: len(c[x]) for x in ('evidence', 'verifiers', 'formalization')},
         'evidence': c['evidence'], 'verifiers': c['verifiers'], 'formalization': c['formalization'], 'spof': m['spof'], 'spof_detail': m['detail'], 'other_weaknesses': [], 'risk_reassessment': 'PENDING_INDEPENDENT_PROOF_REVIEW'}
    v['claims'].append(r)
for r in v['claims']:
    c = C[r['id']]; assert all(r[x] == c[x] for x in F), r['id']
b = open('record/claims.json', 'rb').read(); v['source_blob_sha'] = hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()
open(P, 'w', encoding='utf-8').write(dump(v)); print(v['source_blob_sha'])
