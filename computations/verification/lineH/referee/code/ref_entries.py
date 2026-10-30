"""Referee: independent recomputation of Galerkin entries of the certified matrices.
ghat by FFT of exp(i eta f_B) with f_B taken from lineB/common/model.py fCoeff(k,0) (not from ghat_arb);
Taylor coefficients by FFT on |w|=1 (not the triangular M*C product); rounding f_n(c) in float with margin check."""
import sys, numpy as np, importlib.util
spec=importlib.util.spec_from_file_location('model','/workspace/bgs-int/BGS/computations/verification/lineB/common/model.py')
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
LAM=3+2*np.sqrt(2); c0=1/(LAM-1/LAM); eta=2.0; s=-1; gam=38; lami=32; inv2=25; rho=0.85
NF=1<<14; q=np.arange(NF)/NF
f=sum(mod.fCoeff(k,0)*np.exp(2j*np.pi*k*q) for k in range(-9,10)); assert abs(f.imag).max()<1e-14
G=np.fft.fft(np.exp(1j*eta*f.real))/NF; gh=lambda n: G[n%NF]
NW=512; wpts=np.exp(2j*np.pi*np.arange(NW)/NW)
def build_meta(typ):
    K0=2; Rc=K0 if typ=='V' else K0-0.5
    cores=[c for c in (np.arange(-2,3) if typ=='V' else np.arange(-1.5,2,1.0))]
    K,K2=(30,24) if typ=='V' else (22,18)
    Kc={c:(K2 if abs(c)>Rc-1 else K) for c in cores}; off={}; o=0
    for c in cores: off[c]=o; o+=49*Kc[c]
    return cores,Kc,off,o
def target(typ,c,n):
    x=n/7
    if typ=='V':
        y=(c+x)/LAM; j=np.floor(y+0.5); assert abs(y+0.5-j)>1e-9 and abs(y+0.5-j-1)>1e-9; return j
    y1=(c-0.5+x)/LAM; y2=(c+0.5+x)/LAM; j1=np.floor(y1+0.5); j2=np.floor(y2+0.5)
    if j2!=j1+1: return None
    return j1+0.5
def entry(typ,b,c,so,l,cp,sg,k):
    tot=0
    for n in range(-150,151):
        t=target(typ,c,n)
        if t is None or t!=cp or (lami*(sg+n))%49!=so: continue
        x=n/7
        w=gh(n)*np.exp(2j*np.pi*(s*c0*x*x/2+b*n/8))*np.exp(2j*np.pi*gam*((n*sg+inv2*n*n)%49)/49)
        F=np.exp(2j*np.pi*s*c0*x*(c+rho*wpts))*(((c+rho*wpts+x)/LAM-cp)/rho)**k
        coef=np.fft.fft(F)[l]/NW
        tot+=w*coef
    return tot
rng=np.random.default_rng(12345)
for typ,pre,b in (('V','/workspace/bgs-lineH/data/prodV',0),('E','/workspace/bgs-lineH/data/prodE',2)):
    A=np.load(f'{pre}_b{b}_mid.npy',mmap_mode='r'); cores,Kc,off,D=build_meta(typ); assert D==A.shape[0]
    mx=0; mxabs=0; cnt=0; nz=0
    # sample: pick random nonzero entries and random entries
    nzidx=[]
    while len(nzidx)<40:
        i,j=rng.integers(0,D,2)
        if abs(A[i,j])>1e-6: nzidx.append((i,j))
    for i,j in nzidx+[tuple(rng.integers(0,D,2)) for _ in range(20)]:
        def dec(idx):
            for c in cores[::-1]:
                if idx>=off[c]: r=idx-off[c]; return c, r//Kc[c], r%Kc[c]
        c,so,l=dec(i); cp,sg,k=dec(j)
        v=entry(typ,b,c,so,l,cp,sg,k); d=abs(v-A[i,j]); mx=max(mx,d); mxabs=max(mxabs,abs(A[i,j])); cnt+=1
    print(typ,'sector',b,'entries checked',cnt,'max |A_ref - A_mid| =',mx,'max|A|',mxabs,flush=True)
