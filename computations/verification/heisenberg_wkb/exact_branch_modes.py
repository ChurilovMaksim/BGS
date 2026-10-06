"""Individual four-periodic Fourier modes; extended lattice only, no illicit gluing."""
from exact_controls import *

def branch(m,N,ell):
 if (m,N) not in [(1,3),(2,3),(3,7),(4,3),(4,9)] or len(ell) != m or any(type(v) is not int or abs(v)>9 for v in ell):
  raise ValueError("outside certified exact int64 fixture bounds")
 B=matrix(m);D=int(B.det()); Adj=np.array(B.adjugate()).astype(np.int64);b=np.array(B).astype(np.int64)
 H=hermite_normal_form(B);reps=np.array(list(itertools.product(*(range(int(H[i,i])) for i in range(m)))),dtype=np.int64)
 r=np.arange(m)%4;t=r-3*np.roll(r,1);a=N*t+np.array(ell,dtype=np.int64)
 L=4*N;C=2*L*D
 # Split first axis to cap memory; exact integer histogram.
 p=np.zeros(C,dtype=np.int64)
 tail=np.array(list(itertools.product(range(L),repeat=m-1)),dtype=np.int64).reshape(-1,m-1) if m>1 else np.zeros((1,0),dtype=np.int64)
 for j0 in range(L):
  j=np.column_stack([np.full(len(tail),j0,dtype=np.int64),tail])
  num=D*(-np.einsum('ij,jk,ik->i',j,b,j)+2*j@a)
  p+=np.bincount(num%C,minlength=C)
 w=L*reps+a
 q=np.bincount((np.einsum('ij,jk,ik->i',w,Adj,w)-m*(C//8))%C,minlength=C)
 if m==4:diff=24*(np.roll(p,C//8)+np.roll(p,-C//8))-L*L*q
 elif m==3 and N==7:
  sq=sum((np.roll(q,(k*k%7)*(C//7)-C//4) for k in range(7)),np.zeros(C,dtype=np.int64));diff=14*p-8*N*sq
 elif m==2:diff=4*(np.roll(p,C//8)+np.roll(p,-C//8))-L*q
 elif m==1 and N==3:
  sq=sum((np.roll(q,(k*k%3)*(C//3)-C//4) for k in range(3)),np.zeros(C,dtype=np.int64));diff=2*p-2*sq
 else:raise ValueError()
 if any(reduce_poly(diff,C)): raise RuntimeError((m,N,ell))
 return dict(m=m,N=N,r=r.tolist(),ell=ell,a=a.tolist(),det=D,gcd=math.gcd(D,N),extended_lattice_count=L**m,quotient_count=D,cyclotomic_remainder_zero=True)
def main():
 results=[]
 for m,N in [(1,3),(2,3),(3,7),(4,3),(4,9)]:
  for ell in [[(-1)**i*(i+1) for i in range(m)],[3-2*i for i in range(m)]]:
   z=branch(m,N,ell);results.append(z);print(z,flush=True)
 print(json.dumps(results,indent=2)+'\n')

if __name__ == '__main__':
 main()
