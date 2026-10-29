"""Own transfer-operator implementation for chi_m(eta) (Theorem T), spectrum, small-eta law."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys, numpy as np, math
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__))); from core import *
NG=4096
def what(eta):
    u=uodd_tab(NG); w=np.exp(1j*eta*u); c=np.fft.fft(w)/NG    # c[n] = coeff of e(n theta)
    return lambda n: c[np.asarray(n)%NG], np.sum(np.abs(c)), c
def Mmat(eta,a,K):
    W,_,_=what(eta)
    rng=np.arange(-K,K+1); n=len(rng)
    P,Q,R=np.meshgrid(rng,rng,rng,indexing='ij')   # state (p,q) -> (q,r), weight w(6q-p-r+a)
    M=np.zeros((n,n,n,n),complex)
    vals=W(6*Q-P-R+a)
    for i in range(n):        # q index
        M[:,i,i,:]=vals[:,i,:]
    return M.reshape(n*n,n*n)
def chiT(eta,m,K):
    return sum((-1)**a*np.trace(np.linalg.matrix_power(Mmat(eta,a,K),m)) for a in range(4))
if __name__=='__main__':
    fo=sum(float(b)**2 for k,(a,b) in CK.items())*2   # ||f_odd||^2 = sum_k (Im c_k)^2
    print(f'||f_odd||^2 = {fo:.6e}; 800^2*||f_odd||^2 = {fo*640000:.4f}; 2||f_odd||^2 = {2*fo:.4e}; m_*=1/(2||f_odd||^2 eta^2) = {1/(2*fo):.1f}/eta^2')
    # direct chi values from own t2 logs are compared in the report; here print transfer values
    for m in [3,5,7,9,11,13]:
        print('m=%d '%m+' '.join(f'eta={eta}:{chiT(eta,m,10).real:+.6f}' for eta in [0.5,2,5,10,25,50,100]),flush=True)
    print('spectrum (K=10 and K=14): max|mu_a| over a, rho(|M_a|), half-life, exp(-2||f_odd||^2 eta^2)')
    for eta in [0.1,0.5,1,2,5,10,25,50,100,200,400]:
        row=[]
        for K in (10,14):
            mus=[];rhos=[]
            for a in range(4):
                Mm=Mmat(eta,a,K); ev=np.linalg.eigvals(Mm); mus.append(np.max(np.abs(ev)))
                rhos.append(np.max(np.abs(np.linalg.eigvals(np.abs(Mm)))))
            row.append((max(mus),max(rhos),int(np.argmax(mus))))
        mu=row[1][0]
        print(f'  eta={eta:6}: K=10 max|mu|={row[0][0]:.6f} rho+={row[0][1]:.4f} | K=14 max|mu|={row[1][0]:.6f} (a={row[1][2]}) rho+={row[1][1]:.4f} '
              f'half-life={math.log(2)/(-math.log(mu)) if mu<1 else float("inf"):.1f}  exp-law={math.exp(-2*fo*eta*eta):.6f}  -log(mu)/eta^2={-math.log(mu)/eta**2:.4e}',flush=True)
