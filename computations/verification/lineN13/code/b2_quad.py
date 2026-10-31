"""N13 (B2) [CA]: quadratic single-step bound near the slow twist, all inputs in arb.
Bound (derivation in REPORT_N13 sec 2): for ||v||_H = 1, a = psi v, q = Qt v, w = (A(t)/s) v = (M + tE1 + R(t)) v, ||R(t)||_H <= L2 t^2/2:
  (nP|psi w|, ||Qt w||) <= M2(t) (nP|a|, ||q||) + add(t),  M2 = [[1+da, nP c1 t],[b1 t/nP, kap' + b2 t]],
  nP^2|a|^2 + ||q||^2 <= 1 + 2 g |a|,   ||w||^2 <= nP^2|psi w|^2 + ||Qt w||^2 + 2 g nP... (Pythagoras with defect g = ||Phi^* H Qt||_{H*})
Certified scalars: nP=||Phi||_H, ||psi||_*, g, da (=|psi M Phi - 1| + |1-psi Phi|), |eps0|, b1=||Qt E1 Phi||_H, c1=||psi E1 Qt||_*, b2 (PSD), ||psi M - psi||_*,
||M Phi - Phi||_H, ||psi E1||_*, |1-psi Phi|; L2 and kap'=kap(1+eta)^2 from b_arb.json (V3a,V3b)."""
import sys, json, time, math, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N6/code')
import cert_core as C
from flint import arb, acb, acb_mat, ctx
ctx.prec=96; t00=time.time()
def log(*a): print(round(time.time()-t00,1),*a,flush=True)
B=json.load(open('/workspace/bgs-lineN/N13/logs/b_arb.json'))
z=np.load('/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45.npz')
Tf=z['T']; sf=complex(z['s']); Phif=z['Phi']; psif=z['psi']; kap=float(z['kap']); D=C.D; K=C.K
def tomat(X): return acb_mat(X.shape[0],X.shape[1],[acb(complex(x).real,complex(x).imag) for x in X.ravel()])
def tonp(M): return np.array([[complex(float(e.real.mid()),float(e.imag.mid())) for e in row] for row in M.tolist()])
def ctr(M): return M.transpose().conjugate()
def fro_up(M):
    s=arb(0)
    for row in M.tolist():
        for e in row: s+=abs(e)**2
    return float(s.sqrt().upper())
def psd(G,sig):
    Gh=(G+ctr(G))*acb(0.5); Gm=tonp(Gh); Gm=(Gm+Gm.conj().T)/2
    try: L=np.linalg.cholesky(Gm-sig*np.eye(Gm.shape[0]))
    except np.linalg.LinAlgError: return False,None
    La=tomat(L); n=Gm.shape[0]
    E=Gh-La*ctr(La)-acb_mat(n,n,[acb(sig) if i==j else acb(0) for i in range(n) for j in range(n)])
    e=fro_up(E); return e<sig,e
T=tomat(Tf); H=ctr(T)*T; s=acb(sf.real,sf.imag)
Phi=tomat(Phif.reshape(-1,1)); psi=tomat(psif.reshape(1,-1))
I=acb_mat(D,D,[acb(1) if i==j else acb(0) for i in range(D) for j in range(D)]); Qt=I-Phi*psi
A0=acb_mat(D,D); E1=acb_mat(D,D)
E=[[acb(0)]*D for _ in range(D)]; E1l=[[acb(0)]*D for _ in range(D)]
for (c2,n),(j2,Mx) in C.blocks.items():
    w=C.wa(4,n); w1=w*2*C.pi*C.I*n; i0=C.idx[c2]*K; j0=C.idx[j2]*K
    for i in range(K):
        for j in range(K):
            E[i0+i][j0+j]+=Mx[i,j]*w; E1l[i0+i][j0+j]+=Mx[i,j]*w1
M=acb_mat(E)*(1/s); E1=acb_mat(E1l)*(1/s); log('M,E1 built')
def vnorm(x): return ((ctr(x)*H*x)[0,0].real).sqrt()
def dnorm(y):  # dual norm of row vector y: sqrt(y H^{-1} y^*)
    zz=H.solve(ctr(y)); return abs((y*zz)[0,0]).sqrt()
up=lambda x: float(x.upper()) if hasattr(x,'upper') else float(abs(x).upper())
psiPhi=(psi*Phi)[0,0]
res=dict(nP=up(vnorm(Phi)),nP_lo=float(vnorm(Phi).lower()),psi_dual=up(dnorm(psi)),one_minus_psiPhi=up(abs(1-psiPhi)))
res['g']=up(dnorm(ctr(Phi)*H*Qt)); log('g',res['g'])
res['da']=up(abs((psi*M*Phi)[0,0]-1))+res['one_minus_psiPhi']
res['eps0']=up(abs((psi*E1*Phi)[0,0]))
res['b1']=up(vnorm(Qt*E1*Phi)); res['c1']=up(dnorm(psi*E1*Qt)); log('b1,c1',res['b1'],res['c1'])
res['psiM_minus_psi']=up(dnorm(psi*M-psi)); res['MPhi_minus_Phi']=up(vnorm(M*Phi-Phi)); res['psiE1_dual']=up(dnorm(psi*E1))
X=Qt*E1*Qt; Xf=tonp(X); Tinv=np.linalg.inv(Tf); b2f=np.linalg.norm(Tf@Xf@Tinv,2); b2=b2f*1.001
ok,e=psd(H*acb(b2*b2)-ctr(X)*H*X,1e-6*b2*b2); res['b2']=b2; res['b2_ok']=bool(ok); log('b2',b2,ok,e)
res['L2']=B['L2']; eta=B['V2']['eta']; res['kapp']=kap*(1+eta)**2
json.dump(res,open('/workspace/bgs-lineN/N13/logs/b2_quad.json','w'),indent=1)
# evaluate the bound
nP=res['nP']; nPl=res['nP_lo']; g=res['g']; tiny=res['psiM_minus_psi']+res['psiE1_dual']*2*res['one_minus_psiPhi']*nP*res['psi_dual']
def bound(t):
    m=np.array([[1+res['da']+t*res['eps0'], nP*res['c1']*t],[res['b1']*t/nPl, res['kapp']+res['b2']*t]])
    rad=math.sqrt(1+2*g*res['psi_dual'])
    sig=np.linalg.norm(m,2)*rad
    add=nP*(tiny+res['psi_dual']*res['L2']*t*t/2)+(1+eta)*(res['MPhi_minus_Phi']*res['psi_dual']+res['L2']*t*t/2)
    W=sig+add*math.sqrt(2)
    gw=g*(res['psi_dual'])*W     # Pythagoras defect
    return gw+math.sqrt(gw*gw+W*W)
rows=[]
for t in [0,1/65536,1/16384,1/4096,1/2048,1/1024,1/512,1/256,1/128]:
    b=bound(t)*1.0000001; rows.append(dict(t=t,bound=b,coef=(b-1)/t**2 if t>0 else None)); log(rows[-1])
res['rows']=rows
res['statement']='||A(t)/s||_H <= bound(t) (table) ; N_H(t) <= 1 + C2 t^2 + c0 with c0=bound(0)-1'
res['c0']=rows[0]['bound']-1; res['C2_max_t<=1/256']=max(r['coef'] for r in rows[1:] if r['t']<=1/256)
json.dump(res,open('/workspace/bgs-lineN/N13/logs/b2_quad.json','w'),indent=1); log('done',res['c0'],res['C2_max_t<=1/256'])
