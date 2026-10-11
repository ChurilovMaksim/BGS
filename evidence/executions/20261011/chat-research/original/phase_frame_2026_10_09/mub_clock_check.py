"""Numerical controls of exact MUB/clock identities and Schur realization."""
import json
from pathlib import Path
import numpy as np
from scipy.linalg import null_space
from frame_probe import hermitian_coordinates


def mub_rows(m):
    x=np.arange(m)
    rows=[np.eye(m,dtype=complex)]
    for b in range(m):
        cols=np.stack([np.exp(2j*np.pi*(b*x*x+k*x)/m)/np.sqrt(m) for k in range(m)],axis=1)
        rows.append(cols.conj().T)
    return np.concatenate(rows)


def sqrt_pair(h):
    eig,v=np.linalg.eigh(h)
    assert eig.min()>0
    return (v*np.sqrt(eig))@v.conj().T,(v/np.sqrt(eig))@v.conj().T


def covariance(rows,h):
    hs,_=sqrt_pair(h)
    b=rows@hs
    weight=np.sum(np.abs(b)**2,axis=1)
    p=np.abs(b)**2
    return (p.T@(p/weight[:,None]))/(h.shape[0]+1)


def target_frame(m):
    target=np.eye(m*m)/(m+1)
    target[:m,:m]+=1/(m+1)
    return target


def mixture_realization(m,r,a):
    base=mub_rows(m)
    shift=np.roll(np.eye(m),1,axis=0)
    h=np.eye(m)+(a/2)*(shift+shift.T)
    hs,his=sqrt_pair(h)
    hinv=his@his
    n=(r+m)*m*(m+1)
    lam=np.diag(hinv).real/(r+m)
    mu=float(lam.sum())
    assert mu<1
    standard_cov=covariance(base,h)
    m2=np.trace(h@h).real/m
    formula=(np.ones((m,m))+np.abs(h)**2+(1-m2)/m)/(m+1)
    base_error=np.linalg.norm(standard_cov-formula)
    theta=0.13+2*np.pi*np.arange(m)/m
    s=np.diag(np.exp(1j*theta))
    removed=[np.tile(base,(r,1))*np.sqrt((1-mu)/(r*(m+1)))]
    retained=[]
    cov_mix=(1-mu)*standard_cov
    for j in range(m):
        u=his[:,j]/np.sqrt(hinv[j,j].real)
        rotation=np.column_stack([u,null_space(u.conj()[None,:])])
        assert np.linalg.norm(rotation.conj().T@rotation-np.eye(m))<1e-12
        rows=base@rotation.conj().T
        rowq=lam[j]/(m+1)
        removed.append(np.sqrt(rowq)*rows[1:])
        retained.append(np.exp(1j*theta[j])*np.sqrt(rowq)*rows[0])
        cov_mix+=lam[j]*covariance(rows,h)
    z=np.concatenate([*removed,np.stack(retained)])
    assert z.shape==(n,m)
    q=np.sum(np.abs(z)**2,axis=1)
    coord=hermitian_coordinates(z)/np.sqrt(q[:,None])
    fwhite=coord.T@coord
    b=np.sqrt(n/m)*z@hs
    l=b[:-m]
    k=np.vstack([l,np.eye(m)])
    t=k.conj().T@k
    projection=k@np.linalg.solve(t,k.conj().T)
    w=2*projection-np.eye(n)
    w[-m:]*=np.exp(1j*theta[:,None])
    ell=np.linalg.solve(np.eye(n-m)-w[:-m,:-m],w[:-m,-m:])
    schur=w[-m:,-m:]+w[-m:,:-m]@ell
    p=np.abs(b)**2
    weights=p.sum(axis=1)
    actual_cov=(m/n)*(p.T@(p/weights[:,None]))
    errors={
        "base_covariance_formula":float(base_error),
        "stiefel_normalization":float(np.linalg.norm(z.conj().T@z-np.eye(m))),
        "white_frame_identity":float(np.linalg.norm(fwhite-target_frame(m))),
        "retained_unitary_rows":float(np.linalg.norm(b[-m:]-s)),
        "clock_identity":float(np.linalg.norm((m/n)*t-h)),
        "graph_unitarity":float(np.linalg.norm(w.conj().T@w-np.eye(n))),
        "schur_retained":float(np.linalg.norm(schur-s)),
        "schur_extension":float(np.linalg.norm(ell-l)),
        "mixture_covariance":float(np.linalg.norm(actual_cov-cov_mix)),
        "flat_clock_covariance_row_sums":float(np.linalg.norm(actual_cov.sum(axis=1)-np.ones(m)))
    }
    assert max(errors.values())<2e-8,errors
    return {"m":m,"N":n,"r":r,"a":a,"mixture_mass":mu,"residuals":errors,
            "base_scaled_covariance_error_op":float(np.linalg.norm((m+1)*standard_cov-np.eye(m)-np.ones((m,m)),2)),
            "mixture_scaled_covariance_error_op":float(np.linalg.norm((m+1)*actual_cov-np.eye(m)-np.ones((m,m)),2)),
            "graph_diagonal_transition_mean":float(np.mean(np.abs(np.diag(w))**2))}


def main():
    controls=[]
    for m in [3,5,7]:
        rows=mub_rows(m)
        matrices=rows.reshape(m+1,m,m)
        for b in range(m+1):
            for c in range(m+1):
                overlaps=np.abs(matrices[b]@matrices[c].conj().T)**2
                expected=np.eye(m) if b==c else np.full((m,m),1/m)
                assert np.linalg.norm(overlaps-expected)<2e-12
        controls.append(mixture_realization(m,2*m,.4))
    output={"cases":controls,"arithmetic":"complex128","randomness":"none",
            "non_claims":["Exact theorem is the written algebra, not this floating computation.",
                          "Realization holds at one phase point, not a phase-averaged law.",
                          "Graph-reflection matrix does not meet uniform classical mixing hypotheses.",
                          "This is not a counterexample to BGS."]}
    Path(__file__).with_name("mub_clock_check_results.json").write_text(json.dumps(output,indent=2)+"\n")
    print(json.dumps(output,indent=2))


if __name__=="__main__":
    main()
