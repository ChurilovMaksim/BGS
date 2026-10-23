"""Exact checks for the unbounded maximal-primitive subfamily, not full BGS."""
import itertools
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path


def onecycle(p):
    x = p[0]
    count = 1
    while x != 0 and count < len(p):
        x = p[x]
        count += 1
    return count == len(p) and x == 0


def mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def cycle_lengths(p):
    seen = set()
    out = []
    for i in range(len(p)):
        if i in seen:
            continue
        x = i
        length = 0
        while x not in seen:
            seen.add(x)
            length += 1
            x = p[x]
        out.append(length)
    return out


def exact_connection_check():
    results = []
    for n in range(1, 7):
        cycles = []
        for rest in itertools.permutations(range(1, n)):
            word = (0,) + rest
            g = [0] * n
            for a, b in zip(word, word[1:] + word[:1]):
                g[a] = b
            cycles.append(g)
        checked = 0
        for pi in itertools.permutations(range(n)):
            direct = sum(onecycle([g[pi[i]] for i in range(n)]) for g in cycles)
            polynomial = [F(1)]
            for length in cycle_lengths(pi):
                factor = [F((-1)**i * math.comb(length, i)) for i in range(length + 1)]
                factor[-1] -= (-1)**length
                polynomial = mul(polynomial, factor)
            predicted = math.factorial(n-1) * sum(a / (i+1) for i, a in enumerate(polynomial))
            assert predicted == direct, (pi, predicted, direct)
            checked += 1
        results.append({'n': n, 'all_permutations': checked, 'cycles_per_permutation': len(cycles)})
    return results


def divide_one_minus_z(poly):
    out = []
    current = F(0)
    for i in range(max(poly) + 1):
        current += poly.get(i, F(0))
        out.append(current)
    assert out[-1] == 0
    while out and out[-1] == 0:
        out.pop()
    return out


def read_kernels():
    data = json.loads(Path('dependencies/full_port_reference.json').read_text())
    kernels = [{int(i): F(a) for i, a in p.items()} for p in data['summary'][1]['polynomials']]
    u, v, vi, t = kernels
    assert v == vi
    return u, v, t


def quotient_bivariate(u, v, t):
    U, V, T = map(divide_one_minus_z, (u, v, t))
    assert sum(map(abs, U)) == F(83, 18)
    assert sum(map(abs, V)) == F(5, 36)
    assert sum(map(abs, T)) == 1
    # y=1-2x: g=U+V/2+T*y+(3V/2)*y^2; multiply by 72 for integer arithmetic.
    out = {}
    for j, p in enumerate((U, T, V)):
        if j == 0:
            for i, a in enumerate(p):
                out[i, 0] = out.get((i, 0), F(0)) + a
        elif j == 1:
            for i, a in enumerate(p):
                out[i, 1] = out.get((i, 1), F(0)) + a
        else:
            for i, a in enumerate(p):
                out[i, 0] = out.get((i, 0), F(0)) + a/2
                out[i, 2] = out.get((i, 2), F(0)) + 3*a/2
    out = {key: 72*a for key, a in out.items() if a}
    assert all(a.denominator == 1 for a in out.values())
    return {key: int(a) for key, a in out.items()}


def q_moments(maximum):
    # q(x)=(4+3x+x^2)/2; exact polynomial convolution then integration.
    p = [1]
    moments = [F(1)]
    for d in range(1, maximum+1):
        out = [0] * (len(p)+2)
        for i, a in enumerate(p):
            for j, b in enumerate((4, 3, 1)):
                out[i+j] += a*b
        p = out
        moments.append(sum(F(a, i+1) for i, a in enumerate(p)) / 2**d)
    return moments


