# referee lineN21: (a) F21-2 dps claim; (b) twist-splitting d_t = d^i_t + d^j_{t+G} (mod 1) -- own twist formula at high precision
import sys, json, mpmath as mp
sys.path.insert(0,'/workspace/bgs-lineN/N14/code')
import digits as Dg
TYPES={'odd':(2,0),'sq2':(0,2),'two':(4,0),'2sq2':(0,4),'four':(8,0)}; EPS=(1,1)
def mulq(x,y): return (x[0]*y[0]+2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def lamp(G):
    r=(1,0)
    for _ in range(G): r=mulq(r,(3,2))
    return r
def pairs(G):
    for ti in TYPES:
        for tj in TYPES:
            for h in (0,1):
                for sg in (1,-1):
                    ej=mulq(TYPES[tj],lamp(G))
                    if h: ej=mulq(ej,EPS)
                    yield (ti,tj,h,sg),(TYPES[ti][0]+sg*ej[0],TYPES[ti][1]+sg*ej[1])
def core_at(dps,e,KK=18):
    mp.mp.dps=dps; Dg.S2=mp.sqrt(2); Dg.LAM=3+2*Dg.S2
    return [Dg.core(z,KK) for z in Dg.seeds(*e)]
res={}
# (a) dps 34 vs 300
for G in list(range(2,24))+[25,30,40]:
    mx=0.0
    for key,e in pairs(G):
        a=core_at(34,e); b=core_at(300,e)
        for x,y in zip(a,b):
            assert len(x)==len(y)
            mx=max(mx,max(abs(u-v) for u,v in zip(x,y)))
    res[G]=mx; print('G',G,'max|d34-d300|',mx,flush=True)
# (b) twist splitting, own formula: d(z,t)=red(e1 lam^t) t<=0, red(-e2 lam^-t) t>0, mp.dps=400
mp.mp.dps=400; S2=mp.sqrt(2); LAM=3+2*S2
def red(x): return x-mp.floor(x+mp.mpf(1)/2)
def d(z,t):
    e1=z[0]+z[1]*S2; e2=z[0]-z[1]*S2
    return red(e1*LAM**t) if t<=0 else red(-e2*LAM**(-t))
def seeds(ea,eb):
    zA=(mp.mpf(2*eb)/8, mp.mpf(ea)/8); fu=-ea+2*eb; fv=ea-eb; zB=(-mp.mpf(2*fv)/8,-mp.mpf(fu)/8); return zA,zB
spl={}
for G in (3,15,16,36,37,60):
    mx=mp.mpf(0)
    for (ti,tj,h,sg),e in pairs(G):
        ej=TYPES[tj] if not h else mulq(TYPES[tj],EPS); ej=(sg*ej[0],sg*ej[1])
        for w in (0,1):
            zp=seeds(*e)[w]; zi=seeds(*TYPES[ti])[w]; zj=seeds(*ej)[w]
            for t in range(-G-60,61):
                diff=red(d(zp,t)-d(zi,t)-d(zj,t+G))
                mx=max(mx,abs(diff))
    spl[G]=float(mx); print('split G',G,'max |d_t - d^i_t - d^j_{t+G}| mod 1 =',float(mx),flush=True)
json.dump(dict(dps34_vs_300=res,split=spl),open('../logs/ref_twists.json','w'),indent=1)
