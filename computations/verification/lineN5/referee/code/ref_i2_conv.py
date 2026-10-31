"""Referee: brute-force convention check of the I2' pipeline used in ref_level_dev.py, at m = 5, h = 41 = q (L = 4 words):
Zhat(beta) by brute force for all beta in O/41, then Z(nu0 + 2h j/q) via W(gamma), t = j y', versus direct brute Z_m(nu)."""
import sys, itertools, numpy as np
sys.path.insert(0,'/workspace/bgs-lineI/code'); from law import mdata, pell, kick_ghat
m=5; d=mdata(m); h=d['h']; yp=d['yp']; M=2*h; q=h
gh=kick_ghat('k1',2.0,4); xs=[pell(k) for k in range(m)]; psi=[yp*xs[k][0]-2*h*xs[k][1] for k in range(m)]
nu0=next(x for x in range(1,M,2) if (8*x-2)%M==0)
ns=np.array(list(itertools.product(range(-4,5),repeat=m)))
Pm=np.array([[psi[abs(i-j)] for j in range(m)] for i in range(m)])
P=np.einsum('ki,ij,kj->k',ns,Pm,ns)
g=np.prod(np.vectorize(lambda t: gh[t])(ns),axis=1)
lp=[]; x,y=1,0
for i in range(m): lp.append((x,y)); x,y=3*x+4*y,2*x+3*y
ax=ns@np.array([a for a,_ in lp]); ay=ns@np.array([b for _,b in lp])   # alpha_n = ax + ay sqrt2
def Zdirect(nu): return np.sum(g*np.exp(-2j*np.pi*((nu*P)%M)/M))
w=g*np.exp(-2j*np.pi*((nu0*P)%M)/M)
Zh=np.zeros((q,q),complex)
for bx in range(q):
    for by in range(q):
        Zh[bx,by]=np.sum(w*np.exp(2j*np.pi*((2*(bx*ax+2*by*ay))%q)/q))
G=np.arange(q); Ng=(G[:,None]**2-2*G[None,:]**2)%q
F=np.fft.fft2(Zh); Wg=F[(2*G)%q][:,(4*G)%q]/q**2
Wu=np.array([Wg[Ng==u].sum() for u in range(q)])
step=2*h//q; err=[]
for j in range(1,q):
    nu=(nu0+step*j)%M
    if nu%q==0: continue
    t=(j*yp)%q; zt=np.sum(Wu*np.exp(-2j*np.pi*t*np.arange(q)/q)); err.append(abs(zt-Zdirect(nu))/abs(Zdirect(nu)))
print('m=5 q=41: max rel err of I2-prime pipeline vs brute over members:',max(err),' Z0 check',abs(Zh[0,0]-Zdirect(nu0)))
