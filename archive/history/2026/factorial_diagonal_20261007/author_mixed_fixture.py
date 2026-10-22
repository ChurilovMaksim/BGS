"""Exact cut-port controls and independent full-End interface checks."""
from fractions import Fraction as F
from itertools import product, permutations
from functools import reduce
import json
import numpy as np

def mm(A,B):return [[sum(x*y for x,y in zip(r,c)) for c in zip(*B)] for r in A]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def power(A,k):
    B=eye(len(A))
    for _ in range(k):B=mm(B,A)
    return B

def refl(v):
    n=len(v);s=sum(x*x for x in v)
    return [[F(i==j)-F(2*v[i]*v[j],s) for j in range(n)] for i in range(n)]
def exact(n,l,r):
    m=l+r; U=mm(refl(list(range(1,n+1))),refl([i*i for i in range(n,0,-1)]));P=[[u*u for u in row] for row in U]
    # Nonnormal doubly stochastic Q, distinct from P.
    Q=[[F(1,3)*F(i==j)+F(2,3)*F(i==(j+1)%n) for j in range(n)] for i in range(n)]
    sigma=list(range(1,l))+[0]+list(range(l+1,m))+[l];pi=list(range(1,m))+[0]
    words=list(product(range(n),repeat=m));direct=F(0)
    for x in words:
        for y in words:
            direct+=reduce(lambda z,i:z*Q[x[i]][y[i]]*U[y[sigma[i]]][x[i]]*U[y[pi[i]]][x[i]],range(m),F(1))
    K=mm(P,Q);A=power(K,l-1);B=power(K,r-1)
    W=lambda a,c,b:sum(Q[x][b]*U[a][x]*U[c][x] for x in range(n))
    cut=sum(A[b][a]*B[d][c]*W(a,c,b)*W(c,a,d) for a,c,b,d in product(range(n),repeat=4))
    T=[[K[i][j]-F(1,n) for j in range(n)] for i in range(n)];L=power(T,l-1);R=power(T,r-1)
    err=sum(L[b][a]*R[d][c]*W(a,c,b)*W(c,a,d) for a,c,b,d in product(range(n),repeat=4))
    trace=lambda X:sum(X[i][i] for i in range(n))
    expanded=F(1,n)+trace(power(T,l))/n+trace(power(T,r))/n+err
    assert direct==cut==expanded
    return {'N':n,'l':l,'r':r,'direct':str(direct),'repeated_port_constant':str(F(1,n)),'exact_equalities':True}

def tensor(xs):return reduce(np.kron,xs,np.ones((1,1)))
def full_end(n,l,r):
    m=l+r;words=list(product(range(n),repeat=m));index={w:i for i,w in enumerate(words)};D=n**m
    def perm(p):
        A=np.zeros((D,D))
        for j,w in enumerate(words):A[index[tuple(w[p[i]] for i in range(m))],j]=1
        return A
    V=np.column_stack([perm(p).reshape(-1) for p in permutations(range(m))]);h,s,_=np.linalg.svd(V,full_matrices=False);h=h[:,s>1e-9]
    I=np.eye(D).reshape(-1);diag=np.column_stack([np.diag(np.eye(D)[i]).reshape(-1)-np.diag(np.eye(D)[-1]).reshape(-1) for i in range(D-1)])
    Y=diag-h@(h.T@diag);q,_=np.linalg.qr(Y)
    a=np.arange(1,n+1);b=np.arange(n,0,-1)**2
    U=(np.eye(n)-2*np.outer(a,a)/(a@a))@np.diag([1j**j for j in range(n)])@(np.eye(n)-2*np.outer(b,b)/(b@b));Ub=tensor([U]*m)
    sig=list(range(1,l))+[0]+list(range(l+1,m))+[l];p=list(range(1,m))+[0];Cs=perm(sig);Cp=perm(p)
    action=lambda X:(Cs@Ub@X.reshape(D,D)@Ub.conj().T@Cp.T).reshape(-1)
    direct=sum(np.vdot(q[:,j],action(q[:,j])) for j in range(q.shape[1]))
    J=np.column_stack([np.diag(np.eye(D)[i]).reshape(-1) for i in range(D)])
    H=J.T@h@h.T@J;Hc=H-np.ones((D,D))/D
    BR=J.T@np.column_stack([action(J[:,i]) for i in range(D)])
    HR=J.T@np.column_stack([(Cs@(h@(h.T@J[:,i])).reshape(D,D)@Cp.T).reshape(-1) for i in range(D)])
    compressed=np.trace(np.linalg.solve(np.eye(D)-Hc,BR-HR));assert abs(compressed-direct)<1e-10
    assert np.linalg.norm((BR-HR)@np.ones(D))<1e-10
    assert np.linalg.norm(np.ones(D)@(BR-HR))<1e-10
    return {'N':n,'l':l,'r':r,'direct_real':float(direct.real),'direct_imag':float(direct.imag),'interface_error':float(abs(compressed-direct)),'R_not_conjugation':True}

def main():
    out={'exact_ports':[exact(n,l,r) for n,l,r in [(2,2,2),(2,2,3),(3,2,2)]],'full_end':[full_end(n,l,r) for n,l,r in [(2,2,2),(2,2,3),(3,2,2)]]}
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
