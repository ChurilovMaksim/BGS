import sys,time; sys.path.insert(0,'code'); from twlaw import *
m=33; d=mdata(m); M=2*d['h']; x0=pow(4,-1,M//2); nu0=min(x for x in (x0,x0+M//2) if x%2==1); assert (8*nu0-2)%M==0
tw=TW(m,nu0,L=8,K=32); t=time.time(); tw.Z([0.1]*m); print('sec/run',time.time()-t)
