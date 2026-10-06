#!/usr/bin/env python3
"""Exact finite ramified first-seven controls; no import-time execution.
The uniform valuation/rank argument remains separately reviewed mathematics.
"""
import hashlib, itertools, json, platform, time
from pathlib import Path
import sympy as s
zero = (0,) * 6
one = (1, 0, 0, 0, 0, 0)

def check(ok, msg):
    if not ok:
        raise RuntimeError(msg)

def scalar(k):
    return (k % 5, 0, 0, 0, 0, 0)

def add(a, b):
    return tuple(((u + v) % 5 for u, v in zip(a, b)))

def neg(a):
    return tuple((-v % 5 for v in a))

def sub(a, b):
    return add(a, neg(b))

def mul(a, b):
    c = [0] * 11
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            c[i + j] = (c[i + j] + u * v) % 5
    for k in range(10, 5, -1):
        for j in range(6):
            c[k - 6 + j] = (c[k - 6 + j] - c[k]) % 5
        c[k] = 0
    return tuple(c[:6])

def power(a, n):
    if n < 0:
        check(a != zero, 'Negative power of zero')
        n %= 15624
    b = one
    while n:
        if n % 2:
            b = mul(b, a)
        a = mul(a, a)
        n //= 2
    return b

def inv(a):
    check(a != zero, 'Inverse of zero')
    r = power(a, 15623)
    check(mul(a, r) == one, 'Inverse verification')
    return r

def divide(a, b):
    return mul(a, inv(b))

def ev(poly, z):
    r = zero
    for c in poly:
        r = add(mul(r, z), scalar(int(c)))
    return r

def det(mat):
    out = zero
    n = len(mat)
    for p in itertools.permutations(range(n)):
        term = one
        for i, j in enumerate(p):
            term = mul(term, mat[i][j])
        sign = sum((p[i] > p[j] for i in range(n) for j in range(i + 1, n))) % 2
        out = add(out, neg(term) if sign else term)
    return out

