"""Append BGS-TRACE-352..355 to record/claim_integration_epochs.json (after_wave3), as for TRACE-348..351. Run from the repository root."""
if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
import json
P = 'record/claim_integration_epochs.json'; raw = open(P, encoding='utf-8').read(); d = json.loads(raw)
assert json.dumps(d, indent=2, ensure_ascii=False) + '\n' == raw
C = {c['id']: c for c in json.load(open('record/claims.json'))['claims']}
T = (" No existing claim is edited; H5 (TRACE-303) stays open, H6 (TRACE-304) stays open, TRACE-325 stays conditional, nothing is claimed about R' (TRACE-206);"
     " the seam-decay threshold r < 0.418 and every [N]/[H]/[C] item of the source are not registered.")
lab = {'BGS-TRACE-352': "proved [P] (Lemma S on cross lines, referee-corrected scope: bound for every class off the axis sub-line abar_{-sigma}, only sqrt(min(d_+, d_-)) on it; max(d_+, d_-) >= sqrt(h_p) conditional on H6; exhaustive check p = 11, 13, 17 + sampled exact omega=3 at p = 37; Lean partial)",
       'BGS-TRACE-353': "proved [P] (polymer gap lemma with explicit constant K > log_eps min(d_+, d_-) - 2 log_eps A - 1.214; Lean partial)",
       'BGS-TRACE-354': "proved [P] (Binet generator: N(eta_s) = +h_p, (eta_s) is the Binet-line lattice in Z[zeta_p], index 2h in Z[x]/(x^p - 1); exact resultants p <= 73; Lean partial)",
       'BGS-TRACE-355': "conditional (H5(b) cross lines: a uniform |X_line| <= C e^{-cp}, C <= 1, c >= 0.058 fits the idealised V5/TRACE-333 room at p = 1409 and 3307 recomputed on main; the source's 0.048 is wrong; constant [CA])"}
ids = {r['id'] for r in d['after_wave3']}
for i, t in lab.items():
    assert i not in ids; st = C[i]['state']; assert t.startswith(st)
    d['after_wave3'].append({"id": i, "state": st, "source": C[i]['source'],
        "disposition": "5 November 2026 (Lemma S integration from research1105b; only the results confirmed by its independent internal referee, in the referee's corrected statements): " + t + "." + T})
open(P, 'w', encoding='utf-8').write(json.dumps(d, indent=2, ensure_ascii=False) + '\n'); print(len(d['after_wave3']))
