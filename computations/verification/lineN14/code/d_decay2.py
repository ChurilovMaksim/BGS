"""N14 copy with N13-referee F1 fix: e^{sig}-1 -> e^{Gam sig}-1 in every cross/normalisation term (two core sub-products; higher orders)."""
"""N13 (D): two-bump interaction decay beyond G0, bound from single-bump chains only (p-independent).
Composite twists superpose: d_t = d^i_t + s d^{j'}_{t+G} (mod 1), j' = e_j eps^h  [exact: Tr(zeta lam^u) in Z].
Cut c = -D_i (D_i = floor(G/2), D_j = G - D_i).  With R_i, L_j the single chains right/left of the cut and Phi psi^T + Qt = I:
 r_ij - r_i r_j = psi R_i Qt L_j Phi  [<= Y_i(D_i) X_j(D_j)]                                 (Q-part, both sides contract: kap^G)
                + psi dR L Phi + psi R_i dL Phi   [<= Gam_R(e^{sig_R}-1) Xi_j' + Psi_i Gam_L(e^{sig_L}-1)]   (cross tails)
                - (err_i b + r_i err_j)            [err_i <= Psi_i eps_iL, err_j <= Xi_j eps_jR]          (normalisation)
 Y_i = ||psi R_i Qt||_{H*}, Psi_i = ||psi R_i||_{H*}, X_j = ||Qt L_j Phi||_H, Xi_j = ||L_j Phi||_H  (computed on long single windows),
 sig_R = Lip_H sum_{u>=D_j} |d^j_u|, sig_L = Lip_H sum_{t<-D_i} |d^i_t|, eps = e^{sig}-1 (same sums), Gam = prod of step bounds N^(d) over the segment.
Rates: Y_i ~ kap^{D_i}, X_j ~ kap^{D_j}, sig ~ lam^{-G/2}  =>  bound ~ max(kap, lam^{-1/2})^G.  [P given the H-norm facts V2,V3,Lip; constants float]"""
import sys, json, math, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N12/code'); import a_ops as A
import mpmath as mp
mp.mp.dps=60
z=np.load('/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45.npz')
T=z['T']; Ti=np.linalg.inv(T); s=complex(z['s']); Phi=z['Phi']; psi=z['psi']; Qt=z['Qt']; kap=float(z['kap'])
B=json.load(open('/workspace/bgs-lineN/N13/logs/b_arb.json')); Lip=B['Lip_H']; L2=B['L2']; eta=B['V2']['eta']; NSUM=B['Nsum']
c0=1.01e-12; cq=4260.0   # [CA] N13 b2 + N13-referee arb partition (30,364 cells): N_H(t)<=1+1.01e-12+4260 t^2, |t|<=1/256
tab=json.load(open('/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45_stepnorm_NG4096.json')); NH=np.array(tab['N_H']); cell=tab['cell_add']
def Nhat(d):   # certified single-step bound [CA]: quadratic for |d|<=1/256, else Nsum
    d=abs(d)
    return 1+c0+cq*d*d if d<=1/256 else NSUM
def Gam_core(ds):   # [N] sup over contiguous sub-products of the steps with |d|>1/256 (H-norm, float), times certified factors of the other steps
    us=sorted(ds); core=[u for u in us if abs(ds[u])>1/256]
    if not core: return float(np.prod([Nhat(ds[u]) for u in us]))
    a,b=core[0],core[-1]; seg=[u for u in us if a<=u<=b]; Xs=[A.Amat(ds[u])/s for u in seg]; best=1.0
    for i0 in range(len(Xs)):
        P=np.eye(A.D,dtype=complex)
        for j0 in range(i0,len(Xs)):
            P=Xs[j0]@P; best=max(best,np.linalg.norm(T@P@Ti,2))
    outside=float(np.prod([Nhat(ds[u]) for u in us if u<a or u>b]))
    return best*outside
nH=lambda v: np.linalg.norm(T@v); nHs=lambda w: np.linalg.norm(w@Ti)
S2=mp.sqrt(2); LAM=3+2*S2; KK=34
def red(x): y=x-mp.floor(x+mp.mpf(1)/2); return float(y)
def mulq(u,v): return (u[0]*v[0]+2*u[1]*v[1], u[0]*v[1]+u[1]*v[0])
def seeds(e):
    ea,eb=e; zA=(mp.mpf(2*eb)/8, mp.mpf(ea)/8); fu=-ea+2*eb; fv=ea-eb; zB=(-mp.mpf(2*fv)/8,-mp.mpf(fu)/8); return zA,zB
def seq(z):   # d_u for u in [-KK, KK] (centre 0) plus analytic tail coefficients |e1|, |e2|
    e1=z[0]+z[1]*S2; e2=z[0]-z[1]*S2
    ds={u:(red(e1*LAM**u) if u<=0 else red(-e2*LAM**(-u))) for u in range(-KK,KK+1)}
    return ds,float(abs(e1)),float(abs(e2))
