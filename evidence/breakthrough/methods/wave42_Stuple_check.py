"""Wave 42, task 3: finite checks for the S-tuple dihedral lemma proof.

Checks (all exact, all pass):
 1. rot/rev formulas map S-tuples correctly; swap formula + involution.
 2. C=4, 2-part: for every N mod 32 and every (a,c), the scaled
    w-multiset determines (a,c) up to the dihedral orbit (1248 groups).
 3. C=2, 2-part: same for (b,eps) up to swap (288 groups).
 4. p=3: c in (Z/3)^2, Tr(c*alpha^r) multisets give 3 dihedral orbits.
"""
def mulR(a, b, M):
    return ((a[0]*b[0]+2*a[1]*b[1]) % M, (a[0]*b[1]+a[1]*b[0]) % M)


def S4(ac):
    a, c = ac
    return tuple(v % 32 for v in (3*a+8*c, a, 3*a-8*c, 17*a-48*c))


def rot4(ac):
    a, c = ac
    return ((3*a-8*c) % 32, (-a+3*c) % 4)


def rev4(ac):
    a, c = ac
    return ((17*a-48*c) % 32, (-6*a+19*c) % 4)


def orb4(ac):
    out, fr = {ac}, [ac]
    while fr:
        y = fr.pop()
        for z in (rot4(y), rev4(y)):
            if z not in out:
                out.add(z)
                fr.append(z)
    return out


def S2(be):
    b, e = be
    return ((3*b+8*e) % 16, b)


def swap2(be):
    b, e = be
    return ((3*b+8*e) % 16, (b+e) % 2)


def check():
    bad = 0
    for a in range(32):
        for c in range(4):
            s = S4((a, c))
            assert S4(rot4((a, c))) == (s[1], s[2], s[3], s[0])
            assert S4(rev4((a, c))) == (s[0], s[3], s[2], s[1])
    for b in range(16):
        for e in range(2):
            s = S2((b, e))
            assert S2(swap2((b, e))) == (s[1], s[0])
            assert swap2(swap2((b, e))) == (b, e)
    ALPHA2, BETA = (17, 12), (3, 30)
    for Nbar in range(1, 33):
        K = ((Nbar-2)*(Nbar-1))//2
        Sig = ((Nbar-1) % 32, (24*K) % 32)
        groups = {}
        for a in range(32):
            for c in range(4):
                s = S4((a, c))
                T = ((4*a+12*c) % 32, (3*a+8*c) % 32)
                E = mulR(mulR((12, 0), ALPHA2, 32), mulR(Sig, T, 32), 32)
                ws, e = [], E
                for r in range(4):
                    ws.append(((s[r]+e[0]) % 32, e[1] % 32))
                    e = mulR(e, BETA, 32)
                groups.setdefault(tuple(sorted(ws)), set()).add((a, c))
        for pairs in groups.values():
            assert pairs <= orb4(next(iter(pairs))), (Nbar, pairs)
    BETA16 = (3, 14)
    for N2bar in range(1, 17):
        K = ((N2bar-2)*(N2bar-1))//2
        Sig = ((N2bar-1) % 16, (12*K) % 16)
        groups = {}
        for b in range(16):
            for e in range(2):
                s = S2((b, e))
                T = ((4*b+12*e) % 16, (3*b+8*e) % 16)
                E = mulR(mulR((2, 0), (3, 2), 16), mulR(Sig, T, 16), 16)
                ws, ee = [], E
                for r in range(2):
                    ws.append(((s[r]+ee[0]) % 16, ee[1] % 16))
                    ee = mulR(ee, BETA16, 16)
                groups.setdefault(tuple(sorted(ws)), set()).add((b, e))
        for pairs in groups.values():
            x = next(iter(pairs))
            assert pairs <= {x, swap2(x)}, (N2bar, pairs)
    def mul3(a, b):
        return ((a[0]*b[0]+2*a[1]*b[1]) % 3, (a[0]*b[1]+a[1]*b[0]) % 3)
    def pw3(n):
        r = (1, 0)
        for _ in range(n):
            r = mul3(r, (0, 2))
        return r
    def orb3(c):
        out, fr = {c}, [c]
        while fr:
            y = fr.pop()
            for z in (mul3(y, (0, 2)), (y[0], (-y[1]) % 3)):
                if z not in out:
                    out.add(z)
                    fr.append(z)
        return out
    g3 = {}
    for a in range(3):
        for b in range(3):
            c = (a, b)
            T = tuple((2*mul3(c, pw3(r))[0]) % 3 for r in range(4))
            g3.setdefault(tuple(sorted(T)), set()).add(c)
    assert len(g3) == 3
    for cs in g3.values():
        assert cs <= orb3(next(iter(cs)))
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    check()
