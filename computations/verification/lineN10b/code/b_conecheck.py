"""N10b [N] (argv[1]=raw or J for averaged-Lyapunov norm W=Q^{1/2}): can a cone field around the rank-one direction be invariant under k-step letters? For random y: u = unit dominant
direction at y (J-step push-forward), u' at T^k y; for M=P_k(y): alpha0=<u',M u>, s1=|u'^* M Pperp|, s2=|Pperp' M Pperp|, b0=|Pperp' M u|.
Invariance of K(a)={|x_perp|<=a|<u,x>|} needs |alpha0|>s2 and (|alpha0|-s2)^2>=4 s1 b0. Raw Euclidean norm of the Line-F lift."""
import sys, numpy as np
sys.path.insert(0,'/workspace/bgs-lineF/code')
from lift import ops, wk1
K0,r,K,beta,N0=3,1.2,20,2.5,10
Bn={}
for n in range(-N0,N0+1):
    V,E=ops(lambda m,n=n: 1.0 if m==n else 0.0, N0,K0,r,r,K,beta=beta); Bn[n]=V
ns=np.array(sorted(Bn)); Bst=np.stack([Bn[n] for n in ns]); w0=wk1(2.0,4); w=np.array([w0(int(n)) for n in ns])
L=lambda t: np.tensordot(w*np.exp(2j*np.pi*ns*t),Bst,axes=(0,0))
T=lambda y: np.array([y[1],(6*y[1]-y[0])%1]); Ti=lambda y: np.array([(6*y[0]-y[1])%1,y[0]])
def udir(y,J=10):
    h=[y]
    for i in range(J): h.append(Ti(h[-1]))
    v=np.ones(140,complex)
    for i in range(J,0,-1): v=L(h[i][0])@v; v/=np.linalg.norm(v)
    return v
rng=np.random.default_rng(0)
import sys as _s
NORM=_s.argv[1] if len(_s.argv)>1 else 'raw'
if NORM!='raw':
    rho_,J_=1.3,int(NORM)
    Y=rng.random((600,2)); Q=np.zeros((140,140),complex)
    for y in Y:
        P=np.eye(140,dtype=complex); z=y.copy()
        for j in range(J_+1):
            Q+=rho_**(-2*j)*(P.conj().T@P)/len(Y); P=L(z[0])@P; z=T(z)
    ev,U=np.linalg.eigh(Q); W=(U*np.sqrt(ev))@U.conj().T; Wi=(U/np.sqrt(ev))@U.conj().T
    L0=L; L=lambda t: W@L0(t)@Wi
for k in (1,2,4,6,8):
    ok=0; rat=[]
    for t in range(40):
        y=rng.random(2); u=udir(y); M=np.eye(140,dtype=complex); z=y.copy()
        for i in range(k): M=L(z[0])@M; z=T(z)
        u2=udir(z); Pp=np.eye(140)-np.outer(u,u.conj()); Pp2=np.eye(140)-np.outer(u2,u2.conj())
        a0=abs(u2.conj()@M@u); s1=np.linalg.norm(u2.conj()@M@Pp); s2=np.linalg.norm(Pp2@M@Pp,2); b0=np.linalg.norm(Pp2@M@u)
        good=(a0>s2) and ((a0-s2)**2>=4*s1*b0); ok+=good; rat.append(s2/a0)
    print('k',k,'cone-invariance feasible in',ok,'/40; median s2/|alpha0| = %.3g'%np.median(rat),flush=True)
