# Wave 14, task 2: Lemma PC for (m,p1,p2)=(8,3,17). Exact arithmetic.
# R/p elements (a,b) = a + b*sqrt2 mod p, alpha = 3 + 2*sqrt2, Tr = 2a.
# a_j = Tr(A1 alpha^j) mod 3, b_j = Tr(A2 alpha^j) mod 17, j in Z/8.
# d(j) = eps*j + k mod 8. Classes O_r = {r, r+4}, t = 4.
# v_r = a_r (a has period 4 mod 3); C_r = {b_r, b_{r+4}} = {w_r, -w_r} (alpha^4 = -1 mod 17).
# pi_d(r) = eps*r + k mod 4. Pi_i = {pi in D4 : class multisets of d_i(seq) = those of seq composed with pi}.
from collections import Counter

def mul(x, y, p): return ((x[0]*y[0] + 2*x[1]*y[1]) % p, (x[0]*y[1] + x[1]*y[0]) % p)
def seq(A, p):
    al = (3 % p, 2 % p); cur = (1, 0); out = []
    for _ in range(8):
        out.append((2 * mul(A, cur, p)[0]) % p); cur = mul(cur, al, p)
    return tuple(out)

D4 = [(e, k) for e in (1, -1) for k in range(4)]
def comp(p, q):  # p after q: (e_p*e_q, e_p*k_q + k_p) mod 4
    return (p[0]*q[0], (p[0]*q[1] + p[1]) % 4)
def inv(p): return (p[0], (-p[0]*p[1]) % 4)
def pi_of(eps, k): return (eps, k % 4)

def classes(s):  # tuple of sorted class multisets
    return tuple(tuple(sorted((s[r], s[r+4]))) for r in range(4))
def pi_set(s, ds):
    M, Md = classes(s), classes(ds)
    return [pi for pi in D4 if tuple(M[(pi[0]*r + pi[1]) % 4] for r in range(4)) == Md]
def stab_of_cls(M):
    return [pi for pi in D4 if tuple(M[(pi[0]*r + pi[1]) % 4] for r in range(4)) == M]

def vtype(A1):
    x, y = A1
    if x == 0 and y == 0: return "zero"
    if x == 0: return "x=0"
    if y == 0: return "y=0"
    if x == y: return "x=y"
    if (x + y) % 3 == 0: return "x=-y"
    return "generic"

A1s = [(a, b) for a in range(3) for b in range(3)]
A2s = [(a, b) for a in range(17) for b in range(17)]
S1 = {A: seq(A, 3) for A in A1s}
S2 = {A: seq(A, 17) for A in A2s}
Ds = [(e, k) for e in (1, -1) for k in range(8)]
def dseq(s, e, k): return tuple(s[(e*j + k) % 8] for j in range(8))

pres = bad = 0
prod_fail = 0
cnt = Counter()
examples = {}  # (vtype, delta in StabC?) -> example
for A1 in A1s:
    a = S1[A1]; va = tuple(a[r] for r in range(4)); Sv = stab_of_cls(classes(a))
    for A2 in A2s:
        b = S2[A2]; Cb = classes(b); Sc = stab_of_cls(Cb)
        pairs = tuple(sorted(zip(a, b)))
        for (e1, k1) in Ds:
            a2 = dseq(a, e1, k1); P1 = pi_set(a, a2); pi1 = pi_of(e1, k1)
            for (e2, k2) in Ds:
                b2 = dseq(b, e2, k2)
                if tuple(sorted(zip(a2, b2))) != pairs: continue
                pres += 1
                P2 = pi_set(b, b2)
                if not (set(P1) & set(P2)): bad += 1
                pi2 = pi_of(e2, k2)
                delta = comp(pi1, inv(pi2))  # pi1 o pi2^{-1}
                inC = delta in Sc
                # product Stab(v)*Stab(C): {comp(sv, sc)}
                inProd = any(comp(sv, sc) == delta for sv in Sv for sc in Sc)
                if not inProd: prod_fail += 1
                key = (vtype(A1), inC, inProd)
                cnt[key] += 1
                if (not inC) and key not in examples:
                    examples[key] = (A1, A2, (e1, k1), (e2, k2), delta, Sv, Sc, va, Cb)
print("preserved", pres, "bad", bad, "delta-not-in-Stab(v)Stab(C)", prod_fail)
for k in sorted(cnt): print(k, cnt[k])
for k, ex in examples.items():
    print("EXAMPLE", k, ex)
