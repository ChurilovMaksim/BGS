#!/usr/bin/env python3
"""Exact finite-field certificates for first-order spectral splitting.

No floating-point spectral computation and no matrix exponential is used.
The accompanying exact_spectral_simplicity.md explains the lifting argument.
"""

import argparse
import json
import math
import platform
from pathlib import Path

import numpy as np


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def prime_factors(n):
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out.append(n)
    return out


def primitive_root(p):
    fs = prime_factors(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in fs):
            return g
    raise RuntimeError("No primitive root")


def square_root(a, p):
    a %= p
    if a == 0:
        return 0
    if pow(a, (p - 1) // 2, p) != 1:
        raise ValueError("Not a square")
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    c, x, t, m = pow(z, q, p), pow(a, (q + 1) // 2, p), pow(a, q, p), s
    while t != 1:
        j, tt = 1, t * t % p
        while tt != 1:
            tt = tt * tt % p
            j += 1
        b = pow(c, 1 << (m - j - 1), p)
        x = x * b % p
        t = t * b * b % p
        c, m = b * b % p, j
    assert x * x % p == a
    return x


def cat_order(n):
    a, b, c, d = 1, 0, 0, 1
    for r in range(1, 10 * n * n + 1):
        a, b, c, d = ((3 * a + 2 * b) % n, (4 * a + 3 * b) % n,
                      (3 * c + 2 * d) % n, (4 * c + 3 * d) % n)
        if (a, b, c, d) == (1, 0, 0, 1):
            return r
    raise RuntimeError("Cat order search bound exhausted")


def matmul(a, b, p):
    # Every entry of each input is represented in [0,p).  This is checked
    # globally against signed-int64 overflow before matrices are constructed.
    return (a @ b) % p


def pivot_columns(a, p):
    a = a.copy()
    rows, cols = a.shape
    r, piv = 0, []
    for c in range(cols):
        found = next((j for j in range(r, rows) if a[j, c] != 0), None)
        if found is None:
            continue
        if found != r:
            a[[r, found]] = a[[found, r]]
        a[r] = a[r] * pow(int(a[r, c]), -1, p) % p
        for j in range(r + 1, rows):
            if a[j, c] != 0:
                a[j] = (a[j] - int(a[j, c]) * a[r]) % p
        piv.append(c)
        r += 1
        if r == rows:
            break
    return piv


def inverse(a, p):
    n = len(a)
    b = np.concatenate((a.copy(), np.eye(n, dtype=np.int64)), axis=1)
    for c in range(n):
        r = next((j for j in range(c, n) if b[j, c] != 0), None)
        if r is None:
            raise ValueError("Singular matrix")
        if r != c:
            b[[r, c]] = b[[c, r]]
        b[c] = b[c] * pow(int(b[c, c]), -1, p) % p
        for j in range(n):
            if j != c and b[j, c] != 0:
                b[j] = (b[j] - int(b[j, c]) * b[c]) % p
    return b[:, n:]


def characteristic_polynomial(a, p):
    n = len(a)
    b = np.eye(n, dtype=np.int64)
    coeff = [1]
    for k in range(1, n + 1):
        ab = matmul(a, b, p)
        ck = -int(np.trace(ab)) * pow(k, -1, p) % p
        coeff.append(ck)
        b = ab.copy()
        b[np.diag_indices(n)] = (b[np.diag_indices(n)] + ck) % p
    assert not np.any(b), "Cayley-Hamilton check failed"
    return coeff


def polynomial_trim(a):
    while len(a) > 1 and a[0] == 0:
        a = a[1:]
    return a


def polynomial_remainder(a, b, p):
    a = polynomial_trim(a[:])
    b = polynomial_trim(b[:])
    while a != [0] and len(a) >= len(b):
        z = a[0] * pow(b[0], -1, p) % p
        for j in range(len(b)):
            a[j] = (a[j] - z * b[j]) % p
        a = polynomial_trim(a)
    return a


def squarefree_gcd(coeff, p):
    n = len(coeff) - 1
    derivative = [(n - j) * coeff[j] % p for j in range(n)]
    a, b = coeff[:], polynomial_trim(derivative)
    while b != [0]:
        a, b = b, polynomial_remainder(a, b, p)
    scale = pow(a[0], -1, p)
    return [x * scale % p for x in a]


def exact_matrices(n, p, g):
    zeta, imag = pow(g, (p - 1) // n, p), pow(g, (p - 1) // 4, p)
    inv2, inv8 = pow(2, -1, n), pow(8, -1, n)
    half, inv10, inv100 = pow(2, -1, p), pow(10, -1, p), pow(100, -1, p)
    inv200 = pow(200, -1, p)
    roots = [pow(zeta, j, p) for j in range(n)]
    cos = lambda j: (roots[j % n] + roots[-j % n]) * half % p
    sin = lambda j: (roots[j % n] - roots[-j % n]) * pow(2 * imag, -1, p) % p
    rr = [(1 - cos(7 * j)) * (1 + cos(j)) % p for j in range(n)]
    a = np.zeros((n, n), dtype=np.int64)
    eminus = (-3 - 4 * imag) * pow(5, -1, p) % p
    eplus = (-3 + 4 * imag) * pow(5, -1, p) % p
    for x in range(n):
        a[x, x] = (cos(7 * x) + rr[x] * inv10
                   + rr[x] * sin(x) * inv100 - inv10) % p
        y, mid = (x + 1) % n, (x + inv2) % n
        a[x, y] = (int(a[x, y]) + eminus * rr[mid] * inv200) % p
        a[y, x] = (int(a[y, x]) + eplus * rr[mid] * inv200) % p
    sqn = square_root(n, p)
    sqn_inv = pow(sqn, -1, p)
    m = np.array([[roots[(-inv8 * (3*x*x - 2*x*y + 3*y*y)) % n]
                   * sqn_inv % p for y in range(n)] for x in range(n)], dtype=np.int64)
    return a, m, {"zeta_N": zeta, "i": imag, "sqrt_N": sqn}


def certify_dimension(n, field_multiplier_minimum=1):
    r = cat_order(n)
    modulus = math.lcm(4*n, 8*r)
    field = modulus * field_multiplier_minimum + 1
    while not is_prime(field) or field <= n or field in (2, 5):
        field += modulus
    p, g = field, primitive_root(field)
    assert n * (p - 1) ** 2 < 2**63 - 1, "int64 matmul overflow risk"
    a, m, embedding = exact_matrices(n, p, g)
    ident = np.eye(n, dtype=np.int64)
    powers, current = [], ident
    for _ in range(r):
        powers.append(current.copy())
        current = matmul(current, m, p)
    scalar = int(current[0, 0])
    assert np.array_equal(current, scalar * ident % p), "M^r not scalar"
    root8r = pow(g, (p - 1) // (8*r), p)
    gamma = next((pow(root8r, k, p) for k in range(8)
                  if pow(pow(root8r, k, p), r, p) == scalar), None)
    if gamma is None:
        raise RuntimeError("Scalar phase is not an eighth root in this field")
    gamma_inv, r_inv = pow(gamma, -1, p), pow(r, -1, p)
    normalized = [powers[j] * pow(gamma_inv, j, p) % p for j in range(r)]
    traces = [int(np.trace(b)) % p for b in normalized]
    xi = pow(g, (p - 1) // r, p)
    sectors = []
    all_squarefree = True
    dimension_sum = 0
    for k in range(r):
        coeffs = [pow(xi, (-k*j) % r, p) * r_inv % p for j in range(r)]
        dim = sum(coeffs[j] * traces[j] for j in range(r)) % p
        assert dim <= n, "Projector trace does not represent a dimension"
        dimension_sum += dim
        if dim == 0:
            continue
        sector = {"k": k, "dimension": dim}
        if dim > 1:
            proj = np.zeros((n, n), dtype=np.int64)
            for j in range(r):
                proj = (proj + coeffs[j] * normalized[j]) % p
            columns = pivot_columns(proj, p)
            assert len(columns) == dim
            basis = proj[:, columns]
            rows = pivot_columns(basis.T, p)
            assert len(rows) == dim
            p_ab = matmul(proj, matmul(a, basis, p), p)
            compression = matmul(inverse(basis[rows, :], p), p_ab[rows, :], p)
            char = characteristic_polynomial(compression, p)
            gcd = squarefree_gcd(char, p)
            sector.update({"basis_columns": columns, "basis_rows": rows,
                           "characteristic_polynomial": char,
                           "gcd_with_derivative": gcd,
                           "squarefree": len(gcd) == 1})
            all_squarefree = all_squarefree and len(gcd) == 1
        else:
            sector["squarefree"] = True
        sectors.append(sector)
    assert dimension_sum == n
    return {"N": n, "cat_order": r, "field_prime": p, "primitive_root": g,
            **embedding, "M_power_scalar": scalar, "normalizing_gamma": gamma,
            "xi_order_r": xi, "sectors": sectors,
            "first_order_simple_certificate": all_squarefree}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--maximum", type=int, default=51)
    parser.add_argument("--dimensions", nargs="*", type=int)
    parser.add_argument("--field-multiplier-minimum", type=int, default=1)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("spectral_simplicity_certificates.json"))
    args = parser.parse_args()
    dims = args.dimensions if args.dimensions else range(3, args.maximum + 1, 2)
    result = {"method": "Exact first-order projector compression over a splitting finite field",
              "python": platform.python_version(), "numpy": np.__version__, "dimensions": []}
    for n in dims:
        certificate = certify_dimension(n, args.field_multiplier_minimum)
        result["dimensions"].append(certificate)
        args.output.write_text(json.dumps(result, indent=2) + "\n")
        print(json.dumps({"N": n, "r": certificate["cat_order"],
                          "field": certificate["field_prime"],
                          "maximum_sector_dimension": max(s["dimension"] for s in certificate["sectors"]),
                          "failed_sectors": [s["k"] for s in certificate["sectors"] if not s["squarefree"]],
                          "certificate": certificate["first_order_simple_certificate"]}), flush=True)


if __name__ == "__main__":
    main()
