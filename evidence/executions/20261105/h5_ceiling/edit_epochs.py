if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
import json
P='record/claim_integration_epochs.json'; raw=open(P,encoding='utf-8').read(); d=json.loads(raw)
assert json.dumps(d,indent=2,ensure_ascii=False)+'\n'==raw
C={c['id']:c for c in json.load(open('record/claims.json'))['claims']}
T=" Does not edit TRACE-342 (Lemma W, remains true) and does not close or edit TRACE-303 (H5, open), TRACE-325 (conditional), TRACE-206 or BGS-001; nothing is claimed about R'."
lab={'BGS-TRACE-348':"proved [P] (Lemma W sharpened: q | h_p implies q = 1 mod 2p and q = +-1 mod 8; Lean general proof; exact check q < 1e7, p <= 1500, no presieve)",
     'BGS-TRACE-349':"proved [P] (gcd(h_p, h_p') = 1 for distinct odd primes; Lean general proof; exact check of all pairs p < p' <= 1500)",
     'BGS-TRACE-350':"proved [P] (p = 3 mod 4 and 2p + 1 prime imply 2p + 1 | h_p and least prime factor 2p + 1; Lean general proof; 25 such p in [5, 1500])",
     'BGS-TRACE-351':"proved [P] (h_n = prod (6 - 2 cos(2 pi k/n)) for odd n; 80-digit check n <= 301; not in Lean)"}
ids={r['id'] for r in d['after_wave3']}
for i,t in lab.items():
    assert i not in ids; st=C[i]['state']; assert t.startswith(st)
    d['after_wave3'].append({"id":i,"state":st,"source":C[i]['source'],"disposition":"5 November 2026 (H5 structural-ceiling arithmetic from research1105, re-derived and re-checked at integration; no independent referee): "+t+"."+T})
open(P,'w',encoding='utf-8').write(json.dumps(d,indent=2,ensure_ascii=False)+'\n'); print(len(d['after_wave3']))
