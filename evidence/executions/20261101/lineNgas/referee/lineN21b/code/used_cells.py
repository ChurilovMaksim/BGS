# referee lineN21b: which N_H table cells does N21 actually use? (conv_c.NH lookup: |d|>1/256 -> cell floor((d+0.5)/h), plus neighbour at a boundary)
import sys, json, math, glob
sys.path.insert(0,'/workspace/bgs-lineN/N14/code')
import digits as Dg, mpmath as mp
mp.mp.dps=160; Dg.S2=mp.sqrt(2); Dg.LAM=3+2*Dg.S2
TH=1/2048; NC=2048
def cells(d):
    if abs(d)<=1/256: return []
    x=(d+0.5)/TH; k=min(max(int(math.floor(x)),0),NC-1); out=[k]
    if x-k<1e-9 and k>0: out.append(k-1)
    if k+1-x<1e-9 and k+1<NC: out.append(k+1)
    return out
used=set(); nwin=0
jobs=[]
for f in sorted(glob.glob('/workspace/bgs-lineN/N21/logs/convC_replay_p*.jsonl'))+sorted(glob.glob('/workspace/bgs-lineN/N21/logs/convC_ext_16_60_p*.jsonl')):
    for l in open(f):
        r=json.loads(l); jobs.append(tuple(r['e']))
TY={'odd':(2,0),'sq2':(0,2),'two':(4,0),'2sq2':(0,4),'four':(8,0)}
def mulq(x,y): return (x[0]*y[0]+2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
singles=list(TY.values())+[mulq(v,(1,1)) for v in TY.values()]
singles+= [(-a,-b) for a,b in singles]
for e in jobs:
    for KK in (18,):
        for z in Dg.seeds(*e):
            nwin+=1
            for d in Dg.core(z,KK): used.update(cells(d))
for e in singles:
    for KK in (16,17,18):
        for z in Dg.seeds(*e):
            nwin+=1
            for d in Dg.core(z,KK): used.update(cells(d))
u=sorted(used)
json.dump(dict(n_windows=nwin,n_cells=len(u),cells=u),open('../logs/used_cells.json','w'))
print(nwin,len(u))
