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
for p in (32,64,128):
    pts=kernel_points(p)
    mp_pts=[(y0,y1) for (y0,y1) in pts if minperiod(seq(y0,y1,p))==p]
    # structure: y0 multiples of?
    g0=0
    for (y0,y1) in mp_pts: g0=gcd(g0,y0)
    # for y0 = smallest positive, y1 values
    y0s=sorted(set(y0 for (y0,y1) in mp_pts))
    print("p=%d minperiod pts=%d gcd(y0)=%d y0 count=%d first y0s=%s"%(p,len(mp_pts),g0,len(y0s),y0s[:5]))
    # parametrisation: guess y0 = g0 * t; for each t, y1 = b*t + c*s ? check y1 mod g0 etc.
    # take t=1 point(s): y0=g0
    t1=[y1 for (y0,y1) in mp_pts if y0==g0]
    print("   y1 values at y0=g0:", sorted(set(t1))[:8], "count", len(set(t1)))
    # check linear fit: find b,c s.t. y1 = b*(y0/g0) + c*s mod Q for s in range(Q/c)?
    # instead: for fixed y0, step in y1
    from collections import defaultdict
    by0=defaultdict(set)
    for (y0,y1) in mp_pts: by0[y0].add(y1)
    steps=Counter()
    for y0,ys in by0.items():
        srt=sorted(ys)
        if len(srt)>1:
            diffs=set((srt[i+1]-srt[i])%Q for i in range(len(srt)-1))
            steps[tuple(sorted(diffs))]+=1
    print("   y1-step patterns per y0:", steps.most_common(3))
    # nu=(1,0) subset: parametrisation conditions
    nu10=[]
    for (y0,y1) in mp_pts:
        y=seq(y0,y1,p); h=p//2
        if ((y[h]-y[0])//(Q//2),(y[h+1]-y[1])//(Q//2))==(1,0): nu10.append((y0,y1))
    print("   nu10 count=%d; y0/g0 mod small: t-mod2=%s"%(len(nu10), Counter((y0//g0)%2 for (y0,y1) in nu10)))
    # for nu10: y1 as function of t=y0/g0: y1 - b*t should be multiple of step; find b via t=1 nu10 point
    t1nu=[y1 for (y0,y1) in nu10 if y0==g0]
    print("   nu10 y1 at y0=g0:", sorted(set(t1nu))[:8])
