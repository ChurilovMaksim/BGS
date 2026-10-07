"""Exact finite adversarial controls for the separately audited source bound.
Not a proof of an analytic bound. No randomness or floating-point arithmetic.
"""
from fractions import Fraction as Q
from itertools import combinations_with_replacement
from functools import lru_cache
from math import comb, factorial, prod
import json,time,platform
start=time.monotonic()
counts=0;mono=0
for universe in range(8):
 for k in range(6):
  for ns in combinations_with_replacement(range(universe+1),k):
   @lru_cache(None)
   def assignments(j,mask):
    if j==k:return 1
    return sum(assignments(j+1,mask|(1<<v))for v in range(ns[j])if not mask&(1<<v))
   actual=assignments(0,0)
   claimed=prod(max(n-j,0)for j,n in enumerate(ns))
   assert actual==claimed,(universe,ns,actual,claimed)
   counts+=1
   for j in range(k):
    if ns[j] < (ns[j+1] if j+1<k else universe):
     larger=list(ns);larger[j]+=1
     larger_count=prod(max(n-i,0)for i,n in enumerate(larger))
     assert larger_count>=actual
     mono+=1

def falling(n,k):return prod(range(n-k+1,n+1)) if n>=k else 0
laws=0;moment_checks=0;factorial_checks=0
for n in range(1,21):
 for q in (Q(0),Q(1,100),Q(1,3),Q(1,2),Q(99,100),Q(1)):
  m=n*q
  binomial={z:Q(comb(n,z))*q**z*(1-q)**(n-z)for z in range(n+1)}
  lo=m.numerator//m.denominator;frac=m-lo
  clock={lo:1-frac}
  if frac:clock[lo+1]=frac
  for name,law in [('diagonal',binomial),('clock',clock)]:
   assert sum(law.values())==1
   assert sum(z*p for z,p in law.items())==m
   variance=sum((z-m)**2*p for z,p in law.items())
   assert variance<=m
   for k in range(n+3):
    fac=sum(falling(z,k)*p for z,p in law.items())
    assert fac<=m**k,(name,n,q,k,fac,m**k)
    factorial_checks+=1
   for p in range(2,13):
    neg=sum(max(m-z,0)**p*prob for z,prob in law.items())
    assert neg<=m**(p-1),(name,n,q,p,neg,m**(p-1))
    moment_checks+=1
   laws+=1
# Coefficientwise verification of exp(t)-1-t <= t²/[2(1-t/3)]
# for the specified finite Taylor range; the all-degree induction is in review.
for k in range(2,41):assert Q(1,factorial(k))<=Q(1,2*3**(k-2))
# A rational certificate for the loose analytic numerical constant, using
# pi<22/7 and sqrt(pi)<2:
upper=(Q(22,7)**3)+6*Q(22,7)**2
assert upper<100
# 1+3/(2e)+9/4<4 follows already from e>2.
assert Q(1)+Q(3,4)+Q(9,4)==4
result={'status':'passed','arithmetic':'exact rational; finite integer enumeration',
 'nested_count_chains':counts,'feasible_coordinate_monotonicity_checks':mono,
 'nested_bounds':{'universe_size':'0..7','number_nested_sets':'0..5'},
 'exact_diagonal_clock_laws':laws,'factorial_moment_checks':factorial_checks,
 'lower_deviation_moment_checks':moment_checks,'law_bounds':{'N':'1..20','p_moment':'2..12','arc_fractions':['0','1/100','1/3','1/2','99/100','1']},
 'chernoff_taylor_degree':'2..40','constant_rational_upper':str(upper),'constant_margin_to_100':str(100-upper),
 'python':platform.python_version(),'runtime_seconds':time.monotonic()-start,
 'nonclaims':['Finite enumeration does not prove arbitrary nested-arc resampling.','No numerical integration is used to establish the analytic kernel estimates.','The dimension-uniform theorem is audited by the separate written proof.']}
print(json.dumps(result,indent=2))
