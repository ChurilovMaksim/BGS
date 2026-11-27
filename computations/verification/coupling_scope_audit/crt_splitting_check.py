#!/usr/bin/env python3
"""Exact residue witnesses for distinct phases on the 3*7**k tower."""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations_with_replacement, product


SQUARES = {1, 2, 4}


def require(condition, label):
    if not condition:
        raise RuntimeError(f"CRT splitting certificate failed: {label}")


def literal_coefficients():
    """Integer real and imaginary parts of the modular Weyl coefficients of 4000*A."""
    shape = {0: 4, 1: 2, -1: 2, 6: -1, -6: -1, 7: -2, -7: -2, 8: -1, -8: -1}
    coefficients = {}
    for k in range(-9, 10):
        value = shape.get(k, 0)
        real = 2000 * (abs(k) == 7) + 100 * value - 400 * (k == 0)
        imag = -5 * (shape.get(k - 1, 0) - shape.get(k + 1, 0))
        if real or imag:
            coefficients[0, k] = (real, imag)
        if value:
            for sign in (-1, 1):
                coefficients[sign, k] = (-3 * value, -4 * sign * value)
    return coefficients


def split_labels(modulus):
    rho = next(r for r in range(3, modulus, 7) if r*r % modulus == 2)
    denominator = pow(-2*rho, -1, modulus)

    def split(u, v):
        return (u + rho*v) % modulus, (u - rho*v)*denominator % modulus

    return split, denominator


def unit_logs(modulus):
    half = pow(2, -1, modulus)
    sixth = pow(6, -1, modulus)
    logs = {}
    for x in range(1, modulus):
        if x % 7:
            u = pow(x, 6, modulus) - 1
            logs[x] = (u - half*u*u)*sixth % modulus
    return logs


def stationary_phases(modulus, modes):
    logs = unit_logs(modulus)
    split, _ = split_labels(modulus)
    half = pow(2, -1, modulus)
    table = defaultdict(list)
    for u, v, cocycle, difference in modes:
        a, b = split(u, v)
        if a % 7 == 0:
            # These modes preserve the square class. The only literal
            # such modes are real, and square modes are tested off diagonal.
            require(not difference, ("discarded diagonal mode", u, v))
            continue
        for x in logs:
            y = (x + a) % modulus
            diagonal = y % 7 in SQUARES
            if x % 7 not in SQUARES or y not in logs or (diagonal and not difference):
                continue
            ell = b*x*y*pow(a, -1, modulus) % modulus
            phase = (b*(x + half*a) + half*cocycle + ell*(logs[y] - logs[x])) % modulus
            simple = b*(2*x + a) % 7 != 0
            table[ell, diagonal].append((phase, (u, v), cocycle, x, simple))
    return table


def check_small_factor():
    """Direct algebra over Q(i,sqrt(3)), and the small numerator over F4."""
    import sympy as sp

    root3 = sp.sqrt(3)
    root = (-1 + sp.I*root3)/2
    vectors = [(0, 1, -1), (1 + root3, 1, 1), (1 - root3, 1, 1)]
    weights = [(1, -sp.Rational(1, 2), -sp.Rational(1, 2)),
               (1, (1 + root3)/4, (1 - root3)/4),
               (1, (1 - root3)/4, (1 + root3)/4)]
    for nu in (-1, 1):
        for eta, (vector, eigenvalue) in enumerate(zip(vectors, (sp.I**nu, 1, -1))):
            for x in range(3):
                value = sum(root**(nu*x*y % 3)*vector[y] for y in range(3))/root3
                require(sp.simplify(value - eigenvalue*vector[x]) == 0, ("small eigenline", nu, eta))
            norm = sum(v*v for v in vector)
            for a, b in product(range(3), repeat=2):
                phases = [nu*b*(x + 2*a) % 3 for x in range(3)]
                value = sum(vector[x]*vector[(x+a) % 3]*root**p
                            for x, p in enumerate(phases))/norm
                require(sp.simplify(value - weights[eta][(a*a+b*b) % 3]) == 0,
                        ("small Weyl weight", nu, eta, a, b))
                # Residue representatives 1, omega, omega²=1+omega.
                support = {1, 2}
                residue = 0
                for x in support:
                    if (x + a) % 3 in support:
                        residue ^= (1, 2, 3)[phases[x]]
                require(residue == int(bool(a or b)), ("small numerator at 2", nu, a, b))


def check_primitive(coefficients):
    literal_modes = [(u, v, 0, bool(imag)) for (u, v), (_, imag) in coefficients.items()]
    table = stationary_phases(343, literal_modes)
    for ell in range(343):
        if ell % 7 in (0, 4):
            continue
        found = False
        for diagonal in (False, True):
            candidates = table[ell, diagonal]
            counts = Counter(row[0] for row in candidates)
            found |= any(phase % 7 and simple and counts[phase] == 1
                         for phase, _, _, _, simple in candidates)
        require(found, ("first order", ell))
    table = stationary_phases(49, literal_modes)
    permitted = {4: {(0, -6)}, 11: {(0, 1)}, 18: {(0, 8)}}
    for ell in range(4, 49, 7):
        require(not table[ell, True], ("scalar diagonal", ell))
        require({row[1] for row in table[ell, False]} == permitted.get(ell, set()),
                ("at most one literal off-diagonal candidate", ell))

    split, _ = split_labels(7**4)
    for (mode,) in permitted.values():
        modulus = 7**4
        a, b = split(*mode)
        center = -a*b*pow(4, -1, modulus) % modulus
        ell = (center + 7**3) % modulus
        discriminant = (a*a*pow(4, -1, modulus) + ell*a*pow(b, -1, modulus)) % modulus
        require(discriminant % modulus and discriminant % 7**3 == 0,
                ("permitted does not mean nonzero", mode))

    odd = [v for v, (re, im) in coefficients.items() if (re + im) % 2]
    require(len(odd) == 12, "odd literal support")
    square = Counter((a + u, b + v, a*v - b*u)
                     for (a, b), (u, v) in product(odd, repeat=2))
    require(sum(m % 2 for m in square.values()) == 108, "midpoint square support")
    retained = [(*term, False) for term, multiplicity in square.items()
                if multiplicity % 2 and (term[0] % 3 or term[1] % 3)]
    require(len(retained) == 102, "small-factor residue support")
    table = stationary_phases(49, retained)
    for j in range(7):
        witness = [(phase, mode, cocycle, x, simple)
                   for phase, mode, cocycle, x, simple in table[4+7*j, False] if phase == 11]
        require(witness == [(11, (0, 10), 0, (39+14*j) % 49, True)],
                ("isolated simple phase over two", 4+7*j))


