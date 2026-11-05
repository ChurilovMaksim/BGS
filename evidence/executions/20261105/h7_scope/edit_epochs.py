if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
import json
P='record/claim_integration_epochs.json'; raw=open(P,encoding='utf-8').read(); d=json.loads(raw)
assert json.dumps(d,indent=2,ensure_ascii=False)+'\n'==raw
C={c['id']:c for c in json.load(open('record/claims.json'))['claims']}
T=" Does not close or edit TRACE-305 (H7*, open), TRACE-325 (conditional), TRACE-206 or BGS-001; frozen R' is not refuted."
lab={'BGS-TRACE-344':"proved [P] (7 | K_p and 7 not | h_p for every prime p >= 5, gcd(h_p, K_p) = 1, prime factors of K_p = 1 mod 3; exact check p < 2000; Lean p < 200)",
     'BGS-TRACE-345':"proved [P, finite] (K_p factorisations 5 <= p <= 31; the three crossing conductors and 4663 included, ord = 3p)",
     'BGS-TRACE-346':"proved [CA, finite vertex section only] (sector-0 radii above T' at the three conductors; referee Krawczyk re-enclosure; level-7 calibration against TRACE-223; edge and trace-vs-radius [N]; untruncated operator not claimed)",
     'BGS-TRACE-347':"proved [P on TRACE-346] (scope note: per-orbit sufficient reading of H7* fails on the section; aggregate H7* open; Theorem v5 unaffected; 18 conductors unsearched)"}
ids={r['id'] for r in d['after_wave3']}
for i,t in lab.items():
    assert i not in ids; st=C[i]['state']; assert t.startswith(st)
    d['after_wave3'].append({"id":i,"state":st,"source":C[i]['source'],"disposition":"5 November 2026 (H7* scope integration of PR #85 grok47, hostile referee audit fixes applied): "+t+"."+T})
open(P,'w',encoding='utf-8').write(json.dumps(d,indent=2,ensure_ascii=False)+'\n'); print(len(d['after_wave3']))
