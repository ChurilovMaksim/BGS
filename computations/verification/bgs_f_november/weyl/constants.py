"""Rational checks for estimates in the Weyl-label argument."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from fractions import Fraction as F
from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"research"))
from coefficients import raw_symbol
c=raw_symbol()
mass=sum(abs(x)+abs(y) for x,y in c.values())*F(1,4000)
assert mass<F(6,5)
assert all(abs(a)+F(1415,1000)*abs(b)<14 for a,b in c)
assert 2*F(22,7)*10*mass<80
# e^28 < 3^28; conservative substitute in the negative-binomial estimate.
assert 14*80*F(3**28,10**80)<F(1,2)
# A tighter rational upper bound e < 11/4 (from its Taylor series).
assert 160*F(11,4)**28/F(10**80)<F(1,10**64)
assert 1-F(1,1)/F(58,10) - 6*F(1,10**64)>F(8,10)
# Hyperbolic shell transition and error exponents.
assert 1/F(58,10)+F(1,10)<F(1,2)
assert F(58,10)-F(1,10)>5
assert 2-F(19,100)*100==-17
assert 200-F(8,10)*(400-8)<-110
assert F(6,401)>F(1,70)
# The two linearized conjugacy modes. c is indexed by (a,b), physically (b,a).
def norm2(d):
    x,y=c[d]
    return F(x*x+y*y,4000**2)
gq=norm2((0,1));gp=norm2((1,0))
assert gq/2>F(1,1000)**2 and gp/4>F(1,1000)**2
assert F(10**8,10**80)<F(1,1000)
print(json.dumps(dict(raw_symbol_mass=str(mass),q_mode_modulus_squared=str(gq),
    p_mode_modulus_squared=str(gp),column_exponent="4/5",
    shell_error_power=-17,block_length="ceil(400 log N)",block_norm_upper="N^-12",
    long_time_exponent="1/70"),indent=2))
