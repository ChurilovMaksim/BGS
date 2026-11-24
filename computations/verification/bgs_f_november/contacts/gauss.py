"""Check the exact four-sheet metaplectic kernel using coefficients in Q[zeta_8]."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import json
def basis(k):
    k=k%8
    return tuple((1 if k<4 else -1) if i==k%4 else 0 for i in range(4))
tested=0
for n in (1,3,5,7):
    for x in range(8):
        for y in range(8):
            D=3*x*x-2*x*y+3*y*y
            terms=[basis(-2*k*(3*x-y)-3*n*k*k) for k in range(4)]
            lhs=tuple(map(sum,zip(*terms)))
            rhs=tuple(2*v for v in basis(-3*n+n*D))
            assert lhs==rhs
            tested+=1
print(json.dumps(dict(mod8_kernel_identities=tested,cyclotomic_basis=['1','z','z^2','z^3'],relation='z^4=-1'),indent=2))
