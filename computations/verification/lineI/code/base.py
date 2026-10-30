"""Line I common data: |Z_m(nu)|^2 for all units nu mod 2h, shortest lattice vectors, resonant masks (TRACE-206 frozen def)."""
import os, sys, math, numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from law import mdata
from step1c import divisors
CACHE = os.path.join(os.path.dirname(__file__), '..', 'data')
def load_T(kick, m):
    p = f'/workspace/bgs-lineG/logs/Torb_{kick}_m{m}.bin'
    if os.path.exists(p) and m >= 15: return np.fromfile(p, np.complex128)
    return np.load(f'/workspace/audit/lineE/logs/T_{kick}_eta2.0_m{m}.npy')
def Z2_all(T, m):
    d = mdata(m); h = d['h']; gp = 2*h; yp = d['yp']
    S = np.fft.ifft(T)*h
    nu = np.arange(1, gp, 2, dtype=np.int64)
    g = np.gcd(nu, gp); nu = nu[g == 1]
    c = (-pow(16, -1, h)*pow(yp, -1, h)) % h
    inv = np.array([pow(int(x), -1, h) for x in nu], dtype=np.int64)
    v = (c*inv) % h
    return nu, np.abs(S[v])**2/h**2
def reduce_vec(nu, M):
    """vectorised Lagrange-Gauss reduction of basis (M,0),(nu,1); returns u=(a,b) shortest, v second, b>=0 normalised"""
    ux = np.full(nu.shape, M, np.int64); uy = np.zeros_like(nu); vx = nu.astype(np.int64) % M; vy = np.ones_like(nu)
    for _ in range(200):
        nu2 = ux*ux+uy*uy; nv2 = vx*vx+vy*vy
        sw = nv2 < nu2
        ux, vx = np.where(sw, vx, ux), np.where(sw, ux, vx); uy, vy = np.where(sw, vy, uy), np.where(sw, uy, vy)
        nu2 = ux*ux+uy*uy
        d = ux*vx+uy*vy
        q = np.floor_divide(2*d+nu2, 2*nu2)
        if not q.any(): break
        vx = vx-q*ux; vy = vy-q*uy
    nu2 = ux*ux+uy*uy; nv2 = vx*vx+vy*vy; assert (nu2 <= nv2).all()
    s = np.where((uy < 0) | ((uy == 0) & (ux < 0)), -1, 1); ux, uy = ux*s, uy*s
    s = np.where((vy < 0) | ((vy == 0) & (vx < 0)), -1, 1); vx, vy = vx*s, vy*s
    return ux, uy, vx, vy
PSTAR = {'k1': [(2, 8), (-2, 8), (2, 16), (-2, 16)], 'full': [(2, 392), (-2, 392), (2, 784), (-2, 784)]}
PRBROAD = [(-2, 8), (2, 8), (-2, 16), (2, 16), (-2, 4), (2, 4), (-6, 16), (6, 16)]
def get(kick, m):
    f = os.path.join(CACHE, f'base_{kick}_m{m}.npz')
    if os.path.exists(f): return dict(np.load(f))
    T = load_T(kick, m); h = mdata(m)['h']; nu, Z = Z2_all(T, m)
    a, b, a2, b2 = reduce_vec(nu, 2*h)
    phi = len(nu); RMT = 4*m - m*m/h
    # frozen TRACE-206 resonant set: primaries + included dilation levels (|Z_rho|^2/d^2 >= 4m)
    res = np.zeros(phi, bool); lev = np.zeros(phi, np.int64)
    ds = [d for d in divisors(h) if 1 < d and d*d <= h]
    for (A, B) in PSTAR[kick]:
        p = np.nonzero((B*nu-A) % (2*h) == 0)[0]
        if len(p) == 0: continue
        res[p] = True; Z0 = Z[p[0]]
        for d in ds:
            if Z0/d/d < 4*m: continue
            M = 2*h//d
            mem = ((B*nu-A) % M == 0) & ~res
            res |= mem; lev[mem] = d
    # broad mask (lineG bulk def): dilation families of the 8 broad primaries (+49-images for full), any d|h d<=sqrt h, or height<=8
    PRk = PRBROAD if kick == 'k1' else [(x, 49*y) for x, y in PRBROAD]+PRBROAD
    dil = np.zeros(phi, bool)
    for d in [1]+ds:
        M = 2*h//d
        for (A, B) in PRk: dil |= ((B*nu-A) % M == 0)
    out = dict(nu=nu, Z=Z, a=a, b=b, a2=a2, b2=b2, res=res, lev=lev, dil=dil, h=np.int64(h), m=np.int64(m), RMT=np.float64(RMT))
    np.savez(f, **out); return out
if __name__ == '__main__':
    for spec in sys.argv[1:]:
        k, m = spec.split(':'); D = get(k, int(m)); m = int(m)
        phi = len(D['nu']); F = D['Z'].mean(); Res = (D['Z'][D['res']]-D['RMT']).sum()/phi
        print(f"{k} m={m} h={D['h']} phi={phi} F/2m={F/2/m:.4f} Res/2m={Res/2/m:.4f} W'/m={(F-D['RMT']-Res)/m:+.4f} nres={D['res'].sum()}", flush=True)
