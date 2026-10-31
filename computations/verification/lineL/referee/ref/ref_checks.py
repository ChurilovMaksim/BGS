# Referee [N]/exact sanity checks for Line L: (1) Green's function identity for carries, (2) carry automaton vs brute force,
# (3) Lemma O1 HS bound vs Galerkin truncation of the actual Line F lifted operators (with beta weights).
import sys, math, itertools, numpy as np
sys.path.insert(0,'/workspace/bgs-lineF/code')
from fractions import Fraction
import lift
LAM=lift.LAM; C0=lift.C0
rng=np.random.default_rng(1)
# (1) exact: e_j = -C0g * sum_i v_i lam^{-|j+1-i|}, check in floats with random integer E
mx=0
for _ in range(2000):
    k=int(rng.integers(3,16)); E=[int(x) for x in rng.integers(-9,10,size=k-2)]+[0,0]
    v=[E[j]-6*(E[j-1] if j>=1 else 0)+(E[j-2] if j>=2 else 0) for j in range(k)]
    for j in range(k-2):
        g=-sum(v[i]*LAM**(-abs(j+1-i)) for i in range(k))/(LAM-1/LAM)
        mx=max(mx,abs(g-E[j]))
print('(1) Green identity max err',mx)
# (2) automaton vs brute force for k=6, E0=2 with random positive weights rho_j(d)
k=6;E0=2;DV=8*E0+2
W=[{d:float(rng.random()+0.1) for d in range(-DV,DV+1)} for j in range(k)]
vec={(0,0):1.0}
for j in range(k):
    new={}
    for (a,b),val in vec.items():
        for e in (range(-E0,E0+1) if j<=k-3 else [0]):
            d=e-6*b+a
            if abs(d)>DV: continue
            new[(b,e)]=new.get((b,e),0)+val*W[j][d]
    vec=new
aut=vec[(0,0)]
bf=0
for E in itertools.product(range(-E0,E0+1),repeat=k-2):
    E=list(E)+[0,0]; v=[E[j]-6*(E[j-1] if j>=1 else 0)+(E[j-2] if j>=2 else 0) for j in range(k)]
    # alpha_v = 0 check (exact in Z[sqrt2]):
    a=b=0; pa,pb=1,0
    for j in range(k): a+=v[j]*pa; b+=v[j]*pb; pa,pb=3*pa+4*pb,2*pa+3*pb
    assert a==0 and b==0
    p=1.0
    for j in range(k): p*=W[j][v[j]]
    bf+=p
print('(2) automaton',aut,' brute',bf,' rel',abs(aut-bf)/bf)
# also: every v with alpha_v=0, |v_j|<=3, k=6, arises from some E (completeness)
cnt=0
for v in itertools.product(range(-3,4),repeat=6):
    a=b=0; pa,pb=1,0
    for j in range(6): a+=v[j]*pa; b+=v[j]*pb; pa,pb=3*pa+4*pb,2*pa+3*pb
    if a==0 and b==0:
        cnt+=1
        # recover E by forward recursion and check e_{k-2}=e_{k-1}=0 consistency
        E=[0]*6
        for j in range(6): E[j]=v[j]+6*(E[j-1] if j>=1 else 0)-(E[j-2] if j>=2 else 0)
        assert E[4]==0 and E[5]==0
print('(2b) collisions |v|<=3 k=6:',cnt,' all of form (X^2-6X+1)E')
# (3) Lemma O1 vs Galerkin truncation
from scipy.special import jv
def onebound(word,typ,rho,beta,kap,K0):
    k=len(word); dev=(LAM/(2*(LAM-1))) if typ=='V' else 1/(2*(LAM-1))
    theta=(rho*LAM**(-k)+dev)/rho
    taus=[2*math.pi*kap*rho*LAM**(-j)+beta*LAM**(-(k-j)) for j in range(k)]
    phi=math.prod(abs(jv(n,1.8)) for n in word)
    coth=1/math.tanh(beta*(1-LAM**(-k)))
    return phi*math.prod(math.exp(taus[j]*abs(word[j])) for j in range(k))*(1-theta**2)**-0.5*math.sqrt(coth*math.exp(2*beta*(dev+1)))
worst=0
for typ,rho in (('V',0.75),('V',0.9),('E',0.2)):
  for kap in (C0,C0/2):
    for trial in range(25):
        k=int(rng.integers(1,4)); word=[int(x) for x in rng.integers(-4,5,size=k)]; beta=float(rng.choice([0.25,0.3]))
        K0=12; K=24; a=int(rng.choice([0,2,4,6]))
        mats=[]
        for n0 in word:
            w=lambda n,n0=n0: ((1j)**(n%4)*jv(n,1.8)*np.exp(2j*np.pi*(kap*n*n/2+a*n/8))) if n==n0 else 0
            V,E=lift.ops(w,4,K0,rho if typ=='V' else 1.2,rho if typ=='E' else 0.8,K,beta=beta,coef=kap)
            mats.append(V if typ=='V' else E)
        P=mats[0]
        for M in mats[1:]: P=P@M          # leftmost = outermost = letter j=0
        hs=np.linalg.norm(P)
        bd=onebound(word,typ,rho,beta,kap,K0)
        worst=max(worst,hs/bd)
print('(3) max Galerkin HS / Lemma O1 bound over random words:',worst)
