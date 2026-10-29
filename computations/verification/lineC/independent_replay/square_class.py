# Does the form factor depend on the square class of the cross-term coefficient beta (kernel e_p(beta x y))?
import itertools, numpy as np
from collections import defaultdict
def E(N,m,beta):
    X,Y=np.meshgrid(range(N),range(N),indexing='ij'); M=np.exp(2j*np.pi*((beta*X*Y)%N)/N)/np.sqrt(N)
    g=defaultdict(complex)
    for x in itertools.product(range(N),repeat=m):
        K=1
        for j in range(m): K*=M[x[j],x[(j+1)%m]]
        g[tuple(sorted(x))]+=K
    return sum(abs(v)**2 for v in g.values())
for N,m,nu in [(13,4,2),(5,4,2),(13,5,2),(7,4,3),(11,5,2)]:
    a=E(N,m,1); b=E(N,m,nu)
    print(f"p={N} (mod 4 = {N%4}) m={m}: beta=1 -> {a:.12f}; beta={nu} (nonsquare) -> {b:.12f}; diff={a-b:.3e}")
print("p=13,m=4 exact: 14033/2197 +/- 8*sqrt(13)/2197 =", 14033/2197+8*13**.5/2197, 14033/2197-8*13**.5/2197)
