"""Portable exact controls for global rotated-box contour bookkeeping.
Analytic limits are proved in the maintained mathematical source, not here.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial
import json
import sympy as s

def check(ok, tag):
    if not ok:
        raise RuntimeError(tag)

def Kmat(m):
    if type(m) is not int or not 1 <= m <= 8:
        raise ValueError("dimension outside declared exact fixture range")
    K=s.Rational(3,2)*s.eye(m)
    for j in range(m):
        K[j,(j+1)%m]-=s.Rational(1,4)
        K[j,(j-1)%m]-=s.Rational(1,4)
    return K

def run():
    corners=0
    for m in range(1,7):
     K=Kmat(m)
     for signs in product((-1,1),repeat=m):
      # q_j = s_j (K s)_j are the slopes in each large magnitude.
      q=[signs[j]*sum(K[j,k]*signs[k] for k in range(m)) for j in range(m)]
      check(min(q)>=1,('large slopes',m,signs))
      for mask in range(1,2**m):
       S=[j for j in range(m) if (mask>>j)&1]
       T=[j for j in range(m) if not ((mask>>j)&1)]
       core=sum(K[j,k]*signs[j]*signs[k] for j in T for k in T)
       check(sum(q)-core>=s.Rational(len(S),2),('threshold',m,mask,signs))
       corners+=1
    eta=s.Rational(1,10000);dc=0
    for m in range(1,8):
     for sign in (-1,1):
      K=Kmat(m)
      for j in range(m):
       k=(j+1)%m
       for a,b in [(j,j),(j,k),(k,j),(k,k)]:K[a,b]+=sign*eta
      check(all(K[j,j]-sum(abs(K[j,k]) for k in range(m) if k!=j)>=1-4*eta for j in range(m)),('row',m))
      dk=K.det()
      for mask in range(1,2**m):
       T=[j for j in range(m) if not ((mask>>j)&1)];dT=K.extract(T,T).det() if T else 1
       check(0<dk/dT<=s.Rational(21,10)**(m-len(T)),('schur',m,mask));dc+=1
    check(1-24*eta>=s.Rational(9,10),'D5 slope')
    check(1-24*eta-(s.Rational(1,2)+22*eta)>=s.Rational(2,5),'D5 threshold')
    h=s.Symbol('h',positive=True)
    for m in range(1,8):
     for q in range(1,m+1):
      t=m-q
      rat=2**s.Rational(t,2)*(s.pi*h)**s.Rational(t,2)/(2*s.pi*h)**s.Rational(m,2)
      check(s.simplify(rat-(2*s.pi*h)**(-s.Rational(q,2)))==0,('h normalization',m,q))
    # An unrestricted completion of the true three-cycle core leaves its box.
    y,z=s.symbols('y z');Q=150+s.Rational(3,2)*(y*y+z*z)-s.Rational(1,2)*y*z-s.Rational(101,4)*(y+z)
    sol=s.solve([s.diff(Q,y),s.diff(Q,z)],(y,z));bad=s.factor(Q.subs(sol))
    check(bad<0 and sol[y]>1 and sol[z]>1,'unrestricted shortcut fails')
    result={'exact_corner_certificates':corners,'perturbed_schur_subset_checks':dc,'h_normalization_checks':28,'unrestricted_three_cycle_optimizer':str(sol),'unrestricted_three_cycle_minimum':str(bad),'scope':'finite exact arithmetic only; analytic inequalities reconstructed separately'}
    
    T=F(1,10**80); eup=F(11,4)
    check(sum(F(1,factorial(j)) for j in range(5))+F(1,100)<eup,"e upper")
    check(sum(F(1,factorial(j)) for j in range(4))==F(8,3),"e lower")
    check(45*F(22,7)<142,"strip exponential")
    G=52*eup**142
    check(G<10**66 and G*63**2<10**70 and G*63**3<10**72,"symbol jets")
    check(T*10**73==F(1,10**7),"flow time")
    check(T*10**76==F(1,10000),"edge Hessian")
    check(4*T*10**76<F(1,10),"cyclic Hessian")
    check(F(180,49)<4 and 64*F(1,10000)<F(1,10),"radius finite-family margin")
    check(45<49 and F(8,3)**2>7 and F(8,5)*3-4==F(4,5),"summed exponent margin")
    result["literal_constant_groups"]=9
    result["parameter_convention"]="h=(2*pi*N)^-1; N^-ell=(2*pi*h)^ell"
    return result

def main():
    print(json.dumps(run(), indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
