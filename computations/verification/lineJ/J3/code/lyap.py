"""[N] One-parameter family L_tau = sum_n ghat(n) e(n tau) e(C n^2/2) MC_n on H^2(D_rho) (single disc, Line G Galerkin), C = -4 a c0 / b.
By the exact sector decomposition every (+-2,8) twisted trace at ANY level d is c_m sum_a c_a Tr prod_i L_{a/8 + tau_i} (+edge part).
Computes: r(L_tau) over tau; period-3 d=7 check; top Lyapunov exponent for iid uniform tau; same for b=16 (C=-c0/2, no sector reduction:
here only the scalar family, i.e. a heuristic proxy)."""
import sys, numpy as np, json
sys.path.insert(0,'/workspace/bgs-lineI/code')
from law import kick_ghat, MC, LAM
gh=kick_ghat('k1',2.0,10); K=40; RHO=2.6; c0=1/(LAM-1/LAM)
out={}
for b in (8,16):
    C=-4*2*c0/b
    Mn={n:gn*np.exp(2j*np.pi*C*n*n/2)*MC(n,C,RHO,K) for n,gn in gh.items() if abs(gn)>0}
    L=lambda t: sum(np.exp(2j*np.pi*n*t)*M for n,M in Mn.items())
    ts=np.linspace(0,1,257)[:-1]; rs=[max(abs(np.linalg.eigvals(L(t)))) for t in ts]
    i=int(np.argmax(rs)); print('b',b,'max_tau r(L_tau)',rs[i],'at tau',ts[i],' min',min(rs),flush=True)
    if b==8:
        # d=7 check: class 2:1 sector a: tau_i = a/8 + taus7
        def taus(bx,by):
            d=7; o=[]; x,y=1,0
            for k in range(3): o.append(((2*(bx*x+2*by*y))%d)/d); x,y=(3*x+4*y)%d,(2*x+3*y)%d
            return o
        for cl in ((1,3),(2,1),(0,1)):
            best=max((max(abs(np.linalg.eigvals(L(s+taus(*cl)[2])@L(s+taus(*cl)[1])@L(s+taus(*cl)[0]))))**(1/3),s) for s in np.arange(8)/8)
            print('  d=7 class',cl,'max over 8 shifts a/8 (and sign conventions) r=',best,flush=True)
    rng=np.random.default_rng(7); Lg={}
    grid=np.arange(4096)/4096
    for N,rep in ((4000,4),):
        gams=[]
        for r_ in range(rep):
            v=rng.normal(size=K)+1j*rng.normal(size=K); s=0
            for k in range(N):
                t=grid[rng.integers(4096)]
                if t not in Lg: Lg[t]=L(t)
                v=Lg[t]@v; nv=np.linalg.norm(v); s+=np.log(nv); v/=nv
            gams.append(np.exp(s/N))
        print('  Lyapunov e^gamma (iid uniform tau), runs:',[round(g,4) for g in gams],flush=True)
    out[b]=dict(max_r=rs[i],tau_max=ts[i],lyap=gams)
json.dump(out,open('logs/lyap.json','w'),indent=1)
