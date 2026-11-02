from math import gcd
from collections import Counter
Q = 131072
def matmul(A,B):
    return [[(A[0][0]*B[0][0]+A[0][1]*B[1][0])%Q,(A[0][0]*B[0][1]+A[0][1]*B[1][1])%Q],
            [(A[1][0]*B[0][0]+A[1][1]*B[1][0])%Q,(A[1][0]*B[0][1]+A[1][1]*B[1][1])%Q]]
def matpow(M,n):
    R=[[1,0],[0,1]]
    while n:
        if n&1: R=matmul(M,R)
        M=matmul(M,M); n>>=1
    return R
M=[[6,Q-1],[1,0]]
def kernel_points(p):
    Mp=matpow(M,p)
    a=(Mp[0][0]-1)%Q; b=Mp[0][1]%Q; c=Mp[1][0]%Q; d=(Mp[1][1]-1)%Q
    pts=[]
    for y0 in range(Q):
        rhs=(-b*y0)%Q; g=gcd(a,Q)
        if rhs%g: continue
        a1=a//g; Q1=Q//g; r1=rhs//g
        y1_0=(pow(a1,-1,Q1)*r1)%Q1
        for k in range(g):
            y1=y1_0+k*Q1
            if (c*y1+d*y0)%Q==0: pts.append((y0,y1))
    return pts
def seq(y0,y1,p):
    y=[0]*p; y[0]=y0
    if p>1: y[1]=y1
    for i in range(1,p-1): y[i+1]=(6*y[i]-y[i-1])%Q
    return y
def minperiod(y):
    p=len(y)
    for d in (1,2,4,8,16,32,64,128):
        if p%d==0 and all(y[i]==y[i%d] for i in range(p)): return d
    return p
def nu10pts(p):
    out=[]
    for (y0,y1) in kernel_points(p):
        y=seq(y0,y1,p)
        if minperiod(y)!=p: continue
        h=p//2
        if ((y[h]-y[0])%Q//(Q//2),(y[h+1]-y[1])%Q//(Q//2))==(1,0): out.append(y)
    return out
def wper_ok(y,p):
    w=[y[2*k+1] for k in range(p//4)]
    L=p//4
    for dd in (1,2,4,8,16,32):
        if L%dd==0 and all(w[k]==w[k%dd] for k in range(len(w))): return dd==L
    return True
# p=16 alternation + p=32 (A)(B) + w-periods
for p in (16,32,64,128):
    pts=nu10pts(p); wbad=0; altbad=0
    for y in pts:
        if not wper_ok(y,p): wbad+=1
        w=[y[2*k+1] for k in range(p//4)]; q8=p//8
        eps=[((w[k+q8]-w[k])%Q)//(Q//2) for k in range(q8)]
        for k in range(q8):
            if (eps[k]+eps[k-1])%2==0: altbad+=1
    print("p=%d nu10=%d wperiod_bad=%d alt_bad=%d"%(p,len(pts),wbad,altbad))
# p=32 (A)(B) directly
pts=nu10pts(32); Abad=0; Bbad=0
for y in pts:
    w=[y[2*k+1] for k in range(8)]; v=[x%(Q//2) for x in w]
    d0=((v[2]-v[0])%(Q//2))//(Q//4); d1=((v[3]-v[1])%(Q//2))//(Q//4)
    e0=((w[4]-w[0])%Q)//(Q//2)
    if d0+d1!=1: Abad+=1
    if e0!=d1: Bbad+=1
print("p=32 (A) delta-sum!=1:",Abad," (B) eps0!=delta1:",Bbad)
# p=64: unique phi=0 + failing class 2B-A=+-2
pts=nu10pts(64); uniqbad=0; failbad=0
for y in pts:
    w=[y[2*k+1] for k in range(16)]; v=[x%(Q//2) for x in w]; t=[x//(Q//2) for x in w]
    f=[(y[(i+8)%64]-y[i])%Q for i in range(64)]
    phi=[(f[2*k+1]//(Q//4))%4 for k in range(8)]
    eps=[((w[k+8]-w[k])%Q)//(Q//2) for k in range(8)]
    z0=[j for j in range(4) if eps[j]==0]
    f0=[j for j in z0 if phi[j]==0]
    if len(f0)!=1: uniqbad+=1; continue
    j=f0[0]; c=v[j]
    # 2B-A at class c over k<8
    A=sum(1 for k in range(8) if v[k]==c and eps[k]==0)
    B=sum(1-t[k] for k in range(8) if v[k]==c and eps[k]==0)
    if 2*B-A not in (2,-2): failbad+=1
print("p=64 unique-phi0 violations:",uniqbad," failing-class violations:",failbad)
# p=128: D0=D1=2, H=phi+2, two failing classes
pts=nu10pts(128); Dbad=0; Hbad=0; pairbad=0
for y in pts:
    w=[y[2*k+1] for k in range(32)]; v=[x%(Q//2) for x in w]; t=[x//(Q//2) for x in w]
    f=[(y[(i+16)%128]-y[i])%Q for i in range(128)]
    phi=[(f[2*k+1]//(Q//4))%4 for k in range(16)]
    eps=[((w[k+16]-w[k])%Q)//(Q//2) for k in range(16)]
    h=[(w[(k+4)%32]-w[k])%Q for k in range(32)]
    H=[(hh%(Q//2))//(Q//8) for hh in h]
    D0=(H[0]-phi[0])%4; D1=(H[1]-phi[1])%4
    if D0!=2 or D1!=2: Dbad+=1
    if any((H[k]-phi[k])%4!=2 for k in range(16)): Hbad+=1
    z0=[j for j in range(8) if eps[j]==0]
    f0=[j for j in z0 if phi[j]==0]
    if len(f0)!=2 or f0[1]-f0[0]!=4: pairbad+=1; continue
    if v[f0[0]]==v[f0[1]]: pairbad+=1; continue
    for j in f0:
        c=v[j]
        A=sum(1 for k in range(16) if v[k]==c and eps[k]==0)
        B=sum(1-t[k] for k in range(16) if v[k]==c and eps[k]==0)
        if 2*B-A not in (2,-2): pairbad+=1
print("p=128 D!=2:",Dbad," H!=phi+2:",Hbad," pair/fail violations:",pairbad)
# direct Gap G all periods (recap)
for p in (8,16,32,64,128):
    sym=0
    for y in nu10pts(p):
        O=[y[i] for i in range(p) if i%2==1]
        low=Counter(v for v in O if v<Q//2); up=Counter(v-Q//2 for v in O if v>=Q//2)
        if low==up: sym+=1
    print("p=%d direct Gap G symmetric-O: %d"%(p,sym))
print("ALL CHECKS DONE")
