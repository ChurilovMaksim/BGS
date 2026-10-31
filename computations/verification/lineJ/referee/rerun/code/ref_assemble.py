"""Referee re-derivation of Theorem J constants (arb, independent code; inputs = author's certificate JSONs, Line F JSON,
exact Z[zeta7] W histograms re-evaluated in arb).  Bracket(m) = c|B21| xi_lo^m - |B01| xi01_up^m - Err(m), Err from my own
term-by-term expansion; also the m^- bound WITH the square term absorbed (K_j^-)."""
import json, math
from flint import arb, acb, ctx
ctx.prec=160
J='/workspace/bgs-lineJ/'
LF=json.load(open('/workspace/audit/pr60/computations/verification/lineF/logs/certV_eta2_a4_tight.json'))
s4=LF['sectors']['4']; assert s4['certified']
MSL=arb(s4['mu_abs_lower']); MSU=arb(s4['mu_abs_upper'])
# Line F b11 centre from the STRING (no float rounding), radius r1
b11=acb(arb('1.3572399242659728227708727178601298')+arb('0 +/- 1.85e-35'), arb('-1.3516424762972735896036200390941797')+arb('0 +/- 5.48e-35'))
r1=arb(LF['r1']) if not isinstance(LF['r1'],list) else arb(LF['r1'][0])
assert abs(b11).upper()+r1.upper() <= MSU.upper()*(1+1e-15) and abs(b11).lower()-r1.upper() >= MSL.lower()*(1-1e-15)
TV_F=arb('730.15'); TE_F=arb('22.94'); H0=2*(TV_F+TE_F)        # Line F: |eps| <= 1/2*4*r2^(m-1)(TV+TE), r2=1
assert float(arb(LF['r2']).mid())==1.0
cls=['1:3','2:1','0:1','1:2','1:5','0:3','1:0','0:2']
top={2:{'2:1':4,'0:1':0,'1:3':6},-2:{'2:1':0,'0:1':4,'1:3':2}}
def ld(f): return json.load(open(J+f))
disc={}; Rtop={}; blocks={}
for a in (2,-2):
    for b,C in enumerate(cls):
        L=[]
        for S in (0,2,4,6):
            TV=arb(ld(f'data/cert/V_{a}_s{S}.json')['trace_norm'])*(1+arb(2)**-40); TE=arb(ld(f'data/cert/E_{a}_s{S}.json')['trace_norm'])*(1+arb(2)**-40)
            if top[a].get(C)==S:
                dm=ld(f'logs/cert/V_{a}_s{S}_b{b}_dom.json')['best']; dc=ld(f'logs/cert/V_{a}_s{S}_b{b}_disc.json')['best']
                assert dm['certified'] and dm['count']==3 and dc['certified'] and dc['count_in_disc']==1
                RV=arb(dm['R']); disc[(a,C)]=(acb(dc['center'][0],dc['center'][1]),arb(dc['r']))
                assert (abs(disc[(a,C)][0])-arb(dc['r']))>RV      # disc lies outside the count radius
            else:
                rj=ld(f'logs/cert/V_{a}_s{S}_b{b}_rest.json'); assert rj['certified']; RV=arb(rj['R'])
            ej=ld(f'logs/cert/E_{a}_s{S}_b{b}_rest.json'); assert ej['certified']; RE=arb(ej['R'])
            L.append((RV,TV,RE,TE))
        blocks[(a,C)]=L
mu={C:disc[(2,C)] for C in ('2:1','0:1','1:3')}
# consistency of the - sign discs with conj (moduli)
for C in mu:
    zp,rp=disc[(2,C)]; zm,rm=disc[(-2,C)]
    om=acb(arb(2)/3).exp_pi_i()
    dd=min(float(abs(zm.conjugate()*om**k-zp).upper()) for k in range(3))
    print('disc consistency',C,'min_k |conj(mu-) w^k - mu+| =',dd,' (< 2r =',float(2*rp.upper()),')'); assert dd<2*float(rp.upper())
up={C:abs(mu[C][0])+mu[C][1] for C in mu}; lo={C:abs(mu[C][0])-mu[C][1] for C in mu}
xi_lo=MSL*lo['2:1']; xi01_up=MSU*up['0:1']; sl=(3+2*arb(2).sqrt()).sqrt()
g=xi_lo/sl
# theta
def argerr(z,r): return (r/(abs(z)-r)).asin()
th0=b11.arg()+mu['2:1'][0].arg(); u=argerr(b11,r1+arb('1e-34'))+argerr(*mu['2:1'])
th=168*th0; k=math.floor(float((th/(2*arb.pi())).mid())); th=th-2*arb.pi()*k
thlo=th-168*u; thup=th+168*u
assert thlo>0 and thup<arb.pi()
cwin=(thup/2).cos(); N=math.ceil(float((2*arb.pi()/thlo).upper()))
summary=dict(mu21_abs=[lo['2:1'].lower().str(12),up['2:1'].upper().str(12)],xi21_lo=xi_lo.lower().str(10),growth_lo=g.lower().str(10),
  theta=[thlo.lower().str(10),thup.upper().str(10)],cwin_lo=cwin.lower().str(10),N=N,
  rate01=(xi01_up/xi_lo).upper().str(8),
  rateRest=(MSU*max((max(RV,RE) for L in blocks.values() for RV,TV,RE,TE in L),key=lambda x: float(x.upper()))/xi_lo).upper().str(8),
  rate13=(up['1:3']/xi_lo).upper().str(8), rateSq=(up['1:3']**2/xi_lo).upper().str(8))
