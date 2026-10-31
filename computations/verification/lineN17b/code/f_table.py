# Summarise Dev/(phi m) by class: hp vs non-hp, per rho, from exact (m<=17) and d_g3dev (m=21,33,39) logs. [N]
import json,glob,os
def show(m,rows,src):
    by={}
    for r in rows:
        if not r.get('included'): continue
        k=tuple(r['rho']); by.setdefault(k,[]).append(r)
    for k,rs in by.items():
        hp=sum(r['Dev_over_phim'] for r in rs if r.get('cls')=='hp')
        oth=[r for r in rs if r.get('cls')!='hp']
        so=sum(r['Dev_over_phim'] for r in oth); neg=sum(r['Dev_over_phim'] for r in oth if r['Dev_over_phim']<0)
        mx=max([abs(r['Dev_over_phim']/r.get('main_over_phim',r.get('mainterm_over_phim'))) for r in oth] or [0])
        print(f"m={m:2d} {src:5s} rho={k}: levels={[r['d'] for r in rs]} hpDev={hp:+.4e} nonhpSum={so:+.4e} nonhpNeg={neg:+.4e} max|rel|={mx:.2e}")
for e in json.load(open('logs/b_exact_dev.json')): show(e['m'],e['rows'],'exact')
for f in sorted(glob.glob('logs/d_g3dev_m*.json')):
    e=json.load(open(f)); show(e['m'],e['rows'],'I2p')
