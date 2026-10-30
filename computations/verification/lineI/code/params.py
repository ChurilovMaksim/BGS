import math
from law import mdata
for m in range(3,60,2):
    D=mdata(m); h=D['h']; yp=D['yp']; M=2*h
    out=[]
    for d in (7,23,41,47,71):
        if h%d==0: out.append(d)
    rec=[]
    for (a,b) in ((2,8),(-2,8),(2,16),(-2,16)):
        try:
            nu = next(x for x in [((a//2)*pow(b//2, -1, h)) % h + s*h for s in (0, 1)] if x % 2 == 1)
        except Exception as e: rec.append('na'); continue
        k=(b*nu-a)//M; rec.append((k%b, yp%b, (3*yp-2*h)%b))
    print(m, 'h%7',h%7, 'dlist',out, rec)
