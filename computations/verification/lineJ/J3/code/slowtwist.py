"""[N] slow-twist test: for primitive prime divisors q of h_p (rank p), the twisted per-step radius r_beta of prod_{i<P} L_{a/8+tau_i},
tau_i = Tr(beta lam^i)/q mod 1 (P = ord_q lam), for 'small' beta (|bx|,|by|<=3: tau_i ~ 0 for i < log_lam q) and 150 random beta.
Same toy Galerkin family as levels_survey (reproduces the certified d=7 top 1.2837 and mu* 1.9155)."""
import sys, numpy as np, json, sympy, random
sys.path.insert(0,'/workspace/bgs-lineI/code')
from law import kick_ghat, MC, LAM
gh=kick_ghat('k1',2.0,10); K=40; RHO=2.6; c0=1/(LAM-1/LAM); C=-c0
Mn={n:gn*np.exp(2j*np.pi*C*n*n/2)*MC(n,C,RHO,K) for n,gn in gh.items() if abs(gn)>0}
ns=np.array(list(Mn)); Ms=np.array([Mn[n] for n in ns])
def L(t): return np.tensordot(np.exp(2j*np.pi*ns*t),Ms,axes=1)
h={1:1,3:7}; a,b=1,7
for mm in range(5,80,2): a,b=b,6*b-a; h[mm]=b
random.seed(1); res={}
for p in (17,19,23,29,31,37,41,43,47,53):
    fac=sympy.factorint(h[p]); qs=[q for q in fac if all(h[r]%q for r in range(1,p,2))]
    for q in qs:
        pw=[]; x,y=1,0
        while True:
            pw.append((x,y)); x,y=(3*x+4*y)%q,(2*x+3*y)%q
            if (x,y)==(1,0): break
        P=len(pw)
        if P>200: print(p,q,'period',P,'skip'); continue
        betas=[(bx,by) for bx in range(-3,4) for by in range(-3,4) if (bx,by)!=(0,0)]+[(random.randrange(q),random.randrange(q)) for _ in range(150)]
        rs=[]
        for (bx,by) in betas:
            taus=[((2*(bx*x+2*by*y))%q)/q for (x,y) in pw]
            best=0
            for aa in (0,2,4,6):
                Q=np.eye(K,dtype=complex)
                for t in taus: Q=L(aa/8+t)@Q
                best=max(best,max(abs(np.linalg.eigvals(Q)))**(1/P))
            rs.append(best)
        rs=np.array(rs); small=rs[:48]; rnd=rs[48:]
        res[f'{p}:{q}']=dict(period=P,log_lam_q_over_P=float(np.log(q)/np.log(LAM)/P),r_small_max=float(small.max()),r_rand_max=float(rnd.max()),r_rand_med=float(np.median(rnd)))
        print(p,q,res[f'{p}:{q}'],flush=True)
json.dump(res,open('logs/slowtwist.json','w'),indent=1)