def chains(ds):
    us=sorted(ds); vs={}; v=Phi.astype(complex)
    for u in us: v=(A.Amat(ds[u])@v)/s; vs[u]=v           # vs[u] = L(<=u) Phi
    ws={}; w=psi.astype(complex)
    for u in reversed(us): w=(w@A.Amat(ds[u]))/s; ws[u]=w   # ws[u] = psi R(>=u)
    return vs,ws
TYPES={'odd':(2,0),'sq2':(0,2),'two':(4,0),'2sq2':(0,4),'four':(8,0)}; EPS=(1,1)
def single_data(e):
    out=[]
    for zz in seeds(e):
        ds,a1,a2=seq(zz); vs,ws=chains(ds); us=sorted(ds)
        r=complex(ws[us[0]]@Phi)
        dat=dict(r=r,a1=a1,a2=a2,ds=ds)
        # as bump i: right segment from cut -D (D>=0): t>=-D
        dat['Y']={D:nHs(ws[-D]@Qt) for D in range(0,KK)}; dat['Psi']={D:nHs(ws[-D]) for D in range(0,KK)}
        g=Gam_core(ds); dat['Gam']=g
        dat['GamR']={D:g for D in range(0,KK)}
        # as bump j: left segment up to cut +D (u < D)
        dat['X']={D:nH(Qt@vs[D-1]) for D in range(1,KK)}; dat['Xi']={D:nH(vs[D-1]) for D in range(1,KK)}
        dat['GamL']={D:g for D in range(1,KK)}
        out.append(dat)
    return out
def tailsum_left(a1,D):   # sum_{t< -D} |d^i_t| <= a1 lam^{-D-1}/(1-1/lam)  (valid once a1 lam^{-D-1} < 1/2)
    x=a1*float(LAM)**(-D-1); assert x<0.5; return x/(1-1/float(LAM))
def tailsum_right(a2,D):  # sum_{u>=D} |d^j_u| <= a2 lam^{-D}/(1-1/lam)
    x=a2*float(LAM)**(-D); assert x<0.5; return x/(1-1/float(LAM))
G0=int(sys.argv[1]) if len(sys.argv)>1 else 16; GMAX=2*KK-4
cache={}
def get(name,e):
    if name not in cache: cache[name]=single_data(e); print('single',name,[abs(d['r']) for d in cache[name]],'Gam',[d['Gam'] for d in cache[name]],flush=True)
    return cache[name]
rows=[]
for ti in TYPES:
    Si=get(ti,TYPES[ti])
    for tj in TYPES:
        for h in (0,1):
            for sg in (1,-1):
                ej=TYPES[tj] if h==0 else mulq(TYPES[tj],EPS); ej=(sg*ej[0],sg*ej[1])
                Sj=get(f'{tj}|h{h}|s{sg}',ej)
                per=[]
                for G in range(G0,GMAX+1):
                    Di=G//2; Dj=G-Di; wd=[]
                    for a in (0,1):
                        I_,J_=Si[a],Sj[a]
                        ef=(1+eta)**(4*KK)
                        sR=Lip*tailsum_right(J_['a2'],Dj)*ef; sL=Lip*tailsum_left(I_['a1'],Di)*ef
                        q=I_['Y'][Di]*J_['X'][Dj]
                        cross=I_['GamR'][Di]*math.expm1(I_['GamR'][Di]*sR)*(J_['Xi'][Dj]+J_['GamL'][Dj]*math.expm1(J_['GamL'][Dj]*sL))+I_['Psi'][Di]*J_['GamL'][Dj]*math.expm1(J_['GamL'][Dj]*sL)
                        norm=abs(J_['r'])*I_['Psi'][Di]*math.expm1(J_['GamL'][Dj]*sL)+abs(I_['r'])*J_['Xi'][Dj]*math.expm1(I_['GamR'][Di]*sR)
                        wd.append((q+cross+norm)/abs(I_['r']*J_['r']))
                    cls=(1+wd[0])**3*(1+wd[1])**3-1
                    per.append(dict(G=G,winA=wd[0],winB=wd[1],cls=cls))
                # geometric continuation beyond GMAX with rate rho = max(kap, lam^-1/2) (each term above is monotone in G) [P-sketch]
                rho=max(kap,float(LAM)**-0.5)
                tail_beyond=per[-1]['cls']*rho/(1-rho)
                rows.append(dict(i=ti,j=tj,h=h,s=sg,G0=G0,sum_cls=sum(x['cls'] for x in per)+tail_beyond,first=per[0],last=per[-1],
                                 ratio_last=per[-1]['cls']/per[-2]['cls']))
                print(json.dumps({k:rows[-1][k] for k in ('i','j','h','s','sum_cls')}),'G0 cls %.3g'%per[0]['cls'],'rate %.3f'%rows[-1]['ratio_last'],flush=True)
json.dump(dict(G0=G0,Lip=Lip,cq=cq,L2=L2,eta=eta,rows=rows),open(f'/workspace/bgs-lineN/N14/logs/d_decay2_G{G0}.json','w'),indent=1)
