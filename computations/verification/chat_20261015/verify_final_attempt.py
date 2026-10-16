#!/usr/bin/env python3
"""Final-pass exact and high-precision checks, not a proof of physical BGS.

Deleted-clock spectra test the limits of strict Hardy positivity and fixed
trace bounds. The formulas use no proxy quantization and concern an abstract
spectral control. No output is a claim about U_N=exp(i*10^-80*N*A_N)M_N.
"""
from fractions import Fraction as Q
from pathlib import Path
import json, math
import mpmath as mp

def need(ok, msg):
    if not ok:
        raise AssertionError(msg)

def deleted_energy_r(n, r):
    x = r*r
    return x/(n*n*(1-x)) + Q(n*n-1,n*n)*x**(n+1)/(1-x**(n+1))

def clock_energy_r(n, r):
    x = r*r
    return x**n/(1-x**n)

def periodic_trace_energy(n, r):
    x = r*r
    # One period N+1, followed by its geometric repetitions.
    period = sum((Q(n*n) if k==n+1 else Q(1))*x**k
                 for k in range(1,n+2))
    return period/(n*n*(1-x**(n+1)))

def main():
    mp.mp.dps = 80
    exact=0
    min_checks=0
    for n in range(2,31):
        for r in (Q(1,3),Q(1,2),Q(2,3),Q(9,10)):
            lhs=deleted_energy_r(n,r)
            rhs=periodic_trace_energy(n,r)
            need(lhs==rhs, 'periodic trace summation mismatch')
            need(lhs>clock_energy_r(n,r), 'strict Hardy positivity failed')
            exact+=1
    records=[]
    for sstr in ('0.25','1','2'):
        s=mp.mpf(sstr)
        limit=1/mp.expm1(2*s)
        alpha=1/(2*s)-s/(2*mp.sinh(s)**2)
        need(alpha>0, 'asymptotic coefficient must be positive')
        errors=[]
        for n in (101,1001,10001,100001):
            deleted=1/(n*n*mp.expm1(2*s/n))+(1-mp.mpf(1)/(n*n))/mp.expm1(2*s*(1+mp.mpf(1)/n))
            excess=deleted-limit
            need(excess>0,'positive excess')
            scaled=n*excess
            error=abs(scaled-alpha)
            errors.append(error)
            records.append({'s':sstr,'N':n,
                'L_deleted':mp.nstr(deleted,45),
                'L_clock':mp.nstr(limit,45),
                'N_excess':mp.nstr(scaled,45),
                'predicted_limit':mp.nstr(alpha,45),
                'absolute_error':mp.nstr(error,15)})
        need(errors[-1]<errors[0]/100,'first order asymptotic check')
    # Stable pair window: deleted clock has trace -1 throughout m < N+1.
    pair=[]
    for n in (101,1001,10001):
        modes=[m for m in range(1,n) if Q(1,8)<=Q(m,n)<=Q(1,4)]
        val=sum((Q(1)-m) for m in modes)/n**2
        pair.append({'N':n,'box_pair_defect':float(val),
                     'limiting_value':-3/128})
    need(abs(pair[-1]['box_pair_defect']+3/128)<0.0001,'non-CUE box defect')
    result={'status':'finite checks and asymptotic control only; physical BGS unproved',
            'exact_rational_spectra':exact,
            'strict_positivity_checks':exact,
            'high_precision_rows':records,
            'pair_control':pair,
            'claims':['exact deleted-clock energy','strict positive Hardy excess',
                      'excess=(1/(2s)-s/(2sinh(s)^2))/N+O_s(N^-2)',
                      'fixed traces do not determine microscopic CUE law']}
    out=Path(__file__).with_name('final_attempt_results.json')
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print('PASS',exact,'exact rational cases;',len(records),'high-precision rows')
    print('Pair control:',pair)
    print('Output:',out)
if __name__=='__main__':
    main()
