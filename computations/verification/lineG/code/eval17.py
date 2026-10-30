# Evaluate m=17 class sums against PREDICTIONS_m17.json (pre-registered). Usage: eval17.py k1|full
import sys, json, hashlib, numpy as np
from law import mdata, ratrec
from step1b import Z2all
from step1c import divisors
from step1e import PR
kick=sys.argv[1]; m=17
P=json.load(open('../PREDICTIONS_m17.json'))
print('predictions sha256', hashlib.sha256(open('../PREDICTIONS_m17.json','rb').read()).hexdigest())
T=np.fromfile(f'../logs/Torb_{kick}_m17.bin',np.complex128)
h=mdata(m)['h']; R=Z2all(T,m); nus=np.array([n for n,_ in R]); Z=np.array([z for _,z in R]); phi=len(R)
Zd=dict(zip(nus.tolist(),Z.tolist()))
F2m=Z.mean()/(2*m); print(f'{kick} m=17 h={h} phi={phi} F/2m={F2m:.4f}')
def at(a,b): return [ (int(n),Zd[int(n)]) for n in nus[(b*nus-a)%(2*h)==0] ]
out={'kick':kick,'F2m':F2m}
def chk(name,val,lo,hi):
    ok=lo<=val<=hi; print(f'  {name}: observed {val:.6g} predicted band [{lo:.6g},{hi:.6g}] -> {"PASS" if ok else "FAIL"}'); out[name]=dict(obs=val,lo=lo,hi=hi,ok=ok)
order=sorted(range(phi),key=lambda i:-Z[i])[:12]
print('  top residues:',[(int(nus[i]),f'{Z[i]:.4e}',ratrec(int(nus[i]),2*h)[0]) for i in order])
if kick=='k1':
    for e in P['k1']['primary_law']:
        a,b=e['rho']; v=at(a,b)
        if not v: print('  no unit for',e); continue
        z=v[0][1]; t=e['rel_tol']; chk(f"primary {e['N_mod_h']}",z,e['Z2']*(1-t),e['Z2']*(1+t))
    PRk=PR; prim=[(2,8),(-2,8)]
else:
    PRk=[(a,49*b) for a,b in PR]+PR; prim=[(2,392),(-2,392)]
    for a,b,val in [(2,392,7.048e8),(-2,392,5.666e8)]:
        v=at(a,b); print(f'  full ({a},{b}) observed',v[0][1] if v else None,'LineE registered (sign convention to be matched)',val)
    for a,b in [(2,784),(-2,784)]:
        v=at(a,b); 
        if v: chk(f'primary ({a},{b}) ±392',v[0][1],2.0e6/1.5,2.0e6*1.5)
    for a,b in [(2,196),(-2,196)]:
        v=at(a,b)
        if v: chk(f'primary ({a},{b}) ±98',v[0][1],3.0e5/2,3.0e5*2)
# d=103 dilution of the ±4 (or ±196) primaries
M=2*h//103; mem=[i for i in range(phi) if any((b*nus[i]-a)%M==0 and (b*nus[i]-a)%(2*h)!=0 for a,b in prim)]
dm=float(Z[mem].mean()); 
if kick=='k1': chk('d103 dilution mean',dm,7.5e4,1.17e5)
else: chk('d103 dilution mean (full)',dm,4.0e4,9.0e4)
out['d103_n']=len(mem)
if kick=='k1':
    for e in P['k1']['second_tier_extrapolated']:
        a,b=e['rho']; v=at(a,b)
        if v: chk(f"second tier {tuple(e['rho'])}",v[0][1],e['Z2']/e['band_factor'],e['Z2']*e['band_factor'])
# bulk exactly as registered: outside dilution families (d|h, 1<d<=sqrt h) of PRk and outside shortest-vector height<=8
dil=np.zeros(phi,bool)
for d in [d for d in divisors(h) if 1<d<=h**0.5]:
    M=2*h//d
    for a,b in PRk: dil|=((b*nus-a)%M==0)
hts=np.array([max(abs(ratrec(int(nu),2*h)[0][0]),ratrec(int(nu),2*h)[0][1]) for nu in nus])
for H in [8,16,32,64]:
    rem=dil|(hts<=H); bulk=Z[~rem].mean()/(2*m); print(f'  H={H}: removed {rem.mean():.3%} bulk F/2m={bulk:.4f} W\'/m={2*(bulk-2):+.3f} Ex2={((Z[~rem]/(2*m))**2).mean():.3f} max x={(Z[~rem]/(2*m)).max():.1f}')
    if H==8:
        chk('bulk F/2m (H=8)',bulk,1.95,2.15); out['bulk_removed']=float(rem.mean())
if kick=='k1': chk('total F/2m',F2m,38.7,39.5)
json.dump(out,open(f'../logs/eval17_{kick}.json','w'),default=float)
