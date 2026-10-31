import sys,time; sys.path.insert(0,'/workspace/bgs-lineL/L2/code'); from twlaw import *
for m,L,K in [(33,8,32),(33,8,16),(33,6,16)]:
    d=mdata(m); h=d['h']; M=2*h
    x0=(pow(4,-1,M//2))%(M//2); nu0=min(x for x in (x0,x0+M//2) if x%2==1)
    tw=TW(m,nu0,L=L,K=K); t=time.time(); z=tw.Z([0.5]*m); z2=tw.Z([0.0]*m); print(m,L,K,len(tw.ns),tw.S,(time.time()-t)/2,abs(z),abs(z2))
