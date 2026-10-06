#!/usr/bin/env python3
"""Exact finite rank-two classification kernel; universal scope needs reduction proof."""
from itertools import combinations
from collections import Counter
import json

def check_one(m,classes,kind,stats):
 lab=list(range(m));tau=list(range(m))
 for cl in classes:
  for j in cl:lab[j]=cl[0]
  for a,b in zip(cl,cl[1:]+cl[:1]):tau[a]=b
 ti=[0]*m
 for a,b in enumerate(tau):ti[b]=a
 c=[(i-1)%m for i in range(m)]
 S=set(j for cl in classes for j in cl)
 for H in combinations(range(m),4):
  if len({lab[j] for j in H})<4:continue
  h=list(range(m))
  for a,b in ((H[0],H[2]),(H[1],H[3])):h[a]=b;h[b]=a
  r=[c[h[j]] for j in range(m)]
  rp=[tau[r[ti[j]]] for j in range(m)]
  Hp=tuple(j for j in range(m) if rp[j]!=c[j])
  if len(Hp)!=4 or len({lab[j] for j in Hp})<4:continue
  hp=list(range(m))
  for a,b in ((Hp[0],Hp[2]),(Hp[1],Hp[3])):hp[a]=b;hp[b]=a
  if any(rp[j]!=c[hp[j]] for j in range(m)):continue
  if H==Hp:raise RuntimeError('unexpected identical heads')
  stats['directed_matches']+=1
  if kind=='triple':raise RuntimeError(str(('triple_counterexample',m,classes,H,Hp)))
  starts=[a for a in range(m) if S=={(a+j)%m for j in range(4)}]
  if not starts:raise RuntimeError(str(('nonlocal_counterexample',m,classes,H,Hp)))
  if not any(lab[a]==lab[(a+2)%m] and lab[(a+1)%m]==lab[(a+3)%m] and lab[a]!=lab[(a+1)%m] for a in starts):raise RuntimeError('nonalternating counterexample')
  local_form=False
  for a in starts:
   base={a,(a+4)%m}
   for z in range(m):
    H1=base|{(a+1)%m,z};H2=base|{(a+3)%m,z}
    if len(H1)==len(H2)==4 and {frozenset(H),frozenset(Hp)}=={frozenset(H1),frozenset(H2)}:local_form=True
  if not local_form:raise RuntimeError(str(('unexpected_local_cut_form',m,classes,H,Hp)))
  stats['local_alternating_matches']+=1

def run():
 out={}
 for kind,maxm in (('pairs',12),('triple',10)):
  stats=Counter()
  for m in range(5,maxm+1):
   if kind=='pairs':
    for v in combinations(range(m),4):
     for classes in (((v[0],v[1]),(v[2],v[3])),((v[0],v[2]),(v[1],v[3])),((v[0],v[3]),(v[1],v[2]))):stats['partitions']+=1;check_one(m,classes,kind,stats)
   else:
    for v in combinations(range(m),3):
     for cl in (v,(v[0],v[2],v[1])):stats['oriented_cycles']+=1;check_one(m,(cl,),kind,stats)
  out[kind]={'m_range':[5,maxm],**stats}
 return out

def main():
 out=run()
 if out["pairs"].get("partitions") != 3858 or out["pairs"].get("directed_matches") != 560 or out["pairs"].get("local_alternating_matches") != 560 or out["triple"].get("oriented_cycles") != 650 or out["triple"].get("directed_matches",0) != 0:
  raise RuntimeError("unexpected exhaustive totals")
 print(json.dumps(out,indent=2))

if __name__ == "__main__":
 main()