def run():
    start = time.monotonic()
    input_hashes = {'certificate.json': verify_certificate()}
    saved = json.loads(CERTIFICATE.read_text())
    x = s.symbols('x')
    phi = s.Poly(sum((x ** j for j in range(7))), x, modulus=5)
    check(phi.is_irreducible, 'Phi7 irreducibility')
    laurent = s.expand(3 * (x ** 7 - 1) ** 2 * (x + 1) ** 2 * (x - x ** (-1)) * x ** (-8))
    coeff = {k: int(laurent.coeff(x, k)) % 5 for k in range(-9, 10)}
    expected = {int(k): v for k, v in saved['diagonal_B_over5_coefficients'].items()}
    check(all((coeff[k] == v for k, v in expected.items())), 'Raw-model coefficient match')
    check(all((coeff[k] == 0 for k in coeff if k not in expected)), 'Omitted harmonics')
    rec = []
    polys = []
    for idx, ks in enumerate(([1, 6, 8], [2, 5, 9])):
        f = sum((coeff[k] * x ** k / (1 - x ** (2 * k)) for k in ks))
        nn, dd = s.fraction(s.together(f))
        nn = s.Poly(nn, x, modulus=5)
        dd = s.Poly(dd, x, modulus=5)
        gg = s.gcd(nn, dd)
        nn = nn.exquo(gg)
        dd = dd.exquo(gg)
        aa, rr = divmod(nn, phi ** 2)
        check(rr.is_zero, 'Phi7-square divisibility')
        old = saved['rational_coefficients'][idx]
        fromco = lambda c: s.Poly.from_list(c, x, modulus=5)
        check(nn * fromco(old['denominator']) == dd * fromco(old['numerator']), 'Saved rational function')
        check(aa * fromco(old['denominator']) == dd * fromco(old['normalized_numerator']), 'Saved normalized function')
        orig = s.Poly(s.prod((1 - x ** (2 * k) for k in ks)), x, modulus=5)
        check(orig.rem(dd).is_zero, 'Denominator divides displayed product')
        rec.append({'numerator': list(map(int, nn.all_coeffs())), 'denominator': list(map(int, dd.all_coeffs())), 'normalized_numerator': list(map(int, aa.all_coeffs()))})
        polys.append(aa)
    check(s.gcd(*polys) == s.Poly(x, x, modulus=5), 'gcd = x')
    u, v = [s.Poly.from_list(c, x, modulus=5) for c in saved['normalized_numerator_bezout']]
    check(u * polys[0] + v * polys[1] == s.Poly(x, x, modulus=5), 'Saved Bezout identity')
    w = (0, 1, 0, 0, 0, 0)
    check(power(w, 7) == one and w != one, 'Primitive seventh root')
    check(len({power(w, 5 ** i) for i in range(6)}) == 6, 'All primitive roots Frobenius-conjugate')
    xi = [sub(power(w, j), power(w, -j - 1)) for j in range(7)]
    zi = [sub(power(w, 2 * j), power(w, -2 * j - 2)) for j in range(7)]
    check(len(set(xi)) == 7, 'xi pairwise distinct')
    ratios = {divide(sub(zi[k], zi[j]), sub(xi[j], xi[k])) for j in range(7) for k in range(j + 1, 7)}
    check(len(ratios) == 9, 'Exactly nine collision ratios')
    parts = []
    for rho in sorted(ratios):
        values = [add(mul(rho, xi[j]), zi[j]) for j in range(7)]
        groups = sorted([tuple((j for j in range(7) if values[j] == vv)) for vv in set(values)])
        sizes = sorted(map(len, groups))
        check(sizes in [[1, 1, 1, 1, 3], [1, 1, 1, 2, 2]], 'Partition sizes')
        parts.append({'ratio_low_first_phi7_coefficients': rho, 'groups': groups})
    canon = lambda gs: tuple(sorted((tuple(sorted(g)) for g in gs)))
    check({canon(p['groups']) for p in parts} == {canon(p['groups']) for p in saved['exceptional_partitions']}, 'All saved collision partitions match')
    check(sum((max(map(len, p['groups'])) == 3 for p in parts)) == 3, 'Exactly three triple partitions')
    counts = {}
    for m in (1, 2, 3):
        count = 0
        for rows in itertools.combinations(range(7), m):
            for cols in itertools.combinations(range(7), m):
                check(det([[power(w, r * c) for c in cols] for r in rows]) != zero, 'Vanishing Fourier minor')
                count += 1
        counts[m] = count
    ra, rb = rec
    qa = divide(ev(ra['normalized_numerator'], w), ev(ra['denominator'], w))
    qb = divide(ev(rb['normalized_numerator'], w), ev(rb['denominator'], w))
    pure = []
    for e in range(1, 7):
        L = 5 ** e
        N = 7 * L
        h = (N + 1) // 2
        wc = power(w, 2 * L)
        A = mul(sub(one, wc), qa)
        B = mul(sub(one, power(wc, 2)), qb)
        check(A != zero or B != zero, 'Pure ramified nonzero amplitudes')
        pred = [add(mul(A, sub(power(wc, j), power(wc, -j - 1))), mul(B, sub(power(wc, 2 * j), power(wc, -2 * j - 2)))) for j in range(7)]
        direct = []
        for j in range(7):
            su = zero
            for depth in range(L):
                xx = h + depth + j * L
                z = power(w, 2 * xx)
                term = mul(scalar(2 * xx * xx), mul(power(sub(w, one), 2), mul(add(add(z, scalar(2)), power(z, -1)), sub(z, power(z, -1)))))
                su = add(su, term)
            direct.append(su)
        check(direct == pred, 'Pure ramified direct local expansion mismatch')
        pure.append({'e': e, 'N': N, 'distinct_trace_values': len(set(pred)), 'trace_low_first_phi7_coefficients': pred})
    exponents = 0
    for a, b, c, d in itertools.product(range(1, 7), repeat=4):
        if a == b or c == d:
            continue
        plus = sorted(((a * c + b * d) % 7, a * d % 7, b * c % 7))
        minus = sorted(((a * d + b * c) % 7, a * c % 7, b * d % 7))
        check(plus != minus, 'Integer determinant polynomial identically zero')
        exponents += 1
    out = {'status': 'all exact checks passed', 'input_hashes': input_hashes, 'original_independent_review_base': '66724291b2ec77c22823f52ecc5ee56278fed096', 'python': platform.python_version(), 'sympy': s.__version__, 'arithmetic': 'SymPy F5 polynomials; independent tuple arithmetic in F5[w]/Phi7(w)', 'raw_diagonal_coefficients': coeff, 'rational_functions': rec, 'bezout_verified': True, 'collision_partitions': parts, 'fourier_minor_counts_one_primitive_root': counts, 'normalized_3x3_exponent_configurations': exponents, 'pure_ramified_controls': pure, 'runtime_seconds': time.monotonic() - start}
    return out

CERTIFICATE = Path(__file__).resolve().parent / 'ramified_first_seven' / 'certificate.json'
PINNED_CERTIFICATE = 'e902fdcbf042d53b5df4d8be1f9f44bc5e4866a333e85af5f60cbedfa4419f93'

def verify_certificate(path=None):
    path = CERTIFICATE if path is None else Path(path)
    check(path.is_file() and not path.is_symlink(), 'Certificate must be a regular file')
    value = hashlib.sha256(path.read_bytes()).hexdigest()
    check(value == PINNED_CERTIFICATE, 'Reviewed certificate identity mismatch')
    return value

def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.output:
        output = args.output.resolve()
        root = Path(__file__).resolve().parents[2]
        check(not output.is_relative_to(root) or output.is_relative_to(root / 'build'),
              'Output inside maintained source is forbidden')
        check(not output.exists(), 'Refusing to overwrite an existing result')
        output.parent.mkdir(parents=True, exist_ok=True)
    source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    out = run()
    check(verify_certificate() == out['input_hashes']['certificate.json'], 'Input changed during execution')
    check(hashlib.sha256(Path(__file__).read_bytes()).hexdigest() == source_hash, 'Verifier changed during execution')
    out['verifier_sha256'] = source_hash
    out['promotion_scope'] = 'Portable derivative of the independent exact audit; original review inputs are separately hash-preserved. Finite checks do not alone prove the universal theorem.'
    payload = json.dumps(out, indent=2) + '\n'
    if args.output:
        output.write_text(payload)
    print(payload, end='')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
