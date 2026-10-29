# Prop. 2 evaluated by direct z-sums (any odd N, incl. composite) vs literal-kernel brute force.
import itertools, numpy as np, sys
sys.path.insert(0,'/workspace/audit/lineC/code')
from sym import wseries, setpartitions
from literal_float import run
def prop2(N,m):
    c=pow(4,-1,N); w=wseries(m); tot=0
    for rho in setpartitions(m,m):
        n=max(rho)+1; W=1.0
        for b in range(n): W*=float(w[rho.count(b)])
        Z=np.array(list(itertools.product(range(N),repeat=n)))
        Px=sum(Z[:,rho[j]]*Z[:,rho[(j+1)%m]] for j in range(m))
        for s in itertools.permutations(range(m)):
            y=[rho[s[j]] for j in range(m)]
            Py=sum(Z[:,y[j]]*Z[:,y[(j+1)%m]] for j in range(m))
            tot+=W*np.exp(2j*np.pi*((c*(Px-Py))%N)/N).sum()
    return tot/N**m
for N,m in [(9,3),(15,3),(9,4),(15,4),(21,3),(7,5)]:
    a=prop2(N,m); b=run(N,m); print(N,m,a.real,abs(a.imag),b,abs(a-b))
