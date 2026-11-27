#!/usr/bin/env python3
"""Rational constants for the classical axial Fourier bound."""

from fractions import Fraction as F
from math import factorial, isqrt

from crt_splitting_check import literal_coefficients, require


def ceil_sqrt(integer):
    rounded = isqrt(integer)
    return rounded + (rounded*rounded < integer)


def main():
    coefficients = literal_coefficients()
    weighted = [(abs(re)+abs(im), u*u+v*v) for (u,v),(re,im) in coefficients.items()]
    first = sum(weight*ceil_sqrt(norm2) for weight, norm2 in weighted)
    second = sum(weight*norm2 for weight, norm2 in weighted)
    require((first,second) == (29964,205804), "literal Fourier mass")
    require(F(44,7)*F(first,4000) < 48 and F(44,7)**2*F(second,4000) < 2040,
            "Hamiltonian field bounds")

    endpoint = F(1,15*10**9)
    growth = 2040*endpoint
    require(F(3,2)*7*growth/(1-growth) < F(2,10**6), "Green contraction")
    expansion = F(3,2)*7*2040*(24+504)
    require(expansion == 11309760 and expansion + 504*6400 < 15*10**6,
            "inverse displacement constant")
    lower_sqrt2 = F(7,5)
    upper_sqrt2 = F(99,70)
    require(lower_sqrt2**2 < 2 < upper_sqrt2**2, "sqrt(2) enclosure")
    lam_lower = 3 + 2*lower_sqrt2
    exp_175 = sum(F(7,4)**j/factorial(j) for j in range(13)) + (
        F(7,4)**13/factorial(13))/(1-F(7,4*14))
    require(exp_175 < lam_lower and F(204)/(1-1/lam_lower) < 247, "logarithmic modulus")
    require(F(6120)/F(7,4) < 3500 and 504*3500 < 18*10**5, "logarithmic constants")
    require(sum(F(3)**j/factorial(j) for j in range(9)) > 20 and 20**8 > 15*10**9,
            "log endpoint")
    require((F(44,7)*504)**2/2 + F(44,7)*15*10**6 < 10**8
            and F(44,7)*18*10**5 < 114*10**5, "Fourier Taylor constants")
    require(endpoint*(10**8+114*10**5*24) < F(25,1000), "relative endpoint error")
    # Machin's identity and the first alternating bounds.
    a_lower = F(1,5) - F(1,3*5**3)
    a_upper = a_lower + F(1,5**6)
    b_upper = F(1,239)
    b_lower = b_upper - F(1,3*239**3)
    require(F(157,50) < 16*a_lower-4*b_upper < 16*a_upper-4*b_lower < F(22,7),
            "pi enclosure")
    require(F(157,25)**2/(400*upper_sqrt2) > F(67,1000), "axial first derivative")
    require(F(4,10**10)/6 <= endpoint, "signed physical range")
    print("Exact Fourier masses and rational bounds give the axial range 0 < |tau| <= 4e-10.")


if __name__ == "__main__":
    main()
