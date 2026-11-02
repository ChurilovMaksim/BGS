"""Wave 22, task 3: exact checks for the JBL 2-part step.
R = Z[sqrt2], elements (x, y). Verifies: trace-kernel classification,
eps = alpha^(2^(a-2)) and kappa not in <alpha>, and the m=6 / m=3
counterexamples (identical vectors, not D-related)."""

def mul(a, b): return (a[0]*b[0] + 2*a[1]*b[1], a[0]*b[1] + a[1]*b[0])
def mod(a, m): return (a[0] % m, a[1] % m)
def tr(a): return 2*a[0]
def conj(a): return (a[0], -a[1])
ALPHA = (3, 2)

def pw(a, n, m):
    r = (1, 0)
    for _ in range(n): r = mod(mul(r, a), m)
    return r

for a in (2, 5, 7, 9):
    q = 2**a
    eps = (1, 2**(a-1)); kap = (1 + 2**(a-1), 0)
    assert all(tr(mod(mul(eps, (x, y)), q)) % q == tr((x, y)) % q
               and tr(mod(mul(kap, (x, y)), q)) % q == tr((x, y)) % q
               for x in range(q) for y in range(q))
    if a >= 5:
        assert pw(ALPHA, 2**(a-2), q) == eps
        orb = set(); r = (1, 0)
        while r not in orb:
            orb.add(r); r = mod(mul(r, ALPHA), q)
        assert kap not in orb and eps in orb and len(orb) == 2**(a-1)
print("trace-kernel / eps / kappa checks passed")

def check(m, D, A, Ap, t):
    beta = (1, 0)
    for _ in range(t): beta = mod(mul(beta, ALPHA), D)
    def seq(X):
        ys = []; cur = (1, 0)
        for _ in range(m):
            ys.append(tr(mod(mul(X, cur), D)) % D)
            cur = mod(mul(cur, ALPHA), D)
        return ys
    assert seq(A) == seq(Ap), (m, seq(A), seq(Ap))
    orb = set(); r = (1, 0); orbit = []
    while r not in orb:
        orb.add(r); orbit.append(r); r = mod(mul(r, beta), D)
    assert not any(mod(mul(s, A), D) == mod(Ap, D)
                   or mod(mul(s, conj(A)), D) == mod(Ap, D) for s in orbit)
    print(f"m={m}: identical vectors {seq(A)}, not D-related (|orbit|={len(orbit)})")

check(6, 39200, (35, 0), (19635, 0), 2)
check(3, 196, (7, 0), (7, 98), 1)
print("counterexamples verified")
