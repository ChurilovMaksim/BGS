from math import gcd
from collections import Counter, defaultdict
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
for p in (32,64,128):
    pts=kernel_points(p)
    n10=0; phi0_pat=Counter(); eps0_pat=Counter(); alt_bad=0; par_bad=0; rec_bad=0; iii_bad=0
    p128_detail=defaultdict(Counter)
    for (y0,y1) in pts:
        y=seq(y0,y1,p)
        if minperiod(y)!=p: continue
        h=p//2
        diffs=[(y[(i+h)%p]-y[i])%Q for i in range(p)]
        if any(d not in (0,Q//2) for d in diffs): continue
        nu=(diffs[0]//(Q//2), diffs[1]//(Q//2))
        if nu!=(1,0): continue
        n10+=1
        w=[y[2*k+1] for k in range(p//4)]
        # quarter defect: w[k+p/8] = w[k] + (Q/2) eps[k], k < p/8
        q8=p//8
        eps=[]
        for k in range(q8):
            d=(w[k+q8]-w[k])%Q
            assert d in (0,Q//2), (p,y0,y1,k,d)
            eps.append(d//(Q//2))
        # alternation: eps[k]+eps[k-1] odd cyclic
        for k in range(q8):
            if (eps[k]+eps[k-1])%2==0: alt_bad+=1
        # f_i = y[i+p/8]-y[i]; phi[k] = f[2k+1]/(Q/4) mod 4, k < p/8
        f=[(y[(i+q8)%p]-y[i])%Q for i in range(p)]
        phi=[]
        for k in range(q8):
            assert f[2*k+1]%(Q//4)==0, (p,y0,y1,k,f[2*k+1])
            phi.append((f[2*k+1]//(Q//4))%4)
        for k in range(q8):
            if phi[k]%2!=eps[k]%2: par_bad+=1
        for k in range(q8):
            if (phi[(k+1)%q8]-(2*phi[k]-phi[k-1]))%4!=0: rec_bad+=1
        p16=p//16
        for k in range(q8):
            if (phi[k]+phi[(k+p16)%q8]-2*eps[k])%4!=0: iii_bad+=1
        # epsilon=0 indices among j < p/16, their phi values
        v=[wk%(Q//2) for wk in w]; t=[wk//(Q//2) for wk in w]
        z0=[j for j in range(p16) if eps[j]==0]
        phi0_pat[tuple(phi[j] for j in z0)]+=1
        if p==128:
            f0=[j for j in z0 if phi[j]==0]
            # classes and t of phi=0 indices
            key=tuple(sorted((v[j],t[j]) for j in f0))
            p128_detail['phi0idx'][tuple(f0)]+=1
            p128_detail['phi0classes_same'][len(set(v[j] for j in f0))]+=1
            p128_detail['phi0t_same'][len(set(t[j] for j in f0))]+=1
    print("p=%d nu10=%d alt_bad=%d par_bad=%d rec_bad=%d iii_bad=%d"%(p,n10,alt_bad,par_bad,rec_bad,iii_bad))
    print("   phi at eps=0 indices (j<p/16):", dict(phi0_pat))
    if p==128:
        for k,vv in p128_detail.items(): print("   ",k,dict(vv))
