# Literal-kernel floating brute force: E|Tr U^m|^2 = sum_{multisets} |sum_{x in arrangements} K(x)|^2, U = D_theta M_N,
# M_N(x,y) = N^{-1/2} e_N(-8^{-1}(3x^2-2xy+3y^2)) (repository kernel). Works for composite odd N.
import itertools, numpy as np, sys
from collections import defaultdict
def run(N,m):
    inv8 = pow(8,-1,N)
    M = np.array([[np.exp(2j*np.pi*((-inv8*(3*x*x-2*x*y+3*y*y))%N)/N) for y in range(N)] for x in range(N)])/np.sqrt(N)
    groups=defaultdict(complex)
    for x in itertools.product(range(N),repeat=m):
        K=1
        for j in range(m): K*=M[x[j],x[(j+1)%m]]
        groups[tuple(sorted(x))]+=K
    return sum(abs(v)**2 for v in groups.values())
if __name__=="__main__":
    for N,m in [(7,3),(7,4),(5,4),(11,3),(9,3),(9,4),(15,3),(7,5),(13,4),(13,5)]:
        print(N,m,repr(run(N,m)))
