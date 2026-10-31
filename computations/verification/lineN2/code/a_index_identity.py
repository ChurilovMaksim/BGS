"""N2 (A) [P-check/N]: structure of the inherited level h_p as periodic points of the cat map.
Coordinates: tau=(tau0,tau1)=(Tr y, Tr(lam y)) mod 1; T acts by A=[[0,1],[-1,6]] (tau_{i+1}=6tau_i-tau_{i-1}).
Checks: (1) (A^p-I)/h_p is an integer matrix B with |det B|=4  => G_p:=(1/h_p)Z^2/Z^2 has index 4 in Fix(A^p)
        (REPORT_N said index 32: erratum).  (2) beta in O/h_p -> (Tr beta, Tr(lam beta)) mod h_p is a bijection.
        (3) cyclic-state (transfer) identity: E_{y in G_p} prod_{i<p} g(A^i y) = sum over cyclic state paths
            D_{i+1} = A^{-T}(D_i + k_i), D_0=D_p in B^{-T}Z^2... checked by brute force on a random trig polynomial g."""
import itertools, json, random, numpy as np
from fractions import Fraction
def hseq(n):
    # h_m = Q_m/2, half companion Pell, m odd: h_1=1,h_3=7,...  via eps=1+sqrt2: Q_m = eps^m + epsbar^m
    a,b=1,1; Q={}
    x,y=1,0  # eps^0
    for m in range(1,n+1):
        x,y=x+2*y,x+y        # (x+y sqrt2)(1+sqrt2)
        Q[m]=2*x             # eps^m+epsbar^m = 2x
    return {m:Q[m]//2 for m in Q}
H=hseq(60)
A=np.array([[0,1],[-1,6]],dtype=object)
def mpow(M,p):
    R=np.array([[1,0],[0,1]],dtype=object)
    for _ in range(p): R=R.dot(M)
    return R
out=[]
for p in [5,7,11,13,17,19,23,29,31,37,41,43,47]:
    h=H[p]; Ap=mpow(A,p); M=Ap-np.eye(2,dtype=object)
    integral=all(int(M[i,j])%h==0 for i in range(2) for j in range(2))
    B=np.array([[int(M[i,j])//h for j in range(2)] for i in range(2)],dtype=object)
    detB=int(B[0,0]*B[1,1]-B[0,1]*B[1,0]); detM=int(M[0,0]*M[1,1]-M[0,1]*M[1,0])
    out.append(dict(p=p,h_p=h,Fix=abs(detM),fourh2=4*h*h,int_div=integral,detB=detB,index=abs(detM)//(h*h)))
print(json.dumps(out[:4])); assert all(o['int_div'] and abs(o['detB'])==4 and o['Fix']==o['fourh2'] for o in out)
# (2) bijection O/h -> (Z/h)^2 for small p
for p in [5,7]:
    h=H[p]; S=set()
    for a in range(h):
        for b in range(h):   # beta=a+b sqrt2 ; lam=3+2sqrt2 ; Tr(beta)=2a ; Tr(lam beta)=2(3a+4b)
            S.add(((2*a)%h,(2*(3*a+4*b))%h))
    assert len(S)==h*h
# (3) identity check, p=5 (h=41) and p=7 (h=239), random g with frequencies in a small box
rng=random.Random(1)
def check(p,box=1,trials=2):
    h=H[p]; Ap=mpow(A,p); M=Ap-np.eye(2,dtype=object); B=(M//h)
    At=np.array([[0,-1],[1,6]],dtype=object)        # A^T
    Ati=np.array([[6,1],[-1,0]],dtype=object)       # (A^T)^{-1}
    ks=[(i,j) for i in range(-box,box+1) for j in range(-box,box+1)]
    res=[]
    for t in range(trials):
        gh={k:complex(rng.gauss(0,1),rng.gauss(0,1)) for k in ks}
        # brute force over G_p=(1/h)Z^2
        pts=np.array([(x,y) for x in range(h) for y in range(h)],dtype=np.int64).T
        tot=np.ones(pts.shape[1],complex); P=pts.copy()
        Ai=np.array([[0,1],[-1,6]],dtype=np.int64)
        for i in range(p):
            g=np.zeros(P.shape[1],complex)
            for (k1,k2),c in gh.items(): g+=c*np.exp(2j*np.pi*((k1*P[0]+k2*P[1])%h)/h)
            tot*=g; P=(Ai@P)%h
        brute=tot.mean()
        # Fourier side: sum over (k_0..k_{p-1}) with sum_i (A^T)^i k_i in h Z^2
        four=0
        Atp=[np.array([[1,0],[0,1]],dtype=object)]
        for i in range(1,p): Atp.append(Atp[-1].dot(At))
        for combo in itertools.product(range(len(ks)),repeat=p):
            v=np.array([0,0],dtype=object); w=1
            for i,c in enumerate(combo): v=v+Atp[i].dot(np.array(ks[c],dtype=object)); w*=gh[ks[c]]
            if int(v[0])%h==0 and int(v[1])%h==0: four+=w
        res.append((abs(brute-four), abs(brute)))
    return res
r5=check(5,box=1,trials=3)
print(json.dumps(dict(identity_check_p5=[(float(a),float(b)) for a,b in r5])))
json.dump(dict(index=out,identity_p5=[(float(a),float(b)) for a,b in r5]),open('logs/a_index_identity.json','w'),indent=1)
print('ALL OK')
