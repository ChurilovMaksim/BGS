"""Independent arithmetic cross-check of the m = 17 evidence (written for this PR; reads only files in this folder and
the repository). Exact rationals; every float read from a log is widened by a relative 1e-15 (1-ulp safety for float
printing of arb endpoints). It does NOT recompute any class sum or certificate; it checks the bookkeeping.
Run from the repository root: python3 evidence/executions/20261031/m17/check/m17_crosscheck.py"""
import json, hashlib
from fractions import Fraction as Fr
D = 'evidence/executions/20261031/m17/'
ok = True
def chk(name, cond):
    global ok; ok &= bool(cond); print(('PASS ' if cond else 'FAIL ') + name)
W = Fr(1, 10**15)
lo = lambda x: Fr(x) * (1 - W) if x > 0 else Fr(x) * (1 + W)
hi = lambda x: Fr(x) * (1 + W) if x > 0 else Fr(x) * (1 - W)
cert = json.loads(open(D + 'lineE/cert_m17_full.out').read())
lines = [json.loads(l) for l in open(D + 'lineE/cert_class.jsonl')]
chk('cert_m17_full.out equals the m = 17 line of cert_class.jsonl', lines[-1] == cert)
repo = [json.loads(l) for l in open('computations/verification/lineE/step2/cert_class.jsonl')]
chk('m = 5..13 lines identical to the repository certificate file', lines[:-1] == repo)
m, h, phi = cert['m'], cert['h'], cert['phi_2h']
chk('h_17 = 1607521 = 103 * 15607 and phi(2h) = 102 * 15606', h == 1607521 == 103 * 15607 and phi == 102 * 15606)
a, b = 1, 1
for _ in range(m - 1): a, b = a + 2 * b, a + b   # (1+sqrt2)^k = a + b sqrt2
print('   (1+sqrt2)^17 = %d + %d sqrt2' % (a, b))
chk('h_17 equals the rational part of (1+sqrt2)^17', h == a)
res = {r['N_mod_h']: r for r in cert['residues']}
chk('residues are exactly N = -196, +196', sorted(res) == [-196, 196])
for N, r in res.items():
    chk('N=%d: Z2_lower <= Z2_float <= Z2_upper' % N, r['Z2_lower'] <= r['Z2_float'] <= r['Z2_upper'])
    S2 = Fr(r['S'][0]) ** 2 + Fr(r['S'][1]) ** 2
    print('   N=%d: |S|^2/h^2 = %.9e, enclosure width %.3g' % (N, float(S2 / h**2), r['Z2_upper'] - r['Z2_lower']))
F_lo = (lo(res[-196]['Z2_lower']) + lo(res[196]['Z2_lower'])) / phi   # F_m >= (1/phi) sum over the two residues (all terms >= 0)
print('   F_17 lower (recomputed, exact) = %.10f' % float(F_lo))
chk('F_17/2m >= 23.4893 (claimed in this PR, rounded down)', F_lo / (2 * m) >= Fr(234893, 10**4))
chk('W~rest_17/m = (F - 4m)/m >= 42.9787 (claimed, rounded down)', (F_lo - 4 * m) / m >= Fr(429787, 10**4))
chk('hence |W~rest_17(2)| > 17', F_lo - 4 * m > m)
chk('recomputed values agree with the certificate record', abs(float(F_lo) - cert['F_lower']) < 1e-9 * cert['F_lower'])
# Line E pre-registered predictions (predictions.jsonl, 2026-10-30 06:41 UTC)
pred = {(p['m'], p['N_mod_h']): p['Z2_pred'] for p in map(json.loads, open('computations/verification/lineE/step2/predictions.jsonl'))}
for mm in (11, 13, 17):
    L = [l for l in lines if l['m'] == mm and l['kick'] == 'full'][0]
    for r in L['residues']:
        if abs(r['N_mod_h']) == 196:
            dev = (pred[(mm, r['N_mod_h'])] - r['Z2_float']) / r['Z2_float']
            inside = r['Z2_lower'] <= pred[(mm, r['N_mod_h'])] <= r['Z2_upper']
            print('   m=%d N=%+d: predicted %.6e, certified [%.9e, %.9e], rel. deviation %+.2e, inside enclosure: %s'
                  % (mm, r['N_mod_h'], pred[(mm, r['N_mod_h'])], r['Z2_lower'], r['Z2_upper'], dev, inside))
# Line G float class sums (independent code path: orbit class sums Torb_full_m17.bin, eval17.py)
log = open(D + 'lineG/eval17_full.log').read()
import re
obs = {(int(s), int(d)): float(v) for s, d, v in re.findall(r'full \((-?\d+),(\d+)\) observed ([0-9.e+]+)', log)}
chk('Line G float |Z|^2 at (2,392) lies in the certified N = +196 enclosure', res[196]['Z2_lower'] <= obs[(2, 392)] <= res[196]['Z2_upper'])
chk('Line G float |Z|^2 at (-2,392) lies in the certified N = -196 enclosure', res[-196]['Z2_lower'] <= obs[(-2, 392)] <= res[-196]['Z2_upper'])
ev = json.load(open(D + 'lineG/eval17_full.json'))
tests = {k: v for k, v in ev.items() if isinstance(v, dict) and 'ok' in v}
chk('Line G full-kick evaluation: %d registered tests, all PASS' % len(tests), len(tests) == 6 and all(v['ok'] and v['lo'] <= v['obs'] <= v['hi'] for v in tests.values()))
chk('Line G total F/2m (float, 25.7986) >= certified lower bound', ev['F2m'] >= float(F_lo / (2 * m)))
psha = hashlib.sha256(open('computations/verification/lineG/PREDICTIONS_m17.json', 'rb').read()).hexdigest()
chk('PREDICTIONS_m17.json in the repository has the pre-registered sha256 fa8505f5...aa344', psha.startswith('fa8505f5') and psha.endswith('aa344') and psha in log)
ft = json.load(open(D + 'lineG/formula_table_full_17.json'))[0]
chk('formula table F2m equals eval F2m to relative 1e-12 (two float summations)', abs(ft['F2m'] - ev['F2m']) < 1e-12 * ev['F2m'])
print('ALL_OK' if ok else 'SOME_FAIL')
