import json,hashlib
P='record/claim_verification_inventory.json'; raw=open(P,encoding='utf-8').read(); v=json.loads(raw)
dump=lambda o: json.dumps(o,indent=1,ensure_ascii=False,separators=(',',': ')); assert dump(v)==raw
C={c['id']:c for c in json.load(open('record/claims.json',encoding='utf-8'))['claims']}
F=('title','state','ledger_status','boundary','evidence','verifiers','formalization')
ids={r['id'] for r in v['claims']}
new={'BGS-TRACE-337':dict(methods=['analytic_proof','computer_certificate','independent_review','lean_formalization'],ledger=['analytic_proof','computer_certificate','independent_review'],
        spof='single_verifier_implementation_only',detail='[P] paper proof (verified line by line, referee audit/p4); [N] exact trial division q < 1e8 (lemmaW_trial.py) and referee big-int replay (lw.py); Lean checks the divisor classes at p <= 13 and p, 2 not dividing h_p for p < 100 only.'),
     'BGS-TRACE-338':dict(methods=['computer_certificate','independent_review','conditional_input'],ledger=['computer_certificate','independent_review','conditional_input'],
        spof='conditional_on_unproved_input',detail='[P + CA] arb interval cover + analytic tail (h6_p0.py, restart-on-failure), referee mpmath replay (indep.py); conditional on u = 1 in (C1), h_p squarefree and inherited N4/N2 [CA] constants; 8V/8E only.')}
for i,m in new.items():
    assert i not in ids; c=C[i]
    r={'id':i,'title':c['title'],'state':c['state'],'ledger_status':c['ledger_status'],'boundary':c['boundary'],'methods':m['methods'],'ledger_claimed_methods':m['ledger'],
       'unevidenced':False,'adverse_receipt':False,'receipt_counts':{x:len(c[x]) for x in ('evidence','verifiers','formalization')},
       'evidence':c['evidence'],'verifiers':c['verifiers'],'formalization':c['formalization'],'spof':m['spof'],'spof_detail':m['detail'],'other_weaknesses':[],'risk_reassessment':'PENDING_INDEPENDENT_PROOF_REVIEW'}
    v['claims'].append(r)
for r in v['claims']:
    c=C[r['id']]; assert all(r[x]==c[x] for x in F), r['id']
order=[c['id'] for c in json.load(open('record/claims.json'))['claims']]
b=open('record/claims.json','rb').read(); v['source_blob_sha']=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
open(P,'w',encoding='utf-8').write(dump(v)); print(v['source_blob_sha'])
