"""Finite floating controls of one-phase projection and inverse-clock averages."""
import json
from pathlib import Path
import numpy as np


def unitary(rng,m):
    g=rng.standard_normal((m,m))+1j*rng.standard_normal((m,m))
    q,r=np.linalg.qr(g)
    return q*(np.diag(r)/np.abs(np.diag(r)))


def control(rng,m,isolated=False):
    l=(rng.standard_normal((m+2,m))+1j*rng.standard_normal((m+2,m)))/np.sqrt(m)
    s=unitary(rng,m) if not isolated else np.diag(np.exp(1j*np.arange(m)))
    b0=np.vstack([l,s])
    x=np.linalg.inv(np.eye(m)+l.conj().T@l)
    e=np.eye(m)[:,0]
    v=s.conj().T@e
    rr=float(np.vdot(e,x@e).real)
    ss=float(np.vdot(v,x@v).real)
    gamma=np.vdot(v,x@e)
    delta=rr*ss-abs(gamma)**2
    a,b=b0@x@e,b0@x@v
    ax,bx=x@e,x@v
    r0=b0@x@b0.conj().T
    w=np.exp(2j*np.pi*(np.arange(4096)+.37)/4096)
    ell=e[None,:]-w.conj()[:,None]*v[None,:]
    denominator=np.einsum("ni,ij,nj->n",ell.conj(),x,ell).real
    y=(a[None,:]-w.conj()[:,None]*b[None,:])/np.sqrt(denominator[:,None])
    yx=(ax[None,:]-w.conj()[:,None]*bx[None,:])/np.sqrt(denominator[:,None])
    mean_removed=y.T@y.conj()/len(w)
    mean_clock_removed=yx.T@yx.conj()/len(w)
    if isolated:
        predicted_removed=np.outer(a,a.conj())/rr
        predicted_clock_removed=np.outer(ax,ax.conj())/rr
        leverage_expected=0.
    else:
        discriminant=np.sqrt((rr+ss)**2-4*abs(gamma)**2)
        zeta=2*gamma/(rr+ss+discriminant)
        def prediction(aa,bb):
            return (np.outer(aa,aa.conj())+np.outer(bb,bb.conj())
                    -zeta.conj()*np.outer(aa,bb.conj())
                    -zeta*np.outer(bb,aa.conj()))/discriminant
        predicted_removed=prediction(a,b)
        predicted_clock_removed=prediction(ax,bx)
        leverage_expected=delta/discriminant
    row=len(l)
    errors={
        "projection_average":float(np.linalg.norm(mean_removed-predicted_removed)),
        "inverse_clock_average":float(np.linalg.norm((mean_clock_removed-predicted_clock_removed)[1:,1:])),
        "removed_leverage_average":float(abs((r0[row,row]-mean_removed[row,row]).real-leverage_expected)),
        "projector_trace_one":float(abs(np.trace(predicted_removed).real-1)),
        "denominator_formula":float(np.max(np.abs(denominator-(rr+ss-2*np.real(w*gamma)))))
    }
    assert max(errors.values())<2e-9,(m,isolated,errors)
    return {"m":m,"isolated":isolated,"residuals":errors}


def main():
    rng=np.random.default_rng(202610094)
    cases=[control(rng,m,isolated) for m in [2,3,5,8]
           for isolated in [False,True] for _ in range(8)]
    output={"cases":cases,"samples":len(cases),"phase_grid_size":4096,"seed":202610094,
            "arithmetic":"complex128",
            "non_claims":["Uniform phase grid is a finite floating control.",
                          "Only first conditional averages are tested; no nonlinear energy drift is inferred.",
                          "No BGS proof."]}
    Path(__file__).with_name("fresh_phase_check_results.json").write_text(json.dumps(output,indent=2)+"\n")
    print(json.dumps({"samples":len(cases),"phase_grid_size":4096,
        "max_residual":max(max(c["residuals"].values()) for c in cases)}))


if __name__=="__main__":
    main()
