"""Certified |Z_m(nu)| at the resonant residues N == -+196 (and -+4) for the Line B diagonal kick (and sub-kicks), via
   |Z_m(nu)| = h^{-1} | sum_{z q-seq mod h} e(t R(z)/h) prod_j g(1/2 + z_j/h) |,   t = (16 nu)^{-1} mod h,   R(z) = 2 z^T H z / h mod h,
(Proposition G of step2/PROOF_G.md, from TRACE-163 Theorem 3 + Prop R + TRACE-165 Lemma S).  Tables in arb, kernel zres.c in IEEE double
with an a-priori rounding bound.  Output: rigorous lower/upper bounds for |Z(nu)|^2, F_m >= sum|Z|^2/phi(2h), W~rest >= F - 4m.
usage: cert_class.py kick m eta offsets(e.g. 196,-196) [threads]"""
import sys, os, json, math, time, subprocess, random
from fractions import Fraction as Fr
from flint import arb, acb, ctx
from lawlib import pell, mdata
HERE = os.path.dirname(os.path.abspath(__file__))
def rC(k): return {0:Fr(1),1:Fr(1,2),-1:Fr(1,2),7:Fr(-1,2),-7:Fr(-1,2),6:Fr(-1,4),-6:Fr(-1,4),8:Fr(-1,4),-8:Fr(-1,4)}.get(k,Fr(0))
def fdiag_exact():
    """exact complex-rational Fourier coefficients (re, im) of the Line B diagonal kick, same rule as lineB/common/model.py fCoeff(k,0)"""
    C = {}
    for k in range(-9, 10):
        re = (Fr(1,2) if k in (7,-7) else Fr(0)) + rC(k)/10 - (Fr(1,10) if k == 0 else Fr(0))
        im = -(rC(k-1) - rC(k+1))/200          # (r(k-1)-r(k+1))/(200 i) = -i (r(k-1)-r(k+1))/200
        if re or im: C[k] = (re, im)
    return C
KICKS = {'full': fdiag_exact(), 'k1': {1:(Fr(9,20),Fr(0)), -1:(Fr(9,20),Fr(0))}, 'f7': {7:(Fr(9,20),Fr(0)), -7:(Fr(9,20),Fr(0))},
         'f7f1': {7:(Fr(9,20),Fr(0)), -7:(Fr(9,20),Fr(0)), 1:(Fr(1,20),Fr(0)), -1:(Fr(1,20),Fr(0))}}
def check_model():
    sys.path.insert(0, os.path.join(HERE, '..', '..', 'lineB', 'common'))
    import model
    for k in range(-12, 13):
        c = KICKS['full'].get(k, (0, 0)); assert abs(complex(float(c[0]), float(c[1])) - model.fCoeff(k, 0)) < 1e-15, k
    return True
