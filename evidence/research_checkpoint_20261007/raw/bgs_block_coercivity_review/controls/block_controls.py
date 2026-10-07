#!/usr/bin/env python3
"""Independent, bounded controls. Exact arithmetic is separated from diagnostics."""
import json, time, platform
import numpy as np
import scipy
from scipy.linalg import block_diag, expm
import sympy as sp
import mpmath as mp

SEED = 202610070142
rng = np.random.default_rng(SEED)

def phi(A):
    s = np.linalg.svd(A, compute_uv=False)
    return float(np.sum(np.logaddexp(s, -s) - np.log(2)))

def lift(A):
    L, s, Rh = np.linalg.svd(A)
    W = (L * np.arctanh(s)) @ Rh
    CL = (L / np.sqrt(1-s*s)) @ L.conj().T
    CR = (Rh.conj().T / np.sqrt(1-s*s)) @ Rh
    return W, CL, CR

def haar(n):
    q, r = np.linalg.qr(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))
    return q @ np.diag(np.diag(r)/abs(np.diag(r)))

def floating_controls():
    minima = {}; maxima = {}; counts = {}; cases = 0
    def low(name, value):
        minima[name] = min(minima.get(name, float('inf')), float(value))
    def high(name, value):
        maxima[name] = max(maxima.get(name, 0.), float(value))
    def one(U, zs, family):
        nonlocal cases
        n=len(zs); k=zs[0].shape[0]; m=n*k
        P=abs(U)**2; J=np.ones((n,n))/n
        rho=float(np.linalg.norm(P-J,2)); C=max(1., n*float(P.max()))
        K=1+np.sqrt(C-1)/(1-rho)
        I=np.eye(m); Q=np.kron(U,np.eye(k)); Z=block_diag(*zs)
        H=-float(np.linalg.slogdet(I-Z@Z.conj().T)[1])
        S=float(np.linalg.slogdet(I-Q@Z@Q.conj().T@Z.conj().T)[1])+H
        data=[lift(z) for z in zs]; ws=np.array([v[0] for v in data])
        W=block_diag(*ws); CL=block_diag(*[v[1] for v in data]); CR=block_diag(*[v[2] for v in data])
        X=np.block([[np.zeros((m,m)),W],[W.conj().T,np.zeros((m,m))]])
        g=np.block([[CL,Z@CR],[Z.conj().T@CL,CR]])
        gi=np.block([[CL,-Z@CR],[-Z.conj().T@CL,CR]])
        T=gi@block_diag(Q,Q)@g
        F=CL@(Q-Z@Q@Z.conj().T)@CL
        G=CL@(Q@Z-Z@Q)@CR
        t=np.maximum(np.log(np.linalg.svd(T,compute_uv=False)[:m]),0.)
        d=W-Q@W@Q.conj().T
        s=np.linalg.svd(d,compute_uv=False)
        vs=ws-np.einsum('ij,jab->iab',P,ws)
        pin=block_diag(*vs); ps=np.linalg.svd(pin,compute_uv=False)
        R=np.linalg.inv(np.eye(n)-P+J)
        w0=ws-ws.mean(axis=0)
        modular=sum(phi(v) for v in vs)
        centered=sum(phi(v) for v in w0)
        original=sum(phi(v) for v in ws)
        scart=float(np.sum(np.logaddexp(t,-t)-np.log(2)))
        high('centering_residual',np.linalg.norm(sum(zs)))
        high('maximum_nonnormality',max(np.linalg.norm(z@z.conj().T-z.conj().T@z) for z in zs))
        high('maximum_P_asymmetry',np.linalg.norm(P-P.T))
        high('boost_relative_error',np.linalg.norm(expm(X)-g)/(1+np.linalg.norm(g)))
        high('block_T_relative_error',np.linalg.norm(T[:m]-np.hstack([F,G]))/(1+np.linalg.norm(T[:m])))
        high('J_unitary_relative_error',np.linalg.norm(F@F.conj().T-G@G.conj().T-I)/(1+np.linalg.norm(F)**2+np.linalg.norm(G)**2))
        high('action_Cartan_relative_error',abs(S-scart)/(1+abs(S)))
        high('H_2phi_relative_error',abs(H-2*original)/(1+H))
        high('inverse_identity_error',np.linalg.norm(np.einsum('ij,jab->iab',R,vs)-w0)/(1+np.linalg.norm(w0)))
        low('theorem_margin',S-H/(2*K*K))
        low('all_KyFan_EMI_margin',min(np.cumsum(t)-np.cumsum(s)))
        low('all_KyFan_pinching_margin',min(np.cumsum(s)-np.cumsum(ps)))
        low('action_modular_margin',S-modular)
        low('row_inverse_margin',K-np.max(np.sum(abs(R),axis=1)))
        low('column_inverse_margin',K-np.max(np.sum(abs(R),axis=0)))
        low('matrix_Jensen_margin',modular-sum(phi(v/K) for v in w0))
        low('quadratic_scaling_margin',sum(phi(v/K) for v in w0)-centered/K**2)
        low('nonlinear_centering_margin',centered-original)
        cases+=1; counts[family]=counts.get(family,0)+1
    for n in [2,3,4,5,8]:
        F=np.exp(2j*np.pi*np.outer(np.arange(n),np.arange(n))/n)/np.sqrt(n)
        Q=haar(n); A=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); A=(A+A.conj().T)/2
        E=expm(.25j*A)
        for k in [1,2,3,4]:
            raw=rng.normal(size=(n,k,k))+1j*rng.normal(size=(n,k,k))
            raw-=raw.mean(axis=0)
            raw/=max(np.linalg.norm(z,2) for z in raw)
            for u,name in [(F,'flat'),(Q,'haar'),(E,'near_identity')]:
                for r in [0.,.01,.5,.95,.9999]:one(u,r*raw,name)
            if n%2==0 and k>=2:
                a=np.zeros((k,k),dtype=complex); a[0,1]=.9999
                zs=np.array([a if j%2==0 else -a for j in range(n)])
                one(F,zs,'rank_deficient_nilpotent')
    for k in [1,2,4]:one(np.ones((1,1)),np.zeros((1,k,k)), 'N1_zero')
    gradient=[]
    for k in [2,3,4]:
        for kind in ['zero','rank_deficient','full']:
            A=np.zeros((k,k),dtype=complex)
            if kind=='rank_deficient':A[0,1]=1.3+0.7j
            if kind=='full':A=rng.normal(size=(k,k))+1j*rng.normal(size=(k,k))
            D=rng.normal(size=(k,k))+1j*rng.normal(size=(k,k)); D/=np.linalg.norm(D)
            L,s,Rh=np.linalg.svd(A); grad=(L*np.tanh(s))@Rh
            eps=1e-5
            finite=(phi(A+eps*D)-phi(A-eps*D))/(2*eps)
            formula=float(np.vdot(grad,D).real)
            err=abs(finite-formula); gradient.append({'k':k,'kind':kind,'absolute_error':err})
            if err>1e-7:raise ValueError(('gradient',gradient[-1]))
    # Absolute margins are allowed small roundoff errors. Relative identity controls use 1e-7.
    for key,value in minima.items():
        if value < -1e-7:raise ValueError(('negative_margin',key,value))
    for key,value in maxima.items():
        if key not in ['maximum_nonnormality','maximum_P_asymmetry'] and value>1e-7:raise ValueError(('identity',key,value))
    return {'arithmetic':'complex128, unvalidated floating diagnostics','seed':SEED,'cases':cases,'family_counts':counts,'minima':minima,'maxima':maxima,'gradient_checks':gradient,'tolerance':1e-7,'result':'No counterexample at declared tolerance; not exhaustive and not a proof.'}