def check_positive_depth(coefficients):
    modulus = 343
    split, denominator = split_labels(modulus)
    logs = unit_logs(modulus)
    half = pow(2, -1, modulus)
    groups = defaultdict(lambda: (0, 0))
    for (u, v), (re, im) in coefficients.items():
        a, _ = split(u, v)
        if (-a) % 7 in SQUARES:
            norm = u*u - 2*v*v
            old_re, old_im = groups[norm]
            groups[norm] = old_re + re, old_im + im
    require(len(groups) == 11 and all(re or im for re, im in groups.values()), "11 nonzero b_Q")
    q = {norm: norm*denominator % modulus for norm in groups}
    roots = {
        (norm, depth): {value*z*(7**depth*z - 1) % modulus: z for z in logs}
        for norm, value in q.items() for depth in (1, 2, 3)
    }
    require(all(len(table) == 294 for table in roots.values()), "unit stationary roots")
    for mu in logs:
        signs = {norm: mu*pow(value, -1, 7) % 7 in SQUARES for norm, value in q.items()}
        trace = [(u, v) for u, v in product(groups, repeat=2) if signs[u] == signs[v]]
        mixed = [(u, v) for u, v in product(groups, repeat=2) if signs[u] != signs[v]]
        determinant = [(u, v) for u, v in combinations_with_replacement(groups, 2)
                       if signs[u] == signs[v]
                       and sum(a*b for a, b in zip(groups[u], groups[v]))]
        for depth in (1, 2, 3):
            phase = {}
            for norm, value in q.items():
                z = roots[norm, depth][mu]
                phase[norm] = (value*(7**depth*z-half)
                              + 7**depth*mu*(logs[z]-logs[(7**depth*z-1) % modulus])) % modulus
                if depth >= 2:
                    require(phase[norm] == (-value*half-7**depth*mu) % modulus,
                            ("common deep shift", depth, mu, norm))
            differences = Counter((phase[u] - phase[v]) % modulus for u, v in mixed)
            sums = Counter((phase[u] + phase[v]) % modulus for u, v in determinant)
            require(1 in differences.values() and 1 in sums.values(), ("main block", depth, mu))
        require(115 % 49 not in {0} | {(u-v) % 49 for u, v in trace},
                ("depth-two trace exclusion", mu))
        quartic = Counter((u+v-w-x) % modulus for (u, v), (w, x)
                          in product(determinant, repeat=2))
        require(quartic[115] == 1, ("depth-two determinant-square witness", mu))

    table = stationary_phases(7, [(0, -1, 0, False), (0, 1, 0, False)])
    require(table[2, False] == [(2, (0, -1), 0, 1, True), (5, (0, -1), 0, 2, True)],
            "two simple depth-two phases")
    require(table[4, False] == [(0, (0, 1), 0, 2, False)], "one degenerate depth-two class")
    require(all(not table[ell, False] for ell in (1, 3, 5, 6)), "other depth-two classes")


def main():
    coefficients = literal_coefficients()
    split, _ = split_labels(7)
    nonprimitive = {(0, -7), (0, 7)}
    for mode, value in coefficients.items():
        a, b = split(*mode)
        if mode in nonprimitive:
            require(a == b == 0 and value == (1800, 0), ("nonprimitive mode", mode))
        else:
            require(a and b, ("primitive coordinate units", mode))
    require(len(coefficients) == 32 and sum(abs(x)+abs(y) for x,y in coefficients.values()) == 4744,
            "literal coefficient envelope")
    check_small_factor()
    check_primitive(coefficients)
    check_positive_depth(coefficients)
    square_fraction = Fraction(3, 49)/(1-Fraction(1, 49))
    extra = (1 + square_fraction)/6
    density = Fraction(18, 49)*(2 + Fraction(4, 7) + (5+extra)/49 + Fraction(6, 343)
                               + 7*Fraction(1, 7**4)/(1-Fraction(1, 7)))
    require(square_fraction == Fraction(1, 16) and extra == Fraction(17, 96)
            and density == Fraction(266517, 268912), "exact branch density")
    print("Six small eigenlines, 54 Weyl weights and the characteristic-two numerators verified.")
    print("245 primitive first-order classes, seven modulo-49 supports and quadratic witnesses verified.")
    print("294 unit parameters at each of depths 1,2,3 and the depth-two separation verified.")
    print(f"Distinct-eigenvalue lower density: {density}")


if __name__ == "__main__":
    main()
