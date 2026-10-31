"""Referee independent [N] spot recomputation of D7(m)/(m h) at selected m: own ARPACK spectra of the D=1980 sector blocks,
sector constants from (re-run) sectors_exact.json, Z0 leading terms from the exact sector constants (no kappa formula), members
and W_C from exact Gauss sums (own code), complex arithmetic in mpmath."""
import numpy as np, scipy.sparse.linalg as ssl, json, sys, math, mpmath as mp
sys.path.insert(0,'/workspace/bgs-lineI/dom_v3'); from law import mdata
mp.mp.dps=40
J='/workspace/bgs-lineJ/data/cert/'
sec=json.load(open('/workspace/audit/lineJ/rerun/logs/sectors_exact.json'))['cases']
cls=['1:3','2:1','0:1','1:2','1:5','0:3','1:0','0:2']
SP={}
for T,k in (('V',30),('E',10)):
    for A in (2,-2):
        for S in (0,2,4,6):
            for b in range(8):
                M=np.load(J+f'{T}_{A}_s{S}_b{b}_mid.npy'); SP[(T,A,S,b)]=ssl.eigs(M,k=k,which='LM',tol=1e-13,return_eigenvectors=False)
print('spectra done',flush=True)
mus=mp.mpc('1.3572399242659728227708727178601298','-1.3516424762972735896036200390941797')
def case(m): return {9:9,15:15,21:21,3:27}[m%24]
def cc(case,A,S): return mp.mpc(complex(sec[f'{case},{A}']['c'][str(S)]['c']))
d=7
def Nm(x,y): return (x*x-2*y*y)%d
def G(t,bx,by): return mp.fsum(mp.expjpi(-2*mp.mpf((t*Nm(gx,gy)+2*(bx*gx+2*by*gy))%d)/d) for gx in range(d) for gy in range(d))
def orbit(bx,by):
    o=set(); x,y=bx,by
    for i in range(3):
        o.add((x%7,y%7)); o.add((-x%7,-y%7)); x,y=(3*x+4*y)%7,(2*x+3*y)%7
    return o
orb={c:orbit(*map(int,c.split(':'))) for c in cls}
def members(m,a):
    D=mdata(m); h=D['h']; yp=D['yp']
    # frozen rule: nu unit, 8 nu == a mod 2h/7, nu != nu_rho
    nu0=next(x for x in range(1,2*h,2) if (8*x-a)%(2*h)==0) if h<10**6 else None
    if nu0 is None:
        nu0=next(x for x in [((a//2)*pow(4,-1,h))%h+s*h for s in (0,1)] if x%2==1)
    assert (8*nu0-a)%(2*h)==0
    return [(j*yp)%d for j in range(1,d) if math.gcd(nu0+(2*h//d)*j,2*h)==1]
LAM=3+2*mp.sqrt(2)
out=[]
for m in [int(x) for x in sys.argv[1:]]:
    h=mdata(m)['h']; cm=1-LAM**(-m); C=case(m)
    Z0={-2:cm*cc(C,-2,4)*mus**m, 2:cm*cc(C,2,0)*mp.conj(mus)**m}
    tot=0; sq=0
    for A in (2,-2):
        ts=members(m,A)
        Zh={}
        for b,c in enumerate(cls):
            s=0
            for S in (0,2,4,6):
                s+=cc(C,A,S)*(mp.fsum(mp.mpc(complex(z))**m for z in SP[('V',A,S,b)])-mp.fsum(mp.mpc(complex(z))**m for z in SP[('E',A,S,b)]))/3
            Zh[c]=cm*s
        for t in ts:
            De=mp.fsum(Zh[c]*G(t,bx,by) for c in cls for (bx,by) in orb[c])/d**2
            om=G(t,0,0)/d
            tot+=2*mp.re(mp.conj(om*Z0[A]/d)*De); sq+=abs(De)**2
    r=dict(m=m,D7_over_mh=float((tot+sq)/(m*h)),cross_over_mh=float(tot/(m*h)),sq_over_mh=float(sq/(m*h)))
    out.append(r); print(json.dumps(r),flush=True)
json.dump(out,open('/workspace/audit/lineJ/rerun/logs/ref_numerics.json','w'),indent=1)
