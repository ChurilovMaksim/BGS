"""N17b (2) [N; TW law L=8,K=16]: Dev_d(rho) at every included level d | h_m (d <= DMAX) via the proved member formula TRACE-212 (I2'):
  |Z_m(nu_rho + 2hj/d)|^2 = |sum_{beta mod d} e(tbar Nm(beta)/d) Zhat(beta)|^2 / d^2,  t = j*y' mod d unit  (|G_d(t)| = d),
with Zhat(beta) = twisted sums at nu_rho (twist tau_i = Tr(beta lam^i)/d), reduced over lambda-orbits and beta -> -beta, beta -> beta'.
Members: gcd(j,d)=1 and nu unit mod 2h (all divisors <= sqrt h are included levels here). usage: d_g3dev.py m DMAX"""
import sys, json, math, time, numpy as np, warnings
warnings.filterwarnings('ignore')
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
from sympy import divisors, totient
m=int(sys.argv[1]); DMAX=int(sys.argv[2])
p=m//3; x,y=1,1
for _ in range(p-1): x,y=x+2*y,x+y
hp=x
md=mdata(m); yp=md['yp']
out=dict(m=m,DMAX=DMAX,rows=[])
for sg in (1,-1):
    h,nu0=nu_rho(m,sg); M=2*h; phi=int(totient(M)); tw=TW(m,nu0,L=8,K=16)
    Z0=Zbatch(tw,np.zeros((1,m)))[0]; Z02=abs(Z0)**2
    for d in divisors(h):
        if d<=1 or d*d>h or d>DMAX: continue
        if Z02/d/d<4*m: out['rows'].append(dict(rho=[2*sg,8],d=int(d),included=False)); continue
        cls='hp' if d==hp else ('hp-div' if hp%d==0 else ('inherited' if d%hp==0 else ('K' if (h//hp)%d==0 else 'mixed')))
        t0=time.time(); pw=lam_pows(m,d)
        bx,by=np.meshgrid(np.arange(d),np.arange(d),indexing='ij'); bx=bx.ravel(); by=by.ravel()
        best=bx*d+by; cx,cy=bx.copy(),by.copy()
        for i in range(m):
            for (sx,sy) in [(1,1),(-1,-1),(1,-1),(-1,1)]:
                best=np.minimum(best,((sx*cx)%d)*d+((sy*cy)%d))
            cx,cy=(3*cx+4*cy)%d,(2*cx+3*cy)%d
        reps,inv=np.unique(best,return_inverse=True)
        T=np.array([taus_of((int(r//d),int(r%d)),pw,d) for r in reps]); Zr=np.zeros(len(reps),complex)
        for i in range(0,len(reps),64): Zr[i:i+64]=Zbatch(tw,T[i:i+64])
        Zh=Zr[inv]; Nm=(bx*bx-2*by*by)%d
        A=np.zeros(d,complex); np.add.at(A,Nm,Zh)
        S=0.0; n=0; mx=0.0; us=np.arange(d)
        for j in range(1,d):
            if math.gcd(j,d)!=1: continue
            nu=(nu0+(M//d)*j)%M
            if math.gcd(nu,M)!=1: continue
            t=(j*yp)%d; tb=pow(t,-1,d)
            z=abs(np.sum(np.exp(2j*np.pi*((tb*us)%d)/d)*A))**2/d**2
            S+=z; n+=1; mx=max(mx,z)
        main=n*Z02/d/d; dev=S-main
        row=dict(rho=[2*sg,8],d=int(d),cls=cls,included=True,n_d=n,orbits=int(len(reps)),Zrho2=Z02,Dev=dev,Dev_over_phim=dev/phi/m,
                 main_over_phim=main/phi/m,Dev_rel_main=dev/main,max_member_over_mainper=mx/(Z02/d/d),sec=round(time.time()-t0,1))
        out['rows'].append(row); print(json.dumps(row),flush=True)
    out[f'phi']=phi
json.dump(out,open(f'logs/d_g3dev_m{m}.json','w'),indent=1)
