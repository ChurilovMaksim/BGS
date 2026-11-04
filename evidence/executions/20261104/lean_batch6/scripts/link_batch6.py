"""Integrator script (Lean batch 6, 2026-11-04). Run once from the repository root.

Extends the Lean links (`formalization`), the `formalization_scope` sentence and the batch receipt (`evidence`) of
BGS-TRACE-213 and mirrors the row into record/claim_verification_inventory.json, following
evidence/executions/20261101/lean_batch5/scripts/link_batch5.py. No claim state and no boundary is changed."""
import json, hashlib
F = 'formalization/Bgs/'
RECEIPT = 'evidence/executions/20261104/lean_batch6/README.md'
LINKS = {
 'BGS-TRACE-213': ([F + 'LineIReduction.lean', F + 'LineI213Disjoint.lean'],
   'Partial: the exact identity W\'_m = phi^-1 sum_{nu unit, not resonant} (|Z_nu|^2 - RMT_m) + phi^-1 sum_{rho, d incl.} '
   'Dev_d(rho), Dev_d(rho) = sum_{nu in M_d(rho)} (|Z_nu|^2 - |Z_rho|^2/d^2), from the frozen definitions of F_m, Res_m and '
   'W\'_m (LineIReduction), and the pairwise disjointness of the classes {nu_rho} and the member sets M_d(rho) (rho in P*, '
   'levels d | h with d^2 <= h, nu_rho the d = 1 case) derived from the congruence definition for h > 1 with h^2 + 1 = 2y^2 '
   '(LineI213Disjoint: same rho via gcd(d, d\'), different rho via h odd and 3 not dividing h; reduction_congr gives the '
   'identity with the member sets defined by the congruences). Not formalized: the sufficiency (E\'\'), (T\'\'), (D) => R\' '
   '(the o(m) and diagonal arguments).'),
}
CP = 'record/claims.json'; raw = open(CP, encoding='utf-8').read(); d = json.loads(raw)
assert json.dumps(d, indent=2, ensure_ascii=False) + '\n' == raw
by = {c['id']: c for c in d['claims']}
for i, (files, scope) in LINKS.items():
    c = by[i]; assert c['state'] in ('proved', 'conditional'), i
    old = c['formalization']; assert old == files[:len(old)], i
    for f in files: open(f).close()
    c['formalization'] = files
    c['formalization_scope'] = scope
    if RECEIPT not in c['evidence']: c['evidence'].append(RECEIPT)
open(CP, 'w', encoding='utf-8').write(json.dumps(d, indent=2, ensure_ascii=False) + '\n')
P = 'record/claim_verification_inventory.json'; raw = open(P, encoding='utf-8').read(); v = json.loads(raw)
dump = lambda o: json.dumps(o, indent=1, ensure_ascii=False, separators=(',', ': ')); assert dump(v) == raw
EN = v['method_enumeration']; LF = 'lean_formalization'
seen = set()
for r in v['claims']:
    if r['id'] not in LINKS: continue
    seen.add(r['id']); c = by[r['id']]
    for x in ('boundary', 'evidence', 'verifiers', 'formalization'): r[x] = c[x]
    r['receipt_counts'] = {x: len(c[x]) for x in ('evidence', 'verifiers', 'formalization')}
    meth = set(r['methods']) - {'unevidenced'} | {LF}
    r['methods'] = [x for x in EN if x in meth]
    r['unevidenced'] = c['state'] == 'open' or not any(c[k] for k in ('evidence', 'verifiers', 'formalization'))
assert seen == set(LINKS), set(LINKS) - seen
v['caveats'].append('4 November 2026 (Lean batch 6, evidence/executions/20261104/lean_batch6/README.md): Lean file '
    'LineI213Disjoint appended to BGS-TRACE-213 (disjointness of nu_rho and M_d(rho) from the congruence definition); the '
    'link stays partial as stated in formalization_scope. No state changed.')
b = open(CP, 'rb').read(); v['source_blob_sha'] = hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()
open(P, 'w', encoding='utf-8').write(dump(v)); print('linked', sorted(LINKS), v['source_blob_sha'])
