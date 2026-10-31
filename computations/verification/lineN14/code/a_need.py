"""N14 (A): what constant the rigorous tail needs.  Model bound (the form a lattice->collision lemma + the certified CP rate would give):
   S2(j) := sum_{shell j, bad} |r_A r_B|^2  <=  C * 2^j * (2^j)^{-beta},   beta = -2 ln(rho_bar)/ln(lam)   (n ~ log_lam N per class, two windows)
 per-site tail  T(J0) = 2 sum_{j>J0} S2(j)^{3/2}.  Needed: T(J0) <= budget_T.  Prints C_needed(J0) and the empirical C_emp(j)=S2(j)/(2^j 2^{-j beta})."""
import json, math
lam=3+2*math.sqrt(2); post=json.load(open('/workspace/bgs-lineN/N14/logs/a_post.json'))
budget=6.23397e-4; dint=1.0e-6; bT=(budget-dint)/2          # give half of the remaining budget to the tail
out={}
for rb in (0.2726,0.28,0.30):
    beta=-2*math.log(rb)/math.log(lam); e=1-beta   # S2 ~ C 2^{j e}
    if e>=0: print(rb,'no decay'); continue
    geo=lambda J0: sum(2**(1.5*j*e) for j in range(J0+1,J0+400))
    row={J0:(bT/(2*geo(J0)))**(2/3) for J0 in (8,10,12,14,16,20,25,30)}
    emp={s['j']:s['CS']**(2/3)/(2**(s['j']*e)) for s in post['by_g0']['4']['shells'] if s['CS']>0}
    out[rb]=dict(beta=beta,exp_per_shell=e,C_needed=row,C_emp=emp)
    print('rho_bar',rb,'beta %.3f  S2 ~ 2^{%.3f j}'%(beta,e)); print('  C_needed(J0):',{k:'%.3g'%v for k,v in row.items()}); print('  C_emp(j):',{k:'%.2g'%v for k,v in emp.items()})
json.dump(out,open('/workspace/bgs-lineN/N14/logs/a_need.json','w'),indent=1)
