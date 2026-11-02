"""Wave 29, task 2: verify the mod-9 no-split lemma and validate the
fiber/orbit code against the known m=12, q=81 split.

Component vectors = ker(H_m mod q), H_m = 6I - C - C^T, i.e. sequences
with y_{i+1} = 6*y_i - y_{i-1} (mod q), m-periodic. Fibers = classes by
sorted multiset; Gamma = dihedral perms of positions. A fiber "splits"
if it contains >= 2 Gamma-orbits. Exact integer arithmetic.
"""
import itertools


def ker_mod(m, q):
    """Enumerate ker(H_m mod q) via (y0, y1) seeds + recurrence."""
    out = []
    for y0, y1 in itertools.product(range(q), repeat=2):
        y = [y0, y1]
        for _ in range(m):
            y.append((6 * y[-1] - y[-2]) % q)
        if y[m] == y0 and y[m + 1] == y1:
            out.append(tuple(y[:m]))
    return out


def dihedral_orbits(vecs, m):
    """Partition vecs into Gamma-orbits (shifts + reflections)."""
    vset = set(vecs)
    seen = set()
    orbits = []
    for v in vecs:
        if v in seen:
            continue
        orb = set()
        for j in range(m):
            orb.add(tuple(v[(i + j) % m] for i in range(m)))
            orb.add(tuple(v[(j - i) % m] for i in range(m)))
        orb &= vset
        seen |= orb
        orbits.append(orb)
    return orbits


def check_no_split(m, q):
    vecs = ker_mod(m, q)
    by_mult = {}
    for v in vecs:
        by_mult.setdefault(tuple(sorted(v)), []).append(v)
    splits = []
    for mult, vs in by_mult.items():
        orbs = dihedral_orbits(vs, m)
        if len(orbs) > 1:
            splits.append((mult, len(vs), len(orbs)))
    return len(vecs), len(by_mult), splits


def main():
    # --- Part 1: mod-9 component for 4|m, 3 not| m: expect 9 vectors,
    # 3 fibers, each a single orbit (no splits) ---
    for m in (4, 8, 20, 28, 32, 40):
        assert m % 4 == 0 and m % 3 != 0
        n, n_fib, splits = check_no_split(m, 9)
        print(f"m={m} q=9: |ker|={n} fibers={n_fib} splits={splits}")
        assert n == 9 and splits == []
    # --- Part 2: parametrization y = 3*Tr(B' beta^i), beta = 3+2sqrt2,
    # B' in R/3R; check set equality at m=8 ---
    def mul(p, r, mod):
        a, b = p
        c, d = r
        return ((a * c + 2 * b * d) % mod, (a * d + b * c) % mod)

    def pw(p, e, mod):
        r = (1, 0)
        for _ in range(e):
            r = mul(r, p, mod)
        return r

    beta9 = (3, 2)
    assert pw(beta9, 12, 9) == (1, 0)  # ord_9(beta) = 12
    assert pw(beta9, 6, 9) == (8, 0)   # beta^6 = -1 mod 9
    for m in (4, 8):
        got = set()
        for a, b in itertools.product(range(3), repeat=2):
            Bp = (a, b)
            seq = []
            for i in range(m):
                # Tr(3*B' * beta^i) mod 9, computed in R/9R
                B3 = (3 * a % 9, 3 * b % 9)
                t = mul(B3, pw(beta9, i, 9), 9)
                seq.append((2 * t[0]) % 9)
            got.add(tuple(seq))
        ker = set(ker_mod(m, 9))
        print(f"m={m} parametrization match: {got == ker} (|ker|={len(ker)})")
        assert got == ker
    # --- Part 3: validate fiber/orbit code at m=12, q=81: expect the
    # known split fiber (36 points, 3 orbits) ---
    n, n_fib, splits = check_no_split(12, 81)
    print(f"m=12 q=81: |ker|={n} fibers={n_fib} splits={splits}")
    assert n == 81
    assert any(sz == 36 and no == 3 for _, sz, no in splits)
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
