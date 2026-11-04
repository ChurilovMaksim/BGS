#!/usr/bin/env python3
"""Append curated inventory rows for BGS-TRACE-337..341 to record/claim_verification_inventory.json and refresh source_blob_sha."""
import json, hashlib, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[5]
P = ROOT / 'record/claim_verification_inventory.json'; raw = P.read_text(encoding='utf-8'); v = json.loads(raw)
dump = lambda o: json.dumps(o, indent=1, ensure_ascii=False, separators=(',', ': '))
assert dump(v) == raw
C = {c['id']: c for c in json.loads((ROOT / 'record/claims.json').read_text(encoding='utf-8'))['claims']}
order = list([r for r in v['claims'] if r['id'] == 'BGS-TRACE-333'][0].keys())
EN = v['method_enumeration']
A, E, FC, IR, LF, FN, CI = 'analytic_proof', 'exact_identity', 'finite_control', 'independent_review', 'lean_formalization', 'float_numerics', 'conditional_input'
M = {'337': [A, FC, IR, LF], '338': [A, FC, IR], '339': [E, IR, LF], '340': [A, FN, IR, CI], '341': [FN, IR, CI]}
S = {'337': ('unformalized_analytic_chain', 'Paper proof (PR #85 Lemmas 1-6; P2 two-lift upper bound; PR #83 secondary derivation), exact census through shell 16 as a check; Lean checks the eps^4 step only.'),
     '338': ('unformalized_analytic_chain', 'Paper proof of the half-integer/parity step; finite comparison with the production artifacts (production_match.py).'),
     '339': ('single_verifier_implementation_only', 'Exact integer digits (span_census.py) with independent referee census (referee/code/census.py); Lean floor certificates on a window.'),
     '340': ('conditional_on_unproved_input', 'Conditional on hypothesis (M) and the per-site normalisation of A_M; numbers mpmath (crossover_sharp_bi.py), also conditional on H1-bad.'),
     '341': ('conditional_on_unproved_input', 'Conditional on H1-bad (BGS-TRACE-336), BI rows also on (M); mpmath recomputation of the V5 crossover logic, idealised additive terms.')}
ids = {r['id'] for r in v['claims']}
for k in sorted(M):
    i = 'BGS-TRACE-' + k; c = C[i]; assert i not in ids
    meth = [x for x in EN if x in M[k]]
    r = {'id': i, 'title': c['title'], 'state': c['state'], 'methods': meth,
         'ledger_claimed_methods': [x for x in meth if x != LF], 'unevidenced': False, 'adverse_receipt': False,
         'receipt_counts': {x: len(c[x]) for x in ('evidence', 'verifiers', 'formalization')},
         'evidence': c['evidence'], 'verifiers': c['verifiers'], 'formalization': c['formalization'],
         'ledger_status': c['ledger_status'], 'boundary': c['boundary'], 'spof': S[k][0], 'spof_detail': S[k][1],
         'other_weaknesses': [], 'risk_reassessment': 'PENDING_INDEPENDENT_PROOF_REVIEW'}
    assert set(r) == set(order), set(r) ^ set(order)
    assert bool(r['formalization']) == (LF in r['methods']), i
    v['claims'].append({x: r[x] for x in order})
assert {r['id'] for r in v['claims']} == set(C)
b = (ROOT / 'record/claims.json').read_bytes()
v['source_blob_sha'] = hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()
P.write_text(dump(v), encoding='utf-8'); print(v['source_blob_sha'], len(v['claims']))
