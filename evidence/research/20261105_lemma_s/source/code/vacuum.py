"""research1105b [N]: 'vacuum' (small-cofactor) points on every ideal line of norm h_p, for p up to ~70.
Line a = gamma0*O (class number 1). Points beta = gamma0*c*(2 sqrt2)^{-1} and gamma0*c*(4 sqrt2)^{-1} mod h (the two resonant
backgrounds, cf. lownorm.py), c in O with |N(c)|<=NC, c in a fundamental domain for <lam>,+-1.  For each we compute
 u = Zhat(beta)/Z0 (twb transfer law, m=3p sites, L=8,K=16) and the exact core count at box delta.
Seam prediction for cross lines (Lemma S): the vacuum loses >= log_lam(D)-O(1) core sites, D=max(d+,d-).
usage: vacuum.py p NC"""
import sys, math, json, time, numpy as np
from sympy import factorint, isprime
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import TW, Zbatch, nu_rho
from twist_core import hp, lines
S2=math.sqrt(2); LAM=3+2*S2
def gamma0(h,W):
    # lattice {x+y sqrt2 : x == W y mod h}; Gauss-reduce in the form 2x^2+4y^2 (=|a|^2+|b|^2)
    B=[(h,0),(W%h,1)]
    q=lambda v: 2*v[0]**2+4*v[1]**2; bl=lambda u,v: 2*u[0]*v[0]+4*u[1]*v[1]
    u,v=B
    while True:
        if q(u)>q(v): u,v=v,u
        mu=round(bl(u,v)/q(u)); v=(v[0]-mu*u[0],v[1]-mu*u[1])
        if q(v)>=q(u): break
    for a in range(-3,4):
        for b in range(-3,4):
            x,y=a*u[0]+b*v[0],a*u[1]+b*v[1]; N=x*x-2*y*y
            if abs(N)==h: return x,y
            if abs(N)==2*h:   # divide by sqrt2: (x+y s2)/s2 = y + (x/2) s2
                if x%2==0: return y,x//2
    raise RuntimeError('no generator')
def small_c(NC):
    out=[]
    for y in range(0,40):
        for x in range(-80,81):
            N=x*x-2*y*y
            if N==0 or abs(N)>NC: continue
            a=x+y*S2; b=x-y*S2
            if a<=0: continue
            r=abs(a/b)
            if 1<=r<LAM**2: out.append((x,y,N))
    return sorted(set(out),key=lambda t:abs(t[2]))
def run(p,NC=40,delta=1/50):
    h=hp(p); fac=factorint(h); assert all(isprime(q) for q in fac)
    m=3*p; _,nu0=nu_rho(m,1); tw=TW(m,nu0,L=8,K=16); Z0=Zbatch(tw,np.zeros((1,m)))[0]
    i2=pow(2,-1,h); cs=small_c(NC); res=dict(p=p,h=h,factors=sorted(fac),NC=NC,ncs=len(cs),lines=[])
    pw=[]; x,y=1,0
    for i in range(m): pw.append((x,y)); x,y=(3*x+4*y)%h,(2*x+3*y)%h
    seen=set()
    for L in lines(p,h):
        key=tuple(L['signs']); neg=tuple(-s for s in key)
        if neg in seen: continue          # conj line has identical statistics (time reversal)
        seen.add(key)
        gx,gy=gamma0(h,L['W']); assert (gx-L['W']*gy)%h==0
        B=[]; meta=[]
        for (cx,cy,N) in cs:
            X=gx*cx+2*gy*cy; Y=gx*cy+gy*cx            # gamma = gamma0*c
            # beta = gamma*sqrt2/4 : (X+Y s2) s2 /4 = (2Y + X s2)/4 ; half: /8
            for k,div in ((0,4),(1,8)):
                inv=pow(div,-1,h); B.append(((2*Y*inv)%h,(X*inv)%h)); meta.append((cx,cy,N,k))
        bx=np.array([b[0] for b in B],object); by=np.array([b[1] for b in B],object)
        T=np.array([[ (2*(int(bx[j])*pw[i][0]+2*int(by[j])*pw[i][1]))%h/h for i in range(m)] for j in range(len(B))])
        core=((np.minimum(T,1-T)<delta)|(np.abs(T-0.5)<delta))[:,:p].sum(1)
        t0=time.time(); u=Zbatch(tw,T)/Z0
        k=int(np.argmax(np.abs(u)))
        D=max(L['dplus'],L['dminus']); kind='binet' if len(set(L['signs']))==1 else 'cross'
        row=dict(signs=L['signs'],kind=kind,dplus=L['dplus'],dminus=L['dminus'],log_lam_D=math.log(D)/math.log(LAM),
                 max_abs_u=float(abs(u[k])),argmax=meta[k],core_at_max=int(core[k]),max_core=int(core.max()),
                 sum_abs_u=float(np.abs(u).sum()),sec=time.time()-t0)
        res['lines'].append(row); print(json.dumps(row),flush=True)
    return res
if __name__=='__main__':
    p=int(sys.argv[1]); NC=int(sys.argv[2]) if len(sys.argv)>2 else 40
    r=run(p,NC); json.dump(r,open(f'/workspace/research1105b/logs/vacuum_p{p}_NC{NC}.json','w'),indent=1)
