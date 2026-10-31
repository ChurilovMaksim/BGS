"""Line I: rigorous (arb) data for the lifted G2 (a,8) transfer operators of the k1 kick (eta=2), restricted to the 16 reachable
automaton states, with the d=7 dilation twist realised as a 3-cycle (48 states).  Adapted from Line H cert49_build.py
(sha 2b5d693f...): x = n (integer letters) instead of n/7; multiplier coefficient C = -4 a c0 / b; finite factor = exact monomial
matrices from gstates.py (phase e(-ph8/8) e(n tw/7)); kick ghat(n) = i^n J_n(1.8) with Line F Bessel tail bound.
  (L Phi)_c = sum_{n in Z} w(n) [M_{n,c} C_{n,c}] (x) A_n  Phi_{c'},  c' = round((c+n)/lam) (V), edge rule (E),
  M_{n,c}: multiplication by e(C n u) on D(c,rho);  C_{n,c} phi(u) = phi((u+n)/lam);  w(n) = ghat(n) e(C n^2/2).
Output: JSON (sector-independent bounds) + per twist class j: core Galerkin mid/rad .npy (prefix_b{j}_mid.npy), for rig_spec.py v4.
Usage: certG_build.py typ m a K0 rho K beta Nmax Rmax classes outprefix prec K2
  classes: comma list of bx:by (twist beta mod 7) or 'none' (untwisted, 16 states)"""
import sys, json, time, math, hashlib, os
import numpy as np
from flint import arb, acb, acb_mat, ctx
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from gstates16_block import g2params, reach, taus7, finite, CASE, BLK
typ=sys.argv[1]; m=int(sys.argv[2]); a=int(sys.argv[3]); b=16; K0=int(sys.argv[4]); rho_s=sys.argv[5]; K=int(sys.argv[6]); beta_s=sys.argv[7]
Nmax=int(sys.argv[8]); Rmax=int(sys.argv[9]); classes=sys.argv[10].split(','); outp=sys.argv[11]
ctx.prec=int(sys.argv[12]); K2=int(sys.argv[13])
def sha(f): return hashlib.sha256(open(f,'rb').read()).hexdigest()
here=os.path.dirname(os.path.abspath(__file__))
prov=dict(code_sha256=sha(__file__),gstates16_sha256=sha(os.path.join(here,'gstates16_block.py')),case=CASE,block=BLK,argv=sys.argv,started=time.strftime('%Y-%m-%d %H:%M:%S %z'))
t0=time.time()
two=arb(2); lam=3+2*two.sqrt(); c0=1/(lam-1/lam); pi=arb.pi(); I=acb(0,1); half=arb(1)/2
Cc=arb(-4*a)*c0/b; aC=abs(Cc)
rho=arb(rho_s); beta=arb(beta_s); Rc=arb(K0) if typ=='V' else arb(K0)-half
xk=arb(9)/10*2   # 0.9*eta, eta=2
def e(t): return (2*pi*I*t).exp()
J={n: xk.bessel_j(arb(abs(n)))*(1 if (n>=0 or n%2==0) else -1) for n in range(-Nmax,Nmax+1)}
def gh(n): return (I**(n%4))*J[n]
W={n:abs(J[n]) for n in J}
def btail(alpha):
    """sum_{|n|>Nmax} |J_n(xk)| e^{alpha|n|} <= 2 t^{N+1}/(N+1)! /(1-t/(N+2)), t = xk e^alpha/2 (|J_n(x)| <= (x/2)^n/n!)."""
    t=xk*alpha.exp()/2; N=Nmax; f=arb(1)
    for i in range(1,N+2): f*=i
    q=t/(N+2); assert q<1
    return 2*t**(N+1)/f/(1-q)
a_tail=2*pi*aC*rho+beta/lam
tailT=btail(a_tail); tailB0=btail(2*pi*aC*rho)
print('C',float(Cc.mid()),'tailT',float(tailT.upper()),'tailB0',float(tailB0.upper()),flush=True)
def certfloor(y):
    f=math.floor(float(y.mid())); assert (y-f)>0 and (y-f)<1, 'floor not certified'; return f
def rnd(t): return certfloor(t+half)
def target(c2,n):
    x=arb(n)
    if typ=='V':
        j=rnd((arb(c2)/2+x)/lam); return 2*j, (arb(c2)/2+x)/lam-j
    lo=arb(c2-1)/2; j=rnd((lo+x)/lam); j2=rnd((lo+1+x)/lam)
    if j2!=j+1: return None
    return 2*j+1, (arb(c2)/2+x)/lam-(arb(2*j+1)/2)
def om(c2):
    d=abs(arb(c2)/2)-Rc
    return (-beta*d).exp() if d>0 else arb(1)
