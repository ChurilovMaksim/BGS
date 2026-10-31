"""N8: Prop X' explicit (class (z,e) version of N6 q_propx.py; same error architecture, all arb upward).
For an isotropic class with seed cores zeta_A, zeta_B (Lemma P'), certificate logs/n8_cert_TAG.json:
  |Zhat_x/Z_rho - w(z,e)| <= E_e(w) for half-window w, where versus the family case
  - contamination/tail scale b -> b_e = max_{cores, embeddings} |zeta| (tails are |zeta| lam^{-j}, Lemma P'),
  - core norm bound G_c -> max(GT_A, GT_B) of the class certificate, r_max -> max |r| + radius,
  - half-window w >= floor(((p-1)/2 - 1)/2) - L_e,  L_e = ceil(log_lam(b_e/b + 1)) (window shift).
Usage: q_propx2.py TAG tau [TAG tau ...]; prints p0(e,tau) = least p with E_e <= tau."""
import json, math, sys
from flint import arb, ctx
ctx.prec=128
lf=json.load(open('/workspace/bgs-lineF/logs/certV_eta2_a4_tight.json'))
mu=arb('1.9154712'); lam=3+2*arb(2).sqrt(); b=arb(2).sqrt()/4; pi=arb.pi(); r2=arb(2).sqrt()
out={}
args=sys.argv[1:]
for i in range(0,len(args),2):
    tag=args[i]; tau=arb(args[i+1])
    c=json.load(open(f'/workspace/bgs-lineN/N8/logs/n8_cert_{tag}.json'))
    ea,eb=c['e']; e1=abs(arb(ea)+arb(eb)*r2); e2=abs(arb(ea)-arb(eb)*r2); eps=1+r2
    be=max(e1,e2)*eps/(4*r2)     # |zeta| <= |e| eps /(4 sqrt2) over both seeds and embeddings (|eps^{+-1}| <= eps)
    s=max(be/b,arb(1))
    Le=math.ceil(float((s+1).log().upper()/lam.log().lower()))
    Pert=arb(c['Pert']); F=arb(lf['sectors']['4']['b21'])+Pert; FR2=arb(lf['sectors']['4']['F_R2'])
    R2=FR2/F*arb('1.0000001'); R2p=R2/(1-FR2)
    Pi=arb(c['normPi']); N1=arb(c['N1']); T1=arb(lf['trace_norm'])/mu
    Gc=max(arb(c['rA']['GT']),arb(c['rB']['GT']))*arb('1.001')
    Cpow=Pi+R2p; KK=c['KK']
    sig_t=s*b*lam**(-KK)*lam/(lam-1)
    eps0=(Cpow*2*pi*N1*sig_t/mu).exp()-1
    Gb=Cpow**2*(1+eps0)**2*Gc
    rmax=max(abs(complex(*c['rA']['value']))+c['rA']['radius'],abs(complex(*c['rB']['value']))+c['rB']['radius'])
    rmax=arb(rmax)*arb('1.000001')
    def E(w):
        sc=2*s*b*lam**(-w)*lam/(lam-1); so=2*s*b*lam**(-(w//2))*lam/(lam-1)
        cont=Gb**2*((Gb*2*pi*N1*sc/mu).exp()-1)
        coll=2*Gb*R2p*mu**(-(w//2))*Gb
        outer=Gb**2*((Gb*2*pi*N1*so/mu).exp()-1)
        epsw=(Cpow*2*pi*N1*so/mu).exp()-1
        rtail=Pi*Gb*((1+epsw)**2-1)
        eta=cont+coll+outer+rtail
        x=Pi*rmax
        return 6*(T1*Gb+1)*eta*(x+eta)**5
    w=10
    while not (E(w)<tau): w+=1
    p0=4*(w+Le)+5
    out[tag]=dict(e=c['e'],s=float(s.upper()),L_e=Le,Gb=float(Gb.upper()),rmax=float(rmax.upper()),tau=args[i+1],w0=w,p0=p0,E_w0=float(E(w).upper()),
                  absw_upper=c['absw_upper'],Re_w=[c['Re_w_lower'],c['Re_w_upper']])
    print(tag,json.dumps(out[tag]),flush=True)
json.dump(out,open('/workspace/bgs-lineN/N8/logs/q_propx2_'+'_'.join(args[0::2])[:80]+'.json','w'),indent=1)
