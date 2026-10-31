"""Referee: full recomputation of Gamma_per(theta,L) over all primitive periodic orbits n<=NMAX of the twist cat map,
Line-F default op (agrees with N12 core to 1e-9 on spot checks), for several box sizes theta. Own enumeration (all (x,y) mod D)."""
import sys, json, numpy as np, time
sys.path.insert(0,'/workspace/audit/lineN13/code')
NMAX=int(sys.argv[1])
exec(open('/workspace/audit/lineN13/code/ref_perL.py').read().split("z=np.load")[0])
op=lineF(3,1.2,20,2.5,10); nrm=float(np.abs(np.linalg.eigvals(op(0.0))).max()); MU=1.9154712
def dist(v): v=np.abs(v)%1.0; return np.minimum(v,1-v)
THS=[1/16,3/32,1/8,5/32,3/16,1/4]; out={}
for n in range(1,NMAX+1):
    Mn=np.linalg.matrix_power(np.array([[0,1],[-1,6]],dtype=object),n)-np.eye(2,dtype=object)
    D=abs(int(Mn[0,0]*Mn[1,1]-Mn[0,1]*Mn[1,0]))
    # periodic points: v with (A^n - I) v in Z^2  <=> v = (A^n-I)^{-1} k ; enumerate via adjugate lattice
    adj=np.array([[int(Mn[1,1]),-int(Mn[0,1])],[-int(Mn[1,0]),int(Mn[0,0])]],dtype=object)
    pts=set()
    for i in range(D):
        for j in [0]: pass
    # generate lattice adj*Z^2 mod D by BFS on two generators
    g=[(int(adj[0,0])%D,int(adj[1,0])%D),(int(adj[0,1])%D,int(adj[1,1])%D)]
    pts={(0,0)}; fr=[(0,0)]
    while fr:
        nf=[]
        for p in fr:
            for q in g:
                r=((p[0]+q[0])%D,(p[1]+q[1])%D)
                if r not in pts: pts.add(r); nf.append(r)
        fr=nf
    assert len(pts)==D
    seen=set(); orbs=[]
    for p in pts:
        if p in seen: continue
        o=[p]; x,y=p
        while True:
            x,y=y,(6*y-x)%D
            if (x,y)==p: break
            o.append((x,y))
        seen.update(o)
        if len(o)==n: orbs.append(o)
    rates=[]
    for k in range(0,len(orbs),200):
        ch=orbs[k:k+200]; P=None
        for i in range(n):
            t=np.array([o[i][0]/D for o in ch]); L=np.tensordot(np.exp(2j*np.pi*np.outer(t,np.arange(-10,11))),np.zeros(1),0) if False else None
            Lb=np.stack([op(tt) for tt in t]); P=Lb if P is None else np.matmul(Lb,P)
        rates+=list(MU*np.abs(np.linalg.eigvals(P)).max(axis=1)**(1/n)/nrm)
    for th in THS:
        prof={}
        for o,rt in zip(orbs,rates):
            arr=np.array(o,float)/D; inb=list(np.max(dist(arr),axis=1)<=th)
            if all(inb): rn=10**6
            else:
                k0=inb.index(False); r=m=0
                for q in range(n): r=r+1 if inb[(k0+q)%n] else 0; m=max(m,r)
                rn=m
            for L in range(1,7):
                if rn<L: prof[L]=max(prof.get(L,0),float(rt))
        out.setdefault(str(th),{})[n]=prof
    print(n,D,len(orbs),{th:{L:round(v,4) for L,v in out[str(th)][n].items()} for th in ('0.125','0.25')},flush=True)
    json.dump(out,open(f'logs/ref_perL_all_n{NMAX}.json','w'),indent=1)
