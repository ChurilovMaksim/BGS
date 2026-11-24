"""Exact two-frequency obstruction to a vertical time-reversing involution."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from fractions import Fraction as F
from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'research'))
from coefficients import raw_symbol

def mul(z,w):
    x,y=z; a,b=w
    return (x*a-y*b,x*b+y*a)
symbols={(b,a):tuple(F((-1)**((a*b)%2)*i,4000) for i in z)
         for (a,b),z in raw_symbol().items()}
g1=symbols[1,0];g2=symbols[0,1]
z=mul((0,F(-1,2)),g2)
assert z==(F(-4,2000),F(3,2000))
size=sum(x*x for x in z)
rho=tuple(x/size for x in mul((z[0],-z[1]),(z[0],-z[1])))
fourth=mul(mul(rho,rho),mul(rho,rho))
defect=(fourth[0]-1)**2+fourth[1]**2
assert rho==(F(7,25),F(24,25)) and defect>1
assert sum(x*x for x in g1)/72>F(1,200)**2
def data(z):return [str(i) for i in z]
print(json.dumps(dict(g1=data(g1),g2=data(g2),vertical_mode=data(z),
                      phase_constraint=data(rho),fourth_power=data(fourth),
                      squared_obstruction=str(defect)),indent=2))
