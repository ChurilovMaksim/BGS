"""Line J v2 (referee fixes F1, F2, F7). J1 assembly (arb): explicit d=7 frozen-R' theorem for rho=(+-2,8), all 28 residues m mod 168 with m = 3 mod 6.
Inputs: Line F mu* disc (certV_eta2_a4_tight.json), H0=2(T_V+T_E) (Line F safe_table: T_V<=730.15, T_E<=22.94);
Line J certificates logs/cert/*.json (counts, discs, rest radii), trace norms data/cert/*.json; exact sector constants logs/sectors_exact.json;
W_C: v2 computes |W_C| in arb from exact Z[zeta7] integer histograms (F2); v1 used model_cross doubles with a 1e-9 margin.
Output logs/assemble_v2.json/.log.
 v2: F1 mu* centre from decimal strings; F2 |W_C| in arb from exact Z[zeta7] histograms (exact member sets);
     F7 symmetric m- bound with the square term absorbed: K_j^- = 2(2c^2 bracket - sq)/xi_lo^M0 reported (and monotone check)."""
import json, sys, math, hashlib, cmath, numpy as np
sys.path.insert(0,'/workspace/bgs-lineJ/code')
from flint import arb, acb, ctx
ctx.prec=128
from model_cross import cls, mdata
import math as _m
J='/workspace/bgs-lineJ/'
def sha(f): return hashlib.sha256(open(f,'rb').read()).hexdigest()
inputs={}
def load(f):
    inputs[f]=sha(f); return json.load(open(f))
LF='/workspace/audit/pr60/computations/verification/lineF/logs/certV_eta2_a4_tight.json'
lf=load(LF)['sectors']['4']; assert lf['certified']
mus=acb(arb('1.3572399242659728227708727178601298'),arb('-1.3516424762972735896036200390941797')); r_mus=arb('2e-6')+arb('1e-30')
MSU=arb('1.915475204133258'); H0=2*(arb('730.15')+arb('22.94'))
CL=cls; tracked={2:{'2:1':4,'0:1':0,'1:3':6},-2:{'2:1':0,'0:1':4,'1:3':2}}
Rtop={'2:1':arb('0.8'),'0:1':arb('0.9'),'1:3':arb('1.0')}
blocks={}  # (a,C) -> list of (R,T) for V and E over sectors (top sector: rest radius after orbit)
disc={}
for a in (2,-2):
    for b,C in enumerate(CL):
        L=[]
        for S in (0,2,4,6):
            TV=arb(load(J+f'data/cert/V_{a}_s{S}.json')['trace_norm'])*arb(1+1e-12)
            TE=arb(load(J+f'data/cert/E_{a}_s{S}.json')['trace_norm'])*arb(1+1e-12)
            if tracked[a].get(C)==S:
                dj=load(J+f'logs/cert/V_{a}_s{S}_b{b}_dom.json'); assert dj['best']['certified'] and float(dj['best']['R'])==float(Rtop[C].mid())
                di=load(J+f'logs/cert/V_{a}_s{S}_b{b}_disc.json'); assert di['best']['certified']
                c=di['best']['center']; disc[(a,C)]=(acb(c[0],c[1]),arb(di['best']['r'])); RV=Rtop[C]
            else:
                rj=load(J+f'logs/cert/V_{a}_s{S}_b{b}_rest.json'); assert rj['certified'],(a,S,C); RV=arb(rj['R'])
            ej=load(J+f'logs/cert/E_{a}_s{S}_b{b}_rest.json'); assert ej['certified']; RE=arb(ej['R'])
            L.append((RV,TV,RE,TE))
        blocks[(a,C)]=L
def e_bound(a,C,m):   # |eps| <= sum_S 1/2 * 1/3 * (RV^(m-1) TV + RE^(m-1) TE)
    return sum(((RV**(m-1)*TV+RE**(m-1)*TE) for RV,TV,RE,TE in blocks[(a,C)]),arb(0))/6
def argI(z,r):  # interval for arg of the disc
    ab=abs(z); return z.arg(), (r/(ab-r)).asin() if False else (r/(ab-r))
