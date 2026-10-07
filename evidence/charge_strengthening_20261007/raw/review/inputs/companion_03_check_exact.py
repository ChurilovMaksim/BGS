#!/usr/bin/env python3
"""Bounded exact controls, auxiliary unitaries only. No external packages."""
import argparse, hashlib, itertools, json, math
from collections import defaultdict
from pathlib import Path

Z=(0,0); O=(1,0); I=(0,1)
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def conj(a): return (a[0],-a[1])
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(a,s): return (a[0]*s,a[1]*s)
def ipow(k): return [(1,0),(0,1),(-1,0),(0,-1)][k%4]
def check(ok,msg):
    if not ok: raise RuntimeError(msg)
def mm(A,B):
    return [[sumg(mul(A[i][k],B[k][j]) for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def sumg(xs):
    a=Z
    for b in xs:a=add(a,b)
    return a
def power(A,m):
    n=len(A);B=[[O if i==j else Z for j in range(n)] for i in range(n)]
    for _ in range(m): B=mm(B,A)
    return B
def tr(A):return sumg(A[j][j] for j in range(len(A)))
def dense_u(N):
    v=list(range(1,N+1));w=list(range(N,0,-1));a=sum(t*t for t in v);b=sum(t*t for t in w)
    Hv=[[((a if i==j else 0)-2*v[i]*v[j],0) for j in range(N)] for i in range(N)]
    Hw=[[((b if i==j else 0)-2*w[i]*w[j],0) for j in range(N)] for i in range(N)]
    mid=[[mul(Hv[i][j],ipow(j)) for j in range(N)] for i in range(N)]
    U=mm(mid,Hw); d=a*b
    for i in range(N):
      for j in range(N):
        check(sumg(mul(U[i][k],conj(U[j][k])) for k in range(N))==((d*d if i==j else 0),0),'unitary')
    check(all(v!=Z for row in U for v in row),'dense fixture')
    return U,d

def prune(D):return {k:v for k,v in D.items() if v!=Z}
def delta(j,c,N):
    a=[0]*N;a[j]+=1;a[(j+c)%N]-=1;return tuple(a)
def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def feature(x,y,N):
    c=tuple((b-a)%N for a,b in zip(x,y));m=len(c)
    d=[0]*N
    for a,b in zip(x,y):d[a]+=1;d[b]-=1
    return tuple(d),sum(v!=0 for v in c),sum(c[j]!=c[(j+1)%m] for j in range(m))
def direct_table(U,N,m):
    words=list(itertools.product(range(N),repeat=m)); amps={}
    for x in words:
        a=O
        for j in range(m):a=mul(a,U[x[j]][x[(j+1)%m]])
        amps[x]=a
    D=defaultdict(lambda:Z);witnesses={};fiber=defaultdict(lambda:Z);balance=defaultdict(lambda:Z);off=defaultdict(lambda:Z)
    for x in words:
      for y in words:
        w=mul(amps[x],conj(amps[y]));key=feature(x,y,N)
        D[key]=add(D[key],w);c=tuple((b-a)%N for a,b in zip(x,y));fiber[c]=add(fiber[c],w)
        target=off if any(key[0]) else balance;target[c]=add(target[c],w)
        if sum(c)%N==0 and any(key[0]) and w!=Z:
            witnesses.setdefault('checksum_zero_offcharge',{'x':x,'y':y,'charge':c,'weight_numerator':w})
    for c in fiber:check(add(off[c],balance[c])==fiber[c],'fiber projection')
    return prune(D),len(words)**2,witnesses

def super_matrix_from_units(U,N):
    # Independent U E U* multiplication, charge basis read afterward.
    states=[(c,j) for c in range(N) for j in range(N)]; B=[[Z]*(N*N) for _ in states]
    star=[[conj(U[j][i]) for j in range(N)] for i in range(N)]
    for col,(d,k) in enumerate(states):
        E=[[Z for _ in range(N)] for _ in range(N)];E[k][(k+d)%N]=O
        A=mm(mm(U,E),star)
        for row,(c,j) in enumerate(states):
            B[row][col]=A[j][(j+c)%N]
            check(B[row][col]==mul(U[j][k],conj(U[(j+c)%N][(k+d)%N])),'block dictionary')
    return states,B

def transfer_table(states,B,N,m):
    size=N*N;feat=[delta(j,c,N) for c,j in states];D=defaultdict(lambda:Z)
    for start in range(size):
      # Each partial walk includes contributions from departed vertices only.
      dp={(start,(0,)*N,0,0):O}
      for step in range(m):
        nxt=defaultdict(lambda:Z)
        for (row,occ,h,s),a in dp.items():
          c,_=states[row];occ1=plus(occ,feat[row]);h1=h+(c!=0)
          targets=[start] if step==m-1 else range(size)
          for col in targets:
            d,_=states[col];key=(col,occ1,h1,s+(c!=d));nxt[key]=add(nxt[key],mul(a,B[row][col]))
        dp=prune(nxt)
      for (row,occ,h,s),a in dp.items():
        check(row==start,'trace closure');key=(occ,h,s);D[key]=add(D[key],a)
    return prune(D)

def evaluate_table(table,m,phase_exponents,q_exp,znum=1,zden=3,derivative=False):
    # The common z denominator is zden^m, also for derivative.
    total=Z
    for (occ,h,s),a in table.items():
      if derivative:
        if not s:continue
        weight=s*znum**(s-1)*zden**(m-s+1)
      else:weight=znum**s*zden**(m-s)
      theta=sum(o*p for o,p in zip(occ,phase_exponents))
      total=add(total,scale(mul(a,ipow(theta+q_exp*h)),weight))
    return total

def scalar_transfer(states,B,N,znum=1,zden=3,qexp=1):
    phase=[j*j+2*j for j in range(N)];M=[];der=[]
    for row,(c,j) in enumerate(states):
      ph=ipow(qexp*(c!=0)+phase[j]-phase[(j+c)%N]);line=[];dline=[]
      for col,(d,k) in enumerate(states):
        v=mul(ph,B[row][col]);line.append(scale(v,zden if c==d else znum));dline.append(scale(v,0 if c==d else zden))
      M.append(line);der.append(dline)
    return M,der,phase

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--inject-failure',action='store_true');args=ap.parse_args()
    check(not args.inject_failure,'injected failure remains active under -O')
    out={'arithmetic':'Gaussian integer numerators, positive common denominators; exact integers only','scope':'auxiliary dense complex rational unitaries; no actual-tau numerics; no asymptotic certification','cases':[]};total=0
    for N,maxm in [(2,5),(3,4),(5,3)]:
      U,d=dense_u(N);states,B=super_matrix_from_units(U,N);M,dM,phase=scalar_transfer(states,B,N)
      Bstar=[[conj(B[j][i]) for j in range(N*N)] for i in range(N*N)]
      gram=mm(Bstar,B)
      for i in range(N*N):
        for j in range(N*N):
          check(gram[i][j]==((d**4 if i==j else 0),0),'full superoperator unitarity')
      for c in range(1,N):
        for j in range(N):
          check(sumg(B[c*N+j][k] for k in range(N))==Z,'right zero-run annihilation')
          check(sumg(B[k][c*N+j] for k in range(N))==Z,'left zero-run annihilation')
      # Both transfer and adjoint fix the identity for arbitrary phase/q twists.
      ident=[O if c==0 else Z for c,j in states]
      for row in range(N*N):
        check(sumg(mul(M[row][k],ident[k]) for k in range(N*N))==scale(ident[row],3*d*d),'right identity')
        check(sumg(mul(conj(M[k][row]),ident[k]) for k in range(N*N))==scale(ident[row],3*d*d),'left identity')
      for m in range(1,maxm+1):
        direct,count,witness=direct_table(U,N,m);transfer=transfer_table(states,B,N,m);check(direct==transfer,'full occupation/Hamming/switch polynomial')
        check(evaluate_table(direct,m,phase,1)==tr(power(M,m)),'scalar transfer evaluation')
        ut=tr(power(U,m))
        check(evaluate_table(direct,m,[0]*N,0,znum=1,zden=1)==mul(ut,conj(ut)),'undamped actual trace dictionary')
        deriv=scale(tr(mm(power(M,m-1),dM)),m)
        check(evaluate_table(direct,m,phase,1,derivative=True)==deriv,'cyclic noncommuting derivative')
        off_byhs=defaultdict(lambda:Z);bal_byhs=defaultdict(lambda:Z);full_byhs=defaultdict(lambda:Z)
        for (occ,h,s),a in direct.items():
            key=(h,s);full_byhs[key]=add(full_byhs[key],a);dst=off_byhs if any(occ) else bal_byhs;dst[key]=add(dst[key],a)
        for key in full_byhs:check(full_byhs[key]==add(off_byhs[key],bal_byhs[key]),'torus projection')
        check(all(a==Z for (h,s),a in off_byhs.items() if h==0),'zero charge offcharge empty')
        # The all-zero occupation coefficient is exact torus integration.
        zeroeval=sumg(a for (occ,h,s),a in direct.items() if not any(occ))
        check(zeroeval==sumg(bal_byhs.values()),'balanced coefficient')
        out['cases'].append({'N':N,'m':m,'ordered_pairs':count,'nonzero_monomials':len(direct),'offcharge_hs_coefficients':len(prune(off_byhs)),'witnesses':witness});total+=count
    cat=[]
    for N in [3,5,7,11]:
      h=pow(2,-1,N)
      for c in range(1,N):
        counts=[sum((c*k)%N==a for k in range(N)) for a in range(N)]
        check(len(set(counts))==1,'cat B square character zero')
        # B_c(j,k)=N^-1 e_N(h*c*(j+k+c)), an outer product of two N-vectors of norm sqrt(N).
        for j in range(N):
          for k in range(N):
            check((h*c*(j+k+c))%N==((h*c*j)+(h*c*(k+c)))%N,'cat outer product entries')
            for ell in range(N):
              check((h*c*(j+k+c)+h*c*(k+ell+c)-h*c*(j+ell+2*c))%N==(c*k)%N,'cat square character factor')
        cat.append({'N':N,'c':c,'rank':1,'norm_squared':1,'square_zero':True})
    out['total_ordered_pairs']=total;out['cat_prime_controls']=cat
    out['sha256_source']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
