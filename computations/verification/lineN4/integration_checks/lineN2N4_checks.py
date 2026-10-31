#!/usr/bin/env python3
"""Lines N2-N4 integration: every registered number is recomputed from the committed logs (mpmath, 30 digits) and checked to be a valid
upward rounding (bounds) or below the target (rates). Registered: BGS-TRACE-290 (r_2), 295 (Lambda), 296 (rates, margins)."""
import json, os
from mpmath import mp, mpf, cbrt
mp.dps = 30
H = os.path.dirname(os.path.abspath(__file__)); V = os.path.join(H, '..', '..')
ok = True
def chk(name, cond, info=''):
    global ok; ok &= bool(cond); print(('OK  ' if cond else 'FAIL'), name, info)
r2 = {}
for l in open(os.path.join(V, 'lineN2', 'logs', 'e_r2_cert.jsonl')):
    j = json.loads(l)
    if j['k'] == 4000: r2[j['fam']] = mpf(repr(j['r2_upper']))
REG_R2 = {'8V': '1.0529012', '8E': '1.0519234', '16V': '1.0534557', '16E': '1.0529202'}
for f, s in REG_R2.items(): chk(f'r2(4000) {f} <= {s}', r2[f] <= mpf(s), f'(log {r2[f]})')
b16 = json.load(open(os.path.join(V, 'lineN4', 'logs', 'b16_final.json')))
lam = {'8V': mpf(repr(json.load(open(os.path.join(V, 'lineN4', 'logs', 'b8V_final.json')))['Lambda_free_upper'])),
       '8E': mpf(repr(json.load(open(os.path.join(V, 'lineN4', 'logs', 'b8E_final.json')))['Lambda_free_upper'])),
       '16V': max(mpf(repr(b16[k]['Lambda_free_upper'])) for k in ('V_P0', 'V_P1')),
       '16E': max(mpf(repr(b16[k]['Lambda_free_upper'])) for k in ('E_P0', 'E_P1'))}
REG_L = {'8V': '1.9656353', '8E': '0.4915932', '16V': '2.9413897', '16E': '0.4474396'}
for f, s in REG_L.items(): chk(f'Lambda {f} <= {s}', lam[f] <= mpf(s), f'(log {lam[f]})')
chk('I-1: author 16V value 2.9413896 is below the certified bound', lam['16V'] > mpf('2.9413896'), f'({lam["16V"]})')
T = {'8V': mpf('1.28359'), '8E': mpf('1.28359'), '16V': mpf('1.4742'), '16E': mpf('1.4742')}
REG_RATE = {'8V': '1.27438', '8E': '0.80266', '16V': '1.45789', '16E': '0.77812'}
for f in REG_L:
    rate = cbrt(mpf(REG_L[f]) * mpf(REG_R2[f]))
    chk(f'rate {f} = {rate:.10f} <= {REG_RATE[f]} < T', rate <= mpf(REG_RATE[f]) < T[f])
    chk(f'threshold {f}: Lambda < T^3/r2', mpf(REG_L[f]) < T[f] ** 3 / mpf(REG_R2[f]), f'({T[f]**3/mpf(REG_R2[f])})')
chk('delta 8V >= 0.0071', 1 - mpf('1.27438') / T['8V'] >= mpf('0.0071'))
chk('delta 16V >= 0.011', 1 - mpf('1.45789') / T['16V'] >= mpf('0.011'))
lmb = 3 + 2 * mp.sqrt(2); mus = mpf('1.9154752')
chk('slow orbit (mu*^3/lambda)^{1/3} <= 1.0644', cbrt(mus ** 3 / lmb) <= mpf('1.0644'), f'({cbrt(mus**3/lmb)})')
chk('Green kernel sum = 1/4', abs((lmb + 1) / ((lmb - 1) * (lmb - 1 / lmb)) - mpf(1) / 4) < mpf(10) ** -25)
sq = json.load(open(os.path.join(V, 'lineN4', 'logs', 'd_squarefree_3000000_100000.json')))
chk('d_squarefree: no square hits ([N] evidence only)', sq['square_hits'] == [] and sq['QMAX'] == 3000000 and sq['PMAX'] == 100000, f"({sq['n_pairs']} pairs)")
print('LINE_N2N4_CHECKS_OK' if ok else 'LINE_N2N4_CHECKS_FAIL'); raise SystemExit(0 if ok else 1)
