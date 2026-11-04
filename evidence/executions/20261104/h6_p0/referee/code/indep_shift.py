# independent recomputation (mpmath, 60 digits; not ball arithmetic -> [N-hi-prec])
from mpmath import mp, mpf, sqrt, log, exp, pi, besselj, loggamma, ceil, floor
mp.dps=60
lam=3+2*sqrt(2); eps=1+sqrt(2); C0=1/(lam-1/lam); x=mpf('1.8')
J=[abs(besselj(n,x)) for n in range(120)]
def A(s,pw=0): return (J[0] if pw==0 else 0)+2*sum(J[n]*exp(s*n)*n**pw for n in range(1,120))
def one(a,b,off):
    (ra,ba),(rb,bb)=a,b; th=(rb/lam+off)/ra
    if th>=1 or ba/lam>bb: return None
    return sqrt(6)/sqrt(1-th**2)*exp(ba/2)*A(2*pi*C0*rb+ba/lam)
def two(a,b,off):
    best=None
    for i in range(1,80):
      for j in range(1,60):
        m=(mpf(i)/20,mpf(j)/20); s=one(a,m,off)
        if s is None: continue
        t=one(m,b,off)
        if t is None: continue
        if best is None or s*t<best[0]: best=(s*t,m)
    return best
out={}
for fam,o1,F,off,dev,Lam,kF,r2s in [('8V',(mpf('0.75'),mpf('0.25')),(mpf('1.2'),mpf('2.5')),mpf('0.5'),lam/(2*(lam-1)),mpf('1.9656353'),mpf(4036),{4000:mpf('1.0529011503787689')}),
                                    ('8E',(mpf('0.2'),mpf('0.3')),(mpf('0.8'),mpf('2.5')),1/(2*lam),1/(2*(lam-1)),mpf('0.4915932'),mpf('4.3e4'),{1000:mpf('1.0543495777416303')})]:
    a=two(o1,F,off); b=two(F,o1,off); CI=a[0]*b[0]; S=one(o1,o1,off)
    print(fam,'CI',CI,a[1],b[1],'S',S)
    for k,r2 in r2s.items():
        rho,beta=o1; th=(rho*lam**(-k)+dev)/rho; bb=beta*(1-lam**(-k))
        Cp=1/mp.tanh(bb)*exp(2*beta*(dev+1))/(1-th**2)
        lPA=0; W=0
        for j in range(k):
            tau=2*pi*C0*rho*lam**(-j)+beta*lam**(-(k-j)); a0=A(tau); a1=A(tau,1)
            lPA+=2*log(a0); W+=2*a1/a0*(lam**(j-k)+lam**(-j))
        logLp=log(Cp)+lPA+log(W)
        lk=log(mpf('1.28359')**3/(r2*Lam)); CIk=CI*kF; Sm=max(S,1)
        lH=max(min([l*log(Sm)]+([log(CIk)+(l-4)*log(Lam)] if l>=5 else [])) for l in range(k))
        lc1=log(2*pi)+logLp-log(k)
        K1=log(CIk)-4*log(Lam)+4*lH+(k-1)*log(lam)-log(2*sqrt(2))+2*(lc1-log(2))+2
        print(fam,k,'Cpair',Cp,'logLp',logLp,'logHmax',lH,'K1',K1,'logkappa',lk)
        def wmax(p):
            B=p*log(eps); lp=log(p-1); lo,hi=0,1
            while hi*lp+loggamma(hi+1)<=B: hi*=2
            while hi-lo>1:
                m=(lo+hi)//2
                if m*lp+loggamma(m+1)<=B: lo=m
                else: hi=m
            return lo
        ok=lambda p: wmax(p)*log(2)+K1+2*log(p)-2*log(1-lam**(-p)) < p*lk
        out[fam]=(K1,lk,wmax,ok)
        for p in ([28420499,28420500] if fam=='8V' else [3927,3928]): print(' p',p,'wmax',wmax(p),'ok',ok(p))
# independent cover: on [P1,P2], test with wmax computed at (P1-1, eps^P2); geometric grid
SH={'8V':(10+log(mpf(4)/3),28424695),'8E':(mpf('8.75')+log(mpf(4)/3),3934)}
for fam,(K1,lk,wmax,ok) in out.items():
    K1=K1+SH[fam][0]; P=SH[fam][1]; n=0; X=10**10
    def wb(P1,P2):
        B=P2*log(eps); lp=log(P1-1); lo,hi=0,1
        while hi*lp+loggamma(hi+1)<=B: hi*=2
        while hi-lo>1:
            m=(lo+hi)//2
            if m*lp+loggamma(m+1)<=B: lo=m
            else: hi=m
        return lo
    a=P; step=1
    while a<X:
        b=min(X,a+step)
        if wb(a,b)*log(2)+K1+2*log(b)-2*log(1-lam**(-a)) < a*lk: a=b+1; step=max(1,step*2); n+=1
        else:
            if step==0: print(fam,'COVER FAIL at',a); break
            step//=2
    print(fam,'cover intervals',n,'reached',a)
    cp=(lk-(K1+2*log(X))/X)/log(2)
    print(fam,'tail c\'',cp, 'lhs',log(X-1)+log(cp*X)-1,'rhs',log(eps)/cp)
