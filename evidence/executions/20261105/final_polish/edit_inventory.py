"""Sync the BGS-CAYLEY-002 boundary in record/claim_verification_inventory.json with record/claims.json
(final polish wording sync) and refresh its source blob sha. Same procedure as
evidence/executions/20261105/lemma_s/edit_inventory.py. Run from the repository root."""
if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
import json, hashlib
P = 'record/claim_verification_inventory.json'; raw = open(P, encoding='utf-8').read(); v = json.loads(raw)
dump = lambda o: json.dumps(o, indent=1, ensure_ascii=False, separators=(',', ': ')); assert dump(v) == raw
C = {c['id']: c for c in json.load(open('record/claims.json', encoding='utf-8'))['claims']}
F = ('title', 'state', 'ledger_status', 'boundary', 'evidence', 'verifiers', 'formalization')
changed = []
for r in v['claims']:
    c = C[r['id']]
    for x in F:
        if r[x] != c[x]:
            assert r['id'] == 'BGS-CAYLEY-002' and x == 'boundary', (r['id'], x)
            r[x] = c[x]; changed.append((r['id'], x))
assert changed == [('BGS-CAYLEY-002', 'boundary')], changed
for r in v['claims']:
    c = C[r['id']]; assert all(r[x] == c[x] for x in F), r['id']
b = open('record/claims.json', 'rb').read(); v['source_blob_sha'] = hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()
open(P, 'w', encoding='utf-8').write(dump(v)); print(changed, v['source_blob_sha'])
