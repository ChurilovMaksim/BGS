import numpy as np

def T(N,a,b):
    x=np.arange(N); A=np.zeros((N,N),complex)
    A[x,(x+a)%N]=np.exp(2j*np.pi*((b*(x+a*pow(2,-1,N)))%N)/N)
    return A
for N in [5,7,9,11,21]:
    x=np.arange(N); X=x[:,None]; Y=x[None,:]
    U=np.exp(2j*np.pi*((-pow(8,-1,N)*(3*X*X-2*X*Y+3*Y*Y))%N)/N)/np.sqrt(N)
    comm=T(N,1,0)@T(N,0,1)-T(N,0,1)@T(N,1,0)
    naive=2j*np.sin(np.pi/N)*T(N,1,1)
    cov=max(np.linalg.norm(U@T(N,a,b)@U.conj().T-T(N,3*a+4*b,2*a+3*b),2) for a,b in [(1,0),(0,1),(1,1)])
    r=lambda q:(1-np.cos(14*np.pi*q))*(1+np.cos(2*np.pi*q))
    modzeros=np.where(abs(r(((x+pow(2,-1,N))%N)/N))<1e-12)[0].tolist()
    realzeros=np.where(abs(r((x+.5)/N))<1e-12)[0].tolist()
    print(dict(N=N,wrong_comm_error=np.linalg.norm(comm-naive,2),correct_comm_error=np.linalg.norm(comm+naive,2),covariance_error=cov,modular_hopping_zeros=modzeros,ordinary_hopping_zeros=realzeros))
