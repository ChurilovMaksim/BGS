"""[N] composite level d=7q inheritance: for beta = q*beta' (trivial q-part) the twisted coefficient is the d=7 one (same twist),
and the level-d weight W_{d,C} = sum_{t in M_d} conj G_t(0) sum_{beta in qC} G_t(beta) / d^4 (frozen member rule, label t = j y' mod d)
is compared with W_{7,C}.  Example m=15 (h = 7*31^2*41), d = 287 and 217."""
import sys, math, numpy as np, json
sys.path.insert(0,'/workspace/bgs-lineI/code')
from law import mdata
def orbit(bx,by,d=7):
    o=set(); x,y=bx,by
    for i in range(3):
        o.add((x%7,y%7)); o.add((-x%7,-y%7)); x,y=(3*x+4*y)%7,(2*x+3*y)%7
    return sorted(o)
cls=['1:3','2:1','0:1','1:2','1:5','0:3','1:0','0:2']
def members(m,a,d,proper):
    D=mdata(m); h=D['h']; yp=D['yp']; assert h%d==0
    nu0=next(x for x in [((a//2)*pow(4,-1,h))%h+s*h for s in (0,1)] if x%2==1)
    ts=[]
    for j in range(1,d):
        nu=(nu0+(2*h//d)*j)%(2*h)
        if math.gcd(nu,2*h)!=1: continue
        if any(j%(d//dp)==0 for dp in proper): continue      # bnu = a mod 2h/d'  <=> (d/d') | j
        ts.append((j*yp)%d)
    return ts
def Wlevel(m,a,d,proper,scale):
    g=np.arange(d); GX,GY=np.meshgrid(g,g,indexing='ij'); N=(GX*GX-2*GY*GY)%d
    ts=members(m,a,d,proper); out={}
    for c in cls:
        Bs=[((scale*bx)%d,(scale*by)%d) for (bx,by) in orbit(*map(int,c.split(':')))]
        tot=0
        for t in ts:
            G0=np.exp(-2j*np.pi*((t*N)%d)/d).sum()
            Gb=sum(np.exp(-2j*np.pi*((t*N+2*(bx*GX+2*by*GY))%d)/d).sum() for bx,by in Bs)
            tot+=np.conj(G0)*Gb
        out[c]=tot/d**4
    return out,len(ts)
res={}
for m,a in ((15,2),(15,-2),(33,2)):
    W7,n7=Wlevel(m,a,7,[1],1)
    for q in {15:(41,31),33:(23,)}[m]:
        Wd,nd=Wlevel(m,a,7*q,[1,7,q],q)
        r={c:(abs(Wd[c])*q, abs(W7[c]), complex(Wd[c]*q/W7[c]) if abs(W7[c])>1e-12 else None) for c in cls}
        print(m,a,'q',q,'n_7',n7,'n_7q',nd, {c:(round(v[0],5),round(v[1],5)) for c,v in r.items()},flush=True)
        res[f'{m},{a},{q}']={c:[v[0],v[1],None if v[2] is None else [v[2].real,v[2].imag]] for c,v in r.items()}; print('   ratio qW_7q/W_7:',{c:(None if v[2] is None else (round(v[2].real,5),round(v[2].imag,5))) for c,v in r.items()},flush=True)
json.dump(res,open('logs/inherit7q.json','w'),indent=1)
