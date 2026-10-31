# Line N [P-arith]: scarring threshold theta_F = ((1-delta_F/2) target_F / mu)^{2k} of Theorem N3 for the (+-2,8) families,
# mu = |mu*| lower value 1.91547 (Line F standing input; toy untwisted rate 1.9154732 in logs/n5_slow_toy.log).
# Also: index of conductor-h_p points in Fix(T^p): [ (4 sqrt2 h_p)^{-1} O : h_p^{-1} O ] = N(4 sqrt2) = 32.
import json, math
rows=[json.loads(l) for l in open('/workspace/bgs-lineL/logs/final_constants.jsonl')]
mu=1.91547; LAM=3+2*math.sqrt(2)
for r in rows:
    if r['fam']!='8': continue
    k=r['k']; d=r['delta']; tgt=1.28359
    th=((1-d/2)*tgt/mu)**(2*k)
    print(json.dumps(dict(fam=r['fam']+r['typ'],k=k,delta=d,theta=th,
        rank3p_threshold_log_lam_c_over_p=th*3/2, rank_p_threshold_log_lam_c_over_p=th/2)))
print("N(4 sqrt2) =",(4**2)*2)
print("heuristic slow-beta weighted base (mu^3/lam)^(1/3) =",(mu**3/LAM)**(1/3))
