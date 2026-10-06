from fractions import Fraction as F

def mv(M, v):
    return (M[0][0] * v[0] + M[0][1] * v[1], M[1][0] * v[0] + M[1][1] * v[1])

def mm(A, B):
    return tuple((tuple((sum((A[i][k] * B[k][j] for k in range(2))) for j in range(2))) for i in range(2)))

def plus(v, w):
    return (v[0] + w[0], v[1] + w[1])

def neg(v):
    return (-v[0], -v[1])

def mod(v):
    return tuple((x % 1 for x in v))

def om(v, w):
    return v[0] * w[1] - v[1] * w[0]

def integral(x):
    return x.denominator == 1

def run():
    S = ((3, 4), (2, 3))
    A = ((1, 0), (0, 1))
    rows = []
    checks = 0
    for m in range(1, 65):
        A = mm(S, A)
        B = ((A[0][0] - 1, A[0][1]), (A[1][0], A[1][1] - 1))
        det = B[0][0] * B[1][1] - B[0][1] * B[1][0]
        Bi = ((F(B[1][1], det), F(-B[0][1], det)), (F(-B[1][0], det), F(B[0][0], det)))
        pulse = mv(Bi, (0, 1))
        D = -det
        if not pulse[1] == F(-1, 2):
            raise RuntimeError('Exact check failed at original arithmetic line 19')
        if not pulse[0] == F(A[0][1], D):
            raise RuntimeError('Exact check failed at original arithmetic line 20')

        def Q(z):
            n = mv(B, z)
            if not all((integral(x) for x in n)):
                raise RuntimeError('Exact check failed at original arithmetic line 22')
            return (om(z, n) - n[0] * n[1]) / 2

        def bil(z, d):
            return om(z, mv(B, d))
        if not Q(pulse) == pulse[0] / 2:
            raise RuntimeError('Exact check failed at original arithmetic line 25')
        pos = set()
        z = pulse
        for j in range(m):
            pos.add(mod(z))
            z = mv(S, z)
        if not mod(z) == mod(pulse):
            raise RuntimeError('Exact check failed at original arithmetic line 28')
        nega = {mod(neg(z)) for z in pos}
        union = pos | nega
        if not (len(union) <= 2 * m and (0, 0) not in union):
            raise RuntimeError('Exact check failed at original arithmetic line 30')
        for N in (1, 3, 5, 7, 9, 15, 21, 35):
            if not all((mod((N * z[0], N * z[1])) != (0, 0) for z in union)):
                raise RuntimeError('Exact check failed at original arithmetic line 32')
        for nq in range(-3, 4):
            for np in range(-3, 4):
                z = mv(Bi, (nq, np))
                Sz = mv(S, z)
                exact = -3 * nq * nq - 8 * nq * np - 6 * np * np
                if not Q(Sz) - Q(z) == exact:
                    raise RuntimeError('Exact check failed at original arithmetic line 37')
                candidate = -3 * nq * nq - 10 * nq * np - 6 * np * np
                if not integral(Q(Sz) - Q(z) - candidate):
                    raise RuntimeError('Exact check failed at original arithmetic line 39')
                if not integral(Q(plus(z, pulse)) - Q(z) - Q(pulse) - bil(z, pulse)):
                    raise RuntimeError('Exact check failed at original arithmetic line 40')
                if not integral(Q(neg(pulse)) + bil(plus(z, pulse), neg(pulse)) + Q(pulse) + bil(z, pulse)):
                    raise RuntimeError('Exact check failed at original arithmetic line 41')
                if not integral(bil(Sz, mv(S, pulse)) - bil(z, pulse)):
                    raise RuntimeError('Exact check failed at original arithmetic line 42')
                if not integral(bil(z, pulse) - z[0]):
                    raise RuntimeError('Exact check failed at original arithmetic line 43')
                checks += 6
        rows.append({'m': m, 'D': D, 'positive_count': len(pos), 'negative_overlap': len(pos & nega), 'union_count': len(union), 'pulse_q': str(pulse[0])})
    return {'arithmetic': 'exact integer/Fraction; independent implementation', 'scope': 'm=1..64; 49 lifted label samples per m; all cyclic/negative pulse orbit points; odd-N test list is finite', 'identities_checked': checks, 'rows': rows, 'editorial_note': 'Real-lift Q(Sz)-Q(z) has mixed coefficient -8; candidate -10 remains congruent modulo integers.', 'nonclaims': 'Not exhaustive over all label pairs, not analytic or asymptotic verification.'}
