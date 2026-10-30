"""Line H, H2: rigorous (arb) data for the lifted 49-state operators of the Line B kick f_B (eta = 2), full alphabet.
  (L Phi)_c = sum_{n in Z} w_b(n) [M_{n,c} C_{n,c}] (x) U_n  Phi_{c'},  x = n/7, c' = round((c+x)/lam)   (V: c in Z;  E: c in Z+1/2,
  transition iff round((c-1/2+x)/lam)+1 = round((c+1/2+x)/lam), c' = round((c-1/2+x)/lam)+1/2),
  M_{n,c}: multiplication by e(s c0 x u) on D(c,rho);  C_{n,c} phi(u) = phi((u+x)/lam);  w_b(n) = ghat(n) e(s c0 x^2/2 + b n/8);
  U_n = DP(n)^T on C^49 (TRACE-194 convention): (U_n v)[tgt(sig)] += e(gamma(n sig + 2^{-1} n^2)/49) v[sig], tgt(sig) = lami (sig+n) mod 49.
 Weighted space ||Phi||^2 = sum_c om_c^2 ||Phi_c||^2, om_c = exp(-beta(|c|-Rc)_+), Rc = K0 (V) / K0-1/2 (E).
 Output: JSON with sector-independent bounds (delta1, delta2, Delta, ||X||, trace norm) and, per sector b, the core Galerkin matrix
 as float mid (complex128) + entrywise rad (float64) .npy files, rad covering arb radius + conversion + float accumulation errors.
 Usage: cert49_build.py typ s K0 rho K beta Nmax Rmax sectors outprefix [prec]"""
import sys, json, time, math
import numpy as np
from flint import arb, acb, acb_mat, ctx
sys.path.insert(0,'/workspace/bgs-lineH/code'); sys.path.insert(0,'/workspace/bgs-next/lineE/step2')
from ghat_arb import ghat_arb
from lawlib import law_params
typ=sys.argv[1]; s=int(sys.argv[2]); K0=int(sys.argv[3]); rho_s=sys.argv[4]; K=int(sys.argv[5]); beta_s=sys.argv[6]
Nmax=int(sys.argv[7]); Rmax=int(sys.argv[8]); sectors=[int(t) for t in sys.argv[9].split(',') if t]; outp=sys.argv[10]
ctx.prec=int(sys.argv[11]) if len(sys.argv)>11 else 128
K2=int(sys.argv[12]) if len(sys.argv)>12 else K   # Galerkin degree on the outermost core discs |c|=Rc
t0=time.time()
two=arb(2); lam=3+2*two.sqrt(); c0=1/(lam-1/lam); pi=arb.pi(); I=acb(0,1); half=arb(1)/2
rho=arb(rho_s); beta=arb(beta_s); Rc=arb(K0) if typ=='V' else arb(K0)-half
P=law_params(5,7,s); gam=P['gamma']; li=P['lami']; inv2=pow(2,-1,49)
# m-independence of (gamma, lami) for the chosen sqrt(2) root: checked over m (TRACE-194 sec 10.2 proves it)
for mm in (7,11,13,17,19,23,25,29,31,35,37,41,43,47):
    Pm=law_params(mm,7,s); assert Pm['gamma']==gam and Pm['lami']==li, mm
def e(t): return (2*pi*I*t).exp()
# ---------------- ghat (rigorous) ----------------
a_tail=(2*pi*c0*rho+beta/lam)/7          # weight exponent per unit n for tails at radius rho
a_tail2=(2*pi*c0*2*rho)/7
G,err=ghat_arb(a_list=(0,a_tail.upper(),(2*pi*c0*rho/7).upper()),J={7:60})
errs=list(err.values()); err0,errT,errB0=errs[0],errs[1],errs[2]
def gh(n):
    g=G.get(n,acb(0)); return g+acb(arb(0,err0.upper()),arb(0,err0.upper()))
