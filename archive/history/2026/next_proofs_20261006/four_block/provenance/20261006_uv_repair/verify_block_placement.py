#!/usr/bin/env python3
"""Exact token check of corrected U/V block placement, including empty pieces."""
from itertools import product
import json

def rotate_x(w):
 i=w.index('X');return w[i:]+w[:i]
def token(name,n):return [(name,i) for i in range(n)]
out={}
for case in ('U','V'):
 count=0;old_rejected=0
 for lengths in product(range(3),repeat=6):
  p1,p2,q1,q2,r1,r2=[token(name,n) for name,n in zip(('p1','p2','q1','q2','r1','r2'),lengths)]
  for e in range(1,4):
   E=token('E',e);B=r2+['X']+p1;C=p2+['Y']+q1;D=q2+['Z']+r1
   source_blocks=[B,E,C,D] if case=='U' else [B,C,E,D]
   direct=rotate_x(source_blocks[0]+source_blocks[3]+source_blocks[2]+source_blocks[1])
   U=['X']+p1+q2+['Z']+r1+p2+['Y']+q1+E+r2
   V=['X']+p1+q2+['Z']+r1+E+p2+['Y']+q1+r2
   correct,old=(U,V) if case=='U' else (V,U)
   if direct!=correct:raise RuntimeError(('correct equation mismatch',case,lengths,e))
   if direct==old:raise RuntimeError(('old error not detected',case,lengths,e))
   count+=1;old_rejected+=1
 out[case]={'exact_token_cases':count,'old_placement_rejected':old_rejected,'pieces_allow_empty':True}
print(json.dumps(out,indent=2))
