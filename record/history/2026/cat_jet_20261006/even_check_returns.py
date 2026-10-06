#!/usr/bin/env python3
"""Exact whole-support return and weighted cyclotomic sum controls at r=2,3.
Integer arithmetic only. No author code or floating point.
"""
if not __debug__: raise RuntimeError("Assertions are required")
import json, time, hashlib, platform
from collections import defaultdict, Counter
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parent
raw=json.loads((ROOT/'residue_checks.json').read_text())
coeff={tuple(row['v']):tuple(row['d'])for row in raw['independent_coefficients']}
valuation={tuple(row['v']):row['valuation_at_i_2']for row in raw['independent_coefficients']}
def advance(v,m):a,b=v;return((3*a+4*b)%m,(2*a+3*b)%m)
def pairmul(x,y,m):a,b=x;c,d=y;return((a*c+2*b*d)%m,(a*d+b*c)%m)
def pairpower(k,m):
 ans=(1,0);x=(3,2)
 while k:
  if k&1:ans=pairmul(ans,x,m)
  x=pairmul(x,x,m);k//=2
 return ans
def apply(pair,v,m):a,b=pair;c,d=v;return((a*c+2*b*d)%m,(b*c+a*d)%m)
def norm(v):a,b=v;return 2*b*b-a*a
def content(v):return 1 if v[0]%5==0 and v[1]%5==0 else 0
def cyclotomic_zero(d,n):
 d=dict(d);step=n//5;deg=4*step
 for j in list(d):
  if j>=deg:
   c=d.pop(j)
   for k in range(4):idx=j-deg+k*step;d[idx]=d.get(idx,0)-c
 return not any(d.values())
START=time.time();runs=[]
for r in [2,3]:
 h=5**r;n=h*h;R=6*5**(2*r-1);L=6*5**(r-1);lowerL=L//5
 a,b=pairpower(L,n);assert a==1 and b%h==0 and (b//h)%5==2;beta=b//h
 assert pairpower(R,n)==(1,0)
 assert all(pairpower(R//p,n)!=(1,0)for p in [2,3,5])
 # Complete actual support return enumeration, every k in [0,R).
 vectors={u:u for u in coeff};returns={(v,u):[]for v in coeff for u in coeff}
 target=defaultdict(list)
 for v in coeff:target[tuple(-c%h for c in v)].append(v)
 for k in range(R):
  for u,s in vectors.items():
   for v in target[(s[0]%h,s[1]%h)]:returns[v,u].append((k,((v[0]*s[1]-v[1]*s[0])*pow(2,-1,n))%n))
  vectors={u:advance(s,n)for u,s in vectors.items()}
 # Check the seven-factor constancy independently via its period 3.
 assert pairpower(3,7)==(1,0)and pairpower(1,7)!=(1,0)
 counts=Counter();details=[];sumchecks=0;removed=0
 for (v,u),row in returns.items():
  cv,cu=content(v),content(u)
  should=cv==cu and ((norm(v)//(25**cv)-norm(u)//(25**cu))%(h//(5**cv))==0)
  assert bool(row)==should,(r,v,u)
  if not row:continue
  period=L//(5**cv);ks=[q[0]for q in row];a0=ks[0];length=R//period
  assert 0<=a0<period and ks==[a0+j*period for j in range(length)]
  assert len(row)==length and all(k%3==a0%3 for k in ks)
  E=row[0][1];D=(row[1][1]-E)%n
  assert all(q[1]==(E+j*D)%n for j,q in enumerate(row))
  if cv==0:
   C=(beta*norm(v)*pow(2,-1,h))%h
   assert D==h*C and C%5!=0 and E%h==0
   expected_order=h
  else:
   hp=h//5;a1,b1=pairpower(period,hp*hp);assert a1==1 and b1%hp==0
   bp=b1//hp;C=(bp*(norm(v)//25)*pow(2,-1,hp))%hp
   assert bp%5==2 and D==5*h*C and C%5!=0 and E%(5*h)==0
   expected_order=hp
  from math import gcd
  assert n//gcd(D,n)==expected_order
  # Exact verification of sum_j(R-2k_j) q^E_j = 2R q^E/(1-q^D).
  pol=defaultdict(int)
  for k,e,*_ in row:
   c=R-2*k;pol[e]+=c;pol[(e+D)%n]-=c
  pol[E]-=2*R
  assert cyclotomic_zero(pol,n),(r,v,u,'weighted cyclotomic failure')
  # Eq(2) deletes k=0, and exactly R*theta=R since E_0=0 then.
  if a0==0:
   assert E==0;removed+=1
   # Normalized finite subtraction has valuation a_r+d_v+d_u (>0).
   assert Fraction(1,4*5**(r-1))+valuation[v]+valuation[u]>0
  a_r=Fraction(1,4*5**(r-1));denval=a_r if cv==0 else 5*a_r
  normalizedval=valuation[v]+valuation[u]+a_r-denval
  if v[0]==1 and u[0]==1:
   assert norm(v)==norm(u)and normalizedval==0
   counts['surviving_upper_upper']+=1
  else:assert normalizedval>0
  kind='nonprimitive'if cv else'primitive';counts[kind]+=1;sumchecks+=1
  if cv:details.append({'v':v,'u':u,'return_count':length,'period':period,'a':a0,'root_order':expected_order,'normalized_valuation':str(normalizedval)})
 assert counts['surviving_upper_upper']==17
 runs.append({'r':r,'h':h,'n':n,'R':R,'L':L,'beta_mod_h':beta,'pairs_tested':len(returns),'mode_time_steps':32*R,'return_pair_counts':dict(counts),'weighted_sum_checks':sumchecks,'k0_subtraction_classes':removed,'nonprimitive_details':details})
# independent explicit finite torus classification at mod 5 and 25
norm_tori=[]
for h in [5,25]:
 group={(a,b)for a in range(h)for b in range(h)if (a*a-2*b*b)%h==1};order=6*h//5
 generated={pairpower(k,h)for k in range(order)};assert group==generated
 prim=[(a,b)for a in range(h)for b in range(h)if a%5 or b%5]
 sizes=Counter(norm(v)%h for v in prim)
 assert all(sizes[q]==order for q in range(h)if q%5)
 for v in prim:
  orb={apply(g,v,h)for g in group};assert len(orb)==order and all(norm(w)%h==norm(v)%h for w in orb)
 norm_tori.append({'modulus':h,'torus_size':len(group),'primitive_vectors':len(prim),'all_orbits_full_norm_fibers':True})
# Exact resolvent numerator identity after multiplication by 1-z in Q[z]/(z^R-1).
# Desired at nontrivial roots; difference is a multiple of 1+...+z^(R-1).
resolvents=[]
for R in [3,6,30,150,750,18750]:
 c=[0]+[R-2*k for k in range(1,R)]
 d=[c[j]-c[(j-1)%R]-R*(j in [0,1])for j in range(R)]
 assert d==[-2]*R and sum(c)==0
 resolvents.append(R)
out={'runs':runs,'norm_torus_controls':norm_tori,'resolvent_polynomial_controls':resolvents,'seconds':time.time()-START,'python':platform.python_version()}
(ROOT/'return_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
