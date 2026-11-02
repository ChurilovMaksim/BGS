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
# verify parametrisation y0=2^a t, y1=3*2^a t + 2^(a+3) s
for p,a in ((32,9),(64,8),(128,7)):
    Mp=matpow(M,p)
    ok=0; tot=0; nu_cond=Counter()
    A0=2**a; A1=3*2**a; B1=2**(a+3)
    gen=set()
    for t in range(Q//A0):
        for s in range(Q//B1):
            gen.add(((A0*t)%Q,(A1*t+B1*s)%Q))
    pts=set(kernel_points(p))
    print("p=%d param covers kernel: gen==pts? %s (|gen|=%d |pts|=%d)"%(p,gen==pts,len(gen),len(pts)))
    # nu conditions in (t,s)
    for (y0,y1) in gen:
        y=seq(y0,y1,p)
        if minperiod(y)!=p: continue
        h=p//2
        d0=(y[h]-y[0])%Q; d1=(y[h+1]-y[1])%Q
        if d0 not in (0,Q//2) or d1 not in (0,Q//2): nu_cond['bad']+=1; continue
        nu=(d0//(Q//2),d1//(Q//2))
        t=y0//A0
        # recover s: y1 = A1 t + B1 s mod Q
        s=((y1-A1*t)%Q)//B1
        nu_cond[(nu,t%2,s%2)]+=1
    print("   nu x (t parity, s parity):", dict(nu_cond))
# p=32: Lemma2 instances for e_i = y[i+4]-y[i]; w1 mod 1024 for nu10
p=32; a=9; A0=512; A1=1536; B1=4096
e_odd=Counter(); e_even=Counter(); w1mod=Counter()
for t in range(256):
    for s in range(32):
        y=seq((A0*t)%Q,(A1*t+B1*s)%Q,p)
        if minperiod(y)!=p: continue
        h=16
        d0=(y[h]-y[0])%Q; d1=(y[h+1]-y[1])%Q
        if (d0//(Q//2),d1//(Q//2))!=(1,0): continue
        for i in range(p):
            e=(y[(i+4)%p]-y[i])%Q
            if i%2==1: e_odd[e%(Q//4)]+=1
            else: e_even[e%(Q//4)]+=1
        w1mod[y[3]%1024]+=1
print("p=32 e_odd mod (Q/4):", dict(e_odd), " e_even mod (Q/4):", dict(e_even), " w1 mod 1024:", dict(w1mod))
# p=64: f1,d1,f3,d3 in terms of (t,s): compute linear forms mod Q via two points
p=64; a=8; A0=256; A1=768; B1=2048
def linforms(p,A0,A1,B1,idxs):
    # y_n = An*t + Bn*s mod Q; get An,Bn by evaluating at (t=1,s=0),(t=0,s=1) with big enough range
    res={}
    for n in idxs:
        y_t=seq(A0,A1,p); y_s=seq(0,B1,p)
        res[n]=(y_t[n],y_s[n])
    return res
lf=linforms(64,A0,A1,B1,[1,3,9,11,17,19])
for n,(An,Bn) in lf.items(): print("p=64 y_%d = %d*t + %d*s (mod Q)"%(n,An,Bn))
# check phi0,eps0,phi1,eps1 formulas: f1=y9-y1, d1=y17-y1, f3=y11-y3, d3=y19-y3
def show(p,A0,A1,B1,lf,f_idx,d_idx):
    fA=(lf[f_idx][0]-lf[1][0])%Q; fB=(lf[f_idx][1]-lf[1][1])%Q
    dA=(lf[d_idx][0]-lf[1][0])%Q; dB=(lf[d_idx][1]-lf[1][1])%Q
    print("   f = %d*t + %d*s ; d = %d*t + %d*s"%(fA,fB,dA,dB))
    print("   f mod (Q/2) coeffs: t:%d s:%d ; d mod Q coeffs t:%d s:%d"%(fA%(Q//2),fB%(Q//2),dA,dB))
show(64,A0,A1,B1,lf,9,17)
lf3=linforms(64,A0,A1,B1,[3,11,19])
fA=(lf3[11][0]-lf3[3][0])%Q; fB=(lf3[11][1]-lf3[3][1])%Q
dA=(lf3[19][0]-lf3[3][0])%Q; dB=(lf3[19][1]-lf3[3][1])%Q
print("   f3 = %d*t + %d*s ; d3 = %d*t + %d*s"%(fA,fB,dA,dB))
print("   f3 mod (Q/2): t:%d s:%d"%(fA%(Q//2),fB%(Q//2)))
# p=128: D0,D1: h0=y9-y1, f1=y17-y1, h1=y11-y3, f3=y19-y3
p=128; a=7; A0=128; A1=384; B1=1024
lf=linforms(128,A0,A1,B1,[1,3,9,11,17,19])
for n,(An,Bn) in lf.items(): print("p=128 y_%d = %d*t + %d*s (mod Q)"%(n,An,Bn))
h0A=(lf[9][0]-lf[1][0])%Q; h0B=(lf[9][1]-lf[1][1])%Q
f1A=(lf[17][0]-lf[1][0])%Q; f1B=(lf[17][1]-lf[1][1])%Q
h1A=(lf[11][0]-lf[3][0])%Q; h1B=(lf[11][1]-lf[3][1])%Q
f3A=(lf[19][0]-lf[3][0])%Q; f3B=(lf[19][1]-lf[3][1])%Q
print("p=128 h0 = %d*t + %d*s ; f1 = %d*t + %d*s"%(h0A,h0B,f1A,f1B))
print("p=128 h1 = %d*t + %d*s ; f3 = %d*t + %d*s"%(h1A,h1B,f3A,f3B))
