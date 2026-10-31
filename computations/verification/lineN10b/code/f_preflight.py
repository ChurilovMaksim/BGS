"""N10b [N]: scaled pre-flight of the cone-field certificate on the 1024-grid (outside the 1/8 box of ALL four slow fixed points
(t,t), 4t=0): for a random subsample of cell centres, test k-step cone invariance (condition of b_conecheck.py) in the averaged-
Lyapunov norm W (J=8, rho=1.3), k in {6,8,12}.  Checkpoints: ckpt/f_preflight.json after every chunk (resumable).  usage: f_preflight.py NS"""
import sys, os, json, time, numpy as np
sys.path.insert(0,'/workspace/bgs-lineF/code')
from lift import ops, wk1
NS=int(sys.argv[1]); G=1024; TH=0.125; KS=(6,8,12)
K0,r,K,beta,N0=3,1.2,20,2.5,10
Bn={}
for n in range(-N0,N0+1):
    V,E=ops(lambda m,n=n: 1.0 if m==n else 0.0, N0,K0,r,r,K,beta=beta); Bn[n]=V
ns=np.array(sorted(Bn)); Bst=np.stack([Bn[n] for n in ns]); w0=wk1(2.0,4); w=np.array([w0(int(n)) for n in ns])
L0=lambda t: np.tensordot(w*np.exp(2j*np.pi*ns*t),Bst,axes=(0,0))
T=lambda y: np.array([y[1],(6*y[1]-y[0])%1]); Ti=lambda y: np.array([(6*y[0]-y[1])%1,y[0]])
rng=np.random.default_rng(7)
Y=rng.random((600,2)); Q=np.zeros((140,140),complex)
for y in Y:
    P=np.eye(140,dtype=complex); z=y.copy()
    for j in range(9): Q+=1.3**(-2*j)*(P.conj().T@P)/len(Y); P=L0(z[0])@P; z=T(z)
ev,U=np.linalg.eigh(Q); W=(U*np.sqrt(ev))@U.conj().T; Wi=(U/np.sqrt(ev))@U.conj().T
L=lambda t: W@L0(t)@Wi
def tdist(x): x=x%1.0; return min(x,1-x)
def inbox(y): return any(max(tdist(y[0]-f),tdist(y[1]-f))<TH for f in (0,.25,.5,.75))
def udir(y,J=10):
    h=[y]
    for i in range(J): h.append(Ti(h[-1]))
    v=np.ones(140,complex)
    for i in range(J,0,-1): v=L(h[i][0])@v; v/=np.linalg.norm(v)
    return v
ck='ckpt/f_preflight.json'
st=json.load(open(ck)) if os.path.exists(ck) else dict(done=0,ok={str(k):0 for k in KS},n=0,ratios={str(k):[] for k in KS})
cells=rng.integers(0,G,size=(NS*3,2))
cells=[c for c in cells if not inbox((c+0.5)/G)][:NS]
t0=time.time()
for idx in range(st['done'],len(cells)):
    y=(cells[idx]+0.5)/G; u=udir(y); M=np.eye(140,dtype=complex); z=y.copy(); kk=0
    for k in KS:
        while kk<k: M=L(z[0])@M; z=T(z); kk+=1
        u2=udir(z); Pp=np.eye(140)-np.outer(u,u.conj()); Pp2=np.eye(140)-np.outer(u2,u2.conj())
        a0=abs(u2.conj()@M@u); s1=np.linalg.norm(u2.conj()@M@Pp); s2=np.linalg.norm(Pp2@M@Pp,2); b0=np.linalg.norm(Pp2@M@u)
        st['ok'][str(k)]+=int((a0>s2) and ((a0-s2)**2>=4*s1*b0)); st['ratios'][str(k)].append(float(s2/a0))
    st['n']+=1; st['done']=idx+1
    if st['done']%200==0 or st['done']==len(cells):
        json.dump(st,open(ck+'.tmp','w')); os.replace(ck+'.tmp',ck)
        print(st['done'],{k:st['ok'][k] for k in st['ok']},'median s2/a0',{k:round(float(np.median(st['ratios'][k])),3) for k in st['ratios']},round(time.time()-t0),'s',flush=True)
json.dump(dict(n=st['n'],ok=st['ok'],frac={k:st['ok'][k]/st['n'] for k in st['ok']},median={k:float(np.median(st['ratios'][k])) for k in st['ratios']},
               max_ratio={k:float(np.max(st['ratios'][k])) for k in st['ratios']}),open('logs/f_preflight.json','w'),indent=1)
print('DONE',flush=True)
