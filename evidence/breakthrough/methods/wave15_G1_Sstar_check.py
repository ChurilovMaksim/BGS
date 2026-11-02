#!/usr/bin/env python3
"""Wave 15, task 1: S* check for G1 case (1,2) at f=3.

For (m,p) = (36,3) and (150,5): enumerate all A in R/p^3, group by global
multiset, and for each pair in a fibre find a shift/reflection transform
with A'' == A mod p^2; then S* = Tr(eta1) mod p where A'' = A(1+p^2 eta1).
Also compute low-groups of v=2 singletons for the base A and check the
dichotomy: S* != 0 forces every low-group size divisible by p.
"""
import sys
from collections import defaultdict

def make_ring(P):
    def add(x, y): return ((x[0]+y[0]) % P, (x[1]+y[1]) % P)
    def mul(x, y):
        return ((x[0]*y[0] + 2*x[1]*y[1]) % P, (x[0]*y[1] + x[1]*y[0]) % P)
    def conj(x): return (x[0], (-x[1]) % P)
    def tr(x): return (2*x[0]) % P
    def inv(x):
        # inverse in R/P for units (x not divisible by p); brute force via norm
        # N(x) = a^2 - 2b^2; inverse = conj(x)/N(x) if N(x) a unit mod P
        n = (x[0]*x[0] - 2*x[1]*x[1]) % P
        # invert n mod P (P = p^3, n coprime to p)
        ni = pow(n, -1, P)
        c = conj(x)
        return ((c[0]*ni) % P, (c[1]*ni) % P)
    return add, mul, conj, tr, inv

