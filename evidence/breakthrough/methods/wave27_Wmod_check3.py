"""Wave 27, task 5, checks 3: gluing maps and kernel vectors.

For each failing pair (y, y'):
  - Gamma_q = {dihedral gamma : y' = gamma(y) mod q} for each q || D.
  - e_q = w' - gamma(w) for gamma in Gamma_q: check X e_q = 0 mod q
    (X = adj(H)), entry ranges, gcds, and whether e_q is 0 mod p.
  - Adjugate row of H_12, and ker(X mod p) dimensions for p | D.

Exact integers throughout. Repository untouched; no Lean build.
"""
import json
from collections import defaultdict
from math import gcd

M = 12
D = 1536796800
QS = [128, 81, 25, 49, 121]
PS = [2, 3, 5, 7, 11]


def Hvec(y):
    return [6 * y[i] - y[(i - 1) % M] - y[(i + 1) % M] for i in range(M)]


def dihedral_perms():
    """24 perms pi (as tuples) with (gamma w)[i] = w[pi[i]]."""
    perms = []
    for s in range(M):
        perms.append(tuple((i + s) % M for i in range(M)))
        perms.append(tuple((-i + s) % M for i in range(M)))
    return perms


PERMS = dihedral_perms()


def apply_perm(w, pi):
    return [w[pi[i]] for i in range(M)]


def adjugate_row():
    """First row x of adj(H): x * h = D * delta_0 (cyclic convolution),
    h = (6, -1, 0, ..., 0, -1). Solve via integer linear algebra over Q
    using fractions, then verify integrality."""
    from fractions import Fraction
    # Circulant system: for each shift s, sum_j x_j h_{s-j} = D delta_{s,0}.
    # h_t = 6 if t=0, -1 if t=+-1, else 0.
    # Build matrix A[s][j] = h_{s-j mod 12} and solve A x = D e_0.
    A = [[Fraction(0)] * M for _ in range(M)]
    for s in range(M):
        for j in range(M):
            t = (s - j) % M
            A[s][j] = Fraction(6 if t == 0 else (-1 if t in (1, M - 1) else 0))
    b = [Fraction(D if s == 0 else 0) for s in range(M)]
    # Gaussian elimination
    n = M
    Mx = [row[:] + [b[i]] for i, row in enumerate(A)]
    for col in range(n):
        piv = next(r for r in range(col, n) if Mx[r][col] != 0)
        Mx[col], Mx[piv] = Mx[piv], Mx[col]
        pv = Mx[col][col]
        Mx[col] = [v / pv for v in Mx[col]]
        for r in range(n):
            if r != col and Mx[r][col] != 0:
                f = Mx[r][col]
                Mx[r] = [a - f * bb for a, bb in zip(Mx[r], Mx[col])]
    x = [Mx[i][n] for i in range(n)]
    assert all(v.denominator == 1 for v in x), "adjugate row not integral!"
    return [int(v) for v in x]


def apply_X(w, x):
    """(X w)[i] = sum_j x_{i-j} w_j (circulant, first row x)."""
    return [sum(x[(i - j) % M] * w[j] for j in range(M))
            for i in range(M)]


def ker_dim_mod_p(x, p):
    """Dimension of ker(X mod p) over F_p, via rank of circulant matrix."""
    # Matrix rows: row i = (x_{i-j})_j. Rank over F_p by elimination.
    A = [[x[(i - j) % M] % p for j in range(M)] for i in range(M)]
    rank = 0
    row = 0
    for col in range(M):
        piv = None
        for r in range(row, M):
            if A[r][col] % p != 0:
                piv = r
                break
        if piv is None:
            continue
        A[row], A[piv] = A[piv], A[row]
        inv = pow(A[row][col], -1, p)
        A[row] = [(v * inv) % p for v in A[row]]
        for r in range(M):
            if r != row and A[r][col] % p != 0:
                f = A[r][col]
                A[r] = [(a - f * b) % p for a, b in zip(A[r], A[row])]
        row += 1
        rank += 1
    return M - rank


def main():
    x = adjugate_row()
    print(f"adjugate row x = {x}", flush=True)
    # verify: X w = y for a census rep, and H X = D I via convolution
    print(f"ker(X mod p) dims: "
          f"{ {p: ker_dim_mod_p(x, p) for p in PS} }", flush=True)

    with open("wave18_Pw_m12_census.json") as fh:
        cen = json.load(fh)
    fail_classes = []
    for g in cen["split_groups"]:
        if g["pw_ok"]:
            continue
        by_sw = defaultdict(list)
        for o in g["orbits"]:
            by_sw[tuple(o["sorted_w"])].append(o["rep"])
        for sw, rr in by_sw.items():
            if len(rr) >= 2:
                fail_classes.append(rr)
    assert len(fail_classes) == 152

    gamma_sizes = defaultdict(int)
    e_entry_max = 0
    e_gcd_vals = defaultdict(int)
    e_mod_p_zero = defaultdict(int)  # (p) -> # (pair,q,gamma) with e=0 mod p
    e_total = 0
    shown = 0
    for reps in fail_classes:
        y1, y2 = reps[0], reps[1]
        w1 = [v // D for v in Hvec(y1)]
        w2 = [v // D for v in Hvec(y2)]
        # sanity: y = X w
        assert apply_X(w1, x) == y1 and apply_X(w2, x) == y2
        for q in QS:
            gammas = [pi for pi in PERMS
                      if all(apply_perm(y1, pi)[i] % q == y2[i] % q
                             for i in range(M))]
            gamma_sizes[(q, len(gammas))] += 1
            for pi in gammas:
                gw = apply_perm(w1, pi)
                e = [w2[i] - gw[i] for i in range(M)]
                # check X e = 0 mod q (follows from y-gluing, verify)
                Xe = apply_X(e, x)
                assert all(v % q == 0 for v in Xe), "kernel check failed"
                e_entry_max = max(e_entry_max, max(abs(v) for v in e))
                g = 0
                for v in e:
                    g = gcd(g, v)
                e_gcd_vals[g] += 1
                e_total += 1
                for p in PS:
                    if all(v % p == 0 for v in e):
                        e_mod_p_zero[p] += 1
                if shown < 3:
                    print(f"  q={q} gamma={pi} e={e}", flush=True)
                    shown += 1
    print(f"gamma-set sizes (q, |Gamma_q|): counts = "
          f"{dict(gamma_sizes)}", flush=True)
    print(f"e entry max abs: {e_entry_max}; e gcd histogram: "
          f"{dict(sorted(e_gcd_vals.items()))}", flush=True)
    print(f"e = 0 mod p counts (of {e_total} (pair,q,gamma)): "
          f"{dict(e_mod_p_zero)}", flush=True)


if __name__ == "__main__":
    main()
