"""Exact finite factor for the G2 (a,8) law restricted to the 16 reachable states, optional 3-cycle twist (d=7).
monomial(n) -> list of (out_state, in_state, phase_numerator_over_8 (int), twist index) ; integer arithmetic only."""
import math, sys
sys.path.insert(0,'/workspace/bgs-lineI/code')
from law import mdata
def g2params(m,a,b):
    D=mdata(m); h=D['h']; yp=D['yp']; M=2*h
    nu = next(x for x in [((a//2)*pow(b//2, -1, h)) % h + s*h for s in (0, 1)] if x % 2 == 1)
    assert (b*nu-a) % M == 0
    k=(b*nu-a)//M; psi0=yp%b; psi1=(3*yp-2*h)%b
    return dict(h=h,yp=yp,nu=nu,k=k%b,psi0=psi0,psi1=psi1,b=b)
def reach(P,Nmax):
    b=P['b']; tg=lambda s,n: (((6*(s//b)-(s%b)+n*P['psi1'])%b)*b+(((s//b)+n*P['psi0'])%b))
    orb={0}; fr=[0]
    while fr:
        s=fr.pop()
        for n in range(-Nmax,Nmax+1):
            t=tg(s,n)
            if t not in orb: orb.add(t); fr.append(t)
    idx=sorted(orb); return idx,tg
def taus7(bx,by):
    d=7; out=[]; x,y=1,0
    for i in range(3): out.append((2*(bx*x+2*by*y))%d); x,y=(3*x+4*y)%d,(2*x+3*y)%d
    return out   # tau_i = out[i]/7
def finite(P,idx,tg,n,cyc):
    """returns list of (out,in,ph8,tw7num) with phase e(-ph8/8) * e(n*tw/7); states numbered pos*3+i if cyc else pos."""
    b=P['b']; k=P['k']; pos={s:j for j,s in enumerate(idx)}; out=[]
    for s in idx:
        u=s//b; ph8=(k*((P['psi0']*n*n+2*n*u)%b))%b; t=tg(s,n); assert t in pos
        if cyc is None: out.append((pos[t],pos[s],ph8,0))
        else:
            for i in range(3): out.append((pos[t]*3+(i+1)%3,pos[s]*3+i,ph8,cyc[i]))
    return out
