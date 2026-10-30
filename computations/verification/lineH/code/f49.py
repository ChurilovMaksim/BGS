"""Line H: float builder for lifted 49-state operators (Line B kick), own implementation.
Layout: index = ((c_index)*49 + sigma)*K + i.  Operator  (V Phi)_c = sum_n w_b(n) [M_n C_n]_{c<-c'} (x) DP_n^T  (TRACE-194 convention)."""
import sys, math, numpy as np
sys.path.insert(0,'/workspace/bgs-next/lineE/step2')
from lawlib import law_params, mdata, nu_res
from scipy.special import gammaln
LAM=3+2*math.sqrt(2); C0=1/(LAM-1/LAM)
def rnd(x): return int(math.floor(x+0.5))
def rC(k): return {0:1.0,1:.5,-1:.5,7:-.5,-7:-.5,6:-.25,-6:-.25,8:-.25,-8:-.25}.get(k,0.0)
def fdiag():
    C={}
    for k in range(-9,10):
        v=(0.5 if k in (7,-7) else 0)+rC(k)/10+(rC(k-1)-rC(k+1))/(200j)-(0.1 if k==0 else 0)
        if abs(v)>0: C[k]=complex(v)
    return C
def ghat(eta=2.0,L=60,NF=4096,C=None):
    C=C or fdiag()
    th=np.arange(NF)/NF; f=sum(c*np.exp(2j*np.pi*k*th) for k,c in C.items()).real
    g=np.fft.fft(np.exp(1j*eta*f))/NF
    return {n:g[n%NF] for n in range(-L,L+1)}
def blockmat(x,cout,cin,rout,rin,coef,K):
    A=rout/(LAM*rin); B=(cout+x-LAM*cin)/(LAM*rin)
    i=np.arange(K)[:,None]; l=np.arange(K)[None,:]; e=l-i; ee=np.where(e>=0,e,0)
    logb=gammaln(l+1)-gammaln(i+1)-gammaln(ee+1)
    Cm=np.where(e>=0, np.exp(logb)*A**i*(np.power(B,ee) if B!=0 else (ee==0)*1.0),0.0)
    z=2j*np.pi*coef*x*rout; d=i-l; dd=np.where(d>=0,d,0)
    M=np.where(d>=0, z**dd/np.exp(gammaln(dd+1)),0)
    return np.exp(2j*np.pi*coef*x*cout)*(M@Cm)
def DPT(n,P):
    A2=49; g=P['gamma']; li=P['lami']; inv2=pow(2,-1,A2)
    sg=np.arange(A2); tgt=(li*(sg+n))%A2; ph=np.exp(2j*np.pi*((g*(n*sg+inv2*n*n))%A2)/A2)
    return tgt,ph   # Mx[sg,tgt[sg]]=ph[sg]; we use Mx^T: out[tgt[sg]] += ph[sg]*in[sg]
def build(G,s,b,typ,K0,rho,K,P=None,nst=49):
    P=P or law_params(5,7,s)
    cent=[c for c in range(-K0,K0+1)] if typ=='V' else [e+0.5 for e in range(-K0,K0)]
    nc=len(cent); D=nc*nst*K; A=np.zeros((D,D),complex)
    for n,gn in G.items():
        if gn==0: continue
        x=n/7; w=gn*np.exp(2j*np.pi*(s*C0*x*x/2+b*n/8)); tgt,ph=DPT(n,P)
        for ci,c in enumerate(cent):
            if typ=='V': j=rnd((c+x)/LAM); cj=j
            else:
                lo=c-0.5; j=rnd((lo+x)/LAM); j2=rnd((lo+1+x)/LAM)
                if j2!=j+1: continue
                cj=j+0.5
            if cj not in cent: continue
            cjI=cent.index(cj); Bm=w*blockmat(x,c,cj,rho,rho,s*C0,K)
            for sg in range(nst):
                # Mx^T entry [tgt[sg], sg] = ph[sg]: row sigma_out = tgt[sg], col sigma_in = sg   (per Line E/F kron(R, DP.T))
                r0=(ci*nst+tgt[sg])*K; c0=(cjI*nst+sg)*K
                A[r0:r0+K,c0:c0+K]+=ph[sg]*Bm
    return A
def csec(kappa): return [np.mean([np.exp(2j*np.pi*(kappa*t*t-b*t)/8) for t in range(8)]) for b in range(8)]
