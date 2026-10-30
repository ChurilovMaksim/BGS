import math, numpy as np, json
from law import mdata
from step1b import Z2all, load
V=[(2,392),(-2,392),(2,784),(-2,784),(2,196),(-2,196),(6,784),(-6,784),(2,8),(-2,8),(2,16),(-2,16)]
out={}
for m in [5,7,11,13]:
    T=load('full',m); h=mdata(m)['h']; Z=dict(Z2all(T,m)); out[m]={}
    for a,b in V:
        nus=[nu for nu in range(1,2*h,2) if (b*nu-a)%(2*h)==0 and nu in Z]
        out[m][f'{a},{b}']=Z[nus[0]] if nus else None
for a,b in V:
    k=f'{a},{b}'; vals=[out[m][k] for m in [5,7,11,13]]
    print(k,['%.4g'%v if v else None for v in vals], 'r(11->13)=%.3f'%((vals[3]/vals[2])**0.25) if vals[2] and vals[3] else '')
