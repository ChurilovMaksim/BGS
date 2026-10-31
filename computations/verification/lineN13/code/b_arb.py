"""N13 (B) [CA]: interval (arb, python-flint) upgrade of the N12 adapted-norm checks.
All matrices are acb_mat; the norm is DEFINED by the stored float T (exact binary64 entries): ||v||_H^2 = v^* H v, H := T^* T (computed in arb).
A0 = sum_n w_4(n) M_n assembled from N6 cert_core arb blocks (their radii included). s, Phi, psi, Qt = I - Phi psi^T: exact binary64 data.
PSD test psd(G, sig): float Cholesky L of mid(G_h) - sig I (G_h = Hermitian part), E = G_h - sig I - L L^* in arb; if ||E||_F < sig then G_h >= 0.
Checks: V1 c_lo^2 I <= H <= c_hi^2 I; V2 ||A0/s||_H <= 1+eta; V3a ||Qt||_H <= 1+eta; V3b ||(A0/s)Qt||_H <= kap(1+eta);
per-n ||M_n||_H <= c_n (=> Lip_H, L2, Nsum certified); quadratic step constant via the block matrix
K = [[G0, G1/2],[G1/2, G2]] >= 0, G0=(1+eta)^2 H - M^*HM, G1 = M^*HE1+E1^*HM, G2 = c H - E1^*HE1  =>  ||M + tE1||_H^2 <= (1+eta)^2 + c t^2 for ALL real t."""
import sys, json, time, math, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N6/code')
import cert_core as C
from flint import arb, acb, acb_mat, ctx
ctx.prec=96
t00=time.time(); OUT='/workspace/bgs-lineN/N13/logs/b_arb.json'; res={}
def log(*a):
    print(round(time.time()-t00,1),*a,flush=True)
def save(): json.dump(res,open(OUT,'w'),indent=1)
z=np.load('/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45.npz')
Tf=z['T']; sf=complex(z['s']); Phif=z['Phi']; psif=z['psi']; kap=float(z['kap'])
D=C.D; K=C.K
def tomat(X): return acb_mat(X.shape[0],X.shape[1],[acb(complex(x).real,complex(x).imag) for x in X.ravel()])
def tonp(M):
    L=M.tolist(); return np.array([[complex(float(e.real.mid()),float(e.imag.mid())) for e in row] for row in L])
def ctr(M): return M.transpose().conjugate()
def fro_up(M):
    s=arb(0)
    for row in M.tolist():
        for e in row: s+=abs(e)**2
    return float(s.sqrt().upper())
def psd(G,sig):
    Gh=(G+ctr(G))*acb(0.5)
    Gm=tonp(Gh); Gm=(Gm+Gm.conj().T)/2
    try: L=np.linalg.cholesky(Gm-sig*np.eye(Gm.shape[0]))
    except np.linalg.LinAlgError: return False, None
    La=tomat(L); E=Gh-La*ctr(La)-acb_mat(Gm.shape[0],Gm.shape[0],[acb(sig) if i==j else acb(0) for i in range(Gm.shape[0]) for j in range(Gm.shape[0])])
    e=fro_up(E); return e<sig, e
T=tomat(Tf); H=ctr(T)*T; log('H built')
s=acb(sf.real,sf.imag); Phi=tomat(Phif.reshape(-1,1)); psi=tomat(psif.reshape(1,-1))
I=acb_mat(D,D,[acb(1) if i==j else acb(0) for i in range(D) for j in range(D)])
Qt=I-Phi*psi
# assemble M_n (arb) on the fly
ns=sorted(set(n for (c2,n) in C.blocks))
def Mn(n):
    E=[[acb(0)]*D for _ in range(D)]
    for (c2,nn),(j2,Mx) in C.blocks.items():
        if nn!=n: continue
        i0=C.idx[c2]*K; j0=C.idx[j2]*K
        for i in range(K):
            for j in range(K): E[i0+i][j0+j]=E[i0+i][j0+j]+Mx[i,j]
    return acb_mat(E)
A0=acb_mat(D,D); E1=acb_mat(D,D); Mlist={}
eta=float(sys.argv[1]) if len(sys.argv)>1 else 1e-6
# float H-norms for c_n targets
Ti=np.linalg.inv(Tf)
cn={}
for n in ns:
    M=Mn(n); w=C.wa(4,n)
    A0=A0+M*w; E1=E1+M*(w*2*C.pi*C.I*n)
    Mf=tonp(M); fl=np.linalg.norm(Tf@Mf@Ti,2)
    c=fl*1.0001+1e-12
    G=H*acb(c*c)-ctr(M)*H*M
    ok,e=psd(G,1e-9*c*c)
    if not ok:
        c=fl*1.01+1e-9; ok,e=psd(H*acb(c*c)-ctr(M)*H*M,1e-7*c*c)
    cn[n]=dict(c=c,ok=bool(ok),float=fl,err=e); log('n',n,cn[n])
