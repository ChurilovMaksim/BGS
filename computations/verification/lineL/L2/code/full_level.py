"""Line L2 (c) [N]: full level-q push-forward A(c), c in O/q, from all twisted sums Zhat_beta (one transfer run per lambda-orbit),
then the Theorem K1 quantities D_iso = A(q u qbar) - (2q-1)A_tot/q^2 and E_b(t) = sum_c A(c) e(-N(c)t/q) - A_tot/q for all t in F_q*.
usage: full_level.py m q [sign]"""
import sys, json, time, math; sys.path.insert(0,'/workspace/bgs-lineL/L2/code')
from twlaw import *
m=int(sys.argv[1]); q=int(sys.argv[2]); sg=int(sys.argv[3]) if len(sys.argv)>3 else 1
d=mdata(m); h=d['h']; M=2*h; assert h%q==0 and (h//q)%q!=0
x0=(sg*pow(4,-1,M//2))%(M//2); nu0=min(x for x in (x0,x0+M//2) if x%2==1); assert (8*nu0-2*sg)%M==0
tw=TW(m,nu0,L=8,K=32); pw=lam_pows(m,q)
t0=time.time(); Zh=np.zeros((q,q),complex); seen=np.zeros((q,q),bool); nrun=0
for bx in range(q):
    for by in range(q):
        if seen[bx,by]: continue
        z=tw.Z(taus_of((bx,by),pw,q)); nrun+=1
        x=(bx,by)
        while not seen[x]:
            seen[x]=True; Zh[x]=z; x=((3*x[0]+4*x[1])%q,(2*x[0]+3*x[1])%q)
g=np.arange(q); BX,BY=np.meshgrid(g,g,indexing='ij')
A=np.zeros((q,q),complex)
for cx in range(q):
    ph=np.exp(-2j*np.pi*((2*(BX*cx))%q)/q)
    for cy in range(q):
        A[cx,cy]=(Zh*ph*np.exp(-2j*np.pi*((4*BY*cy)%q)/q)).sum()/q**2
Atot=Zh[0,0]; N=(BX*BX-2*BY*BY)%q
Diso=A[N==0].sum()-(2*q-1)*Atot/q**2
Eb=[ (A*np.exp(-2j*np.pi*((N*t)%q)/q)).sum()-Atot/q for t in range(1,q)]
comb=[abs(Diso-e/q) for e in Eb]
Zn=np.abs(Zh); iso=(N==0); iso[0,0]=False; non=(N!=0)
res=dict(res=f'({2*sg},8)',m=m,q=q,runs=nrun,absZ=abs(Atot),target8_m=1.28359**m,absDiso=abs(Diso),max_absEb_over_q=max(abs(e) for e in Eb)/q,
  max_comb=max(comb),min_comb=min(comb),comb_rate=max(comb)**(1/m),sumA_check=abs(A.sum()-Atot),l2_level=float((np.abs(A)**2).sum()),
  max_noniso_Z=float(Zn[non].max()),max_noniso_rate=float(Zn[non].max()**(1/m)),noniso_meansq=float((Zn[non]**2).mean()),
  slow_beta1=float(abs(Zh[1,0])),sec=round(time.time()-t0,1))
print(json.dumps(res),flush=True)
