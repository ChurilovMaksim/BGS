import sympy as sp
from sympy.matrices.normalforms import smith_normal_decomp
M=sp.Matrix([[6,-1],[1,0]])
for m in [8,12]:
    A=M**m - sp.eye(2)
    print(f"m={m} det={A.det()}")
    S, U, V = smith_normal_decomp(A, domain=sp.ZZ)
    print(f"  SNF diag = {[S[i,i] for i in range(2)]}")
    print(f"  U = {U.tolist()}")
    print(f"  V = {V.tolist()}")
    print(f"  check U*A*V == S: {U*A*V==S}")
    Vi=V.inv()
    print(f"  Vinv = {Vi.tolist()}")
    # Kernel mod 2^A: seed x with A x =0 mod 2^A. Via SNF: U A V = diag(d1,d2), let z=V^{-1} x? Let's define: A x=0 mod q iff diag * (V^{-1} x)?? Since U A V = D => A = U^{-1} D V^{-1}. So A x=0 iff D (V^{-1} x)=0 (U^{-1} unit). So y=V^{-1} x must satisfy d1*y1=0, d2*y2=0 mod q.
    # So x = V y with y1 multiple of q/gcd(d1,q), y2 multiple of q/gcd(d2,q).