# certified moduli
def mod_bounds(z,r): return abs(z)-r, abs(z)+r
mu21,r21=disc[(2,'2:1')]; mu01,r01=disc[(2,'0:1')]; mu13,r13=disc[(2,'1:3')]
lo21,up21=mod_bounds(mu21,r21); lo01,up01=mod_bounds(mu01,r01); lo13,up13=mod_bounds(mu13,r13)
MSL=arb('1.9154712041332578')
xi21_lo=MSL*lo21; xi01_up=MSU*up01
LAMs=(3+2*arb(2).sqrt()).sqrt()
# argument of xi21 and theta = 168 arg mod 2pi
th0=mus.arg()+mu21.arg(); u=(r_mus/(abs(mus)-r_mus)).asin()+(r21/(abs(mu21)-r21)).asin()
th=168*th0; tw=2*arb.pi(); thm=th-tw*math.floor(float((th/tw).mid()))
th_lo=thm-168*u; th_up=thm+168*u
assert th_lo>0 and th_up<arb.pi()
c_win=(th_up/2).cos(); Nwin=math.ceil(float((2*arb.pi()/th_lo).upper()))
out=dict(mu21=[float(mu21.real),float(mu21.imag)],r21=float(r21),mu21_abs=[float(lo21.lower()),float(up21.upper())],
         mu01_abs=[float(lo01.lower()),float(up01.upper())],mu13_abs=[float(lo13.lower()),float(up13.upper())],
         xi21_lo=float(xi21_lo.lower()),xi01_up=float(xi01_up.upper()),sqrt_lam=float(LAMs.mid()),
         growth_lo=float((xi21_lo/LAMs).lower()),theta=[float(th_lo.lower()),float(th_up.upper())],c_window=float(c_win.lower()),N_window=Nwin)
print(json.dumps(out),flush=True)
# F2: exact W per residue: 7^4 W_C = sum_k H_k zeta7^k (integer histograms), evaluated in arb
d7=7
Nm=lambda x,y:(x*x-2*y*y)%d7
def orbit(bx,by):
    o=set(); x,y=bx,by
    for i in range(3):
        o.add((x%7,y%7)); o.add((-x%7,-y%7)); x,y=(3*x+4*y)%7,(2*x+3*y)%7
    return o
orbs={c:orbit(*map(int,c.split(':'))) for c in cls}
def Ghist(t,bx,by):
    H=[0]*d7
    for gx in range(d7):
        for gy in range(d7): H[(-(t*Nm(gx,gy)+2*(bx*gx+2*by*gy)))%d7]+=1
    return H
def hmul(A,B):
    C_=[0]*d7
    for i in range(d7):
        for j in range(d7): C_[(i+j)%d7]+=A[i]*B[j]
    return C_
