import math, json
from mpmath import mp, mpf, log, sqrt
mp.dps=50
eps=1+sqrt(2); L2=log(2)
def wmax(p):
    w=0; lhs=mpf(0)
    while True:
        nxt=lhs+log(p-1)+log(w+1)
        if nxt>p*log(eps): return w
        lhs=nxt; w+=1
def csharp(p): return int(math.floor(p*math.log(1+2**.5)/math.log(p-1)))
rooms={1409:mpf('0.02011297'),3307:mpf('0.00334719')}
out=[]
for p in (1409,3307):
    wm=wmax(p); cs=csharp(p); crude=p/math.log(p-1)
    row=dict(p=p,wmax=wm,csharp=cs,p_over_ln=crude,room=float(rooms[p]))
    for name,w in (('wmax',wm),('w228',228),('csharp',cs),('crude',crude)):
        nl=mpf(2)**w-2
        row[f'c_noroom_{name}']=float(log(nl)/p)               # (2^w-2) e^{-cp} < 1
        row[f'c_room_{name}']=float((log(nl)-log(rooms[p]))/p)  # (2^w-2) C e^{-cp} < room, C=1
    out.append(row); print(json.dumps(row,indent=1))
# asymptotic threshold: smallest p (prime-agnostic) with ln2*wmax(p)/p < 0.048, and with crude bound
for c in (0.048,):
    for p in [3307,5000,10000,20000,50000,100000,200000,500000]:
        print(p, 'ln2*wmax/p=',float(L2*wmax(p)/p), ' ln2/ln(p-1)=',math.log(2)/math.log(p-1))
print('crude p0 for 0.048: p-1 >', math.exp(math.log(2)/0.048))
json.dump(out,open('h5b_const.json','w'),indent=1)
