import sys; sys.path.insert(0,'code'); from digits import *
def mulq(u,v): return (u[0]*v[0]+2*u[1]*v[1], u[0]*v[1]+u[1]*v[0])
def lamp(G):
    r=(1,0)
    for _ in range(G): r=mulq(r,(3,2))
    return r
TYPES={'odd':(2,0),'sq2':(0,2),'two':(4,0),'2sq2':(0,4),'four':(8,0)}; EPS=(1,1)
for t,e in TYPES.items():
    w,g,_=eps_digits(*e); print(t,[round(x,3) for x in w],g)
import collections
res=collections.defaultdict(list)
for ti in TYPES:
  for tj in TYPES:
    for h in (0,1):
      for sg in (1,-1):
        for G in range(0,9):
          n=2*G+h
          if n==0: continue
          ej=mulq(TYPES[tj],lamp(G))
          if h: ej=mulq(ej,EPS)
          e=(TYPES[ti][0]+sg*ej[0],TYPES[ti][1]+sg*ej[1])
          if e==(0,0): continue
          w,g,_=eps_digits(*e); res[n].append(g)
for n in sorted(res): print(n,min(res[n]),max(res[n]),collections.Counter(res[n]).most_common(4))
