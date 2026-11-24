"""Independent word enumeration and transfer comparison on small unitary matrices."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import itertools, json
import numpy as np
def run(U,m,t):
    n=len(U);P=abs(U)**2;J=np.ones((n,n))/n
    rho=np.linalg.norm(P-J,2)
    powU=[np.linalg.matrix_power(U,j) for j in range(m+1)]
    D=m-2*t+1
    words=np.array(list(itertools.product(range(n),repeat=m)))
    A=np.prod(U[words,np.roll(words,-1,axis=1)],axis=1)
    cyc=np.hstack((words,words[:,:1]))
    match=np.all(cyc[:,None,:t+1]==cyc[None,:,:t+1],axis=2)
    allweights=A[:,None]*A.conj()[None,:]
    H=np.linalg.matrix_power(P,t); maxerr=0;sum_full=0j;maxboundslack=0
    for g in range(D):
        h=D-1-g
        for gp in range(D):
            if g==gp:continue
            hp=D-1-gp
            mask=match & np.all(cyc[:,None,t+g:2*t+g+1]==cyc[None,:,t+gp:2*t+gp+1],axis=2)
            brute=np.sum(allweights[mask])
            form=np.trace(H@(powU[g]*powU[gp].conj())@H@(powU[h]*powU[hp].conj()))
            leading=abs(np.trace(powU[abs(g-gp)]))**2/n**2
            maxerr=max(maxerr,abs(form-brute))
            maxboundslack=max(maxboundslack,abs(form-leading)-2*rho**t-n*rho**(2*t))
            sum_full+=leading
    gram=sum(abs(np.trace(powU[abs(g-gp)]))**2/n**2 for g in range(D) for gp in range(D))
    assert maxerr<1e-12 and maxboundslack<1e-12
    assert gram+1e-10>=D**2/n and abs(sum_full+D-gram)<1e-10
    return dict(N=n,m=m,t=t,max_word_vs_transfer=float(maxerr),gram=float(gram),diagonal_lower=D**2/n)
U=np.diag([1,1j])@np.array([[3,4],[-4,3]])/5
V=np.exp(2j*np.pi*np.outer(np.arange(3),np.arange(3))/3)/np.sqrt(3)
print(json.dumps([run(U,7,2),run(V,5,1)],indent=2))
