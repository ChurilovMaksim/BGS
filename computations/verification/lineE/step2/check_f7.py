"""E11 check (BGS-TRACE-193): Z_{f7}(nu) = Z_{k1}(49 nu), hence F_m(f7) = F_m(k1) iff 49 is a unit mod 2h (3 does not divide m).
Uses Proposition G (exact orbit formula on the support, no n-truncation) in numpy double precision, over ALL units nu.
Independent of cert_class.py's kernel (plain numpy); shares only the exact q-form coefficients routine."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import math, json, numpy as np
from lawlib import mdata
from cert_class import qform
def gvals(kick, eta, h):
    x = 0.5 + np.arange(h)/h
    f = 0.9*np.cos(2*np.pi*x) if kick == 'k1' else 0.9*np.cos(2*np.pi*7*x)
    return np.exp(1j*eta*f)
def allZ2(kick, m, eta):
    d = mdata(m); h = d['h']; a, b, A, B, C = qform(m, h)
    G = gvals(kick, eta, h); z0 = np.arange(h)[:, None]; z1 = np.arange(h)[None, :]
    P = np.ones((h, h), complex)
    for j in range(m): P *= G[(a[j]*z0 + b[j]*z1) % h]
    R = (A*z0*z0 + B*z0*z1 + C*z1*z1) % h
    T = np.bincount(R.ravel(), weights=P.real.ravel(), minlength=h) + 1j*np.bincount(R.ravel(), weights=P.imag.ravel(), minlength=h)
    out = {}
    for nu in range(1, 2*h, 2):
        if math.gcd(nu, h) != 1: continue
        t = pow(16*nu % h, -1, h)
        out[nu] = abs(np.sum(T*np.exp(2j*np.pi*t*np.arange(h)/h)))**2/h**2
    return h, out
for m in (5, 7, 9, 11):
    h, Zk = allZ2('k1', m, 2.0); _, Z7 = allZ2('f7', m, 2.0)
    Fk = np.mean(list(Zk.values())); F7 = np.mean(list(Z7.values()))
    unit49 = math.gcd(49, h) == 1
    dev = max(abs(Z7[nu] - Zk[(49*nu) % (2*h)]) for nu in Z7) if unit49 else None
    rec = dict(m=m, h=h, three_divides_m=(m % 3 == 0), seven_divides_h=(h % 7 == 0), F_k1=Fk, F_f7=F7, rel_F_diff=abs(Fk - F7)/Fk,
               max_abs_Z2_f7_minus_k1_49nu=dev)
    print(json.dumps(rec), flush=True)
    if unit49:
        assert dev < 1e-6*max(Zk.values()) and abs(Fk - F7) < 1e-9*Fk
    else:
        assert abs(Fk - F7) > 1e-3*Fk   # the corollary genuinely needs 3 does not divide m
print('E11 check OK')
