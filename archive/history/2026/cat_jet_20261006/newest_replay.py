#!/usr/bin/env python3
"""Independent raw-symbol/coherent-packet and polynomial determinant audit.
No author verifier imports. Exact finite field K=F5[w]/(1+w+...+w^6).
"""
import itertools,json,time,hashlib,sys,platform
from pathlib import Path
from fractions import Fraction
ROOT=Path(__file__).resolve().parent

def need(b,msg):
 if not b: raise RuntimeError(msg)
class Field:
 def __init__(self,mod):
  self.mod=mod; self.digits=[tuple((i//5**j)%5 for j in range(6)) for i in range(15625)]
  self.small=[[sum(((i//5**j+jv//5**j)%5)*5**j for j in range(3)) for jv in range(125)] for i in range(125)]
  self.neg=[sum((-d%5)*5**j for j,d in enumerate(ds)) for ds in self.digits]
  self.g=next(g for g in range(5,100) if all(self.rawpow(g,15624//p)!=1 for p in [2,3,7,31]))
  self.ex=[];a=1
  for k in range(15624):self.ex.append(a);a=self.rawmul(a,self.g)
  need(a==1 and len(set(self.ex))==15624,'Field generator enumeration')
  self.log=[-1]*15625
  for k,a in enumerate(self.ex):self.log[a]=k
 def add(self,a,b):return self.small[a%125][b%125]+125*self.small[a//125][b//125]
 def sub(self,a,b):return self.add(a,self.neg[b])
 def rawmul(self,a,b):
  p=[0]*11
  for i,x in enumerate(self.digits[a]):
   for j,y in enumerate(self.digits[b]):p[i+j]+=x*y
  for i in range(10,5,-1):
   c=p[i]%5
   for j in range(6):p[i-6+j]-=c*self.mod[j]
  return sum(p[j]%5*5**j for j in range(6))
 def rawpow(self,a,n):
  r=1
  while n:
   if n&1:r=self.rawmul(r,a)
   a=self.rawmul(a,a);n//=2
  return r
 def mul(self,a,b):return self.ex[(self.log[a]+self.log[b])%15624] if a and b else 0
 def pow(self,a,n):
  if not a:need(n>=0,'negative zero power');return int(n==0)
  return self.ex[self.log[a]*n%15624]
 def inv(self,a):need(a!=0,'inverse zero');return self.pow(a,-1)
 def sum(self,seq):
  r=0
  for a in seq:r=self.add(r,a)
  return r
 def mm(self,A,B):return [[self.sum(self.mul(a,b) for a,b in zip(row,col)) for col in zip(*B)] for row in A]
 def inverse(self,A):
  n=len(A);B=[r[:]+[int(i==j) for j in range(n)] for i,r in enumerate(A)]
  for c in range(n):
   r=next((r for r in range(c,n) if B[r][c]),None);need(r is not None,'singular basis');B[c],B[r]=B[r],B[c]
   s=self.inv(B[c][c]);B[c]=[self.mul(s,x) for x in B[c]]
   for r in range(n):
    if r!=c:
     s=B[r][c];B[r]=[self.sub(x,self.mul(s,y)) for x,y in zip(B[r],B[c])]
  need(all(B[i][j]==int(i==j) for i in range(n) for j in range(n)),'inverse residual')
  return [r[n:] for r in B]
 def rank(self,A):
  A=[r[:] for r in A];r=0
  for c in range(len(A[0])):
   k=next((k for k in range(r,len(A)) if A[k][c]),None)
   if k is None:continue
   A[r],A[k]=A[k],A[r];u=self.inv(A[r][c]);A[r]=[self.mul(u,x) for x in A[r]]
   for k in range(r+1,len(A)):
    u=A[k][c];A[k]=[self.sub(x,self.mul(u,y)) for x,y in zip(A[k],A[r])]
   r+=1
   if r==len(A):break
  return r
 def trim(self,p):
  while len(p)>1 and p[-1]==0:p.pop()
  return p
 def rem(self,p,q):
  p=p[:]
  while len(p)>=len(q) and p!=[0]:
   u=self.mul(p[-1],self.inv(q[-1]));k=len(p)-len(q)
   for j,v in enumerate(q):p[k+j]=self.sub(p[k+j],self.mul(u,v))
   self.trim(p)
  return p
 def gcd(self,p,q):
  while q!=[0]:p,q=q,self.rem(p,q)
  return [self.mul(x,self.inv(p[-1])) for x in p]
 def charpoly(self,C):
  # Polynomial determinant by subset expansion, not evaluation/interpolation.
  n=len(C);dp={0:[1]}
  for mask in range(1<<n):
   if mask not in dp:continue
   k=mask.bit_count()
   if k==n:continue
   for j in range(n):
    if mask>>j&1:continue
    sign=4 if (mask>>(j+1)).bit_count()%2 else 1
    a=self.mul(sign,self.neg[C[k][j]]);b=sign if k==j else 0
    p=dp[mask];q=[0]*(len(p)+1)
    for t,x in enumerate(p):q[t]=self.add(q[t],self.mul(a,x));q[t+1]=self.add(q[t+1],self.mul(b,x))
    new=mask|1<<j
    if new not in dp:dp[new]=[0]*len(q)
    dp[new]=[self.add(x,y) for x,y in zip(dp[new],q)]
  return dp[(1<<n)-1]

def raw_symbol():
 # Exact expansion of r(q), sin(q), cos(p-alpha), plus the centered q terms.
 R={0:Fraction(1),1:Fraction(1,2),-1:Fraction(1,2),6:Fraction(-1,4),-6:Fraction(-1,4),7:Fraction(-1,2),-7:Fraction(-1,2),8:Fraction(-1,4),-8:Fraction(-1,4)}
 D={}
 def add(a,b,re=0,im=0):
  x,y=D.get((a,b),(0,0));D[(a,b)]=(x+re,y+im)
 for b,r in R.items():
  add(0,b,r/10);add(0,b+1,im=-r/200);add(0,b-1,im=r/200)
  add(1,b,-3*r/1000,-4*r/1000);add(-1,b,-3*r/1000,4*r/1000)
 add(0,7,Fraction(1,2));add(0,-7,Fraction(1,2));add(0,0,-Fraction(1,10))
 out={}
 for u,(x,y) in D.items():
  if x or y:
   x*=4000;y*=4000;need(x.denominator==1 and y.denominator==1,'coefficient denominator');out[u]=(int(x),int(y))
 need(len(out)==32 and (0,0) not in out,'raw symbol cardinality')
 return out

def act(v,h):a,b=v;return ((3*a+4*b)%h,(2*a+3*b)%h)
def norm(v,h):a,b=v;return (2*b*b-a*a)%h

def main():
 start=time.time();F=Field([1]*6);A=Field([1,0,1,3,1,0]);w=5;xi=F.pow(F.g,2604);omega=F.pow(xi,2)
 need(F.pow(w,7)==1 and w!=1 and F.pow(xi,6)==1 and F.pow(xi,3)!=1 and F.pow(xi,2)!=1,'root orders')
 aw=A.pow(5,9);axi=A.pow(9,2604)
 def convert(x):return A.sum(A.mul(d,A.pow(aw,k)) for k,d in enumerate(F.digits[x]))
 xi_image=convert(xi);xi_index=next(k for k in [1,5] if A.pow(axi,k)==xi_image)
 wp=[F.pow(w,k) for k in range(7)]
 G=[[wp[(-(3*x*x-2*x*y+3*y*y))%7] for y in range(7)] for x in range(7)]
 tr=F.sum(G[j][j] for j in range(7));H=[[F.mul(x,F.inv(tr)) for x in row] for row in G]
 H2=F.mm(H,H);H3=F.mm(H,H2);need(H3==[[int(i==j) for j in range(7)] for i in range(7)],'H7 order')
 # Projector-column bases, different construction from author nullspaces.
 columns=[];labels=[];ranks=[]
 for z in [1,omega,F.pow(omega,2)]:
  P=[[F.mul(2,F.sum([int(i==j),F.mul(F.inv(z),H[i][j]),F.mul(F.pow(z,-2),H2[i][j])])) for j in range(7)] for i in range(7)]
  cols=[]
  for col in zip(*P):
   trial=cols+[list(col)]
   if F.rank(trial)>len(cols):cols=trial
  ranks.append(len(cols));columns+=cols;labels += [z]*len(cols)
 need(ranks==[3,2,2],'seven multiplicities');V=[list(r) for r in zip(*columns)];Vi=F.inverse(V)
 need(F.mm(H,V)==[[F.mul(V[i][j],labels[j]) for j in range(7)] for i in range(7)],'eigenbasis')
 D=raw_symbol();upper=sorted(u for u in D if u[0]==1)
 need(all((re+2*im)%5==0 for (a,b),(re,im) in D.items() if a!=1),'i=2 surviving modes')
 B={}
 for a,b in upper:
  T=[[wp[b*(x+4*a)%7] if y==(x+a)%7 else 0 for y in range(7)] for x in range(7)]
  B[(a,b)]=F.mm(Vi,F.mm(T,V))
 author=json.loads((ROOT/'inputs/new_layer_coherent_residue.json').read_text())['records'];lookup={(r['generic_l_ge2'],r['norm_mod5'],r['tame_index']):r for r in author}
 records=[]
 for deep in [False,True]:
  for c in range(1,5):
   v=min(v for v in itertools.product(range(5),repeat=2) if norm(v,5)==c);orb=[]
   for _ in range(6):orb.append(v);v=act(v,5)
   need(len(set(orb))==6 and v==orb[0],'F5 orbit');idx={v:k for k,v in enumerate(orb)}
   for tau in range(6):
    gamma=[F.mul(F.pow(xi,tau),F.inv(z)) for z in labels];C=[[0]*7 for _ in range(7)]
    for a,b in upper:
     if deep and (4*c-norm((a,b),5))%5==0:continue
     weights=[[0]*7 for _ in range(7)]
     for ky,y in enumerate(orb):
      x=((y[0]+a)%5,(y[1]+b)%5)
      if x not in idx:continue
      kx=idx[x]
      for i in range(7):
       for j in range(7):weights[i][j]=F.add(weights[i][j],F.mul(F.pow(gamma[i],kx),F.pow(gamma[j],-ky)))
     du=(D[(a,b)][0]+2*D[(a,b)][1])%5
     for i in range(7):
      for j in range(7):C[i][j]=F.add(C[i][j],F.mul(du,F.mul(B[(a,b)][i][j],weights[i][j])))
    p=F.charpoly(C);der=[F.mul(k%5,p[k]) for k in range(1,8)];gd=F.gcd(p,F.trim(der));need(len(gd)==1,'nonsquarefree residue')
    converted=[convert(x) for x in p];ar=lookup[deep,c,xi_index*tau%6];need(converted==ar['characteristic_ascending'],'author polynomial mismatch')
    records.append({'l_ge_2':deep,'norm_mod5':c,'tame_index':tau,'characteristic_ascending_phi7':p,'gcd_degree':len(gd)-1,'author_tame_index':xi_index*tau%6})
 print('Independent 48 polynomial determinants passed; exact field-isomorphism match.',flush=True)
 output={'status':'passed','arithmetic':'F5[w]/(1+w+w²+w³+w4+w5+w6), polynomial determinants by subset expansion','field_generator':F.g,'sixth_root':xi,'author_xi_index':xi_index,'seven_ranks':ranks,'symbol':[{'a':u[0],'b':u[1],'gaussian_4000':d,'i2_residue':(d[0]+2*d[1])%5} for u,d in sorted(D.items())],'records':records,'python':sys.version,'platform':platform.platform(),'duration_seconds':time.time()-start}
 (ROOT/'finite_results.json').write_text(json.dumps(output,indent=2)+'\n')
if __name__=='__main__':main()
