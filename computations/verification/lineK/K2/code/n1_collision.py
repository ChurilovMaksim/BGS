"""N1 [N]: exact cat-map second moment I_k = int_{T^2} ||P_k(y)||_HS^2 dy for the toy Galerkin twisted family (b=8, as J3 lyap.py),
P_k(y) = L_{tau_{k-1}} ... L_{tau_0},  tau_j = Tr(y lam^j) + theta,  L_tau = sum_n e(n tau) M_n.
||P||_HS^2 = sum_{w,w'} e(sum_j (n_j-n'_j) tau_j) Tr(M_w M_w'^*); integrating over y keeps exactly the pairs with sum_j d_j lam^j = 0, d = n-n',
i.e. D(X) = (X^2-6X+1) E(X), e_j = d_j + 6 e_{j-1} - e_{j-2}, E ends at 0.  Carry automaton with states (e_{j-1}, e_j) (|e|<=EMAX) and parity of
sum e (theta=a/8 contributes e(theta sum d) = e(-4 theta E(1)): sectors a=0,4 -> +, a=2,6 -> (-1)^{E(1)}).
Output: I_k for both sector types, and the rate I_k^{1/(2k)} (to compare with the d=7 survivor 1.2836) and ratios I_{k+1}/I_k."""
import sys, numpy as np, json, os, time
os.environ.setdefault('OMP_NUM_THREADS','2')
sys.path.insert(0,'/workspace/bgs-lineI/code')
from law import kick_ghat, MC, LAM
K=int(sys.argv[1]) if len(sys.argv)>1 else 40; EMAX=int(sys.argv[2]) if len(sys.argv)>2 else 6
NMAX=int(sys.argv[3]) if len(sys.argv)>3 else 7; KSTEPS=int(sys.argv[4]) if len(sys.argv)>4 else 80
BB=int(sys.argv[5]) if len(sys.argv)>5 else 8
SCALE=float(sys.argv[6]) if len(sys.argv)>6 else 1.0   # control: non-unitary scaling of ghat
gh=kick_ghat('k1',2.0,10); RHO=2.6; c0=1/(LAM-1/LAM); C=-4*2*c0/BB
ns=[n for n,g in gh.items() if abs(g)>0 and abs(n)<=NMAX]
M={n:SCALE*gh[n]*np.exp(2j*np.pi*C*n*n/2)*MC(n,C,RHO,K) for n in ns}
Mh={n:M[n].conj().T for n in ns}
dvals=sorted(set(a-b for a in ns for b in ns))
# state: dict (a,b,par) -> KxK matrix X = sum M_w M_w'^*
st={(0,0,0):np.eye(K,dtype=complex)}; logscale=0.0; out=[]; prev=None
t0=time.time()
for k in range(1,KSTEPS+1):
    new={}
    for (a,b,par),X in st.items():
        Y={n:M[n]@X for n in ns}
        for d in dvals:
            e=d+6*b-a
            if abs(e)>EMAX: continue
            Z=sum(Y[n]@Mh[n-d] for n in ns if (n-d) in M)
            key=(b,e,(par+e)%2)
            new[key]=new.get(key,0)+Z
    st=new
    nrm=max(np.abs(X).max() for X in st.values()); logscale+=np.log(nrm)
    for kk in st: st[kk]/=nrm
    Ie=np.trace(st.get((0,0,0),np.zeros((K,K)))).real; Io=np.trace(st.get((0,0,1),np.zeros((K,K)))).real
    Iplus=Ie+Io; Imin=Ie-Io       # sector a=0,4 and a=2,6
    lp=np.log(abs(Iplus))+logscale if Iplus!=0 else -np.inf; lm=np.log(abs(Imin))+logscale if Imin!=0 else -np.inf
    r=dict(k=k,log_I_a04=float(lp),log_I_a26=float(lm),rate_a04=float(np.exp(lp/(2*k))),rate_a26=float(np.exp(lm/(2*k))),
           ratio_a04=(float(np.exp((lp-prev[0])/2)) if prev else None),nstates=len(st),sec=round(time.time()-t0,1))
    prev=(lp,lm); out.append(r); print(json.dumps(r),flush=True)
    json.dump(dict(b=BB,K=K,EMAX=EMAX,NMAX=NMAX,rows=out),open((f'logs/n1_collision_b{BB}_K{K}_E{EMAX}_N{NMAX}.json' if SCALE==1.0 else f'logs/n1_collision_b{BB}_K{K}_E{EMAX}_N{NMAX}_s{SCALE}.json'),'w'))
