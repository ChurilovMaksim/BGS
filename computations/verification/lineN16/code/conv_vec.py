"""N16 (2): VECTOR-propagated core->true conversion (finishes N15 conv_est.py).  Replaces every operator sub-product bound GA = sqrt(cond_H) prod N_H
of the N8 lemma (n8_cert.excursion, used in N15 conv.py, vacuous: radii 0.03..38) by quantities carried along the actual chain:
 forward  v_k = X(d_k) v_{k-1}, v_0 = Phi~ :  H-norm error recursion of N15 c3_mid (derived binary64 constants) PLUS the core->true
          perturbation  ||Delta X_k|| <= g Fs,  Fs = Pert/|s|, g = 1+Xn/|s|  (lifted-operator factor of N8: GT = GA g):
          e_k = (N_H(d_k) + cT g Fs) e_{k-1} + ||T||_F [rounding_k + g Fs ||v^_{k-1}||],   cT = ||T||_F ||Ti||_F/(1-eta_T)  (>= ||T . T^-1||)
 backward w_k = w_{k+1} X(d_k), w_n = psi~ : same recursion in the dual norm ||w||_* = ||w T^-1|| (constants swapped T <-> Ti) -> F_b = ||psi~ prod X||_2 upper.
 ends     err_proj = (el F_b + er F_f + el er GA)/den + |r| er/den,  err_dPi = 2 dPi g max(F_f,F_b),
          err_tail = normPi g max(F_f,F_b)(1+scale)((1+eps)^2-1),  scale = (1+mus/(|s|-mus))^n - 1   (same N8 constants; GA only in the 1e-20 el*er term).
 E_vec = num_err/(|p^|-eps_p) + ... (c3 final step) + |r| scale + (err_proj+err_dPi)(1+scale) + err_tail.
Label: numerics [CA-fp: IEEE std model + libm<=1ulp];  the vector form of the N8 lemma itself (that the lifted perturbation enters per step as
g Fs ||v|| and the projector mismatch only at the ends) is [P-sketch] -- it is the termwise reading of the N8 telescoping, not re-proved here.
usage: conv_vec.py replay|classes [jmax]"""
import sys, json, math, time, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N15/code'); sys.path.insert(0,'/workspace/bgs-lineN/N14/code')
import c3_mid as M, rig, digits as Dg
sys.argv_s=sys.argv
import conv as CV          # N15 conv.py: N8 constants, er, el, den, tails(), Nbar
sys.argv=sys.argv_s
from rig import u, cgam
Fs=CV.Fs; g=1+CV.Xn/abs(M.s); nTi=rig.fro(M.Ti); cT=M.nT*nTi/(1-M.etaT)
def absstpT(wa):
    ub=wa.reshape(M.NB,M.K); y=np.einsum('bij,bi->bj',M.BA,ub[M.BI])*M.CA[M.BK][:,None]; out=np.zeros((M.NB,M.K)); np.add.at(out,M.BJ,y); return out.reshape(M.D)
def stpT(w,d):
    c=M.C*np.exp(2j*np.pi*M.NS*d); ub=w.reshape(M.NB,M.K)
    y=np.einsum('bij,bi->bj',M.BB,ub[M.BI])*c[M.BK][:,None]; out=np.zeros((M.NB,M.K),complex); np.add.at(out,M.BJ,y); return out.reshape(M.D)
def loc(xa_norm,xn,d,nPre): return nPre*(M.KAP*xa_norm*M.ABSDIV+M.RADT*xn+M.Lip2*abs(d)*2.3e-16*xn+g*Fs*xn)*(1+1e-14)
def chain(ds,tail):
    v=M.Phi.copy(); e=0.0
    for d in ds:
        e=((M.NH(d)+cT*g*Fs)*e+loc(rig.fro(M.absstp(np.abs(v))),rig.fro(v),d,M.nT))*(1+4*u); v=M.stp(v,d)
    Ff=rig.fro(v)+nTi/(1-M.etaT)*e
    w=M.psi.copy(); eb=0.0
    for d in reversed(ds):
        eb=((M.NH(d)+cT*g*Fs)*eb+loc(rig.fro(absstpT(np.abs(w))),rig.fro(w),d,nTi/(1-M.etaT)))*(1+4*u); w=stpT(w,d)
    Fb=rig.fro(w)+M.nT*eb
    a=M.psi@v; Ea=M.npsi*e+cgam(M.D)*float(np.abs(M.psi)@np.abs(v))*1.01
    r=a/M.psiPhi; P=abs(M.psiPhi)
    rad=(Ea/(P-M.eps_p)+abs(a)*M.eps_p/(P*(P-M.eps_p))+1e-15*abs(r))*(1+1e-14)
    n=len(ds); GA=CV.sq
    for d in ds: GA*=CV.Nbar(d)
    Fm=max(Ff,Fb)
    err_proj=(CV.el*Fb+Ff*CV.er+CV.el*GA*CV.er)/CV.den+abs(r)*CV.er/CV.den
    err_dPi=2*CV.dPi*g*Fm
    eps=math.expm1(CV.Cpow*2*math.pi*CV.N1*tail/(abs(M.s)-CV.mus)); scale=(1+CV.mus/(abs(M.s)-CV.mus))**n-1
    err_tail=CV.normPi*g*Fm*(1+scale)*((1+eps)**2-1)
    E=(rad+abs(r)*scale+(err_proj+err_dPi)*(1+scale)+err_tail)*(1+1e-12)
    return r,E,dict(rad_c3=rad,Ff=Ff,Fb=Fb,err_proj=err_proj,err_dPi=err_dPi,err_tail=err_tail,scale=scale,GA_old=GA)
def window(ea,eb):
    return [chain(Dg.core(zz,18),CV.tails(zz)) for zz in Dg.seeds(ea,eb)]
if __name__=='__main__':
    mode=sys.argv[1]; t0=time.time()
    print('Fs',Fs,'g',g,'cT',cT,'er',CV.er,'el',CV.el,'den',CV.den,'dPi',CV.dPi,flush=True)
    if mode=='test':
        for e in ((2,0),(0,2),(4,0)):
            for r,E,inf in window(*e): print(e,abs(r),E,inf,flush=True)
        sys.exit()
    if mode=='replay':
        rows=[json.loads(l) for l in open('/workspace/bgs-lineN/N15/logs/c3_mid.jsonl')]
        with open('/workspace/bgs-lineN/N16/logs/conv_vec_replay.jsonl','w') as f:
            for i,rw in enumerate(rows):
                for W,(r,E,inf) in zip('AB',window(*rw['e'])):
                    rw[W]=dict(re=[r.real-E,r.real+E],im=[r.imag-E,r.imag+E],abs_up=abs(r)+E,rad=E,conv=inf)
                f.write(json.dumps(rw)+'\n')
                if i%200==0: print(i,round(time.time()-t0),flush=True)
    else:
        jmax=int(sys.argv[2]); rows=[json.loads(l) for l in open('/workspace/bgs-lineN/N14/logs/a_enum.jsonl') if json.loads(l)['j']<=jmax]
        with open('/workspace/bgs-lineN/N16/logs/conv_vec_classes.jsonl','w') as f:
            for i,rw in enumerate(rows):
                w=window(2*rw['a'],2*rw['b']); up=[abs(r)+E for r,E,_ in w]
                f.write(json.dumps(dict(j=rw['j'],a=rw['a'],b=rw['b'],zr=rw['zr'],absw_up=(up[0]*up[1])**3,EA=w[0][1],EB=w[1][1]))+'\n')
                if i%500==0: print(i,round(time.time()-t0),flush=True)
    print('done',round(time.time()-t0))
