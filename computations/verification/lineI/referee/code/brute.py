"""Referee: brute-force Zhat(beta) = sum_n Phihat(n) e(-nu P(n)/2h) e(Tr(beta alpha_n)/7), m=9, alphabet |n|<=L, k1 kick,
directly from the definitions (P(n)=sum psi(|i-j|) n_i n_j, psi(d)=y' x_d - 2h y_d, lam^d = x_d + 2 y_d sqrt2; alpha_n = sum n_i lam^i).
Independent of the G2 law / transfer operators.  Also |Z(nu)|^2 at the d=7 dilation members for cross-checks."""
import numpy as np, itertools, math, sys, json
from scipy.special import jv
m=int(sys.argv[1]); L=int(sys.argv[2]); nu=int(sys.argv[3]) if len(sys.argv)>3 else None
def pell(d):
    x,y=1,0
    for _ in range(d): x,y=3*x+8*y,x+3*y
    return x,y
xm,ym=pell(m); h=math.isqrt((xm-1)//2); assert 2*h*h+1==xm; yp=ym//h; assert h*yp==ym and h*h+1==2*yp*yp
M2=2*h
if nu is None:
    nu=next(v for v in range(1,M2,2) if (8*v-2)%M2==0)   # rho=(2,8): 8 nu = 2 mod 2h
gh={n:(1j**(n%4))*jv(n,1.8) for n in range(-L,L+1)}
vals=np.arange(-L,L+1); ghv=np.array([gh[int(v)] for v in vals])
grid=np.array(list(itertools.product(range(2*L+1),repeat=m)),dtype=np.int64); n=vals[grid]
psi=[(yp*pell(d)[0]-2*h*pell(d)[1])%M2 for d in range(m)]
P=np.zeros(len(n),dtype=np.int64)
for i in range(m):
    for j in range(m): P=(P+psi[abs(i-j)]*((n[:,i]*n[:,j])%M2))%M2
w=np.prod(ghv[grid],axis=1)*np.exp(-2j*np.pi*((nu*P)%M2)/M2)
x=np.zeros(len(n),np.int64); y=np.zeros(len(n),np.int64); lx,ly=1,0
for i in range(m): x=(x+n[:,i]*lx)%7; y=(y+n[:,i]*ly)%7; lx,ly=(3*lx+4*ly)%7,(2*lx+3*ly)%7
Wg=np.zeros((7,7),complex); np.add.at(Wg,(x,y),w)
Zh=np.zeros((7,7),complex)
for bx in range(7):
    for by in range(7):
        gx,gy=np.meshgrid(range(7),range(7),indexing='ij')
        Zh[bx,by]=(Wg*np.exp(2j*np.pi*((2*(bx*gx+2*by*gy))%7)/7)).sum()
# members
mem={}
for j in range(1,7):
    v=(nu+(2*h//7)*j)%M2
    mem[v]=complex(np.sum(np.prod(ghv[grid],axis=1)*np.exp(-2j*np.pi*((v*P)%M2)/M2)))
np.save(f'out/brute_m{m}_L{L}_nu{nu}.npy',Zh); np.save(f'out/bruteW_m{m}_L{L}_nu{nu}.npy',Wg)
json.dump(dict(m=m,L=L,h=h,yp=yp,nu=nu,Z0=str(Zh[0,0]),members={str(k):[v.real,v.imag] for k,v in mem.items()}),open(f'out/brute_m{m}_L{L}_nu{nu}.json','w'),indent=1)
print('h',h,'yp',yp,'nu',nu,'Z0',Zh[0,0],'|Z0|^2',abs(Zh[0,0])**2)
for bx in range(7): print(' '.join('%10.4f'%abs(Zh[bx,by]) for by in range(7)))
