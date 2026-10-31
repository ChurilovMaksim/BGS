"""N15 [CA-fp]: certified step-norm table N_H(d) = ||A(d)/s~||_H on [-1/2,1/2] in NC cells (N12-referee/N13 item 4: table was [N]).
Cell k: centre c_k; bound = (||S(c_k)||_2 (1+1e-12) + formation error) / (1 - ||T Ti - I||) + Lip_H h/2,  S = sum c_n e(n c) T M_n Ti / s~,
formation error <= 2.5e-13 sum_n |c_n/s~| || |T||M_n||Ti| ||_F + 1e-13||S|| (binary64 rounding, generous); Lip_H = 167.2135 [CA] (N13 b_arb).
For |d|<=1/256 use instead the [CA] quadratic bound 1+1.01e-12+4260 d^2 (N13 b2 + referee partition).  usage: nh_table.py NC"""
import sys, json, time, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N12/code'); import a_ops as A
NC=int(sys.argv[1]); h=1.0/NC
z=np.load('/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45.npz'); T=z['T']; s=complex(z['s']); Ti=np.linalg.inv(T)
etaT=np.linalg.norm(T@Ti-np.eye(A.D),2)*1.01; LIP_H=167.21344682844932
C=A.COEF0/s; CA_=np.abs(C); NS=A.NS.astype(float)
TM=np.array([T@Mk@Ti for Mk in A.MS]); aF=np.array([np.linalg.norm(np.abs(T)@np.abs(Mk)@np.abs(Ti)) for Mk in A.MS])
ferr=2.5e-13*float(CA_@aF)
tab=[]; t0=time.time()
for k in range(NC):
    c=-0.5+(k+0.5)*h
    S=np.tensordot(C*np.exp(2j*np.pi*NS*c),TM,1); n=np.linalg.norm(S,2)
    tab.append((n*(1+1e-12)+ferr+1e-13*n)/(1-etaT)+LIP_H*h/2*1.0000001)
    if k%256==0: print(k,c,n,tab[-1],round(time.time()-t0,1),flush=True)
json.dump(dict(NC=NC,h=h,lo=-0.5,etaT=etaT,ferr=ferr,Lip_H=LIP_H,bound=tab,max=max(tab),label='CA-fp'),open(f'/workspace/bgs-lineN/N15/logs/nh_table_{NC}.json','w'))
print('max',max(tab))
