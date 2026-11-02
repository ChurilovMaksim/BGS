#!/usr/bin/env python3
"""Wave 46, task 1: L1 single-cycle lemma checks.

Ring R/p^f = (Z/p^f)[sqrt(2)]: element (a,b) = a + b*sqrt(2).
beta = 17 + 12*sqrt(2) (norm 1). Trace(a,b) = 2a, conj(a,b) = (a,-b).
Cycle of C: t_k = Tr(C * beta^k). Dihedral orbit of C:
  { beta^r * C, beta^r * conj(C) : r }.
L1-naive: multiset M(C) determines the dihedral orbit.
"""
import sys
from collections import defaultdict

def add(x, y, m): return ((x[0]+y[0]) % m, (x[1]+y[1]) % m)
def mul(x, y, m): return ((x[0]*y[0]+2*x[1]*y[1]) % m, (x[0]*y[1]+x[1]*y[0]) % m)
def conj(x, m): return (x[0], (-x[1]) % m)
def tr(x, m): return (2*x[0]) % m
def pw(x, e, m):
    r = (1 % m, 0)
    while e:
        if e & 1: r = mul(r, x, m)
        x = mul(x, x, m); e >>= 1
    return r

def order(beta, m, cap=10000):
    x = (1 % m, 0); 
    for k in range(1, cap+1):
        x = mul(x, beta, m)
        if x == (1 % m, 0): return k
    return None

def cycle_multiset(C, beta, T, m):
    x = C; vals = []
    for _ in range(T):
        vals.append(tr(x, m)); x = mul(x, beta, m)
    return tuple(sorted(vals))

def dihedral_orbit(C, beta, T, m):
    out = set(); x = C; xc = conj(C, m); y = xc
    # beta^r * C and beta^r * conj(C)
    bC = C; bCc = xc
    for _ in range(T):
        out.add(bC); out.add(bCc)
        bC = mul(bC, beta, m); bCc = mul(bCc, beta, m)
    return out

def check_mod_p(p):
    m = p; beta = (17 % p, 12 % p)
    T = order(beta, m)
    qr = any((k*k) % p == 2 for k in range(p))
    groups = defaultdict(list)
    for a in range(p):
        for b in range(p):
            C = (a, b)
            groups[cycle_multiset(C, beta, T, m)].append(C)
    viol = []
    for M, cs in groups.items():
        orb = dihedral_orbit(cs[0], beta, T, m)
        for C in cs:
            if C not in orb: viol.append((M, cs[0], C))
    return dict(p=p, split=qr, T=T, p_div_T=(T % p == 0),
                nparams=p*p, ngroups=len(groups), nviol=len(viol),
                viol=viol[:5])

def main():
    print("=== mod-p fiber check (beta = 17+12sqrt2) ===")
    for p in [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
        r = check_mod_p(p)
        print(f"p={p} split={r['split']} T={r['T']} p|T={r['p_div_T']} "
              f"params={r['nparams']} groups={r['ngroups']} violations={r['nviol']}")
        for M, c0, c in r['viol'][:3]:
            print(f"   VIOL: multiset={M} rep={c0} outsider={c}")
    print()
    print("=== mod-25 scaling example (m=30) ===")
    m = 25; beta = (17, 12)
    T = order(beta, m); print("ord beta mod 25 =", T)
    C1 = (0, 1); C2 = (1, 2)
    M1 = cycle_multiset(C1, beta, T, m); M2 = cycle_multiset(C2, beta, T, m)
    print("M(sqrt2) == M(1+2sqrt2):", M1 == M2)
    print("M =", M1)
    orb = dihedral_orbit(C1, beta, T, m)
    print("1+2sqrt2 in dihedral orbit of sqrt2:", C2 in orb)
    # scaling check: 21 * M1 == M1 ?
    print("21*M == M:", tuple(sorted((21*v) % 25 for v in M1)) == M1)
    # full stabilizer of M1 in (Z/25)^x
    stab = [lam for lam in range(25) if __import__('math').gcd(lam, 25) == 1
            and tuple(sorted((lam*v) % 25 for v in M1)) == M1]
    print("Stab(M) in (Z/25)^x =", stab)
    # cycle identity t2[k] = 21 * t1[k-10]
    def cyc(C):
        x = C; out = []
        for _ in range(T): out.append(tr(x, m)); x = mul(x, beta, m)
        return out
    t1, t2 = cyc(C1), cyc(C2)
    print("t2[k] == 21*t1[k-10] for all k:",
          all(t2[k] == (21*t1[(k-10) % T]) % 25 for k in range(T)))
    # 21*beta^5*sqrt2 == 1+2sqrt2 ?
    print("21*beta^5*sqrt2 mod 25 =", mul((21, 0), mul(pw(beta, 5, m), C1, m), m))

def check_mod_pf(p, f):
    m = p**f; beta = (17 % m, 12 % m)
    T = order(beta, m)
    units = [u for u in range(m) if __import__('math').gcd(u, m) == 1]
    groups = defaultdict(list)
    for a in range(m):
        for b in range(m):
            C = (a, b)
            groups[cycle_multiset(C, beta, T, m)].append(C)
    nviol = 0; nscal = 0; unexpl = []
    for M, cs in groups.items():
        c0 = cs[0]; orb = dihedral_orbit(c0, beta, T, m)
        # scaling closure of the orbit
        scal = set()
        for lam in units:
            for o in orb: scal.add(mul((lam, 0), o, m))
        for C in cs:
            if C not in orb:
                nviol += 1
                if C in scal: nscal += 1
                elif len(unexpl) < 3: unexpl.append((c0, C))
    return dict(p=p, f=f, m=m, T=T, vpT=(T % p == 0),
                nparams=m*m, ngroups=len(groups), nviol=nviol,
                nscal=nscal, unexpl=unexpl)

def main2():
    print("=== mod-p^f fiber check (f>=2: failure regime?) ===")
    for p, f in [(5, 2), (7, 2), (11, 2), (5, 3), (13, 2)]:
        r = check_mod_pf(p, f)
        print(f"p^{f}={r['m']} T={r['T']} p|T={r['vpT']} params={r['nparams']} "
              f"groups={r['ngroups']} violations={r['nviol']} "
              f"scaling-explained={r['nscal']} unexplained={r['nviol']-r['nscal']}")
        for c0, c in r['unexpl']:
            print(f"   UNEXPLAINED: rep={c0} outsider={c}")

if __name__ == "__main__":
    main(); print(); main2()
