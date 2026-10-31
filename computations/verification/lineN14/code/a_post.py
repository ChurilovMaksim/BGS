"""N14 (A) pre-flight post-processing [N]: per-site bad-cluster activity from the exact enumeration (a_enum.jsonl).
Polymers = eps-digit clusters (internal zero-runs < g0).  Model = alpha in {1, sqrt2, 2, 2sqrt2} (fam, near0, z0_e4, z0_e4s2).
Bad clusters: all other classes with max internal zero-run < g0 (incl. alpha=4 'four', the 169+ short clusters, and every deep class).
A_bad(<=J) = 2 * sum |w|   (factor 2 per site as in Re Lambda = 2(sum Re w));  CS form per shell: (sum |r_A r_B|^2)^{3/2}.
Tail beyond J: geometric extrapolation of the last shells' ratio [H: extrapolation]."""
import json, math, sys, collections
rows=[json.loads(l) for l in open('/workspace/bgs-lineN/N14/logs/a_enum.jsonl')]
MODEL={(1,0),(0,1),(2,0),(0,2)}
J=max(r['j'] for r in rows); budget=6.23397e-4
out={'J':J,'n_classes':len(rows),'by_g0':{}}
for g0 in (2,3,4,5,6):
    S1=collections.defaultdict(float); S2=collections.defaultdict(float); n=collections.Counter(); ncoded=collections.Counter(); Sc=collections.defaultdict(float)
    for r in rows:
        if (r['a'],r['b']) in MODEL: continue
        if r['zr']>=g0: ncoded[r['j']]+=1; Sc[r['j']]+=r['absw']; continue
        S1[r['j']]+=r['absw']; S2[r['j']]+=r['rArB2']; n[r['j']]+=1
    shells=[dict(j=j,n_bad=n[j],S1=S1[j],CS=S2[j]**1.5,n_coded=ncoded[j],S_coded=Sc[j]) for j in range(J+1)]
    tot=2*sum(S1.values()); totCS=2*sum(S2[j]**1.5 for j in S2)
    # tail: ratio over last 3 shells
    rr=[S1[j]/S1[j-1] for j in range(J-2,J+1) if S1[j-1]>0]; q=max(rr) if rr else 1
    rc=[(S2[j]/S2[j-1])**1.5 for j in range(J-2,J+1) if S2[j-1]>0]; qc=max(rc) if rc else 1
    tail=2*S1[J]*q/(1-q) if q<1 else float('inf'); tailc=2*S2[J]**1.5*qc/(1-qc) if qc<1 else float('inf')
    out['by_g0'][g0]=dict(A_bad_enum=tot,A_bad_CS_enum=totCS,ratio_last=q,ratio_last_CS=qc,tail_extrap=tail,tail_extrap_CS=tailc,
        A_bad_total_est=tot+tail,frac_of_budget=(tot+tail)/budget,shells=shells,
        top=sorted([(r['absw'],r['a'],r['b'],r['word']) for r in rows if (r['a'],r['b']) not in MODEL and r['zr']<g0],reverse=True)[:12])
    print('g0',g0,'A_bad(<=J) %.4e  CS-form %.4e  last ratios %.3f / %.3f  tail %.2e / %.2e  => %.4e = %.4f of budget'%(tot,totCS,q,qc,tail,tailc,tot+tail,(tot+tail)/budget))
for s in out['by_g0'][4]['shells']: print(s)
print('top g0=4:',out['by_g0'][4]['top'][:8])
json.dump(out,open('/workspace/bgs-lineN/N14/logs/a_post.json','w'),indent=1)
