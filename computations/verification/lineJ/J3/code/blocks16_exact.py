"""EXACT block decomposition of the 64-state G2 (a,16) automaton, all 16 operator cases (m = 3 mod 6: 8 residues mod 48, a=+-2).
A_n: column s -> row tg(s,n), entry e(-ph/16), ph = k(psi0 n^2 + 2 n u) mod 16 (u = s//16).  Found numerically, verified EXACTLY:
 8 pairs (f1,f2), entries in {0} U {zeta16^e}, with A_n f1 = zeta^{p} f1, A_n f2 = zeta^{q} f2 (n even) / A_n f1 = zeta^p f2, A_n f2 = zeta^q f1 (n odd);
 all 16 vectors pairwise orthogonal with equal norms (Z[zeta16] arithmetic, basis 1..z^7, z^8=-1); u = sum_s e_s lies in their span.
Writes logs/blocks16_exact.json: per case, per block, the 2x2 monomial action (perm, exponents) for n mod 16 and the read-out J_b."""
import sys, json, hashlib, os, numpy as np
sys.path.insert(0,'/workspace/bgs-lineI/dom_v3')
from gstates import g2params, reach
here=os.path.dirname(os.path.abspath(__file__)); b=16
def zv(e):
    e%=16; v=[0]*8; v[e%8]=1 if e<8 else -1; return v
def zadd(u,v): return [x+y for x,y in zip(u,v)]
def zsum(es):
    s=[0]*8
    for e in es: s=zadd(s,zv(e))
    return s
def zmul(u,v):
    r=[0]*16
    for i in range(8):
        for j in range(8): r[i+j]+=u[i]*v[j]
    return [r[i]-r[i+8] for i in range(8)]
def zc(v): return complex(sum(v[i]*np.exp(2j*np.pi*i/16) for i in range(8)))
reps={}
for a in (2,-2):
    for m in range(3,49,6): reps[(a,m)]=m
