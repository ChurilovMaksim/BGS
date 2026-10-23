
# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import sympy as s
q,p=s.symbols('q p',real=True)
r=(1-s.cos(14*s.pi*q))*(1+s.cos(2*s.pi*q))
f=s.cos(14*s.pi*q)+r/10+r*s.sin(2*s.pi*q)/100+r*(-3*s.cos(2*s.pi*p)+4*s.sin(2*s.pi*p))/500
H=s.hessian(f,(q,p)); grad=s.Matrix([s.diff(f,x) for x in (q,p)])
for x in [(0,0),(0,s.Rational(1,2)),(s.Rational(1,2),0),(s.Rational(1,2),s.Rational(1,2))]:
    print('fixed',x,'gradient',grad.subs(dict(zip((q,p),x))).applyfunc(s.simplify),'hessian/pi2', (H.subs(dict(zip((q,p),x)))/s.pi**2).applyfunc(s.simplify))
x,y,z=s.symbols('x y z'); S=s.Matrix([[3,4],[2,3]])
M=lambda t:S*s.Matrix([[1,0],[t,1]])
assert s.expand(s.trace(M(z)*M(y)*M(x))-(198+140*(x+y+z)+96*(x*y+x*z+y*z)+64*x*y*z))==0
print('period-three trace polynomial: exact PASS')
