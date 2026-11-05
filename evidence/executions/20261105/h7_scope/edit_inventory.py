if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
import json,hashlib
P='record/claim_verification_inventory.json'; raw=open(P,encoding='utf-8').read(); v=json.loads(raw)
dump=lambda o: json.dumps(o,indent=1,ensure_ascii=False,separators=(',',': ')); assert dump(v)==raw
C={c['id']:c for c in json.load(open('record/claims.json',encoding='utf-8'))['claims']}
F=('title','state','ledger_status','boundary','evidence','verifiers','formalization')
ids={r['id'] for r in v['claims']}
new={'BGS-TRACE-344':dict(methods=['analytic_proof','exact_identity','finite_control','independent_review','lean_formalization'],ledger=['analytic_proof','exact_identity','independent_review'],
        spof='unformalized_analytic_chain',detail='[P] paper proof (Lemmas 3, 4; checked by hand by the hostile referee); exact-integer checks p < 2000 (kp_arith.py, referee ints.py) and the Lean kernel check p < 200 cover finite instances only.'),
     'BGS-TRACE-345':dict(methods=['exact_identity','finite_control','independent_review','lean_formalization'],ledger=['exact_identity','independent_review'],
        spof='NONE',detail='Exact integer computation with two independent implementations (kp_arith.py/h7h8.py and referee ints.py/ints2.py) and a Lean kernel check of the products, residues, divisibility, gcd, floors and orders; primality by BPSW below 2^64 (deterministic) and trial division, not in Lean.'),
     'BGS-TRACE-346':dict(methods=['computer_certificate','independent_review'],ledger=['computer_certificate','independent_review'],
        spof='partial_scope',detail='[CA] on the finite vertex section only (|c| <= 3, 40 modes, |n| <= 16): Newton-Kantorovich (h7_multidisc_cert.py/h7_rates.py, arb error sums) and an independent referee Krawczyk test (krawczyk.py) that shares only build_blocks/assemble; edge comparison, trace-vs-radius and the untruncated operator are not certified.'),
     'BGS-TRACE-347':dict(methods=['analytic_proof','independent_review'],ledger=['analytic_proof','independent_review'],
        spof='unformalized_analytic_chain',detail='Scope reasoning on TRACE-346 and the registered TRACE-305/325 rows (closure condition, infinitely-many-primes hypothesis, p_thr >= 1409); checked by one hostile referee; changes no state.')}
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
