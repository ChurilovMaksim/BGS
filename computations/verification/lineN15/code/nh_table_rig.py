"""N15 [CA-fp: IEEE standard model + libm <=1 ulp]: step-norm table N_H(d) on [-1/2,1/2], NC cells, SVD-free (rig.norm2_upper).
bound_k = (norm2_upper(fl S(c_k)) + ||fl S - S||_F) / (1 - eta_T) + Lip_H h/2,  S = sum_n C_n e(n c) TM_n, TM_n = fl(T M_n Ti),
||fl S - S||_F <= sum_n |C_n| (e_TM_n + 6.2e-14 ||TM_n||_F) + cgam(61)*sum|C_n|||TM_n||_F,  e_TM_n = rigorous matmul errors of T M_n Ti
(+ the RAD data radius of M_n), phase error of e(n c) <= (|2 pi n c| 3u + 2u) (n<=30): 6.2e-14 covers it with C_n rounding.
eta_T >= ||T Ti - I||_2 rigorous (Frobenius + matmul error).  usage: nh_table_rig.py NC"""
import sys, json, time, math, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N12/code'); sys.path.insert(0,'/workspace/bgs-lineN/N15/code')
import a_ops as A, rig
NC=int(sys.argv[1]); h=1.0/NC
z=np.load('/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45.npz'); T=z['T']; s=complex(z['s']); Ti=np.linalg.inv(T)
P,eP=rig.matmul_err(T,Ti); etaT=rig.fro(P-np.eye(A.D))+eP; assert etaT<0.5
LIP_H=167.21344682844932; C=A.COEF0/s; CA=np.abs(C)*(1+4*rig.u); NS=A.NS.astype(float)
TM=[]; eTM=[]
for Mk in A.MS:
    X1,e1=rig.matmul_err(T,Mk); X2,e2=rig.matmul_err(X1,Ti)
    eTM.append(e2+e1*rig.fro(Ti)+rig.fro(np.abs(T))*A.RAD*A.D*rig.fro(np.abs(Ti))); TM.append(X2)
TM=np.array(TM); nTM=np.array([rig.fro(x) for x in TM])
ferr=float(CA@(np.array(eTM)+6.2e-14*nTM))+rig.cgam(61)*float(CA@nTM)
tab=[]; t0=time.time()
for k in range(NC):
    c=-0.5+(k+0.5)*h
    S=np.tensordot(C*np.exp(2j*np.pi*NS*c),TM,1)
    tab.append((rig.norm2_upper(S)+ferr)/(1-etaT)+LIP_H*h/2*1.0000001)
    if k%256==0: print(k,c,tab[-1],round(time.time()-t0,1),flush=True)
json.dump(dict(NC=NC,h=h,lo=-0.5,etaT=etaT,ferr=ferr,Lip_H=LIP_H,bound=tab,max=max(tab),label='CA-fp (IEEE std model + libm<=1ulp), SVD-free'),
          open(f'/workspace/bgs-lineN/N15/logs/nh_table_rig_{NC}.json','w'))
print('max',max(tab),'etaT',etaT,'ferr',ferr)
