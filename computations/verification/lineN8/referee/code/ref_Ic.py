"""Referee [exact]: spot-check N8b identity (I_c): Tr(lam^i beta) == sigma Tr(eps^{2i-M} beta) (mod c) for beta on the consistent
lines L(gamma) (sigma=-(-1)^k) and L(gammabar) (sigma=(-1)^k), c | h_p, M = p.  Tr(a+b sqrt2)=2a."""
def xy(n):
    x,y=1,0
    for _ in range(n): x,y=x+2*y,x+y
    return x,y
def mul(a,b): return (a[0]*b[0]+2*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def epow(n):
    r=(1,0); u=(1,1) if n>=0 else (-1,1)
    for _ in range(abs(n)): r=mul(r,u)
    return r
bad=0; tot=0; badl=[]
for p,c in [(11,353),(11,23),(13,79),(13,599),(17,103),(17,15607),(23,47)]:
    M=p; k=(M-1)//2; g=(xy(k+1)[0],xy(k)[1])
    for s in range(1,30):
        for t in [(0,0),(1,2),(3,-1)]:
            for line,gg,sig in [('g',g,-(-1)**k),('gbar',(g[0],-g[1]),(-1)**k)]:
                beta=(s*gg[0]+c*t[0], s*gg[1]+c*t[1])
                for i in range(0,3*M):
                    lhs=(2*mul(epow(2*i),beta)[0])%c; rhs=(sig*2*mul(epow(2*i-M),beta)[0])%c
                    tot+=1
                    if lhs!=rhs: bad+=1; badl.append((p,c,line))
print('checks',tot,'bad',bad,sorted(set(badl))[:5])
