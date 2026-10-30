"""Rigorous Fourier coefficients of g = exp(i eta f_B), f_B the Line B diagonal kick (exact rational coefficients, same rule as
lineB/common/model.py fCoeff(k,0); cf. lineE/step2/cert_class.py fdiag_exact).
f_B(q) = sum_{k=-9}^{9} C_k e(kq), C_{-k} = conj(C_k), C_0 = 0  =>  f_B = sum_{k>=1} 2|C_k| cos(2 pi k q + phi_k).
exp(i eta 2|C_k| cos t) = sum_j i^j J_j(2 eta |C_k|) e^{i j t}  (Jacobi-Anger), so ghat = *-convolution over k of the sequences
 a_k(k j) = i^j J_j(x_k) u_k^j,  x_k = 2 eta |C_k|, u_k = C_k/|C_k|.
Truncation |j|<=J_k; exact weighted-l1 error: for weight e^{a|n|} (submultiplicative),
 sum_n |ghat(n)-ghat_T(n)| e^{a|n|} <= prod_k S_k - prod_k S_k^T,  S_k^T = sum_{|j|<=J_k}|J_j(x_k)|e^{a k|j|},
 S_k <= S_k^T + tau_k,  tau_k = 2 t^{J+1}/(J+1)!/(1-t/(J+2)),  t = x_k e^{a k}/2   (|J_j(x)| <= (x/2)^j/j!, DLMF 10.14.4)."""
from fractions import Fraction as Fr
from flint import arb, acb, ctx
def rC(k): return {0:Fr(1),1:Fr(1,2),-1:Fr(1,2),7:Fr(-1,2),-7:Fr(-1,2),6:Fr(-1,4),-6:Fr(-1,4),8:Fr(-1,4),-8:Fr(-1,4)}.get(k,Fr(0))
def fdiag_exact():
    C={}
    for k in range(-9,10):
        re=(Fr(1,2) if k in (7,-7) else Fr(0))+rC(k)/10-(Fr(1,10) if k==0 else Fr(0))
        im=-(rC(k-1)-rC(k+1))/200
        if re or im: C[k]=(re,im)
    return C
def A(fr): return arb(fr.numerator)/fr.denominator
def ghat_arb(eta_fr=Fr(2), J=None, a_list=(0,)):
    """returns (G, err, tail) : G dict n -> acb (truncated convolution, exact up to ball radius), err[a] = weighted l1 error bound
    of truncation for weight e^{a|n|} (a given as arb-convertible strings), so |ghat(n)-G[n]| <= err[0]*e^{-0}."""
    C=fdiag_exact(); assert 0 not in C
    for k,(re,im) in C.items(): assert C[-k]==(re,-im)
    eta=A(eta_fr); I=acb(0,1)
    seqs=[]
    for k in sorted(kk for kk in C if kk>0):
        re,im=C[k]; mod=(A(re)**2+A(im)**2).sqrt(); u=acb(A(re),A(im))/mod; x=2*eta*mod
        Jk=(J or {}).get(k,40 if k==7 else 14)
        seq={}
        for j in range(-Jk,Jk+1):
            Jj=x.bessel_j(arb(abs(j)))*(1 if (j>=0 or j%2==0) else -1)   # J_{-j}=(-1)^j J_j
            seq[k*j]=(I**(j%4))*Jj*(u**j if j>=0 else (u.conjugate())**(-j))
        seqs.append((k,x,Jk,seq))
    G={0:acb(1)}
    for k,x,Jk,seq in seqs:
        NG={}
        for n1,v1 in G.items():
            for n2,v2 in seq.items():
                NG[n1+n2]=NG.get(n1+n2,acb(0))+v1*v2
        G=NG
    err={}
    for a in a_list:
        a=arb(a); ST_l=[]; tau_l=[]
        for k,x,Jk,seq in seqs:
            ST=sum((abs(seq[k*j])*(a*k*abs(j)).exp() for j in range(-Jk,Jk+1)),arb(0))
            t=x*(a*k).exp()/2; f=arb(1)
            for i in range(1,Jk+2): f*=i
            q=t/(Jk+2); assert q<1
            tau=2*t**(Jk+1)/f/(1-q)
            ST_l.append(ST); tau_l.append(tau)
        # telescoping: prod(ST+tau)-prod(ST) = sum_k tau_k prod_{k'<k} ST_k' prod_{k'>k} (ST_k'+tau_k')
        e_=arb(0)
        for k in range(len(seqs)):
            pr=tau_l[k]
            for kk in range(k): pr*=ST_l[kk]
            for kk in range(k+1,len(seqs)): pr*=ST_l[kk]+tau_l[kk]
            e_+=pr
        err[str(a.mid())]=e_
    return G,err
if __name__=='__main__':
    import numpy as np, sys
    ctx.prec=128
    G,err=ghat_arb(a_list=(0,'0.25','0.4'))
    sys.path.insert(0,'/workspace/bgs-lineH/code'); from f49 import ghat
    Gf=ghat(2.0,200,NF=8192)
    mx=max(abs(complex(G.get(n,acb(0)).mid())-Gf[n]) for n in range(-200,201))
    print('support',min(G),max(G),'err',{k:float(v.upper()) for k,v in err.items()},'max|arb-fft|',mx)
    print('max rad',max(float(v.rad()) for v in G.values()))
    print('ghat(0),(7),(1),(-1):',[complex(G[n].mid()) for n in (0,7,-7,1,-1,6,8)])
