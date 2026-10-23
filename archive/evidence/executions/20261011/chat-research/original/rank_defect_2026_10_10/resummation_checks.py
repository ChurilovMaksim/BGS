"""Exact rational checks of inactive-label summation; no asymptotic inference."""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from math import factorial
from pathlib import Path
import json

from independent_checks import alpha, partitions

ROOT = Path(__file__).resolve().parent


def mul(a, b, limit):
    out = [Fraction(0)] * (limit+1)
    for i,u in enumerate(a[:limit+1]):
        for j,v in enumerate(b[:limit+1-i]):
            out[i+j] += u*v
    return out


@lru_cache(None)
def Fpower(exponent, limit):
    assert exponent >= 0
    base = [Fraction(1,factorial(j)**2) for j in range(limit+1)]
    result = [Fraction(1)] + [Fraction(0)]*limit
    while exponent:
        if exponent % 2:
            result = mul(result,base,limit)
        exponent //= 2
        if exponent:
            base = mul(base,base,limit)
    return tuple(result)


def compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for j in range(1,total-length+2):
        for rest in compositions(total-j,length-1):
            yield (j,)+rest


@lru_cache(None)
def P_polynomial(s, limit):
    # Independent log-derivative formula in terms of F and its derivatives.
    out = [Fraction(0)]*(limit+1)
    for length in range(1,s+1):
        factor = Fraction(factorial(s)*(-1)**(length-1),length)
        for js in compositions(s,length):
            term = list(Fpower(s-length,limit))
            for j in js:
                derivative_divided_by_factorial = [
                    Fraction(1,factorial(t)*factorial(t+j)*factorial(j))
                    for t in range(limit+1)]
                term = mul(term,derivative_divided_by_factorial,limit)
            out = [u+factor*v for u,v in zip(out,term)]
    return tuple(out)


def check_P():
    count = 0
    for s in range(1,9):
        for limit in range(9-s):
            values = alpha(s+limit)
            logarithmic_derivative = [values[s+t]/factorial(t)
                                      for t in range(limit+1)]
            assert tuple(mul(Fpower(s,limit),logarithmic_derivative,limit)) == (
                P_polynomial(s,limit)), (s,limit)
            count += 1
    return count


def restriction(blocks,k):
    return tuple(tuple(i for i in b if i<k) for b in blocks
                 if any(i<k for i in b))


def check_W(N,n,k):
    values = alpha(n)
    actual = defaultdict(Fraction)
    for blocks in partitions(n):
        weight = Fraction(1)
        for block in blocks:
            weight *= values[len(block)]
        actual[restriction(blocks,k)] += weight / N**(n-len(blocks))
    m = n-k
    expected = {}
    for sigma in partitions(k):
        coefficient_series = list(Fpower(N,m))
        for block in sigma:
            s = len(block)
            coefficient_series = mul(coefficient_series,
                [values[s+t]/factorial(t) for t in range(m+1)],m)
        g = k-len(sigma)
        expected[sigma] = factorial(m)*coefficient_series[m]/N**(m+g)
        if N >= k:
            entire_series = list(Fpower(N-k,m))
            for block in sigma:
                entire_series = mul(entire_series,P_polynomial(len(block),m),m)
            assert entire_series == coefficient_series, (N,n,k,sigma,'entire')
    assert dict(actual) == expected, (N,n,k)
    return {'N':N,'n':n,'active_vertices':k,'active_partitions':len(expected),
            'entire_expression_checked':N>=k}


def main():
    p_cases = check_P()
    cases = [check_W(N,n,k) for n in range(8) for k in range(n+1)
             for N in (1,2,5,8)]
    cases += [check_W(N,8,k) for k in (0,4,8) for N in (1,3,8)]
    result = {'all_passed':True,'P_polynomial_cases':p_cases,'W_cases':cases,
              'scope':'Exact formal identities on finite rational cases; '
                      'the general proof is in inactive_resummation.md.'}
    (ROOT/'resummation_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'all_passed':True,'P_polynomial_cases':p_cases,
                      'W_parameter_cases':len(cases),
                      'W_coefficients':sum(c['active_partitions'] for c in cases)}))


if __name__ == '__main__':
    main()
