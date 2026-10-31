"""K2-F1: explicit S_Z = sum_{rho in P*} C_rho^2 with |Z_rho(m)| <= C_rho * mu^m, mu = 1.9154753 (upper end of |mu*|), for m >= 495.
P* = {(2,8),(-2,8),(2,16),(-2,16)} (TRACE-206 frozen mask: resonance_classification_lineG.md line 107 'P* = {(2,8),(-2,8),(2,16),(-2,16)}
(N = +-4, +-8)' at repo fa172e82; Line I implementation bgs-lineI/code/base.py PSTAR['k1']).
(+-2,8): Line F [CA]: Z = c_m (c^f mu*^m + eps), |c^f| = 1/2, |eps| <= H0 = 1506.18, |c_m| <= 1 + lam^-m  (Line J v2 §Z0).
(+-2,16): J3 §1 + Lemma L16 [CA, accepted]: Z = (1-lam^-m) sum_B [tr(J_B V_B^m) - tr(J_B E_B^m)], each term <= C_{B,T} R_{B,T}^m with
C = (1/2)||T||_1 fullR/(1-F) from the stored rig_spec 'rest' certificates (same formula as J3 code/assemble16.py, read-only)."""
import json, os
from flint import arb, ctx
ctx.prec=128
J3='/workspace/bgs-lineJ/J3'
reps=json.load(open(f'{J3}/logs/blocks16_reps.json')); mem=reps['members']
def bound(T,r,kind,b):
    c=json.load(open(f'{J3}/logs/cert/{T}_r{r}_{kind}_b{b}_rest.json')); assert c['certified'] and c['mode']=='rest'
    B=json.load(open(f'{J3}/data/cert/{T}_r{r}_{kind}.json'))
    R=arb(c['R']); SY=arb(c['SY_R'])*(1+arb(2)**-40); kap=arb(c['kappa_str'].split('+/-')[0].strip('[ ]'))+arb('1e-18')
    Xn=arb(B['Xnorm'])*(1+arb(2)**-40); F=arb(c['F_R2'])*(1+arb(2)**-40); assert F<1
    fullR=(kap*SY+1/R)*(1+Xn/R)+1/R
    return R, arb(B['trace_norm'])*(1+arb(2)**-40)/2*fullR/(1-F)
cases={}
for r,lst in mem.items():
    for (case,blk) in lst: cases.setdefault(case,[]).append(int(r))
mu=arb('1.9154753'); lam=3+2*arb(2).sqrt(); M=495
C16=arb(0); Rmax=arb(0)
for case,rs in cases.items():
    tot=arb(0)
    for r in rs:
        for T in 'VE':
            R,C=bound(T,r,'u',0); Rmax=arb.max(Rmax,R)
            assert R<mu
            tot+=C          # R^m <= mu^m ; (1-lam^-m) <= 1
    C16=arb.max(C16,tot)
C8=(1+lam**(-M))*(arb('0.5')+arb('1506.18')*arb('1.9154712')**(-M))   # m >= 495; mu*^m >= 1.9154712^m
# for m>=M, (R16/mu)^m <= (Rmax/mu)^M : use sharper bound C16 (Rmax/mu)^M as the effective coefficient
C16eff=C16*(Rmax/mu)**M
SZ=2*C8**2+2*C16eff**2
SZ_crude=2*C8**2+2*C16**2
out=dict(P_star=['(2,8)','(-2,8)','(2,16)','(-2,16)'],m_min=M,C8_upper=float(C8.upper()),C16_upper=float(C16.upper()),R16_max=float(Rmax.upper()),
         C16eff_upper=float(C16eff.upper()),S_Z_upper=float(SZ.upper()),S_Z_crude_upper=float(SZ_crude.upper()))
print(json.dumps(out,indent=1)); json.dump(out,open('logs/k2_SZ.json','w'),indent=1)
