"""Referee: (1) cross-validate N14 c2_mid [CA-fp] boxes against N13 arb replay [CA] boxes on all overlapping jobs:
boxes must intersect; and the c2 midpoint error vs the arb midpoint must be << c2 radius when the arb radius is small (honesty of rad).
(2) independent recomputation of delta_int (coded) from c2_mid boxes with own interval code (mpmath iv), and of the short-type split."""
import json, mpmath as mp
mp.iv.dps=30
c2={}; 
for l in open('/workspace/bgs-lineN/N14/logs/c2_mid.jsonl'): r=json.loads(l); c2[r['k']]=r
arbr={}
for l in open('/workspace/bgs-lineN/N13/logs/c_replay.jsonl'): r=json.loads(l); arbr[r['k']]=r
res=dict(n_overlap=0,all_intersect=True,max_err_over_rad_when_arbtight=0.0,examples=[],e_match=True)
for k,ra in arbr.items():
    rc=c2.get(k)
    if rc is None: continue
    if ra['e']!=rc['e']: res['e_match']=False
    res['n_overlap']+=1
    for L in 'AB':
        a=ra[L]; c=rc[L]
        inter=all(max(a[x][0],c[x][0])<=min(a[x][1],c[x][1]) for x in ('re','im'))
        if not inter: res['all_intersect']=False; res['examples'].append((k,L))
        ma=complex(sum(a['re'])/2,sum(a['im'])/2); mc=complex(sum(c['re'])/2,sum(c['im'])/2)
        if a['rad']<c['rad']:
            res['max_err_over_rad_when_arbtight']=max(res['max_err_over_rad_when_arbtight'],abs(ma-mc)/c['rad']); res.setdefault('n_arbtight',0); res['n_arbtight']+=1
# (2) delta_int
def box(w): return mp.iv.mpc(mp.iv.mpf(w['re']),mp.iv.mpf(w['im']))
def W(r): z=box(r['A'])*box(r['B']); return z*z*z
def absup(z):
    rx=max(abs(float(z.real.a)),abs(float(z.real.b))); ix=max(abs(float(z.imag.a)),abs(float(z.imag.b)))
    return (rx*rx+ix*ix)**0.5*(1+1e-14)
S={}
for r in c2.values():
    if r['kind']=='single': S[(r['name'],0)]=W(r)
    if r['kind']=='single_eps': S[(r['name'],1)]=W(r)
tot=0.0; npair=0; byG={}
for r in c2.values():
    if r['kind']!='pair': continue
    i,j=r['name'].split('+'); d=W(r)-S[(i,0)]*S[(j,r['h'])]; u=absup(d); tot+=u; npair+=1; byG[r['G']]=byG.get(r['G'],0)+u
res.update(delta_int_coded_upper=tot,n_pairs=npair,byG=byG,radmax_c2=max(max(r['A']['rad'],r['B']['rad']) for r in c2.values()))
print(json.dumps(res,indent=1)); json.dump(res,open('logs/ref_c2_vs_arb.json','w'),indent=1)
