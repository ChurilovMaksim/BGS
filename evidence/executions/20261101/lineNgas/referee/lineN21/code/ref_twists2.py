import sys, json, mpmath as mp
sys.path.insert(0,'/workspace/audit/lineN21/code'); sys.path.insert(0,'/workspace/bgs-lineN/N14/code')
from ref_twists_lib import *
out={}
for G in (15,20,21,22,23,25,30,35,40):
    mxa=0.0; mxr=0.0
    for key,e in pairs(G):
        a=core_at(34,e); b=core_at(300,e)
        for x,y in zip(a,b):
            for u,v in zip(x,y):
                dd=abs((u-v+0.5)%1.0-0.5); mxa=max(mxa,dd)
                if abs(v)>0: mxr=max(mxr,dd/abs(v))
    out[G]=(mxa,mxr); print(G,'max mod-1 abs diff %.3g  max rel %.3g'%(mxa,mxr),flush=True)
json.dump(out,open('../logs/ref_twists_mod1.json','w'),indent=1)
