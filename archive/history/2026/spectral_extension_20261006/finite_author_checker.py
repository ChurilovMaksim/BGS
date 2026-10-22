#!/usr/bin/env python3
"""Finite exact-dyadic certificate of A simplicity and leading spectral M minors.
All scientific acceptance uses Python integer arithmetic with directed rounding.
No floating point eigensolver, trigonometry, or decision enters certification.
M is scaled by sqrt(N); eigenvectors are deliberately left unnormalised.
"""
if not __debug__:
 raise RuntimeError("Certification requires assertions; do not use -O/-OO or PYTHONOPTIMIZE.")
import argparse, json, math, time, hashlib, platform
from fractions import Fraction
from pathlib import Path

P=512; S=1<<P

def ceildiv(a,b):return -((-a)//b)
class I:
 __slots__=('l','h')
 def __init__(self,l,h=None):self.l=l;self.h=l if h is None else h;assert self.l<=self.h
 @classmethod
 def rat(cls,n,d=1):
  if d<0:n,d=-n,-d
  return cls(n*S//d,ceildiv(n*S,d))
 def __add__(a,b):
  if not isinstance(b,I):b=I.rat(b)
  return I(a.l+b.l,a.h+b.h)
 __radd__=__add__
 def __neg__(a):return I(-a.h,-a.l)
 def __sub__(a,b):return a+-b
 def __rsub__(a,b):return -a+b
 def __mul__(a,b):
  if not isinstance(b,I):b=I.rat(b)
  v=[a.l*b.l,a.l*b.h,a.h*b.l,a.h*b.h]
  return I(min(v)//S,ceildiv(max(v),S))
 __rmul__=__mul__
 def __truediv__(a,b):
  if not isinstance(b,I):b=I.rat(b)
  if b.l<=0<=b.h:raise ArithmeticError('Real interval division by possible zero')
  v=[(aa*S,bb) for aa in (a.l,a.h) for bb in (b.l,b.h)]
  return I(min(n//d for n,d in v),max(ceildiv(n,d) for n,d in v))
 def square(a):
  lo=0 if a.l<=0<=a.h else min(a.l*a.l,a.h*a.h)
  return I(lo//S,ceildiv(max(a.l*a.l,a.h*a.h),S))
 def sign(a):
  if a.l>0:return 1
  if a.h<0:return -1
  raise ArithmeticError('Indeterminate sign')
 def width(a):return a.h-a.l
 def serialize(a):return [str(a.l),str(a.h)]
 def lower_abs(a):return max(0,a.l,-a.h)

class C:
 __slots__=('r','i')
 def __init__(self,r=None,i=None):self.r=I.rat(0) if r is None else r;self.i=I.rat(0) if i is None else i
 def __add__(a,b):return C(a.r+b.r,a.i+b.i)
 def __neg__(a):return C(-a.r,-a.i)
 def __sub__(a,b):return a+-b
 def __mul__(a,b):return C(a.r*b.r-a.i*b.i,a.r*b.i+a.i*b.r)
 def conj(a):return C(a.r,-a.i)
 def __truediv__(a,b):
  d=b.r.square()+b.i.square()
  if d.l<=0:raise ArithmeticError('Complex pivot may be zero')
  return C((a.r*b.r+a.i*b.i)/d,(a.i*b.r-a.r*b.i)/d)
 def serialize(a):return {'real':a.r.serialize(),'imag':a.i.serialize()}
 def lower_abs(a):return max(a.r.lower_abs(),a.i.lower_abs())


def atan_recip(n):
 # Alternating-series bound from exact rational partial sums.
 s=Fraction(0);k=0
 while True:
  s+=Fraction((-1)**k,(2*k+1)*n**(2*k+1));k+=1
  rem=Fraction(1,(2*k+1)*n**(2*k+1))
  if rem*S<1:break
 lo,hi=(s,s+rem) if k%2==0 else (s-rem,s)
 return I(I.rat(lo.numerator,lo.denominator).l,I.rat(hi.numerator,hi.denominator).h)

def trig_grid(N):
 pi=16*atan_recip(5)-4*atan_recip(239)
 assert 3*S<pi.l<pi.h<4*S
 # Taylor truncations at degree 2K and 2K+1. Remainders bounded by
 # |x|^(2K+1)/(2K+1)! and |x|^(2K+2)/(2K+2)!, |x|<=4.
 K=1
 while Fraction(4**(2*K+1),math.factorial(2*K+1))*S>1:K+=1
 out=[]
 for j in range(N):
  jj=j if 2*j<=N else j-N
  if jj==0:out.append((I.rat(1),I.rat(0)));continue
  x=pi*I.rat(2*jj,N);xx=x.square();c=I.rat(1);ss=x;ct=I.rat(1);st=x
  for k in range(1,K+1):
   ct=-ct*xx/(2*k*(2*k-1));st=-st*xx/(2*k*(2*k+1));c=c+ct;ss=ss+st
  c=I(c.l-1,c.h+1);ss=I(ss.l-1,ss.h+1)
  out.append((c,ss))
 return out,pi,K

def chains(N,trig):
 h=pow(2,-1,N);r=[];diag=[]
 for x in range(N):
  c,s=trig[x];c7=trig[7*x%N][0]
  rr=(1-c7)*(1+c);r.append(rr)
  diag.append(c7+rr/10+rr*s/100-I.rat(1,10))
 cuts=[x for x in range(N) if 7*((x+h)%N)%N==0];L=N//len(cuts);out=[]
 for cut in cuts:
  inds=[(cut+1+j)%N for j in range(L)]
  ds=[diag[x] for x in inds];bs=[r[(x+h)%N]/200 for x in inds[:-1]]
  assert all(b.l>0 for b in bs)
  out.append((inds,ds,bs))
 return out

def sturm_count(ds,bs,q):
 a=I.rat(1);b=ds[0]-q;sgn=b.sign();vari=int(sgn<0);old=sgn
 for j in range(1,len(ds)):
  a,b=b,(ds[j]-q)*b-bs[j-1].square()*a
  sgn=b.sign();vari+=int(sgn!=old);old=sgn
 return vari

def isolate_roots(ds,bs,target_bits):
 # Root-independent global bound ||A||<=79/50<2; all bisections exact.
 roots=[];target=1<<(P-target_bits)
 for k in range(len(ds)):
  lo=-2*S;hi=2*S
  assert sturm_count(ds,bs,I(lo))==0 and sturm_count(ds,bs,I(hi))==len(ds)
  while hi-lo>target:
   mid=(lo+hi)//2
   try:c=sturm_count(ds,bs,I(mid))
   except ArithmeticError:
    # Try two nearby rational points; no unproved sign is accepted.
    success=False
    for mid in ((3*lo+hi)//4,(lo+3*hi)//4):
     try:c=sturm_count(ds,bs,I(mid));success=True;break
     except ArithmeticError:pass
    if not success:raise ArithmeticError('Sturm endpoint uncertainty; raise precision or reduce target bits')
   if c<=k:lo=mid
   else:hi=mid
  assert sturm_count(ds,bs,I(lo))==k and sturm_count(ds,bs,I(hi))==k+1
  roots.append(I(lo,hi))
 return roots

def run(N,target_bits):
 started=time.time();trig,pi,K=trig_grid(N);chs=chains(N,trig)
 if N==7:raise ValueError('N7 exact degeneracy handled separately')
 roots=[]
 for ci,(inds,ds,bs) in enumerate(chs):
  for ri,lam in enumerate(isolate_roots(ds,bs,target_bits)):roots.append((lam,ci,ri))
 roots.sort(key=lambda x:x[0].l,reverse=True)
 assert all(roots[j][0].l>roots[j+1][0].h for j in range(N-1))
 print(f'N={N}: all eigenvalues certified distinct',flush=True)
 eta=C(I.rat(-3,5),I.rat(4,5));phases=[C(I.rat(1))]
 for j in range(1,len(chs[0][0])):phases.append(phases[-1]*eta)
 vectors=[]
 for lam,ci,ri in roots:
  inds,ds,bs=chs[ci];v=[I.rat(1)]
  if len(ds)>1:v.append((lam-ds[0])/bs[0])
  for j in range(1,len(ds)-1):v.append(((lam-ds[j])*v[-1]-bs[j-1]*v[-2])/bs[j])
  vectors.append([(x,C(vv)*phases[j]) for j,(x,vv) in enumerate(zip(inds,v))])
 inv8=pow(8,-1,N)
 G=[[C(*trig[(-inv8*(3*x*x-2*x*y+3*y*y))%N]) for y in range(N)] for x in range(N)]
 H=[]
 for left in vectors:
  row=[]
  for right in vectors:
   val=C()
   for x,vx in left:
    for y,vy in right:val=val+vx.conj()*G[x][y]*vy
   row.append(val)
  H.append(row)
 print(f'N={N}: spectral-basis matrix enclosed',flush=True)
 pivots=[]
 for k in range(N):
  pivot=H[k][k];lb=pivot.lower_abs()
  if lb<=0:raise ArithmeticError(f'N={N}: pivot{k+1} interval contains zero')
  pivots.append(pivot.serialize())
  for i in range(k+1,N):
   rat=H[i][k]/pivot
   for j in range(k+1,N):H[i][j]=H[i][j]-rat*H[k][j]
 print(f'N={N}: all {N} leading pivots certified nonzero',flush=True)
 gaps=[roots[j][0].l-roots[j+1][0].h for j in range(N-1)]
 return {'N':N,'arithmetic':'exact outward-rounded dyadic intervals using Python integers','precision_bits':P,'root_target_bits':target_bits,'pi_interval':pi.serialize(),'taylor_K':K,'sqrt_N_factor_omitted':True,'unnormalized_eigenvectors':True,'chain_indices':[c[0] for c in chs],'ordered_roots':[{'interval':lam.serialize(),'chain':ci,'chain_root_ascending':ri} for lam,ci,ri in roots],'min_eigenvalue_gap_lower_dyadic':str(min(gaps)),'pivots':pivots,'all_eigenvalues_distinct':True,'all_ordered_leading_minors_nonzero':True,'wall_seconds':time.time()-started}

def main():
 global P,S
 ap=argparse.ArgumentParser();ap.add_argument('--N',type=int,nargs='+',default=[21,35,49,63]);ap.add_argument('--precision',type=int,default=512);ap.add_argument('--root-bits',type=int,default=384);ap.add_argument('--out',default='certificates');args=ap.parse_args();P=args.precision;S=1<<P
 assert 0<args.root_bits<P-16
 out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
 for N in args.N:
  assert N>7 and N%14==7
  data=run(N,args.root_bits);data['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();data['python']=platform.python_version()
  dest=out/f'N{N}.json';dest.write_text(json.dumps(data,indent=2)+'\n');print(f'Saved {dest}',flush=True)
if __name__=='__main__':main()
