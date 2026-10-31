"""[N] leading model: total d=7 cross (both rho) ~ 2 c_m^2 Re( sum_C B_C(m) xi_C^m ), xi_C = mu* mu_{C,+}."""
import numpy as np, json, sys
sys.path.insert(0,'/workspace/bgs-lineJ/code')
from model_cross import W, cls, mdata, LAM, mus, e
sec=json.load(open('logs/sectors_exact.json'))['cases']
def case(m): return {9:9,15:15,21:21,3:27}[m%24]
top={}   # (a,C) -> (sector, mu)
for a in (2,-2):
    for j,c in enumerate(cls):
        best=None
        for S in (0,2,4,6):
            ev=np.linalg.eigvals(np.load(f'data/sec/V_{a}_s{S}_b{j}_mid.npy')); z=ev[np.argmax(abs(ev))]
            if best is None or abs(z)>abs(best[1]): best=(S,z)
        top[(a,c)]=best
def kappa(m):
    D=mdata(m); h=D['h']; yp=D['yp']
    nus=next(x for x in [((-1)*pow(4,-1,h))%h+s*h for s in (0,1)] if x%2==1)
    return (((-4*nus-1)//h)*yp)%8
def B(m,C):
    kap=kappa(m); c4=-e(kap/8)/2; c0=e(kap/8)/2
    Wp,_=W(m,2); Wm,_=W(m,-2)
    Sp,mp=top[(2,C)]; Sm,mm=top[(-2,C)]
    cp=complex(sec[f'{case(m)},2']['c'][str(Sp)]['c']); cm=complex(sec[f'{case(m)},-2']['c'][str(Sm)]['c'])
    assert abs(mm**3-np.conj(mp)**3)<1e-9
    return c0*cp*Wp[C] + c4*np.conj(cm*Wm[C]), mus*mp
if __name__=='__main__':
    for m in (39,63,81,99,105,117,123):
        cm=1-LAM**-m; h=mdata(m)['h']
        model=0; parts={}
        for C in ('1:3','2:1','0:1','1:2','1:5','0:3'):
            b,xi=B(m,C); v=2*cm*cm*np.real(b*xi**m); model+=v; parts[C]=(abs(b),v/(m*h))
        ex=0
        for a in (2,-2):
            Zh=np.load(f'/workspace/bgs-lineI/data/zpred_d7_{a}_8_m{m}_K40.npy'); Wc,_=W(m,a)
            ex+=2*np.real(np.conj(Zh[0,0])*sum(Zh[tuple(map(int,c.split(':')))]*Wc[c] for c in cls))
        print(m,'exact/(mh)',ex/(m*h),'model/(mh)',model/(m*h),{k:(round(v[0],4),f'{v[1]:.3g}') for k,v in parts.items()})
