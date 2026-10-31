"""lineN16 referee: recompute N16 aggregates from the authors' jsonl (no reliance on their unarchived post-processing).
(a) A_bad true vs core on j<=10 classes (a_post rule: drop MODEL classes and zr>=g0);  (b) dev_by_G sum and flatness;
(c) E/|r| statistics and dominance of err_dPi;  (d) consistency of replay rows with c3_mid mids."""
import json, collections, math
B='/workspace/bgs-lineN/'
MODEL={(1,0),(0,1),(2,0),(0,2)}
tru=[json.loads(l) for l in open(B+'N16/logs/conv_vec_classes.jsonl')]
core=[json.loads(l) for l in open(B+'N15/logs/a_cert3.jsonl')]
ck={(r['j'],r['a'],r['b'],r['zr']):r for r in core}
out={}
for g0 in (2,4,6):
    St=sum(r['absw_up'] for r in tru if (r['a'],r['b']) not in MODEL and r['zr']<g0)
    keys=[(r['j'],r['a'],r['b'],r['zr']) for r in tru]
    Sc=sum(ck[k]['absw_up'] for k,r in zip(keys,tru) if (r['a'],r['b']) not in MODEL and r['zr']<g0 and k in ck)
    miss=sum(1 for k in keys if k not in ck)
    out[f'g0={g0}']=dict(true=2*St,core_same=2*Sc,ratio=St/Sc,missing=miss)
cnt=collections.Counter(r['j'] for r in tru); out['shells_true']=dict(cnt)
cc=collections.Counter(r['j'] for r in core); out['shells_core']=dict(cc)
# core j=11,12 contribution at g0=4
out['core_j11_12_g0_4']=2*sum(r['absw_up'] for r in core if r['j'] in (11,12) and (r['a'],r['b']) not in MODEL and r['zr']<4)
out['core_total_g0_4']=2*sum(r['absw_up'] for r in core if (r['a'],r['b']) not in MODEL and r['zr']<4)
f=json.load(open(B+'N16/logs/f_post_true.json'))
dG={int(k):v for k,v in f['dev_by_G'].items()}
out['dev_by_G_sum']=sum(dG.values()); out['coded_upper']=f['coded_sum_abs_dev_upper']
out['dev_by_G']=dict(sorted(dG.items()))
rep=[json.loads(l) for l in open(B+'N16/logs/conv_vec_replay.jsonl')]
mid=[json.loads(l) for l in open(B+'N15/logs/c3_mid.jsonl')]
rel=[];dom=0;tot=0;rel_s=[];mism=0
for rw,m in zip(rep,mid):
    for W in 'AB':
        x=rw[W]; r=complex(sum(x['re'])/2,sum(x['im'])/2); E=x['rad']; c=x['conv']
        rel.append(E/abs(r));tot+=1
        if c['err_dPi']>0.5*E: dom+=1
        if rw['kind']=='single': rel_s.append(E/abs(r))
        mm=m[W]; rm=complex(sum(mm['re'])/2,sum(mm['im'])/2)
        if abs(rm-r)>1e-12*max(1,abs(r)): mism+=1
out['E_over_r']=dict(max=max(rel),median=sorted(rel)[len(rel)//2],singles_median=sorted(rel_s)[len(rel_s)//2] if rel_s else None,
                     frac_dPi_dominant=dom/tot,mid_mismatch_vs_c3=mism,n=tot)
json.dump(out,open('/workspace/audit/lineN16/logs/ref_n16_post.json','w'),indent=1); print(json.dumps(out,indent=1))
# (e) which term dominates E, by kind
dom=collections.defaultdict(collections.Counter)
for rw in rep:
    for W in 'AB':
        c=rw[W]['conv']; r=complex(sum(rw[W]['re'])/2,sum(rw[W]['im'])/2)
        terms=dict(rad_c3=c['rad_c3'],r_scale=abs(r)*c['scale'],proj=c['err_proj'],dPi=c['err_dPi'],tail=c['err_tail'])
        dom[rw['kind']][max(terms,key=terms.get)]+=1
out['dominant_term_by_kind']={k:dict(v) for k,v in dom.items()}
print(out['dominant_term_by_kind'])
json.dump(out,open('/workspace/audit/lineN16/logs/ref_n16_post.json','w'),indent=1)
# (f) pairs: per-G medians of E components and of the pure-rounding c3 radius (N15)
pg=collections.defaultdict(list)
for rw,m in zip(rep,mid):
    if rw['kind']!='pair': continue
    for W in 'AB':
        c=rw[W]['conv']; pg[rw['G']].append((rw[W]['rad'],c['rad_c3'],c['err_dPi'],max(m[W]['rad']) if isinstance(m[W]['rad'],list) else m[W]['rad'],abs(complex(sum(rw[W]['re'])/2,sum(rw[W]['im'])/2))))
tab={}
for G,L in sorted(pg.items()):
    med=lambda i: sorted(x[i] for x in L)[len(L)//2]
    tab[G]=dict(n=len(L),E=med(0),rad_c3_true=med(1),dPi=med(2),rad_c3_N15=med(3),absr=med(4))
out['pairs_by_G']=tab
for G,t in tab.items(): print(G,{k:('%.3g'%v) for k,v in t.items()})
json.dump(out,open('/workspace/audit/lineN16/logs/ref_n16_post.json','w'),indent=1)
