"""Independent re-enclosure (auditor). Reuses only build_blocks/assemble from
h7_multidisc_cert.py (checked by hand); product, eigen-centre and inclusion test
are new: Krawczyk/Brouwer box test on the exact quadratic expansion
F(y0+X) = F(y0) + J0 X - dmu*dv, in acb ball arithmetic, no power-of-two scaling."""
if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")

import sys, os, json, time, math
import numpy as np
# Paths relative to this file (integration 2026-11-05; the audit ran against the PR #85
# checkout at b8e91215, evidence/research/20261104_grok47/code). Repository root = parents[6].
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, *(['..'] * 6)))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'verification', 'lineI', 'code'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'verification', 'h7_scope', 'code'))
from flint import acb, acb_mat, arb, ctx
import h7_multidisc_cert as M
ctx.prec = 320
M.RHO = arb(6)/arb(5)

def orbit(d):
    # my own lambda-orbit: lambda^j = x + y sqrt2, lambda = 3+2sqrt2
    x, y = 1, 0; out = []
    while True:
        out.append((x, y))
        x, y = (3*x + 4*y) % d, (2*x + 3*y) % d
        if (x, y) == (1, 0): return out

def trace_twist(d, bx, by, pw):
    # Tr((bx+by s2)(x+y s2)) = 2(bx x + 2 by y)
    return [(2*(bx*x + 2*by*y)) % d for x, y in pw]

def mid_np(A):
    n = A.nrows()
    return np.array([[complex(float(A[i,j].real.mid()), float(A[i,j].imag.mid())) for j in range(n)] for i in range(n)])

def run(name, d, bx, by, a):
    t0 = time.time()
    centers, index, blocks, n_out = M.build_blocks()
    assert n_out == 0
    pw = orbit(d); P = len(pw)
    tws = trace_twist(d, bx, by, pw)
    dim = len(centers)*M.K_MODES
    Q = None
    for tw in tws:
        L = M.assemble(centers, index, blocks, d, tw, a)
        Q = L if Q is None else L*Q          # first factor on the right
    Qm = mid_np(Q)
    radmax = max(float(Q[i,j].rad()) for i in range(dim) for j in range(dim))
    ev, V = np.linalg.eig(Qm)
    k = int(np.argmax(abs(ev))); mu0 = complex(ev[k]); v = V[:, k]
    piv = int(np.argmax(abs(v))); v = v/v[piv]
    ev_sorted = sorted(abs(ev), reverse=True)
    # exact (point) centre
    va = [acb(complex(z)) for z in v]; va[piv] = acb(1); mua = acb(mu0)
    # residual F0 = Q v - mu v  (ball)
    vcol = acb_mat(dim, 1, va)
    F0 = Q*vcol
    F0 = [F0[i,0] - mua*va[i] for i in range(dim)]
    # J0 (ball): column piv replaced by -v  (unknowns: dv_free in place, dmu at piv slot)
    J0 = acb_mat(dim, dim, [ (Q[i,j] - (mua if i==j else 0)) if j != piv else -va[i]
                             for i in range(dim) for j in range(dim)])
    Jm = mid_np(J0)
    R = np.linalg.inv(Jm)
    Ra = acb_mat(dim, dim, [acb(complex(R[i,j])) for i in range(dim) for j in range(dim)])
    G = Ra*J0
    RF = Ra*acb_mat(dim, 1, F0)
    # row bounds
    c0 = []; c1 = []; c2 = []
    for i in range(dim):
        s1 = arb(0); s2 = arb(0)
        for j in range(dim):
            s1 += ((acb(1) if i==j else acb(0)) - G[i,j]).abs_upper()
            s2 += Ra[i,j].abs_upper()
        c0.append(RF[i,0].abs_upper()); c1.append(s1); c2.append(s2)
    n1 = max(float(x.upper()) for x in c1)
    assert n1 < 1, n1            # R nonsingular, and contraction
    e0 = max(float(x.upper()) for x in c0)
    # choose r with margin
    r = arb(4*e0/(1-n1)) if e0 > 0 else arb('1e-300')
    ok = all(bool(c0[i] + c1[i]*r + c2[i]*r*r < r) for i in range(dim))
    mod = abs(mua)
    lo = (mod - r) ** (arb(1)/P); hi = (mod + r) ** (arb(1)/P)
    out = dict(name=name, d=d, beta=[bx,by], sector=a, period=P, dim=dim, ok=ok,
               rad_entry_max=radmax, resid_bound=e0, norm_I_minus_RJ=n1,
               box_r=float(r.upper()), product_mod_center=abs(mu0),
               second_eig_ratio=float(ev_sorted[1]/ev_sorted[0]),
               rate_lo=str(lo), rate_hi=str(hi), rate_lo_f=float(lo.lower()), rate_hi_f=float(hi.upper()),
               secs=round(time.time()-t0,1))
    print(json.dumps(out), flush=True)
    return out

if __name__ == '__main__':
    specs = {'l7_21': ('level7_2_1', 7, 2, 1, 4), 'l7_13': ('level7_1_3', 7, 1, 3, 6),
             'l7_01': ('level7_0_1', 7, 0, 1, 0), 'd34': ('d3437426497', 3437426497, -208, 0, 0)}
    res = [run(*specs[k]) for k in sys.argv[1:]]
    json.dump(res, open(os.path.join(HERE, 'krawczyk_%s.json' % '_'.join(sys.argv[1:])), 'w'), indent=1)
