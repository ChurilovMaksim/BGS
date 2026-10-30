"""F_m/2m  vs  RMT(=(B^sym+2m chi)/2m ≈ 2) + explicit resonance sum (primaries P* = ±N≡4, ±N≡8 and their dilutions d|h, d<=sqrt h,
using the Gauss main term n_d |Z_rho|^2/d^2), all from class sums at m<=15."""
import math, numpy as np, json, sys
from law import mdata
from step1b import Z2all, load
from step1c import divisors
kick=sys.argv[1]
Pst=[(2,8),(-2,8),(2,16),(-2,16)] if kick=='k1' else [(2,392),(-2,392),(2,784),(-2,784)]
rows=[]
for m in ([int(x) for x in sys.argv[2].split(',')] if len(sys.argv)>2 else [9,11,13,15]):
    T=load(kick,m); h=mdata(m)['h']; Z=dict(Z2all(T,m)); phi=len(Z); F=sum(Z.values())/phi
    RMT=(2*m-m*m/h+2*m)  # B^sym ≈ 2m - m^2/h (TRACE-165 Thm D leading term), chi=1 (even kick; for full kick chi≈1 assumed)
    res_pred=0; res_act=0; nres=0
    for a,b in Pst:
        p=[nu for nu in Z if (b*nu-a)%(2*h)==0]
        if not p:
            # virtual primary (e.g. 7|h for the 49-images): count the level-d families' actual excess only (|Z|^2 > 4m*10)
            for d in divisors(h):
                if d==1 or d*d>h: continue
                M=2*h//d
                mem=[nu for nu in Z if (b*nu-a)%M==0 and all((b*nu-a)%(2*h//dd)!=0 for dd in divisors(d) if dd<d)]
                big=[n for n in mem if Z[n]>40*m]
                if len(big)>len(mem)//2:
                    ex=sum(Z[n]-RMT for n in mem); res_act+=ex; res_pred+=ex; nres+=len(mem)
            continue
        Z0=Z[p[0]]; res_pred+=Z0-RMT; res_act+=Z0-RMT; nres+=1
        for d in divisors(h):
            if d==1 or d*d>h: continue
            M=2*h//d
            mem=[nu for nu in Z if (b*nu-a)%M==0 and all((b*nu-a)%(2*h//dd)!=0 for dd in divisors(d) if dd<d)]
            if Z0/d/d < 4*m: continue   # only resonant if main term exceeds the bulk scale
            res_pred+=len(mem)*(Z0/d/d-RMT); res_act+=sum(Z[n]-RMT for n in mem); nres+=len(mem)
    W=F-RMT; Wp_pred=W-res_pred/phi; Wp_act=W-res_act/phi
    r=dict(m=m,F2m=F/(2*m),RMT2m=RMT/(2*m),Res_pred_2m=res_pred/phi/(2*m),Res_act_2m=res_act/phi/(2*m),Wrest_over_m=W/m,Wprime_pred_over_m=Wp_pred/m,Wprime_act_over_m=Wp_act/m,n_res=nres)
    rows.append(r); print(' '.join(f'{k}={v:.4f}' if isinstance(v,float) else f'{k}={v}' for k,v in r.items()))
json.dump(rows,open(f'../logs/formula_table_{kick}'+('' if len(sys.argv)<=2 else '_'+sys.argv[2].replace(',','_'))+'.json','w'))
