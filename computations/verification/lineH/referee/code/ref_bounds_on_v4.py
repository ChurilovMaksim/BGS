# Mechanical copy of referee ref_bounds.py with input file names switched to the v4 certificate outputs (no logic change).
"""Referee: independent exact-rational re-derivation of (a) the V_0 dom certificate scalars from stored N_j, rows_j upper
bounds (v4_V0_dom.json, *_str fields), (b) the rest certificates from stored N (floats, upward-padded), (c) the all-m chain.
All quantities as Fractions; upper bounds padded up by 1e-12 relative, lower down."""
import json, math, sys
from fractions import Fraction as Fr
from decimal import Decimal
L='/workspace/bgs-lineH/logs/'; Dd='/workspace/bgs-lineH/data/'
PADU=Fr(1)+Fr(1,10**12); PADL=Fr(1)-Fr(1,10**12)
def upf(x): return Fr(Decimal(repr(float(x))))*PADU
def ups(s):  # arb string "[m +/- r]" -> rational upper bound
    s=s.strip('[]')
    if '+/-' not in s: return Fr(Decimal(s))*PADU
    m,r=s.split('+/-'); return (Fr(Decimal(m.strip()))+Fr(Decimal(r.strip())))*PADU
def sqrt_lo(q):  # rational lower bound of sqrt(q)
    n=10**30; a=math.isqrt(q.numerator*n*n//q.denominator); return Fr(a,n)
def sqrt_up(q): return sqrt_lo(q)+Fr(1,10**30)
d=json.load(open(L+'v4_V0_dom.json')); bV=json.load(open(Dd+'prodV.json')); bE=json.load(open(Dd+'prodE.json'))
N=[ups(s) for s in d['N_str']]; rows=[ups(s) for s in d['rows_str']]; p=d['p']; assert len(N)==p+1 and len(rows)==p+1
kap=ups(d['kappa_str']); epsH=ups(d['epsH_str']); b21=ups(d['b21_str'])
pertV=upf(bV['delta1'])+upf(bV['delta2'])+upf(bV['Delta'])+upf(d['epsA'])
pertT=pertV+kap*(epsH+b21); X=upf(bV['Xnorm'])
b11=complex(d['b11_re'],d['b11_im']); ab2=Fr(Decimal(repr(b11.real)))**2+Fr(Decimal(repr(b11.imag)))**2
ab_lo=sqrt_lo(ab2); ab_hi=sqrt_up(ab2)
def neum(z,V):  # z lower bound of |z| (rational)
    q=N[p]/z**p; assert q<1, 'Neumann fails'
    return sum(V[j]/z**(j+1) for j in range(p))/(1-q)
full=lambda Rc,za,k:(k*Rc+1/za)*(1+X/za)+1/za
out={}
for R_,r1_ in [('1.5','0.05'),('1.55','0.05')]:
    R=Fr(R_); r1=Fr(r1_); z1=ab_lo-r1; assert z1>R
    Rc1=(1+neum(z1,rows))/r1+neum(z1,N); Rc2=(1+neum(R,rows))/(ab_lo-R)+neum(R,N)
    F1=pertT*full(Rc1,z1,kap); F2=pertT*full(Rc2,R,kap)
    out[f'dom R={R_} r1={r1_}']=dict(F1=float(F1),F2=float(F2),cert=F1<1 and F2<1,mu_lo=float(ab_lo-r1),mu_hi=float(ab_hi+r1))
print(out)
# rest: N lists in JSON are float upper bounds of arb values (float(x.upper())), so pad up
def rest(f,pert_build,R_):
    r=json.load(open(L+f)); Nr=[upf(x) for x in r['N']]; pp=r['p']; R=Fr(R_)
    q=Nr[pp]/R**pp; assert q<1
    SY=sum(Nr[j]/R**(j+1) for j in range(pp))/(1-q)
    b=pert_build; pert=upf(b['delta1'])+upf(b['delta2'])+upf(b['Delta'])+upf(r['epsA'])
    Xr=upf(b['Xnorm']); FR=pert*((SY+1/R)*(1+Xr/R)+1/R); return float(FR), FR<1
bVr=json.load(open(Dd+'prodVr.json'))
for f,b_,R_ in [('v4_V2_rest.json',bVr,'1.45'),('v4_V4_rest.json',bVr,'1.45'),('v4_V6_rest.json',bVr,'1.45'),
                ('v4_E0_rest.json',bE,'1.0'),('v4_E2_rest.json',bE,'1.0'),('v4_E4_rest.json',bE,'1.0'),('v4_E6_rest.json',bE,'1.0')]:
    print(f,R_,rest(f,b_,R_))
# all-m chain, exact rationals; lam bounds
s2_lo=sqrt_lo(Fr(2)); s2_hi=sqrt_up(Fr(2)); lam_lo=3+2*s2_lo; lam_hi=3+2*s2_hi
mu=ab_lo-Fr('0.05'); TV=upf(bV['trace_norm']); TE=upf(bE['trace_norm'])
assert bVr['trace_norm']==bV['trace_norm']
Rs=[Fr('1.45')]*3; RE=[Fr(1)]*4; R0=Fr('1.5')
def h(m):
    x,y=1,0
    for _ in range(m): x,y=3*x+8*y,x+3*y
    hh=math.isqrt((x-1)//2); assert 2*hh*hh==x-1 and hh%2==1; return hh
def Zlo(m):
    S=mu**m-R0**(m-1)*TV-sum(R**(m-1)*TV for R in Rs)-sum(R**(m-1)*TE for R in RE)
    return (1-1/lam_lo**m)/2*S
first=None; tab={}
for m in range(5,601,2):
    if m%3==0: continue
    z=Zlo(m)
    if z>0 and first is None: first=m
    if first is not None:
        assert z>0
        if m in (47,49,53,61,71,85,101,151,199,599):
            F=z*z/(h(m)-1); tab[m]=(float(F/(2*m)),float((F-4*m)/m))
print('first m',first,'prev odd non-mult-3:',[m for m in range(5,first) if m%2 and m%3][-1])
for m,v in tab.items(): print(m,'F/2m>=%.4g  Wrest/m>=%.4g'%v)
M=599; eps=(R0**(M-1)*TV+sum(R**(M-1)*TV for R in Rs)+sum(R**(M-1)*TE for R in RE))/mu**M
g2=mu**4/lam_hi   # g^2 = mu^4/lam
C=(1-1/lam_lo**M)**2*(1-eps)**2/4
print('eps599 <= %.3g'%float(eps),' g^2 >= %.8f -> g >= %.6f'%(float(g2),math.sqrt(float(g2))),' C >= %.6f'%float(C))
# check g >= 1.41279 claimed
print('g>=1.41279 ?', g2>=Fr('1.41279')**2)
