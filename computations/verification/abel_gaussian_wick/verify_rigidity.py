"""Finite supplements to square_root_rigidity.md; no numerical asymptotic claim."""

import json
from fractions import Fraction
from pathlib import Path

import mpmath as mp

from verify_abel import mpr, q, qper, require


mp.mp.dps = 60


def direct_delta(theta, s):
    N = len(theta)
    theta = list(map(mpr, theta))
    radial = mp.exp(-2*s/N)
    energy = mp.mpf(0)
    for a in theta:
        for b in theta:
            z = radial * mp.exp(2j*mp.pi*(a-b))
            energy += (z/(1-z)).real / N**2
    return energy - 1/mp.expm1(2*s)


def exact_alternating_delta(epsilon, s):
    z = mp.exp(-s)
    c = mp.cos(2*mp.pi*epsilon)
    return z*(1-z)*(1-c)/(2*(1+z)*(1+2*z*c+z*z))


def circle_distance(x, t):
    a = (x-t) % 1
    return min(a, 1-a)


def main():
    ss = list(map(mp.mpf, ["0.15", "1", "3"]))
    epsilons = list(map(Fraction, ["0.001", "0.01", "0.1", "0.2"]))
    maxerr = mp.mpf(0)
    energy_cases = 0
    for N in [2, 4, 8, 12]:
        for eps in epsilons:
            theta = [Fraction(j,N)+eps*Fraction((-1)**j,N) for j in range(N)]
            gaps = [1 + 2*eps*(-1)**(j+1) for j in range(N)]
            deficit = sum(max(Fraction(0),1-g) for g in gaps)/N
            require(deficit == eps, (N,eps,deficit))
            require(sum(abs(g-1) for g in gaps)/N == 2*eps, (N,eps,gaps))
            for s in ss:
                actual = direct_delta(theta, s)
                exact = exact_alternating_delta(mpr(eps),s)
                err = abs(actual-exact)
                require(err < mp.mpf("1e-45"), (N,eps,s,err))
                maxerr = max(maxerr,err)
                e = sum(qper(s,N,N*(mpr(theta[j])-mpr(theta[k])))
                        for j in range(N) for k in range(N) if j!=k)/N
                nearest = sum(q(s,mpr(g)) for g in gaps)/N
                cs = 4*s**3/(mp.pi**2*mp.sinh(s)**2*(s*s+mp.pi**2))
                require(nearest <= e + mp.mpf("1e-45"), (N,eps,s,nearest,e))
                require(cs*mpr(eps)**2 <= nearest + mp.mpf("1e-45"), (N,eps,s))
                require(e <= 2*actual + mp.mpf("1e-45"), (N,eps,s,e,actual))
                energy_cases += 1

    chord_cases = 0
    for s in ss:
        cs = 4*s**3/(mp.pi**2*mp.sinh(s)**2*(s*s+mp.pi**2))
        for g in [Fraction(j,100) for j in range(101)] + [1-Fraction(1,10**j) for j in range(3,13)]:
            require(q(s,mpr(g)) >= cs*(1-mpr(g))**2-mp.mpf("1e-50"), (s,g))
            chord_cases += 1

    lower_bound_cases = 0
    minmargin = None
    for eps in epsilons:
        for offset in [Fraction(k,37) for k in range(74)]:
            points = [Fraction(j) + eps*((-1)**j) - offset for j in range(-4,6)]
            inner = [p for p in points if -1<=p<1]
            require(len(inner)==2, (eps,offset,inner))
            require(circle_distance(inner[0],inner[1]) == 2*eps, (eps,offset,inner))
            for t in [Fraction(k,41) for k in range(41)]:
                # The explicit allowed BL test vanishes at every target-clock atom.
                test_sum = sum(min(circle_distance(p,t),2-abs(p),1) for p in inner)
                require(test_sum >= eps, (eps,offset,t,test_sum))
                margin=test_sum-eps
                minmargin=margin if minmargin is None else min(minmargin,margin)
                lower_bound_cases += 1

    cue_cases = 0
    cue_maxerr = mp.mpf(0)
    for s in ss:
        low = mp.quad(lambda t: t*(mp.sinh(2*s*(1-t))-2*s*(1-t))/(2*mp.sinh(s)**2),[0,1])
        formula = (mp.sinh(2*s)-2*s-mp.mpf(4)/3*s**3)/(8*s**2*mp.sinh(s)**2)
        cue_maxerr=max(cue_maxerr,abs(low-formula))
        require(abs(low-formula)<mp.mpf("1e-50"), (s,low,formula))
        cue_cases+=1

    report={
        "arithmetic":"mpmath 60 decimal digits plus exact rational phase/lower-bound checks",
        "alternating_exact_energy_and_gap_cases":energy_cases,
        "max_exact_energy_absolute_error":mp.nstr(maxerr,12),
        "gap_chord_bound_cases":chord_cases,
        "exact_rational_lower_bound_test_cases":lower_bound_cases,
        "minimum_lower_bound_test_margin":str(minmargin),
        "cue_low_mode_integral_cases":cue_cases,
        "max_cue_integral_absolute_error":mp.nstr(cue_maxerr,12),
        "nonclaims":["finite checks do not prove the analytic theorem", "no BGS physical limit", "no formal Lean certification"],
    }
    Path(__file__).with_name("square_root_receipt.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))


if __name__=="__main__":
    main()
