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
