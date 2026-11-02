# Wave 44, task 1 — independent witness check for the GPL refutation.
# Recomputes from scratch with direct powers of alpha (no reuse of the
# census code): B2=(128,64) mod 8192, Bq=(8,8) vs (9,9)=-Bq mod 17.
ALPHA = (3, 2)
def mul(a, b, M):
    return ((a[0]*b[0] + 2*a[1]*b[1]) % M, (a[0]*b[1] + a[1]*b[0]) % M)
def pw(a, n, M):
    r = (1, 0); base = a
    while n:
        if n & 1: r = mul(r, base, M)
        base = mul(base, base, M); n >>= 1
    return r
def tr(a, M): return (2*a[0]) % M
m, q2, q, t = 32, 8192, 17, 4
perms = [tuple((eps*r + b) % t for r in range(t)) for eps in (1, -1) for b in range(t)]
def data(B2, Bq):
    s = [(tr(mul(B2, pw(ALPHA, i, q2), q2), q2),
          tr(mul(Bq, pw(ALPHA, i, q), q), q)) for i in range(m)]
    marg = tuple((tuple(sorted(x[0] for x in s[r::t])),
                  tuple(sorted(x[1] for x in s[r::t]))) for r in range(t))
    joint = tuple(tuple(sorted(s[r::t])) for r in range(t))
    return tuple(sorted(s)), marg, joint
g0, m0, j0 = data((128, 64), (8, 8))
g1, m1, j1 = data((128, 64), (9, 9))
assert g0 == g1, "globals differ!"
assert m0 == m1, "class-by-class marginals differ!"
assert j0 != j1, "joints equal — not a counterexample!"
pis = [p for p in perms if all(j1[r] == j0[p[r]] for r in range(t))]
print("globals equal: PASS; class-by-class marginals equal: PASS")
print("joints differ class-by-class: PASS; joint pi-set:", pis)
assert pis == [(3, 2, 1, 0)], pis
stab = [p for p in perms
        if tuple(m0[p[r]] for r in range(t)) == m0]
print("marginal-stabilizer contains (3,2,1,0):", (3, 2, 1, 0) in stab)
print("class-0 joints A :", j0[0])
print("class-0 joints A':", j1[0])
print("WITNESS VERIFIED")
