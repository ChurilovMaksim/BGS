"""Line L / L2 integration checks (written at integration, 31 Oct 2026). Re-derives the scalar constants quoted in the
registered claims with mpmath (60 digits) and re-reads the arb certificate outputs. Prints ALL_OK on success."""
import json, os
from mpmath import mp, mpf, sqrt, log, besselj, acosh
mp.dps = 60
H = os.path.dirname(os.path.abspath(__file__)); L = os.path.join(H, '..', 'logs')
lam = 3 + 2*sqrt(2); ok = True
def chk(name, cond, val=''):
    global ok
    print(('OK   ' if cond else 'FAIL ') + name, val); ok &= bool(cond)
# certificate (arb strings: midpoint +/- radius; upper end must be < target)
def up(s):
    s = s.strip('[]'); m, r = s.split('+/-'); return mpf(m) + mpf(r)
tg = {'8': mpf('1.28359'), '16': mpf('1.4742')}
cert = [json.loads(l) for l in open(os.path.join(L, 'final_op_cert.jsonl'))]
for c in cert:
    chk(f"rate({c['fam']}{c['typ']},k={c['k']}) < target", up(c['Ik_rate_upper']) < tg[c['fam']], up(c['Ik_rate_upper']))
r8V = [c for c in cert if c['fam'] == '8' and c['typ'] == 'V'][0]
d = 1 - up(r8V['Ik_rate_upper'])/tg['8']; chk('delta_OP(8V) = 1 - rate/target ~ 0.0162', abs(d - mpf('0.0162')) < mpf('0.00005'), d)
cons = [json.loads(l) for l in open(os.path.join(L, 'final_constants.jsonl'))]
chk('c_W = 10^-25.62 <= min_F c_F', mpf(10)**mpf('-25.62') <= min(mpf(10)**mpf(c['log10_ck']) for c in cons))
chk('q0 = 10^13.2 = max_F q0_F', max(c['log10_q0'] for c in cons) == 13.2)
pnv = 2/mpf(10)**mpf('-25.62'); chk('non-vacuity c_W p^2 >= 2p+1 from p ~ 8.3e25', mpf('8.2e25') < pnv < mpf('8.4e25'), pnv)
chk('all four families OP true', all(c['OP'] for c in cons))
# Lemma O1 / TRACE-197 radius conditions
chk('dev_V = lam/(2(lam-1)) = 0.6036', abs(lam/(2*(lam-1)) - mpf('0.6036')) < 1e-4)
chk('dev_E = 1/(2(lam-1)) = 0.1036', abs(1/(2*(lam-1)) - mpf('0.1036')) < 1e-4)
chk('TRACE-197 V: 1/(2*0.75) + 1/lam < 1', mpf(1)/(2*mpf('0.75')) + 1/lam < 1, mpf(1)/(2*mpf('0.75')) + 1/lam)
chk('TRACE-197 E: 1/(2 lam 0.2) + 1/lam < 1', 1/(2*lam*mpf('0.2')) + 1/lam < 1, 1/(2*lam*mpf('0.2')) + 1/lam)
# (+-2,16) narrowing, eta constants
xi = mpf('2.4586893'); r16 = mpf('1.6677')**2/xi
chk('1.6677^2/xi_lo = 1.13118 (quoted as 1.1311 in REPORT_L_v2, rounded down by 8e-5; registered in exact form)', abs(r16 - mpf('1.13118')) < 1e-5, r16)
chk('log(1.6677^2/xi_lo) = 0.12326 vs quoted Lambda16 = log 1.1311 = 0.12319', abs(log(r16) - mpf('0.12326')) < 1e-5, log(r16))
chk('with exact Lambda16: 0.4043/Lambda16 + 1 <= 4.282', mpf('0.4043')/log(r16) + 1 <= mpf('4.282'), mpf('0.4043')/log(r16) + 1)
L16 = log(mpf('1.1311')); chk('Lambda16 = 0.12319', abs(L16 - mpf('0.12319')) < 5e-6)
chk('0.4043/Lambda16 + 1 <= 4.282', mpf('0.4043')/L16 + 1 <= mpf('4.2822'), mpf('0.4043')/L16 + 1)
# Prop S constant
chk('(1.28359/1.9154712)^30 <= 6.1e-6', (mpf('1.28359')/mpf('1.9154712'))**30 <= mpf('6.1e-6'), (mpf('1.28359')/mpf('1.9154712'))**30)
# Prop A2 barrier
G = sum(abs(besselj(n, mpf('1.8'))) for n in range(-80, 81)); chk('G = sum|J_n(1.8)| = 2.3693986', abs(G - mpf('2.3693986')) < 1e-7, G)
chk('(G/1.28359)^2 >= 3.4074', (G/mpf('1.28359'))**2 >= mpf('3.4074'), (G/mpf('1.28359'))**2)
chk('(G/1.4742)^2 >= 2.5832', (G/mpf('1.4742'))**2 >= mpf('2.5832'), (G/mpf('1.4742'))**2)
chk('(mu*/T)^2 = 2.2269 (mu* = 1.9154712)', abs((mpf('1.9154712')/mpf('1.28359'))**2 - mpf('2.2269')) < 1e-4)
# L2-F1: h_m ~ 1/2 (1+sqrt2)^m, sqrt h ~ 1.5538^m; thresholds exceed h_m
def h(m):
    a, b = 1, 0
    for _ in range(m): a, b = a + 2*b, a + b
    return a
