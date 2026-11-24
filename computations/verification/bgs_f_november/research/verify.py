"""Verify the numerical inequalities in the manuscript in exact rational arithmetic."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from fractions import Fraction as F
from pathlib import Path
from decimal import Decimal, getcontext
import json
from coefficients import Q,K,pell
P=Path(__file__).resolve().parent/"data"
getcontext().prec=30
def decimal(v):
    return str(Decimal(v.numerator)/Decimal(v.denominator))
def main():
    b=json.loads((P/"bounds.json").read_text())
    N=pell(K);assert int(b["N"])==N
    dims=b["shapes"];eps=F(8,10**10)
    assert len(dims)==4 and max(dims)<2400
    # Uniform envelope for all powers, from Bernoulli's inequality (negative exponent).
    eta=F(10*max(dims),Q)
    growth=1/(1-2*K*(eps+eta))
    assert growth<F(1000001,1000000)
    error=growth*(K*eps+sum(F(K*10*d*d,Q) for d in dims)+F(1,10**60))
    assert error<F(21,10**8)
    assert all(F(z["exact"])>=0 for z in json.loads((P/"error_budget.json").read_text()).values())
    total=[0,0];sectors=[]
    for lab in ("00","01","10","11"):
        with (P/f"diag{lab}.txt").open() as f:
            pairs=[list(map(int,t.split())) for t in f if t.strip()]
        assert len(pairs)<=max(dims)
        s=[sum(row[j] for row in pairs) for j in (0,1)]
        for j in (0,1):total[j]+=s[j]
        sectors.append({"sector":lab,"diagonal_sum":[str(n) for n in s]})
    re,im=[F(t,Q) for t in total]
    c=F(18,10**6)
    assert re-error>c
    L=10**12;s=10**6
    # sin(x)/x >=1-x^2/6 and exp(-x)>=1-x
    sinc=1-F(4*K*L,N)**2/6
    dgap=c*sinc/2-F(1,2*10**6)
    abel=(1-F(2*s*K,N))*c*c - F(1,4*s*s)
    assert dgap>F(84,10**7) and abel>F(32,10**11)
    T=10**6
    triangular=c*(1-F(4*K*T,N)**2/6)**2/2-F(1,4*T)
    assert triangular>F(874,10**8) and c*c-F(K,N)>F(323,10**12)
    out={"triangular_gap_strict_lower":"0.00000874","signed_interference_normalized_strict_lower":"3.23e-10","normalized_trace_center":[decimal(re),decimal(im)],"error_bound":decimal(error),
         "trace_abs_lower":decimal(c),"rectangular_gap_strict_lower":"0.0000084",
         "abel_gap_strict_lower":"3.2e-10","sectors":sectors}
    print(json.dumps(out,indent=2))
if __name__=="__main__":main()
