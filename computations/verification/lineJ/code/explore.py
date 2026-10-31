"""Float exploration: left/right top eigenvectors of a certG_build Galerkin matrix, T = l^* J r / l^* r. Usage: explore.py prefix"""
import sys, json, numpy as np, scipy.sparse.linalg as ssl
pre=sys.argv[1]; info=json.load(open(pre+'.json'))
A=np.load(pre+'_b0_mid.npy'); D=A.shape[0]; NS=info['NS']; K=info['K']; K2=info['K2']; K0=info['K0']
Rc=K0
cores=[c2 for c2 in range(-2*K0-2,2*K0+3) if c2%2==0 and abs(c2/2)<=Rc]
Kc={c2:(K2 if abs(c2/2)>Rc-1 else K) for c2 in cores}
off={};o=0
for c2 in cores: off[c2]=o; o+=NS*Kc[c2]
assert o==D
def Jop(x):
    y=np.zeros_like(x)
    for c2 in cores:
        Ko=Kc[c2]; blk=x[off[c2]:off[c2]+NS*Ko].reshape(NS,Ko)
        y[off[c2]:off[c2]+Ko]=blk[0::3].sum(0)   # state 0 row = sum over e%3==0
    return y
ev,vr=ssl.eigs(A,k=8,which='LM',tol=1e-13)
o=np.argsort(-abs(ev)); ev=ev[o]; vr=vr[:,o]
print('eigs',ev, abs(ev))
lv,vl=ssl.eigs(A.conj().T,k=8,which='LM',tol=1e-13)
for i in range(3):
    mu=ev[i]; r=vr[:,i]; j=np.argmin(abs(lv.conj()-mu)); l=vl[:,j]
    den=np.vdot(l,r); T=np.vdot(l,Jop(r))/den
    kap=np.linalg.norm(l)*np.linalg.norm(r)/abs(den)
    print(i,'mu',mu,'|mu|',abs(mu),'T',T,'|T|',abs(T),'3T',3*T,'kappa',kap, 'res', np.linalg.norm(A@r-mu*r))
    # mass on outer discs
    for c2 in cores:
        Ko=Kc[c2]; print('   disc',c2/2,'|r|',np.linalg.norm(r[off[c2]:off[c2]+NS*Ko])/np.linalg.norm(r),'|l|',np.linalg.norm(l[off[c2]:off[c2]+NS*Ko])/np.linalg.norm(l))
np.savez(sys.argv[2],ev=ev,vr=vr[:,:3],lv=lv,vl=vl)
