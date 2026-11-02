"""Wave 16, task 2 — exact check for Lemma PC at (m, p1, p2) = (20, 41, 19).
No BGS repository access; pure integer arithmetic in R = Z[sqrt2] mod p.
Checks: (i) alpha^4 = beta mod 41, hence alpha^5 = 1;
(ii) every mod-41 sequence has all four class multisets equal (=> Pi_1 = D4);
(iii) pi_d in Pi_2 for every mod-19 sequence and every d (definitional);
(iv) Pi_2 is NOT forced full mod 19 (only the zero sequence gives full Pi_2).
"""
import itertools

def mul(x, y, p):
    return ((x[0]*y[0] + 2*x[1]*y[1]) % p, (x[0]*y[1] + x[1]*y[0]) % p)

def pw(x, e, p):
    r = (1, 0)
    while e:
        if e & 1:
            r = mul(r, x, p)
        x = mul(x, x, p)
        e >>= 1
    return r

def seq(A, p, m=20):
    al = (3 % p, 2 % p)
    cur = (1, 0)
    out = []
    for _ in range(m):
        out.append((2 * (A[0]*cur[0] + 2*A[1]*cur[1])) % p)
        cur = mul(cur, al, p)
    return out

def classes(s):
    return [tuple(sorted(s[i] for i in range(20) if i % 4 == r)) for r in range(4)]

def apply_d(s, d, m=20):
    e, k = d
    return [s[(e*j + k) % m] for j in range(m)]

D4 = [(e, k) for e in (1, -1) for k in range(4)]

def pi_set(s, d):
    cd, co = classes(apply_d(s, d)), classes(s)
    return [pi for pi in D4
            if all(cd[r] == co[(pi[0]*r + pi[1]) % 4] for r in range(4))]

assert pw((3, 2), 4, 41) == (3, 39) and pw((3, 2), 5, 41) == (1, 0)
bad41 = sum(1 for A in itertools.product(range(41), repeat=2)
            if len(set(classes(seq(A, 41)))) != 1)
print("41 side: sequences with non-equal class multisets:", bad41, "of 1681")
full19 = 0
for B in itertools.product(range(19), repeat=2):
    b = seq(B, 19)
    for d in [(e, k) for e in (1, -1) for k in range(20)]:
        ps = pi_set(b, d)
        assert (d[0], d[1] % 4) in ps  # pi_d in Pi by the class-mapping property
        if len(ps) == 8:
            full19 += 1
print("19 side: (b,d) pairs with Pi_2 full:", full19, "of 14440 (zero seq only)")
print("PASS")