def nine_port_jet_check(moments):
    order = [(0, 1, 2), (1, 2, 0), (2, 0, 1), (1, 0, 2), (2, 1, 0), (0, 2, 1)]
    # 12 times the coefficients of (1-z) in the six local channels.
    weights = [-34, -1, -1, 4, 4, 4]
    local = []
    for a in range(6):
        for b in range(6):
            for c in range(6):
                pi = list(order[a]) + [x+3 for x in order[b]] + [x+6 for x in order[c]]
                local.append((pi, weights[a]*weights[b]*weights[c]))
    weighted = 0
    nshuffles = 0
    for rest in itertools.permutations(range(1, 9)):
        word = (0,) + rest
        if tuple(x for x in word if x < 3) != (0, 1, 2):
            continue
        if any(tuple(x-base for x in word if base <= x < base+3) not in ((0, 1, 2), (1, 2, 0), (2, 0, 1)) for base in (3, 6)):
            continue
        g = [0] * 9
        for a, b in zip(word, word[1:] + word[:1]):
            g[a] = b
        nshuffles += 1
        for pi, weight in local:
            if onecycle([g[pi[i]] for i in range(9)]):
                weighted += weight
    assert nshuffles == 5040
    actual = F(weighted, math.factorial(3)*12**3)
    predicted = -F(math.factorial(8), 2**3*math.factorial(3))*moments[3]
    assert actual == predicted
    return {'port_count': 9, 'cyclic_shuffles': nshuffles, 'local_channel_choices': len(local),
            'direct_quotient_jet_at_one': str(actual), 'integral_formula_jet_at_one': str(predicted)}


def root_bracket(tau, q, bits=64):
    lo, hi = F(0), tau
    for _ in range(bits):
        mid = (lo+hi)/2
        if mid+mid**2+q*mid**3/2 <= tau:
            lo = mid
        else:
            hi = mid
    return lo, hi


def value(w, q):
    return -(w+q*w*w)/(1+2*w+3*q*w*w/2)


def value_fixedpoint_bracket(tau, q):
    lo, hi = root_bracket(tau, q)
    scale = 2**56
    a = value(hi, q)*scale
    b = value(lo, q)*scale
    return a.numerator//a.denominator, -((-b.numerator)//b.denominator)


def cubic_integral_bracket(tau, subdivisions=1024):
    # At fixed tau: dF/dq=-tau*w*(1+w)/(1+2w+3q*w^2/2)^3 < 0.
    # q increases in x, so left and right Riemann sums give rigorous bounds.
    endpoints = []
    for j in range(subdivisions+1):
        x = F(j, subdivisions)
        q = 2+3*x/2+x*x/2
        endpoints.append(value_fixedpoint_bracket(tau, q))
    lower = F(sum(a for a, b in endpoints[1:]), subdivisions*2**56)
    upper = F(sum(b for a, b in endpoints[:-1]), subdivisions*2**56)
    neutral_lo, neutral_hi = value_fixedpoint_bracket(tau, F(0))
    return lower-F(neutral_hi, 2**56), upper-F(neutral_lo, 2**56)


