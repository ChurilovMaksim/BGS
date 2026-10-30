"""Lemma V (finite part) and numerical check of the lower bound chi_m >= 1 - m eta^2 sigma^2/2.
Lambda_m = {n in Z^m : sum_j n_j x_j = 0 mod h for all orbits x_{j+1}=6x_j-x_{j-1} mod h of period m}.
Lemma V(m): no nonzero n in Lambda_m with |supp n|<=2 and |n|_inf<=18."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys, itertools
def nsw(m):
    s=[1,7]
    while len(s)<=(m-1)//2: s.append(6*s[-1]-s[-2])
    return s[(m-1)//2]
def basis(m,h):
    out=[]
    for x0,x1 in [(1,0),(0,1)]:
        x=[x0,x1]
        while len(x)<m+2: x.append((6*x[-1]-x[-2])%h)
        assert x[m]%h==x0 and x[m+1]%h==x1, 'period'
        out.append(x[:m])
    return out
def lemmaV(m,B=18):
    h=nsw(m); X=basis(m,h); bad=[]
    # by shift invariance of Lambda (orbit set is shift invariant) we may take supp in {0,d}
    for d in range(0,m):
        for a in range(-B,B+1):
            for b in (range(-B,B+1) if d>0 else [0]):
                if a==0 and b==0: continue
                if all((a*x[0]+b*x[d])%h==0 for x in X): bad.append((d,a,b))
    return h,bad
if __name__=='__main__':
    for m in range(3,62,2):
        h,bad=lemmaV(m); print(m,h,'violations:',bad[:4],len(bad),flush=True)
