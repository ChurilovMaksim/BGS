# referee lineN21: own aggregation of the Lemma C boxes (arb), duplicates/coverage, F21-4 medians
import json, glob, statistics as st
from flint import arb, acb
R=[json.loads(l) for f in sorted(glob.glob('/workspace/bgs-lineN/N21/logs/convC_replay_p*.jsonl')) for l in open(f)]
X=[json.loads(l) for f in sorted(glob.glob('/workspace/bgs-lineN/N21/logs/convC_ext_16_60_p*.jsonl')) for l in open(f)]
out={}
out['replay_rows']=len(R); out['replay_unique_k']=len({r['k'] for r in R}); out['ext_rows']=len(X); out['ext_unique_k']=len({r['k'] for r in X})
# ext coverage per G and uniqueness of (name,h,s,G)
from collections import Counter
cX=Counter(r['G'] for r in X); out['ext_count_by_G']={g:cX[g] for g in sorted(cX)}
out['ext_dup_keys']=len(X)-len({(r['name'],r['h'],r['s'],r['G']) for r in X})
# N15 job list equality
N15=[json.loads(l) for l in open('/workspace/bgs-lineN/N15/logs/c3_mid.jsonl')]
m15={r['k']:(r['kind'],r['name'],r['h'],r['s'],r['G'],tuple(r['e'])) for r in N15}
out['replay_matches_N15_jobs']=all(m15[r['k']]==(r['kind'],r['name'],r['h'],r['s'],r['G'],tuple(r['e'])) for r in R) and len(m15)==len(R)
def box(w):
    # own ball: midpoint +- rad on both real and imag (rad = E), widened by 2^-50 relative
    return acb(arb(w['mid'][0],w['rad']*(1+2**-40)),arb(w['mid'][1],w['rad']*(1+2**-40)))
def W(r): return (box(r['A'])*box(r['B']))**3
S={}
for r in R:
    if r['kind']=='single': S[(r['name'],0)]=W(r)
    if r['kind']=='single_eps': S[(r['name'],1)]=W(r)
tot=arb(0); byG={}
for r in R+X:
    if r['kind']!='pair': continue
    i,j=r['name'].split('+'); d=abs(W(r)-S[(i,0)]*S[(j,r['h'])])
    byG.setdefault(r['G'],arb(0)); byG[r['G']]+=d
    if r['G']<=15: tot+=d
out['sum_G_le_15_upper']=float(tot.upper())
s1636=sum((byG[g] for g in range(16,37)),arb(0)); out['sum_16_36_upper']=float(s1636.upper())
out['byG']={g:float(byG[g].upper()) for g in (15,16,36,37,44)}
# F21-4 medians / E/|r|
pr=[w for r in R if r['kind']=='pair' for w in (r['A'],r['B'])]
out['pair_median_err_pert']=st.median(w['conv']['err_pert'] for w in pr); out['pair_median_err_dPi']=st.median(w['conv']['err_dPi'] for w in pr)
er=[w['rad']/abs(complex(*w['mid'])) for w in pr]; out['pair_E_over_r_median']=st.median(er); out['pair_E_over_r_max']=max(er)
sg=[w for r in R if r['kind'] in('single','single_eps') for w in (r['A'],r['B'])]
es=[w['rad']/abs(complex(*w['mid'])) for w in sg]; out['single_E_over_r']=[min(es),max(es)]
dom=Counter(max(('rad','err_proj','err_pert','err_dPi','err_tail'),key=lambda k:w['conv'][k]) for w in pr); out['pair_dominant_term']=dict(dom)
print(json.dumps(out,indent=1)); json.dump(out,open('../logs/ref_post.json','w'),indent=1)
