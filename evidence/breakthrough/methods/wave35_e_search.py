import sys
def sieve(n):
    bs=bytearray(b'\x01')*(n+1); bs[0:2]=b'\x00\x00'
    for i in range(2,int(n**0.5)+1):
        if bs[i]:
            step=i; start=i*i; bs[start:n+1:step]=b'\x00'*(((n-start)//step)+1)
    return [i for i, v in enumerate(bs) if v]
PRIMES=sieve(100000)
def factorize(n):
    f={}
    for pr in PRIMES:
        if pr*pr>n: break
        if n%pr==0:
            c=0
            while n%pr==0: n//=pr; c+=1
            f[pr]=c
        if n==1: break
    if n>1: f[n]=1
    return f
def tonelli(n,p):
    # sqrt of n mod p, p odd prime, n QR; returns r with r^2=n
    if n%p==0: return 0
    if pow(n,(p-1)//2,p)!=1: return None
    if p%4==3: return pow(n,(p+1)//4,p)
    # factor p-1 = q*2^s
    q=p-1; s=0
    while q%2==0: q//=2; s+=1
    z=2
    while pow(z,(p-1)//2,p)!=p-1: z+=1
    c=pow(z,q,p); x=pow(n,(q+1)//2,p); t=pow(n,q,p); m=s
    while t!=1:
        i=1; t2=pow(t,2,p)
        while i<m:
            if t2==1: break
            t2=pow(t2,2,p); i+=1
        b=pow(c,1<<(m-i-1),p)
        x=x*b%p; c=b*b%p; t=t*c%p; m=i
    return x
def mul(x,y,mod):
    return ((x[0]*y[0]+2*x[1]*y[1])%mod,(x[0]*y[1]+x[1]*y[0])%mod)
def pw(x,n,mod):
    r=(1%mod,0)
    while n:
        if n&1: r=mul(r,x,mod)
        x=mul(x,x,mod); n>>=1
    return r
def order_in_group(elem, N, mod, mulfn, one):
    # order of elem dividing N
    fac=factorize(N); o=N
    for pr in fac:
        while o%pr==0 and pw(elem,o//pr,mod)==one:
            o//=pr
    return o

e2=[]; e3=[]
for p in PRIMES:
    if p<5: continue
    # beta = 17+12 sqrt2
    if p%8 in (1,7):  # split
        r=tonelli(2,p)
        b1=(17+12*r)%p
        # order_in_group uses pw for ints? handle separately: use pow
        # recompute with pow for ints
        fac=factorize(p-1); o=p-1
        for pr in fac:
            while o%pr==0 and pow(b1,o//pr,p)==1: o//=pr
        d=o
    else:  # inert: order in F_p2 norm-1 subgroup divides p+1
        d=order_in_group((17%p,12%p),p+1,p,None,(1,0))
    # valuation: beta^d mod p^4
    mod=p**4
    v=pw((17%mod,12%mod),d,mod)
    e=0
    for ee in range(1,5):
        if (v[0]-1)%(p**ee)==0 and v[1]%(p**ee)==0: e=ee
        else: break
    if e>=2:
        twin = (d%3!=0)
        (e3 if e>=3 else e2).append((p,d,e,twin))
print("e==2:", e2)
print("e>=3:", e3)
