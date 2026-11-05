if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
import json,hashlib
P='record/claim_verification_inventory.json'; raw=open(P,encoding='utf-8').read(); v=json.loads(raw)
dump=lambda o: json.dumps(o,indent=1,ensure_ascii=False,separators=(',',': ')); assert dump(v)==raw
C={c['id']:c for c in json.load(open('record/claims.json',encoding='utf-8'))['claims']}
F=('title','state','ledger_status','boundary','evidence','verifiers','formalization')
ids={r['id'] for r in v['claims']}
L='[P] paper proof re-derived by the integrator (no independent referee); Lean general proof (Bgs.H5CeilingArith, Mathlib, standard axioms only); exact Python checks in h5_arith.py (single implementation).'
new={'BGS-TRACE-348':dict(methods=['analytic_proof','exact_identity','finite_control','lean_formalization'],ledger=['analytic_proof','exact_identity','lean_formalization'],spof='single_reviewer_author_check_only',detail=L),
     'BGS-TRACE-349':dict(methods=['analytic_proof','exact_identity','finite_control','lean_formalization'],ledger=['analytic_proof','exact_identity','lean_formalization'],spof='single_reviewer_author_check_only',detail=L),
     'BGS-TRACE-350':dict(methods=['analytic_proof','exact_identity','finite_control','lean_formalization'],ledger=['analytic_proof','exact_identity','lean_formalization'],spof='single_reviewer_author_check_only',detail=L),
     'BGS-TRACE-351':dict(methods=['analytic_proof','float_numerics','finite_control'],ledger=['analytic_proof','float_numerics'],spof='single_reviewer_author_check_only',
        detail='[P] paper proof re-derived by the integrator (no independent referee); 80-digit mpmath check for odd n <= 301 (h5_arith.py); not formalized.')}
for i,m in new.items():
    assert i not in ids; c=C[i]
    r={'id':i,'title':c['title'],'state':c['state'],'ledger_status':c['ledger_status'],'boundary':c['boundary'],'methods':m['methods'],'ledger_claimed_methods':m['ledger'],
       'unevidenced':False,'adverse_receipt':False,'receipt_counts':{x:len(c[x]) for x in ('evidence','verifiers','formalization')},
       'evidence':c['evidence'],'verifiers':c['verifiers'],'formalization':c['formalization'],'spof':m['spof'],'spof_detail':m['detail'],'other_weaknesses':[],'risk_reassessment':'PENDING_INDEPENDENT_PROOF_REVIEW'}
    v['claims'].append(r)
for r in v['claims']:
    c=C[r['id']]; assert all(r[x]==c[x] for x in F), r['id']
b=open('record/claims.json','rb').read(); v['source_blob_sha']=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
open(P,'w',encoding='utf-8').write(dump(v)); print(v['source_blob_sha'])
