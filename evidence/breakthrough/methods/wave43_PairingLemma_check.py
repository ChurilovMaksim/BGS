# Independent verifier for the wave-43 Pairing Lemma counterexample.
# Recomputes everything from scratch (direct powers of alpha, no reuse
# of the search code): genuineness, per-class marginals/joints, pi-sets,
# global multisets. Run: python3 wave43_PairingLemma_check.py
ALPHA = (3, 2)

def mul(a, b, M):
    return ((a[0]*b[0] + 2*a[1]*b[1]) % M, (a[0]*b[1] + a[1]*b[0]) % M)

def pw(a, n, M):
    r = (1, 0)
    base = a
    while n:
        if n & 1:
            r = mul(r, base, M)
        base = mul(base, base, M)
        n >>= 1
    return r

def tr(a, M):
    return (2*a[0]) % M

def perms_of(t):
    return [tuple((eps*r + b) % t for r in range(t)) for eps in (1, -1) for b in range(t)]

m, q2, q = 32, 8192, 17
t, S = 4, 8
B2 = (0, 128)          # genuine mod 8192, class-0 pattern period 2
Bq = (1, 0)            # genuine mod 17, class-0 odd period 2
beta_q = pw(ALPHA, 4, q)
Bq_shift = mul(Bq, beta_q, q)
print("beta mod 17 =", beta_q, "(alpha^4 = -1 mod 17R: the odd sequence alternates)")

# (1) genuineness, direct: (alpha^m - 1) * B = 0
for M, B, name in [(q2, B2, "B2"), (q, Bq, "Bq"), (q, Bq_shift, "Bq'")]:
    d = pw(ALPHA, m, M)
    d = ((d[0]-1) % M, d[1])
    assert mul(d, B, M) == (0, 0), (name, "not genuine")
print("(1) genuineness: B2, Bq, Bq' all genuine: PASS")

def data(A2, Aq):
    s = []
    for i in range(m):
        s.append((tr(mul(A2, pw(ALPHA, i, q2), q2), q2),
                  tr(mul(Aq, pw(ALPHA, i, q), q), q)))
    marg, joint = [], []
    for r in range(t):
        cls = [s[r + t*k] for k in range(S)]
        marg.append((tuple(sorted(x[0] for x in cls)), tuple(sorted(x[1] for x in cls))))
        joint.append(tuple(sorted(cls)))
    return tuple(marg), tuple(joint), tuple(sorted(s))

m0, j0, g0 = data(B2, Bq)
m1, j1, g1 = data(B2, Bq_shift)
assert m0 == m1
print("(2) per-class marginals of A and A' exactly equal: PASS")
perms = perms_of(t)
marg_pis = [p for p in perms if all(m1[r] == m0[p[r]] for r in range(t))]
joint_pis = [p for p in perms if all(j1[r] == j0[p[r]] for r in range(t))]
print("(3) marginal pi-set:", marg_pis)
print("(4) joint pi-set:   ", joint_pis)
assert marg_pis and not joint_pis
assert not (set(marg_pis) & set(joint_pis))
print("(5) marg_pis ∩ joint_pis = EMPTY: Pairing Lemma refuted: PASS")
print("    joint class 0, A :", j0[0])
print("    joint class 0, A':", j1[0])
print("(6) global multisets equal:", g0 == g1,
      "-> this pair is NOT a JBL counterexample (JBL hypothesis is stronger)")
print("ALL CHECKS PASS")
