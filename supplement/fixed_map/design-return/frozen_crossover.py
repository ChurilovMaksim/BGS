"""Exact integer/rational certificate for the fixed 10^-80 kick.

No giant quantum matrix is constructed. The certificate checks the
arithmetic period and inequalities used in the accompanying proof.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext
import json
import math


def matmul(a,b,n):
    return [[sum(a[i][k]*b[k][j] for k in range(2))%n
             for j in range(2)] for i in range(2)]


def matpow(a,k,n):
    out=[[1,0],[0,1]]
    while k:
        if k%2:out=matmul(out,a,n)
        a=matmul(a,a,n)
        k//=2
    return out


def dec(x):
    with localcontext() as ctx:
        ctx.prec=65
        return str(Decimal(x.numerator)/Decimal(x.denominator))


def check(k):
    n,f=1,0
    for _ in range(k):n,f=n+2*f,n+f
    assert k%2==1 and n%2==1
    assert n*n-2*f*f==-1
    assert matpow([[3,4],[2,3]],k,n)==[[1,0],[0,1]]
    C=F(127,100)
    t=F(1,10**80)
    eta=C*t*n*n
    delta=C*t*n
    # eta=N times the angular displacement bound. Within a cat cluster
    # the unfolded pair separation is at most eta/pi, hence <1 if eta<3.
    assert eta<3
    assert eta<F(4,5)  # stronger bound used for the sub-Heisenberg window
    # For m in [N/4,N/2], m*delta <= eta/2 < 2/5, so at multiples
    # of k the normalized trace is at least 3/5 in absolute value.
    lo=(n+3)//4
    hi=n//2
    count=hi//k-(lo-1)//k
    positive=F(9,25)*count
    cue_subtraction=F((lo+hi)*(hi-lo+1),2*n*n)
    window_lower=positive-cue_subtraction
    assert window_lower>0
    pair_lower=F(n,k)-1
    # Denominator bound for the regularized s=1 energy.
    energy_lower=pair_lower/(1+4*eta*eta)
    return dict(k=k,N=str(n),pell_coefficient=str(f),
        exact_period_mod_N=True,
        eta_upper=dec(eta),
        one_step_unitary_error_upper=dec(delta),
        classical_gap_defect_upper=dec(2*delta),
        local_pair_mass_lower=dec(pair_lower),
        regularized_pair_energy_lower=dec(energy_lower),
        multiples_in_window=str(count),
        box_form_factor_discrepancy_lower=dec(window_lower),
        scope="Finite-dimensional bounds at the prescribed fixed coupling; no BGS limit claim")


def occupied_arc_check(k):
    n,f=1,0
    for _ in range(k):n,f=n+2*f,n+f
    assert n*n-2*f*f==-1
    assert matpow([[3,4],[2,3]],k,n)==[[1,0],[0,1]]
    delta=F(127*n,100*10**80)
    assert delta<1  # sufficient for the angular spectral inclusion
    eta=n*delta
    # Cover each of at most k spectral arcs by bins of unfolded length 1.
    # Each arc has angular length at most 2*delta. Since pi>3,
    # the total bin count is <=k*(1+eta/3).
    lower=F(n,1)/(k*(1+eta/3))-1
    assert lower>3
    return dict(k=k,N=str(n),angular_radius_upper=dec(delta),
        classical_gap_defect_upper=dec(2*delta),
        local_pair_mass_lower=dec(lower),
        proof="Exact modular period, operator spectral inclusion, occupancy Cauchy-Schwarz",
        scope="One very large finite dimension, not a fixed-coupling asymptotic counterexample")


def coherent_return_check(k):
    assert all(k%d for d in range(2,math.isqrt(k)+1))
    n,f=1,0
    for _ in range(k):n,f=n+2*f,n+f
    assert matpow([[3,4],[2,3]],k,n)==[[1,0],[0,1]]
    assert F(17)*F(22,7)*F(1483,200)**2<3000
    eps=F(n,10**80)
    b=(math.isqrt(k)+1)*(F(117,100)*eps+3000*eps*eps)
    assert b<F(1,2)
    lower=F(9,16)/(F(k,n)+b)-1
    assert lower>3
    return dict(K=k,N=str(n),normalized_HS_return_error_upper=dec(b),
                local_pair_mass_lower=dec(lower),
                source="General finite-symbol coherent normal form, prime K")


if __name__=='__main__':
    print(json.dumps(dict(narrow_clusters=[check(k) for k in (99,101,103,105)],
        wider_clusters=[occupied_arc_check(k) for k in (195,197,199,201,203)],
        coherent_returns=[coherent_return_check(k) for k in (193,197,199)]),indent=2))
