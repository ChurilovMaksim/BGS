"""Line I (2): rigorous bound on the d=7 twisted sums and the dilation SQUARE term for rho=(2,8), m ≡ 9 (mod 24).
From rig_spec v4 'rest' certificates (spectrum of the lifted core comparison op. + perturbation inside |z|<R):
  sup_{|z|=R} ||(z-L)^{-1}|| <= G/(1-F),  G = (SY_R + 1/R)(1 + ||X||/R) + 1/R  (kappa=1),  F = pert*G  (decided < 1 in arb)
  ||L^n|| <= R^{n+1} G/(1-F)  (Cauchy),   |Tr(B L^m)| <= ||L||_1 ||L^{m-1}|| ||B||,  ||B|| = ||e_(0,0)|| ||1_{i=0}|| = 4.
  |Zhat(beta)| <= |TrB V^m| + |TrB E^m|  (lifted partial-trace identity, prefactor <= 1).
  Square term (Prop I2): d sum_u |delta_u|^2 <= ((2d-1)/d) sum_{beta≠0} |Zhat(beta)|^2 <= (13/7)*48*max_beta |Zhat|^2
  (Zhat constant on the 8 classes of beta≠0 under beta -> ±lam beta).  Contribution to W' (F units) <= that / phi(h)  (h odd, phi(2h)=phi(h)).
  phi(h) >= h/(e^gamma lnln h + 2.50637/lnln h)  (Rosser-Schoenfeld 1962, h >= 3).
All JSON floats padded upward by (1+2^-40); stored *_upper values are already rounded up."""
import json, sys, math, glob, hashlib
from flint import arb, ctx
ctx.prec=128
PAD=1+arb(2)**-40
def U(x): return arb(float(x))*PAD
cls=['1:3','2:1','0:1','1:2','1:5','0:3','1:0','0:2']
lam=3+2*arb(2).sqrt()
def lat(typ,c):
    t=c.replace(':','_'); b=json.load(open(f'data/{typ}_{t}.json')); r=json.load(open(f'logs/{typ}_{t}_rest.json'))
    best=None
    for s in r['scan']:
        if not s.get('certified'): continue
        R=arb(s['R']); SY=U(s['SY_R']); X=U(b['Xnorm']); G=(SY+1/R)*(1+X/R)+1/R
        pert=U(b['delta1'])+U(b['delta2'])+U(b['Delta'])+U(r['epsA'])
        F=pert*G; assert F<1
        C=4*U(b['trace_norm'])*G/(1-F)          # |TrB L^m| <= C R^m
        cand=(R,C,F)
        if best is None or float(R.mid())<float(best[0].mid()): best=cand
    return best
rows=[]; done=[]
for c in cls:
    try: V=lat('V',c); E=lat('E',c)
    except FileNotFoundError: continue
    if V is None or E is None: print(c,'NOT certified'); continue
    done.append(c); rows.append((c,V,E))
    print(c,'V: R=%s C<=%.4g F=%.3g | E: R=%s C<=%.4g F=%.3g'%(V[0].str(5),float(V[1].upper()),float(V[2].upper()),E[0].str(5),float(E[1].upper()),float(E[2].upper())))
if len(done)<8: print('classes certified:',done,'-> theorem needs all 8'); 
if rows:
    RV=max((r[1][0] for r in rows),key=lambda x:float(x.mid())); CV=max((r[1][1] for r in rows),key=lambda x:float(x.upper()))
    RE=max((r[2][0] for r in rows),key=lambda x:float(x.mid())); CE=max((r[2][1] for r in rows),key=lambda x:float(x.upper()))
    print('uniform over certified classes: |Zhat| <= %.4g * %s^m + %.4g * %s^m'%(float(CV.upper()),RV.str(5),float(CE.upper()),RE.str(5)))
    g=(RV**2/lam.sqrt()); print('decay ratio of square-term/phi: R^2/sqrt(lam) =',g.str(10))
    eg=arb('0.5772156649015328606065120900824024310422').exp()
    out=[]
    for m in [9+24*j for j in range(0,60)]:
        x,y=1,0
        for _ in range(m): x,y=3*x+8*y,x+3*y
        h=math.isqrt((2*(x-1))//4); H=arb(h); ll=H.log().log()
        phi_lo=H/(eg*ll+arb('2.50637')/ll)
        Zm=CV*RV**m+CE*RE**m
        sq=arb(13)/7*48*Zm**2
        out.append((m,sq/phi_lo))
    for m,v in out[::6]: print('m=%d  square-term contribution to W\' (F units) <= %.3e'%(m,float(v.upper())))
    first=next((m for m,v in out if v<arb('0.01')),None); print('first m (≡9 mod 24, <=1425) with bound < 0.01:',first)
    json.dump(dict(classes=done,RV=RV.str(10),CV=float(CV.upper()),RE=RE.str(10),CE=float(CE.upper()),ratio=g.str(10),
        table={m:float(v.upper()) for m,v in out},code_sha256=hashlib.sha256(open(__file__,'rb').read()).hexdigest()),open('logs/bounds_sq.json','w'),indent=1)
