"""N12 (1g) per-site interaction delta_int (absolute activities), coded configurations only (eps-gap n = 2G+h >= g0 = 5, Lemma C(i)).
|w_ij - w_i w_j| = |w_i||w_j| dev_ij, single |w_t| = |r_A r_B|^3 (window model). Explicit types G<=15 (d_merged, float),
tail G>=16 from e_tailH (adapted norm, kap_H = 0.45, constant 1). Both orderings counted (conservative).
Smaller gaps (n<5) are NOT two-bump polymers: their seeds coincide with other single types or are uncoded -> tail (T)."""
import json,glob,collections
rows=[];single=None
for f in glob.glob('/workspace/bgs-lineN/N12/logs/d_merged_*.json'):
    d=json.load(open(f))
    if d['Gmax']!=16: continue
    rows+=d['rows']; single=d['single']
w={k:abs(complex(*v[0])*complex(*v[1]))**3 for k,v in single.items()}
out=dict(single_abs=w)
for r in rows: r['abs']=w[r['i']]*w[r['j']]*r['dev']; r['n']=2*r['G']+r['h']
tail=json.load(open('/workspace/bgs-lineN/N12/logs/e_tailH_G16.json'))['rows']
tail_abs=sum(w[r['i']]*w[r['j']]*r['tail_devsum'] for r in tail)
for g0 in (5,6,7):
    sel=[r for r in rows if r['n']>=g0 and r['G']<16]
    out[f'g0={g0}']=dict(n_types=len(sel),max_dev=max(r['dev'] for r in sel),explicit_abs=sum(r['abs'] for r in sel))
out['tail_abs_G>=16']=tail_abs
out['delta_int_bound']=out['g0=5']['explicit_abs']+tail_abs
out['ReLambda_lo']=6.23397e-4; out['ratio']=out['delta_int_bound']/out['ReLambda_lo']
out['top']=[{k:r[k] for k in ('i','j','h','s','G','n','dev','abs')} for r in sorted([r for r in rows if r['n']>=5],key=lambda r:-r['abs'])[:12]]
print(json.dumps(out,indent=1))
json.dump(out,open('/workspace/bgs-lineN/N12/logs/g_dint.json','w'),indent=1)
