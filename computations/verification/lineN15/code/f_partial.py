"""N15 (0): partial N13 arb replay (597 jobs, stopped) -- N13 f_post formulas via N14 f_post2 on the partial set, plus job-by-job
cross-check against N14 c2_mid ([CA-fp]): the two certified boxes must intersect for every window; reports overlap and radius ratios."""
import json, subprocess, sys
src='/workspace/bgs-lineN/N13/logs/c_replay.jsonl'
subprocess.run([sys.executable,'/workspace/bgs-lineN/N14/code/f_post2.py',src,'/workspace/bgs-lineN/N15/logs/f_post_partial.json'],check=True,stdout=subprocess.DEVNULL)
arb={json.loads(l)['k']:json.loads(l) for l in open(src)}
mid={json.loads(l)['k']:json.loads(l) for l in open('/workspace/bgs-lineN/N14/logs/c2_mid.jsonl')}
bad=0; n=0; rr=[]; byG={}
for k,a in arb.items():
    m=mid[k]; assert m['e']==a['e']
    for W in 'AB':
        n+=1
        for c in ('re','im'):
            lo=max(a[W][c][0],m[W][c][0]); hi=min(a[W][c][1],m[W][c][1])
            if lo>hi: bad+=1
        rr.append(a[W]['rad']/m[W]['rad']); byG.setdefault(a['G'],[]).append(a[W]['rad']/m[W]['rad'])
fp=json.load(open('/workspace/bgs-lineN/N15/logs/f_post_partial.json'))
out=dict(jobs=len(arb),windows=n,disjoint_components=bad,arb_over_mid_rad_median=sorted(rr)[len(rr)//2],arb_over_mid_rad_max_by_G={g:max(v) for g,v in sorted(byG.items())},
         f_post_partial={k:fp[k] for k in ('coded_pairs','coded_sum_abs_dev_upper','coded_sum_abs_dev_mid','short_types')})
# same subset from c2_mid
sub=[mid[k] for k in arb]; json.dump(out,open('/workspace/bgs-lineN/N15/logs/f_partial.json','w'),indent=1); print(json.dumps(out,indent=1))
