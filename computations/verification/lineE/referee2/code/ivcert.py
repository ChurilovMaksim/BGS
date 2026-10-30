"""Auditor's independent rigorous recomputation of |Z_m(nu)|^2 at N == -off (mod h) via Prop. G,
with directed-rounding interval kernel ivsum.c.  Tables enclosed in arb, outward-rounded to double.
usage: ivcert.py kick m eta off1,off2,... threads"""
import sys, os, math, json, struct, subprocess, time
from fractions import Fraction as Fr
from flint import arb, acb, ctx
import sympy
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', '..'))  # repository root (repo copy: was an absolute scratch path)
def r(k): return {0: Fr(1), 1: Fr(1,2), -1: Fr(1,2), 7: Fr(-1,2), -7: Fr(-1,2), 6: Fr(-1,4), -6: Fr(-1,4), 8: Fr(-1,4), -8: Fr(-1,4)}.get(k, Fr(0))
def coeffs(kick):
    if kick == 'k1': return {1: (Fr(9,20), Fr(0)), -1: (Fr(9,20), Fr(0))}
    if kick == 'f7': return {7: (Fr(9,20), Fr(0)), -7: (Fr(9,20), Fr(0))}
    # model.py fCoeff(k,0) = 0.5[k=+-7] + r(k)/10 + (r(k-1)-r(k+1))/(200 i) - 0.1[k=0]
    C = {}
    for k in range(-12, 13):
        re = (Fr(1,2) if abs(k) == 7 else 0) + r(k)/10 - (Fr(1,10) if k == 0 else 0)
        im = Fr(0) - (r(k-1) - r(k+1))/200      # 1/(200i) = -i/200
        if re or im: C[k] = (Fr(re), im)
    sys.path.insert(0, os.path.join(REPO, 'computations/verification/lineB/common')); import model
    for k in range(-12, 13):
        c = C.get(k, (0, 0)); assert abs(complex(float(c[0]), float(c[1])) - model.fCoeff(k, 0)) < 1e-15
    for k, (re, im) in C.items(): assert C[-k] == (re, -im)   # real kick
    return C
def nsw(m):
    a, b = 1, 1   # h_1 = 1, h_3 = 7 ; h_{m+2} = 6h_m - h_{m-2}
    hs = {1: 1, 3: 7}
    for k in range(5, m + 1, 2): hs[k] = 6*hs[k-2] - hs[k-4]
    return hs[m]
def outward(x):
    lo, hi = x.lower(), x.upper()
    return math.nextafter(float(lo), -math.inf), math.nextafter(float(hi), math.inf)
def tables(kick, eta, h):
    ctx.prec = 160
    C = coeffs(kick); e = arb(eta); tp = 2*arb.pi(); out = []
    for k in range(h):
        x = arb(1)/2 + arb(k)/h
        f = arb(0)
        for n, (re, im) in C.items():
            th = tp*n*x
            f += arb(re.numerator)/re.denominator*th.cos() - arb(im.numerator)/im.denominator*th.sin()
        g = (acb(0, 1)*e*f).exp()
        lo, hi = outward(g.real); ilo, ihi = outward(g.imag)
        out.append((-lo, hi, -ilo, ihi))
    Et = []
    for k in range(h):
        z = (acb(0, 1)*tp*arb(k)/h).exp()
        lo, hi = outward(z.real); ilo, ihi = outward(z.imag)
        Et.append((-lo, hi, -ilo, ihi))
    return out, Et
def qform(m, h):
    a, b = [1, 0], [0, 1]
    for j in range(2, m + 2): a.append((6*a[-1] - a[-2]) % h); b.append((6*b[-1] - b[-2]) % h)
    assert (a[m], b[m], a[m+1], b[m+1]) == (1, 0, 0, 1)
    def R(z0, z1):
        z = [a[j]*z0 + b[j]*z1 for j in range(m)]       # integer lift (not reduced) -- R mod h is lift independent
        Hz = [6*z[j] - z[(j+1) % m] - z[(j-1) % m] for j in range(m)]
        assert all(v % h == 0 for v in Hz)
        s = 2*sum(z[j]*Hz[j] for j in range(m)); assert s % h == 0
        return (s//h) % h
    A, Cc = R(1, 0), R(0, 1); B = (R(1, 1) - A - Cc) % h
    return a[:m], b[:m], A, B, Cc
def run(kick, m, eta, offs, threads):
    h = nsw(m); t0 = time.time()
    G, E = tables(kick, eta, h)
    a, b, A, B, C = qform(m, h)
    tf = f'/tmp/aud_tab_{os.getpid()}.bin'; cf = f'/tmp/aud_coef_{os.getpid()}.txt'
    with open(tf, 'wb') as fh:
        for v in G + E: fh.write(struct.pack('4d', *v))
    with open(cf, 'w') as fh:
        for j in range(m): fh.write(f'{a[j]} {b[j]}\n')
        fh.write(f'{A} {B} {C}\n')
    phi = int(sympy.totient(h)); res = []; tot = arb(0)
    ts = {}
    for off in offs:
        N = (-off) % h; nu = pow(N, -1, h); ts[off] = (nu, pow(16*nu % h, -1, h))
    of = f'/tmp/aud_out_{os.getpid()}.txt'; t1 = time.time()
    subprocess.run([os.path.join(HERE, 'ivsum'), str(m), str(h), tf, cf, str(len(offs))] + [str(ts[o][1]) for o in offs] + [of], check=True,
                   env=dict(os.environ, OMP_NUM_THREADS=str(threads)))
    lines = open(of).read().split('\n'); os.remove(of)
    for off, line in zip(offs, lines):
        nu, t = ts[off]
        tt, rl, rh, il, ih = line.split(); assert int(tt) == t; rl, rh, il, ih = float(rl), float(rh), float(il), float(ih)
        ctx.prec = 128
        # rigorous: |S| >= dist(0, box)
        dr = 0 if rl <= 0 <= rh else min(abs(arb(rl)), abs(arb(rh)))
        di = 0 if il <= 0 <= ih else min(abs(arb(il)), abs(arb(ih)))
        Slo2 = arb(dr)**2 + arb(di)**2
        Shi2 = max(abs(arb(rl)), abs(arb(rh)))**2 + max(abs(arb(il)), abs(arb(ih)))**2
        Z2lo = Slo2/(h*h); Z2hi = Shi2/(h*h); tot += Z2lo
        res.append(dict(off=off, N_mod_h=-off, nu_mod_h=nu, t=t, Re=[rl, rh], Im=[il, ih], width=max(rh-rl, ih-il),
                        Z2_lo=float(Z2lo.lower()), Z2_hi=float(Z2hi.upper()), secs=round(time.time()-t1, 1)))
    os.remove(tf); os.remove(cf)
    F = tot/phi
    return dict(kick=kick, m=m, eta=eta, h=h, phi=phi, R=[A, B, C], residues=res, F_lo=float(F.lower()),
                F_over_2m_lo=float((F/(2*m)).lower()), Wrest_over_m_lo=float(((F - 4*m)/m).lower()), secs=round(time.time()-t0, 1))
if __name__ == '__main__':
    kick, m, eta = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    offs = [int(x) for x in sys.argv[4].split(',')]; thr = int(sys.argv[5]) if len(sys.argv) > 5 else 4
    rec = run(kick, m, eta, offs, thr); print(json.dumps(rec), flush=True)
    open(os.path.join(HERE, '..', 'logs', 'ivcert.jsonl'), 'a').write(json.dumps(rec) + '\n')
