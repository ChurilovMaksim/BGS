"""Wave 35, task 5: the t=2, a=b subcase at m=10 (exhaustive, per constant
mod-32 component).

D_10 = 32 * 29^2 * 41^2 = 32 * 841 * 1681. For each constant mod-32
component a in {0,8,16,24}, enumerate K_841 x K_1681 (1,413,721 global
points), group by sorted multiset, and for each fiber pair compute:
  - Pi_841, Pi_1681 and their intersection,
  - whether y' is in the dihedral orbit of y.
"""
import numpy as np
from collections import Counter


def kernel_mod_np(m, mod):
    a, b = np.meshgrid(np.arange(mod, dtype=np.int64),
                       np.arange(mod, dtype=np.int64), indexing="ij")
    a = a.ravel()
    b = b.ravel()
    seqs = [a, b]
    for _ in range(m):
        seqs.append((6 * seqs[-1] - seqs[-2]) % mod)
    ok = (seqs[m] == a) & (seqs[m + 1] == b)
    return np.stack([s[ok] for s in seqs[:m]], axis=1).astype(np.int32)


def crt_combine_np(A, mod_a, B, mod_b):
    """A: (n, m) mod mod_a; B: (k, m) mod mod_b -> (n*k, m) mod mod_a*mod_b."""
    A = A.astype(np.int64)
    B = B.astype(np.int64)
    inv = pow(int(mod_a), -1, int(mod_b))
    diff = (B[None, :, :] - A[:, None, :]) % mod_b
    t = (diff * inv) % mod_b
    out = (A[:, None, :] + mod_a * t).reshape(-1, A.shape[1])
    return out.astype(np.int32)


def class_counter(row, q, t, r, m):
    return Counter(int(row[i]) % q for i in range(m) if i % t == r)


def pi_set_np(y, yp, m, q, t=2):
    res = set()
    C = [class_counter(y, q, t, r, m) for r in range(t)]
    Cp = [class_counter(yp, q, t, r, m) for r in range(t)]
    if all(Cp[r] == C[r] for r in range(t)):
        res.add('id')
    if all(Cp[r] == C[1 - r] for r in range(t)):
        res.add('swap')
    return res


def dihedral_contains(y, yp, m):
    for eps in (1, -1):
        for k in range(m):
            if all(yp[i] == y[(eps * i + k) % m] for i in range(m)):
                return True
    return False


def main():
    m = 10
    t = 2
    k841 = kernel_mod_np(m, 841)
    k1681 = kernel_mod_np(m, 1681)
    print(f"kernel 841: {len(k841)} (expect 841)")
    print(f"kernel 1681: {len(k1681)} (expect 1681)")
    # component class-coincidence stats
    for q, k in ((841, k841), (1681, k1681)):
        eq = 0
        for v in k:
            ce = Counter(int(v[i]) % q for i in range(m) if i % 2 == 0)
            co = Counter(int(v[i]) % q for i in range(m) if i % 2 == 1)
            if ce == co:
                eq += 1
        print(f"mod {q}: M_E == M_O for {eq}/{len(k)} kernel vectors")
    # divisibility of component values
    for q, k, p in ((841, k841, 29), (1681, k1681, 41)):
        div = sum(1 for v in k if all(int(x) % p == 0 for x in v))
        print(f"mod {q}: {div}/{len(k)} kernel vectors all divisible by {p}")

    tot_pairs = 0
    dih = 0
    common_fail = 0
    pi_pat = Counter()
    for a in (0, 8, 16, 24):
        const = np.full((1, m), a, dtype=np.int32)
        pts = crt_combine_np(const, 32, k841, 841)
        pts = crt_combine_np(pts, 32 * 841, k1681, 1681)
        assert len(pts) == 841 * 1681
        srt = np.sort(pts, axis=1)
        _, inv, counts = np.unique(srt, axis=0, return_inverse=True,
                                   return_counts=True)
        order = np.argsort(inv, kind="stable")
        bounds = np.concatenate([[0], np.cumsum(counts)])
        inv_sorted = inv[order]
        nfib = 0
        for fi in range(len(counts)):
            if counts[fi] < 2:
                continue
            nfib += 1
            idx = order[bounds[fi]:bounds[fi + 1]]
            base = pts[idx[0]]
            for j in idx[1:]:
                other = pts[j]
                tot_pairs += 1
                p841 = pi_set_np(base, other, m, 841)
                p1681 = pi_set_np(base, other, m, 1681)
                common = p841 & p1681
                pi_pat[(tuple(sorted(p841)), tuple(sorted(p1681)),
                        tuple(sorted(common)))] += 1
                if not common:
                    common_fail += 1
                    if common_fail <= 3:
                        print("COMMON-PI FAILURE a=", a, "base=", base.tolist(),
                              "other=", other.tolist(), p841, p1681)
                if dihedral_contains(base, other, m):
                    dih += 1
        print(f"a={a}: fibers with >=2 members: {nfib}", flush=True)
    print(f"TOTAL a=b fiber pairs: {tot_pairs}")
    print(f"dihedrally related: {dih}")
    print(f"common-pi failures: {common_fail}")
    print("pi patterns (Pi841, Pi1681, common):")
    for k, v in sorted(pi_pat.items()):
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