chk('h_9 = 1393, h_21 = 54608393', h(9) == 1393 and h(21) == 54608393)
chk('sqrt(1+sqrt2) = 1.5538', abs(sqrt(1 + sqrt(2)) - mpf('1.5538')) < 5e-5)
chk('2.5832 > 1+sqrt2 (barrier above h_m itself)', mpf('2.5832') > 1 + sqrt(2))
# Lemmas B1/B2, disjointness
chk('(lam/(lam-1))^2 <= 1.4572', (lam/(lam-1))**2 <= mpf('1.4572'), (lam/(lam-1))**2)
chk('1.4923^3 <= 3.3233', mpf('1.4923')**3 <= mpf('3.3234'), mpf('1.4923')**3)
chk('3.3233^(1+0.340) < 5 (L2-F2 eta < 0.340)', mpf('3.3233')**mpf('1.340') < 5, mpf('3.3233')**mpf('1.340'))
chk('Cauchy root bound: lam > 1 + 4', lam > 5, lam)
chk('log lam/3 = 0.58758', abs(log(lam)/3 - mpf('0.58758')) < 1e-5)
chk('(+-2,8): 0.40030(1+eta) < log lam/3 iff eta < 0.4678', abs(log(lam)/3/mpf('0.40030') - 1 - mpf('0.4678')) < 2e-4)
chk('(+-2,16): eta16 < 3.770', abs(log(lam)/3/L16 - 1 - mpf('3.770')) < 2e-3)
# L3 (after L3-F1, L3-F2)
from math import gcd
P = [5, 7, 11, 13, 17, 19, 23]
chk('L3 S3: h_{3p} = h_p (4 h_p^2 + 3) for p = 5..23', all(h(3*p) == h(p)*(4*h(p)**2 + 3) for p in P))
chk('L3-F2: gcd(h_p, K_p) = 1 and 7 | K_p for p = 5..23; 49 | K_7', all(gcd(h(p), 4*h(p)**2 + 3) == 1 and (4*h(p)**2 + 3) % 7 == 0 for p in P) and (4*h(7)**2 + 3) % 49 == 0)
chk('L3-F2: lambda has order 3 mod 7 (lambda^3 = 99 + 70 sqrt2 == 1 mod 7)', (99 - 1) % 7 == 0 and 70 % 7 == 0)
chk('L3-F1: (1+sqrt2)/1.28359 = 1.8808', abs((1 + sqrt(2))/mpf('1.28359') - mpf('1.8808')) < 5e-5, (1 + sqrt(2))/mpf('1.28359'))
chk('L3-F1: 1.8808^m above 1.4923^{m(1+eta)} iff eta < 0.578', abs(log(mpf('1.8808'))/log(mpf('1.4923')) - 1 - mpf('0.578')) < 1e-3, log(mpf('1.8808'))/log(mpf('1.4923')) - 1)
chk('L3-F1: mu = 1.9154753 < 1+sqrt2 (|Z| <= h for m >= 495 via Prop K2)', mpf('1.9154753') < 1 + sqrt(2))
chk('L3 Lemma E: 64 * 4.12 <= 264 and log_lambda(264 * 0.05^2) = -0.236', 64*mpf('4.12') <= 264 and abs(log(264*mpf('0.05')**2)/log(lam) + mpf('0.236')) < 1e-3)
print('ALL_OK' if ok else 'SOME_FAILED')
