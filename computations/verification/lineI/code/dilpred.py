"""Predict dilation-coset members Z(nu_rho + 2hj/d) from the twisted G2 law (Zhat(beta), beta in O/d) and compare with class sums.
Structured application (no dense kron). Saves Zhat arrays to ../data/zhat_d{d}_{a}_{b}_m{m}.npy."""
import numpy as np, math, sys, json, os
from law import mdata, kick_ghat, LAM
from twist import build
from base import get
def Zseq(parts, taus, m, S, K):
    X = np.zeros((K, S, K), complex); X[:, 0, :] = np.eye(K)
    items = [(n, Mn, P) for n, (Mn, P) in parts.items()]
    tg = {n: (P != 0).argmax(axis=0) for n, Mn, P in items}; ph = {n: P[tg[n], np.arange(S)] for n, Mn, P in items}
    for tau in taus:
        Y = np.zeros_like(X)
        for n, Mn, P in items:
            c = np.exp(2j*np.pi*n*tau)*np.einsum('ij,jsk->isk', Mn, X)*ph[n][None, :, None]
            Y[:, tg[n], :] += c          # tgt is a permutation of states
        X = Y
    return (1-LAM**(-m))*np.einsum('isi->', X)
if __name__ == '__main__':
    d = int(sys.argv[1]); ms = [int(x) for x in sys.argv[2].split(',')]; rhos = [(2, 8), (-2, 8)]
    K = 40; gh = kick_ghat('k1', 2.0, 10); out = {}
    for m in ms:
      for (a, b) in rhos:
        D = mdata(m); h = D['h']; yp = D['yp']; assert h % d == 0
        parts, nu0, S = build(m, a, b, gh, 2.6, K)
        for n,(Mn,P) in parts.items(): assert (np.count_nonzero(P,axis=0)==1).all() and len(set((P!=0).argmax(axis=0)))==S
        f = f'../data/zhat_d{d}_{a}_{b}_m{m}.npy'
        lam = []; x, y = 1, 0
        for i in range(m): lam.append((x, y)); x, y = (3*x+4*y) % d, (2*x+3*y) % d
        if os.path.exists(f): Zh = np.load(f)
        else:
            Zh = np.zeros((d, d), complex)
            for bx in range(d):
                for by in range(d):
                    Zh[bx, by] = Zseq(parts, [((2*(bx*lx+2*by*ly)) % d)/d for (lx, ly) in lam], m, S, K)
            np.save(f, Zh)
        Z0 = Zh[0, 0]
        X, Y = np.meshgrid(np.arange(d), np.arange(d), indexing='ij')
        Wg = np.array([[np.sum(Zh*np.exp(-2j*np.pi*((2*(X*gx+2*Y*gy)) % d)/d))/d**2 for gy in range(d)] for gx in range(d)])
        Nmg = (X*X-2*Y*Y) % d; Wu = np.zeros(d, complex); np.add.at(Wu, Nmg.ravel(), Wg.ravel()); Nu = np.bincount(Nmg.ravel(), minlength=d)
        eps = 1 if pow(2, (d-1)//2, d) == 1 else -1; dl = Wu-Z0*Nu/d**2
        Zt = np.array([np.sum(Wu*np.exp(-2j*np.pi*t*np.arange(d)/d)) for t in range(d)])
        mem = []; bad = None
        for j in range(1, d):
            nu = (nu0+(2*h//d)*j) % (2*h)
            if math.gcd(nu, 2*h) != 1: bad = abs(Zt[(j*yp) % d])**2; continue
            mem.append((nu, (j*yp) % d))
        pred = np.array([abs(Zt[t])**2 for _, t in mem])
        rec = dict(m=m, rho=[a, b], Z0=float(abs(Z0)**2), main_each=float(abs(Z0)**2/d**2), cross=float(2*eps*np.real(np.conj(Z0)*dl[0])),
                   square=float(d*np.sum(abs(dl)**2)), bad=float(bad), maxbeta2=float(np.max(abs(Zh.ravel()[1:]))**2),
                   pred_mean=float(pred.mean()), pred_rel=float(pred.mean()/(abs(Z0)**2/d**2)-1))
        try:
            DD = get('k1', m); Zd = dict(zip(DD['nu'].tolist(), DD['Z'].tolist()))
            act = np.array([Zd[nu] for nu, _ in mem]); rec['act_mean'] = float(act.mean()); rec['maxrel_pred_vs_act'] = float(np.max(abs(pred/act-1)))
        except Exception as e: rec['act'] = 'n/a'
        print(json.dumps(rec), flush=True); out[f'{a},{b},{m}'] = rec
    json.dump(out, open(f'../logs/dilpred_d{d}.json', 'w'), indent=1)
