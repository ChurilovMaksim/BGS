"""Referee N12 [CA]: interval (arb) verification of the adapted-norm inequalities, independent of N12's float error model.
Inputs: N12's H, Qt, s (exact float numbers, taken as given: the claims are about THIS H, Qt, s) and the sector-4 core
operator A0 = sum_n w_4(n) M_n rebuilt in ball arithmetic from (i) the cached cert_core block midpoints MS (+ radius RAD per entry)
and (ii) weights w_4(n) = i^n J_n(9/10*eta) e(cc n^2/2 + 4n/8) recomputed here in arb (eta = 2, cc = 1/(lam - 1/lam)).
For each claim c^2 H - X^* H X >= 0 we compute R in arb, take a float Cholesky L of mid(R) - sigma I, and bound
E = R - sigma I - L L^* rigorously (Frobenius, arb).  If ||E||_F < sigma then R >= sigma I - E > 0 [CA].
Also cond: (c_lo')^2 I <= H <= (c_hi')^2 I with c_lo' = 0.7208, c_hi' = 15.1811."""
import os; os.environ.setdefault('OMP_NUM_THREADS','4')
import sys, json, time, numpy as np
from flint import arb, acb, acb_mat, ctx
ctx.prec=106
t0=time.time()
z=np.load('/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45.npz'); H=z['H']; Qt=z['Qt']; s=complex(z['s']); kap=float(z['kap'])
c=np.load('/workspace/bgs-lineN/N12/logs/a_ops.npz',allow_pickle=True); NS=c['NS']; MS=c['MS']; COEF0=c['COEF0']; RAD=float(c['RAD']); D=int(c['D'])
two=arb(2); lam=3+2*two.sqrt(); cc=1/(lam-1/lam); pi=arb.pi(); I=acb(0,1); x=arb(9)/10*2
def e(t): return (2*pi*I*t).exp()
def J(n):
    v=x.bessel_j(arb(abs(n))); return v if (n>=0 or n%2==0) else -v
w={int(n):(I**(int(n)%4))*J(int(n))*e(cc*int(n)*int(n)/2+arb(4*int(n))/8) for n in NS}
wdiff=max(abs(complex(w[int(n)].real.mid(),w[int(n)].imag.mid())-COEF0[k]) for k,n in enumerate(NS))
# sector-shift identity: w_a(n) = w_4(n) e(n(a-4)/8), checked in arb for all a, n
def wa(a,n): return (I**(n%4))*J(n)*e(cc*n*n/2+arb(a*n)/8)
ident_ok=all(abs(wa(a,int(n))-w[int(n)]*e(arb(int(n)*(a-4))/8)).upper()<1e-25 for a in range(8) for n in NS[::7])
def tomat(Mf,rad=0.0):
    r=arb(0,rad) if rad else None
    return acb_mat([[acb(arb(float(v.real),rad) if rad else arb(float(v.real)),arb(float(v.imag),rad) if rad else arb(float(v.imag))) for v in row] for row in Mf])
A0=acb_mat(D,D)
for k,n in enumerate(NS):
    A0+=tomat(MS[k],RAD)*w[int(n)]
print('A0 built',round(time.time()-t0),'s; weight mid diff vs N12 cache',wdiff,'identity',ident_ok,flush=True)
Ha=tomat(H); Qa=tomat(Qt); sa=acb(s.real,s.imag)
M=A0*(1/sa)
def H_of(X): return X.conjugate().transpose()*Ha*X
def mid_np(R): return np.array([[complex(float(R[i,j].real.mid()),float(R[i,j].imag.mid())) for j in range(D)] for i in range(D)])
def psd_cert(R,label):
    Rm=mid_np(R); Rm=(Rm+Rm.conj().T)/2
    lmin=float(np.linalg.eigvalsh(Rm).min()); sig=lmin/2
    L=np.linalg.cholesky(Rm-sig*np.eye(D))
    La=tomat(L); E=R-La*La.conjugate().transpose()
    for i in range(D): E[i,i]-=sig
    fro=arb(0); rmax=0.0; bad=0
    for i in range(D):
        for j in range(D):
            v=E[i,j]
            if not v.is_finite(): bad+=1
            fro+=v.real*v.real+v.imag*v.imag
            if bad==0 and not fro.is_finite():
                print('nonfinite at',i,j,v,R[i,j],flush=True); bad=-1
            rmax=max(rmax,float(R[i,j].real.rad())+float(R[i,j].imag.rad()))
    fro=arb(fro.upper()).sqrt()   # |E|_F^2 <= upper endpoint
    ok=bool(fro.upper()<sig)
    r=dict(nan_entries=bad,R_max_rad=rmax,label=label,lmin_float=lmin,sigma=sig,E_frob_upper=float(fro.upper()),certified=ok,t=round(time.time()-t0))
    print(json.dumps(r),flush=True); return r
eta=1e-8; out=dict(weight_mid_diff=wdiff,sector_identity_arb=ident_ok,prec=ctx.prec)
G=H_of(M); import sys as _s
ONLY=_s.argv[1] if len(_s.argv)>1 else None
if ONLY!='V3b': out['V2']=psd_cert(Ha*((1+eta)**2)-G,'V2 ||A0/s||_H<=1+1e-8')
MQ=M*Qa; G=H_of(MQ); out['V3b']=psd_cert(Ha*((kap*(1+eta))**2)-G,'V3b ||(A0/s)Qt||_H<=0.45(1+1e-8)')
if ONLY=='V3b':
    json.dump(out,open('/workspace/audit/lineN12/logs/ref_arb_V3b.json','w'),indent=1); raise SystemExit
G=H_of(Qa); out['V3a']=psd_cert(Ha*((1+eta)**2)-G,'V3a ||Qt||_H<=1+1e-8')
Id=acb_mat(D,D)
for i in range(D): Id[i,i]=acb(1)
out['clo']=psd_cert(Ha-Id*(0.7208**2),'H >= 0.7208^2 I')
out['chi']=psd_cert(Id*(15.1811**2)-Ha,'H <= 15.1811^2 I')
out['cond_upper']=15.1811/0.7208
json.dump(out,open('/workspace/audit/lineN12/logs/ref_arb_adapted.json','w'),indent=1); print('done',round(time.time()-t0))
