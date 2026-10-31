"""Referee [N]: isotropic line sums X_d = sum_{beta iso != 0} Zhat_beta/Z0 at other prime levels d | h_m (m = 3p), exact over lambda-orbits,
and the iso-coherent deviation in W'/m units (both rho, no inherited factor), for comparison with the h_p level.
usage: p d1,d2,..."""
import sys, json, math
sys.path.insert(0,'/workspace/bgs-lineL/L2/code'); sys.path.insert(0,'/workspace/bgs-lineI/code')
from law import mdata
from twlaw import TW, lam_pows, taus_of
from sympy import sqrt_mod, totient
p=int(sys.argv[1]); m=3*p; dd=mdata(m); h=dd['h']; M=2*h; phi=int(totient(2*h))
x0=(pow(4,-1,M//2))%(M//2); nu0=min(x for x in (x0,x0+M//2) if x%2==1)
tw=TW(m,nu0,L=8,K=32); Z0=tw.Z([0.0]*m); out=[]
for d in [int(t) for t in sys.argv[2].split(',')]:
    assert h%d==0
    X=0j; ev=0; mx=0
    for r in sqrt_mod(2,d,all_roots=True):
        r=int(r); seen=set()
        for t in range(1,d):
            if t in seen: continue
            beta=((r*t)%d,t); orb=0; x,y=beta
            while True:      # lambda-orbit on the line (multiplication by lambda maps the line to itself)
                if y in seen: break
                seen.add(y); orb+=1; x,y=(3*x+4*y)%d,(2*x+3*y)%d
            z=tw.Z(taus_of(beta,lam_pows(m,d),d))/Z0; ev+=1; X+=orb*z; mx=max(mx,abs(z))
    dev=(d-2)*abs(Z0)**2/d**2*(2*X.real+abs(X)**2)
    rec=dict(p=p,d=d,evals=ev,X=[X.real,X.imag],max_abs_ratio=mx,Wprime_over_m_iso=2*dev/phi/m); out.append(rec); print(json.dumps(rec),flush=True)
json.dump(out,open(f'logs/ref_other_levels_p{p}.json','w'),indent=1)
