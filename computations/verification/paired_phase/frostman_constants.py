"""Exact constants for the reviewed Sections1-3 only; imports are silent."""
from fractions import Fraction as F
from pathlib import Path
import hashlib, json
from decimal import Decimal, localcontext

def run():
    EXPECTED = '2bddd915330543828c5637ea966f8b2081ce79208655c4632342b3f351391ee9'
    checks = []

    def check(name, condition, detail=''):
        if not condition:
            raise RuntimeError(name)
        checks.append({'name': name, 'passed': True, 'detail': detail})

    def sha(p):
        return hashlib.sha256(p.read_bytes()).hexdigest()
    check('frozen original target hash', sha(TARGET) == EXPECTED)
    slo = F(1414213562373095, 10 ** 15)
    shi = F(1414213562373096, 10 ** 15)
    check('rational enclosure for sqrt(2)', slo * slo < 2 < shi * shi)
    llo, lhi = (3 + 2 * slo, 3 + 2 * shi)
    beta = F(29, 5)
    eta = F(1, 10 ** 70) + F(1, 10 ** 110)
    check('beta below lambda below seven', 1 < beta < llo < lhi < 7)
    check('eta inequalities', 0 < eta < F(2, 10 ** 70) < F(1, 36) < F(1, 16))
    Lbound = (lhi + beta) / (slo * (llo - beta))
    check('infinite beta Green norm below 300', Lbound < 300, str(Lbound))
    check('nonlinear Hessian beta norm below 14 eta', 2 * (1 + beta) < 14)
    check('resolvent at most 301', 300 / (1 - 4200 * eta) <= 301)
    check('resolvent difference constant', 301 * 14 * 300 == 1264200)
    check('G E constant', 301 * 14 == 4214)
    period = 600 * beta / (beta - 1)
    check('nonzero period sum constant', period == 725)
    check('defect beta locality constant', 4214 * 725 <= 4 * 10 ** 6)
    holder_bound = 2 * lhi / (llo - beta) + 2 * beta / (beta - 1)
    check('Holder split constant below 500', holder_bound < 500, str(holder_bound))
    check('Holder final constant below 2e7', 301 * 32 * 500 * 4 < 2 * 10 ** 7)
    check('positive mass and negative off-diagonals', 1 - 4 * eta > 0 and F(1, 4) - eta > 0)
    check('one-neighbour propagation factor at least 1/7', (F(1, 4) - eta) / (F(3, 2) + 2 * eta) >= F(1, 7))
    check('inverse Holder prefactor identity', F(4, 7) / 16 == F(1, 28))

    def inverse_first_column(m):
        A = [[F(0) for _ in range(m + 1)] for __ in range(m)]
        for i in range(m):
            A[i][i] += F(3, 2)
            A[i][(i - 1) % m] -= F(1, 4)
            A[i][(i + 1) % m] -= F(1, 4)
        A[0][m] = 1
        for i in range(m):
            pivot = A[i][i]
            A[i] = [x / pivot for x in A[i]]
            for j in range(m):
                if j == i:
                    continue
                a = A[j][i]
                A[j] = [x - a * y for x, y in zip(A[j], A[i])]
        return [r[-1] for r in A]
    cycles = []
    for m in range(1, 25):
        v = inverse_first_column(m)
        weighted = sum((beta ** min(j, m - j) * v[j] for j in range(m)))
        if not all((x > 0 for x in v)):
            raise RuntimeError('Exact Frostman check failed (original line 66)')
        if not sum(v) == 1:
            raise RuntimeError('Exact Frostman check failed (original line 67)')
        if not weighted < 300:
            raise RuntimeError('Exact Frostman check failed (original line 68)')
        if m == 1:
            if not v == [1]:
                raise RuntimeError('Exact Frostman check failed (original line 69)')
        if m == 2:
            if not v == [F(3, 4), F(1, 4)]:
                raise RuntimeError('Exact Frostman check failed (original line 70)')
        cycles.append({'m': m, 'weighted_norm': str(weighted), 'unweighted_row_sum': '1'})
    check('finite beta-weighted Green controls', len(cycles) == 24, 'Exact Q arithmetic, m=1..24 including repeated neighbours.')
    with localcontext() as ctx:
        ctx.prec = 60
        lam = Decimal(3) + Decimal(2) * Decimal(2).sqrt()
        displays = {'alpha_beta': str((Decimal(29) / 5).ln() / lam.ln()), 'gamma': str(lam.ln() / Decimal(7).ln()), 'p_star': str(Decimal(7).ln() / lam.ln())}
    record = {'arithmetic': 'Exact integers/Fraction for decisions; Decimal exponents display only', 'checks': checks, 'finite_cycles': cycles, 'decimal_display_only': displays, 'scope': 'Finite constant/Green controls only; not the nonlinear theorem.'}
    return record

TARGET = Path(__file__).resolve().parents[3] / 'record/history/2026/paired_phase_20261006/transversality_full_original.md'

def main():
    result = run()
    print(json.dumps(result,indent=2))

if __name__ == '__main__':
    main()
