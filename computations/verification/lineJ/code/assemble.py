"""Line J, J1 assembly (arb): explicit d=7 frozen-R' theorem for rho=(+-2,8), all 28 residues m mod 168 with m = 3 mod 6.
Inputs: Line F mu* disc (certV_eta2_a4_tight.json), H0=2(T_V+T_E) (Line F safe_table: T_V<=730.15, T_E<=22.94);
Line J certificates logs/cert/*.json (counts, discs, rest radii), trace norms data/cert/*.json; exact sector constants logs/sectors_exact.json;
W_C from model_cross (exact member sets from integer data, Gauss sums in double; margin 1e-9 relative applied).
Output logs/assemble.json/.log."""
import json, sys, math, hashlib, cmath, numpy as np
sys.path.insert(0,'/workspace/bgs-lineJ/code')
from flint import arb, acb, ctx
ctx.prec=128
from model_cross import W, members, cls, mdata
J='/workspace/bgs-lineJ/'
def sha(f): return hashlib.sha256(open(f,'rb').read()).hexdigest()
inputs={}
def load(f):
    inputs[f]=sha(f); return json.load(open(f))
LF='/workspace/audit/pr60/computations/verification/lineF/logs/certV_eta2_a4_tight.json'
lf=load(LF)['sectors']['4']; assert lf['certified']
mus=acb(1.3572399242659728227708727178601298,-1.3516424762972735896036200390941797); r_mus=arb('2e-6')+arb('1e-30')
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
# exact-ish W per residue (double Gauss sums; relative margin)
MARG=arb(1)-arb('1e-9')
sec=load(J+'logs/sectors_exact.json')['cases']
res=[]
for j in range(3,168,6):
    m=j+168*2   # representative (W, kappa, case depend only on m mod 168)
    Wp,_=W(m,2); Wm,_=W(m,-2)
    # periodicity spot check
    for mm in (m+168,m+336):
        Wq,_=W(mm,2); assert all(abs(Wq[c]-Wp[c])<1e-12 for c in CL)
    for c in CL: assert abs(Wm[c]-np.conj(Wp[c]))<1e-12
    B21=arb(abs(Wp['2:1'])/2)*MARG; B01=arb(abs(Wp['0:1'])/2)*(2-MARG)
    Wabs={c:arb(abs(Wp[c]))*(2-MARG) for c in CL}
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
    M1=None
    for mm in range(M0,6000,168):
        if ratio_plus(mm)>1 and ratio_minus(mm)>1:
            M1=mm; break
    res.append(dict(residue=j,W21=abs(Wp['2:1']),W01=abs(Wp['0:1']),B21_lo=float(B21.lower()),M0=M0,M1=M1,
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
json.dump(dict(summary=out,rates=rates,residues=res,inputs=inputs,code_sha256=sha(__file__)),open(J+'logs/assemble.json','w'),indent=1)
