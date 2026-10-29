"""Independent check of Lemma V: no nonzero n = a e_0 + b e_d (|a|,|b|<=18, 0<=d<=(m-1)/2) lies in
Lambda = H Z^m + Z 1 (H = 6I - C - C^T, circulant). Membership test: n - c*1 in H Z^m for some c in Z,
c taken mod the order of 1 in Z^m/HZ^m; exact integer linear algebra via sympy-free circulant inversion:
H^{-1} has entries in (1/D)Z, D=det H... we use adj(H) = D * H^{-1} computed exactly with fractions on the
first column (circulant => H^{-1} circulant)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys
from fractions import Fraction as Fr
def first_col_inverse(m):
    # solve H x = e_0 exactly (H circulant symmetric): x_j satisfies 6x_j - x_{j-1} - x_{j+1} = delta_{j0}
    # Gaussian elimination with Fractions (m<=61 is fine)
    M=[[Fr(0)]*m for _ in range(m)]
    for i in range(m):
        M[i][i]+=6; M[i][(i-1)%m]-=1; M[i][(i+1)%m]-=1
    rhs=[Fr(1 if i==0 else 0) for i in range(m)]
    A=[row[:]+[rhs[i]] for i,row in enumerate(M)]
    for c in range(m):
        p=next(r for r in range(c,m) if A[r][c]!=0); A[c],A[p]=A[p],A[c]
        pv=A[c][c]; A[c]=[x/pv for x in A[c]]
        for r in range(m):
            if r!=c and A[r][c]!=0:
                f=A[r][c]; A[r]=[x-f*y for x,y in zip(A[r],A[c])]
    return [A[i][m] for i in range(m)]
def inv_apply(g,n):   # H^{-1} n, g = first column (circulant: (H^-1)_{ij}=g[(i-j)%m])
    m=len(g); return [sum(g[(i-j)%m]*n[j] for j in range(m) if n[j]) for i in range(m)]
def in_lattice(g,n,ones_inv):
    # n in HZ^m+Z1 iff exists c: H^{-1}n - c H^{-1}1 integral; H^{-1}1 = (1/4)1  (row sums of H are 4)
    x=inv_apply(g,n)
    for c in range(4):
        if all((xi-Fr(c,4)).denominator==1 for xi in x): return True
    return False
res={}
for m in range(3,62,2):
    g=first_col_inverse(m); bad=[]
    for d in range(0,(m-1)//2+1):
        for a in range(-18,19):
            for b in range(-18,19):
                n=[0]*m; n[0]+=a; n[d]+=b
                if all(x==0 for x in n): continue
                if in_lattice(g,n,None): bad.append((d,a,b))
    res[m]=bad
    print(f'm={m}: {len(bad)} lattice vectors with |supp|<=2, entries<=18' + (f'  e.g. {bad[:4]}' if bad else ''),flush=True)
# norm inequality 324(2+T_d) < h^2, T_d = lam^d+lam^-d (integer recurrence), h^2 = (T_m-2)/4
T=[2,6]
for i in range(2,200): T.append(6*T[-1]-T[-2])
print('norm inequality 324(2+T_{(m-1)/2}) < (T_m-2)/4 holds for odd m in [3,199]:',
      [m for m in range(3,200,2) if not 324*(2+T[(m-1)//2])<(T[m]-2)//4], '<- failures')
