if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import math
from law import mdata, ratrec
for m,nus in [(11,[9975,11001,11019,773,955,12009,11333,11831]),(13,[36505,22675,25691,75911,2029,92613,5567,3847]),(15,[339013,212601,149733,11831,539783,401881,178125,297581])]:
    d=mdata(m); h=d['h']; yp=d['yp']
    w=pow(yp,-1,h)  # sqrt2 mod h (up to sign): w^2 == 2
    assert (w*w-2)%h==0
    print('m',m)
    for nu in nus:
        r=[]
        for name,mult in [('nu',1),('nu*w',w),('nu/w',pow(w,-1,h)),('nu*(1+w)',1+w),('nu*(1-w)',(1-w)%h),('nu/(1+w)',pow(1+w,-1,h)),('nu/(1-w)',pow((1-w)%h,-1,h))]:
            x=(nu*mult)%h
            (a,b),_=ratrec(x,h); r.append(f'{name}:{a}/{b}')
        print('  ',nu,' '.join(r))
