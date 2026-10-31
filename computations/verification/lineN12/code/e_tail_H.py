"""N12 (1d-H) ADAPTED-NORM version of e_tail: C_A*kappa^m replaced by kap_H^m with constant 1, K measured in H/H* norms
(||(A0/s)^m Qt||_H <= kap_H^m, verify_adapted.py V3b). Inserted background steps cost (1+Lip_H|d|) each, |d|<=1e-13 -> folded into M.
Original doc: N12 (1d): analytic tail of the pair interaction for centre distance G0+m, m>=0 (all ordered type pairs, h, s).
Exact identity at any cut t of the composite chain: r_ij = (w_t Phi)(psi^T v_t) + w_t Q v_t, v_t = prod_{<=t} A(d)/s Phi,
w_t = psi^T prod_{>t} A(d)/s.  Inserting m background steps at the cut (exact up to tails |d|<=|zeta|lam^{-17}~1e-14):
|w_t (A0/s)^m Q v_t| <= ||w_t Q|| ||Q v_t|| C_A(r) (r/|s|)^m,  C_A(0.8)=10.654 (b_powerbound, [CA*]), kappa=0.41765.
Per window: dev(G0+m) <= K_t C_A kappa^m + M_t,  K_t = ||w_tQ|| ||Qv_t||/|r_i r_j|, M_t = |(w_tPhi)(psi v_t)/(r_i r_j) - 1| (tail mismatch,
decreasing in m [P-sketch]).  Cut t chosen to minimise K_t + M_t."""
import sys, json, numpy as np
_G0=int(sys.argv[1]) if len(sys.argv)>1 else 34
sys.argv=['c_pairs.py','A','0']
exec(open('/workspace/bgs-lineN/N12/code/c_pairs.py').read().split('pairset=sys.argv')[0])
G0=_G0
G0=_G0
CA=1.0; kap=0.45
zN=np.load('/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45.npz'); TH=zN['T']; THi=np.linalg.inv(TH)
nH=lambda v: np.linalg.norm(TH@v); nHs=lambda w: np.linalg.norm(w@THi)
def chain(ds):
    vs=[Phi.astype(complex)]
    for d in ds: vs.append((A.Amat(d)@vs[-1])/s)
    # left vectors w_t = psi^T prod_{>t}: build backwards
    ws=[psi.astype(complex)]
    for d in reversed(ds): ws.append((ws[-1]@A.Amat(d))/s)
    ws=ws[::-1]   # ws[t] = psi^T prod_{steps >= t}  (so r = ws[t] @ vs[t] for any t)
    return vs,ws
EPS=(1,1); rows=[]
for ti in TYPES:
    for tj in TYPES:
        for h in (0,1):
            for sg in (1,-1):
                ej=mulq(TYPES[tj],lamp(G0)); 
                if h: ej=mulq(ej,EPS)
                e=(TYPES[ti][0]+sg*ej[0],TYPES[ti][1]+sg*ej[1]); zA,zB=seeds(e)
                sjA,sjB=(win(mulq(TYPES[tj],EPS)) if h else single[tj])
                res=[]
                for z,ri,rj in [(zA,single[ti][0],sjA),(zB,single[ti][1],sjB)]:
                    vs,ws=chain(core(z)); best=None
                    for t in range(len(vs)):
                        K=nHs(ws[t]@Q)*nH(Q@vs[t])/abs(ri*rj)
                        M=abs((ws[t]@Phi)*(psi@vs[t])/(ri*rj)-1)
                        tot=K*CA+M
                        if best is None or tot<best[0]: best=(tot,K,M,t)
                    res.append(best)
                (tA,KA,MA,_),(tB,KB,MB,_)=res
                # class-level tail sum over m>=0: per window dev<=K CA kap^m + M ; class dev <= (1+devA)^3(1+devB)^3-1
                devsum=0.0
                for m in range(0,200):
                    dA=KA*CA*kap**m+MA*(kap**m); dB=KB*CA*kap**m+MB*(kap**m)   # M assumed to decay at least like kappa^m [P-sketch]
                    devsum+=(1+dA)**3*(1+dB)**3-1
                rows.append(dict(i=ti,j=tj,h=h,s=sg,KA=KA,MA=MA,KB=KB,MB=MB,tail_devsum=devsum))
                print(json.dumps(rows[-1]),flush=True)
json.dump(dict(G0=G0,CA=CA,kappa=kap,rows=rows),open(f'/workspace/bgs-lineN/N12/logs/e_tailH_G{G0}.json','w'),indent=1)
