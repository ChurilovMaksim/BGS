"""Referee: Galerkin-level check of the sym/ intertwiners.  target = U f(src) U^-1, f = id (linear) or conj (antilinear),
U e_(c,pos,i,k) = e(-c_pos/8) e_(c,pi(pos),i,k)."""
import numpy as np, json
W=json.load(open('code/monomial_intertw.json'))
def load(p,j):
    info=json.load(open(p+'.json')); return np.load(f'{p}_b{j}_mid.npy'), info
def Umat(info,wit):
    NS=info['NS']; K0=info['K0']; Rc=K0
    cores=[c2 for c2 in range(-2*K0-2,2*K0+3) if c2%2==0 and abs(c2/2)<=Rc]
    Kc={c2:(info['K2'] if abs(c2/2)>Rc-1 else info['K']) for c2 in cores}
    D=sum(NS*Kc[c] for c in cores); U=np.zeros((D,D),complex); off=0
    for c2 in cores:
        Ko=Kc[c2]
        for pos in range(16):
            for i in range(3):
                for k in range(Ko):
                    U[off+(wit['pi'][pos]*3+i)*Ko+k, off+(pos*3+i)*Ko+k]=np.exp(-2j*np.pi*wit['c'][pos]/8)
        off+=NS*Ko
    assert off==D; return U
src,info=load('data/sm_src92',0)   # (9,2) beta=6:4 = -(1:3)
src13,_=load('data/sm_src92',1)    # (9,2) beta=1:3
for name,tp,tj,s,mode,key in [('(15,-2) b=1:3 <- J (9,2) b=-(1:3)','data/sm_t15m',0,src,'conj','15,-2'),
                               ('(21,2) b=1:3 <- U (9,2) b=1:3','data/sm_t21p',0,src13,'lin','21,2'),
                               ('(27,-2) b=1:3 <- J (9,2) b=-(1:3)','data/sm_t27m',0,src,'conj','27,-2'),
                               ('(27,-2) b=-(1:3) <- J (9,2) b=1:3','data/sm_t27m',1,src13,'conj','27,-2'),
                               ('NEG CONTROL (15,-2) b=1:3 <- U (9,2) b=-(1:3) linear','data/sm_t15m',0,src,'lin','15,-2')]:
    T,inf=load(tp,tj); U=Umat(inf,W[key][mode]); S=s.conj() if mode=='conj' else s
    d=np.abs(T-U@S@U.conj().T).max(); print(f'{name}: max|T - U f(S) U^-1| = {d:.2e}  (max|T| = {np.abs(T).max():.3f})')
