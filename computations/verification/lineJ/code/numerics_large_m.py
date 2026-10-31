"""[N] direct numerical check of the frozen d=7, rho=(+-2,8) deviation D7(m) = sum_rho sum_{t in M_rho} (|Z_t|^2 - |Z0|^2/49)
for m = 3 mod 6, 201..453, using the exact sector law (float spectra of the certified D=1980 V and E sector blocks) and Line F's Z0
leading term (|eps|<=1506 is ~1e-80 relative here).  Also per-rho cross, the 1:3 parts (which cancel), and the 2:1 leading model."""
import numpy as np, json, os, sys
sys.path.insert(0,'/workspace/bgs-lineJ/code')
from model_cross import W, members, cls, mdata, G, orb
LAM=3+2*np.sqrt(2); d=7; mus=1.3572399242659728-1.3516424762972736j
def e(x): return np.exp(2j*np.pi*x)
sec=json.load(open('logs/sectors_exact.json'))['cases']
def case(m): return {9:9,15:15,21:21,3:27}[m%24]
cache='data/cert/spectra.npz'
if os.path.exists(cache): SP=dict(np.load(cache))
else:
    SP={}
    for A in (2,-2):
        for S in (0,2,4,6):
            for T in 'VE':
                for b in range(8):
                    SP[f'{T}{A}_{S}_{b}']=np.linalg.eigvals(np.load(f'data/cert/{T}_{A}_s{S}_b{b}_mid.npy'))
    np.savez(cache,**SP)
def kappa(m):
    D=mdata(m); h=D['h']; yp=D['yp']
    nus=next(x for x in [((-1)*pow(4,-1,h))%h+s*h for s in (0,1)] if x%2==1)
    return (((-4*nus-1)//h)*yp)%8
def Zhat(m,A,b):
    cs=sec[f'{case(m)},{A}']['c']
    return (1-LAM**-m)*sum(complex(cs[str(S)]['c'])*(np.sum(SP[f'V{A}_{S}_{b}'].astype(complex)**m)-np.sum(SP[f'E{A}_{S}_{b}'].astype(complex)**m))/3 for S in (0,2,4,6))
rows=[]
for m in range(201,454,6):
    D=mdata(m); h=D['h']; cm=1-LAM**-m; kap=kappa(m)
    Z0={-2:cm*(-e(kap/8)/2)*mus**m, 2:np.conj(cm*(e(kap/8)/2)*mus**m)}
    tot=0; sq=0; per={}; p13={}
    for A in (2,-2):
        Wc,ts=W(m,A); Zh={c:Zhat(m,A,b) for b,c in enumerate(cls)}
        cr=2*np.real(np.conj(Z0[A])*sum(Zh[c]*Wc[c] for c in cls)); per[A]=cr; tot+=cr
        p13[A]=2*np.real(np.conj(Z0[A])*Zh['1:3']*Wc['1:3'])
        for t in ts:
            De=sum(Zh[c]*sum(G[t,bx,by] for (bx,by) in orb[c]) for c in cls)/d**2; sq+=abs(De)**2
    D7=tot+sq
    rows.append(dict(m=m,res168=m%168,cross_plus=per[2]/(m*h),cross_minus=per[-2]/(m*h),c13_plus=p13[2]/(m*h),c13_minus=p13[-2]/(m*h),
                     square=sq/(m*h),D7_over_mh=D7/(m*h)))
    r=rows[-1]; print(f"m={m:3d} r168={m%168:3d}  cross+/(mh)={r['cross_plus']:+.3e} cross-/(mh)={r['cross_minus']:+.3e}  1:3 parts {r['c13_plus']:+.3e} {r['c13_minus']:+.3e}  square/(mh)={r['square']:.1e}  D7/(mh)={r['D7_over_mh']:+.4e}",flush=True)
json.dump(rows,open('logs/numerics_large_m.json','w'),indent=0)
