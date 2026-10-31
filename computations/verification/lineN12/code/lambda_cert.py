"""N11-F3 archive: Re Lambda_lo from the archived N8/N9 arb enclosures (exact rational arithmetic on the stored float bounds).
Re Lambda >= 2(Re_w_lo[fam] + Re_w_lo[near0] + Re_w_lo[z0_e4]) - 2|w(e4s2)|_up   [CA: certified listed activities; identification
with the gas Lambda is model-level, N11-F3].  Also: budget with the uncertified type-4 activity c16 (|.|~2.2e-9, charged x10 = 2.2e-8 per
sign pair) and the N11-F4 corrected bound 2(1+ReL)^p e^{-p delta} - 1."""
import json
from fractions import Fraction as F
L='/workspace/bgs-lineN/'
f=lambda p,k: F(json.load(open(L+p))[k])
fam=f('N8/logs/n8_cert_fam.json','Re_w_lower'); n0=f('N8/logs/n8_cert_near0.json','Re_w_lower')
z4=f('N9/logs/n9_cert_z0_e4.json','Re_w_lower'); e4s2=f('N9/logs/n9_cert_z0_e4s2.json','absw_upper')
ReL=2*(fam+n0+z4)-2*e4s2
print('certified ReL_lo =',float(ReL))
c16=F(22,10**9); ReL2=ReL-2*10*c16
print('with c16 charged (2*10*2.2e-9):',float(ReL2))
out=dict(ReL_lo=float(ReL),ReL_lo_c16=float(ReL2),rows=[])
for p in [29,47,75,101,200,500,1289,2000,5000,10000]:
    for d in [0,1e-5,1e-4]:
        b=2*(1+float(ReL2))**p*__import__('math').exp(-p*d)-1
        out['rows'].append(dict(p=p,delta_int=d,lower_abs_1pX=b))
    print(p,'|1+X_gas| >= 2(1+ReL)^p e^{-p d} - 1 :',[round(r['lower_abs_1pX'],5) for r in out['rows'][-3:]])
# F4: smallest p with bracket base^2 >= 1.2 at delta_int=0 and no tail (Theorem N11 needs (base)^2-1 > 0.2)
import math
p=3
while (2*(1+float(ReL2))**p-1)**2-1<=0.2: p+=2
out['p_min_bracket']=p; print('bracket alone needs p >=',p)
json.dump(out,open('/workspace/bgs-lineN/N12/logs/lambda_cert.json','w'),indent=1)
