"""Referee N12: compare N12 window-model merged-type ratios (d_merged, p-independent, float Galerkin) with exact-twist TW values
computed by the referee at p=59 (lineN10 ref_gas: odd+sqrt2 / odd+2 two-bump at lambda-gap g; lineN11 ref_gas2: odd+odd at eps-gap n).
Ratio = w_pair/(w_i w_j). Conventions differ by complex conjugation (referee normalises Im w*>0) -> compare up to conjugation."""
import json
rows=json.load(open('/workspace/bgs-lineN/N12/logs/d_merged_odd_sq2.json'))['rows']
R={(r['i'],r['j'],r['h'],r['s'],r['G']):complex(*r['cls']) for r in rows}
c0=complex(2.9866107087366787e-05,-6.598660723733838e-06); c4=complex(1.0413467768390528e-06,-3.116369935363968e-06)
out=[]
for p in (37,59):
    g10={x['name']:x for x in json.load(open(f'/workspace/audit/lineN10/logs/ref_gas_p{p}.json'))['rows']}
    for nm,x in g10.items():
        if not nm.startswith('two_'): continue
        _,b,s,g=nm.split('_'); s=int(s[1:]); g=int(g[1:])
        phi=complex(*x['phi']); ex=phi/(c0 if b=='r2' else c4)
        key=('odd','sq2' if b=='r2' else 'two',0,s,g)
        if key in R: w=R[key]; out.append(dict(p=p,cls=nm,exact=[ex.real,ex.imag],window=[w.real,w.imag],diff=min(abs(ex-w),abs(ex-w.conjugate()))))
    g11={x['name']:x for x in json.load(open(f'/workspace/audit/lineN11/logs/ref_gas2_p{p}.json'))['rows']}
    for nm,x in g11.items():
        if not nm.startswith('odd2_z0'): continue
        n=int(nm.split('_')[2][1:]); s=int(nm.split('_')[3][1:]); G,h=divmod(n,2)
        ex=complex(*x['ratio_to_wstar_n']); key=('odd','odd',h,s,G)
        if key in R: w=R[key]; out.append(dict(p=p,cls=nm,exact=[ex.real,ex.imag],window=[w.real,w.imag],diff=min(abs(ex-w),abs(ex-w.conjugate()))))
mx=max(o['diff'] for o in out)
print(json.dumps(dict(n=len(out),max_abs_diff=mx,rows=out),indent=0)[:3000]); json.dump(dict(n=len(out),max_abs_diff=mx,rows=out),open('logs/ref_window_vs_exact.json','w'),indent=1)
