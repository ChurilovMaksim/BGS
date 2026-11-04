"""Integrator script (Lean batch 6b, 2026-11-04). Run once from the repository root.

Appends the batch-6b Lean files to `formalization`, rewrites `formalization_scope` and adds the batch receipt (`evidence`)
for BGS-TRACE-214 and BGS-TRACE-218 only, and mirrors those rows (boundary, evidence, verifiers, formalization) into the
curated record/claim_verification_inventory.json, following evidence/executions/20261101/lean_batch5/scripts/link_batch5.py.
No claim state is changed; no sealed or frozen row is touched; no other row is edited."""
import json, hashlib
F = 'formalization/Bgs/'
RECEIPT = 'evidence/executions/20261104/lean_batch6b/README.md'
LINKS = {
 'BGS-TRACE-214': ([F + 'LineIHorocycle.lean', F + 'LineIHorocycleSummable.lean'],
   'Full for the two identities: for every kick with sum |Phihat| < infinity (finite support in LineIHorocycle, '
   'infinite support with absolutely convergent pair series in LineIHorocycleSummable) and weights f(z_nu) = sum_k c_k '
   'e(k nu/M) with sum |c_k| < infinity: (a) sum_{nu mod M} |Z_nu|^2 f(z_nu) = M sum_k c_k C(k), C(k) = sum_{n,n\'} '
   'Phihat(n) conj Phihat(n\') 1[P(n) - P(n\') == k mod M], and (b) sum_{nu unit} |Z_nu|^2 f(z_nu) = sum_k c_k sum_{n,n\'} '
   'Phihat(n) conj Phihat(n\') c_M(k - P(n) + P(n\')), c_M the Ramanujan sum. Not formalized (not identities of the claim): '
   'the remarks on the diagonal class and on the R\' use.'),
 'BGS-TRACE-218': ([F + 'LineIAliasing.lean', F + 'LineIMoebius.lean', F + 'LineISummable.lean', F + 'LineIRegroup.lean',
                    F + 'LineIMoebiusSummable.lean', F + 'LineIRegroupSummable.lean'],
   'Full for the two identities: for every q >= 1, (1/q) sum_{nu mod q} |Z_m(nu/q)|^2 = sum_{j in Z} C_Z(j q), and F_m = '
   'phi(2h)^-1 sum_{e | 2h} mu(e) (2h/e) sum_{j in Z} C_Z(j 2h/e), for finite support (LineIAliasing, LineIMoebius, '
   'LineIRegroup) and for every kick with sum |Phihat| < infinity, C_Z(k) then an absolutely convergent pair series '
   '(LineISummable, LineIMoebiusSummable, and the regrouping of the pair series into sum_j C_Z in LineIRegroupSummable). '
   'Not formalized: the heuristic assessment, which is not part of the claim.'),
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
v['caveats'].append('4 November 2026 (Lean batch 6b, evidence/executions/20261104/lean_batch6b/README.md): Lean files '
    'LineIHorocycleSummable and LineIRegroupSummable appended to BGS-TRACE-214 and BGS-TRACE-218 (summable, infinite-support '
    'kicks); coverage as stated in formalization_scope. No state changed.')
b = open(CP, 'rb').read(); v['source_blob_sha'] = hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()
open(P, 'w', encoding='utf-8').write(dump(v)); print('linked', sorted(LINKS), v['source_blob_sha'])
