"""Line L2 (c) [N]: isotropic-line mass deviations at true levels q || h_m (TRACE-206 weights, (2,8)-resonant nu0).
For each of the two isotropic lines l (=ideals qbar, q above q): D_l = (1/q) sum_{beta in l, beta!=0} Zhat_beta = A(ideal) - A_tot/q.
Zhat is constant on lambda-orbits [N-checked], so one transfer run per orbit.  Also: mean-square (1/(q-1)) sum |Zhat|^2,
max |Zhat|, and the phase-blind analogue W_beta = prod_i phi1(tau_i) (phi1(t)=sum_a |J_a(1.8)| e(at)),
Dpb_l = (1/q) sum_{beta in l,!=0} W_beta = M(ideal) - G^m/q.
usage: iso_survey.py m q [L K sign]  (sign=+1: (2,8) resonance 8nu=2; -1: (-2,8))"""
import sys, json, time, math; sys.path.insert(0,'/workspace/audit/lineL/L2rerun/code')
from twlaw import *
from scipy.special import jv
m=int(sys.argv[1]); q=int(sys.argv[2]); L=int(sys.argv[3]) if len(sys.argv)>3 else 8; K=int(sys.argv[4]) if len(sys.argv)>4 else 32; sg=int(sys.argv[5]) if len(sys.argv)>5 else 1
d=mdata(m); h=d['h']; M=2*h; assert h%q==0 and (h//q)%q!=0
x0=(sg*pow(4,-1,M//2))%(M//2); nu0=min(x for x in (x0,x0+M//2) if x%2==1); assert (8*nu0-2*sg)%M==0
tw=TW(m,nu0,L=L,K=K); pw=lam_pows(m,q)
Ja=np.abs(jv(np.arange(-40,41),1.8)); G=Ja.sum()
def phi1(t): return float((Ja*np.cos(2*np.pi*np.arange(-40,41)*t)).sum())
s=next(x for x in range(q) if (x*x-2)%q==0)
t0=time.time(); Z0=tw.Z([0.0]*m)
res=dict(res=f'({2*sg},8)',m=m,q=q,h=h,nu0=nu0,L=L,K=K,absZ=abs(Z0),log_q_over_m=math.log(q)/m,target8_m=1.28359**m,target16_m=1.4742**m,G=G)
lines={}
for sign in (1,-1):
    v0=(sign*s%q,1); seen=set(); S=0j; S2=0.0; mx=0.0; Spb=0.0; norb=0; r=None
    for t in range(1,q):
        b=((t*v0[0])%q,(t*v0[1])%q)
        if b in seen: continue
        orb=[]; x=b
        while x not in seen:
            seen.add(x); orb.append(x)
            bx,by=x; x=((3*bx+4*by)%q,(2*bx+3*by)%q)   # beta*lam, lam=3+2sqrt2 -> (3bx+4by) + (2bx+3by)sqrt2
        r=len(orb); tau=taus_of(b,pw,q); z=tw.Z(tau); wpb=math.prod(phi1(tt) for tt in tau)
        S+=r*z; S2+=r*abs(z)**2; mx=max(mx,abs(z)); Spb+=r*wpb; norb+=1
    assert len(seen)==q-1
    lines[sign]=dict(r=r,n_orbits=norb,D=[(S/q).real,(S/q).imag],absD=abs(S/q),meansq=S2/(q-1),maxZ=mx,
                     Dpb=Spb/q,G_m_over_q=G**m/q,absZ_over_q=abs(Z0)/q)
res['lines']=lines; res['sec']=round(time.time()-t0,1)
print(json.dumps(res),flush=True)
