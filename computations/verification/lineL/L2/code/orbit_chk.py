import sys; sys.path.insert(0,'code')
from twlaw import *
m=15; d=mdata(m); h=d['h']; M=2*h
nu0=next(x for x in range(1,M,2) if (8*x-2)%M==0)
print('h',h,'nu0',nu0)
tw=TW(m,nu0,L=8,K=32)
for q in (41,31):
    pw=lam_pows(m,q); beta=(3,5)
    tau=taus_of(beta,pw,q)
    vals=[tw.Z(tau[j:]+tau[:j]) for j in (0,1,2)]
    print(q,[complex(round(v.real,8),round(v.imag,8)) for v in vals])
