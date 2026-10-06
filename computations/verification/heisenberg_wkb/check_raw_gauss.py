import sympy as s, json
from fractions import Fraction as F

def main():
    z = (1 + s.I) / s.sqrt(2)
    c = {'raw_midpoint_phase': 0, 'initial_gauss_sum': 0, 'modular_phase_closure': 0}
    for N in range(1, 32, 2):
        inv2 = pow(2, -1, N) if N > 1 else 0
        inv8 = pow(8, -1, N) if N > 1 else 0
        for k in range(-9, 10):
            for l in [-1, 0, 1]:
                diff = F(k * l, 2) + F(k * inv2 * l, N) - F(k * l, 2 * N)
                if not diff.denominator == 1:
                    raise RuntimeError('exact control failed: diff.denominator == 1')
                c['raw_midpoint_phase'] += 1
        for j in range(N):
            for k in range(N):
                P = 3 * j * j - 2 * j * k + 3 * k * k
                t = j - 3 * k
                diff = F(-P + 3 * N * N * t * t, 8 * N) + F(inv8 * P, N)
                if not diff.denominator == 1:
                    raise RuntimeError('exact control failed: diff.denominator == 1')
                c['modular_phase_closure'] += 1
    for N in [1, 3, 5, 7]:
        for t in range(8):
            lhs = sum((z ** ((-3 * N * r * r + 2 * t * r) % 8) for r in range(4)))
            rhs = 2 * z ** ((-3 * N + 3 * N * t * t) % 8)
            if not s.simplify(s.expand_complex(lhs - rhs)) == 0:
                raise RuntimeError('exact control failed: s.simplify(s.expand_complex(lhs - rhs)) == 0')
            c['initial_gauss_sum'] += 1
    print(json.dumps({'passed': True, 'counts': c, 'arithmetic': 'exact rational/cyclotomic'}, indent=2))
if __name__ == '__main__':
    main()
