import sys, itertools, numpy as np
sys.path.insert(0,'code'); sys.path.insert(0,'/workspace/bgs-lineI/code')
from twlaw import TW, lam_pows, taus_of
from law import mdata, pell
m=7; d=mdata(m); h=d['h']; yp=d['yp']; M=2*h; L=3
nu0=next(x for x in range(1,M,2) if (8*x-2)%M==0)
tw=TW(m,nu0,L=L,K=40); q=h; pw=lam_pows(m,q)
xs=[pell(k) for k in range(m)]; psi=[yp*xs[k][0]-2*h*xs[k][1] for k in range(m)]
ns=np.array(list(itertools.product(range(-L,L+1),repeat=m)))
P=np.zeros(len(ns),dtype=object)
for i in range(m):
  for j in range(m): P=P+psi[abs(i-j)]*ns[:,i].astype(object)*ns[:,j].astype(object)
ph=np.array([(nu0*int(p))%M for p in P],dtype=float)
gh=np.array([tw.gh[t] for t in range(-L,L+1)])
w=np.prod(gh[ns+L],axis=1)*np.exp(-2j*np.pi*ph/M)
for beta in [(0,0),(1,0),(3,7),(17,100)]:
  tau=np.array(taus_of(beta,pw,q),dtype=float)
  br=(w*np.exp(2j*np.pi*(ns@tau))).sum()
  print(beta,'brute',np.round(br,7),'tw',np.round(tw.Z(list(tau)),7),flush=True)
