#!/usr/bin/env python3
"""Finite checks for exact edge-type regrouping of unitary traces.

The code checks integer counting and finite-dimensional identities only.
It does not prove a BGS limit or extrapolate a proxy coupling.
Run: OPENBLAS_NUM_THREADS=1 python -O verify_edge_occupation.py
"""
from __future__ import annotations
import itertools
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Sequence

import numpy as np
from scipy.linalg import expm


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def det_integer(a: Sequence[Sequence[int]]) -> int:
    """Fraction-free Bareiss determinant, including the empty determinant."""
    b = [list(map(int, row)) for row in a]
    n = len(b)
    if n == 0:
        return 1
    sign, prev = 1, 1
    for k in range(n - 1):
        if b[k][k] == 0:
            pivot = next((i for i in range(k + 1, n) if b[i][k]), None)
            if pivot is None:
                return 0
            b[k], b[pivot] = b[pivot], b[k]
            sign = -sign
        p = b[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = p * b[i][j] - b[i][k] * b[k][j]
                require(numerator % prev == 0, "nonintegral Bareiss quotient")
                b[i][j] = numerator // prev
            b[i][k] = 0
        prev = p
    return sign * b[-1][-1]


def edge_type(word: Sequence[int], n: int) -> tuple[int, ...]:
    counts = [0] * (n * n)
    for a, b in zip(word, tuple(word[1:]) + (word[0],)):
        counts[a * n + b] += 1
    return tuple(counts)


def formula_multiplicity(edges: Sequence[int], n: int) -> int:
    e = [list(edges[i*n:(i+1)*n]) for i in range(n)]
    out = [sum(row) for row in e]
    require(out == [sum(e[i][j] for i in range(n)) for j in range(n)],
            "not an Eulerian type")
    vertices = [i for i, degree in enumerate(out) if degree]
    m = sum(out)
    require(m > 0, "empty word")
    # For an Eulerian connected graph every rooted tree cofactor agrees.
    tree_counts = []
    for root in vertices:
        retained = [i for i in vertices if i != root]
        lap = [[(out[i] if i == j else 0) - e[i][j]
                for j in retained] for i in retained]
        tree_counts.append(det_integer(lap))
    require(len(set(tree_counts)) == 1, "Eulerian cofactors differ")
    tau = tree_counts[0]
    if tau == 0:
        return 0
    numerator = m * tau * math.prod(math.factorial(out[i]-1) for i in vertices)
    denominator = math.prod(math.factorial(x) for x in edges)
    require(numerator % denominator == 0, "nonintegral tour count")
    return numerator // denominator


def matrices(n: int) -> list[tuple[str, np.ndarray]]:
    x = np.arange(n)
    fourier = np.exp(2j*np.pi*np.outer(x, x)/n)/math.sqrt(n)
    ans = [("fourier", fourier)]
    if n % 2 == 1:
        # Exact prescribed matrix formula; proxy coupling for numerical algebra.
        q = x / n
        profile = lambda q: (1-np.cos(14*np.pi*q))*(1+np.cos(2*np.pi*q))
        diag = np.cos(14*np.pi*q) + profile(q)/10 \
            + profile(q)*np.sin(2*np.pi*q)/100 - .1
        inv2, inv8 = pow(2, -1, n), pow(8, -1, n)
        upper = (-3-4j)/1000 * profile(((x+inv2) % n)/n)
        a = np.diag(diag).astype(complex)
        for j in range(n):
            a[j, (j+1) % n] += upper[j]
            a[(j+1) % n, j] += np.conjugate(upper[j])
        xx, yy = np.meshgrid(x, x, indexing="ij")
        phase = (-inv8*(3*xx*xx-2*xx*yy+3*yy*yy)) % n
        metaplectic = np.exp(2j*np.pi*phase/n)/math.sqrt(n)
        u = expm(.03j*n*a) @ metaplectic
        ans.append(("BGS_proxy_tau_0.03", u))
    return ans


def finite_case(n: int, m: int) -> dict:
    counts: Counter = Counter(edge_type(word, n)
                              for word in itertools.product(range(n), repeat=m))
    for edges, observed in counts.items():
        predicted = formula_multiplicity(edges, n)
        require(predicted == observed, f"BEST mismatch N={n} m={m}")
        deg = [sum(edges[i*n:(i+1)*n]) for i in range(n)]
        collisions = sum(v*(v-1)//2 for v in edges)
        exponent = sum(max(r-2, 0) for r in deg) - collisions
        # Exact lower bound C(e) >= m*2**exponent.
        bound = Fraction(m) * (Fraction(2)**exponent)
        require(Fraction(observed) >= bound, "multiplicity lower bound failed")
    total_square_count = sum(v*v for v in counts.values())
    bflat = Fraction(total_square_count, n**m)
    records = []
    max_trace_error, max_decomp_error = 0., 0.
    for label, u in matrices(n):
        require(np.linalg.norm(u.conj().T@u-np.eye(n)) < 2e-11, "unitarity")
        grouped = 0j
        same_edges = 0.
        vertex_group: dict[tuple[int,...], complex] = {}
        for edges, number in counts.items():
            amplitude = 1+0j
            for index, power in enumerate(edges):
                if power:
                    amplitude *= u.flat[index]**power
            grouped += number*amplitude
            same_edges += number**2 * abs(amplitude)**2
            occ = tuple(sum(edges[i*n:(i+1)*n]) for i in range(n))
            vertex_group[occ] = vertex_group.get(occ, 0j) + number*amplitude
        direct = np.trace(np.linalg.matrix_power(u, m))
        phase_average = sum(abs(a)**2 for a in vertex_group.values())
        tr_error = abs(grouped-direct)
        require(tr_error < 5e-9, f"trace regrouping {label}")
        require(phase_average <= n*n + 5e-9, "row-phase unitarity bound")
        require(same_edges > 0, "positive sector")
        if label == "fourier":
            require(abs(same_edges-float(bflat)) < 5e-9, "flat sector exact value")
        # Alias-free finite integration over independent row phases.
        # Total per-coordinate Laurent degree is <=m; grid m+1 is sufficient.
        step = m+1
        phase_integral = 0.
        for labels in itertools.product(range(step), repeat=n):
            diag = np.exp(2j*np.pi*np.array(labels)/step)
            phase_integral += abs(np.trace(np.linalg.matrix_power(diag[:,None]*u, m)))**2
        phase_integral /= step**n
        decomp_error = abs(phase_integral-phase_average)
        require(decomp_error < 5e-9, "row-phase Parseval")
        max_trace_error = max(max_trace_error, tr_error)
        max_decomp_error = max(max_decomp_error, decomp_error)
        records.append({"matrix": label, "same_edge_mass": same_edges,
                        "row_phase_mass": phase_average,
                        "actual_squared_trace": abs(direct)**2,
                        "trace_regrouping_error": tr_error,
                        "row_phase_error": decomp_error})
    # Explicit flat finite-N Jensen lower bound.
    H = m-2*n+2*n*((1-1/n)**m)+m*((1-1/n)**(m-1))
    collision_mean = m*(m-1)/(2*n*n)
    lower = m*2.**(H-collision_mean)
    require(float(bflat) + 1e-10 >= lower, "flat Jensen lower bound")
    return {"N": n, "m": m, "words": n**m, "edge_types": len(counts),
            "flat_sector_exact": str(bflat), "flat_Jensen_lower": lower,
            "matrices": records}


def markov_factorial_checks() -> dict:
    """Exact rational enumeration versus cyclic-gap formula, N=3,m=6."""
    n, m = 3, 6
    # Doubly stochastic, non-symmetric, strictly positive rational example.
    p = [[Fraction(1,2),Fraction(1,3),Fraction(1,6)],
         [Fraction(1,6),Fraction(1,2),Fraction(1,3)],
         [Fraction(1,3),Fraction(1,6),Fraction(1,2)]]
    ident = [[Fraction(i==j) for j in range(n)] for i in range(n)]
    powers = [ident]
    for _ in range(m):
        old = powers[-1]
        powers.append([[sum(old[i][k]*p[k][j] for k in range(n))
                        for j in range(n)] for i in range(n)])
    z = sum(powers[m][a][a] for a in range(n))
    moment_direct = {(a,k):Fraction(0) for a in range(n) for k in range(1,m+1)}
    collisions = Fraction(0)
    for word in itertools.product(range(n), repeat=m):
        weight = math.prod(p[a][b] for a,b in zip(word, word[1:]+word[:1]))/z
        occ = Counter(word)
        for a in range(n):
            for k in range(1,m+1):
                r = occ[a]
                fall = math.factorial(r)//math.factorial(r-k) if r>=k else 0
                moment_direct[a,k] += weight*fall
        edge = Counter(zip(word, word[1:]+word[:1]))
        collisions += weight*sum(c*(c-1)//2 for c in edge.values())
    checks=0
    for a in range(n):
        for k in range(1,m+1):
            total=Fraction(0)
            for chosen in itertools.combinations(range(m),k):
                gaps=[chosen[j+1]-chosen[j] for j in range(k-1)]+[m-chosen[-1]+chosen[0]]
                total+=math.prod(powers[g][a][a] for g in gaps)
            total*=Fraction(math.factorial(k),1)/z
            require(total==moment_direct[a,k],"cyclic gap factorial mismatch")
            checks+=1
    C=max(map(max,p))*n
    bound=Fraction(m*(m-1),2)*C**3/(z*n*n)
    require(collisions<=bound,"collision bound")
    return {"checks":checks,"Z":str(z),"edge_collision_expectation":str(collisions),
            "edge_collision_bound":str(bound)}


def main() -> None:
    result={"status":"finite controls only; no BGS proof",
            "cases":[finite_case(n,m) for n,maxm in [(2,9),(3,8),(4,6)]
                     for m in range(3,maxm+1)],
            "markov":markov_factorial_checks()}
    lower=[]
    for n in [50,100,250,500,1000,2000]:
        m=n
        H=m-2*n+2*n*(1-1/n)**m+m*(1-1/n)**(m-1)
        K=m*(m-1)/(2*n*n)
        lower.append({"N":n,"m":m,"log10_flat_sector_lower":math.log10(m)+(H-K)*math.log10(2),
                      "log10_unitarity_bound":2*math.log10(n)})
    result["flat_explicit_lower"]=lower
    n=m=1009
    v=Fraction(n-1,n)
    F=Fraction(m-2*n)+2*n*v**m+m*v**(m-1)-Fraction(m*(m-1),2*n*n)
    integer_bound=n*2**103
    require(F>103 and integer_bound>10**34, "large flat rational certificate")
    result["large_flat_rational_certificate"]={
        "N":n,"m":m,"exponent_exceeds_integer":103,
        "integer_lower_bound":str(integer_bound),"exceeds_10_power_34":True}
    result["exponent_alpha_one"]=(3/math.e-1)*math.log(2)
    result["total_words"]=sum(x["words"] for x in result["cases"])
    result["total_edge_types"]=sum(x["edge_types"] for x in result["cases"])
    target=Path(__file__).with_name("verification.json")
    target.write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps({k:result[k] for k in ["status","total_words","total_edge_types","markov","exponent_alpha_one","flat_explicit_lower"]},indent=2))

if __name__=="__main__":
    main()