def exact_controls():
    I=sp.I; q=sp.Rational
    H2=sp.Matrix([[1,1],[1,-1]])/sp.sqrt(2)
    H4=sp.kronecker_product(H2,H2)
    records=[]
    def one(U,zs,name):
        n=len(zs); k=zs[0].rows; Z=sp.diag(*zs); Ubig=sp.kronecker_product(U,sp.eye(k)); m=n*k
        if sum(zs,sp.zeros(k))!=sp.zeros(k):raise ValueError('not centered')
        for z in zs:
            d=sp.eye(k)-z*z.conjugate().T
            for j in range(1,k+1):
                if not d[:j,:j].det()>0:raise ValueError('not strictly contractive')
        D=sp.factor((sp.eye(m)-Z*Z.conjugate().T).det())
        a=sp.factor((sp.eye(m)-Ubig*Z*Ubig.conjugate().T*Z.conjugate().T).det())
        b=sp.factor((sp.eye(m)-Ubig.conjugate().T*Z*Ubig*Z.conjugate().T).det())
        diff=sp.simplify(a*sp.conjugate(a)-D)
        if sp.simplify(b-sp.conjugate(a))!=0 or not diff>=0:raise ValueError('exact inequality or orientation')
        records.append({'name':name,'N':n,'k':k,'detD':str(D),'det_action':str(a),'squared_coercivity_margin':str(diff),'nonnormal_blocks':sum(z*z.conjugate().T!=z.conjugate().T*z for z in zs),'all_flat_P':True})
    for r in [q(1,2),q(99,100),1-q(1,10**20)]:
        a=sp.Matrix([[0,r],[0,0]]); one(H2,[a,-a],f'nilpotent_pair_r={r}')
    a=sp.Matrix([[q(1,5),q(1,3)],[0,q(1,7)]])/2
    b=sp.Matrix([[0,I*q(1,4)],[q(1,6),0]])/2
    c=sp.Matrix([[-q(1,9),0],[I*q(1,5),-q(1,8)]])/2
    one(H4,[a,b,c,-a-b-c],'noncommuting_complex_centered_4')
    a3=sp.Matrix([[q(1,5),q(1,3),0],[0,0,q(1,6)],[0,0,0]])
    b3=sp.Matrix([[0,0,0],[I*q(1,4),0,0],[0,q(1,7),0]])
    one(H4,[a3,b3,-a3,-b3],'singular_nonnormal_noncommuting_k3')
    # Missing-centering control is exact: identical blocks commute with U tensor I.
    Ubig=sp.kronecker_product(H2,sp.eye(2)); a=sp.Matrix([[0,q(1,2)],[0,0]]); Z=sp.diag(a,a)
    uncentered=sp.simplify((sp.eye(4)-Ubig*Z*Ubig.conjugate().T*Z.conjugate().T).det()/(sp.eye(4)-Z*Z.conjugate().T).det())
    if uncentered!=1:raise ValueError('uncentered benchmark')
    # A symbolic genuinely nonnormal block inherits exact flat sharpness.
    r=sp.symbols('r',real=True); F4=sp.Matrix([[I**(j*l) for l in range(4)] for j in range(4)])/2
    a=sp.Matrix([[0,r],[0,0]]); Z=sp.diag(a,-a,a,-a); Ubig=sp.kronecker_product(F4,sp.eye(2))
    detA=sp.factor((sp.eye(8)-Ubig*Z*Ubig.conjugate().T*Z.conjugate().T).det())
    detD=sp.factor((sp.eye(8)-Z*Z.conjugate().T).det())
    if sp.factor(detA-(1-r*r)**2*(1+r*r)**2)!=0 or sp.factor(detD-(1-r*r)**4)!=0:raise ValueError('sharpness polynomial')
    return {'arithmetic':'exact SymPy rational and algebraic expressions','cases':records,'uncentered_action_exponential':str(uncentered),'sharpness':{'det_action':str(detA),'detD':str(detD),'interpretation':'S/H tends to 1/2 as r approaches 1 from below, for nonnormal rank-one blocks.'},'result':'Exact finite controls and symbolic benchmark pass; not universal proof.'}

