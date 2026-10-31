"""N11 [N]: completeness check of the bump-type list: all classes with |N|<=Nmax, dyadic-shell sums of |w| for non-model classes.
Model single-bump types: bg1/4 alpha=1 (family); bg0 alpha' in {1, sqrt2, 2, 2sqrt2} (c0, c4, e4s2, e8) up to units/sign."""
import json, math, sys, collections
f=sys.argv[1]; d=json.load(open(f))
MODEL0={(1,0),(0,1),(2,0),(0,2)}
sh=collections.defaultdict(lambda:[0,0.0,0.0]); To=Te=0; top=[]
for r in d['res']:
    mag=math.hypot(*r['r']); a=tuple(map(abs,r['alpha']))
    if (r['bg']=='q' and a==(1,0)) or (r['bg']=='0' and a in MODEL0): continue
    j=int(math.log2(abs(r['N']))); sh[j][0]+=1; sh[j][1]+=mag; sh[j][2]=max(sh[j][2],mag); top.append((mag,r['bg'],r['alpha'],r['N']))
    if r['bg']=='q': To+=mag
    else: Te+=2*mag
top.sort(reverse=True)
print(f, 'p=',d['p'],'Nmax=',d['Nmax'],'classes',len(d['res']))
print('top non-model:',[(f'{m:.2e}',b,al,N) for m,b,al,N in top[:12]])
print('shell j (|N| in [2^j,2^j+1)): count sum max')
for j in sorted(sh): print(j,sh[j][0],'%.3e'%sh[j][1],'%.3e'%sh[j][2])
print('T_odd=%.3e T_even=%.3e (per-position units: odd adds to w_o, even adds to R)'%(To,Te))
