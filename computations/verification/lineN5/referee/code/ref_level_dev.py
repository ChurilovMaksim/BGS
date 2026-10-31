"""Referee (Grok Bot) [N]: exact level-q deviation of the frozen R' (TRACE-206) at q = h_p, m = 3p, from the full
twisted-sum array Zhat(beta), beta in O/q (N2 d_Zh arrays; spot-rechecked here with the twlaw transfer law).
Members: nu = nu0 + (2h/q) j, j = 1..q-1, nu unit (excludes j_b with nu == 0 mod q).  TRACE-212 (I2'):
  Z(nu) = sum_gamma W(gamma) e(-t N(gamma)/q), t = j y' mod q,  W(gamma) = q^-2 sum_beta Zhat(beta) e(-Tr(beta gamma)/q).
Dev_q = sum_members (|Z_nu|^2 - |Z0|^2/q^2)  (frozen main term n_q |Z_rho|^2/q^2).  Split Zhat by beta-classes
{0}, 16D=1 family, other isotropic, non-isotropic; report cross (2 Re conj(main) * part) and square parts.
usage: m q"""
import sys, json, math, numpy as np
sys.path.insert(0,'/workspace/bgs-lineL/L2/code'); sys.path.insert(0,'/workspace/bgs-lineI/code')
from law import mdata
from twlaw import TW, lam_pows, taus_of
m,q=int(sys.argv[1]),int(sys.argv[2]); s2=math.sqrt(2)
Zh=np.load(f'/workspace/bgs-lineN/N2/logs/d_Zh_m{m}_q{q}_s1.npy'); Z0=Zh[0,0]
d=mdata(m); h=d['h']; yp=d['yp']; M=2*h; assert h%q==0
nu0=next(x for x in range(1,M,2) if (8*x-2)%M==0)
# spot re-check of the array with the transfer law at higher truncation
tw=TW(m,nu0,L=10,K=40); pw=lam_pows(m,q); rng=np.random.default_rng(1)
chk=[(0,0)]+[tuple(int(v) for v in rng.integers(0,q,2)) for _ in range(3)]
r0=[t for t in range(q) if (t*t-2)%q==0][0]; chk.append(((r0*5)%q,5))
spot=[(b,abs(tw.Z(taus_of(b,pw,q))-Zh[b])/max(1,abs(Zh[b]))) for b in chk]
# classes
bx=np.arange(q)[:,None]; by=np.arange(q)[None,:]
iso=((bx*bx-2*by*by)%q==0); iso[0,0]=False
R=int(4*math.sqrt(q))+40; a=np.arange(-R,R+1)[:,None]; b=np.arange(-R,R+1)[None,:]; w=b/2+a*s2/4; wc=b/2-a*s2/4
fam=np.zeros((q,q),bool); depth={}
for (x,y) in zip(*np.nonzero(iso)):
    yy=(x+y*s2)/q; yc=(x-y*s2)/q; k=int(round(16*q*np.min(np.abs((yy-0.25-w)*(yc-0.25-wc)))))
    depth[(int(x),int(y))]=k
    if k==1: fam[x,y]=True
zero=np.zeros((q,q),bool); zero[0,0]=True
non=~(iso|zero)
G=np.arange(q); Ng=(G[:,None]**2-2*G[None,:]**2)%q
def Zt_of(mask):
    A=np.where(mask,Zh,0); F=np.fft.fft2(A)
    Wg=F[(2*G)%q][:,(4*G)%q]/q**2           # W(gx,gy)
    Wu=np.bincount(Ng.ravel(),weights=Wg.real.ravel(),minlength=q)+1j*np.bincount(Ng.ravel(),weights=Wg.imag.ravel(),minlength=q)
    t=np.arange(q); return np.exp(-2j*np.pi*np.outer(t,np.arange(q))/q)@Wu   # Z_t for all t mod q
parts={'main':Zt_of(zero),'fam':Zt_of(fam),'iso_rest':Zt_of(iso&~fam),'noniso':Zt_of(non)}
tot=sum(parts.values())
# members
step=(2*h//q)
jb=[j for j in range(1,q) if (nu0+step*j)%q==0]; members=[j for j in range(1,q) if (nu0+step*j)%q!=0]
tt=[(j*yp)%q for j in members]
# direct check of I2' for two members
dchk=[]   # I2' convention is checked by brute force at m=5 (code/ref_i2_conv.py)
main=parts['main'][tt]; T=tot[tt]
Dev=float(np.sum(np.abs(T)**2)-len(tt)*abs(Z0)**2/q**2)
res=dict(m=m,q=q,h=h,nu0=nu0,absZ0=float(abs(Z0)),spot_relerr=[float(e) for _,e in spot],I2prime_relerr=[float(e) for e in dchk],
  main_modulus_check=float(np.max(np.abs(np.abs(main)-abs(Z0)/q))/(abs(Z0)/q)),n_members=len(tt),j_b=jb,
  Dev=Dev,Dev_over_mainterm=Dev/(len(tt)*abs(Z0)**2/q**2),
  cross={k:float(2*np.sum((np.conj(main)*v[tt]).real)) for k,v in parts.items() if k!='main'},
  square=float(np.sum(np.abs(T-main)**2)),
  n_fam=int(fam.sum()),n_iso=int(iso.sum()),
  X_fam=complex(Zh[fam].sum()/Z0).__repr__(),X_iso_all=complex(Zh[iso].sum()/Z0).__repr__(),
  fam_ratio_phases=sorted(set(round(float(np.angle(v/Z0)),6) for v in Zh[fam])),fam_abs_ratio=sorted(set(round(float(abs(v/Z0)),9) for v in Zh[fam])))
res['cross_total']=sum(res['cross'].values())
from collections import defaultdict
byk=defaultdict(complex)
for (x,y),k in depth.items(): byk[k]+=Zh[x,y]/Z0
res['X_by_16D_first']={int(k):repr(complex(v)) for k,v in sorted(byk.items())[:12]}
X=Zh[iso].sum()/Z0; res['pred_Dev_iso_only']=float(len(tt)*abs(Z0)**2/q**2*(abs(1+X)**2-1))
print(json.dumps(res,indent=1)); json.dump(res,open(f'logs/ref_level_dev_m{m}_q{q}.json','w'),indent=1)
