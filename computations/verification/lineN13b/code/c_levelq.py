"""N13b R3 [N] (from N11b b_exactXY): EXACT level-q decomposition for a PRIME FACTOR q of h_p (usage: c_levelq.py p q); (prime d = h_p, all d^2 beta, orbit-reduced; N6 j_exactdev.py set-up verbatim) into
X = sum_{iso beta != 0} Zhat/Z (weight kappa(0)/n = 1) and Y = (1/n) sum_{unit beta} kappa(N beta) Zhat/Z, kappa(u) = sum_{t in S} e(tbar u/d),
plus the unit-gas part Y_gas (small-beta single-bump classes) and the CS check Dev/main >= |1+X+Y|^2 - 1.  usage: b_exactXY.py p"""
import sys, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
p=int(sys.argv[1]); sg=1
def hp(p):
    x,y=1,1
    for _ in range(p-1): x,y=x+2*y,x+y
    return x
d=int(sys.argv[2]); m=3*p; md=mdata(m); h=md["h"]; yp=md["yp"]; assert (2*h)%d==0 and hp(p)%d==0
h_,nu0=nu_rho(m,sg); tw=TW(m,nu0,L=8,K=16); pw=lam_pows(m,d)
bx,by=np.meshgrid(np.arange(d),np.arange(d),indexing='ij'); key=(bx*d+by).ravel()
best=key.copy(); cx,cy=bx.ravel().copy(),by.ravel().copy()
for i in range(p):
    for (sx,sy) in [(1,1),(-1,-1),(1,-1),(-1,1)]:
        best=np.minimum(best,((sx*cx)%d)*d+((sy*cy)%d))
    cx,cy=(3*cx+4*cy)%d,(2*cx+3*cy)%d
reps,inv=np.unique(best,return_inverse=True)
T=np.array([taus_of((int(r//d),int(r%d)),pw,d) for r in reps]); Zr=np.zeros(len(reps),complex)
for i in range(0,len(reps),32): Zr[i:i+32]=Zbatch(tw,T[i:i+32])
Zh=Zr[inv]; Z0=Zh[0]; r=Zh/Z0
Nm=((bx.ravel()**2-2*by.ravel()**2)%d)
S=[]
for j in range(1,d):
    nu=nu0+2*h*j//d
    if nu%d==0: continue
    S.append((j*yp)%d)
n=len(S); u=np.arange(d)
kap=np.zeros(d,complex)
for t in S: kap+=np.exp(2j*np.pi*((pow(t,-1,d)*u)%d)/d)
iso=(Nm==0); iso[0]=False; unit=(Nm!=0)
X=r[iso].sum(); Y=(kap[Nm[unit]]*r[unit]).sum()/n
# unit gas: |beta|-small classes (balanced reps |a|,|b|<=3 up to lam-shift)
small=np.zeros(d*d,bool)
for a in range(-3,4):
    for b in range(-3,4):
        if (a,b)==(0,0): continue
        x,y=a%d,b%d
        for i in range(p):
            small[x*d+y]=True; x,y=(3*x+4*y)%d,(2*x+3*y)%d
small&=unit
Ygas=(kap[Nm[small]]*r[small]).sum()/n
Ybulk=Y-Ygas
Sabs=np.abs(r[unit]).sum(); Sgas=np.abs(r[small]).sum()
# exact Dev/main for the CS check (as j_exactdev)
A=np.zeros(d,complex); np.add.at(A,Nm,Zh); dev=0.0
for t in S:
    ph=np.exp(2j*np.pi*((pow(t,-1,d)*u)%d)/d); tot=(ph*A).sum(); dev+=abs(tot)**2/d**2-abs(Z0)**2/d**2
main=n*abs(Z0)**2/d**2
res=dict(p=p,d=d,n=n,kappa_unit_max=float(np.abs(kap[1:]).max()),X=[X.real,X.imag],Y=[Y.real,Y.imag],absY=abs(Y),Ygas=[Ygas.real,Ygas.imag],Ybulk=[Ybulk.real,Ybulk.imag],
         sum_abs_r_unit=float(Sabs),sum_abs_r_gas=float(Sgas),one_plus_X_plus_Y=abs(1+X+Y),one_plus_X=abs(1+X),CS_lower=abs(1+X+Y)**2-1,Dev_over_main=dev/main,
         Ygas_vs_minus_sum_over_n=[(-r[small].sum()/n).real,(-r[small].sum()/n).imag])
print(json.dumps(res)); json.dump(res,open(f'logs/c_levelq_p{p}_q{d}.json','w'),indent=1)
