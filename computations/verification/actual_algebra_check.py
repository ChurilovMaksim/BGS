"""Portable exact FM-024 certificate. Importing this module performs no checks or writes."""
from pathlib import Path
import argparse
from actual_commutant_common import verify_data, require

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(__file__).resolve().parents[2] / 'build' / 'actual_commutant')
    args = parser.parse_args(argv)
    data = Path(__file__).resolve().parent / 'actual_commutant_data'
    verify_data(data)
    output = args.output
    output.mkdir(parents=True, exist_ok=True)
    import sympy as s, json, time
    R = output
    S = data
    q, w = s.symbols('q w')
    start = time.time()
    
    def expand_t(t):
        a = [s.Integer(0)] * 7
        a[2 * t % 7] = 1
        for u in range(t + 1, 7):
            a = [s.expand(a[k] + 2 * q ** u * a[(k - 1) % 7] + q ** (2 * u) * a[(k - 2) % 7]) for k in range(7)]
        return a
    C = s.Matrix([expand_t(t) for t in range(7)])
    yd = json.loads((S / 'bounded_boundary_polynomials.json').read_text())
    den = s.sympify(yd['denominator'])
    yn = s.Matrix([[s.sympify(v) for v in yd['y_numerators']]])
    r = s.Matrix([[C[0, (k - 5) % 7] for k in range(7)]])
    require(all((s.expand(v) == 0 for v in yn * C - den * r)), 'exact check failed at original line 11')
    print('Exact seven y numerator identities passed', flush=True)
    DM = s.polys.matrices.DomainMatrix.from_Matrix(C).convert_to(s.GF(5).poly_ring(q))
    AI, ad = DM.inv_den()
    AI = AI.to_Matrix()
    ad = ad.as_expr()
    kd = json.loads((S / 'bounded_boundary_norm_input.json').read_text())
    kden = s.sympify(kd['denominator'])
    loaded = [s.sympify(v) for v in kd['coefficients_w']]
    K = [0] * 7
    for i in range(7):
        for j in range(7):
            shift = (i + j) % 7
            weight = (-1) ** (i + j) * q ** (14 - i - j)
            K[shift] += weight * sum((C[0, (a - i - j) % 7] * AI[a, 0] for a in range(7)))
    K = [s.Poly(s.expand(K[j] - K[6]), q, modulus=5).as_expr() for j in range(6)]
    for j in range(6):
        require(s.Poly(s.expand(K[j] * kden - loaded[j] * ad), q, modulus=5).is_zero, 'exact check failed at original line 23')
    P = DM.det().as_expr()
    require(s.Poly(den, q, modulus=5).monic() == s.Poly(P, q, modulus=5).monic(), 'exact check failed at original line 25')
    require(s.Poly(kden, q, modulus=5).monic() == s.Poly(P, q, modulus=5).monic(), 'exact check failed at original line 26')
    print('K numerator and denominator identities passed', flush=True)
    N = s.zeros(6)
    for c in range(6):
        for k, coeff in enumerate(loaded):
            exponent = (c + k) % 7
            if exponent == 6:
                for j in range(6):
                    N[j, c] -= coeff
            else:
                N[exponent, c] += coeff
    ndm = s.polys.matrices.DomainMatrix.from_Matrix(N).convert_to(s.GF(5).poly_ring(q))
    norm = s.Poly(ndm.det().as_expr(), q, modulus=5)
    pinned = json.loads((S / 'bounded_boundary_norm.json').read_text())
    want = s.Poly.from_list(pinned['norm_coefficients'], q, modulus=5)
    require(norm == want, 'exact check failed at original line 38')
    out = {'seven_y_identities': True, 'K_identity': True, 'denominators_associate_P': True, 'independent_norm_matrix_determinant_matches': True, 'norm_degree': norm.degree(), 'seconds': time.time() - start}
    (R / 'actual_algebra_results.json').write_text(json.dumps(out, indent=2))
    print(json.dumps(out), flush=True)

if __name__ == '__main__':
    main()
