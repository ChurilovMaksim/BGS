"""research1105b [N/CA]: for the top-|u| points of each line (p=11,13 exact 'ii' data), compute the cofactor c (beta*2sqrt2 = gamma0*c,
or beta*4sqrt2 for the half background), and the epsilon-profile G(n) = min height of a representative of c*eps^n mod abar,
height = max(|rho|,|rho'|).  Lemma S predicts for cross lines: min_n max(G(n),G(n+p)) >= ~ sqrt(D)/2 for primitive points."""
import sys, math, json, numpy as np
from sympy import factorint, sqrt_mod
from twist_core import hp, lines
from vacuum import gamma0
S2=math.sqrt(2)
def reduce2(u,v):
    q=lambda w:(w[0]+w[1]*S2)**2+(w[0]-w[1]*S2)**2; bl=lambda a,b:(a[0]+a[1]*S2)*(b[0]+b[1]*S2)+(a[0]-a[1]*S2)*(b[0]-b[1]*S2)
    while True:
        if q(u)>q(v): u,v=v,u
        mu=round(bl(u,v)/q(u)); v=(v[0]-mu*u[0],v[1]-mu*u[1])
        if q(v)>=q(u): return u,v
def minrep(cx,cy,u,v,R=6):
    # min over lattice points l of height(c - l); lattice basis u,v (integer coords x,y)
    a=cx+cy*S2; b=cx-cy*S2
    M=np.array([[u[0]+u[1]*S2,v[0]+v[1]*S2],[u[0]-u[1]*S2,v[0]-v[1]*S2]])
    z=np.linalg.solve(M,[a,b]); z0=np.round(z)
    best=1e300
    for i in range(-R,R+1):
        for j in range(-R,R+1):
            w=M@(z0+[i,j]); best=min(best,max(abs(a-w[0]),abs(b-w[1])))
    return best
def mul(a,b): return (a[0]*b[0]+2*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def run(p,prefix,top=6):
    h=hp(p); f=np.load(f'{prefix}_ii.npz'); Z0=complex(f['Z0']); bx=f['bx'].astype(object); by=f['by'].astype(object); u=f['Zh']/Z0
    out=[]
    for L in lines(p,h):
        gx,gy=gamma0(h,L['W']); W=L['W']
        # abar = conj line: x == -W y ; lattice basis (h,0),(-W,1)
        bu,bv=reduce2((h,0),((-W)%h,1))
        on=[(int(bx[k])-W*int(by[k]))%h==0 for k in range(len(bx))]
        idx=[k for k in np.argsort(-np.abs(u)) if on[k]][:top]
        # inverse of gamma0 mod abar: c = gamma*gamma0bar / N(gamma0) ; gamma0bar*gamma0 = N
        phig0=pow((gx+W*gy)%h,-1,h); epsW=(1+W)%h
        D=max(L['dplus'],L['dminus']); kind='binet' if len(set(L['signs']))==1 else 'cross'
        for k in idx:
            b=(int(bx[k]),int(by[k])); res=None
            for div,tag in ((4,'bg0'),(8,'bg1/2')):
                # gamma = beta * div / sqrt2 = beta*div*sqrt2/2
                g=mul(b,(0,div)); g=((g[0]*pow(2,-1,h))%h,(g[1]*pow(2,-1,h))%h)
                ci=((g[0]+W*g[1])*phig0)%h
                prof=[]
                for n in range(2*p):
                    prof.append(minrep(ci,0,bu,bv)); ci=(ci*epsW)%h
                pair=min(max(prof[n],prof[(n+p)%(2*p)]) for n in range(2*p))
                mn=min(prof)
                if res is None or mn<res['minG']: res=dict(bg=tag,minG=mn,pairmax=pair)
            out.append(dict(signs=L['signs'],kind=kind,D=D,sqrtD=math.sqrt(D),absu=float(abs(u[k])),**res))
            print(json.dumps(out[-1]),flush=True)
    return out
if __name__=='__main__':
    p=int(sys.argv[1]); r=run(p,sys.argv[2]); json.dump(r,open(f'/workspace/research1105b/logs/seam_profile_p{p}.json','w'),indent=1)
