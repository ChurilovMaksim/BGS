"""Line L3 [N] check of the cusp-excursion lemma: max run of consecutive i with |tau_i| (dist to Z) <= eps,
for all beta on isotropic lines and all non-isotropic beta (small q), vs log_lam q."""
import sys, math, json; sys.path.insert(0,'/workspace/bgs-lineL/L2/code')
from twlaw import lam_pows, taus_of, LAM
out=[]
for (m,q) in [(15,41),(21,239),(33,353),(39,599),(21,4663),(51,15607)]:
    pw=lam_pows(m,q); s=next(x for x in range(q) if (x*x-2)%q==0); eps=0.05
    def run(b):
        t=taus_of(b,pw,q); t=t+t  # cyclic
        best=cur=0
        for x in t:
            d=min(x,1-x)
            cur=cur+1 if d<=eps else 0; best=max(best,cur)
        return min(best,m)
    iso=max(run(((u*s)%q,u)) for u in range(1,q))
    non=max(run((bx,by)) for bx in range(min(q,400)) for by in range(min(q,400)) if (bx*bx-2*by*by)%q and (bx,by)!=(0,0)) if q<=5000 else None
    r=dict(m=m,q=q,eps=eps,log_lam_q=math.log(q)/math.log(LAM),bound_iso=math.log(q/eps**2)/math.log(LAM),max_run_iso=iso,max_run_noniso_sampled=non)
    print(r,flush=True); out.append(r)
json.dump(out,open('/workspace/bgs-lineL/L3/logs/excursion_check.json','w'),indent=1)
