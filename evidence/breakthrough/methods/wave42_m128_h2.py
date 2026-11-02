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
tab=Counter()
pts=kernel_points(128)
for (y0,y1) in pts:
    y=seq(y0,y1,128)
    if minperiod(y)!=128: continue
    h=64
    if any(((y[(i+h)%128]-y[i])%Q) not in (0,Q//2) for i in range(128)): continue
    if ((y[h]-y[0])//(Q//2),(y[h+1]-y[1])//(Q//2))!=(1,0): continue
    w=[y[2*k+1] for k in range(32)]
    f=[(y[(i+16)%128]-y[i])%Q for i in range(128)]
    phi=[(f[2*k+1]//(Q//4))%4 for k in range(16)]
    for j in range(8):
        hj=(w[(j+4)%32]-w[j])%Q
        tab[(phi[j], hj%(Q//2))]+=1
for k in sorted(tab): print("phi_j=%d h_j mod (Q/2)=%d count=%d"%(k[0],k[1],tab[k]))