iscore=lambda c2: abs(arb(c2)/2)<=Rc
Mn=lambda n,R: (2*pi*aC*abs(arb(n))*R).exp()
thstar=(half/rho+1/lam) if typ=='V' else (half/lam/rho+1/lam)
assert thstar<1
P=g2params(m,a,b); idx,tg=reach(P,Nmax)
cycs={c:(None if c=='none' else taus7(*[int(t) for t in c.split(':')])) for c in classes}
NS=len(idx)*(1 if classes==['none'] else 3)
assert all((cycs[c] is None)==(classes==['none']) for c in classes)
cores=[c2 for c2 in range(-2*K0-2,2*K0+3) if (c2%2==(0 if typ=='V' else 1)) and iscore(c2)]
Kc={c2:(K2 if abs(arb(c2)/2)>Rc-1 else K) for c2 in cores}
off={}; _o=0
for c2 in cores: off[c2]=_o; _o+=NS*Kc[c2]
D=_o
print('typ',typ,'m',m,'a',a,'params',P,'states',len(idx),'NS',NS,'cores',[c/2 for c in cores],'Kc',[Kc[c] for c in cores],'dim',D,flush=True)
KM=max(K,K2)
fact=[arb(1)]
for i in range(1,KM+1): fact.append(fact[-1]*i)
lamp=[arb(1)]
for i in range(1,KM+1): lamp.append(lamp[-1]/lam)
blocks={}; col_tail={c2:arb(0) for c2 in cores}; col_d2={c2:arb(0) for c2 in cores}
Del_rows={}; X_rows={}; Tn=arb(0)
for c2 in cores:
    Del_rows[c2]=arb(0)
    for n in range(-Nmax,Nmax+1):
        tgv=target(c2,n)
        if tgv is None: continue
        j2,dl=tgv; th=abs(dl)/rho+1/lam; assert th<1
        bn=W[n]*Mn(n,rho)/(1-th*th).sqrt(); tn=W[n]*Mn(n,rho)/(1-th)
        ratio=om(c2)/om(j2); Tn+=ratio*tn
        if not iscore(j2):
            Del_rows[c2]+=ratio*bn; continue
        x=arb(n); Ko=Kc[c2]; Ki=Kc[j2]
        z=2*pi*I*Cc*x*rho; zp=[acb(1)]
        for i in range(1,Ko): zp.append(zp[-1]*z)
        M=acb_mat(Ko,Ko)
        for l in range(Ko):
            for jj in range(l+1): M[l,jj]=zp[l-jj]/fact[l-jj]
        Cm=acb_mat(Ko,Ki); B=dl/rho; bp=[arb(1)]
        for i in range(1,max(Ko,Ki)): bp.append(bp[-1]*B)
        for k in range(Ki):
            for jj in range(min(k+1,Ko)): Cm[jj,k]=fact[k]/(fact[jj]*fact[k-jj])*lamp[jj]*bp[k-jj]
        blocks[(c2,n)]=(j2,(M*Cm)*e(Cc*x*arb(c2)/2))
        col_tail[j2]+=W[n]*Mn(n,rho)*th**Ki/(1-th*th).sqrt()
        best=None
        for rr in ('1.25','1.5','1.75','2','2.5','3','4'):
            r_=arb(rr); g=abs(dl)/rho+r_/lam
            hs2=sum(((g**l)**2 for l in range(Ki)),arb(0))*(1/r_)**(2*Ko)/(1-1/r_**2)
            v=W[n]*Mn(n,r_*rho)*hs2.sqrt()
            if best is None or v.upper()<best.upper(): best=v
        col_d2[j2]+=best
    tailfac=(beta*(abs(arb(c2)/2)/lam+half)).exp()
    Del_rows[c2]+=tailfac*tailT/(1-thstar*thstar).sqrt(); Tn+=tailfac*tailT/(1-thstar)
delta1=sum((col_tail[c]**2 for c in cores),arb(0)).sqrt()
delta2=sum((col_d2[c]**2 for c in cores),arb(0)).sqrt()
print('delta1',float(delta1.upper()),'delta2',float(delta2.upper()),'blocks',len(blocks),round(time.time()-t0,1),'s',flush=True)
lat=[c2 for c2 in range(-2*Rmax,2*Rmax+1) if (c2%2==(0 if typ=='V' else 1)) and not iscore(c2)]
for c2 in lat:
    X_rows[c2]=arb(0); Del_rows[c2]=arb(0)
    for n in range(-Nmax,Nmax+1):
        tgv=target(c2,n)
        if tgv is None: continue
        j2,dl=tgv; th=abs(dl)/rho+1/lam
        bn=W[n]*Mn(n,rho)/(1-th*th).sqrt(); tn=W[n]*Mn(n,rho)/(1-th)
        ratio=om(c2)/om(j2); Tn+=ratio*tn
        if iscore(j2): X_rows[c2]+=ratio*bn
        else: Del_rows[c2]+=ratio*bn
    tailfac=om(c2)*(beta*(abs(arb(c2)/2)/lam+half)).exp()
    Del_rows[c2]+=tailfac*tailT/(1-thstar*thstar).sqrt(); Tn+=tailfac*tailT/(1-thstar)
