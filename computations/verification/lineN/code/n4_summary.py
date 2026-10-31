# Line N [N]: summary of n1 factorisations: congruence/rank checks; position of prime levels q | h_{3p}/7 in the bands
# (<=p^2], (p^2,p^{7/3}], (p^{7/3},p^3], (p^3,p^10], >p^10 ; "scarring fraction" phi(q)=2 log_lam(q)/r(q); h_p composite or prime.
import json, glob, math
LAM=3+2*math.sqrt(2)
recs={}
for f in sorted(glob.glob('/workspace/bgs-lineN/logs/n1_factor_P*.jsonl')):
    for l in open(f):
        r=json.loads(l); recs[r['p']]=r
bands=[('<=p^2',0,2),('p^2..p^7/3',2,7/3),('p^7/3..p^3',7/3,3),('p^3..p^10',3,10),('>p^10',10,1e9)]
tot={b[0]:0 for b in bands}; bad_cong=[]; incomplete=[]; rows=[]; scar=[]
nfac=0
for p in sorted(recs):
    r=recs[p]; row={'p':p}
    for part in ('h_p','K_p'):
        for it in r[part]['factors']:
            q=int(it['q']); 
            if q==7: continue
            if not it['prime']: incomplete.append((p,part,it['digits'])); 
            lp=it['log_p_q']
            for name,a,b in bands:
                if a<lp<=b: tot[name]+=1
            nfac+=1
            if it['prime']:
                if 'q_mod_2p' in it and (it['q_mod_2p']!=1 or it['q_mod_8'] not in (1,7)): bad_cong.append((p,q))
                rk=it.get('rank') or (p if part=='h_p' else 3*p)
                if 'rank' in it and it['rank'] not in (p,3*p): bad_cong.append((p,q,'rank',it['rank']))
                phi=2*math.log(q)/math.log(LAM)/rk
                scar.append((p,part,round(lp,2),round(phi,3)))
    row['h_p_prime']= (len(r['h_p']['factors'])==1 and r['h_p']['factors'][0]['prime'] and r['h_p']['factors'][0]['e']==1)
    rows.append(row)
print("primes p covered:",len(recs), "max p:",max(recs))
print("prime-level counts by band (excluding 7; composite cofactors counted by size):",tot," total",nfac)
print("congruence/rank failures:",bad_cong)
print("unfactored composite cofactors (p,part,digits):",incomplete)
print("h_p prime for p in:",[r['p'] for r in rows if r['h_p_prime']])
big=[s for s in scar if s[3]>=0.25]
print("prime levels with scarring fraction 2log_lam(q)/r >= 0.25 (p,part,log_p q,frac):",len(big),"of",len(scar))
print(big)
json.dump(dict(tot=tot,bad=bad_cong,incomplete=incomplete,scar=scar),open('/workspace/bgs-lineN/logs/n4_summary.json','w'),indent=1)
