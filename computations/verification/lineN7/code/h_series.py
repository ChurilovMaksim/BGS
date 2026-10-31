"""N7 [N]: depth-shell sums of |w| for the isotropic classes at q = h_p from e_isodepth3 logs (one representative per ideal class, sg=+1).
Ratio to Re w_fam (same multiplicity per class: 2 lines x 2p points)."""
import json, sys, math, glob
for f in sorted(glob.glob('/workspace/bgs-lineN/N7/logs/e_isodepth3_p*_K*_*.json')):
    d=json.load(open(f)); R=[r for r in d['res'] if r['sg']==1]
    fam=next(r for r in json.load(open('/workspace/bgs-lineN/N7/logs/e_isodepth_p29_K60.json'))['res'] if r['N']==1 and r['sg']==1)['r'][0]
    shells={}
    for r in R:
        a=math.hypot(*r['r']); j=int(math.log2(r['N'])); s=shells.setdefault(j,[0,0.0,0.0,0.0]); s[0]+=1; s[1]+=a; s[2]=max(s[2],a); s[3]+=r['r'][0]
    print(f.split('/')[-1],'Re w_fam(base1/4)=%.5e'%fam)
    tot=0; totre=0
    for j in sorted(shells):
        c,sa,mx,sre=shells[j]
        if not (j==0 and f.endswith('_q.json')): tot+=sa; totre+=sre
        print(' N in [%5d,%5d): classes %3d  sum|w| %.3e  max|w| %.3e  sum Re w %+.3e'%(2**j,2**(j+1),c,sa,mx,sre))
    print(' non-family total sum|w| = %.4e  (= %.4f of Re w_fam);  sum Re w = %+.4e'%(tot,tot/fam,totre))
