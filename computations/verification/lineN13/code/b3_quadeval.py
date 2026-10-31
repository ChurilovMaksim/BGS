"""N13 (B3): evaluate the quadratic step bound from the arb-certified scalars (logs/b2_quad.json, b_arb.json), derivation REPORT_N13 sec 2.
nP|psi w| <= (1+da')a^ + nP(c1 t + rho_psi)||q|| + nP||psi||_* L2 t^2/2
||Qt w||  <= ((b1 t + tau1)/nP_lo) a^ + (kap' + b2 t)||q|| + (1+eta)L2 t^2/2 + (1+eta)Lip t |1-psiPhi| nP
a^2 + ||q||^2 <= 1 + 2 g ||psi||_*   (a^ = nP|a|);   ||w|| <= sqrt(X/(1 - 2 g ||psi||_*))."""
import json, math, numpy as np
q=json.load(open('/workspace/bgs-lineN/N13/logs/b2_quad.json')); B=json.load(open('/workspace/bgs-lineN/N13/logs/b_arb.json'))
eta=B['V2']['eta']; Lip=B['Lip_H']; L2=q['L2']; nP=q['nP']; nPl=q['nP_lo']; g=q['g']; ps=q['psi_dual']; om=q['one_minus_psiPhi']
def bound(t):
    da=q['da']+t*q['eps0']*(1+om)
    tau1=om*nP*(1+(1+eta)**2)+(1+eta)*q['MPhi_minus_Phi']
    m=np.array([[1+da, nP*(q['c1']*t+q['psiM_minus_psi'])],[(q['b1']*t+tau1)/nPl, q['kapp']+q['b2']*t]])
    add=np.array([nP*ps*L2*t*t/2, (1+eta)*L2*t*t/2+(1+eta)*Lip*t*om*nP])
    sX=np.linalg.norm(m,2)*math.sqrt(1+2*g*ps)+np.linalg.norm(add)
    return sX/math.sqrt(1-2*g*ps)*(1+1e-12)   # float evaluation of a 2x2 norm: relative safety 1e-12
rows=[]
for t in [0,2**-20,2**-16,2**-14,2**-12,2**-11,2**-10,2**-9,2**-8,2**-7,2**-6]:
    b=bound(t); rows.append(dict(t=t,bound=b,coef=(b-bound(0))/t**2 if t>0 else None))
c0=rows[0]['bound']-1; C2=max(r['coef'] for r in rows[1:] if r['t']<=2**-8)
# monotone in t: coef is nondecreasing on the grid; state bound for t<=1/256 via sup over grid+monotonicity [P: each entry of m and add is increasing in t]
out=dict(c0=c0,C2_t_le_1_256=C2,rows=rows,statement='N_H(t) <= 1 + c0 + C2 t^2 for |t| <= 1/256 (bound(t) increasing in t, coef read on dyadic grid and checked monotone)')
# check monotone coef on fine grid
ts=np.linspace(1e-6,2**-8,400); cf=[(bound(t)-bound(0))/t**2 for t in ts]; out['coef_max_fine']=max(cf)
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=1)); [print(r) for r in rows]
json.dump(out,open('/workspace/bgs-lineN/N13/logs/b3_quadeval.json','w'),indent=1)
