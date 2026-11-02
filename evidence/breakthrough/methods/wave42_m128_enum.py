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
            if (c*y1+d*y0)%Q==0:
                pts.append((y0,y1))
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
for p in (8,16,32,64,128):
    pts=kernel_points(p)
    # group by minimal period and nu
    from collections import defaultdict
    groups=defaultdict(int); sym=0; tot10=0; bad=[]
    for (y0,y1) in pts:
        y=seq(y0,y1,p)
        mp=minperiod(y)
        if mp!=p: continue
        h=p//2
        diffs=[(y[(i+h)%p]-y[i])%Q for i in range(p)]
        # check nu structure: diffs in {0,Q/2}, even/odd constant
        if any(d not in (0,Q//2) for d in diffs): groups[('non-nu',)]+=1; continue
        nu=(diffs[0]//(Q//2), diffs[1]//(Q//2))
        groups[nu]+=1
        if nu==(1,0):
            tot10+=1
            O=[y[i] for i in range(p) if i%2==1]
            cnt=Counter(v%(Q//2) for v in O); cntU=Counter(v-(Q//2) for v in O if v>=Q//2)
            # symmetric iff for every class, lower count == upper count
            low=Counter(v for v in O if v<Q//2); up=Counter(v-Q//2 for v in O if v>=Q//2)
            if low==up: sym+=1; bad.append((y0,y1))
    print("p=%d kernel=%d nu-groups=%s nu10=%d symmetric-O=%d"%(p,len(pts),dict(groups),tot10,sym))
    if bad: print("  SYMMETRIC EXAMPLES:",bad[:3])
