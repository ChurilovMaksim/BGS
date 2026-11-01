if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import sys, math, json, numpy as np
sys.path.insert(0,'computations/verification/lineE/referee/code')
from aud import data
def gauss_reduce(u,v):
    # Lagrange-Gauss reduction, integer vectors
    def n2(w): return w[0]*w[0]+w[1]*w[1]
    if n2(u)>n2(v): u,v=v,u
    while True:
        d=u[0]*v[0]+u[1]*v[1]; nu=n2(u)
        q=(2*d+nu)//(2*nu)  # round(d/nu)
        v=(v[0]-q*u[0],v[1]-q*u[1])
        if n2(v)>=n2(u): return u,v
        u,v=v,u
def ratrec(N,h):
    u,v=gauss_reduce((h,0),(N%h,1))
    a,b=u
    if b<0: a,b=-a,-b
    return a,b   # N ≡ a/b mod h  (a ≡ N b)
def Z2all(T,m):
    d=data(m); h=d['h']; gp=d['gp']; yp=d['yp']
    S=np.fft.ifft(T)*h
    res=[]
    for nu in range(1,gp,2):
        if math.gcd(nu,gp)!=1: continue
        v=(-pow(16,-1,h)*pow(nu,-1,h)*pow(yp,-1,h))%h
        res.append((nu,abs(S[v])**2/h**2))
    return res
if __name__=='__main__':
    kick=sys.argv[1]; out=[]
    for m in [5,7,9,11,13,15]:
        T=np.load(f'computations/verification/lineE/referee/logs/T_{kick}_eta2.0_m{m}.npy')
        d=data(m); h=d['h']; R=Z2all(T,m); F=np.mean([z for _,z in R])
        rows=[]
        for nu,z in R:
            N=pow(nu,-1,h); a,b=ratrec(N,h); rows.append((z,nu,N,a,b))
        rows.sort(reverse=True)
        print(f'== {kick} m={m} h={h} units={len(R)} F/2m={F/(2*m):.4f}')
        for z,nu,N,a,b in rows[:24]:
            print(f'  |Z|^2={z:12.5g}  z/(2m)/phi={z/len(R)/(2*m):8.4f}  N≡{a}/{b}  ht={max(abs(a),b)}')
        # cumulative share by height
        hts=np.array([max(abs(a),b) for _,_,_,a,b in rows]); zs=np.array([r[0] for r in rows])
        for H in [4,10,30,100,300,1000]:
            sel=hts<=H
            print(f'  height<={H}: count={sel.sum()} share F/2m={zs[sel].sum()/len(R)/(2*m):.4f} rest F/2m={zs[~sel].sum()/len(R)/(2*m):.4f}')
        out.append(dict(m=m,h=h,rows=[(float(z),int(nu),int(N),int(a),int(b)) for z,nu,N,a,b in rows[:200]]))
    json.dump(out,open(f'../logs/step1_{kick}.json','w'))
