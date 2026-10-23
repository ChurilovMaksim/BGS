"""Exact finite-grid beta-moment controls and floating differential checks.

This is a control of the written theorem, not a replacement for its proof.
Uses no BGS repository files.
"""
from fractions import Fraction as F
import json
from pathlib import Path
import numpy as np


def rising(a, k):
    result = F(1)
    for j in range(k):
        result *= a+j
    return result


def moment(a, b, k, complement=False):
    value = rising(a, k)/rising(a+b, k)
    return value*b/(a+b+k) if complement else value


def exact_case(field, m, n, terms=64):
    is_complex = field == "complex"
    c = F(m*m*(m-1), m+2) if is_complex else F(m*(m*m-1), m+4)
    shift = 1 if is_complex else 2
    lo = c/(n+shift)
    hi = lo+(F(2*m*(m-1), (n+1)*(n+2)) if is_complex
             else F(3*m*(m-1), (n+2)*(n+4)))
    benchmark = F(2*m, m+1) if is_complex else F(3*m, m+2)
    if m == 1:
        interval = (F(0), F(0))
        assert lo == hi == 0
    elif n == m:
        interval = (m-benchmark, m-benchmark)
        assert interval[0] == hi
    else:
        scale = 1 if is_complex else 2
        a, b = F(m, scale), F(n-m, scale)
        t_a, t_b = F(1, scale), F(m-1, scale)
        base = F(m*(m-1), n+shift)
        corr_max = n*m*moment(a,b,2)*moment(t_a,t_b,2,True)
        corr_min = n*m*moment(a,b,2,True)*moment(t_a,t_b,2,True)
        assert base-corr_max == lo
        assert base-corr_min == hi
        first = corr_min
        partial = F(0)
        for k in range(terms):
            partial += first
            first *= F(a+k+2, a+b+k+3)*F(t_a+k+2, t_a+t_b+k+3)
        # Positive geometric remainder, using (1-x)/(1-xt) <= 1.
        tail = n*m*moment(a,b,terms+2)*moment(t_a,t_b,terms+2,True)
        interval = (max(lo, base-partial-tail), min(hi, base-partial))
        assert interval[0] <= interval[1]
    return {"field":field, "m":m, "N":n,
            "proved_bounds_exact":[str(lo),str(hi)],
            "beta_series_interval_exact":[str(v) for v in interval],
            "beta_series_interval_float":[float(v) for v in interval],
            "positive_series_terms":terms if 1<m<n else 0}


def raw_operator(z):
    q = float(np.vdot(z,z).real)
    if q == 0:
        return np.zeros((z.size*z.size,z.size*z.size),complex)
    qmat = np.outer(z,z.conj())/q
    # Complex Hilbert-space extension of the Hermitian operator preserves HS norm.
    vec = qmat.reshape(-1)
    return q*np.outer(vec,vec.conj())


def differential_check(rng, m, real):
    z = rng.standard_normal(m).astype(complex)
    dz = rng.standard_normal(m).astype(complex)
    if not real:
        z += 1j*rng.standard_normal(m)
        dz += 1j*rng.standard_normal(m)
    q = float(np.vdot(z,z).real)
    u = z/np.sqrt(q)
    a = np.vdot(u,dz)
    v = dz-a*u
    qmat = np.outer(u,u.conj())
    dq = 2*np.sqrt(q)*a.real
    dqm = (np.outer(v,u.conj())+np.outer(u,v.conj()))/np.sqrt(q)
    qv,dqv=qmat.reshape(-1),dqm.reshape(-1)
    df=dq*np.outer(qv,qv.conj())+q*(np.outer(dqv,qv.conj())+np.outer(qv,dqv.conj()))
    expected = 4*q*(a.real*a.real+np.vdot(v,v).real)
    norm = np.linalg.norm(df)**2
    exact_residual = abs(norm-expected)/max(1,expected)
    assert exact_residual < 2e-13
    eps=1e-6
    fd=(raw_operator(z+eps*dz)-raw_operator(z-eps*dz))/(2*eps)
    floating_residual=np.linalg.norm(fd-df)/max(1,np.linalg.norm(df))
    assert floating_residual < 2e-8
    assert norm <= 4*q*np.vdot(dz,dz).real*(1+2e-13)
    return exact_residual,floating_residual


def main():
    cases=[]
    for field in ["complex","real"]:
        for m in [1,2,3,4,8,16,31]:
            for n in sorted({m,m+1,2*m,4*m,max(m,m*m),max(m,128)}):
                cases.append(exact_case(field,m,n))
    rng=np.random.default_rng(202610093)
    residuals=[differential_check(rng,m,real) for real in [False,True]
               for m in [1,2,4,8] for _ in range(16)]
    result={"exact_beta_cases":len(cases),"cases":cases,
            "differential_float_cases":len(residuals),"seed":202610093,
            "max_relative_algebraic_differential_residual":max(x[0] for x in residuals),
            "max_relative_finite_difference_residual":max(x[1] for x in residuals),
            "non_claims":["Rational grid is finite; the uniform theorem is the written proof.",
                          "Series bounds bracket an expectation, not each individual frame.",
                          "No phase-cavity or BGS universality assertion."]}
    Path(__file__).with_name("finite_stiefel_check_results.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k!="cases"}))


if __name__=="__main__":
    main()
