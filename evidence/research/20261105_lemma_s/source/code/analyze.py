"""research1105b: assemble level-D member data from level.py npz files (exact I2' member formula).
For a member t (j coprime to D, nu unit mod 2h), with tbar = (j y')^{-1} mod D:
   |Z(nu_j)|^2 = (|Z0|^2/D^2) |1+E(tbar)|^2,   E(s) = sum_{beta!=0} e(s Nm(beta)/D) Zhat(beta)/Z0  (via FFT of A_k).
Dev_D/main_D = <|1+E|^2> - 1 = |1+<E>|^2 - 1 + Var(E);  <E> = sum_k w(k) A_k with w(k) = mean_t e(tbar k/D).
usage: analyze.py m sg D prefix spec1,spec2,...  (classes not given are treated as 0)"""
import sys, json, math, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import nu_rho, mdata
def member_tbars(m,sg,D):
    h,nu0=nu_rho(m,sg); M=2*h; yp=mdata(m)['yp']; ts=[]
    for j in range(1,D):
        if math.gcd(j,D)!=1: continue
        nu=(nu0+(M//D)*j)%M
        if math.gcd(nu,M)!=1: continue
        ts.append(pow((j*yp)%D,-1,D))
    return np.array(ts,np.int64)
def assemble(m,sg,D,prefix,specs,verbose=False):
    tb=member_tbars(m,sg,D); n=len(tb)
    A=np.zeros(D,complex); comp={}; Z0=None
    for s in specs:
        f=np.load(f'{prefix}_{s}.npz'); Z0=complex(f['Z0'])
        isz=(f['bx']==0)&(f['by']==0)
        u=np.where(isz,0,f['w']*f['Zh']/Z0); Nm=f['Nm']
        Ak=np.zeros(D,complex); np.add.at(Ak,Nm,u)
        if not bool(f['sampled']): A+=Ak
        Ehat=D*np.fft.ifft(Ak)          # Ehat[s] = sum_k Ak e(s k/D)
        comp[s]=dict(mean=complex(Ehat[tb].mean()), sum=complex(u.sum()), abs_sum=float(np.abs(u).sum()),
                     max_abs=float(np.abs(f['Zh'][~isz]/Z0).max()) if (~isz).any() else 0.0,
                     var=float(np.var(Ehat[tb])), nrep=int(len(u)), total=int(f['total']), sampled=bool(f['sampled']))
    E=(D*np.fft.ifft(A))[tb]; r=np.abs(1+E)**2
    smean=sum(v['mean'] for v in comp.values() if v['sampled'])
    mE=E.mean()+smean
    out=dict(m=m,sg=sg,D=D,n=n,Z0abs2=abs(Z0)**2,
             comp={k:dict(mean=[v['mean'].real,v['mean'].imag],sum=[v['sum'].real,v['sum'].imag],abs_sum=v['abs_sum'],max_abs=v['max_abs'],var=(v['var'] if not v['sampled'] else None),nrep=v['nrep'],total=v['total'],sampled=v['sampled']) for k,v in comp.items()},
             note='E/var/member stats use exactly enumerated classes only; meanE adds sampled-class means (estimates)',
             meanE=[mE.real,mE.imag], meanE_exact=[E.mean().real,E.mean().imag], varE_exact=float(np.var(E)),
             dev_over_main_exact=float(r.mean()-1), lb_over_main=float(abs(1+mE)**2-1),
             max_member=float(r.max()), min_member=float(r.min()), Dev_exact=float((r.mean()-1)*n*abs(Z0)**2/D**2))
    return out
if __name__=='__main__':
    m,sg,D=map(int,sys.argv[1:4]); prefix=sys.argv[4]; specs=sys.argv[5].split(',')
    print(json.dumps(assemble(m,sg,D,prefix,specs),indent=1))
