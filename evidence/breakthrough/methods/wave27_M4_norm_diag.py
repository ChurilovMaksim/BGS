"""Diagnose the norm vs delta contradiction at (108,3).
Find a group pair with N(A') != N(A) mod 81 and inspect its twist candidates.
"""
MOD = 81
def mul(x, y): return ((x[0]*y[0] + 2*x[1]*y[1]) % MOD, (x[0]*y[1] + x[1]*y[0]) % MOD)
def tr(x): return (2*x[0]) % MOD
def conj(x): return (x[0], (-x[1]) % MOD)
def norm(x): return (x[0]*x[0] - 2*x[1]*x[1]) % MOD
def inv(x):
    n = norm(x) % MOD
    ni = pow(n, -1, MOD)
    return ((x[0]*ni) % MOD, ((-x[1]*ni) % MOD))
def mod3(x): return (x[0] % 3, x[1] % 3)

ALPHA = (3, 2)
pw = [(1, 0)]
for _ in range(200):
    pw.append(mul(pw[-1], ALPHA))
M = 108
seqs = {}
for a in range(81):
    for b in range(81):
        A = (a, b)
        seqs[A] = [tr(mul(A, pw[i])) for i in range(M)]
groups = {}
for A, y in seqs.items():
    groups.setdefault(tuple(sorted(y)), []).append(A)

def class_multis_mod(y, m):
    return [tuple(sorted((y[i] % m) for i in range(M) if i % 4 == r)) for r in range(4)]
cm27 = {A: class_multis_mod(seqs[A], 27) for A in seqs}

found = 0
for key, As in groups.items():
    A0 = As[0]
    for A in As[1:]:
        if norm(A) != norm(A0):
            # valid candidates for pair (A0, A)? and (A, A0)?
            for (X, Y) in ((A0, A), (A, A0)):
                cands = []
                for eps in (1, -1):
                    Xe = X if eps == 1 else conj(X)
                    for s in range(108):
                        if mod3(mul(Xe, pw[s])) != mod3(Y):
                            continue
                        pi = [(r + s) % 4 for r in range(4)] if eps == 1 else [(-r - s) % 4 for r in range(4)]
                        if all(cm27[Y][r] == cm27[X][pi[r]] for r in range(4)):
                            cands.append((eps, s, pi))
                print("pair", X, "->", Y, " N:", norm(X), norm(Y),
                      " valid candidates:", len(cands),
                      " first:", cands[:3])
                if cands:
                    eps, s, pi = cands[0]
                    Xe = X if eps == 1 else conj(X)
                    base = mul(Xe, pw[s])
                    ratio = mul(Y, inv(base))
                    eta = (((ratio[0]-1)//3) % 27, (ratio[1]//3) % 27)
                    print("   eta (unnormalized):", eta,
                          " N(1+3eta) mod 81:", ((1+3*eta[0])**2 - 2*(3*eta[1])**2) % 81,
                          " N-ratio:", (norm(Y) * pow(norm(X), -1, 81)) % 81)
            found += 1
            break
    if found:
        break
