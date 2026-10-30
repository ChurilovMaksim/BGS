import math,sys
sys.setrecursionlimit(10000)
def hy(m):
    h,y=1,0
    for _ in range(m): h,y=h+2*y,h+y   # (h+y r)(1+r)
    return h,y
bad=[];tab={}
for m in range(1,700):
    h,yp=hy(m)
    if m%2==1: assert h*h+1==2*yp*yp
    if (h%7==0)!=(m%6==3): bad.append(('7|h',m))
    if m%2==1 and h%7==0:
        nu=next(x for x in [((1)*pow(4,-1,h))%h+s*h for s in (0,1)] if x%2==1)   # a/2 * (b/2)^-1 = 1*4^-1
        assert (8*nu-2)%(2*h)==0; k=((8*nu-2)//(2*h))%8
        par=(k,yp%8,(3*yp-2*h)%8)
        assert k==(3*pow(h,-1,8))%8, m
        tab.setdefault(m%24,set()).add(par)
        if m%24==9: assert par==(3,1,1),(m,par)
print('7|h <=> m=3 mod 6 for m<700:',not bad)
print({r:sorted(v) for r,v in tab.items()})
# (1+sqrt2)^m mod 8 period
seq=[(hy(m)[0]%8,hy(m)[1]%8) for m in range(1,60)]
per=next(p for p in range(1,30) if all(seq[i]==seq[i+p] for i in range(len(seq)-p)))
print('period of (1+sqrt2)^m mod 8:',per)
