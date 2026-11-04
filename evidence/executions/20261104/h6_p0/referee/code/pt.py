exec(open('indep.py').read().split('# independent cover')[0].replace("print(","(lambda *a,**k:None)("))
K1,lk,wmax,ok=out['8V']
bad=[p for p in range(28420500,28420500+3000) if not ok(p)]
print('pointwise fails in [p0,p0+3000):',len(bad),bad[:10])
from sympy import isprime
print('prime fails:',[p for p in bad if isprime(p)][:10])
