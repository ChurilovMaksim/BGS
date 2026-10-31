"""[CA] rotation angle for the big modulus M* (window lemma on the subsequence m = j + M* k): theta* = M* arg(xi21) mod 2pi, enclosure."""
import sys, json, math, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))   # J3-F7: all paths relative to J3/
from flint import arb, acb, ctx
ctx.prec=200
J=json.load(open('../logs/assemble_v2.json'))
mus=acb(arb('1.3572399242659728227708727178601298'),arb('-1.3516424762972735896036200390941797')); r_mus=arb('2e-6')+arb('1e-15')
c=json.load(open('../logs/cert/V_2_s4_b1_disc.json'))['best']; mu21=acb(c['center'][0],c['center'][1]); r21=arb(c['r'])+arb('1e-15')
u=(r_mus/(abs(mus)-r_mus)).asin()+(r21/(abs(mu21)-r21)).asin(); th0=mus.arg()+mu21.arg()
out={}
if len(sys.argv)<2: sys.exit("usage: theta_big.py M1 [M2 ...]  (refuses to overwrite logs/theta_big.json with an empty result)")
for Ms in sys.argv[1:]:
    M=int(Ms); th=M*th0; tw=2*arb.pi(); k=math.floor(float((th/tw).mid())); thm=th-tw*k
    lo=thm-M*u; hi=thm+M*u
    out[Ms]=dict(theta_lo=float(lo.lower()),theta_hi=float(hi.upper()),halfwidth=float((M*u).upper()))
    print(Ms,out[Ms])
json.dump(out,open('logs/theta_big.json','w'),indent=1)
