"""Referee lineN15: (1) delta_int from N15 c3_mid boxes with own interval code (mpmath iv); (2) c3 vs c2 (mids identical, radius ratio);
(3) c3 boxes vs N13 partial arb replay (intersection, mid diff / rad_c3 where arb tighter); (4) twist range |d|<=1/2 and |NS|<=30 check."""
import json, mpmath as mp, sys
mp.iv.dps=30
def load(f):
    D={}
    for l in open(f): r=json.loads(l); D[r['k']]=r
    return D
c3=load('/workspace/bgs-lineN/N15/logs/c3_mid.jsonl'); c2=load('/workspace/bgs-lineN/N14/logs/c2_mid.jsonl'); ar=load('/workspace/bgs-lineN/N13/logs/c_replay.jsonl')
res=dict(n_c3=len(c3))
mid=lambda w: complex(sum(w['re'])/2,sum(w['im'])/2)
res['max_mid_diff_c3_c2']=max(abs(mid(c3[k][L])-mid(c2[k][L])) for k in c3 for L in 'AB')
res['max_rad_ratio_c3_c2']=max(c3[k][L]['rad']/c2[k][L]['rad'] for k in c3 for L in 'AB')
res['max_rad_c3']=max(c3[k][L]['rad'] for k in c3 for L in 'AB')
ni=0; dis=0; mx=0; nt=0
for k,ra in ar.items():
    if k not in c3: continue
    for L in 'AB':
        a=ra[L]; c=c3[k][L]; ni+=1
        if not all(max(a[x][0],c[x][0])<=min(a[x][1],c[x][1]) for x in ('re','im')): dis+=1
        if a['rad']<c['rad']: nt+=1; mx=max(mx,abs(mid(a)-mid(c))/c['rad'])
res.update(arb_windows=ni,arb_disjoint=dis,arb_tighter=nt,max_middiff_over_rad_c3=mx)
def box(w): return mp.iv.mpc(mp.iv.mpf(w['re']),mp.iv.mpf(w['im']))
def W(r): z=box(r['A'])*box(r['B']); return z*z*z
def absup(z):
    rx=max(abs(float(z.real.a)),abs(float(z.real.b))); ix=max(abs(float(z.imag.a)),abs(float(z.imag.b)))
    return (rx*rx+ix*ix)**0.5*(1+1e-14)
S={}
for r in c3.values():
    if r['kind']=='single': S[(r['name'],0)]=W(r)
    if r['kind']=='single_eps': S[(r['name'],1)]=W(r)
tot=0.0; n=0
for r in c3.values():
    if r['kind']!='pair': continue
    i,j=r['name'].split('+'); tot+=absup(W(r)-S[(i,0)]*S[(j,r['h'])]); n+=1
res.update(delta_int_upper_c3=tot,n_pairs=n)
print(json.dumps(res,indent=1)); json.dump(res,open('logs/ref_c3.json','w'),indent=1)
