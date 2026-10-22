import json,pathlib,sympy as sp
if not __debug__:raise RuntimeError("Assertions must be enabled")
D=pathlib.Path(__file__).parent

def mm(A,B,p):return [[sum(a*b for a,b in zip(row,col))%p for col in zip(*B)] for row in A]
def inv(A,p):
 n=len(A);M=[row[:]+[int(i==j) for j in range(n)] for i,row in enumerate(A)]
 for k in range(n):
  r=next(r for r in range(k,n) if M[r][k]);M[r],M[k]=M[k],M[r];v=pow(M[k][k],-1,p);M[k]=[x*v%p for x in M[k]]
  for i in range(n):
   if i!=k:
    c=M[i][k];M[i]=[(x-c*y)%p for x,y in zip(M[i],M[k])]
 return [row[n:] for row in M]
def scale(A,c,p):return [[x*c%p for x in row] for row in A]
def diag(v):return [[x if i==j else 0 for j in range(len(v))]for i,x in enumerate(v)]
records=[]
for N in [21,63,77,91,133,203]:
 p=next(4*N*k+1 for k in range(1,1000) if sp.isprime(4*N*k+1));g=int(sp.primitive_root(p));q=pow(g,(p-1)//N,p);ii=pow(g,(p-1)//4,p)
 if (-3-4*ii)%p==0:ii=(-ii)%p
 L=N//7;l=L%7;h=pow(2,-1,N);a=(1-h)%N;w=pow(q,L,p);inv8=pow(8,-1,N)
 def raw(x,y):return pow(q,-inv8*(3*x*x-2*x*y+3*y*y)%N,p)
 def block(r,s):return [[raw((a+L-1-r+j*L)%N,(a+s+k*L)%N)for k in range(7)]for j in range(7)]
 def bond(u,j):
  z=pow(q,u+j*L,p);r=-(pow(z,7,p)-1)**2*(z+1)**2*pow(4*pow(z,8,p)%p,-1,p)%p
  return (-3-4*ii)*r%p
 A,B,C,T=block(0,0),block(0,1),block(1,0),block(1,1);Ai=inv(A,p)
 Al=[[pow(w,(-3*l*(j*j+k*k)+2*l*j*k+(l+4)*j+(2*l+3)*k)%7,p)for k in range(7)]for j in range(7)]
 assert A==scale(Al,A[0][0],p)
 d1=diag([pow(bond(1,j),-1,p)for j in range(7)]);dl=diag([pow(bond(L-1,j),-1,p)for j in range(7)])
 theta=pow(q,-pow(4,-1,N),p)*pow(w,2*pow(L,-1,7),p)%p
 assert theta!=1 and T==scale(mm(mm(C,Ai,p),B,p),theta,p)
 J=mm(mm(Ai,dl,p),C,p);K=mm(mm(Ai,B,p),d1,p)
 U=diag([pow(w,2*j,p)for j in range(7)]);Ui=diag([pow(w,-2*j,p)for j in range(7)])
 Sc=diag([sum(pow(-w*pow(w,j,p)%p,k,p)*pow(q,6-k,p)for k in range(7))**2%p for j in range(7)])
 Sq=diag([sum(pow(-q*pow(w,j,p)%p,k,p)for k in range(7))**2%p for j in range(7)])
 JB=mm(mm(mm(Ai,Sc,p),A,p),Ui,p);KB=mm(mm(mm(mm(Ai,U,p),A,p),U,p),Sq,p)
 ij=next((i,j)for i in range(7)for j in range(7)if JB[i][j]);i,j=ij;lam=J[i][j]*pow(JB[i][j],-1,p)%p
 assert lam and J==scale(JB,lam,p)and K==scale(KB,lam*pow(w,2,p)%p,p)
 R=diag([sp.prod(bond(u,j)for u in range(1,L))%p for j in range(7)])
 E0=mm(R,A,p);E1=mm(mm(R,B,p),d1,p);F0=mm(mm(R,dl,p),C,p);F1=mm(mm(mm(R,dl,p),T,p),d1,p)
 assert F1==scale(mm(mm(F0,inv(E0,p),p),E1,p),theta,p)
 rec={'N':N,'L_mod7':l,'prime':p,'raw_fourier_dictionary':True,'raw_and_gauged_cross_ratio':True,'normalized_JK_common_scalar':True};records.append(rec);print(rec,flush=True)
assert sorted(x['L_mod7']for x in records)==list(range(1,7))
(D/'dictionary_results.json').write_text(json.dumps(records,indent=2)+'\n')