print(json.dumps(summary))
def e_C(a,C,m):   # |non-top part of Zhat_C|/c_m <= sum_S |c_S| (1/3)(RV^(m-1)TV + RE^(m-1)TE)
    return sum((RV**(m-1)*TV+RE**(m-1)*TE for RV,TV,RE,TE in blocks[(a,C)]),arb(0))/6
# exact W in arb
eB=ld('logs/exact_B.json')['residues']
z7=[acb(arb(2*k)/7).exp_pi_i() for k in range(7)]
import sys
sys.path.insert(0,'/workspace/bgs-lineI/dom_v3'); 
# full W for all classes in arb from exact histograms (recompute, independent of model_cross doubles)
from law import mdata
d=7
def Nm(x,y): return (x*x-2*y*y)%d
def orbit(bx,by):
    o=set(); x,y=bx,by
    for i in range(3):
        o.add((x%7,y%7)); o.add((-x%7,-y%7)); x,y=(3*x+4*y)%7,(2*x+3*y)%7
    return o
orb={c:orbit(*map(int,c.split(':'))) for c in cls}
def Gh(t,bx,by):
    H=[0]*7
    for gx in range(7):
        for gy in range(7): H[(-(t*Nm(gx,gy)+2*(bx*gx+2*by*gy)))%7]+=1
    return H
def Wabs(ts):
    out={}
    for c in cls:
        T=[0]*7
        for t in ts:
            g0=[Gh(t,0,0)[(-k)%7] for k in range(7)]
            for (bx,by) in orb[c]:
                G=Gh(t,bx,by)
                for i in range(7):
                    for j2 in range(7): T[(i+j2)%7]+=g0[i]*G[j2]
        out[c]=abs(sum((z7[k]*T[k] for k in range(7)),acb(0)))/arb(7)**4
    return out
res=[]
for r in ld('logs/assemble.json')['residues']:
    j=r['residue']; ts=eB[str(j)]['members_plus']; W=Wabs(ts)
    B21=W['2:1']/2; B01=W['0:1']/2
    def Err(m):
        t=arb(0)
        for a in (2,-2):
            for C in cls:
                e=e_C(a,C,m); mup=up[C] if C in up else arb(0)
                # |conj Z| <= MSU^m/2 + H0 ;  |Zhat_C| <= mup^m/2 + e ; leading x leading handled separately
                t+=W[C]*((MSU**m/2+H0)*(mup**m/2+e) - MSU**m/2*mup**m/2)
        return t
    def sq(m):
        t=arb(0)
        for a in (2,-2):
            s=sum(((up[C]**m/2 if C in up else 0)+e_C(a,C,m) for C in cls),arb(0))
            t+=6*(arb(6)/7*s)**2
        return t
    br=lambda m: cwin*B21*xi_lo**m - B01*xi01_up**m - Err(m)
    M0=None
    for mm in range(j,3000,168):
        if br(mm)>0: M0=mm; break
    # check positivity of all later scanned values (monotone anyway)
    assert all(br(mm)>0 for mm in range(M0,3000,168))
    if M0-168>0: assert not (br(M0-168)>0)
    Kp=4*br(M0)/xi_lo**M0*(1-arb(3+2*arb(2).sqrt())**(-M0))**2
    brm=lambda m: 2*(1-(3+2*arb(2).sqrt())**(-m))**2*br(m)-sq(m)
    Km=2*brm(M0)/xi_lo**M0
    def rp(m): return 2*(1-(3+2*arb(2).sqrt())**(-m))**2*br(m)/(m*sl**m/2)
    def rm(m): return brm(m)/(m*sl**m/2)
    M1=next(mm for mm in range(M0,6000,168) if rp(mm)>1 and rm(mm)>1)
    res.append(dict(j=j,W21=W['2:1'].str(8),M0=M0,K_plus=Kp.lower().str(5),K_minus=Km.lower().str(5),M1=M1,author=(r['M0'],r['M1'],round(4*r['bracket_M0_over_xi']*0.999,5))))
    print(json.dumps(res[-1]),flush=True)
json.dump(dict(summary=summary,residues=res),open('/workspace/audit/lineJ/rerun/logs/ref_assemble.json','w'),indent=1)
