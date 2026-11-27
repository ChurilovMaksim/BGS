#!/usr/bin/env python3
"""Exact grouped Hilbert–Schmidt Fejér bound at Pell index 205."""

from collections import defaultdict
from fractions import Fraction as F
from math import isqrt

from crt_splitting_check import literal_coefficients


def require(condition, label):
    if not condition:
        raise RuntimeError(f"Grouped Pell Fejér certificate failed: {label}")


def ceil_sqrt(n):
    a = isqrt(n)
    return a + (a*a < n)


def ceil_div(a, b):
    return -(-a//b)


def step(x, y, dimension):
    return (3*x+4*y) % dimension, (2*x+3*y) % dimension


def main():
    r = 205
    dimension, v = 1, 0
    for _ in range(r):
        dimension, v = dimension+2*v, dimension+v
    coeffs = literal_coefficients()
    literal = {(x % dimension, y % dimension): (a,b)
               for (x,y),(a,b) in coeffs.items()}
    require(len(literal) == 32, "literal support")

    shifted = literal
    aggregate = defaultdict(lambda: [0,0])
    for _ in range(r):
        for xy,(a,b) in shifted.items():
            aggregate[xy][0] += a
            aggregate[xy][1] += b
        shifted = {step(*xy,dimension): c for xy,c in shifted.items()}
    sigma_r = F(sum(a*a+b*b for a,b in aggregate.values()),4000**2)
    require(shifted == literal and len(aggregate) == 6150, "closed modular orbit")
    require(sigma_r == F(r*1650797,4000000), "exact summed Weyl variance")

    Q = 10**10
    src = [(x,y,ceil_div(ceil_sqrt(Q*Q*(a*a+b*b)),4000))
           for (x,y),(a,b) in literal.items()]
    dst = src
    hs = 0
    for _ in range((r-1)//2):
        dst = [(*step(x,y,dimension),w) for x,y,w in dst]
        mass = defaultdict(int)
        for x,y,a in src:
            for u,v,b in dst:
                det = (x*v-y*u) % dimension
                centered = min(det,dimension-det)
                p = ceil_div(355*centered*Q,113*dimension)
                require(p <= 1572*Q//1000, "sine majorant interval")
                sin_upper = ceil_div(120*p*Q**4-20*p**3*Q**2+p**5,120*Q**4)
                mass[((x+u) % dimension,(y+v) % dimension)] += 2*sin_upper*a*b
        hs += ceil_sqrt(sum(x*x for x in mass.values()))
    require(hs == 1704565319048937248481397059063, "102-lag sum")

    time_upper = F(147226335,Q)
    rms_upper = F(91980077327,Q)
    require(time_upper >= F(dimension,10**80) and rms_upper**2 >= sigma_r,
            "time and variance enclosures")
    chord = F(r,2)*time_upper**2*F(hs,Q**3)
    require(chord < F(38,1000), "Duhamel chord")
    factor = F(1001,1000)
    require(factor**2 * (1-chord**2/4) >= 1, "chord-to-angle enclosure")
    angle = F(1736,10000)
    require(time_upper*rms_upper+factor*chord < angle, "return angle")

    window = dimension//4
    require(9*r < window, "all retained lags lie inside the Fejér window")
    lower = F(0)
    for j in range(1,10):
        y = j*angle
        cosine_lower = 1-y*y/2+y**4/24-y**6/720
        require(cosine_lower > 0 and y*y < 3, "positive cosine lower bound")
        lower += F(dimension,window)*(1-F(r*j,window))**2*cosine_lower**2
    require(lower > F(1609,100), "Fejér lower bound")
    print("Pell index 205: exact variance, 102 grouped commutators, Fejer energy > 16.09.")


if __name__ == "__main__":
    main()
