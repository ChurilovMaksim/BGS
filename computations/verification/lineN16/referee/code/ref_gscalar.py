"""lineN16 referee: independent re-implementation of the N16 scalar carry sum, tracking the NONZERO-carry part separately
(no cancellation: C_n = sum over carry paths with some e_t != 0, start/end state (0,0)), so C_n/S_n^(0) is computed directly.
Operator data: N12 a_ops (M_n, COEF0) and the N12 adapted-norm npz (s, Phi, psi) -- the refereed inputs; own blocks, own DP.
Recurrence: v_t = e_t - 6 e_{t-1} + e_{t-2};  pair-letter transfer T_v(Y) = sum_{n1-n2=v} (c_{n1}/s) M_{n1} Y (c_{n2}/s)^* M_{n2}^*."""
import sys, json, time, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N12/code'); import a_ops as A
z=np.load('/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45.npz'); s=complex(z['s']); Phi=z['Phi'].astype(complex); psi=z['psi'].astype(complex)
E=int(sys.argv[1]); NM=int(sys.argv[2]); D=A.D; K=55; NB=D//K; NS=[int(x) for x in A.NS]
L={}
for k,n in enumerate(NS):
    M=A.MS[k]*(A.COEF0[k]/s); bl=[]
    for ib in range(NB):
        for jb in range(NB):
            B=M[ib*K:(ib+1)*K,jb*K:(jb+1)*K]
            if np.abs(B).max()>0: bl.append((ib,jb,B))
    L[n]=bl
def left(n,Y):
    T=np.zeros((D,D),complex)
    for ib,jb,B in L[n]: T[ib*K:(ib+1)*K,:]+=B@Y[jb*K:(jb+1)*K,:]
    return T
def right(n,T):
    Z=np.zeros((D,D),complex)
    for ib,jb,B in L[n]: Z[:,ib*K:(ib+1)*K]+=T[:,jb*K:(jb+1)*K]@B.conj().T
    return Z
def Tv(v,Y):
    Z=np.zeros((D,D),complex)
    for n1 in NS:
        if n1-v in L: Z+=right(n1-v,left(n1,Y))
    return Z
Y0=np.outer(Phi,Phi.conj())
Z={(0,0):Y0}; N={}      # Z: all-zero history; N: paths with some nonzero carry, keyed by state (e_{t-1},e_{t-2})
res=[]; t0=time.time()
for n in range(1,NM+1):
    nZ={}; nN={}
    for (a,b),Y in list(Z.items())+[(k,None) for k in []]:
        for e in range(-E,E+1):
            v=e-6*a+b
            if abs(v)>60: continue
            W=Tv(v,Y)
            if e==0 and a==0 and b==0: nZ[(0,0)]=nZ.get((0,0),0)+W
            else: nN[(e,a)]=nN.get((e,a),0)+W
    for (a,b),Y in N.items():
        for e in range(-E,E+1):
            v=e-6*a+b
            if abs(v)>60: continue
            nN[(e,a)]=nN.get((e,a),0)+Tv(v,Y)
    Z,N=nZ,nN
    S0=float(np.real(psi@Z[(0,0)]@psi.conj()))
    C=complex(psi@N[(0,0)]@psi.conj()) if (0,0) in N else 0j
    res.append(dict(n=n,S0=S0,C=C.real,Cim=C.imag,rel=C.real/S0)); print(res[-1],round(time.time()-t0,1),flush=True)
json.dump(dict(E=E,rows=res),open(f'/workspace/audit/lineN16/logs/ref_gscalar_E{E}_n{NM}.json','w'),indent=1)
