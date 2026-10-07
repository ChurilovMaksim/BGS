"""Matched multi-cycle support control. Silent on import."""
import itertools,json
import numpy as np
from check_mixed import tensor

def check(n):
    m=4;words=list(itertools.product(range(n),repeat=m));ix={w:i for i,w in enumerate(words)};dim=n**m
    def perm(p):
        A=np.zeros((dim,dim))
        for j,w in enumerate(words):A[ix[tuple(w[p[i]] for i in range(m))],j]=1
        return A
    Z=np.column_stack([perm(p).reshape(-1) for p in itertools.permutations(range(m))]);h,s,_=np.linalg.svd(Z,full_matrices=False);h=h[:,s>1e-9]
    loc=[np.eye(n)/np.sqrt(n)]
    for k in range(1,n):
        a=np.zeros(n);a[:k]=1;a[k]=-k;loc.append(np.diag(a/np.sqrt(k*(k+1))))
    labels=[w for w in itertools.product(range(n),repeat=m) if any(w)]
    D=np.column_stack([tensor([loc[j] for j in w]).reshape(-1) for w in labels]);Y=D-h@(h.T@D)
    rng=np.random.default_rng(310+n);raw=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));U,_=np.linalg.qr(raw);Ub=tensor([U]*m);C=perm([1,0,3,2]);action=lambda v:(C@Ub@v.reshape(dim,dim)@Ub.conj().T@C.T).reshape(-1)
    q,_=np.linalg.qr(Y);full=sum(np.vdot(q[:,j],action(q[:,j])) for j in range(q.shape[1]));selected=0j;excluded=0
    for k in range(1,m+1):
        for S in itertools.combinations(range(m),k):
            ids=[j for j,w in enumerate(labels) if tuple(i for i,x in enumerate(w) if x)==S];ys=Y[:,ids];val=np.trace(np.linalg.solve(ys.T@ys,ys.T@np.column_stack([action(ys[:,j]) for j in range(ys.shape[1])])))
            if S in [(0,1),(2,3),(0,1,2,3)]:selected+=val
            else:excluded=max(excluded,abs(val))
    assert abs(full-selected)<1e-10 and excluded<1e-10
    return {'N':n,'cycles':[2,2],'full_real':float(full.real),'full_imag':float(full.imag),'union_support_error':float(abs(full-selected)),'excluded_support_max':float(excluded)}
def main():print(json.dumps([check(2),check(3)],indent=2))
if __name__=='__main__':main()
