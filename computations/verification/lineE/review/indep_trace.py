"""INDEPENDENT recomputation (no class sums, no nu-reduction): the physical trace Tr (K M_N)^m
 for the actual dimensions N = h_m - 4 (so N = -4 mod h_m, N odd), Line B conventions (TRACE-163 Sec.1):
   M_N(x,y) = N^{-1/2} e_N(-8bar (3x^2 - 2xy + 3y^2)),  K = diag exp(i eta f(x/N)),  f(q) = 0.9 cos(2 pi q)  (kick 'k1').
 M_N is applied matrix-free: chirp * permuted DFT * chirp.  Trace = sum over basis vectors, batched.
 Usage: indep_trace.py m eta batch"""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import numpy as np, sys, time, json
m=int(sys.argv[1]); eta=float(sys.argv[2]); B=int(sys.argv[3])
def nsw(m):
    a,b=1,7
    if m==1: return 1
    for _ in range((m-3)//2): a,b=b,6*b-a
    return b
h=nsw(m); N=h-4; assert N%2==1
x=np.arange(N)
i8=pow(8,-1,N); i4=pow(4,-1,N)
chirp=np.exp(-2j*np.pi*((3*i8*(x*x % N)) % N)/N)
perm=(i4*x) % N
kick=np.exp(1j*eta*0.9*np.cos(2*np.pi*x/N))
def applyU(V):                       # V: N x b
    W=chirp[:,None]*V
    F=np.fft.ifft(W,axis=0)*N        # F[k] = sum_y e^{2 pi i k y/N} W[y]
    W=F[perm,:]*chirp[:,None]/np.sqrt(N)
    return kick[:,None]*W
# sanity: unitarity of M on random vectors
t0=time.time()
v=np.random.default_rng(0).standard_normal((N,2))+0j
u=applyU(v/kick[:,None]*1) ; 
tr=0j
for s in range(0,N,B):
    b=min(B,N-s); V=np.zeros((N,b),complex); V[np.arange(s,s+b),np.arange(b)]=1
    for _ in range(m): V=applyU(V)
    tr+=np.sum(V[np.arange(s,s+b),np.arange(b)])
r=dict(m=m,eta=eta,N=N,h=h,trace_re=tr.real,trace_im=tr.imag,abs2=abs(tr)**2,unit_check=float(np.linalg.norm(u)/np.linalg.norm(v)),secs=time.time()-t0)
print(json.dumps(r),flush=True)
open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'indep_trace.jsonl'),'a').write(json.dumps(r)+'\n')
