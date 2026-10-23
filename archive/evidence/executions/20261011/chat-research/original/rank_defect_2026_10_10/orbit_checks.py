"""Exact word-orbit controls and numerical illustrations of a proved saddle law."""
from collections import Counter
from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import product
from math import factorial
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent


def multiply(a,b,limit):
    out=[Fraction(0)]*min(len(a)+len(b)-1,limit+1)
    for i,u in enumerate(a):
        for j,v in enumerate(b[:max(0,limit+1-i)]):
            out[i+j] += u*v
    return out


def occupation_coefficient(N,n):
    base=[Fraction(1,factorial(m)**2) for m in range(n+1)]
    out=[Fraction(1)]
    exponent=N
    while exponent:
        if exponent%2:
            out=multiply(out,base,n)
        exponent//=2
        if exponent:
            base=multiply(base,base,n)
    return factorial(n)*out[n]/N**n


def orbit(word):
    reversed_word=tuple(reversed(word))
    return {w[i:]+w[:i] for w in (word,reversed_word) for i in range(len(word))}


def direct_case(N,n):
    inverse_stabilizer=Fraction(0)
    orbit_count=0
    for word in product(range(N),repeat=n):
        f=1
        for m in Counter(word).values():
            f*=factorial(m)
        inverse_stabilizer += Fraction(1,f)
        orbit_count += len(orbit(word))
    Z=inverse_stabilizer/N**n
    diagonal=Fraction(orbit_count,N**n)
    assert Z==occupation_coefficient(N,n)
    # Square both positive sides to check the bound without square roots.
    deficit=2*n-diagonal
    assert deficit>=0
    assert deficit**2 <= Fraction((2*n*(2*n-1))**2)*Fraction(N)**(2-n)
    if n==5:
        assert diagonal==10-Fraction(25,N**2)+Fraction(16,N**4)
    return {'N':N,'n':n,'words':N**n,'Z':str(Z),
            'physical_diagonal':str(diagonal),
            'dihedral_permutation_sector':str(2*n*Z)}


def bessel_saddle(tau):
    def F_and_mean(rho):
        term,total,weighted=Decimal(1),Decimal(1),Decimal(0)
        for m in range(1,1000):
            term*=rho/Decimal(m*m)
            total+=term
            weighted+=m*term
            if term < Decimal('1e-65')*total:
                return total,weighted/total
        raise ArithmeticError('Positive series did not settle within 1000 terms')
    def mean(rho):
        if not rho:
            return Decimal(0)
        return F_and_mean(rho)[1]
    lo,hi=Decimal(0),max(Decimal(1),tau*tau+tau+1)
    while mean(hi)<tau:
        hi*=2
    for _ in range(240):
        mid=(lo+hi)/2
        if mean(mid)<tau:
            lo=mid
        else:
            hi=mid
    rho=(lo+hi)/2
    assert abs(mean(rho)-tau)<Decimal('1e-50')
    variance=rho-tau*tau
    assert variance>0
    F,_=F_and_mean(rho)
    rate=tau*tau.ln()-tau+F.ln()-tau*rho.ln()
    assert rate<0
    return rho,variance,rate


def main():
    exact=[direct_case(N,n) for N in (2,3,4,5) for n in range(3,7)]
    getcontext().prec=60
    illustrations=[]
    for tau in (Decimal('0.5'),Decimal(1),Decimal(2)):
        rho,variance,rate=bessel_saddle(tau)
        for N in (4,8,16,32):
            n=int(tau*N)
            value=occupation_coefficient(N,n)
            z=Decimal(value.numerator)/value.denominator
            leading=(tau/variance).sqrt()*(N*rate).exp()
            illustrations.append({'N':N,'n':n,'tau':str(tau),
                 'rho':str(rho),'variance':str(variance),
                 'exponential_rate':str(rate),
                 'exact_Z':str(value),'saddle_approximation':str(leading),
                 'ratio_exact_to_approximation':str(z/leading),
                 'status':'Numerical illustration of a separately proved asymptotic; not an error certificate.'})
    result={'all_passed':True,'exact_cases':exact,'saddle_illustrations':illustrations,
            'scope':'Distinct words, not permutation representations. Finite exact checks do not prove the asymptotic.'}
    (ROOT/'orbit_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'all_passed':True,'exact_word_cases':len(exact),
                      'exact_words':sum(c['words'] for c in exact),
                      'saddle_illustrations':len(illustrations)}))


if __name__=='__main__':
    main()
