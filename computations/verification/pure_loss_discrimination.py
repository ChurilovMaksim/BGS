#!/usr/bin/env python3
"""Deterministic high-precision audit of the pure-loss two-state bound.

This verifies the scalar inequalities and finite-B block formula used in the
analytic theorem. It is not a substitute for the proof for all real parameters.
"""
from __future__ import annotations
import json, math
import mpmath as mp

mp.mp.dps = 1400


def params(u, eta, n):
    u=mp.mpf(u); eta=mp.mpf(eta); n=int(n)
    q=u*eta**n
    a=1-u+u*(1-eta)**n
    b=q
    c2=u*(1-u)*eta**n
    s=a+b
    r=mp.sqrt((a-b)**2+4*c2)
    d=a*b-c2
    gamma=(a-b)**2/r**2
    delta=1-gamma
    L=-mp.log(gamma)
    ell=(s-r)/2
    return q,a,b,c2,s,r,d,gamma,delta,L,ell


def audit_point(u, eta, n):
    q,a,b,c2,s,r,d,gamma,delta,L,ell=params(u,eta,n)
    eps=mp.mpf('1e-1200')
    assert abs(d-u*u*(eta*(1-eta))**n) < eps + mp.mpf('1e-1100')*max(1,abs(d))
    assert 1-u-eps <= s <= 1+eps
    assert r*r + eps >= (1-2*u)**2
    assert q <= u+eps
    assert delta <= 5*q+eps
    assert abs(delta-4*q) <= 16*u*q+eps
    assert abs(L-4*q) <= 35*u*q+eps
    assert L <= 8*q+eps
    assert ell <= 2*d/s+eps
    return float(delta/q if q else 0), float(abs(L-4*q)/(u*q) if u*q else 0)


def exact_replacement_distance(B, s, gamma):
    # E sqrt(1-gamma^M), evaluated stably by the binomial recurrence.
    B=int(B)
    if B==0: return mp.mpf('0')
    p0=(1-s)**B
    total=p0*0
    prob=p0
    if 1-s == 0:
        return mp.sqrt(1-gamma**B)
    ratio=s/(1-s)
    for m in range(1,B+1):
        prob *= (B-m+1)/m*ratio
        total += prob*mp.sqrt(1-gamma**m)
    return total


def theorem_rhs(u,t):
    return 5*u*t + mp.sqrt(u*(43*t+8*mp.sqrt(t)))


def finite_check(u,eta,n,B):
    q,a,b,c2,s,r,d,gamma,delta,L,ell=params(u,eta,n)
    t=B*q
    repl=exact_replacement_distance(B,s,gamma)
    target=mp.sqrt(1-mp.e**(-4*t))
    # The original distance is not needed: triangle comparison bounds its
    # difference from repl by 2B ell. Check that the proven envelope fits PL.1.
    lhs_bound=2*B*ell + abs(repl-target)
    rhs=theorem_rhs(u,t)
    assert lhs_bound <= rhs + mp.mpf('1e-1000')
    return float(lhs_bound), float(rhs)


def main():
    max_delta=0.; max_L=0.; points=0
    us=[mp.mpf(1)/16, mp.mpf(1)/32, mp.mpf(1)/100,
        mp.mpf(1)/1000, mp.mpf('1e-6')]
    etas=[mp.mpf('1e-6'), mp.mpf('0.001'), mp.mpf('0.01'), mp.mpf('0.1'),
          mp.mpf('0.25'), mp.mpf('0.5'), mp.mpf('0.75'), mp.mpf('0.9'),
          mp.mpf('0.99'), mp.mpf('0.999999'), mp.mpf(1)]
    for u in us:
        for eta in etas:
            for n in [1,2,3,5,10,25,50,100]:
                a,b=audit_point(u,eta,n)
                max_delta=max(max_delta,a); max_L=max(max_L,b); points+=1
    finite=0; worst_ratio=0.0
    for u in [mp.mpf(1)/16,mp.mpf(1)/50,mp.mpf('1e-4')]:
      for eta in [mp.mpf('0.05'),mp.mpf('0.3'),mp.mpf('0.8'),mp.mpf('0.99'),mp.mpf(1)]:
       for n in [1,2,5,20]:
        for B in [1,2,5,20,100]:
            lhs,rhs=finite_check(u,eta,n,B)
            if rhs: worst_ratio=max(worst_ratio,lhs/rhs)
            finite += 1
    out={
      'status':'PASS',
      'scalar_grid_points':points,
      'finite_B_cases':finite,
      'max_delta_over_q':max_delta,
      'max_abs_L_minus_4q_over_uq':max_L,
      'max_proved_lhs_over_theorem_rhs':worst_ratio,
      'scope':'Deterministic high-precision finite checks of scalar inequalities and the binomial replacement formula; analytic proof supplies the continuum theorem.'
    }
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__': main()