def qform(m, h):
    """z_j = a_j z0 + b_j z1 mod h; R(z) = 2 z^T H z / h mod h as A z0^2 + B z0 z1 + C z1^2 (exact, verified)."""
    a, b = [1, 0], [0, 1]
    for j in range(2, m + 2): a.append((6*a[-1] - a[-2]) % h); b.append((6*b[-1] - b[-2]) % h)
    assert a[m] % h == 1 and b[m] % h == 0 and a[m+1] % h == 0 and b[m+1] % h == 1, 'T^m != I mod h'
    def R(z0, z1):
        z = [(a[j]*z0 + b[j]*z1) % h for j in range(m)]
        Hz = [6*z[j] - z[(j+1) % m] - z[(j-1) % m] for j in range(m)]
        assert all(v % h == 0 for v in Hz)
        return (2*sum(z[j]*Hz[j] for j in range(m))//h) % h
    A, C = R(1, 0), R(0, 1); B = (R(1, 1) - A - C) % h
    rnd = random.Random(m)
    for _ in range(200):
        z0, z1 = rnd.randrange(h), rnd.randrange(h)
        assert R(z0, z1) == (A*z0*z0 + B*z0*z1 + C*z1*z1) % h
    return a[:m], b[:m], A, B, C
def tables(kick, eta, h, prec=96):
    ctx.prec = prec; C = KICKS[kick]; et = arb(eta) if isinstance(eta, str) else arb(str(eta))
    G = []; E = []; eps = arb(0); twopi = 2*arb.pi()
    for k in range(h):
        x = arb(1)/2 + arb(k)/h
        f = arb(0)
        for n, (re, im) in C.items():
            cr = arb(re.numerator)/re.denominator; ci = arb(im.numerator)/im.denominator
            th = twopi*n*x
            f += cr*th.cos() - ci*th.sin()      # Re[(cr + i ci) e(n x)]
        g = acb(0, et*f).exp()
        gd = complex(float(g.real.mid()), float(g.imag.mid()))
        e = acb(0, twopi*arb(k)/h).exp(); ed = complex(float(e.real.mid()), float(e.imag.mid()))
        eps = max(eps, abs(acb(gd.real, gd.imag) - g).upper(), abs(acb(ed.real, ed.imag) - e).upper(), key=lambda v: float(v))
        G.append(gd); E.append(ed)
    return G, E, arb(eps).upper()
def errbound(m, h, eps, nthreads):
    """a-priori bound on |S_computed - S_exact| (see docstring of zres.c)"""
    ctx.prec = 128
    u = arb(2)**-53; uL = arb(2)**-64; s5 = arb(5).sqrt(); e = arb(eps)
    ek = e                        # first factor
    for k in range(m):            # m further multiplications (m-1 G's and the E factor)
        ek = ek*(1 + e)*(1 + s5*u) + e + s5*u*(1 + e)
    n = arb(h)
    gam = lambda nn, uu: nn*uu/(1 - nn*uu)
    term_tot = n*n*ek
    sum_row = arb(2).sqrt()*gam(n, u)*n*n*(1 + ek)
    sum_rows = arb(2).sqrt()*gam(n + nthreads + 2, uL)*n*n*(1 + ek)*(1 + gam(n, u))
    return (term_tot + sum_row + sum_rows).upper()
def run(kick, m, eta, offsets, threads=8):
    d = mdata(m); h, gp, yp = d['h'], d['gp'], d['yp']
    t0 = time.time(); G, E, eps = tables(kick, eta, h); t_tab = time.time() - t0
    a, b, A, B, C = qform(m, h)
    res = []
    nus = []
    for off in offsets:
        N = (-off) % h           # N == -off (mod h)
        nu = pow(N, -1, h)
        if nu % 2 == 0: nu += h
        assert math.gcd(nu, gp) == 1
        t = pow(16*nu % h, -1, h); nus.append((off, nu, t))
    tf = f'/tmp/zres_tab_{os.getpid()}.bin'; cf = f'/tmp/zres_coef_{os.getpid()}.txt'; of = f'/tmp/zres_out_{os.getpid()}.txt'
    import struct
    with open(tf, 'wb') as fh:
        fh.write(struct.pack(f'{2*h}d', *[v for z in G for v in (z.real, z.imag)]))
        fh.write(struct.pack(f'{2*h}d', *[v for z in E for v in (z.real, z.imag)]))
    with open(cf, 'w') as fh:
        for j in range(m): fh.write(f'{a[j]} {b[j]}\n')
        fh.write(f'{A} {B} {C}\n')
    t1 = time.time()
    subprocess.run([os.path.join(HERE, 'zres'), str(m), str(h), tf, cf, str(len(nus))] + [str(t) for _, _, t in nus] + [of],
                   check=True, env=dict(os.environ, OMP_NUM_THREADS=str(threads)))
    t_k = time.time() - t1
    out = {int(l.split()[0]): complex(float(l.split()[1]), float(l.split()[2])) for l in open(of)}
    for p in (tf, cf, of): os.remove(p)
    err = errbound(m, h, eps, threads)
    ctx.prec = 128
    phi = sum(1 for _ in [0]) and None
    import sympy
    phih = int(sympy.totient(h))
    totlo = arb(0)
    for off, nu, t in nus:
        S = out[t]; Sabs = arb(abs(S)); 
        absS_lo = (Sabs*(1 - arb(2)**-50) - arb(err)); absS_hi = Sabs*(1 + arb(2)**-50) + arb(err)
        Z2lo = (absS_lo/h)**2 if absS_lo > 0 else arb(0); Z2hi = (absS_hi/h)**2
        totlo += Z2lo
        res.append(dict(N_mod_h=-off, nu=nu, t=t, S=[S.real, S.imag], Z2_lower=float(Z2lo.lower()), Z2_upper=float(Z2hi.upper()), Z2_float=abs(S)**2/h**2))
    F_lo = totlo/phih
    rec = dict(kick=kick, m=m, eta=eta, h=h, phi_2h=phih, R_form=[A, B, C], minus_ybar=(-pow(yp, -1, h)) % h, table_eps=float(eps), err_abs_S=float(err),
               residues=res, F_lower=float(F_lo.lower()), F_over_2m_lower=float((F_lo/(2*m)).lower()),
               Wrest_over_m_lower=float(((F_lo - 4*m)/m).lower()), secs_tables=round(t_tab, 1), secs_kernel=round(t_k, 1))
    return rec
if __name__ == '__main__':
    assert check_model()
    kick = sys.argv[1]; m = int(sys.argv[2]); eta = sys.argv[3]; offs = [int(x) for x in sys.argv[4].split(',')]
    thr = int(sys.argv[5]) if len(sys.argv) > 5 else 8
    rec = run(kick, m, eta, offs, thr)
    print(json.dumps(rec), flush=True)
    open(os.path.join(HERE, 'cert_class.jsonl'), 'a').write(json.dumps(rec) + '\n')
