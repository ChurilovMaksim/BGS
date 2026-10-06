#!/usr/bin/env python3
"""Exact characteristic-zero N=7 controls, using integer phase histograms.

Coverage: 49 cube entries, one trace-square identity, 512 multiplicity
triples. Fixed dimension seven only; no finite spectral pivot certificates.
All arithmetic is Python arbitrary-precision integer arithmetic. No inputs,
network, dependencies, source writes or assertions; bounded loops only.
"""
import json


def require(condition, label):
    if not condition:
        raise RuntimeError("Exact N7 check failed: " + label)


def check():
    def exponent(x, y):
        return -(3*x*x - 2*x*y + 3*y*y) % 7
    trace = [0]*7
    for x in range(7):
        trace[exponent(x, x)] += 1
    for x in range(7):
        for y in range(7):
            hist = [0]*7
            for u in range(7):
                for v in range(7):
                    hist[(exponent(x,u)+exponent(u,v)+exponent(v,y)) % 7] += 1
            if x == y:
                hist = [a+7*b for a,b in zip(hist,trace)]
            require(len(set(hist)) == 1, "G^3=-7 trace(G) I")
    trace2 = [0]*7
    for x in range(7):
        for y in range(7):
            trace2[(exponent(x,x)+exponent(y,y)) % 7] += 1
    trace2[0] += 7
    require(len(set(trace2)) == 1, "trace(G)^2=-7")
    possible = [(a,b,c) for a in range(8) for b in range(8) for c in range(8)
                if a+b+c == 7 and a-c == 1 and b-c == 0]
    require(possible == [(3,2,2)], "cube-root multiplicities")
    dimension = sum(v*v for v in possible[0])
    require(dimension == 17, "commutant dimension")
    return {"N":7, "cube_entry_identities":49, "trace_square_identity":True,
            "raw_trace_histogram":trace, "multiplicities":list(possible[0]),
            "complex_commutant_dimension":dimension, "arithmetic":"exact integers"}


def main():
    print(json.dumps(check(), sort_keys=True))


if __name__ == "__main__":
    main()
