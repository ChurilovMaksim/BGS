"""J3 (a): rigorous bound for the (±2,16) members' d=7 contribution D7^{(16)} = sum_rho (cross_rho + sq_rho) [CA].
Inputs: rig_spec 'rest' certificates for all 32 distinct (sign, block) factors x {V,E} x {untwisted, 8 classes} (logs/cert/*_rest.json)
and build JSONs (trace-norm bound ||T||_1, ||X||).  Per certificate: sup_{|z|=R} ||(z-T)^-1|| <= fullR/(1-F), fullR = (kap SY + 1/R)(1+Xn/R) + 1/R
(the quantity rig_spec certifies F = pert*fullR < 1 with), hence ||T^{m-1}|| <= R^m fullR/(1-F) (Cauchy) and
|tr((J (x) P0) T^m)| <= ||J|| ||T||_1 ||T^{m-1}|| <= (1/2) ||T||_1 R^m fullR/(1-F)   (||J||_2 <= ||J||_F = 1/2, exact, blocks16_exact).
Read-out per case: Z = (1-lam^-m) sum_{8 blocks} [tr_J V^m - tr_J E^m] (same lifted trace identity as Lines F/I, TRACE-197, with the
finite factor = exact invariant block; numerically validated by wordtest16 for the finite part).  |W_C| <= 36/49 crude (n<=6 members,
|G_t(0)|=7, |sum_{beta in C} G_t(beta)| <= 42).  sq <= 6 ((6/7) sum_C |Zhat_C|)^2 per rho (Prop I2').
Output: rates, constants and M16 = least m with E16(m) <= eps (K_min/2) xi_lo^m for all larger m (eps = 1/2, 1/10)."""
import json, glob, os
from flint import arb, ctx
ctx.prec=128
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
reps=json.load(open('logs/blocks16_reps.json')); mem=reps['members']
CL=['1:3','2:1','0:1','1:2','1:5','0:3','1:0','0:2']
def bound(T,r,kind,b):
    c=json.load(open(f'logs/cert/{T}_r{r}_{kind}_b{b}_rest.json')); assert c['certified'] and c['mode']=='rest'
    B=json.load(open(f'data/cert/{T}_r{r}_{kind}.json'))
    assert c['build_json_sha256'] if 'build_json_sha256' in c else True
    R=arb(c['R']); SY=arb(c['SY_R'])*(1+arb(2)**-40); kap=arb(c['kappa_str'].split('+/-')[0].strip('[ ]'))+arb('1e-18')
    Xn=arb(B['Xnorm'])*(1+arb(2)**-40); F=arb(c['F_R2'])*(1+arb(2)**-40); assert F<1
    fullR=(kap*SY+1/R)*(1+Xn/R)+1/R
    C=arb(B['trace_norm'])*(1+arb(2)**-40)/2*fullR/(1-F)
    return R,C
cases={}
for r,lst in mem.items():
    for (case,blk) in lst: cases.setdefault(case,[]).append(int(r))
assert len(cases)==16 and all(len(v)==8 for v in cases.values())
data={}
for r in range(32):
    for T in ('V','E'):
        data[(r,T,'u')]=bound(T,r,'u',0)
        for j,c in enumerate(CL): data[(r,T,c)]=bound(T,r,'t',j)
Ru=max(max(data[(r,T,'u')][0] for T in 'VE') for r in range(32)); Rt=max(max(data[(r,T,c)][0] for T in 'VE' for c in CL) for r in range(32))
LAM=3+2*arb(2).sqrt(); XI=arb('2.4586893')   # xi_lo from Line J assembly (rounded down)
A=json.load(open('../logs/assemble_v2.json')); Kmin=min(min(x['K_plus'],x['K_minus']) for x in A['residues'])
Kmin=arb(Kmin)*(1-arb('1e-6'))
def E16(m,case):
    Zb=sum((data[(r,T,'u')][1]*data[(r,T,'u')][0]**m for r in cases[case] for T in 'VE'),arb(0))
    Zh=[sum((data[(r,T,c)][1]*data[(r,T,c)][0]**m for r in cases[case] for T in 'VE'),arb(0)) for c in CL]
    S=sum(Zh,arb(0))
    return 2*Zb*S*arb(36)/49 + 6*(arb(6)/7*S)**2
caseset={}
for case in cases:
    m_,a_=case.split(','); caseset.setdefault(m_,[]).append(case)
def Etot(m):  # both rho = (2,16), (-2,16) for the operator case m mod 48
    key=str((m-3)%48+3); return sum((E16(m,c) for c in caseset[key]),arb(0))
out=dict(R_untwisted_max=float(Ru.upper()),R_twisted_max=float(Rt.upper()),rate_cross=float((Ru*Rt).upper()),rate_sq=float((Rt*Rt).upper()),
         xi_lo=float(XI.lower()),ratio_cross=float((Ru*Rt/XI).upper()),ratio_sq=float((Rt*Rt/XI).upper()),K_min=float(Kmin.lower()))
assert Ru*Rt<XI and Rt*Rt<XI
for eps in ('0.5','0.1','0.01'):
    e=arb(eps); M=3
    # rates below xi_lo => E16(m)/xi^m decreasing; find least m (m = 3 mod 6) beyond which E16 <= eps (Kmin/2) xi^m
    while not all(Etot(mm)<=e*Kmin/2*XI**mm for mm in range(M,M+48,6)): M+=6
    out[f'M16_eps{eps}']=M
    # with the composite-level inheritance factor A16 <= sigma(h)/h <= 1 + ln h <= 1 + (m/2) ln lam (multiplies the (±2,16) d=7 cross part)
    M=3
    while not all((1+arb(mm)/2*LAM.log())*Etot(mm)<=e*Kmin/2*XI**mm for mm in range(M,M+48,6)): M+=6
    out[f'M16inh_eps{eps}']=M
print(json.dumps(out,indent=1))
json.dump(out,open('logs/assemble16.json','w'),indent=1)
