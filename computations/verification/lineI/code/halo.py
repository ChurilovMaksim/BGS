"""Integrated theta-halo contributions to W'/m: windows around resonant couplings, and theta~0 deficit, by height band."""
import sys, numpy as np, json
from base import get
out={}
for spec in sys.argv[1:]:
    k,m=spec.split(':'); m=int(m); D=get(k,m); Z=D['Z']; RMT=float(D['RMT']); nr=~D['res']&~D['dil']; phi=len(Z); h=int(D['h'])
    a=D['a'].astype(float); b=D['b'].astype(float); l=np.hypot(a,b); th=2*a/np.maximum(b,1)
    W=lambda s:(Z[s]-RMT).sum()/phi/m
    tot=(Z.mean()-RMT-(Z[D['res']]-RMT).sum()/phi)/m
    wins={'|th|=0.5±.1':(np.abs(np.abs(th)-0.5)<0.1),'|th|=0.25±.05':(np.abs(np.abs(th)-0.25)<0.05),'|th|=0.75±.05':(np.abs(np.abs(th)-0.75)<0.05),'|th|<0.1':(np.abs(th)<0.1),
          'rest':None}
    ws=np.zeros(phi,bool)
    for kk,v in wins.items():
        if v is not None: ws|=v
    wins['rest']=~ws
    line=f'{k} m={m} W\'/m={tot:+.4f} | broad-dil/low removed: {W(~nr&~D["res"]):+.4f} |'
    o={}
    for kk,v in wins.items():
        c=W(nr&v); fr=(nr&v).mean(); o[kk]=(c,fr); line+=f' {kk}: {c:+.4f} (frac {fr:.3f}, x={Z[nr&v].mean()/RMT:.3f});'
    print(line); out[spec]=o
json.dump(out,open('../logs/halo.json','w'))
