"""N21: final delta_true = coded pairs G<=15 (Lemma C boxes) + sum_{G=16}^{Gb} box(G) + sum_{G>Gb} analytic Lemma D^T (KK=16 anchors)
+ remainder; arb sums of the stored upper bounds (each per-G value is itself an upper bound).  usage: final_delta.py Gb"""
import json, sys
from flint import arb, ctx
ctx.prec=80
Gb=int(sys.argv[1]) if len(sys.argv)>1 else 36
F=json.load(open('/workspace/bgs-lineN/N21/logs/f_postC.json')); T=json.load(open('/workspace/bgs-lineN/N21/logs/tail_DT_36_60_KK16.json'))
up=lambda a: float(a.upper())
assert all(F['count_by_G'][str(G)]==100 for G in range(16,Gb+1))
low=arb(F['coded_sum_abs_dev_upper_G_le_15'])
box={G:F['dev_by_G'][str(G)] for G in range(16,Gb+1)}
ana={int(G):v for G,v in T['T_by_G'].items() if int(G)>Gb}
assert min(ana)==Gb+1 and max(ana)==T['GMAX']
sb=sum((arb(v) for v in box.values()),arb(0)); sa=sum((arb(v) for v in ana.values()),arb(0)); rem=arb(T['remainder'])
tot=low+sb+sa+rem
out=dict(Gb=Gb,G_le_15=F['coded_sum_abs_dev_upper_G_le_15'],box_16_Gb=up(sb),analytic_Gb1_60=up(sa),remainder_G_gt_60=T['remainder'],
         delta_true_upper=up(tot),box_by_G=box,analytic_by_G=ana)
print(json.dumps({k:v for k,v in out.items() if not k.endswith('by_G')},indent=1))
json.dump(out,open('/workspace/bgs-lineN/N21/logs/final_delta.json','w'),indent=1)
