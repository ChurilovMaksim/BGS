# Referee: independent rational-exclusion for arg(xi)/2pi, exact Fractions with outward rounding; density of S+ per class.
import json, math
from fractions import Fraction as Fr
from flint import arb, acb, ctx
ctx.prec=256
mus=acb(arb('1.3572399242659728227708727178601298'),arb('-1.3516424762972735896036200390941797')); rm=arb('2e-6')+arb('1e-30')
c=json.load(open('/workspace/bgs-lineJ/logs/cert/V_2_s4_b1_disc.json'))['best']
mu21=acb(arb(c['center'][0]),arb(c['center'][1])); r21=arb(c['r'])+arb('1e-15')
u=(rm/(abs(mus)-rm)).asin()+(r21/(abs(mu21)-r21)).asin()
x=(mus.arg()+mu21.arg())/(2*arb.pi()); x=x-x.floor() if float(x.mid())>=0 else x+1
lo=x-u/(2*arb.pi()); hi=x+u/(2*arb.pi())
def F(a,up): # outward exact rational
    s=a.str(50,radius=False).replace('[','').split(' ')[0]; v=Fr(s); eps=Fr(1,10**45)
    return v+eps if up else v-eps
L=F(lo.lower(),False); H=F(hi.upper(),True)
bad=[(p,q) for q in range(1,1339) for p in range(math.ceil(L*q),math.floor(H*q)+1)]
best=min(range(1,3000),key=lambda q: (math.floor(H*q)<math.ceil(L*q), q))
print('interval',float(L),float(H),'width',float(H-L))
print('rationals q<1339 inside:',bad)
q0=next(q for q in range(1,5000) if math.ceil(L*q)<=math.floor(H*q)); print('least denominator in interval',q0,math.ceil(L*q0))
cw=0.84431; print('density per class arccos(c)/pi =',math.acos(cw)/math.pi, ' arccos=',math.acos(cw))
print('xi_lo/sqrt(lam)=',2.4586893/math.sqrt(3+2*math.sqrt(2)))
