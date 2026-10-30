"""Fast d=7 dilation predictor on the 16 reachable states (single disc). For m≡3 mod 6, rho=(±2,8):
Zhat(beta) for all beta mod 7, exact Gauss-sum member formula Z_t = (1/d^2) sum_beta Zhat(beta) G_t(beta),
deviation split dev_t = 2Re(conj(om_t Z0/d) Delta_t) + |Delta_t|^2 (no cancellation).  Usage: zpred.py K rho Lk mlist"""
import numpy as np, json, sys, math
from law import kick_ghat, mdata, LAM
from twist import build
from twrad2_lib import restricted
K=int(sys.argv[1]); RHO=float(sys.argv[2]); Lk=int(sys.argv[3]); ms=[int(x) for x in sys.argv[4].split(',')]
gh=kick_ghat('k1',2.0,Lk); d=7
def lampow(m):
    out=[];x,y=1,0
    for i in range(m): out.append((x,y)); x,y=(3*x+4*y)%d,(2*x+3*y)%d
    return out
G=np.zeros((d,d,d),complex)   # G[t,bx,by] gauss sums
gx,gy=np.meshgrid(np.arange(d),np.arange(d),indexing='ij'); Nm=(gx*gx-2*gy*gy)%d
for t in range(d):
    for bx in range(d):
        for by in range(d):
            G[t,bx,by]=np.exp(-2j*np.pi*((t*Nm+2*(bx*gx+2*by*gy))%d)/d).sum()
def phi(n):
    import sympy; return int(sympy.totient(n))
out={}
for m in ms:
  D=mdata(m); h=D['h']; yp=D['yp']; assert h%d==0
  for (a,b) in ((2,8),(-2,8)):
    sub,idx,nu0=restricted(build,m,a,b,gh,RHO,K)
    S=len(idx); z0=idx.index(0)
    ops={}
    def L(tau):
        if tau not in ops: ops[tau]=sum(np.exp(2j*np.pi*n*tau)*np.kron(Mn,P) for n,(Mn,P) in sub.items())
        return ops[tau]
    lp=lampow(m)
    Zh=np.zeros((d,d),complex)
    for bx in range(d):
        for by in range(d):
            ts=[((2*(bx*lx+2*by*ly))%d)/d for (lx,ly) in lp]
            # period 3: Q = L(t2)L(t1)L(t0); product = Q^(m/3)
            Q=L(ts[2])@L(ts[1])@L(ts[0]); X=np.linalg.matrix_power(Q,m//3)
            X=X.reshape(K,S,K,S)
            Zh[bx,by]=(1-LAM**(-m))*np.einsum('isi->',X[:,:,:,z0])
    Z0=Zh[0,0]; Zn=Zh.copy(); Zn[0,0]=0
    mem=[]; bad=None
    for j in range(1,d):
        nu=(nu0+(2*h//d)*j)%(2*h); t=(j*yp)%d
        om=G[t,0,0]/d; Delta=np.sum(Zn*G[t])/d**2
        dev=2*np.real(np.conj(om*Z0/d)*Delta)+abs(Delta)**2
        rec=(nu,t,float(dev),float(abs(Delta)))
        if math.gcd(nu,2*h)!=1: bad=rec; continue
        mem.append(rec)
    Dev=sum(r[2] for r in mem); ph=phi(h) if m<=45 else None
    r=dict(m=m,rho=[a,b],absZ0_2=float(abs(Z0)**2),main_each=float(abs(Z0)**2/d**2),Dev=Dev,rel=Dev/(len(mem)*abs(Z0)**2/d**2),
           S=float(abs(Zn).sum()),maxZhat=float(abs(Zn).max()),
           dW=(Dev/(2*m*ph) if ph else None), dW_over_m=(Dev/(2*m*m*ph) if ph else None), Dev_over_2m2h=Dev/(2*m*m*h))
    try:
        from base import get
        DD=get('k1',m); Zd=dict(zip(DD['nu'].tolist(),DD['Z'].tolist()))
        act=np.array([Zd[x[0]] for x in mem]); predm=np.array([abs(Z0)**2/d**2+x[2] for x in mem])
        r['maxrel_vs_act']=float(np.max(abs(predm/act-1))); r['act_rel']=float(act.sum()/(len(mem)*abs(Z0)**2/d**2)-1)
    except Exception as e: r['act']=str(e)[:60]
    print(json.dumps(r),flush=True); out[f'{m},{a},{b}']=r
    np.save(f'../data/zpred_d7_{a}_{b}_m{m}_K{K}.npy',Zh)
json.dump(out,open(f'../logs/zpred_d7_K{K}_r{RHO}_L{Lk}.json','w'),indent=1)
