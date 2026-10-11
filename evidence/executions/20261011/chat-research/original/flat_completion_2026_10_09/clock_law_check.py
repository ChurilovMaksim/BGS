"""Quantile controls only; no huge N×N completions are allocated here."""
import json
import math
from pathlib import Path
import numpy as np
from scipy.integrate import quad


def primitive(t,law):
    if law=="zero_atom":
        return 2*np.maximum(t-.5,0.)
    if law=="exponential":
        out=np.zeros_like(t)
        mask=t<1
        s=1-t[mask]
        out[mask]=s*np.log(s)-s
        return out
    if law=="pareto_alpha_1_5":
        return -(1-t)**(1/3)
    raise ValueError(law)


def limiting_c1(law):
    if law=="zero_atom":
        return -2j/np.pi
    if law=="exponential":
        re=quad(lambda t:-np.log1p(-t)*np.cos(2*np.pi*t),0,1,epsabs=1e-10)[0]
        im=quad(lambda t:-np.log1p(-t)*np.sin(2*np.pi*t),0,1,epsabs=1e-10)[0]
        return re+1j*im
    re=quad(lambda t:np.cos(2*np.pi*t)/3,0,1,weight="alg",wvar=(0.,-2/3))[0]
    im=quad(lambda t:np.sin(2*np.pi*t)/3,0,1,weight="alg",wvar=(0.,-2/3))[0]
    return re+1j*im


def main():
    cases=[]
    for law in ["zero_atom","exponential","pareto_alpha_1_5"]:
        c1=limiting_c1(law)
        assert c1.imag<0
        for m in [3,5,7,11,31,101,521]:
            endpoints=np.linspace(0,1,m+1)
            raw=m*np.diff(primitive(endpoints,law))
            h=(raw+1/m)/(1+1/m)
            assert h.min()>=1/(m+1)-1e-12
            assert abs(h.mean()-1)<3e-12
            r=m**5
            n=(r+m)*m*(m+1)
            inverse_diagonal=float(np.mean(1/h))
            mu=m*inverse_diagonal/(r+m)
            c=float(h.min())
            assert mu<1
            kappa2=max((r+m)/r,inverse_diagonal)
            assert kappa2<=m+1+1e-9
            ell2=max(kappa2*m/n,32/(9*n)*(2*m*math.log(9)+math.log(32*n)))
            epsilon=10*math.sqrt(n)*ell2
            neighbor=np.mean(h*np.exp(2j*np.pi*np.arange(m)/m))
            second=float(np.mean(h**2))
            defect=float(abs(neighbor)**2+(1-second)/m)
            cases.append({"law":law,"m":m,"formal_completion_dimension_N":n,
                "clock_min":c,"clock_max":float(h.max()),"clock_mean":float(h.mean()),
                "clock_moments_2_to_4":[float(np.mean(h**k)) for k in [2,3,4]],
                "M2_over_m":second/m,"mixing_entry_error_bound_epsilon":float(epsilon),
                "mixture_mass":mu,"mixture_scaled_neighbor_error_bound":4*mu/c,
                "base_neighbor_scaled_defect":defect,"limiting_defect":float(abs(c1)**2),
                "limiting_c1":[float(c1.real),float(c1.imag)]})
    output={"cases":cases,"finite_cases":len(cases),"randomness":"none",
        "scope":["Only the m-dimensional quantile spectra and analytic bounds were computed.",
                 "No N×N matrix was allocated for these enormous formal dimensions.",
                 "The full completion is supplied by the written existence theorem.",
                 "Pareto has infinite second and higher moments; their finite approximants are not uniform moment bounds."]}
    here=Path(__file__).resolve().parent
    path=here/"clock_law_check_results.json"
    path.write_text(json.dumps(output,indent=2)+"\n")
    print(json.dumps({"finite_cases":len(cases),"largest_m_results":[c for c in cases if c['m']==521],
                      "scope":output['scope']},indent=2),flush=True)


if __name__=="__main__":
    main()
