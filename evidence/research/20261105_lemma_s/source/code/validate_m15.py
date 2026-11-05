"""Independent check of the level pipeline (twisted law + I2' + member set) against the EXACT all-unit |Z_15(nu)|^2
class-sum table (Line G orbit-canonical C code, k1 kick): Dev_d(rho) for rho=(+-2,8) at prime levels d=7,31,41 (squarefree D only)."""
import sys, json, subprocess, numpy as np, math
sys.path.insert(0,'/workspace/audit/pr60/computations/verification/lineI/code')
from base import load_T, Z2_all
sys.path.insert(0,'/workspace/research1105b/code'); from analyze import assemble
m=15; nu,Z=Z2_all(load_T('k1',m),m); 
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import nu_rho
out=[]
for sg in (1,-1):
    h,nu0=nu_rho(m,sg); M=2*h
    for D in (7,31,41):
        pre=f'/workspace/research1105b/logs/val/m15_s{sg}_D{D}'
        subprocess.run(['/workspace/lineNgas/venv/bin/python','/workspace/research1105b/code/level.py',str(m),str(sg),str(D),'a',pre],check=True,capture_output=True)
        r=assemble(m,sg,D,pre,['a'])
        # exact: members nu0+(2h/D)j, gcd(j,D)=1, unit
        idx={int(x):i for i,x in enumerate(nu)}
        i0=idx[nu0]; Z0e=Z[i0]; S=0; nn=0
        for j in range(1,D):
            if math.gcd(j,D)!=1: continue
            v=(nu0+(M//D)*j)%M
            if math.gcd(v,M)!=1: continue
            S+=Z[idx[v]]; nn+=1
        dev_ex=S-nn*Z0e/D/D
        row=dict(sg=sg,D=D,n=nn,n_pipe=r['n'],Z0abs2_exact=float(Z0e),Z0abs2_law=r['Z0abs2'],Dev_exact=float(dev_ex),Dev_law=r['Dev'],
                 rel_dev_exact=float(dev_ex/(nn*Z0e/D/D)),rel_dev_law=r['dev_over_main'])
        print(json.dumps(row),flush=True); out.append(row)
json.dump(out,open('/workspace/research1105b/logs/validate_m15.json','w'),indent=1)
