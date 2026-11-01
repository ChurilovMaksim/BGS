# referee lineN22: independent crossover (mpmath 60 digits; own code from lineN21b), delta_eff = delta_true + S0(C) from N20 tail_kp_v2.json
import json, sys
src=open('/workspace/audit/lineN21b/code/ref_crossover21b.py').read().split('out=[run')[0]
ns={}; exec(src,ns); run=ns['run']
d=json.load(open('/workspace/bgs-lineN/N20/logs/tail_kp_v2.json'))
DT=5.0313e-6
rows=[]
for c in d['cases']:
    de=DT+c['S0']; r=run(repr(de)); r.update(C=c['C'],J0=c['J0'],S0=c['S0'],a=c['a'],src='exact S0+delta_true'); rows.append(r); print(c['C'],c['J0'],de,r['first_int_env'],r['first_prime'],r['viol'])
for de in ['3.4962e-4','1.1691e-4','7.4115e-6','7.1864e-6','7.0944e-6','5.0313e-6']:
    r=run(de); r.update(src='V5 rounded input'); rows.append(r); print(de,r['first_int_env'],r['first_prime'],r['viol'])
# alternative (stronger) charge: full KP weight a instead of S0
for c in d['cases']:
    if c['J0']==12:
        de=DT+c['a']
        if de<6.234e-4:
            r=run(repr(de)); r.update(C=c['C'],src='a+delta_true (overly conservative alt)'); rows.append(r); print('alt a',c['C'],de,r['first_int_env'],r['first_prime'])
        else: print('alt a',c['C'],de,'>= ReLambda: no crossover')
json.dump(rows,open('../logs/xover22.json','w'),indent=1)