res['Mn_H']={str(k):v for k,v in cn.items()}; save()
M=A0*(1/s); E1=E1*(1/s)
absw=[float(abs(C.wa(4,n)).upper()) for n in ns]
res['Lip_H']=float(2*math.pi/abs(sf)*sum(abs(n)*a*cn[n]['c'] for n,a in zip(ns,absw)))*(1+1e-12)
res['L2']=float((2*math.pi)**2/abs(sf)*sum(n*n*a*cn[n]['c'] for n,a in zip(ns,absw)))*(1+1e-12)
res['Nsum']=float(1/abs(sf)*sum(a*cn[n]['c'] for n,a in zip(ns,absw)))*(1+1e-12)
res['all_Mn_ok']=all(v['ok'] for v in cn.values()); log('Lip',res['Lip_H'],'L2',res['L2'],'Nsum',res['Nsum']); save()
# V1
ev=np.linalg.eigvalsh(Tf.conj().T@Tf); clo=math.sqrt(ev.min())*0.999; chi=math.sqrt(ev.max())*1.001
ok1,e1=psd(H-I*acb(clo*clo),1e-6*clo*clo); ok1b,e1b=psd(I*acb(chi*chi)-H,1e-6*clo*clo)
res['V1']=dict(c_lo=clo,c_hi=chi,cond=chi/clo,ok=bool(ok1 and ok1b),err=[e1,e1b]); log('V1',res['V1']); save()
# V2, V3
MHM=ctr(M)*H*M
ok2,e2=psd(H*acb((1+eta)**2)-MHM, eta*clo*clo); res['V2']=dict(eta=eta,ok=bool(ok2),err=e2); log('V2',res['V2'])
ok3,e3=psd(H*acb((1+eta)**2)-ctr(Qt)*H*Qt, eta*clo*clo); res['V3a']=dict(ok=bool(ok3),err=e3); log('V3a',res['V3a'])
MQ=M*Qt; ok4,e4=psd(H*acb((kap*(1+eta))**2)-ctr(MQ)*H*MQ, 1e-4); res['V3b']=dict(kap=kap,ok=bool(ok4),err=e4); log('V3b',res['V3b']); save()
# commutation / eigen residual enclosures (informational)
r1=M*Phi-Phi; r2=psi*M-psi
res['resid_Phi_H']=float(((ctr(r1)*H*r1)[0,0].real).sqrt().upper()) if True else None
res['psiPhi']=str((psi*Phi)[0,0]); res['eps0']=str((psi*E1*Phi)[0,0]); log('eps0',res['eps0'],'psiPhi',res['psiPhi']); save()
# Perturbation (Galerkin->true, 2-norm Pert from n_cert) in H coordinates
Pert=float((C.delta+C.Delta).upper()); res['Pert_2']=Pert; res['Pert_H_rel']=chi/clo*Pert/abs(sf)*(1+1e-12)
# quadratic constant: find c by float, certify K>=0
G0=H*acb((1+eta)**2)-MHM; MHE=ctr(M)*H*E1; G1=MHE+ctr(MHE); EHE=ctr(E1)*H*E1
G0f=tonp(G0); G1f=tonp(G1); EHEf=tonp(EHE); Hf=tonp(H)
def Kf(c): 
    G2=c*Hf-EHEf; return np.block([[G0f,G1f/2],[G1f/2,G2]])
lo,hi=1.0,1e7
for _ in range(40):
    mid=math.sqrt(lo*hi); Km=Kf(mid); Km=(Km+Km.conj().T)/2
    if np.linalg.eigvalsh(Km).min()>0: hi=mid
    else: lo=mid
res['c_quad_float']=hi; log('c_quad float',hi)
for fac in (1.05,1.3,2.0,4.0):
    c=hi*fac; G2=H*acb(c)-EHE
    Kb=acb_mat([[ (G0 if bi==0 and bj==0 else (G1*acb(0.5) if bi!=bj else G2))[i,j] for bj in range(2) for j in range(D)] for bi in range(2) for i in range(D)])
    ok,e=psd(Kb,eta*clo*clo*0.5)
    log('K psd c',c,ok,e)
    if ok: res['c_quad']=c; res['quad_err']=e; break
res['quad_statement']='||A(t)/s||_H <= sqrt((1+eta)^2 + c_quad t^2) + L2 t^2/2 for all real t'
res['secs']=round(time.time()-t00,1); save(); log('done')