def members7(m,a):
    D=mdata(m); h=D['h']; yp=D['yp']
    nu0=next(x for x in [((a//2)*pow(4,-1,h))%h+s_*h for s_ in (0,1)] if x%2==1)
    return [(j*yp)%d7 for j in range(1,d7) if _m.gcd((nu0+(2*h//d7)*j)%(2*h),2*h)==1]
def Wabs_exact(m,a):
    out={}
    for c in cls:
        T=[0]*d7
        for t in members7(m,a):
            g0=Ghist(t,0,0); g0=[g0[(-k)%d7] for k in range(d7)]
            for (bx,by) in orbs[c]: T=[x+y for x,y in zip(T,hmul(g0,Ghist(t,bx,by)))]
        re=sum((T[k]*(2*arb.pi()*k/7).cos() for k in range(d7)),arb(0)); im=sum((T[k]*(2*arb.pi()*k/7).sin() for k in range(d7)),arb(0))
        out[c]=(re*re+im*im).sqrt()/arb(7)**4
    return out
MARG=arb(1)
sec=load(J+'logs/sectors_exact.json')['cases']
res=[]
for j in range(3,168,6):
    m=j+168*2   # representative (W, kappa, case depend only on m mod 168)
    Wabs=Wabs_exact(m,2); Wabs_m=Wabs_exact(m,-2)
    for c in CL: assert abs(Wabs[c]-Wabs_m[c]).upper()<1e-30      # |W(-rho)| = |conj W(rho)|
    B21=Wabs['2:1']/2; B01=Wabs['0:1']/2
    def errp(m):
        tot=arb(0)
        for a in (2,-2):
            for C in CL:
                e=e_bound(a,C,m); trk=C in tracked[a]
                mu_up={'2:1':up21,'0:1':up01,'1:3':up13}.get(C,arb(0))
                tot+=Wabs[C]*(MSU**m*e/2+H0*((mu_up**m)/2 if trk else 0)+H0*e)
        return tot
    def sqb(m):   # sum_rho sum_t |Delta_t|^2 <= sum_rho 6 * ((6/7) sum_C |Zhat_C|)^2
        tot=arb(0)
        for a in (2,-2):
            s=arb(0)
            for C in CL:
                mu_up={'2:1':up21,'0:1':up01,'1:3':up13}.get(C)
                s+=(mu_up**m/2 if mu_up is not None else 0)+e_bound(a,C,m)
            tot+=6*(arb(6)/7*s)**2
        return tot
    def lower(m):  # cm^2 factor dropped: cross/(2 cm^2) >= c|B21|xi^m - |B01|xi01^m - err ; returns that bracket
        return c_win*B21*xi21_lo**m-B01*xi01_up**m-errp(m)
    # first M in this residue with bracket>0 for all larger m (monotone check: bracket/xi21^m increasing after it; we scan to 3000)
    M0=None; ok_from=None
    for mm in range(j,4000,168):
        v=lower(mm)
        if v>0:
            if ok_from is None: ok_from=mm
        else: ok_from=None
    M0=ok_from
    # tail argument: for m>=M0 each subtracted term / xi21_lo^m is decreasing geometrically (all ratios <1 checked below)
    # explicit D7/(m phi) bounds: phi < h < lam^{m/2}/2 ; cm^2 >= (1-lam^-m)^2
    def ratio_plus(m):
        cm2=(1-(3+2*arb(2).sqrt())**(-m))**2
        return 2*cm2*lower(m)/(m*LAMs**m/2)
    def ratio_minus(m):   # D7(m-)/(m phi) <= ( -2cm^2 lower + square ) / (m phi);  phi >= ? not needed: bound |.|/(m*h) from below
        cm2=(1-(3+2*arb(2).sqrt())**(-m))**2
        return (2*cm2*lower(m)-sqb(m))/(m*LAMs**m/2)
    def Kminus(m):
        cm2=(1-(3+2*arb(2).sqrt())**(-m))**2
        return 2*(2*cm2*lower(m)-sqb(m))/xi21_lo**m
    M1=None
    for mm in range(M0,6000,168):
        if ratio_plus(mm)>1 and ratio_minus(mm)>1:
            M1=mm; break
    Kp=4*((1-(3+2*arb(2).sqrt())**(-M0))**2)*lower(M0)/xi21_lo**M0; Km=Kminus(M0)
    assert Km>0 and Kminus(M0+168*6)>Km      # (2c^2 bracket - sq)/xi^m increasing (spot check; all subtracted rates < xi_lo)
    res.append(dict(residue=j,W21=float(Wabs['2:1'].mid()),W01=float(Wabs['0:1'].mid()),K_plus=float(Kp.lower()),K_minus=float(Km.lower()),B21_lo=float(B21.lower()),M0=M0,M1=M1,
                    bracket_M0_over_xi=float((lower(M0)/xi21_lo**M0).lower()),rp_M1=float(ratio_plus(M1).lower()),rm_M1=float(ratio_minus(M1).lower())))
    print(json.dumps(res[-1]),flush=True)
# geometric-decay sanity for the tail (ratios of every subtracted rate to xi21_lo)
rates=dict(xi01=float((xi01_up/xi21_lo).upper()))
worst=arb(0)
for (a,C),L in blocks.items():
    for RV,TV,RE,TE in L:
        worst=arb.max(worst,arb.max(RV,RE))
rates['max_rest_radius']=float(worst.upper()); rates['MSU*Rmax/xi21']=float((MSU*worst/xi21_lo).upper())
rates['H0 mu13/xi21']=float((up13/xi21_lo).upper()); rates['square: mu13^2/xi21']=float((up13**2/xi21_lo).upper())
print(json.dumps(rates))
json.dump(dict(summary=out,rates=rates,residues=res,inputs=inputs,code_sha256=sha(__file__)),open('/workspace/audit/lineJ/delta2/logs/assemble_v2_rerun.json','w'),indent=1)
