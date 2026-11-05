"""research1105b: collect all level analyses into logs/final_levels.json (rerunnable; uses whatever npz exist).
Dev normalised by phi*m with phi = phi(2h_m) (frozen TRACE-206 normalisation)."""
import os, json, math, numpy as np
from sympy import totient
from analyze import assemble
from twb import mdata
L='../logs'; out={}
def phim(m): h=mdata(m)['h']; return int(totient(2*h))*m
def have(prefix,s): return os.path.exists(f'{prefix}_{s}.npz')
jobs=[]
for sg in (1,-1):
    for D in (7,23,161,353): jobs.append((33,sg,D,f'{L}/prop/m33_s{sg}_D{D}',['aa' if D==161 else 'a']))
    for D in (7,79,553,599): jobs.append((39,sg,D,f'{L}/prop/m39_s{sg}_D{D}',['aa' if D==553 else 'a']))
    jobs.append((69,sg,47,f'{L}/prop/m69_s{sg}_D47',['a']))
jobs+= [(33,1,8119,f'{L}/lvl/p11_s1',['ii','ui','iu','uu']),(33,-1,8119,f'{L}/lvl/p11_sm1',['ii','ui']),
        (39,1,47321,f'{L}/lvl/p13_s1',['ii','ui','iu','uu']),(51,1,1607521,f'{L}/lvl/p17_s1',['ii','iu','ui','uu'])]
for m,sg,D,pre,specs in jobs:
    sp=[s for s in specs if have(pre,s)]
    if not sp: continue
    # assemble needs at least one exact class for E; if only sampled classes exist, report component means only
    try: r=assemble(m,sg,D,pre,sp)
    except Exception as e: out[f'm{m}_s{sg}_D{D}']=dict(error=str(e)); continue
    pm=phim(m); r['phim']=pm; r['Dev_over_phim']=r['Dev_exact']/pm; r['Z0abs2_over_phim']=r['Z0abs2']/pm
    r['gas_scale_main_over_phim']=r['n']*r['Z0abs2']/D**2/pm; r['specs_used']=sp
    out[f'm{m}_s{sg}_D{D}']=r
    print(f"m{m} s{sg} D{D} {sp}: Dev/phim={r['Dev_over_phim']:.4e} dev/main={r['dev_over_main_exact']:.4e} meanE={r['meanE'][0]:.3e}{r['meanE'][1]:+.3e}i var={r['varE_exact']:.2e}",flush=True)
json.dump(out,open(f'{L}/final_levels.json','w'),indent=1,default=str)
