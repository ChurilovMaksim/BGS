import sympy as sp
from sympy.matrices.normalforms import smith_normal_decomp
M=sp.Matrix([[6,-1],[1,0]])
for m in range(4,25):
    A=M**m - sp.eye(2)
    S, U, V = smith_normal_decomp(A, domain=sp.ZZ)
    d1,d2=int(S[0,0]),int(S[1,1])
    import math
    print(f"m={m} d1={d1} d2={d2} d1*d2={d1*d2} |det|={abs(int(A.det()))} V={V.tolist()} v2d1={d1.bit_length()-1 if d1 else 0} gcd_entries={math.gcd(math.gcd(abs(int(A[0,0])),abs(int(A[0,1]))),math.gcd(abs(int(A[1,0])),abs(int(A[1,1]))))}")
