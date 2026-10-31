"""[CA] (v2, J3-F7: outward rounding of the enclosure to exact Fractions) arg(xi21)/2pi is not a rational a/b with b < b_min: smallest denominator in the certified enclosure (Stern-Brocot search, exact Fractions
against arb endpoints rounded outward)."""
import json, math, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
from fractions import Fraction as Fr
from flint import arb, acb, ctx
ctx.prec=200
mus=acb(arb('1.3572399242659728227708727178601298'),arb('-1.3516424762972735896036200390941797')); r_mus=arb('2e-6')+arb('1e-15')
c=json.load(open('../logs/cert/V_2_s4_b1_disc.json'))['best']; mu21=acb(c['center'][0],c['center'][1]); r21=arb(c['r'])+arb('1e-15')
u=(r_mus/(abs(mus)-r_mus)).asin()+(r21/(abs(mu21)-r21)).asin(); th0=mus.arg()+mu21.arg()
tw=2*arb.pi(); x=th0/tw; lo=x-u/tw; hi=x+u/tw
k=math.floor(float(lo.lower())); assert lo-k>0 and hi-k<1          # enclosure inside one unit interval
L=Fr(math.nextafter(float((lo-k).lower()),-math.inf)); H=Fr(math.nextafter(float((hi-k).upper()),math.inf))   # outward: L <= true lo, H >= true hi
# smallest-denominator fraction in [L,H] (mod 1 shift)
def simplest(L,H):
    a=L.numerator//L.denominator
    if Fr(a)>=L and Fr(a)<=H: return Fr(a)
    if a+1<=H: return Fr(a+1)
    r=simplest(1/(H-a),1/(L-a)); return a+1/r
s=simplest(L,H)
out=dict(interval=[float(L),float(H)],simplest=str(s),b_min=s.denominator)
print(out); json.dump(out,open('logs/rat_excl.json','w'))