B0=sum((W[n]*Mn(n,rho) for n in W),arb(0))+tailB0
B1=sum((W[n]*Mn(n,rho)*(beta*abs(arb(n))/lam).exp() for n in W),arb(0))+tailT
g1=beta; g2=beta*(1-1/lam); cmin=arb(Rmax)+half
def geo(g,pw): return 2*(-pw*g*cmin).exp()/(1-(-pw*g).exp())
far2=2*((g1*Rc).exp()**2*geo(g1,2)*B0**2+(beta).exp()*geo(g2,2)*B1**2)/(1-thstar*thstar)
farT=((g1*Rc).exp()*geo(g1,1)*B0+(beta/2).exp()*geo(g2,1)*B1)/(1-thstar)
Delta=(sum((v**2 for v in Del_rows.values()),arb(0))+far2).sqrt()
Xn=(sum((v**2 for v in X_rows.values()),arb(0))).sqrt()
Tn=(Tn+farT)*NS
res=dict(typ=typ,m=m,a=a,b=b,params=P,states=idx,NS=NS,K0=K0,rho=rho_s,K=K,K2=K2,beta=beta_s,prec=ctx.prec,Nmax=Nmax,Rmax=Rmax,D=D,
         tailT=float(tailT.upper()),delta1=float(delta1.upper()),delta2=float(delta2.upper()),
         Delta=float(Delta.upper()),Xnorm=float(Xn.upper()),trace_norm=float(Tn.upper()),far2=float(far2.upper()),
         classes={str(j):c for j,c in enumerate(classes)},provenance=prov,sectors={})
print('Delta',res['Delta'],'||X||',res['Xnorm'],'trace',res['trace_norm'],round(time.time()-t0,1),'s',flush=True)
json.dump(res,open(outp+'.json','w'),indent=1)
U=2.0**-53
def acb_to_mr(Mx):
    n_=Mx.nrows(); m_=Mx.ncols(); mid=np.zeros((n_,m_),complex); rad=np.zeros((n_,m_))
    for i in range(n_):
        for j in range(m_):
            v=Mx[i,j]; re=v.real; im=v.imag
            aa=float(re.mid()); bb=float(im.mid()); mid[i,j]=complex(aa,bb)
            r=float(re.rad())+float(im.rad())
            rad[i,j]=r*(1+4*U)+U*(abs(aa)+abs(bb))*(1+4*U)+1e-300
    return mid,rad
for jc,cname in enumerate(classes):
    t1=time.time(); cyc=cycs[cname]
    Amid=np.zeros((D,D),complex); Arad=np.zeros((D,D))
    for c2 in cores:
        agg={}
        for n in range(-Nmax,Nmax+1):
            if (c2,n) not in blocks: continue
            j2,Bk=blocks[(c2,n)]; x=arb(n)
            w=gh(n)*e(Cc*x*x/2)
            for (so,sg,ph8,tw) in finite(P,idx,tg,n,cyc):
                key=(j2,sg,so)
                ph=e(-arb(ph8)/16+arb(n*tw)/7)
                term=Bk*(w*ph)
                agg[key]=term if key not in agg else agg[key]+term
        for (j2,sg,so),Mx in agg.items():
            mid,rad=acb_to_mr(Mx)
            Ko=Kc[c2]; Ki=Kc[j2]; r0=off[c2]+so*Ko; q0=off[j2]+sg*Ki
            assert not Amid[r0:r0+Ko,q0:q0+Ki].any()
            Amid[r0:r0+Ko,q0:q0+Ki]=mid; Arad[r0:r0+Ko,q0:q0+Ki]=rad
    np.save(outp+f'_b{jc}_mid.npy',Amid); np.save(outp+f'_b{jc}_rad.npy',Arad)
    radF=float(np.sqrt((Arad**2).sum())*(1+1e-10))
    res['sectors'][str(jc)]=dict(cls=cname,rad_fro=radF,mid_fro=float(np.linalg.norm(Amid)),secs=round(time.time()-t1,1))
    print('class',jc,cname,res['sectors'][str(jc)],flush=True)
    json.dump(res,open(outp+'.json','w'),indent=1)
res['secs']=round(time.time()-t0,1); json.dump(res,open(outp+'.json','w'),indent=1); print('done',res['secs'],flush=True)
