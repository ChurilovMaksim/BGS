"""N11 corrected gas model. bg0 admits an EVEN number of odd bumps (2-odd-bump weight w*^2, found in t_classes shells),
so per line X_line = [(1+R+2w)^p - 1]  (sinh+cosh = exp), X = 2[(1+L)^p - 1], L = R + 2w*.
(a) nominal numbers; (b) residual completeness check: classes explained by gas products removed by magnitude matching."""
import json, math, cmath, numpy as np
ws=complex(3.43579708677916e-4,1.9579583160123678e-4); c0=complex(2.9868592945521465e-05,-6.606363627303442e-06)
c4=complex(1.0445006903993471e-06,-3.1194465556049058e-06); c8=complex(1.3823269841170871e-08,1.1106723814121258e-08); c16=complex(-2.028329022775319e-09,-9.053883890665937e-10)
R=2*(c0+c4+c8+c16); L=R+2*ws
out=dict(R=[R.real,R.imag],L=[L.real,L.imag],absOnePlusL=abs(1+L))
ps=np.arange(3,200001,2)
X=2*((1+L)**ps-1); Xe=2*(np.exp(ps*L)-1)
negp=ps[X.real<0]
out.update(first_ReX_neg_product=int(negp[0]),first_ReX_neg_exp=int(ps[Xe.real<0][0]),frac_neg=float(np.mean(X.real<0)),
   min_abs1pX_p_ge29=float(np.abs(1+X[ps>=29]).min()), lower_bound_formula='|1+X| >= 2|1+L|^p - 1')
for p in [13,29,47,1165,1289,4001,10001]:
    z=2*((1+L)**p-1); out[f'X_p{p}']=[z.real,z.imag,abs(z),abs(1+z)]
# compare old N10 model at p=47
old=2*(cmath.exp(47*R)*(cmath.sinh(94*ws)+1)-1); out['N10_old_p47']=[old.real,old.imag]
# residual completeness check at p=47
d=json.load(open('/workspace/bgs-lineN/N11/logs/t_classes_p47_N2000.json'))
cands={'w*^2':abs(ws)**2,'w*c0':abs(ws*c0),'w*c4':abs(ws*c4),'c0^2':abs(c0)**2,'w*^2c0':abs(ws)**2*abs(c0),'w*^3':abs(ws)**3,'c0c4':abs(c0*c4),'w*c8':abs(ws*c8)}
MODEL0={(1,0),(0,1),(2,0),(0,2)}
import collections
raw=collections.defaultdict(float); resid=collections.defaultdict(float); expl=collections.Counter()
for r in d['res']:
    a=tuple(map(abs,r['alpha']))
    if (r['bg']=='q' and a==(1,0)) or (r['bg']=='0' and a in MODEL0): continue
    m=math.hypot(*r['r']); j=int(math.log2(abs(r['N']))); raw[j]+=m
    hit=[k for k,v in cands.items() if 0.5*v<=m<=2*v]
    if hit: expl[hit[0]]+=1
    else: resid[j]+=m
out['shells']={j:dict(raw=raw[j],unexplained=resid[j]) for j in sorted(raw)}
out['explained_counts']=dict(expl)
out['unexplained_total']=sum(resid.values())
print(json.dumps(out,indent=1)); json.dump(out,open('/workspace/bgs-lineN/N11/logs/g_model2.json','w'),indent=1)