def high_precision_controls():
    mp.mp.dps=120
    def adj(A):return A.conjugate().T
    def blockdiag(mats):
        n=sum(A.rows for A in mats); out=mp.zeros(n); j=0
        for A in mats:
            out[j:j+A.rows,j:j+A.cols]=A; j+=A.rows
        return out
    def tensor(U,k):
        out=mp.zeros(U.rows*k)
        for i in range(U.rows):
            for j in range(U.cols):
                for a in range(k):out[i*k+a,j*k+a]=U[i,j]
        return out
    def svmax(A):return mp.sqrt(max(mp.eighe(adj(A)*A,eigvals_only=True)))
    def radial(A):
        e,V=mp.eighe(adj(A)*A); vals=[]
        for x in e:
            if abs(x)<mp.mpf('1e-110'):vals.append(mp.mpf(1))
            else:
                s=mp.sqrt(x); vals.append(mp.atanh(s)/s)
        return A*V*mp.diag(vals)*adj(V)
    def phimp(A):
        e=mp.eighe(adj(A)*A,eigvals_only=True)
        return sum(mp.log(mp.cosh(mp.sqrt(max(mp.mpf(0),x)))) for x in e)
    records=[]
    a=mp.matrix([[mp.mpf(1)/5,mp.mpf(1)/3],[0,mp.mpf(1)/7]])
    b=mp.matrix([[0,mp.j/4],[mp.mpf(1)/6,0]])
    raw=[a,b,-a-b]; scale=max(svmax(z) for z in raw)
    U=mp.matrix([[mp.exp(2*mp.pi*mp.j*j*l/3)/mp.sqrt(3) for l in range(3)] for j in range(3)]); Ubig=tensor(U,2)
    for r in [mp.mpf('.25'),mp.mpf('.9'),1-mp.mpf('1e-20'),1-mp.mpf('1e-60')]:
        zs=[z*r/scale for z in raw]; Z=blockdiag(zs); Id=mp.eye(6)
        H=-mp.log(mp.det(Id-Z*adj(Z))).real
        S=mp.log(abs(mp.det(Id-Ubig*Z*adj(Ubig)*adj(Z))))+H
        ws=[radial(z) for z in zs]; mean=sum(ws,mp.zeros(2))/3
        original=sum(phimp(w) for w in ws); centered=sum(phimp(w-mean) for w in ws)
        margin=S-H/2
        error=abs(H-2*original)
        if margin < -mp.mpf('1e-50') or centered-original < -mp.mpf('1e-50') or error>mp.mpf('1e-50'):raise ValueError('high_precision_general')
        records.append({'family':'nonnormal_noncommuting_N3_k2','radius':mp.nstr(r,75),'coercivity_margin':mp.nstr(margin,40),'centering_margin':mp.nstr(centered-original,40),'H_2phi_error':mp.nstr(error,8)})
    for power in [2,20,60]:
        r=1-mp.mpf(10)**(-power)
        S=2*mp.log((1+r*r)/(1-r*r)); H=-4*mp.log(1-r*r)
        records.append({'family':'F4_nonnormal_nilpotent_sharpness','radius':'1-10^(-%d)'%power,'S_over_H':mp.nstr(S/H,50),'margin':mp.nstr(S-H/2,30)})
    return {'arithmetic':'mpmath 120-digit floating, no rigorous interval enclosure','cases':records,'result':'No counterexample; high precision is diagnostic, not exact arithmetic.'}

if __name__=='__main__':
    start=time.monotonic()
    result={'exact':exact_controls(),'high_precision':high_precision_controls(),'floating':floating_controls(),'software':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'sympy':sp.__version__,'mpmath':mp.__version__}}
    result['runtime_seconds']=time.monotonic()-start
    print(json.dumps(result,indent=2,allow_nan=False))