W={n:abs(gh(n)) for n in range(-Nmax,Nmax+1)}
# weighted tails beyond Nmax: sum_{|n|>Nmax} |ghat(n)| e^{a|n|} <= sum_{Nmax<|n|<=supp} |G_n| e^{a|n|} + err(a)
def wtail(a,errA):
    return sum((abs(v)*(a*abs(n)).exp() for n,v in G.items() if abs(n)>Nmax),arb(0))+errA
tailT=wtail(a_tail,errT); tailB0=wtail(2*pi*c0*rho/7,errB0)
print('ghat: err0',float(err0.upper()),'tailT',float(tailT.upper()),'tailB0',float(tailB0.upper()),flush=True)
def certfloor(y):
    f=math.floor(float(y.mid())); assert (y-f)>0 and (y-f)<1, 'floor not certified'; return f
def rnd(t): return certfloor(t+half)
def target(c2,n):
    x=arb(n)/7
    if typ=='V':
        j=rnd((arb(c2)/2+x)/lam); return 2*j, (arb(c2)/2+x)/lam-j
    lo=arb(c2-1)/2; j=rnd((lo+x)/lam); j2=rnd((lo+1+x)/lam)
    if j2!=j+1: return None
    return 2*j+1, (arb(c2)/2+x)/lam-(arb(2*j+1)/2)
def om(c2):
    d=abs(arb(c2)/2)-Rc
    return (-beta*d).exp() if d>0 else arb(1)
iscore=lambda c2: abs(arb(c2)/2)<=Rc
Mn=lambda n,R: (2*pi*c0*abs(arb(n)/7)*R).exp()
thstar=(half/rho+1/lam) if typ=='V' else (half/lam/rho+1/lam)
assert thstar<1
cores=[c2 for c2 in range(-2*K0-2,2*K0+3) if (c2%2==(0 if typ=='V' else 1)) and iscore(c2)]
idx={c2:i for i,c2 in enumerate(cores)}; nc=len(cores); NS=49
Kc={c2:(K2 if abs(arb(c2)/2)>Rc-1 else K) for c2 in cores}
off={}; _o=0
for c2 in cores: off[c2]=_o; _o+=NS*Kc[c2]
D=_o
print('typ',typ,'s',s,'cores',[c/2 for c in cores],'Kc',[Kc[c] for c in cores],'dim',D,flush=True)
KM=max(K,K2)
fact=[arb(1)]
for i in range(1,KM+1): fact.append(fact[-1]*i)
lamp=[arb(1)]
for i in range(1,KM+1): lamp.append(lamp[-1]/lam)
Rp=2*rho
blocks={}; col_tail={c2:arb(0) for c2 in cores}; col_d2={c2:arb(0) for c2 in cores}
Del_rows={}; X_rows={}; Tn=arb(0)
for c2 in cores:
    Del_rows[c2]=arb(0)
    for n in range(-Nmax,Nmax+1):
        tg=target(c2,n)
        if tg is None: continue
        j2,dl=tg; th=abs(dl)/rho+1/lam; assert th<1
        bn=W[n]*Mn(n,rho)/(1-th*th).sqrt(); tn=W[n]*Mn(n,rho)/(1-th)
        ratio=om(c2)/om(j2); Tn+=ratio*tn
        if not iscore(j2):
            Del_rows[c2]+=ratio*bn; continue
        x=arb(n)/7; Ko=Kc[c2]; Ki=Kc[j2]
        z=2*pi*I*s*c0*x*rho; zp=[acb(1)]
        for i in range(1,Ko): zp.append(zp[-1]*z)
        M=acb_mat(Ko,Ko)
        for l in range(Ko):
            for jj in range(l+1): M[l,jj]=zp[l-jj]/fact[l-jj]
        Cm=acb_mat(Ko,Ki); B=dl/rho; bp=[arb(1)]
        for i in range(1,max(Ko,Ki)): bp.append(bp[-1]*B)
        for k in range(Ki):
            for jj in range(min(k+1,Ko)): Cm[jj,k]=fact[k]/(fact[jj]*fact[k-jj])*lamp[jj]*bp[k-jj]
        blocks[(c2,n)]=(j2,(M*Cm)*e(s*c0*x*arb(c2)/2))
        col_tail[j2]+=W[n]*Mn(n,rho)*th**Ki/(1-th*th).sqrt()
        # Cauchy estimate on |sig|=r (r optimised per letter on a grid): Taylor coeff i of M*(e_l o psi) <= W e^{2pi c0|x| r rho} g_r^l r^{-i}
        best=None
        for rr in ('1.25','1.5','1.75','2','2.5','3','4'):
            r_=arb(rr); g=abs(dl)/rho+r_/lam
            hs2=sum(((g**l)**2 for l in range(Ki)),arb(0))*(1/r_)**(2*Ko)/(1-1/r_**2)
            v=W[n]*Mn(n,r_*rho)*hs2.sqrt()
            if best is None or v.upper()<best.upper(): best=v
        col_d2[j2]+=best
    al=a_tail; tailfac=(beta*(abs(arb(c2)/2)/lam+half)).exp()
    Del_rows[c2]+=tailfac*tailT/(1-thstar*thstar).sqrt(); Tn+=tailfac*tailT/(1-thstar)
