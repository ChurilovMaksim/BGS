"""N2 (C2) [N]: JSR lower bounds from ALL periodic points of the cat map of period n<=NMAX (exact rational points
(A^n-I)^{-1}Z^2/Z^2), and upper-side estimates sup_y ||P_k(y)||^{1/k} by random sampling + local refinement,
for the lifted Line-F operators with twist e(n tau).  usage: c2_jsr_periodic.py typ K0 r K beta N0 NMAX kup nsamp"""
import sys, math, json, time, numpy as np
from fractions import Fraction
sys.path.insert(0,'/workspace/bgs-lineF/code')
from lift import ops, wk1
typ=sys.argv[1]; K0=int(sys.argv[2]); r=float(sys.argv[3]); K=int(sys.argv[4]); beta=float(sys.argv[5])
N0=int(sys.argv[6]); NMAX=int(sys.argv[7]); kup=[int(x) for x in sys.argv[8].split(',')]; nsamp=int(sys.argv[9])
Bn={}
for n in range(-N0,N0+1):
    V,E=ops(lambda m,n=n: 1.0 if m==n else 0.0, N0,K0,r,r,K,beta=beta); Bn[n]=V if typ=='V' else E
ns=np.array(sorted(Bn)); Bst=np.stack([Bn[n] for n in ns])
def Lmat(w,tau): return np.tensordot(w*np.exp(2j*np.pi*ns*tau),Bst,axes=1)
def periodic_points(n):
    # solve (A^n - I) x = z mod 1 ; enumerate x = (A^n-I)^{-1} z for z in Z^2 / (A^n-I)Z^2
    A=np.array([[0,1],[-1,6]],dtype=object); P=np.eye(2,dtype=object)
    for _ in range(n): P=P.dot(A)
    M=P-np.eye(2,dtype=object); det=int(M[0,0]*M[1,1]-M[0,1]*M[1,0]); D=abs(det)
    # points are (1/D) * adj(M) z mod 1, z ranges over Z^2 mod D -> collect unique
    adj=np.array([[M[1,1],-M[0,1]],[-M[1,0],M[0,0]]],dtype=object)
    S=set()
    for z0 in range(D):
        for z1 in range(D):
            x0=(int(adj[0,0])*z0+int(adj[0,1])*z1)%D; x1=(int(adj[1,0])*z0+int(adj[1,1])*z1)%D
            S.add((x0,x1))
            if len(S)==D: break
        if len(S)==D: break
    return D,[(Fraction(a,D),Fraction(b,D)) for a,b in S]
res=dict(typ=typ,K0=K0,r=r,K=K,beta=beta,N0=N0,sectors={})
rng=np.random.default_rng(7); t0=time.time()
for a in (4,0,2):
    w0=wk1(2.0,a); w=np.array([w0(int(n)) for n in ns])
    L0=Lmat(w,0.0); rho0=float(max(abs(np.linalg.eigvals(L0))))
    per=[]
    for n in range(1,NMAX+1):
        D,pts=periodic_points(n); best=0.0; argb=None
        for (x0,x1) in pts:
            t0_,t1_=x0,x1; P=np.eye(L0.shape[0],dtype=complex)
            for i in range(n):
                P=Lmat(w,float(t0_))@P; t0_,t1_=t1_,(6*t1_-t0_)%1
            rr=float(max(abs(np.linalg.eigvals(P))))**(1/n)
            if rr>best: best=rr; argb=(str(x0),str(x1))
        per.append(dict(n=n,count=D,max_specrad_rate=best,arg=argb))
    # sampling sup ||P_k(y)||^{1/k}
    sup={}
    for k in kup:
        def nr(y):
            t0_,t1_=y; P=np.eye(L0.shape[0],dtype=complex)
            for i in range(k): P=Lmat(w,t0_)@P; t0_,t1_=t1_,(6*t1_-t0_)%1.0
            return float(np.linalg.norm(P,2))**(1/k)
        ys=[(0.0,0.0)]+[tuple(rng.random(2)) for _ in range(nsamp)]
        vals=[(nr(y),y) for y in ys]; vals.sort(reverse=True)
        top=vals[:5]; bestv,besty=top[0]
        for v,y in top:   # local refinement
            step=0.02
            while step>1e-4:
                imp=False
                for d0,d1 in ((step,0),(-step,0),(0,step),(0,-step)):
                    y2=((y[0]+d0)%1,(y[1]+d1)%1); v2=nr(y2)
                    if v2>v: v,y,imp=v2,y2,True
                if not imp: step/=2
            if v>bestv: bestv,besty=v,y
        sup[k]=dict(untwisted=nr((0.0,0.0)),sup_est=bestv,argmax=besty)
    res['sectors'][a]=dict(rho_untwisted=rho0,periodic=per,sup=sup)
    print(json.dumps(dict(a=a,rho0=rho0,per=[(d['n'],round(d['max_specrad_rate'],6)) for d in per],
          sup={k:(round(v['untwisted'],5),round(v['sup_est'],5),[round(z,4) for z in v['argmax']]) for k,v in sup.items()},sec=round(time.time()-t0))),flush=True)
json.dump(res,open(f'logs/c2_jsr_{typ}_K0{K0}_r{r}_K{K}_b{beta}_N{NMAX}.json','w'),indent=1)
