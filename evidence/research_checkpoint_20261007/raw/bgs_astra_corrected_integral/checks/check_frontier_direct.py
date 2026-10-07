"""Independent finite coefficient checks for the first off-hook diagnostic.
Loads the explicit cyclotomic arithmetic only, then recomputes the m=4 power
sum by rooted closed words and h_4 by repeated-index permanents.
"""
import runpy,sys,itertools,json,math,io,contextlib
from pathlib import Path
sys.argv=['check_hook_covariance.py','5','4']
with contextlib.redirect_stdout(io.StringIO()):d=runpy.run_path(str(Path(__file__).with_name('check_hook_covariance.py')))
C=d['C'];p=d['p'];sigma=d['sigma'];h=d['h'];power=d['power']
def compositions(n,k):
 if k==1:yield(n,);return
 for a in range(n+1):
  for b in compositions(n-a,k-1):yield(a,)+b
checks=[]
for m in (2,3,4):
 direct={}
 for word in itertools.product(range(p),repeat=m):
  e=tuple(word.count(i)for i in range(p));ex=sum(sigma[word[i]]*word[(i+1)%m] for i in range(m))
  direct[e]=direct.get(e,C())+C.z(ex)
 assert all(direct.get(e,C()).v==power[m].get(e,C()).v for e in set(direct)|set(power[m]))
 for e in compositions(m,p):
  inds=tuple(i for i in range(p)for _ in range(e[i]));num=C()
  for perm in itertools.permutations(range(m)):
   num+=C.z(sum(sigma[inds[i]]*inds[perm[i]]for i in range(m)))
  den=math.prod(math.factorial(a)for a in e)
  assert all(v%den==0 for v in num.v)
  val=C([v//den for v in num.v])
  assert val.v==h[m].get(e,C()).v
 checks.append(dict(m=m,rooted_words=p**m,occupation_classes=math.comb(p+m-1,m),passed=True))
print(json.dumps({'arithmetic':'exact cyclotomic integer coefficients','checks':checks,'Re_M_4_0_1':'3*sqrt(5)/625','finite_diagnostic_only':True},indent=2))