delta1=sum((col_tail[c]**2 for c in cores),arb(0)).sqrt()
delta2=sum((col_d2[c]**2 for c in cores),arb(0)).sqrt()
delta=delta1+delta2
print('delta1',float(delta1.upper()),'delta2',float(delta2.upper()),'blocks',len(blocks),round(time.time()-t0,1),'s',flush=True)
lat=[c2 for c2 in range(-2*Rmax,2*Rmax+1) if (c2%2==(0 if typ=='V' else 1)) and not iscore(c2)]
for c2 in lat:
    X_rows[c2]=arb(0); Del_rows[c2]=arb(0)
    for n in range(-Nmax,Nmax+1):
        tg=target(c2,n)
        if tg is None: continue
        j2,dl=tg; th=abs(dl)/rho+1/lam
        bn=W[n]*Mn(n,rho)/(1-th*th).sqrt(); tn=W[n]*Mn(n,rho)/(1-th)
        ratio=om(c2)/om(j2); Tn+=ratio*tn
        if iscore(j2): X_rows[c2]+=ratio*bn
        else: Del_rows[c2]+=ratio*bn
    tailfac=om(c2)*(beta*(abs(arb(c2)/2)/lam+half)).exp()
    Del_rows[c2]+=tailfac*tailT/(1-thstar*thstar).sqrt(); Tn+=tailfac*tailT/(1-thstar)
# analytic rows |c|>Rmax: ratio <= e^{-beta(|c|-Rc)} + e^{-beta|c|(1-1/lam)+beta/2} e^{beta|x|/lam}
B0=sum((W[n]*Mn(n,rho) for n in W),arb(0))+tailB0
B1=sum((W[n]*Mn(n,rho)*(beta*abs(arb(n)/7)/lam).exp() for n in W),arb(0))+tailT
g1=beta; g2=beta*(1-1/lam); cmin=arb(Rmax)+half
def geo(g,pw): return 2*(-pw*g*cmin).exp()/(1-(-pw*g).exp())
far2=2*((g1*Rc).exp()**2*geo(g1,2)*B0**2+(beta).exp()*geo(g2,2)*B1**2)/(1-thstar*thstar)
farT=((g1*Rc).exp()*geo(g1,1)*B0+(beta/2).exp()*geo(g2,1)*B1)/(1-thstar)
Delta=(sum((v**2 for v in Del_rows.values()),arb(0))+far2).sqrt()
Xn=(sum((v**2 for v in X_rows.values()),arb(0))).sqrt()
Tn=(Tn+farT)*NS      # trace norm of U_n on C^49 is 49
res=dict(typ=typ,s=s,eta='2',K0=K0,rho=rho_s,K=K,K2=K2,beta=beta_s,prec=ctx.prec,Nmax=Nmax,Rmax=Rmax,gamma=gam,lami=li,D=D,
         ghat_err0=float(err0.upper()),tailT=float(tailT.upper()),delta1=float(delta1.upper()),delta2=float(delta2.upper()),
         Delta=float(Delta.upper()),Xnorm=float(Xn.upper()),trace_norm=float(Tn.upper()),far2=float(far2.upper()),sectors={})