def limiting_series(tau, moments, maximum=80):
    total = F(0)
    for h in range(2, maximum+1):
        for d in range(1, h//2+1):
            n = h-2*d
            total += F(math.factorial(3*d+2*n-1)*(-1)**(d+n),
                       2**d*math.factorial(d)*math.factorial(n)*math.factorial(h-1))*moments[d]*tau**h
    tail = F(196, 111)*(tau/F(13, 100))**(maximum+1)
    return total, tail


def finite_family_values(G, cases):
    M = max(m for m, N in cases)
    power = {(0, 0): 1}
    totals = [F(0)] * len(cases)
    terms = [0] * len(cases)
    first_two = []
    for d in range(1, M//3+1):
        out = {}
        for (i, j), a in power.items():
            for (k, l), b in G.items():
                if i+k <= M:
                    key = i+k, j+l
                    out[key] = out.get(key, 0)+a*b
        power = {key: a for key, a in out.items() if a}
        H = {}
        for (i, j), a in power.items():
            if j % 2 == 0:
                H[i] = H.get(i, F(0))+F(a, j+1)
        H = {i: a/72**d for i, a in H.items() if a}
        if d <= 2:
            first_two.append(H)
        K = [math.comb(s+2*d-1, 2*d-1) for s in range(M+1)]
        for n in range((M-3*d)//2+1):
            if n:
                prefix = []
                running = 0
                for a in K:
                    running += a
                    prefix.append(running)
                K = [sum(prefix[s-r] for r in range(4) if s >= r) for s in range(M+1)]
            base = F(math.factorial(3*d+2*n-1)*(-1)**n,
                     2**d*math.factorial(d)*4**n*math.factorial(n))
            for index, (m, N) in enumerate(cases):
                if m < 3*d+2*n:
                    continue
                coefficient = sum(a*K[m-2*n-i] for i, a in H.items() if i <= m-2*n)
                totals[index] += m*base*coefficient / N**(2*d+n)
                terms[index] += 1
    # Whole polynomial comparison for d=1 and d=2, not just a value at z=1.
    u, v, t = read_kernels()
    p21 = {i: u.get(i, F(0))+v.get(i, F(0)) for i in set(u)|set(v)}
    assert first_two[0] == {i: a for i, a in enumerate(divide_one_minus_z(p21)) if a}
    p42 = {int(i): F(a) for i, a in json.loads(Path('dependencies/gluing_reference.json').read_text())['P42'].items()}
    quotient = divide_one_minus_z(p42)
    quotient = divide_one_minus_z(dict(enumerate(quotient)))
    assert {i: 15*a for i, a in first_two[1].items()} == {i: a for i, a in enumerate(quotient) if a}
    return [{'m': m, 'N': N, 'ratio': str(F(m, N)), 'terms': terms[i],
             'exact_value': str(totals[i]), 'display_value': float(totals[i])} for i, (m, N) in enumerate(cases)]


def main(destination):
    u, v, t = read_kernels()
    G = quotient_bivariate(u, v, t)
    moments = q_moments(40)
    print('starting exhaustive character-normalization check', flush=True)
    connections = exact_connection_check()
    print('starting nine-port weighted gluing check', flush=True)
    nine = nine_port_jet_check(moments)
    assert -moments[1] == F(-35, 12)
    assert 15*moments[2] == F(1061, 8)
    kappa = F(53, 18)
    assert F(13, 100)+F(1, 5)**2+kappa*F(1, 5)**3 < F(1, 5)
    assert 2*F(1, 5)+3*kappa*F(1, 5)**2 == F(113, 150)
    assert (F(1, 5)+2*kappa*F(1, 5)**2)/(1-2*F(1, 5)-3*kappa*F(1, 5)**2) == F(196, 111)
    limits = []
    print('starting certified cubic integral and all-defect series comparison', flush=True)
    for tau in (F(1, 20), F(1, 10)):
        series, tail = limiting_series(tau, moments)
        lo, hi = cubic_integral_bracket(tau)
        assert lo-tail <= series <= hi+tail
        limits.append({'tau': str(tau), 'series_through_order': 80,
                       'series_exact': str(series), 'series_display': float(series),
                       'uniform_tail_bound_exact': str(tail), 'uniform_tail_bound_display': float(tail),
                       'certified_integral_interval_exact': [str(lo), str(hi)],
                       'certified_integral_interval_display': [float(lo), float(hi)],
                       'interval_method': '1024 monotone Riemann intervals, 64 rational root bisections, outward rounding to 2^-56'})
    print('starting original finite-N sums, all allowed defects and neutral decorations', flush=True)
    finite = finite_family_values(G, [(16, 169), (62, 625), (96, 961)])
    for record in finite:
        lo, hi = cubic_integral_bracket(F(record['m'], record['N']), subdivisions=256)
        record['limit_interval_display'] = [float(lo), float(hi)]
        record['comparison_scope'] = 'Display only; finite-N error is not a numerical proof of the limit.'
    data = {'status': 'passed_all_exact_and_certified_checks',
            'connection_coefficients_all_permutations': connections, 'nine_port_gluing': nine,
            'L1_majorant_C': '53/9', 'majorant_tau_endpoint': '13/100',
            'tail_prefactor': '196/111', 'limit_comparisons': limits, 'finite_N_all_terms': finite,
            'scope': 'Checks the maximal primitive j=2*delta family only, with all allowed delta and neutral n. Full BGS and other primitive families remain open.'}
    Path(destination).write_text(json.dumps(data, indent=2)+'\n')
    print(json.dumps({'status': data['status'], 'nine_port_jet': nine['direct_quotient_jet_at_one'],
                      'limit_displays': [r['series_display'] for r in limits],
                      'finite_N_displays': [r['display_value'] for r in finite]}))


if __name__ == '__main__':
    main(sys.argv[1])
