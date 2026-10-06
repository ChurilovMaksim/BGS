"""Exact finite controls for weighted stationary-action resolvents."""
from fractions import Fraction as F
import sympy as s
import json

def check(v,msg):
 if not v:raise RuntimeError(msg)
def weighted(A,m):
 return max(sum(abs(A[i,j])*2**min((i-j)%m,(j-i)%m) for j in range(m)) for i in range(m))
def run():
 eta=s.Rational(1,10000);rows=[]
 for m in range(1,13):
  K=s.Rational(3,2)*s.eye(m);E=s.zeros(m);F0=s.zeros(m);Er=s.zeros(m)
  for j in range(m):
   nxt=(j+1)%m
   K[j,nxt]-=s.Rational(1,4);K[nxt,j]-=s.Rational(1,4)
   for a,b in [(j,j),(j,nxt),(nxt,j),(nxt,nxt)]:E[a,b]+=eta
   F0[j,j]+=s.Rational(1,4);F0[nxt,j]-=s.Rational(3,4)
   Er[j,j]+=eta;Er[nxt,j]+=eta
  G0=K.inv();check(weighted(G0,m)<=2,('base weighted',m))
  check(weighted(E,m)<=6*eta and weighted(F0,m)<=s.Rational(7,4) and weighted(Er,m)<=3*eta,('input norms',m))
  for sign in [-1,1]:
   G=(K-sign*E).inv();d=G-G0
   check(weighted(G,m)<=3,('actual weighted',m,sign))
   check(weighted(d,m)<=36*eta,('difference',m,sign))
   check(weighted(d*F0+G*Er,m)<=72*eta,('branch derivative',m,sign))
   rows.append({'m':m,'sign':sign,'weighted_G':str(weighted(G,m)),'weighted_difference_over_eta':str(s.factor(weighted(d,m)/eta))})
 tau=F(1,10**80);realeta=10**10*tau+10**50*tau*tau
 check(realeta<2*F(1,10**70),'literal eta')
 check(12*realeta<F(1,3),'Neumann denominator')
 check(F(1)+F(2,5)<3*(1-F(2,5)),'Green convolution factor')
 check(96*10*4<10000,'Holder constant slack')
 return {'arithmetic':'exact rational matrices; no floating point','rows':rows,'literal_tau':str(tau),'boundary':'Finite checks support resolvent bookkeeping, not the nonlinear infinite-chain proof or Fourier decay.'}
def main():
    print(json.dumps(run(),indent=2))

if __name__=='__main__':
    main()
