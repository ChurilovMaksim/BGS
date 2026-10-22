"""Independent finite controls for the physical weight audit.
These exact computations support identities and constant margins, not the
all-length proof, smooth foliation proof, EQ, or a quantum trace theorem.
"""
import json
from fractions import Fraction as Q
import sympy as s

def run():
    a,b,c,z=s.symbols('a b c z', nonzero=True)
    M=s.Matrix([[a/b,1/b],[(a*c-b*b)/b,c/b]])
    assert s.simplify(M.det()-1)==0
    assert s.simplify((a+c-b*(z+1/z))+(b/z)*(M-z*s.eye(2)).det())==0
    cases=[]
    for m in range(2,10):
        for seed in range(5):
            # Algebraic arrays deliberately include negative entries and b signs.
            aa=[s.Rational((-1)**(j+seed)*(11+2*j+seed),13) for j in range(m)]
            cc=[s.Rational((-1)**j*(17+j+3*seed),19) for j in range(m)]
            bb=[s.Rational((-1)**(j+1)*(3+j+seed),23) for j in range(m)]
            K=s.zeros(m); M=s.eye(2); prod=s.Integer(1)
            for j in range(m):
                k=(j+1)%m
                K[j,j]+=aa[j];K[k,k]+=cc[j]
                if j==m-1:
                    K[j,k]-=bb[j]*z;K[k,j]-=bb[j]/z
                else:
                    K[j,k]-=bb[j];K[k,j]-=bb[j]
                M=s.Matrix([[aa[j]/bb[j],1/bb[j]],[(aa[j]*cc[j]-bb[j]**2)/bb[j],cc[j]/bb[j]]])*M
                prod*=bb[j]
            diff=s.factor(K.det()+prod*(M-z*s.eye(2)).det()/z)
            assert diff==0,(m,seed,diff)
            cases.append({'m':m,'seed':seed,'identity':'det K(z)=-(product b)/z det(M-zI)'})
    delta=Q(1,10**50)
    margins={
        'holder_square': Q(3,100)**2*6**3 < Q(441,1000)**2,
        'graph_contraction': Q(441,1000)+10**12*delta < Q(1,2),
        'ball_invariance': 10**6*delta+Q(1,2)*10**8*delta<10**8*delta,
        'phase_derivative': 1-10**25*delta>Q(1,2),
        'physical_leaf_small': 10**22*delta<Q(1,100),
    }
    assert all(margins.values())
    return {'arithmetic':'symbolic and rational, no floating evaluation at tau',
            'symbolic_m1':True,'twisted_hill_cases':cases,'constant_margins':margins,
            'nonclaims':['EQ','bundle regularity proved mechanically','finite-h factor harmlessness','TRACE-005','BGS']}
if __name__=='__main__':
    print(json.dumps(run(),indent=2))
