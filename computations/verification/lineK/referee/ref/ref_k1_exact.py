# Referee: exact check of K1 in Z[zeta_q] for every delta-mass A=delta_x (identity is linear in A), every t_b.
# q^2 * [ sum_{beta!=0} e(Tr(beta x)/q) W_beta ]  vs  q^2*[1_{N(x)=0} - (2q-1)/q^2 - (e(-N(x)t_b/q) - 1/q)/q]
# Elements of Z[zeta] as integer vectors of length q; equal iff difference is a constant vector.
import numpy as np, sys
def check(q):
    b1,b2=np.meshgrid(np.arange(q),np.arange(q),indexing='ij'); b1=b1.ravel(); b2=b2.ravel()
    nz=~((b1==0)&(b2==0)); b1=b1[nz]; b2=b2[nz]; Nb=(b1*b1-2*b2*b2)%q
    inv=np.array([0]+[pow(t,-1,q) for t in range(1,q)])
    bad=0; tot=0
    for x1 in range(q):
        for x2 in range(q):
            a=(2*(b1*x1+2*b2*x2))%q
            Nx=(x1*x1-2*x2*x2)%q
            M=np.zeros((q,q),np.int64)       # M[t,k] = #beta with a + N(beta) t^-1 = k
            for t in range(1,q):
                M[t]=np.bincount((a+Nb*inv[t])%q,minlength=q)
            S=M[1:].sum(0)
            for tb in range(1,q):
                lhs=S-M[tb]
                rhs=np.zeros(q,np.int64)
                rhs[0]+= (q*q if Nx==0 else 0) -(2*q-1) + 1
                rhs[(-Nx*tb)%q]-=q
                d=lhs-rhs; tot+=1
                if not (d==d[0]).all(): bad+=1
    return bad,tot
for q in map(int,sys.argv[1:]):
    bad,tot=check(q); print(q,'q mod 8 =',q%8,' cases',tot,' mismatches',bad,flush=True)
