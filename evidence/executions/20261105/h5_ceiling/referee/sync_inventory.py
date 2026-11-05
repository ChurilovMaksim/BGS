"""Mirror the referee-updated ledger_status of BGS-TRACE-348..351 from record/claims.json into
record/claim_verification_inventory.json and refresh its source blob sha (same procedure as ../edit_inventory.py).
spof classes are not changed; only the stale '(no independent referee)' wording in spof_detail is updated."""
if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
import json, hashlib
P = 'record/claim_verification_inventory.json'; raw = open(P, encoding='utf-8').read(); v = json.loads(raw)
dump = lambda o: json.dumps(o, indent=1, ensure_ascii=False, separators=(',', ': ')); assert dump(v) == raw
C = {c['id']: c for c in json.load(open('record/claims.json', encoding='utf-8'))['claims']}
F = ('title', 'state', 'ledger_status', 'boundary', 'evidence', 'verifiers', 'formalization')
OLD = '(no independent referee)'
NEW = '(independent internal referee audit afterwards, 2026-11-05: evidence/executions/20261105/h5_ceiling/referee/AUDIT.md; not external)'
for r in v['claims']:
    if r['id'] in ('BGS-TRACE-348', 'BGS-TRACE-349', 'BGS-TRACE-350', 'BGS-TRACE-351'):
        r['ledger_status'] = C[r['id']]['ledger_status']
        assert r['spof_detail'].count(OLD) == 1; r['spof_detail'] = r['spof_detail'].replace(OLD, NEW)
for r in v['claims']:
    c = C[r['id']]; assert all(r[x] == c[x] for x in F), r['id']
b = open('record/claims.json', 'rb').read(); v['source_blob_sha'] = hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()
open(P, 'w', encoding='utf-8').write(dump(v)); print(v['source_blob_sha'])