def run(m, p, max_pairs_per_group=50):
    P = p**3
    add, mul, conj, tr, inv = make_ring(P)
    alpha = (3 % P, 2 % P)
    # powers of alpha
    pw = [(1, 0)]
    for i in range(1, m):
        pw.append(mul(pw[-1], alpha))
    assert mul(pw[-1], alpha) == (1, 0), "alpha^m != 1"
    # L0 = order of alpha mod p
    Pp = p
    addp, mulp, conjp, trp, invp = make_ring(Pp)
    ap = (3 % p, 2 % p)
    x = (1, 0); L0 = 0
    while True:
        x = mulp(x, ap); L0 += 1
        if x == (1, 0): break
        assert L0 < 1000
    print(f"=== (m,p)=({m},{p}) P={P} L0={L0} k check ===")
    gamma = pw[L0 % m] if L0 < m else None
    # gamma = alpha^L0 mod P^3; compute directly
    g = (1, 0)
    for _ in range(L0):
        g = mul(g, alpha)
    gamma = g
    assert gamma[0] % p == 1 and gamma[1] % p == 0, f"gamma not 1 mod p: {gamma}"
    u = ((gamma[0]-1)//p % (p*p), gamma[1]//p % (p*p))  # u in R/p^2
    print(f"gamma={gamma} u={u} u0=({u[0]%p},{u[1]%p})")
    import math
    t = math.gcd(m, 4)
    gg = math.gcd(L0, t)  # g in wave12 notation (classes mod g)
    print(f"t={t} g={gg}")
    # enumerate A
    groups = defaultdict(list)
    seqs = {}
    for a in range(P):
        for b in range(P):
            A = (a, b)
            vals = tuple(sorted(tr(mul(A, pw[i])) for i in range(m)))
            groups[vals].append(A)
    print(f"A count={P*P} groups={len(groups)} "
          f"group sizes: min={min(len(v) for v in groups.values())} "
          f"max={max(len(v) for v in groups.values())}")
    # per group: D-relatedness check of g-class multisets + S* computation
    def class_multisets(A):
        # classes r mod gg: values Tr(A alpha^i) for i in Z/m, i%gg==r
        out = []
        for r in range(gg):
            out.append(tuple(sorted(tr(mul(A, pw[i])) for i in range(m) if i % gg == r)))
        return out
    def d_related(cm1, cm2):
        # D_g action: rotation r->r+b, reflection r->-r+b
        n = len(cm1)
        for b in range(n):
            if all(cm2[(r+b) % n] == cm1[r] for r in range(n)):
                return True
            if all(cm2[(-r+b) % n] == cm1[r] for r in range(n)):
                return True
        return False
    bad = 0
    sstar_nonzero = []
    sstar_zero = 0
    sstar_pairs = 0
    no_transform = []
    lowgroup_bad_config = []  # fibres where ALL low-groups have size % p == 0
    for vals, members in groups.items():
        base = members[0]
        cm0 = class_multisets(base)
        # v=2 low-groups for base (unit case only)
        lowgroups = None
        if not (base[0] % p == 0 and base[1] % p == 0):
            # H0 = <alpha^{t p^2}>; coset reps C_{r,z} = A alpha^r z, z in H0
            step = (t * p * p) % m
            H0 = []
            z = (1, 0)
            while True:
                H0.append(z)
                z = mul(z, pw[step])
                if z == (1, 0): break
            lg = defaultdict(list)
            for r in range(gg):
                for z in H0:
                    C = mul(mul(base, pw[r]), z)
                    # Tr(C u) mod p^2: C in R/P^3, u in R/p^2 -> product mod p^2
                    Cu = ((C[0]*u[0] + 2*C[1]*u[1]) % (p*p),
                          (C[0]*u[1] + C[1]*u[0]) % (p*p))
                    if (2*Cu[0]) % (p*p) == 0:  # v=2
                        low = tr(C) % (p*p)
                        top = (tr(C) // (p*p)) % p
                        lg[low].append(top)
            lowgroups = {k: sorted(v) for k, v in lg.items()}
            if lg and all(len(v) % p == 0 for v in lg.values()):
                lowgroup_bad_config.append((base, lowgroups))
        for A2 in members[1:]:
            if not d_related(cm0, class_multisets(A2)):
                bad += 1
            # S* via transform search (unit base only)
            if base[0] % p == 0 and base[1] % p == 0:
                continue
            found_set = set()
            for j in range(m):
                for refl in (False, True):
                    App = conj(A2) if refl else A2
                    App = mul(App, pw[j])
                    if (App[0]-base[0]) % (p*p) == 0 and (App[1]-base[1]) % (p*p) == 0:
                        D = mul(App, inv(base))
                        assert D[0] % (p*p) == 1 and D[1] % (p*p) == 0, f"D={D}"
                        eta1 = ((D[0]-1)//(p*p) % p, D[1]//(p*p) % p)
                        found_set.add((2*eta1[0]) % p)
            if len(found_set) > 1:
                print(f"!! S* inconsistent in fibre of {base}: {found_set}")
            found = found_set.pop() if found_set else None
            if found is None:
                no_transform.append((base, A2))
            else:
                sstar_pairs += 1
                if found != 0:
                    sstar_nonzero.append((base, A2, found, lowgroups))
                else:
                    sstar_zero += 1
            if sstar_pairs >= max_pairs_per_group * len(groups):
                pass
    print(f"D-bad pairs: {bad}")
    print(f"S* pairs computed: {sstar_pairs}, S*=0: {sstar_zero}, S*!=0: {len(sstar_nonzero)}")
    print(f"pairs with NO transform to A''==A mod p^2: {len(no_transform)}")
    print(f"fibres where ALL low-groups have size divisible by p: {len(lowgroup_bad_config)}")
    for base, A2, s, lg in sstar_nonzero[:10]:
        print(f"  S*={s} base={base} A2={A2} lowgroups={lg}")
    for base, lg in lowgroup_bad_config[:10]:
        print(f"  all-uniform lowgroups base={base} lowgroups={lg}")
    return groups

if __name__ == "__main__":
    import sys
    m = int(sys.argv[1]) if len(sys.argv) > 1 else 36
    p = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    run(m, p)
