"""research1105b [CA, exact]: N_{Q(zeta_p)/Q}(eta_s) = h_p for eta_s = z - 1 - 2 s z^{(p+1)/2}, s=+-1 (Binet generator),
and N(z^2-6z+1) = h_p^2... (full-level kernel eta_+ eta_-).  Exact resultants with Phi_p (python-flint fmpz_poly)."""
import json, flint
from twist_core import hp
out=[]
for p in [5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73]:
    Phi=flint.fmpz_poly([1]*p)
    row=dict(p=p,h=hp(p))
    for s in (1,-1):
        c=[0]*((p+1)//2+1); c[0]=-1; c[1]+=1; c[(p+1)//2]+=-2*s
        row[f'N_eta_{s}']=int(flint.fmpz_poly(c).resultant(Phi)) if hasattr(flint.fmpz_poly,'resultant') else None
    row['N_kernel']=int(flint.fmpz_poly([1,-6,1]).resultant(Phi)) if hasattr(flint.fmpz_poly,'resultant') else None
    row['ok']=abs(row['N_eta_1'])==row['h'] and abs(row['N_eta_-1'])==row['h']
    out.append(row); print(p,row['ok'],row['N_eta_1']//row['h'] if row['N_eta_1'] else None,row['N_eta_-1']//row['h'],row['N_kernel']//row['h']**2 if row['N_kernel'] else None)
json.dump(out,open('/workspace/research1105b/logs/eta_norm.json','w'),indent=1)
