"""Referee: recompute w* = -(rA rB)^3 from the N6 boxes (rect. balls) with python-flint acb, and recompute q_propx E(w), p0
independently from the printed constants (upper bounds), plus the margin of F_m vs 4m*phi/delta for p>=1165."""
from flint import arb, acb, ctx
import json
ctx.prec=200
def box(re,im,r): return acb(arb(re,r),arb(im,r))
rA=box('0.1751797516056337','0.16837443765078877','0.003225324395231572')
rB=box('-0.17859356709279434','0.24364103113127292','0.003211650728668734')
w=-(rA*rB)**3
out=dict(w_re=[float(w.real.lower()),float(w.real.upper())],w_im=[float(w.imag.lower()),float(w.imag.upper())],
 cstar=[float(abs(w).lower()),float(abs(w).upper())])
# arg: use the 4 corners of the rectangle (w rect is in 4th quadrant, Re>0)
import math
re=out['w_re']; im=out['w_im']
out['arg_range']=[math.atan2(im[0],re[0]),math.atan2(im[1],re[1])]
# E(w) recomputation from N6 constants
Pi=arb('21.968115036763887'); Cpow=arb('3246.806275804417'); R2p=arb('3224.8381607676533'); Gb=arb('390538488.38817495'); T1=arb('381.18144385777515')
N1=arb('573.59386436705001185'); mu=arb('1.9154712'); lam=3+2*arb(2).sqrt(); b=arb(2).sqrt()/4; pi=arb.pi()
def E(w):
    sc=2*b*lam**(-w)*lam/(lam-1); so=2*b*lam**(-(w//2))*lam/(lam-1)
    cont=Gb**2*((Gb*2*pi*N1*sc/mu).exp()-1); coll=2*Gb*R2p*mu**(-(w//2))*Gb
    outer=Gb**2*((Gb*2*pi*N1*so/mu).exp()-1); epsw=(Cpow*2*pi*N1*so/mu).exp()-1
    rtail=Pi*Gb*((1+epsw)**2-1); eta=cont+coll+outer+rtail; x=Pi*arb('0.3066')
    return 6*(T1*Gb+1)*eta*(x+eta)**5, dict(cont=float(cont.upper()),coll=float(coll.upper()),outer=float(outer.upper()),rtail=float(rtail.upper()))
for w0 in (280,289,290,300):
    e,parts=E(w0); out[f'E({w0})']=float(e.upper()); out[f'parts({w0})']=parts
# which term dominates; Rew/2
out['Rew_lo/2']=2.8895e-4/2
# F_m vs 4 m phi/delta : F_m >= 2.3e-3 p |Z8|^2 / h_p ; |Z8| >= 0.5(1-lam^-m)(mu^m-3012.3); phi<=h_m=h_p(4h_p^2+3)
# need 2.3e-3 p |Z8|^2/h_p >= 4*3p*h_m/delta  <=>  |Z8|^2 >= (12/2.3e-3) h_p^2 (4h_p^2+3)/delta
import mpmath as mp
mp.mp.dps=50
eps=1+mp.sqrt(2); L=3+2*mp.sqrt(2); MU=mp.mpf('1.9154712')
def hp(p): return (eps**p+(-1)**(p+1)*eps**(-p))/2  # x-coordinate? check below
rows=[]
for p in (1165,1171,2000,5000):
    m=3*p; Z8=mp.mpf('0.5')*(1-L**(-m))*(MU**m-mp.mpf('3012.3'))
    h=mp.floor(eps**p/2+mp.mpf('0.5'))
    lhs=mp.log10(Z8**2); rhs=mp.log10(mp.mpf(12)/mp.mpf('2.3e-3')*h**2*(4*h**2+3))
    rows.append(dict(p=p,log10_Z8sq=float(lhs),log10_needed_times_delta=float(rhs),log10_margin=float(lhs-rhs)))
out['Fm_vs_4m_phi']=rows
print(json.dumps(out,indent=1)); json.dump(out,open('logs/ref_wstar.json','w'),indent=1)
