"""Line L2 (a)/(b): barrier constants, arb [CA]."""
from flint import arb, ctx
ctx.prec=100
x=arb('1.8'); G=abs(x.bessel_j(0))+2*sum((abs(x.bessel_j(a)) for a in range(1,80)),arb(0))
lam=3+2*arb(2).sqrt(); xi=arb('2.4586893'); mu=arb('1.9154753'); mu16=arb('1.6677')
t8=arb('1.28359'); t16=arb('1.4742')
out=dict(G=G, G2_over_t8sq=G**2/t8**2, G2_over_t16sq=G**2/t16**2, G_over_t8=G/t8, G_over_t16=G/t16,
 mu2_over_t8sq=mu**2/t8**2, mu16sq_over_t16sq=mu16**2/t16**2, Lm8=mu**2/xi, Lm16=mu16**2/xi,
 lam13=lam**(arb(1)/3), lam12=lam.sqrt(), rabs='1.0511158 [N]')
for k,v in out.items(): print(k, v if isinstance(v,str) else v.str(8))
