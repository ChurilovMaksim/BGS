"""Compute all four localized data for the one-step trace in exact arithmetic."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys
from pathlib import Path
from fractions import Fraction as F
import json
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'research'))
from coefficients import raw_symbol
symbol=raw_symbol()
fixed=[]
for q in (0,1):
    for p in (0,1):
        def derivative(a_power,b_power):
            return tuple(sum(F((-1)**((a*b+b*q+a*p)%2)*a**a_power*b**b_power*z[i],4000)
                             for (a,b),z in symbol.items()) for i in (0,1))
        g=derivative(0,0);assert g[1]==0
        assert derivative(1,0)==derivative(0,1)==(0,0)
        assert derivative(2,0)==derivative(1,1)==(0,0)
        x,y=derivative(0,2);assert y==0
        h=-4*x
        chars=[]
        for nmod in (1,3):
            pairs=[(1,0),(0,1),(-1,0),(0,-1)]
            v=[0,0]
            for a in (0,1):
                for b in (0,1):
                    re,im=pairs[(nmod*a*a)%4]
                    sign=(-1)**((a*b+b+b*q+a*p)%2)
                    v[0]+=sign*re;v[1]+=sign*im
            chars.append([str(F(i,4)) for i in v])
        fixed.append(dict(q_twice=q,p_twice=p,value=str(g[0]),hessian=str(h),weights=chars))
assert [F(k['hessian']) for k in fixed]==list(map(F,['-19606/125','-19594/125','24306/125','24894/125']))
assert [F(k['value']) for k in fixed]==[F(9,10)]*2+[F(-11,10)]*2
print(json.dumps(fixed,indent=1))
