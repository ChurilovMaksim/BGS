from mpmath import mp, mpf, sqrt
mp.dps=40
def green(r1,r2,c):  # operator e -> c[0] e_k + c[1] e_{k-1} + c[2] e_{k-2}; char poly c0 + c1 z + c2 z^2 with roots |r1|>1>|r2| in z (z=shift)
    pass
# eps: u_k = -e_k -2 e_{k-1} + e_{k-2}. Try ansatz g_k = A*x^k for k>=0, B*y^k for k<0 with x,y roots of -1 -2/z... solve numerically by least squares on a window
import numpy as np
def solve(c,L=80):
    # unknown g_{-L..L}; equations sum_d c_d g_{k-d} = delta_k for k=-L+2..L ; add decay by solving bi-infinite via roots
    # characteristic: c0 + c1 w^{-1} + c2 w^{-2}=0 for g_k ~ w^k  -> c0 w^2 + c1 w + c2 = 0
    w=np.roots([c[0],c[1],c[2]]); ws=sorted(w,key=abs)  # |ws[0]|<1 for k>=0 side, |ws[1]|>1 for k<0 side
    a,b=ws[0],ws[1]
    # g_k = A a^k (k>=0), g_k = B b^k (k<0); conditions: equations at k=0 and k=1
    # k=1: c0 g1 + c1 g0 + c2 g_{-1} = 0 ; k=0: c0 g0 + c1 g_{-1} + c2 g_{-2} = 1
    M=np.array([[c0*a+c1, c2/b] for c0,c1,c2 in [c]]+[[c[0], c[1]/b + c[2]/b**2]])
    A,B=np.linalg.solve(M,[0,1])
    g={k:(A*a**k if k>=0 else B*b**k) for k in range(-L,L+1)}
    res=max(abs(sum(cd*g.get(k-d,0) for d,cd in enumerate(c))-(1 if k==0 else 0)) for k in range(-L+3,L-3))
    return sum(abs(v) for v in g.values()), res, A, B
print('eps', solve((-1,-2,1)), (2+2**.5)/4)
print('lam', solve((1,-6,1)))
