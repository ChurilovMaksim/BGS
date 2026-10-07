"""Bounded reviewed arithmetic. All executable work is inside run(root); outputs stay in scratch. Original assertions are explicit RuntimeError checks, including under python -O. Original __debug__ preconditions are obsolete after this conversion."""

def run(scratch_root):
    __file__ = str(scratch_root / 'nonprimitive_minimal_period_checks.py')
    from pathlib import Path
    import json, time, platform
    import numpy as np, sympy as sp
    BASE = Path(__file__).resolve().parent
    cases = json.loads((BASE / 'frozen/workspace/shared/bgs_intermediate_return_test/intermediate_return_control.json').read_text())['cases']

    def need(x, msg):
        if not x:
            raise RuntimeError(msg)

    def mp(A, k, p):
        B = np.eye(len(A), dtype=np.int64)
        while k:
            if k & 1:
                B = B @ A % p
            A = A @ A % p
            k //= 2
        return B

    def inv(A, p):
        C = np.c_[A.copy(), np.eye(len(A), dtype=np.int64)]
        for k in range(len(A)):
            at = next((x for x in range(k, len(A)) if C[x, k]))
            C[[at, k]] = C[[k, at]]
            C[k] = C[k] * pow(int(C[k, k]), -1, p) % p
            for r in range(len(A)):
                if r != k:
                    C[r] = (C[r] - int(C[r, k]) * C[k]) % p
        need(np.array_equal(C[:, :len(A)], np.eye(len(A), dtype=np.int64)), 'inverse')
        return C[:, len(A):]

    def W(m, q, a, b, p):
        C = np.zeros((m, m), dtype=np.int64)
        for x in range(m):
            C[x, (x + a) % m] = pow(q, b * (x + a * pow(2, -1, m)) % m, p)
        return C

    def rawcat(m, q, p):
        return np.array([[pow(q, -pow(8, -1, m) * (3 * x * x - 2 * x * y + 3 * y * y) % m, p) * pow(5, -1, p) % p for y in range(m)] for x in range(m)], dtype=np.int64)
    start = time.monotonic()
    rows = []
    for case in cases:
        j = case['j']
        p = case['prime']
        h = 5 ** j
        m = 25
        n = h * h * m
        L = 6 if j == 1 else 6 * 5 ** (j - 2)
        D = case['R'] // L
        R = case['R']
        qn = case['qn']
        qm = case['qm']
        M = rawcat(m, qm, p)
        S = np.array([[3, 4], [2, 3]], dtype=np.int64)
        ML = mp(M, L, p)
        I = np.eye(m, dtype=np.int64)
        for sign in [1, -1]:
            u = np.array([0, 5 * sign], dtype=np.int64)
            su = mp(S, L, n) @ u % n
            sum_ = mp(S, L * m, n) @ u % n
            b = tuple((int((int(su[k]) - int(u[k])) // h % m) for k in range(2)))
            z = pow(qn, -int(u[0] * su[1] - u[1] * su[0]) * pow(2, -1, n) % n, p)
            zm = pow(qn, -int(u[0] * sum_[1] - u[1] * sum_[0]) * pow(2, -1, n) % n, p)
            B = z * (W(m, qm, *b, p) @ ML % p) % p
            ranks = []
            for entry in case['residual_character_labels']:
                mu = entry['mu']
                X = pow(mu, -L, p) * B % p
                need(np.array_equal(mp(X, D, p), I), 'return exponent')
                Pi = np.zeros_like(X)
                weighted = np.zeros_like(X)
                power = I.copy()
                a = 1
                for t in range(D):
                    Pi = (Pi + power) % p
                    weighted = (weighted + (R - 2 * a - 2 * L * t) * power) % p
                    power = power @ X % p
                Pi = Pi * pow(D, -1, p) % p
                need(np.array_equal(Pi @ Pi % p, Pi), 'projector idempotence')
                rank = int(np.trace(Pi)) % p
                need(rank <= m, 'projector trace')
                ranks.append(rank)
                sharp = (inv((I - X + Pi) % p, p) - Pi) % p
                need(np.array_equal(weighted, (2 * R * sharp + D * (L - 2 * a) * Pi) % p), 'minimal-period weighted identity')
                if j == 1:
                    need(rank == (1 if entry['wild_order'] == 1 else 6), 'resonant rank')
                else:
                    need(rank == 0, 'j2 nonresonance')
                    need(pow(zm, 5, p) == 1 and zm != 1, 'scalar order5')
                    need(np.array_equal(mp(X, m, p), zm * I % p), 'j2 scalar return')
            rows.append({'j': j, 'u': [0, 5 * sign], 'L_used': L, 'D_used': D, 'cat_power_scalar': bool(np.array_equal(ML, int(ML[0, 0]) * I % p)), 'eigenvalue_one_ranks': ranks, 'weighted_identity_all_residual_characters': True})
    out = {'scope': 'Actual content-five modes using the declared correct periods, beyond the source script long-period j2 control.', 'rows': rows, 'seconds': time.monotonic() - start, 'result': 'All checks passed.'}
    (BASE / 'nonprimitive_minimal_period_checks.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({'result': out['result'], 'seconds': out['seconds']}))
