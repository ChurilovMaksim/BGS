# Independent referee checks for Line N.
import json, math, numpy as np
from mpmath import mp, mpf, log10, sqrt as msqrt, power
from sympy import factorint, sqrt_mod, primerange, Matrix
mp.dps=50
rows=[json.loads(l) for l in open('/workspace/bgs-lineL/logs/final_constants.jsonl')]
print("[A] constants from Line L final_constants.jsonl (Line-L budget eps=eta/(3A_k))")
C17=4*mpf(3)**(mpf(4)/3)
print("    4*3^(4/3) =",mp.nstr(C17,8))
for r in rows:
    eta=mpf(r['eta']); A=mpf(10)**mpf(r['log10_Ak']); eps=eta/(3*A)
    lw=2*log10(eps/2); C=mpf('17.31')
    l33=9*log10(eps)-log10(C); l23=6*log10(eps)-log10(2*C)/2; liso=8*log10(eps/(2/mpf(3)**0.25))
    print("   ",r['fam']+r['typ'],"k",r['k'],"log10 eps %.3f  log10 cW %.3f (L: %.3f)  log10 cN %.3f  c23 %.2f  ciso %.2f  p*(33>W) 10^%.2f"%(
        log10(eps),lw,r['log10_ck'],l33,l23,liso,3*(lw-l33)))
# J3 constant validity in the region where W+ beats Weil: q in (cW p^2, cN p^(7/3)], tau in {p,3p}
eps=mpf(rows[0]['eta'])/(3*mpf(10)**mpf(rows[0]['log10_Ak'])); cW=(eps/2)**2; cN=eps**9/mpf('17.31')
def J3b(q,tau): return tau**3*(C17*(q*tau/(q-1))**(mpf(2)/3)+3*q*tau**2/(q-1)**2)+12*tau**3
print("[B] J3 bound / tau^(11/3) in the W+ region (needs <= 17.31):")
for lp in (264.6, 300, 344, 400):
    p=mpf(10)**lp
    for tau in (p,3*p):
        for q in (cW*p**2, cN*p**(mpf(7)/3)):
            if q<cW*p**2: continue
            print("    log10p=%5.1f tau=%s q/tau^2=10^%.1f  ratio=%s"%(lp,'p ' if tau==p else '3p',float(log10(q/tau**2)),mp.nstr(J3b(q,tau)/tau**(mpf(11)/3),12)))
    print("    q>=tau^2 at top of range (q=cN p^7/3, tau=3p)?", cN*p**(mpf(7)/3)>=9*p**2)
# theta
mu=mpf('1.9154712')
for r in rows[:2]:
    th=((1-mpf(r['delta'])/2)*mpf('1.28359')/mu)**(2*r['k'])
    print("[C] theta",r['fam']+r['typ'],mp.nstr(th,5),"(N: 5.39e-6 / 6.01e-6)")
# index of conductor-h_p points in Fix(T^p): torus (O tensor R)/O^dual, O^dual=(1/(2sqrt2))O, basis e1=1/(2sqrt2), e2=1/2
def lam_matrix():
    # lambda*(u e1 + v e2): lambda=3+2sqrt2; lambda*e1 = 3/(2sqrt2)+1 = 3 e1 + 2 e2 ; lambda*e2 = 3/2+sqrt2 = 3 e2 + 4 e1  (sqrt2 = 4 e1)
    return Matrix([[3,4],[2,3]])
M=lam_matrix()
def hp(p):
    x,y=1,1
    for _ in range(p-1): x,y=x+2*y,x+y
    return x
print("[D] Fix(T^p) vs conductor-h_p points")
for p in (3,5,7):
    h=hp(p); Mp=M**p; det=abs((Mp-Matrix.eye(2)).det())
    # conductor points beta/h, beta=a+b sqrt2 -> coords (u,v)=(4b/h, 2a/h) mod 1
    allfixed=True; pts=set()
    for a in range(h):
        for b in range(h):
            u=(4*b)%h; v=(2*a)%h; pts.add((u,v))
            w=Mp*Matrix([u,v])-Matrix([u,v])   # in units of 1/h
            if w[0]%h or w[1]%h: allfixed=False
    print("    p=%d h_p=%d  #Fix=|det(S^p-I)|=%d  (4h^2=%d)  #cond pts=%d  all fixed=%s  index=%s"%(p,h,det,4*h*h,len(pts),allfixed,det/len(pts)))
# energies and sup|S| on real levels, direct (no FFT), independent code
print("[E] exact J2, J3, max|S| (direct), real levels q | h_{3p}, q<=4700")
def H(m):
    x,y=1,1
    for _ in range(m-1): x,y=x+2*y,x+y
    return x
from collections import Counter
cnt=0
for p in primerange(5,70):
    for q in [q for q in primerange(3,4701) if H(3*p)%q==0]:
        if q==7 or q>4700: continue
        r2=sqrt_mod(2,q); l=(3+2*r2)%q
        tau=1; v=l
        while v!=1: v=v*l%q; tau+=1
        U=[pow(l,i,q) for i in range(tau)]; V=[pow(u,q-2,q) for u in U]
        pts=list(zip(U,V))
        n2=Counter(((a[0]+b[0])%q,(a[1]+b[1])%q) for a in pts for b in pts)
        J2=sum(c*c for c in n2.values())
        n3=Counter()
        for w,c in n2.items():
            for (x,y) in pts: n3[((w[0]+x)%q,(w[1]+y)%q)]+=c
        J3=sum(c*c for c in n3.values())
        a=np.arange(1,q)
        E1=np.exp(2j*np.pi*np.outer(a,U)/q); E2=np.exp(2j*np.pi*np.outer(a,V)/q)
        Smax=np.abs(E1@E2.T).max()/tau
        Fb=float(J3b(mpf(q),mpf(tau)))
        b33=(q**2*tau**6*Fb**2)**(1/18)/tau; b23=(q**2*tau**2*(2*tau**2-tau)*Fb)**(1/12)/tau; b22=(q**2*(2*tau**2-tau)**2)**(1/8)/tau
        iso=max(abs(np.exp(2j*np.pi*np.outer(np.arange(1,q),U)/q).sum(1)))/tau
        cp=1.5196713713*q**(1/8)*tau**(-3/8)
        ok=J2==2*tau*tau-tau and J3<=Fb and Smax<=min(b22,b23,b33)+1e-9 and iso<=min(cp,math.sqrt(q)/tau)+1e-9
        cnt+=1
        print("    p=%d q=%d tau=%d J2=%d(=2t^2-t:%s) J3=%d J3/bound=%.4f max|S|/tau=%.4f b22=%.3f b23=%.3f b33=%.3f iso=%.4f CP=%.3f ok=%s"%(
            p,q,tau,J2,J2==2*tau*tau-tau,J3,J3/Fb,Smax,b22,b23,b33,iso,cp,ok))
print("    levels:",cnt)
