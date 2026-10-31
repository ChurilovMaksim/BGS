import sys, math, numpy as np
sys.path.insert(0,'/workspace/bgs-lineF/code')
import lift
from scipy.special import jv
LAM=lift.LAM; C0=lift.C0; rng=np.random.default_rng(7)
def onebound(word,typ,rho,beta,kap):
    k=len(word); dev=(LAM/(2*(LAM-1))) if typ=='V' else 1/(2*(LAM-1))
    theta=(rho*LAM**(-k)+dev)/rho
    taus=[2*math.pi*kap*rho*LAM**(-j)+beta*LAM**(-(k-j)) for j in range(k)]
    phi=math.prod(abs(jv(n,1.8)) for n in word)
    coth=1/math.tanh(beta*(1-LAM**(-k)))
    return phi*math.prod(math.exp(taus[j]*abs(word[j])) for j in range(k))*(1-theta**2)**-0.5*math.sqrt(coth*math.exp(2*beta*(dev+1)))
for rev in (False,True):
  worst=0
  for typ,rho in (('V',0.75),('V',0.65),('E',0.2),('E',0.12)):
    for kap in (C0,C0/2):
      for trial in range(12):
        k=int(rng.integers(1,6)); word=[int(x) for x in rng.integers(-10,11,size=k)]; beta=0.25
        mats=[]
        for n0 in word:
            w=lambda n,n0=n0: ((1j)**(n%4)*jv(n,1.8)*np.exp(2j*np.pi*(kap*n*n/2))) if n==n0 else 0
            V,E=lift.ops(w,10,14,rho if typ=='V' else 1.2,rho if typ=='E' else 0.8,30,beta=beta,coef=kap)
            mats.append(V if typ=='V' else E)
        P=mats[0]
        for M in mats[1:]: P=P@M
        hs=np.linalg.norm(P); bd=onebound(word[::-1] if rev else word,typ,rho,beta,kap)
        if hs>0: worst=max(worst,hs/bd)
  print('reversed assignment' if rev else 'stated assignment','max ratio',worst,flush=True)
