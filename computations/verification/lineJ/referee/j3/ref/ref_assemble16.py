# Referee: independent recomputation of the (±2,16) d=7 bound from the author's certificates (mpmath, upward-padded).
import json, glob, math
from mpmath import mp, mpf, log, sqrt
mp.dps=40
J3='/workspace/bgs-lineJ/J3'
mem=json.load(open(f'{J3}/logs/blocks16_reps.json'))['members']
pad=mpf(1)+mpf(2)**-30
def C(T,r,kind,b):
    c=json.load(open(f'{J3}/logs/cert/{T}_r{r}_{kind}_b{b}_rest.json')); B=json.load(open(f'{J3}/data/cert/{T}_r{r}_{kind}.json'))
    assert c['certified'] and c['mode']=='rest' and c['provenance']['code_sha256'].startswith('f346e22c') if isinstance(c['provenance'],dict) else True
    R=mpf(c['R']); SY=mpf(c['SY_R'])*pad; F=mpf(c['F_R2'])*pad; Xn=mpf(B['Xnorm'])*pad; tn=mpf(B['trace_norm'])*pad
    assert F<1
    fr=(SY+1/R)*(1+Xn/R)+1/R
    return R, tn/2*fr/(1-F)
D={}
for r in range(32):
    for T in 'VE':
        D[(r,T,'u')]=C(T,r,'u',0)
        for b in range(8): D[(r,T,b)]=C(T,r,'t',b)
# cases: operator case (m mod 48, a)
cases={}
for r,l in mem.items():
    for case,blk in l: cases.setdefault(case,[]).append(int(r))
lam=3+2*sqrt(2); xi=mpf('2.4586893')
A=json.load(open('/workspace/bgs-lineJ/logs/assemble_v2.json'))['residues']; Kmin=min(min(x['K_plus'],x['K_minus']) for x in A)*mpf('0.999999')
def X16(m):  # |cross| bound summed over rho=(±2,16), with sq (conservative), times inheritance factor
    key=(m-3)%48+3; tot=0
    for a in (2,-2):
        rs=cases[f'{key},{a}']
        Zb=sum(D[(r,T,'u')][1]*D[(r,T,'u')][0]**m for r in rs for T in 'VE')
        S=sum(D[(r,T,b)][1]*D[(r,T,b)][0]**m for r in rs for T in 'VE' for b in range(8))
        tot+=2*Zb*S*mpf(36)/49+6*(mpf(6)/7*S)**2
    return tot
Ru=max(D[k][0] for k in D if k[2]=='u'); Rt=max(D[k][0] for k in D if k[2]!='u')
print('Ru',Ru,'Rt',Rt,'RuRt/xi',Ru*Rt/xi,'Rt^2/xi',Rt*Rt/xi,'Kmin',Kmin)
for inh in (False,True):
    ok=[m for m in range(3,400,6) if (1+(m/2*log(lam) if inh else 0))*X16(m) > mpf('0.01')*Kmin/2*xi**m]
    print('inheritance' if inh else 'plain','last failing m (eps=0.01):',max(ok) if ok else None, ' => threshold', (max(ok)+6) if ok else 3)
for m in (243,495):
    print(m,'ratio X16_inh/((Kmin/2)xi^m)=',mp.nstr((1+m/2*log(lam))*X16(m)/(Kmin/2*xi**m),5))
