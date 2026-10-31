# Non-h_p Dev in units of S_rho/m = |Z_rho|^2/(phi m h_p) (the h_p-gain scale), from d_g3dev logs + exact m=15. [N]
import json,glob
HP={15:41,21:239,33:8119,39:47321}
rows=[]
for e in json.load(open('logs/b_exact_dev.json')):
    if e['m']==15: rows+= [dict(r,m=15,main_over_phim=r.get('mainterm_over_phim')) for r in e['rows'] if r.get('included')]
for f in sorted(glob.glob('logs/d_g3dev_m*.json')):
    e=json.load(open(f))
    if e['m']!=15: rows+=[dict(r,m=e['m']) for r in e['rows']]
import sys
try:
    for l in open('logs/d39.out'):
        r=json.loads(l); r['m']=39
        if not any(x['m']==39 and x['d']==r['d'] and x['rho']==r['rho'] for x in rows): rows.append(r)
except Exception as ex: print('d39 partial',ex)
print("| m | ρ | d | class | Dev/(φm) | Dev/main | Dev/(S_ρ/m) |"); print("|---|---|---|---|---|---|---|")
for r in sorted(rows,key=lambda r:(r['m'],r['rho'],r['d'])):
    Sm=r['main_over_phim']*r['d']**2/r['n_d']/HP[r['m']]
    print(f"| {r['m']} | ({r['rho'][0]},{r['rho'][1]}) | {r['d']} | {r.get('cls')} | {r['Dev_over_phim']:+.3e} | {r['Dev_over_phim']/r['main_over_phim']:+.1e} | {r['Dev_over_phim']/Sm:+.2e} |")
