#!/usr/bin/env python3
"""Portable exact author controls; finite scope only. Import has no execution side effects.

Derived mechanically from the losslessly preserved original. Explicit failure
branches remain active under -O. Resource limits belong to the bounded runner.
"""
import itertools, json, time, sys
from fractions import Fraction
import sympy as s
from sympy.polys.domains import QQ_I

def run_checks():
    started = time.monotonic()
    M = 6
    N = 3
    v = s.Matrix([1, 2, 3])
    H = s.eye(N) - v * v.T / s.Integer(7)
    U = H * s.diag(s.I, (3 + 4 * s.I) / 5, -1)
    if s.simplify(U * U.conjugate().T - s.eye(N)) != s.zeros(N):
        raise RuntimeError('unitarity')
    Q = [[QQ_I.from_sympy(U[i, j]) for j in range(N)] for i in range(N)]
    zero = QQ_I.zero
    one = QQ_I.one

    def conj(x):
        return QQ_I.from_sympy(s.conjugate(QQ_I.to_sympy(x)))

    def norm(x):
        return (x * conj(x)).x

    def add(p, key, value):
        p[key] = p.get(key, zero) + value
        if not p[key]:
            p.pop(key)

    def mult(p, q):
        out = {}
        for (d, x), a in p.items():
            for (e, y), b in q.items():
                if d + e <= M:
                    add(out, (d + e, tuple((x[i] + y[i] for i in range(N)))), a * b)
        return out

    def trace_words(k, m):
        out = {}
        for word in itertools.product(range(k), repeat=m):
            a = one
            x = [0] * N
            for t, i in enumerate(word):
                a *= Q[i][word[(t + 1) % m]]
                x[i] += 1
            add(out, (m, tuple(x)), a)
        return out

    def schur_f(k):
        out = {(1, (0,) * N): Q[k][k]}
        for d in range(1, M):
            for word in itertools.product(range(k), repeat=d):
                a = Q[k][word[0]] * Q[word[-1]][k]
                x = [0] * N
                for j in word:
                    x[j] += 1
                for i, j in zip(word, word[1:]):
                    a *= Q[i][j]
                add(out, (d + 1, tuple(x)), a)
        return out
    full_B = {m: sum((norm(a) for a in trace_words(N, m).values())) for m in range(1, M + 1)}
    energy = {m: 0 for m in range(1, M + 1)}
    log_checks = 0
    energy_checks = 0
    for k in range(N):
        f = schur_f(k)
        power = {(0, (0,) * N): one}
        loginc = {}
        for n in range(1, M + 1):
            power = mult(power, f)
            for (d, x), a in power.items():
                y = list(x)
                y[k] += n
                add(loginc, (d, tuple(y)), -a / QQ_I.convert(n))
        for m in range(1, M + 1):
            diff = trace_words(k + 1, m)
            for key, a in trace_words(k, m).items():
                add(diff, key, -a)
            expected = {key: -a / QQ_I.convert(m) for key, a in diff.items()}
            actual = {key: a for key, a in loginc.items() if key[0] == m}
            if actual != expected:
                raise RuntimeError(('log increment', k, m))
            log_checks += 1
        zfp = {(d, x): QQ_I.convert(d) * a for (d, x), a in f.items()}
        power = {(0, (0,) * N): one}
        local = {m: 0 for m in range(1, M + 1)}
        for n in range(1, M + 1):
            A = mult(zfp, power)
            for (d, x), a in A.items():
                local[d] += norm(a)
            power = mult(power, f)
        for m in range(1, M + 1):
            expected = sum((norm(a) * m * m for (d, x), a in loginc.items() if d == m))
            if local[m] != expected:
                raise RuntimeError(('energy increment', k, m))
            energy[m] += local[m]
            energy_checks += 1
    if energy != full_B:
        raise RuntimeError('full energy')
    phase = [s.Rational(3, 5) + s.Rational(4, 5) * s.I, s.I, -s.I]
    identity_checks = 0
    loss_checks = 0
    boundary_checks = 0
    for k in range(1, N + 1):
        a = U[k - 1, k - 1]
        b = U[k - 1, :k - 1]
        c = U[:k - 1, k - 1]
        d = U[:k - 1, :k - 1]
        D = s.diag(*phase[:k - 1]) if k > 1 else s.zeros(0)
        for r in [s.Rational(1, 3), s.Rational(2, 3)]:
            y = (s.eye(k - 1) - r * d * D).inv() * c if k > 1 else s.zeros(0, 1)
            h = a + r * (b * D * y)[0] if k > 1 else a
            lhs = (s.eye(k) - r * s.diag(*phase[:k]) * U[:k, :k]).det()
            rhs = (s.eye(k - 1) - r * D * d).det() * (1 - r * phase[k - 1] * h)
            if s.simplify(lhs - rhs) != 0:
                raise RuntimeError('Schur determinant')
            identity_checks += 1
            vec = s.Matrix([1, *[r * t for t in y]])
            inds = [k - 1, *range(k - 1)]
            T = U.extract(inds, inds) * s.diag(1, *phase[:k - 1])
            loss = (vec.conjugate().T * (s.eye(k) - T.conjugate().T * T) * vec)[0]
            expr = 1 - h * s.conjugate(h) - (1 - r * r) * (y.conjugate().T * y)[0]
            if s.simplify(expr - loss) != 0 or s.simplify(loss) < 0:
                raise RuntimeError('energy loss')
            if k == N and s.simplify(loss) != 0:
                raise RuntimeError('full energy loss')
            loss_checks += 1
        if k == N:
            y = (s.eye(k - 1) - d * D).inv() * c
            h = a + (b * D * y)[0]
            if s.simplify(h * s.conjugate(h) - 1) != 0:
                raise RuntimeError('boundary inner')
            boundary_checks += 1
    z = s.symbols('z')
    moment_checks = []
    for r, a, x, A in [(s.Rational(1, 2), s.Rational(1, 3), s.Rational(2, 5), s.I / 7), (s.Rational(2, 3), (1 + s.I) / 4, (2 - s.I) / 7, (3 + 2 * s.I) / 9), (s.Integer(1), (1 + 2 * s.I) / 5, (3 - s.I) / 8, (2 + 3 * s.I) / 10)]:
        F = A + r * z * x / (1 - r * z * a)
        Fb = s.conjugate(A) + r * s.conjugate(x) / (z - r * s.conjugate(a))
        t = a * s.conjugate(a)
        den = 1 - r * r * t
        p = r * s.conjugate(a)
        vals = []
        for power in [1, 2]:
            integrand = s.cancel((F * Fb) ** power / z)
            res0 = s.limit(z * integrand, z, 0)
            resp = s.diff(s.cancel((z - p) ** power * integrand), z, power - 1).subs(z, p) / s.factorial(power - 1)
            vals.append(s.simplify(res0 + resp))
        ex2 = A * s.conjugate(A) + r * r * x * s.conjugate(x) / den
        coh = (s.conjugate(A) * x * s.conjugate(a) + A * s.conjugate(x) * a) / 2
        ex4 = (A * s.conjugate(A)) ** 2 + 4 * r * r * A * s.conjugate(A) * x * s.conjugate(x) / den + 4 * r ** 4 * x * s.conjugate(x) * coh / den ** 2 + r ** 4 * (x * s.conjugate(x)) ** 2 * (1 + r * r * t) / den ** 3
        if s.simplify(vals[0] - ex2) != 0 or s.simplify(vals[1] - ex4) != 0:
            raise RuntimeError('scalar moment')
        moment_checks.append({'r': str(r), 'second': str(vals[0]), 'fourth': str(vals[1])})
    a = s.sqrt(3)
    Up = s.Matrix([[1, 1 + a, 1 - a], [1 - a, 1, 1 + a], [1 + a, 1 - a, 1]]) / 3
    Um = s.eye(3) - s.ones(3) * s.Rational(2, 3)
    minor_checks = 0
    for size in range(4):
        for subset in itertools.combinations(range(3), size):
            bp = Up.extract(subset, subset).det()
            bm = Um.extract(subset, subset).det()
            if s.simplify(bp * bp - bm * bm) != 0:
                raise RuntimeError('minor moduli')
            minor_checks += 1
    B2 = []
    for V in [Up, Um]:
        if s.simplify(V * V.T - s.eye(3)) != s.zeros(3):
            raise RuntimeError('witness unitarity')
        b = sum((V[i, i] ** 4 for i in range(3))) + sum(((2 * V[i, j] * V[j, i]) ** 2 for i in range(3) for j in range(i + 1, 3)))
        B2.append(str(s.simplify(b)))
    if B2 != ['17/27', '65/27']:
        raise RuntimeError('B2 witness')
    cycle_checks = 0
    for n in [2, 3, 5, 7]:
        C = s.zeros(n)
        for j in range(n):
            C[j, (j + 1) % n] = 1
        for m in range(1, 2 * n + 2):
            got = s.trace(C ** m) ** 2
            if got != (n * n if m % n == 0 else 0):
                raise RuntimeError('cycle')
            cycle_checks += 1
    return {'status': 'passed', 'arithmetic': 'Exact Q(i), Q(sqrt(3)), and rational symbolic residues; no floating tests', 'inputs': {'N': N, 'maximum_power': M, 'U': str(U)}, 'counts': {'log_increment_coefficients': log_checks, 'energy_increment_coefficients': energy_checks, 'schur_determinants': identity_checks, 'contraction_losses': loss_checks, 'boundary_inner': boundary_checks, 'scalar_second_and_fourth_pairs': len(moment_checks), 'principal_minor_pairs': minor_checks, 'cycle_powers': cycle_checks}, 'full_B_through_6': {str(m): str(v) for m, v in full_B.items()}, 'scalar_moments': moment_checks, 'same_minors_distinct_B2': B2, 'caps': {'cpu_seconds': 60, 'address_space_bytes': 2 * 1024 ** 3, 'maximum_dimension': 7, 'max_word_dimension': 3, 'max_word_length': 6, 'max_cycle_power': 15}, 'runtime_seconds': time.monotonic() - started, 'python': sys.version, 'sympy': s.__version__, 'nonclaims': ['No numerical evaluation of actual fixed-tau quantum matrices', 'No large-N universality estimate', 'No independent proof review']}


def main(argv=None):
    import argparse
    from pathlib import Path
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args(argv)
    if args.output is None:
        return 0
    result = run_checks()
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
