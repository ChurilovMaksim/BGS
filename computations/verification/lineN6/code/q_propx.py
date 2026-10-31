"""N6 (1) [P+CA bookkeeping]: explicit error of Prop X (sector-4 window/excursion factorisation) from the certified constants of
n_cert.json and Line F certV_eta2_a4_tight; returns the block half-window w0 and p0 beyond which |error| <= Re(w*)_lo / 2.
All arithmetic in arb (upward)."""
import json, math
from flint import arb, ctx
ctx.prec=128
c=json.load(open('/workspace/bgs-lineN/N6/logs/n_cert.json'))
lf=json.load(open('/workspace/bgs-lineF/logs/certV_eta2_a4_tight.json'))
mu=arb('1.9154712'); lam=3+2*arb(2).sqrt(); b=arb(2).sqrt()/4; pi=arb.pi()
Pert=arb(c['Pert']); F=arb(lf['sectors']['4']['b21'])+Pert; FR2=arb(lf['sectors']['4']['F_R2'])
R2=FR2/F*arb('1.0000001'); R2p=R2/(1-FR2)
Pi=arb(c['normPi']); N1=arb(c['N1']); T1=arb(lf['trace_norm'])/mu
Gc=max(arb(c['rA']['GT']),arb(c['rB']['GT']))*arb('1.001')
Cpow=Pi+R2p
KK=18; sig_t=b*lam**(-KK)*lam/(lam-1)
eps0=(Cpow*2*pi*N1*sig_t/mu).exp()-1
Gb=Cpow**2*(1+eps0)**2*Gc
rmax=arb('0.3066'); Rew=arb('2.8895e-4')
def E(w):
    sc=2*b*lam**(-w)*lam/(lam-1); so=2*b*lam**(-(w//2))*lam/(lam-1)
    cont=Gb**2*((Gb*2*pi*N1*sc/mu).exp()-1)
    coll=2*Gb*R2p*mu**(-(w//2))*Gb
    outer=Gb**2*((Gb*2*pi*N1*so/mu).exp()-1)
    epsw=(Cpow*2*pi*N1*so/mu).exp()-1
    rtail=Pi*Gb*((1+epsw)**2-1)
    eta=cont+coll+outer+rtail
    x=Pi*rmax
    return 6*(T1*Gb+1)*eta*(x+eta)**5, eta
w=10
while True:
    e,eta=E(w)
    if e<Rew/2: break
    w+=1
res=dict(Cpow=float(Cpow.upper()),R2p=float(R2p.upper()),Gb=float(Gb.upper()),T1=float(T1.upper()),w0=w,p0=4*w+5,err_at_w0=float(e.upper()),eta=float(eta.upper()),
         Re_w_lo=float(Rew),note='blocks: 6 per m=3p; half-window w >= floor(((p-1)/2-1)/2) => p >= 4w+5')
print(json.dumps(res,indent=1)); json.dump(res,open('/workspace/bgs-lineN/N6/logs/q_propx.json','w'),indent=1)
