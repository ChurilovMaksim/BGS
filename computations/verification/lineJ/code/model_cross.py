"""[N] leading-term model of the frozen d=7 cross term (both rho=(+-2,8)) vs exact-law (zpred) values.
cross(rho) = sum_{t in M} 2 Re(conj(om_t Z0/d) Delta_t) = 2 Re(conj(Z0) sum_C Zhat_C W_C(rho,m))."""
import numpy as np, json, sys, math
sys.path.insert(0,'/workspace/bgs-lineI/dom_v3')
from law import mdata
LAM=3+2*np.sqrt(2); d=7; mus=1.3572399242659728-1.3516424762972736j
def e(x): return np.exp(2j*np.pi*x)
gx,gy=np.meshgrid(np.arange(d),np.arange(d),indexing='ij'); Nm=(gx*gx-2*gy*gy)%d
G=np.zeros((d,d,d),complex)
for t in range(d):
    for bx in range(d):
        for by in range(d): G[t,bx,by]=np.exp(-2j*np.pi*((t*Nm+2*(bx*gx+2*by*gy))%d)/d).sum()
cls=['1:3','2:1','0:1','1:2','1:5','0:3','1:0','0:2']
def orbit(bx,by):
    o=set(); x,y=bx,by
    for i in range(3):
        o.add((x%7,y%7)); o.add((-x%7,-y%7)); x,y=(3*x+4*y)%7,(2*x+3*y)%7
    return o
orb={c:orbit(*map(int,c.split(':'))) for c in cls}
assert sum(len(v) for v in orb.values())==48
def members(m,a):
    D=mdata(m); h=D['h']; yp=D['yp']; assert h%7==0
    nu0=next(x for x in [((a//2)*pow(4,-1,h))%h+s*h for s in (0,1)] if x%2==1)
    ts=[]
    for j in range(1,d):
        nu=(nu0+(2*h//d)*j)%(2*h)
        if math.gcd(nu,2*h)==1: ts.append((j*yp)%d)
    return ts,D
def W(m,a):
    ts,D=members(m,a)
    return {c:sum(np.conj(G[t,0,0])*sum(G[t,bx,by] for (bx,by) in orb[c]) for t in ts)/d**4 for c in cls},ts
if __name__=='__main__':
    for m in (39,63,81,99,105,117,123):
        tot=0
        for a in (2,-2):
            Zh=np.load(f'/workspace/bgs-lineI/data/zpred_d7_{a}_8_m{m}_K40.npy'); Z0=Zh[0,0]
            Wc,ts=W(m,a)
            cr=2*np.real(np.conj(Z0)*sum(Zh[tuple(map(int,c.split(':')))]*Wc[c] for c in cls))
            # direct from zpred formula
            Zn=Zh.copy(); Zn[0,0]=0; cr2=0
            for t in ts:
                om=G[t,0,0]/d; De=np.sum(Zn*G[t])/d**2; cr2+=2*np.real(np.conj(om*Z0/d)*De)
            h=mdata(m)['h']
            print(m,a,'n_mem',len(ts),'cross',cr,'direct',cr2,'cross/(m h)',cr/(m*h),' |W|:',{c:round(abs(Wc[c]),4) for c in ('1:3','2:1','0:1')})
            tot+=cr
        print('   total cross/(m h)',tot/(m*h))