print('Delta rows',{k/2:float(v.upper()) for k,v in Del_rows.items() if float(v.upper())>1e-5});print('Delta',res['Delta'],'||X||',res['Xnorm'],'trace',res['trace_norm'],round(time.time()-t0,1),'s',flush=True)
json.dump(res,open(outp+'.json','w'),indent=1)
# ---------------- Galerkin matrices: mid + rad ----------------
U=2.0**-53
def acb_to_mr(Mx):
    """acb_mat -> (mid complex128, rad float64) with |true - mid| <= rad entrywise (conversion rounding included)."""
    n_=Mx.nrows(); m_=Mx.ncols(); mid=np.zeros((n_,m_),complex); rad=np.zeros((n_,m_))
    for i in range(n_):
        for j in range(m_):
            v=Mx[i,j]; re=v.real; im=v.imag
            a=float(re.mid()); b=float(im.mid())
            mid[i,j]=complex(a,b)
            r=float(re.rad())+float(im.rad())   # |dz| <= |dre|+|dim|
            # conversion error of mid to double: <= u*|.| per component (plus tiny absolute)
            rad[i,j]=r*(1+4*U)+U*(abs(a)+abs(b))*(1+4*U)+1e-300
    return mid,rad
tgt_of=lambda n,sg: (li*(sg+n))%49
for b in sectors:
    t1=time.time()
    Amid=np.zeros((D,D),complex); Arad=np.zeros((D,D))
    for c2 in cores:
        agg={}
        for n in range(-Nmax,Nmax+1):
            if (c2,n) not in blocks: continue
            j2,Bk=blocks[(c2,n)]; x=arb(n)/7
            w=gh(n)*e(s*c0*x*x/2+arb(b*n)/8)
            for sg in range(NS):
                key=(j2,sg,tgt_of(n,sg))
                ph=e(arb((gam*(n*sg+inv2*n*n))%49)/49)
                term=Bk*(w*ph)
                agg[key]=term if key not in agg else agg[key]+term
        for (j2,sg,so),Mx in agg.items():
            mid,rad=acb_to_mr(Mx)
            Ko=Kc[c2]; Ki=Kc[j2]; r0=off[c2]+so*Ko; q0=off[j2]+sg*Ki
            # each (row-block, col-block) gets exactly one aggregated block (key unique) -> no float accumulation
            assert not Amid[r0:r0+Ko,q0:q0+Ki].any()
            Amid[r0:r0+Ko,q0:q0+Ki]=mid; Arad[r0:r0+Ko,q0:q0+Ki]=rad
    np.save(outp+f'_b{b}_mid.npy',Amid); np.save(outp+f'_b{b}_rad.npy',Arad)
    radF=float(np.sqrt((Arad**2).sum())*(1+1e-10))
    res['sectors'][str(b)]=dict(rad_fro=radF,mid_fro=float(np.linalg.norm(Amid)),secs=round(time.time()-t1,1))
    print('sector',b,res['sectors'][str(b)],flush=True)
    json.dump(res,open(outp+'.json','w'),indent=1)
res['secs']=round(time.time()-t0,1); json.dump(res,open(outp+'.json','w'),indent=1); print('done',res['secs'],flush=True)
