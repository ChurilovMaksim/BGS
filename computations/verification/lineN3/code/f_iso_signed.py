"""N3 (F) [N]: signed vs absolute isotropic sums at c=q | h_p from saved TRACE-206 twisted sums Zhat[bx,by] (N2 d_level_split).
Isotropic lines: N(beta)=bx^2-2by^2 == 0 mod q, i.e. bx == +-r*by with r^2==2.  Reports per line:
  S_line = sum_{beta in line, beta!=0} Zhat,  A_line = sum |Zhat|, and q*D = S_line (since sum_{s!=0} Zhat(s) = q D_q),
plus the M6-relevant weighted isotropic cross piece  ((q-2)/q^2) * sum_iso Zhat  and its m-th root, and the unit-part signed sum
 sum_unit W_beta Zhat_beta (needs t_b: computed from nu0)."""
import sys, json, numpy as np
m=int(sys.argv[1]); q=int(sys.argv[2]); sg=int(sys.argv[3]) if len(sys.argv)>3 else 1
BASE=sys.argv[4] if len(sys.argv)>4 else '/workspace/bgs-lineN/N2/logs'
Zh=np.load(f'{BASE}/d_Zh_m{m}_q{q}_s{sg}.npy')
r=[x for x in range(q) if (x*x-2)%q==0]
out=dict(m=m,q=q,sg=sg,Z0=abs(Zh[0,0]))
lines={}
for rr in r:
    pts=[((rr*t)%q,t) for t in range(1,q)]
    S=sum(Zh[p] for p in pts); A=sum(abs(Zh[p]) for p in pts)
    lines[rr]=dict(S_abs=abs(S),A=A,ratio=abs(S)/A,S_over_q_rate=(abs(S)/q)**(1/m) if S!=0 else 0,A_over_q_rate=(A/q)**(1/m))
    # orbit structure: Zhat constant on lambda-orbits; number of distinct values
    vals=np.array([Zh[p] for p in pts]); out.setdefault('distinct',[]).append(int(len(np.unique(np.round(vals,6)))))
out['lines']=lines
Siso=sum(sum(Zh[((rr*t)%q,t)] for t in range(1,q)) for rr in r)
out['iso_weighted_signed']=abs((q-2)/q**2*Siso); out['iso_weighted_signed_rate']=out['iso_weighted_signed']**(1/m)
out['iso_weighted_abs_rate']=((q-2)/q**2*sum(lines[rr]['A'] for rr in r))**(1/m)
print(json.dumps(out,indent=1))
json.dump(out,open(f'logs/f_iso_signed_m{m}_q{q}_s{sg}.json','w'),indent=1)
