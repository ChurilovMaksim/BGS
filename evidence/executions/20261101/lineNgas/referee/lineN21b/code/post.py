import json,glob
N15=json.load(open('/workspace/bgs-lineN/N15/logs/nh_table_rig_2048.json'))
rows={}
for f in glob.glob('logs/nh_fp_p*.jsonl'):
    for l in open(f): r=json.loads(l); rows[r['k']]=r
NC=2048;h=N15['h'];LIP=167.19672738313594;LIPN13=N15['Lip_H']
assert len(rows)==NC
used=set(json.load(open('logs/used_cells.json'))['cells'])
arb={}
for f in ['logs/nh_arb_cells_partial.jsonl','logs/nh_arb_test3.jsonl']:
    for l in open(f):
        r=json.loads(l); arb[r['k']]=r.get('center_up',r.get('centre_up'))
def inner(k):  # cell fully within |t|<=1/256
    a=-0.5+k*h;b=a+h;return a>=-1/256 and b<=1/256
out={}
for name,L in [('Lip_ref',LIP),('Lip_N13',LIPN13)]:
    for sel_name,sel in [('all',range(NC)),('|t|>1/256',[k for k in range(NC) if not inner(k)]),('used946',sorted(used))]:
        b={k:rows[k]['centre_up']+L*h/2 for k in sel}
        marg={k:N15['bound'][k]-b[k] for k in sel}
        km=max(b,key=b.get);kmin=min(marg,key=marg.get)
        out[f'{name}/{sel_name}']=dict(n=len(sel),max=b[km],k_max=km,t_max=-0.5+(km+0.5)*h,
          min_margin=marg[kmin],k_minmargin=kmin,n_exceed=sum(1 for k in sel if marg[k]<0))
ac={k:dict(arb=arb[k],fp=rows[k]['centre_up'],fp_minus_arb=rows[k]['centre_up']-arb[k]) for k in arb if arb[k] is not None}
out['arb_crosscheck']=ac
out['arb_all_fp_ge_arb']=all(v['fp_minus_arb']>=0 for v in ac.values())
out['N15_max']=N15['max'];out['dS_max']=max(r['dS'] for r in rows.values())
out['n_inner_excluded']=sum(inner(k) for k in range(NC)); out['used_inner']=sorted(k for k in used if inner(k))
json.dump(out,open('logs/post.json','w'),indent=1);print(json.dumps(out,indent=1))
