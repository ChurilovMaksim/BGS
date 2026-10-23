#!/usr/bin/env python3
"""Bounded integer checks of the disjoint raw masks; no analytic inference."""
from pathlib import Path
import itertools as it,json
rows=[]
for N in [2,3]:
 for m in range(1,5):
  counts={};words=list(it.product(range(N),repeat=m))
  for x in words:
   for y in words:
    c=tuple((b-a)%N for a,b in zip(x,y));ham=sum(a!=b for a,b in zip(x,y));support=sum(a!=0 for a in c)
    switches=sum(c[j]!=c[(j+1)%m] for j in range(m));checksum=sum(c)%N
    off=any(x.count(a)!=y.count(a) for a in range(N))
    assert ham==support;assert not checksum or off
    xr=x[1:]+x[:1];yr=y[1:]+y[:1];cr=c[1:]+c[:1]
    assert sum(a!=b for a,b in zip(xr,yr))==ham
    assert sum(cr[j]!=cr[(j+1)%m] for j in range(m))==switches
    assert sum(cr)%N==checksum
    for r in range(m+1):
     for R in range(m+1):
      first=off and ham<=r;second=switches<=R and checksum!=0 and ham>r
      assert not(first and second);assert not second or off
      key=(r,R);v=counts.setdefault(key,[0,0,0]);v[0]+=first;v[1]+=second;v[2]+=(first or second)
  for (r,R),v in sorted(counts.items()):
   assert v[0]+v[1]==v[2]
   rows.append({'N':N,'m':m,'hamming_radius':r,'switch_radius':R,'offcharge_low_hamming':v[0],'nonzero_checksum_low_switch_high_hamming':v[1],'disjoint_union':v[2]})
Path(__file__).with_name('synthesis_results.json').write_text(json.dumps({'arithmetic':'exact integers','pair_families':[[N,m,N**(2*m)] for N in [2,3] for m in range(1,5)],'all_radii':True,'mask_cases':rows},indent=2)+'\n')
print('PASS',len(rows),'radius pairs across eight literal coordinate families')