out={}
for (a,m) in (list(reps) if len(sys.argv)<2 else [(int(sys.argv[2]),int(sys.argv[1]))]):
    P=g2params(m,a,b); idx,tg=reach(P,80); NS=len(idx); pos={s:j for j,s in enumerate(idx)}
    act={}
    for n in range(b):
        mp={}
        for s in idx:
            u=s//b; ph=(P['k']*((P['psi0']*n*n+2*n*u)%b))%b; mp[pos[s]]=(pos[tg(s,n)],(-ph)%b)
        act[n]=mp
    An=[np.zeros((NS,NS),complex) for n in range(b)]
    for n in range(b):
        for i,(o,e) in act[n].items(): An[n][o,i]=np.exp(2j*np.pi*e/b)
    # numerical: commutant isotypic clusters (generic hermitian commutant element), then a monomial basis inside each 2-dim cluster
    I=np.eye(NS); G=np.zeros((NS*NS,NS*NS),complex)
    for A in An:
        Mx=np.kron(I,A)-np.kron(A.T,I); G+=Mx.conj().T@Mx
    w_,v_=np.linalg.eigh(G); null=v_[:,w_<1e-8]
    rng=np.random.default_rng(1); Y=sum(rng.normal()*null[:,i].reshape(NS,NS,order='F') for i in range(null.shape[1])); Y=Y+Y.conj().T
    ew,ev=np.linalg.eigh(Y); cl=[]
    for i,z in enumerate(ew):
        if cl and abs(ew[cl[-1][0]]-z)<1e-6: cl[-1].append(i)
        else: cl.append([i])
    vecs=[]; uu=np.ones(NS)
    for c in cl:
        F=ev[:,c]
        if len(c)!=2 or np.linalg.norm(F.conj().T@uu)<1e-6: continue
        Bs=[F.conj().T@An[n]@F for n in range(b)]
        for w in [(n,) for n in range(b)]+[(n,k) for n in range(b) for k in range(b)]:
            M=np.eye(2,dtype=complex)
            for n in w: M=Bs[n]@M
            wv,V=np.linalg.eig(M)
            if abs(wv[0]-wv[1])<1e-6: continue
            Vi=np.linalg.inv(V); Cs=[Vi@B@V for B in Bs]
            if all(min(abs(C[0,1])+abs(C[1,0]),abs(C[0,0])+abs(C[1,1]))<1e-9 for C in Cs):
                f=F@V[:,0]; vecs.append(f/np.linalg.norm(f)); break
    # choose those with nonzero overlap structure; convert to exact exponent form
    def exact(f):
        j=np.argmax(abs(f)); f=f/(f[j]/abs(f[j])); mx=abs(f[j]); sup=[s for s in range(NS) if abs(f[s])>1e-6]
        assert np.allclose(abs(f[sup]),mx,atol=1e-8), 'non-flat'
        return {s:int(round(np.angle(f[s])/(2*np.pi)*b))%b for s in sup}
    print("joint even eigvecs",len(vecs))
    exs=[]
    for f in vecs:
        try: exs.append(exact(f))
        except AssertionError: pass
    def apply(n,ex):   # A_n applied to exponent-vector ex (dict s->e): returns dict
        r={}
        for s,e in ex.items():
            o,ph=act[n][s]; r[o]=(e+ph)%b
        return r
    def ratio(x,y):    # if x = zeta^k y exactly (same support), return k else None
        if set(x)!=set(y): return None
        ks={(x[s]-y[s])%b for s in x}
        return ks.pop() if len(ks)==1 else None
    print("flat",len(exs))
    blocks=[]; used=[]
    def inner(x,y):  # <x|y> exact
        return zsum([(y[s]-x[s])%b for s in set(x)&set(y)])
    for f1 in exs:
        if any(ratio(f1,g) is not None for g in used): continue
        nsw=next((n for n in range(b) if ratio(apply(n,f1),f1) is None),None)
        if nsw is None: continue
        f2=apply(nsw,f1); ok=True; actb={}
        for n in range(b):
            g1=apply(n,f1); g2=apply(n,f2)
            p=ratio(g1,f1); q=ratio(g2,f2); perm=(0,1)
            if p is None or q is None:
                p=ratio(g1,f2); q=ratio(g2,f1); perm=(1,0)
            if p is None or q is None: ok=False; break
            actb[n]=dict(perm=perm,exps=(p,q))
        if not ok: continue
        if inner(f1,f2)!=[0]*8: continue
        blocks.append(dict(f1=f1,f2=f2,act=actb)); used+= [f1,f2]
    # exact orthogonality of all vectors, equal norms
    allv=[v for B in blocks for v in (B['f1'],B['f2'])]
    nrm=NS   # common denominator; vector v has <v|v> = |supp v| (divides NS)
    for i,x in enumerate(allv):
        assert NS%len(x)==0
        for j,y in enumerate(allv):
            g=inner(x,y); assert g==([len(x)]+[0]*7 if i==j else [0]*8),(i,j)
    # u or e0 in span (either suffices: <u|A_w|e0> = <P u|A_w|P e0>, P = projector on the span, A_w preserve span and complement)
    recon={s:[0]*8 for s in range(NS)}
    for v in allv:
        cu=[x*(NS//len(v)) for x in zsum([(-e)%b for e in v.values()])]
        for s,e in v.items(): recon[s]=zadd(recon[s],zmul(cu,zv(e)))
    u_in=all(recon[s]==[nrm]+[0]*7 for s in range(NS))
    s0=pos[0]; recon0={s:[0]*8 for s in range(NS)}
    for v in allv:
        if s0 not in v: continue
        c0=[x*(NS//len(v)) for x in zv(-v[s0])]
        for s,e in v.items(): recon0[s]=zadd(recon0[s],zmul(c0,zv(e)))
    e0_in=all(recon0[s]==([nrm]+[0]*7 if s==s0 else [0]*8) for s in range(NS))
    Uf=np.array([[ (np.exp(2j*np.pi*v[s]/b)/np.sqrt(len(v)) if s in v else 0) for s in range(NS)] for v in allv]).T
    uu=np.ones(NS); ee=np.zeros(NS); ee[s0]=1
    print('nblocks',len(blocks),'nrm',nrm,'|P u|^2',np.linalg.norm(Uf.conj().T@uu)**2,'/',NS,' |P e0|^2',np.linalg.norm(Uf.conj().T@ee)**2,flush=True)
    assert u_in or e0_in, 'neither u nor e0 in span'
    # read-out J_b[j][k] = <f_j|e0><u|f_k>/nrm  (e0 = state 0 = pos[0])
    s0=pos[0]; Jb=[]
    for B in blocks:
        fs=(B['f1'],B['f2']); J=[[None,None],[None,None]]
        for j in range(2):
            for k in range(2):
                a_=zv(-fs[j][s0]) if s0 in fs[j] else [0]*8
                c_=zsum(list(fs[k].values()))
                J[j][k]=[x*(NS//len(fs[j])) for x in zmul(a_,c_)]
        Jb.append(J)
        B['J_times_nrm']=J; B['J_fro']=float(np.sqrt(sum(abs(zc(J[j][k]))**2 for j in range(2) for k in range(2))))/nrm
        B['f1']={str(k):v for k,v in B['f1'].items()}; B['f2']={str(k):v for k,v in B['f2'].items()}
        B['act']={str(n):v for n,v in B['act'].items()}
    out[f'{m},{a}']=dict(u_in_span=u_in,e0_in_span=e0_in,params=P,nblocks=len(blocks),dim_span=2*len(blocks),norm2=nrm,blocks=blocks)
    print(m,a,'u_in',u_in,'e0_in',e0_in,'k,psi0,psi1',P['k'],P['psi0'],P['psi1'],'blocks',len(blocks),'J_fro',[round(B['J_fro'],4) for B in blocks],
          'acts n=0,1',[ (B['act']['0']['exps'],B['act']['1']['exps']) for B in blocks],flush=True)
json.dump(dict(code_sha256=hashlib.sha256(open(__file__,'rb').read()).hexdigest(),cases=out),open(os.path.join(here,'../logs/blocks16_exact.json'),'w'))
print('ALL EXACT CHECKS PASSED')
