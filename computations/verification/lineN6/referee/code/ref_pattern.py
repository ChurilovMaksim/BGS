"""Referee [N, exact arithmetic]: the N6 'pattern lemma' at large p.  q = h_p prime, gamma a generator of a prime above q chosen with
q + gamma in sqrt2*O (the 16D=1 family point), twists tau_i = Tr(lam^i (q+gamma))/(4q) mod 1 computed exactly (integers mod 4q),
d_i = tau_i - 1/2 in (-1/2, 1/2].  Pattern: excursion A (d = -a, +a at consecutive steps, a = (2-sqrt2)/4) with tails -+a lam^-k,
excursion B (d = -b, b = sqrt2/4) with tails -b lam^-|k| (signs may flip per point; fitted).  Prediction = sum of the tails of all
excursions in the cyclic period; reports max |d_i - pred_i| (absolute) and the window lengths.  usage: p1,p2,..."""
import sys, json, math
from sympy import isprime, sqrt_mod
import mpmath as mp
def hp(p):
    x,y=1,1
    for _ in range(p-1): x,y=x+2*y,x+y
    return x
def N(u): return u[0]*u[0]-2*u[1]*u[1]
def mul(u,v): return (u[0]*v[0]+2*u[1]*v[1],u[0]*v[1]+u[1]*v[0])
def gen(q):
    r=int(sqrt_mod(2,q)); u=(q,0); v=(r,1); f=lambda w:w[0]**2+2*w[1]**2; dot=lambda w,z:w[0]*z[0]+2*w[1]*z[1]
    if f(u)<f(v): u,v=v,u
    while True:
        k=(2*dot(u,v)+f(v))//(2*f(v)); u=(u[0]-k*v[0],u[1]-k*v[1])
        if f(u)>=f(v): break
        u,v=v,u
    for w in (v,u):
        if abs(N(w))==q: return w
    raise RuntimeError
out=[]
for p in [int(t) for t in sys.argv[1].split(',')]:
    q=hp(p); assert isprime(q), p
    mp.mp.dps=len(str(q))+40
    g=gen(q); c=None; u=g
    for j in range(4*p):
        for s in (1,-1):
            if (q+s*u[0])%2==0: c=(s*u[0],s*u[1]); break
        if c: break
        u=mul(u,(1,1))
    A,B=q+c[0],c[1]; M4=4*q; d=[]
    for i in range(p):
        t=(2*A)%M4; d.append(mp.mpf(t-2*q)/M4); A,B=(3*A+4*B)%M4,(2*A+3*B)%M4
    lam=3+2*mp.sqrt(2); a=(2-mp.sqrt(2))/4; b=mp.sqrt(2)/4
    big=[i for i in range(p) if abs(d[i])>0.1]
    pred=[mp.mpf(0)]*p
    exc=[]
    for i in big:
        if abs(abs(d[i])-b)<1e-6: exc.append(('B',i,mp.sign(d[i])))
        elif abs(abs(d[i])-a)<1e-6:
            j=(i+1)%p
            if j in big and abs(abs(d[j])-a)<1e-6 and mp.sign(d[j])==-mp.sign(d[i]): exc.append(('A',i,mp.sign(d[i])))   # pair (i, i+1)
    for kind,i0,sg in exc:
        for i in range(p):
            if kind=='B':
                k=min((i-i0)%p,(i0-i)%p); pred[i]+=sg*b*lam**(-k)
            else:
                fwd=(i-(i0+1))%p; bwd=(i0-i)%p          # i0 carries sg*a, i0+1 carries -sg*a
                if fwd<=bwd: pred[i]+=-sg*a*lam**(-fwd)
                else: pred[i]+=sg*a*lam**(-bwd)
    res=[abs(d[i]-pred[i]) for i in range(p)]
    rec=dict(p=p,q_digits=len(str(q)),excursions=[(k,i,int(s)) for k,i,s in exc],n_big=len(big),
             max_abs_residual=mp.nstr(max(res),5),log_lam_max_residual=float(mp.log(max(res))/mp.log(lam)),
             max_abs_d_outside_cores=mp.nstr(max(abs(d[i]) for i in range(p) if i not in big),5))
    out.append(rec); print(json.dumps(rec),flush=True)
json.dump(out,open('logs/ref_pattern.json','w'),indent=1)
