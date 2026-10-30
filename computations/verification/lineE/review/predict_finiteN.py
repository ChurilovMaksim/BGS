"""Transfer-operator prediction of |Tr U_N^m|^2 at N = h_m - 4 (k1 kick): c -> c(1+4/N), Z=(1-lam^-m) sum_a c_a sum mu^m.
Referee fixes F7/F8: vendored (no external imports), and run with Galerkin parameters satisfying the
H^2(D_rho) invariance hypothesis rho > L/(lam-1) of E2 (default L=10, rho=2.6 > 10/4.83 = 2.07).
Usage: predict_finiteN.py m [eta=2.0] [L=10] [rho=2.6] [K=90]"""
import os, sys, numpy as np, cmath
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'code'))
import ifs_explore as I
def hm(m):
    a,b=1,7
    for _ in range((m-3)//2): a,b=b,6*b-a
    return b
m=int(sys.argv[1]); eta=float(sys.argv[2]) if len(sys.argv)>2 else 2.0; L=int(sys.argv[3]) if len(sys.argv)>3 else 10
rho=float(sys.argv[4]) if len(sys.argv)>4 else 2.6; K=int(sys.argv[5]) if len(sys.argv)>5 else 90
assert rho > L/(I.lam-1), 'Galerkin space not invariant: need rho > L/(lam-1)'
h=hm(m); N=h-4
kap={5:7,7:5,1:3,3:1}[m%8]
c0=1/(I.lam-1/I.lam); I.c=c0*(1+4/N)
Z=0
for a in range(0,8,2):
    ca=sum(cmath.exp(2j*cmath.pi*(kap*b*b-a*b)/8) for b in range(8))/8
    ev=np.linalg.eigvals(I.build(a,eta,L,rho,K)); Z+=ca*np.sum(ev**m)
Z*=(1-I.lam**(-m)); print(m,N,abs(Z)**2)
