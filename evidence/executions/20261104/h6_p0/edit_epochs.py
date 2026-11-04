import json
P='record/claim_integration_epochs.json'; raw=open(P,encoding='utf-8').read(); d=json.loads(raw)
assert json.dumps(d,indent=2,ensure_ascii=False)+'\n'==raw
C={c['id']:c for c in json.load(open('record/claims.json'))['claims']}
T=" Does not close TRACE-206, TRACE-148, TRACE-304 or BGS-001; frozen R' is not refuted."
lab={'BGS-TRACE-337':"proved [P] (Lemma W; referee audit/p4 CONFIRMED)",
     'BGS-TRACE-338':"conditional [P + CA] (explicit H6/Theorem C' threshold 8V p0 = 28,424,695, 8E p0 = 3,934; mod u = 1, h_p squarefree, inherited N4/N2 constants; referee audit/p4 fixes 1-6 applied)"}
ids={r['id'] for r in d['after_wave3']}
for i,t in lab.items():
    assert i not in ids; st=C[i]['state']; assert t.startswith(st)
    d['after_wave3'].append({"id":i,"state":st,"source":C[i]['source'],"disposition":"4 November 2026 (P4 v2, H6 explicit p0 and Lemma W): "+t+"."+T})
open(P,'w',encoding='utf-8').write(json.dumps(d,indent=2,ensure_ascii=False)+'\n'); print(len(d['after_wave3']))
