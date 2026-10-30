"""Exact (Fraction) aliasing of the fixed diagonal symbol on small torsion subgroups (1/n)Z/Z:
f(a/n) = sum_r C_r e(ra/n), C_r = sum_{k = r mod n} c_k.  Explains the exact non-dihedral coincidences found at m=6."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys; sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','common'))
from audit46_core import cEx
from fractions import Fraction as F
c={k:cEx(k,0) for k in range(-9,10) if cEx(k,0)!=(0,0)}
print('exact l=0 coefficients c_k=(Re,Im):',{k:(str(v[0]),str(v[1])) for k,v in sorted(c.items())})
for n in [2,3,4,5,6,7,8,14,28]:
    C={}
    for k,(re,im) in c.items():
        r=k%n; a,b=C.get(r,(F(0),F(0))); C[r]=(a+re,b+im)
    nz={r:(str(v[0]),str(v[1])) for r,v in C.items() if v!=(0,0)}
    print(f'n={n}: nonzero aliased coefficients C_r = {nz}')
