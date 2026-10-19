import json
import sys
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path

@dataclass(frozen=True)
class G:
    re:F=F(0)
    im:F=F(0)
    def __post_init__(self):object.__setattr__(self,'re',F(self.re));object.__setattr__(self,'im',F(self.im))
    @staticmethod
    def cast(z):return z if isinstance(z,G) else G(z)
    def __add__(self,z):z=G.cast(z);return G(self.re+z.re,self.im+z.im)
    __radd__=__add__
    def __neg__(self):return G(-self.re,-self.im)
    def __sub__(self,z):return self+-G.cast(z)
    def __rsub__(self,z):return G.cast(z)+-self
    def __mul__(self,z):z=G.cast(z);return G(self.re*z.re-self.im*z.im,self.re*z.im+self.im*z.re)
    __rmul__=__mul__
    def __truediv__(self,z):z=G.cast(z);norm=z.re*z.re+z.im*z.im;return self*G(z.re/norm,-z.im/norm)
    def conj(self):return G(self.re,-self.im)

I=G(0,1)
def eye(n):return [[G(int(i==j)) for j in range(n)] for i in range(n)]
def diag(v):return [[G.cast(v[i]) if i==j else G() for j in range(len(v))] for i in range(len(v))]
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(a,c):return [[c*x for x in r] for r in a]
def mul(a,b):return [[sum((a[i][k]*b[k][j] for k in range(len(b))),G()) for j in range(len(b[0]))] for i in range(len(a))]
def star(a):return [[a[j][i].conj() for j in range(len(a))] for i in range(len(a[0]))]
def reflector(v):
    norm=sum((x.conj()*x for x in v),G());assert norm.im==0 and norm.re>0
    return add(eye(len(v)),[[(-2*x*y.conj())/norm for y in v] for x in v])

def exact_checks():
    count=0
    for n in range(1,6):
        e=eye(n);v=[G(j+1,(j*j+1)%3) for j in range(n)];w=[G(2*j+1,(j+2)%4) for j in range(n)]
        r=reflector(v);q=mul(r,reflector(w));s4=mul(mul(q,diag([(-1)**j for j in range(n)])),star(q))
        for s in (e,scale(e,-1),r,s4):
            assert star(s)==s and mul(s,s)==e
            for tv in ([F(j-2,3) for j in range(n)],[F((-1)**j*(2*j+1),j+1) for j in range(n)],[F(1000001) if j==0 else F(j,7) for j in range(n)]):
                t=diag(tv);d=diag([(G(v)+I)/(G(v)-I) for v in tv]);u=scale(mul(d,s),-I);h=add(s,scale(t,-1))
                assert mul(u,star(u))==e
                for a in (F(0),F(1,10),F(-1,10),F(1,3),F(-1,3),F(2,3),F(-2,3)):
                    phase=(G(1)+I*a)/(G(1)-I*a);tangent=2*a/(1-a*a);secant=(1+a*a)/(1-a*a)
                    k=add(add(h,scale(e,-tangent)),scale(s,secant-1))
                    lhs=mul(mul(add(t,scale(e,-I)),add(u,scale(e,-phase))),add(s,scale(e,I)))
                    rhs=scale(mul(k,add(e,scale(s,a))),I*(G(1)+phase))
                    assert lhs==rhs,(n,tv,a)
                    count+=1
    # A nonconstant diagonal, exact zero mode and its unit crossing speed.
    s=[[G(F(3,5)),G(F(4,5))],[G(F(4,5)),G(F(-3,5))]];tv=[F(0),F(-5,3)];u=[G(-4),G(3)]
    h=add(s,scale(diag(tv),-1));assert mul(h,[[z] for z in u])==[[G()],[G()]]
    norm=sum((z.conj()*z for z in u),G());weighted=sum(((1+v*v)*z.conj()*z/2 for v,z in zip(tv,u)),G());assert weighted==norm
    return {'exact_pencil_cases':count,'nonconstant_zero_mode_speed_checked':True}

def numerical_checks():
    import itertools
    import numpy as np
    rng=np.random.default_rng(202610191205);matches=0;max_relative=0.;max_kernel=0.;max_ratio=0.;max_involution=0.;counts=[]
    for p,d in ((3,1),(5,1),(3,2)):
        points=np.array(list(itertools.product(range(p),repeat=2*d)),dtype=int);n=len(points)
        omega=points[:,:d]@points[:,d:].T-points[:,d:]@points[:,:d].T
        s=np.exp(2j*np.pi*(omega%p)/p)/np.sqrt(n);e=np.eye(n);inv_error=np.linalg.norm(s@s-e,2);assert inv_error<1e-12;max_involution=max(max_involution,inv_error)
        per_model=0
        for _ in range(12):
            tv=np.tan(np.pi*(rng.random(n)-.5));t=np.diag(tv);u=-1j*((tv+1j)/(tv-1j))[:,None]*s;h=s-t
            assert np.linalg.norm(u@u.conj().T-e,2)<1e-12
            lam=np.linalg.eigvalsh(h);angles=np.angle(np.linalg.eigvals(u));found=set()
            for theta in (-.2,.07,.24):
                a=np.tan(theta/2);k=h-np.tan(theta)*e+(1/np.cos(theta)-1)*s
                lhs=(t-1j*e)@(u-np.exp(1j*theta)*e)@(s+1j*e);rhs=1j*(1+np.exp(1j*theta))*k@(e+a*s)
                error=np.linalg.norm(lhs-rhs)/max(1,np.linalg.norm(lhs),np.linalg.norm(rhs));assert error<1e-11;max_relative=max(max_relative,error)
            for theta in angles[np.abs(angles)<.25]:
                kval=np.linalg.eigvalsh(h-np.tan(theta)*e+(1/np.cos(theta)-1)*s);j=int(np.argmin(np.abs(kval)));err=float(abs(kval[j]));max_kernel=max(max_kernel,err);assert err<1e-8
                if abs(lam[j])<=.125:
                    assert j not in found;found.add(j);delta=abs(float(theta-lam[j]));bound=8*float(lam[j])**2
                    assert delta<=bound+1e-9
                    if abs(lam[j])>1e-7:max_ratio=max(max_ratio,delta/float(lam[j])**2)
                    matches+=1;per_model+=1
            assert found==set(np.flatnonzero(np.abs(lam)<=.125)),(n,lam,angles,found)
        counts.append({'N':n,'p':p,'d':d,'samples':12,'matched_near_zero_points':per_model})
    return {'numpy_version':np.__version__,'matched_points':matches,'models':counts,'max_relative_pencil_residual':max_relative,'max_kernel_residual':max_kernel,'max_observed_quadratic_ratio':max_ratio,'max_involution_error':max_involution}

def main(destination):
    data={'status':'passed_exact_and_finite_numeric_checks',**exact_checks(),**numerical_checks(),
          'scope':'The matrix identity is proved separately; these checks detect signs, order and finite spectral matching errors. No Cauchy-model universality is inferred.'}
    Path(destination).write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data))

if __name__=='__main__':main(sys.argv[1])
