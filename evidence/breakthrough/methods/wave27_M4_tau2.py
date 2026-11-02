"""Wave 27, task 1: is tau2=0 forced by mod-27 matching alone?
For collapsed pairs, compare mod-27 candidates vs level-81-matching candidates,
and record tau2 for each.
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
GAMMA_INV = conj(pw[4])
M = 108
seqs = {}
for a in range(81):
    for b in range(81):
        A = (a, b)
        seqs[A] = [tr(mul(A, pw[i])) for i in range(M)]
groups = {}
for A, y in seqs.items():
    groups.setdefault(tuple(sorted(y)), []).append(A)

def class_multis(y, m):
    return [tuple(sorted((y[i] % m) for i in range(M) if i % 4 == r)) for r in range(4)]
cm27 = {A: class_multis(seqs[A], 27) for A in seqs}
cm81 = {A: class_multis(seqs[A], 81) for A in seqs}

def collapsed(A):
    out = []
    for r in range(4):
        C = mul(A, pw[r])
        if C[1] % 3 == 0:
            out.append(r)
    return out

n27 = 0
n81 = 0
tau2_nonzero_27only = 0
tau2_nonzero_81 = 0
tau2_dist_27only = {}
examples = []
for key, As in groups.items():
    for A in As:
        if A[0] % 3 == 0 and A[1] % 3 == 0:
            continue
        if not collapsed(A):
            continue
        for Aprime in As:
            if Aprime == A:
                continue
            for eps in (1, -1):
                Ae = A if eps == 1 else conj(A)
                for s in range(108):
                    if mod3(mul(Ae, pw[s])) != mod3(Aprime):
                        continue
                    pi = [(r + s) % 4 for r in range(4)] if eps == 1 else [(-r - s) % 4 for r in range(4)]
                    if not all(cm27[Aprime][r] == cm27[A][pi[r]] for r in range(4)):
                        continue
                    n27 += 1
                    match81 = all(cm81[Aprime][r] == cm81[A][pi[r]] for r in range(4))
                    if match81:
                        n81 += 1
                    base = mul(Ae, pw[s])
                    ratio = mul(Aprime, inv(base))
                    eta = (((ratio[0]-1)//3) % 27, (ratio[1]//3) % 27)
                    eta0 = (eta[0] % 3, eta[1] % 3)
                    k = eta0[1]
                    gk = (1, 0)
                    for _ in range(k):
                        gk = mul(gk, GAMMA_INV)
                    one_p_eta = ((1 + 3*eta[0]) % 81, (3*eta[1]) % 81)
                    prod = mul(gk, one_p_eta)
                    etaN = (((prod[0]-1)//3) % 27, (prod[1]//3) % 27)
                    e1 = ((etaN[0]//3) % 3, (etaN[1]//3) % 3)
                    e2 = (((etaN[0] - 3*e1[0])//9) % 3, ((etaN[1] - 3*e1[1])//9) % 3)
                    if eps == -1:
                        e2 = conj(e2)
                    tau2 = (2*e2[0]) % 3
                    if not match81:
                        tau2_dist_27only[tau2] = tau2_dist_27only.get(tau2, 0) + 1
                        if tau2 != 0:
                            tau2_nonzero_27only += 1
                            if len(examples) < 3:
                                examples.append((A, Aprime, eps, s, tau2))
                    elif tau2 != 0:
                        tau2_nonzero_81 += 1
print("mod-27 candidates:", n27)
print("of which level-81 matching:", n81)
print("tau2 distribution among mod-27-only (non-81) candidates:", tau2_dist_27only)
print("tau2 != 0 among mod-27-only:", tau2_nonzero_27only)
print("tau2 != 0 among level-81 candidates:", tau2_nonzero_81)
print("examples:", examples)
