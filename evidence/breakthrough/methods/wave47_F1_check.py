"""Wave 47, task 5: F1 check at 729 (m=36, 252) and at 6561 (m=108, e=3).

Kernel points at 3^(2e+2): C in 3^(e+1) R / 3^(2e+2) R, C' = C/3^(e+1)
in R/3^(e+1)R, K_i = 3^(e+1) * Tr(C' alpha^i) mod 3^(2e+2).
Top-digit move: C' -> C' - 3^e sqrt(2).
Theorem to check: if x % 3 != 0 and y % 3 != 0, then K(C') and
K(C'-3^e sqrt2) share the value-multiset (same fiber) but have
different norms mod 3^(e+1) (hence different Gamma-orbits).
"""
import sys
from collections import defaultdict


def alpha_powers(mod, n):
    """alpha^i = (x_i, y_i) mod `mod`, alpha = 3+2 sqrt2."""
    xs, ys = [1], [0]
    x, y = 1, 0
    for _ in range(n):
        x, y = (3 * x + 4 * y) % mod, (2 * x + 3 * y) % mod
        xs.append(x)
        ys.append(y)
    return xs, ys


def check(m, e):
    mod = 3 ** (e + 1)          # modulus for C'
    q = 3 ** (2 * e + 2)        # full 3-component
    step = 3 ** e               # top-digit step in C'
    xs, ys = alpha_powers(mod, m)
    # sequence for C'=(x,y): K_i = step3 * Tr(C' alpha^i) mod q, step3=3^(e+1)
    scale = 3 ** (e + 1)

    def seq(x, y):
        return tuple((scale * (2 * (x * xs[i] + 2 * y * ys[i]) % mod)) % q
                     for i in range(m))

    def fiber(x, y):
        return tuple(sorted(seq(x, y)))

    def norm(x, y):
        return (x * x - 2 * y * y) % mod

    bad_fiber = bad_norm = 0
    n = 0
    for x in range(mod):
        if x % 3 == 0:
            continue
        for y in range(mod):
            if y % 3 == 0:
                continue
            n += 1
            if fiber(x, y) != fiber(x, (y - step) % mod):
                bad_fiber += 1
            if norm(x, y) == norm(x, (y - step) % mod):
                bad_norm += 1
    print(f"m={m} e={e} q={q}: C' tested={n} fiber-mismatch={bad_fiber} "
          f"norm-collision={bad_norm}", flush=True)
    # fiber-0 members at e=2 (x=14): list k values in the fiber of (14,20)
    if e == 2:
        f0 = fiber(14, 20)
        members = [(x, y) for x in range(mod) for y in range(mod)
                   if fiber(x, y) == f0]
        print(f"  fiber of (14,20): {len(members)} points, "
              f"x=14 members y={sorted(y for x, y in members if x == 14)}",
              flush=True)
        # orbit check for the triple (14,20),(14,11),(14,2): dihedral?
        def dihedral_orbit(s):
            orb = set()
            for k in range(m):
                orb.add(tuple(s[(i + k) % m] for i in range(m)))
                orb.add(tuple(s[(-i + k) % m] for i in range(m)))
            return orb
        s20, s11, s2 = seq(14, 20), seq(14, 11), seq(14, 2)
        o20 = dihedral_orbit(s20)
        print(f"  triple in one fiber: {fiber(14,2)==f0 and fiber(14,11)==f0}; "
              f"s11 in orb(s20): {s11 in o20}; s2 in orb(s20): {s2 in o20}",
              flush=True)
    return bad_fiber, bad_norm


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("all", "36"):
        check(36, 2)
    if which in ("all", "252"):
        check(252, 2)
    if which in ("all", "108"):
        check(108, 3)
