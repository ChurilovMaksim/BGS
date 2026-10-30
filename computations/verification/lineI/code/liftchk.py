"""Float check: lifted (vertex/edge lattice) twisted cyclic operators reproduce Zhat(beta) (zpred, single-disc K=40) at m=9,15.
Usage: liftchk.py K0 r K Lk"""
import sys, numpy as np, math
sys.path.insert(0,'/workspace/bgs-lineF/code')
from lift import blockmat, rnd
from law import kick_ghat, LAM, C0
from gstates import g2params, reach, taus7, finite
K0=int(sys.argv[1]); r=float(sys.argv[2]); K=int(sys.argv[3]); Lk=int(sys.argv[4])
gh=kick_ghat('k1',2.0,Lk)
def ops(m,a,b,beta):
    P=g2params(m,a,b); idx,tg=reach(P,Lk); cyc=None if beta is None else taus7(*beta)
    NS=len(idx)*(1 if cyc is None else 3); coef=-4*a*C0/b
    F={}
    for n in gh:
        A=np.zeros((NS,NS),complex)
        for (o,i,ph8,tw) in finite(P,idx,tg,n,cyc): A[o,i]+=np.exp(-2j*np.pi*ph8/8)*np.exp(2j*np.pi*n*tw/7)
        F[n]=A
    nv=2*K0+1; ne=2*K0; B=K*NS
    V=np.zeros((nv*B,)*2,complex); E=np.zeros((ne*B,)*2,complex)
    for n,gn in gh.items():
        w=gn*np.exp(2j*np.pi*coef*n*n/2)
        for kk in range(-K0,K0+1):
            j=rnd((kk+n)/LAM)
            if abs(j)>K0: continue
            V[(kk+K0)*B:(kk+K0+1)*B,(j+K0)*B:(j+K0+1)*B]+=w*np.kron(blockmat(n,kk,j,r,r,coef,K),F[n])
        for e in range(-K0,K0):
            j=rnd((e+n)/LAM); j2=rnd((e+1+n)/LAM)
            if j2!=j+1 or j<-K0 or j>K0-1: continue
            E[(e+K0)*B:(e+K0+1)*B,(j+K0)*B:(j+K0+1)*B]+=w*np.kron(blockmat(n,e+.5,j+.5,r,r,coef,K),F[n])
    return V,E,NS,idx,cyc
def ptrace(Mat,m,nd,NS,cyc):
    # Tr[(I x |e_(0,0)><1_{i=0}|) Mat^m]: sum over discs, poly k, end states with i=0 of <(c,end,k)| Mat^m |(c,start,k)>
    X=np.linalg.matrix_power(Mat,m).reshape(nd,K,NS,nd,K,NS)
    ends=[s for s in range(NS) if (cyc is None or s%3==0)]
    return sum(np.einsum('ckck->',X[:,:,e,:,:,0]) for e in ends)
for m in [int(x) for x in sys.argv[5].split(',')]:
    Zh=np.load(f'../data/zpred_d7_2_8_m{m}_K40.npy')
    for beta in (None,(1,0),(0,1),(1,2),(2,1)):
        V,E,NS,idx,cyc=ops(m,2,8,beta)
        tv=ptrace(V,m,2*K0+1,NS,cyc); te=ptrace(E,m,2*K0,NS,cyc)
        ref=Zh[0,0] if beta is None else Zh[beta]
        for name,c in (('1',1.0),('(1-l^-m)',1-LAM**-m),('(1-l^-m)^2',(1-LAM**-m)**2)):
            pass
        val=tv-te
        print(m,beta,'NS',NS,'dimV',V.shape[0],'lift',val,'ref',ref,'ratio',ref/val,'(1-l^-m)',1-LAM**-m,flush=True)
