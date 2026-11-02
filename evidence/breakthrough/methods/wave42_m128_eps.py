from math import gcd
from collections import Counter
Q = 131072
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
# p=128 linear forms for y33, y35
A0=128; A1=384; B1=1024
y_t=seq(A0,A1,128); y_s=seq(0,B1,128)
for n in (33,35):
    print("p=128 y_%d = %d*t + %d*s"%(n,y_t[n],y_s[n]))
# eps0 = (y33-y1)/(Q/2), eps1 = (y35-y3)/(Q/2): compute formulas
# y33-y1 = (y_t[33]-384)t + (y_s[33]-1024)s ; y35-y3 = (y_t[35]-12672)t + (y_s[35]-35840)s
print("d1 = %d*t + %d*s"%((y_t[33]-384)%Q,(y_s[33]-1024)%Q))
print("d3 = %d*t + %d*s"%((y_t[35]-12672)%Q,(y_s[35]-35840)%Q))
# p=8 swapped defect: for nu10 points, w1-w0 mod Q
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
wd=Counter()
for (y0,y1) in kernel_points(8):
    y=seq(y0,y1,8)
    if minperiod(y)!=8: continue
    h=4
    if ((y[h]-y[0])%Q//(Q//2),(y[h+1]-y[1])%Q//(Q//2))!=(1,0): continue
    wd[(y[3]-y[1])%Q]+=1
print("p=8 w1-w0 values (nu10):", dict(wd))
# p=128: g_odd mod (Q/8), w minimal period check, eps0/eps1 formulas check
gmod=Counter(); wper=Counter(); epscheck=Counter()
for t in range(1024):
    for s in range(128):
        y=seq((128*t)%Q,(384*t+1024*s)%Q,128)
        if minperiod(y)!=128: continue
        h=64
        if ((y[h]-y[0])%Q//(Q//2),(y[h+1]-y[1])%Q//(Q//2))!=(1,0): continue
        # g_i = y[i+8]-y[i], odd i
        for i in range(1,128,2):
            gmod[((y[(i+8)%128]-y[i])%Q)%(Q//8)]+=1
        w=[y[2*k+1] for k in range(32)]
        # minimal period of w
        L=32
        for dd in (1,2,4,8,16,32):
            if all(w[k]==w[k%dd] for k in range(32)): L=dd; break
        wper[L]+=1
        # eps0, eps1
        e0=((y[33]-y[1])%Q)//(Q//2); e1=((y[35]-y[3])%Q)//(Q//2)
        a=(t-1)//2; b=(s-1)//2
        epscheck[(e0,(a+b)%2,e1,(a+b+1)%2)]+=1
print("p=128 g_odd mod (Q/8):", dict(gmod))
print("p=128 w minimal periods:", dict(wper))
print("p=128 (eps0, (a+b)%2, eps1, (a+b+1)%2) counts:", len(epscheck), "all match:", all(k[0]==k[1] and k[2]==k[3] for k in epscheck))
