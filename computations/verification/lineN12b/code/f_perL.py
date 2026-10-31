"""N12b f_perL (copy of N9b a_per.py + box-run statistic) [N]: spectral rates rho(P_n)^{1/n} of ALL periodic orbits of the twist cat map A=[[0,1],[-1,6]] on (tau_i,tau_{i+1}) in T^2,
period n<=NMAX, for the Line-F lifted 8V operator (sector a=4; N2 c2 parameters).  Records per orbit: rate, min sup-distance of the
orbit to the slow fixed point (0,0) and to the other fixed points (1/4,1/4),(1/2,1/2),(3/4,3/4).  usage: a_per.py NMAX [a] [NMIN]"""
import sys, math, json, time, numpy as np
sys.path.insert(0,'/workspace/bgs-lineF/code')
from lift import ops, wk1
NMAX=int(sys.argv[1]); a=int(sys.argv[2]) if len(sys.argv)>2 else 4; NMIN=int(sys.argv[3]) if len(sys.argv)>3 else 1
K0,r,K,beta,N0=3,1.2,20,2.5,10
Bn={}
for n in range(-N0,N0+1):
    V,E=ops(lambda m,n=n: 1.0 if m==n else 0.0, N0,K0,r,r,K,beta=beta); Bn[n]=V
ns=np.array(sorted(Bn)); Bst=np.stack([Bn[n] for n in ns])
w0=wk1(2.0,a); w=np.array([w0(int(n)) for n in ns])
def Lbatch(t): return np.tensordot(w[None,:]*np.exp(2j*np.pi*np.outer(t,ns)),Bst,axes=([1],[0]))
def dist(x):
    x=np.abs(x)%1.0; return np.minimum(x,1-x)
out=open(f'/workspace/bgs-lineN/N12b/logs/f_perL_a{a}.jsonl','a'); t0=time.time()
for n in range(NMIN,NMAX+1):
    A=np.array([[0,1],[-1,6]],dtype=object); P=np.eye(2,dtype=object)
    for _ in range(n): P=P.dot(A)
    M=P-np.eye(2,dtype=object); D=abs(int(M[0,0]*M[1,1]-M[0,1]*M[1,0]))
    adj=[[int(M[1,1]),-int(M[0,1])],[-int(M[1,0]),int(M[0,0])]]
    c1=(adj[0][0]%D,adj[1][0]%D); c2=(adj[0][1]%D,adj[1][1]%D)
    o1=D//math.gcd(D,math.gcd(c1[0],c1[1])) if (c1[0] or c1[1]) else 1
    base=[((i*c1[0])%D,(i*c1[1])%D) for i in range(o1)]
    cur=set(base); frontier=list(base)
    while True:
        new=[((x+c2[0])%D,(y+c2[1])%D) for (x,y) in frontier]
        new=[q for q in new if q not in cur]
        if not new: break
        cur.update(new); frontier=new
    assert len(cur)==D, (n,len(cur),D)
    seen=set(); orbs=[]
    for q in cur:
        if q in seen: continue
        orb=[q]; x=q
        while True:
            x=(x[1],(6*x[1]-x[0])%D)
            if x==q: break
            orb.append(x)
        seen.update(orb); orbs.append(orb)
    orbs=[o for o in orbs if len(o)==n]
    recs=[]; B=300
    for s in range(0,len(orbs),B):
        ch=orbs[s:s+B]; Pm=np.broadcast_to(np.eye(Bst.shape[1],dtype=complex),(len(ch),)+Bst.shape[1:]).copy()
        for i in range(n):
            t=np.array([o[i][0]/D for o in ch]); Pm=np.matmul(Lbatch(t),Pm)
        ev=np.linalg.eigvals(Pm); rr=np.abs(ev).max(axis=1)**(1/n)
        for o,rate in zip(ch,rr):
            arr=np.array(o,float)/D
            d0=float(np.max(dist(arr),axis=1).min())
            inb=(np.max(dist(arr),axis=1)<=0.125)
            if inb.all(): run=10**6
            else:
                k0=int(np.argmin(inb)); rr_=0; run=0
                for q in range(n):
                    if inb[(k0+q)%n]: rr_+=1; run=max(run,rr_)
                    else: rr_=0
            dq=[float(np.max(dist(arr-f),axis=1).min()) for f in (.25,.5,.75)]
            recs.append((float(rate),d0,dq,o[0],run))
    recs.sort(key=lambda z:-z[0])
    prof={}
    for th in (0.0,1/64,1/32,1/16,1/8,3/16,1/4):
        cand=[z[0] for z in recs if z[1]>=th]; prof[str(th)]=max(cand) if cand else None
    profL={str(L):max([z[0] for z in recs if z[4]<L],default=None) for L in range(1,9)}
    rec=dict(n=n,D=D,orbits=len(orbs),profL=profL,top=[(z[0],z[1],z[2],[z[3][0],z[3][1],D],z[4]) for z in recs[:10]],profile=prof,
             frac_above_Tp=sum(1 for z in recs if z[0]>1.4279)/max(1,len(recs)),sec=round(time.time()-t0,1))
    out.write(json.dumps(rec)+'\n'); out.flush()
    print(n,D,len(orbs),{k[:6]:(round(v,4) if v else v) for k,v in prof.items()},'top',[(round(z[0],4),round(z[1],3)) for z in recs[:4]],rec['sec'],flush=True)
