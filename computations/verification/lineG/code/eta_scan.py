if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
# Test: is the bulk (non-resonant) F/2m kick-universal at fixed m? Scan k1 kick strength eta.
import sys,os,subprocess,json,numpy as np,time
sys.path.insert(0,'computations/verification/lineE/referee/code')
from aud import data,K1,fvals
from law import mdata, ratrec
from step1b import Z2all
from step1c import divisors
from step1e import PR
res={}
for m in [9,11,13]:
  for eta in [0.5,1.0,2.0,3.0,4.0]:
    h=data(m)['h']; tab=np.exp(1j*eta*fvals(K1,0.5+np.arange(h)/h)).astype(np.complex128)
    tf=f'/tmp/lg_eta_{os.getpid()}.bin'; out=f'/tmp/lg_eta_T_{os.getpid()}.bin'; tab.tofile(tf)
    subprocess.run(['./classes_orb',str(m),str(h),tf,out],check=True,env=dict(os.environ,OMP_NUM_THREADS='2'),stdout=subprocess.DEVNULL)
    T=np.fromfile(out,np.complex128); os.remove(tf); os.remove(out)
    R=Z2all(T,m); nus=np.array([n for n,_ in R]); Z=np.array([z for _,z in R]); phi=len(R)
    dil=np.zeros(phi,bool)
    for d in [d for d in divisors(h) if 1<=d<=h**0.5]:
        M=2*h//d
        for a,b in PR: dil|=((b*nus-a)%M==0)
    hts=np.array([max(abs(ratrec(int(nu),2*h)[0][0]),ratrec(int(nu),2*h)[0][1]) for nu in nus])
    rem=dil|(hts<=32)
    r=dict(m=m,eta=eta,F2m=Z.mean()/(2*m),bulk2m=Z[~rem].mean()/(2*m),rm=float(rem.mean()),Ex2=float(((Z[~rem]/(2*m))**2).mean()))
    print(json.dumps(r),flush=True); res[f'{m}_{eta}']=r
json.dump(res,open('../logs/eta_scan.json','w'))
