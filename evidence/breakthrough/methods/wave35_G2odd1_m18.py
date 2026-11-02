"""Wave 35, task 5: the t=2, a=b subcase at m=18 — first case with TWO
constraining odd primes (5 and 197).

Slice: mod-32 component constant, mod-49 and mod-199^2 components zero
(D_18 = 2^5*5^2*7^2*197^2*199^2; 49 and 39601 are non-constraining:
alpha^9+1 is a unit mod 49 and mod 199^2, so their class multisets
always coincide and Pi is always full there).
In this slice the global multiset condition is EXACTLY the pair
multiset condition on (mod-25, mod-38809) pairs, and the slice is
fiber-closed (mates of a slice point stay in the slice). So grouping
the 25*38809 = 970,225 slice points by sorted pair multiset gives
all fibers in the slice exactly. For each fiber pair, compute Pi_25
and Pi_38809 and check for a common pi: PC fails iff some pair has
Pi_25 = {id}-only and Pi_38809 = {swap}-only, or vice versa.
"""
import numpy as np
from collections import Counter


def kernel_mod_small(m, mod):
    out = []
    for a in range(mod):
        for b in range(mod):
            seq = [a, b]
            for _ in range(m):
                seq.append((6 * seq[-1] - seq[-2]) % mod)
            if seq[m] == a and seq[m + 1] == b:
                out.append(tuple(seq[:m]))
    return np.array(out, dtype=np.int32)


def alpha_powers(m, mod):
    """X_i, Y_i with alpha^i = X_i + Y_i*sqrt(2) mod `mod`."""
    X = [1 % mod, 3 % mod]
    Y = [0, 2 % mod]
    for _ in range(2, m):
        x0, y0 = X[-1], Y[-1]
        X.append((3 * x0 + 4 * y0) % mod)
        Y.append((2 * x0 + 3 * y0) % mod)
    # note: recurrence for (X,Y): alpha^{i+1} = (3+2s)(X_i+Y_i s)
    # = (3X_i+4Y_i) + (2X_i+3Y_i) s. Check X_2 = 17, Y_2 = 12.
    return np.array(X[:m], dtype=np.int64), np.array(Y[:m], dtype=np.int64)


def kernel_mod_38809(m):
    """Kernel mod 197^2: B = 197*C, C in R/197 (197 inert, v=1).
    Sequence values = 197 * Tr(C alpha^i) mod 38809."""
    p = 197
    q = p * p
    X, Y = alpha_powers(m, q)
    # Tr(C alpha^i) mod p, C = x + y sqrt2, x,y in Z/p
    x, y = np.meshgrid(np.arange(p, dtype=np.int64),
                       np.arange(p, dtype=np.int64), indexing="ij")
    x = x.ravel()
    y = y.ravel()
    # Tr(C alpha^i) = 2*(x*X_i + 2*y*Y_i) mod p; values mod q are p*that.
    seqs = (2 * (x[:, None] * (X % p)[None, :] +
                 2 * y[:, None] * (Y % p)[None, :])) % p
    seqs = (seqs * p).astype(np.int32)
    assert len(seqs) == q
    # checks: distinctness, alpha^18 == 1 mod 197, and direct
    # recurrence + 18-periodicity of every enumerated vector
    assert len(np.unique(seqs, axis=0)) == q, "kernel vectors not distinct"
    X18, Y18 = alpha_powers(m + 1, q)
    assert X18[m] % p == 1 and Y18[m] % p == 0, "alpha^18 != 1 mod 197"
    y18 = (6 * seqs[:, 17].astype(np.int64) -
           seqs[:, 16].astype(np.int64)) % q
    y19 = (6 * y18 - seqs[:, 17].astype(np.int64)) % q
    assert np.all(y18 == seqs[:, 0]) and np.all(y19 == seqs[:, 1]), \
        "periodicity fails"
    return seqs


def row_keys(arr):
    _, ids = np.unique(arr, axis=0, return_inverse=True)
    return ids


def main():
    m = 18
    k25 = kernel_mod_small(m, 25)
    k38809 = kernel_mod_38809(m)
    print(f"kernel 25: {len(k25)} (expect 25)")
    print(f"kernel 38809: {len(k38809)} (expect 38809)")
    # sanity: class coincidence at non-constraining components is by
    # theory (alpha^9+1 unit); here just confirm kernels look right:
    # every mod-25 vector's values and mod-38809 vector's values.
    # pair keys: (25, 38809, 18)
    pk = (k25[:, None, :].astype(np.int64) * 38809 +
          k38809[None, :, :].astype(np.int64)).astype(np.int32)
    pk_sorted = np.sort(pk, axis=2)
    flat = pk_sorted.reshape(-1, m)
    _, inv, counts = np.unique(flat, axis=0, return_inverse=True,
                               return_counts=True)
    order = np.argsort(inv, kind="stable")
    bounds = np.concatenate([[0], np.cumsum(counts)])
    print(f"slice points: {len(flat)}, fibers: {len(counts)}, "
          f"multi-member fibers: {int((counts >= 2).sum())}", flush=True)
    # class keys per kernel vector
    def class_keys(k, q):
        ke = row_keys(np.sort(k[:, 0::2] % q, axis=1))
        ko = row_keys(np.sort(k[:, 1::2] % q, axis=1))
        return ke, ko
    ke25, ko25 = class_keys(k25, 25)
    ke38, ko38 = class_keys(k38809, 38809)
    # pair arrays over flat point index = i25*38809 + i38
    n38 = len(k38809)
    base_list, other_list = [], []
    for fi in range(len(counts)):
        if counts[fi] < 2:
            continue
        idx = order[bounds[fi]:bounds[fi + 1]]
        base_list.append(np.full(len(idx) - 1, idx[0]))
        other_list.append(idx[1:])
    base_idx = np.concatenate(base_list)
    other_idx = np.concatenate(other_list)
    nb = len(base_idx)
    print(f"fiber pairs in slice: {nb}", flush=True)
    b25, o25 = base_idx // n38, other_idx // n38
    b38, o38 = base_idx % n38, other_idx % n38
    id25 = (ke25[o25] == ke25[b25]) & (ko25[o25] == ko25[b25])
    sw25 = (ke25[o25] == ko25[b25]) & (ko25[o25] == ke25[b25])
    id38 = (ke38[o38] == ke38[b38]) & (ko38[o38] == ko38[b38])
    sw38 = (ke38[o38] == ko38[b38]) & (ko38[o38] == ke38[b38])
    print(f"Pi_25: id={int(id25.sum())} swap={int(sw25.sum())} "
          f"both={int((id25 & sw25).sum())} "
          f"neither={int((~(id25 | sw25)).sum())}")
    print(f"Pi_38809: id={int(id38.sum())} swap={int(sw38.sum())} "
          f"both={int((id38 & sw38).sum())} "
          f"neither={int((~(id38 | sw38)).sum())}")
    fail = ((id25 & ~sw25) & (sw38 & ~id38)) | \
           ((sw25 & ~id25) & (id38 & ~sw38))
    print(f"COMMON-PI FAILURES (PC counterexamples): {int(fail.sum())}")
    bad = np.where(fail)[0][:5]
    for j in bad:
        print("FAIL pair: base point idx", int(base_idx[j]),
              "i25", int(b25[j]), "i38", int(b38[j]),
              "other idx", int(other_idx[j]),
              "i25", int(o25[j]), "i38", int(o38[j]))
        print("  k25 base:", k25[b25[j]].tolist())
        print("  k25 other:", k25[o25[j]].tolist())
        print("  k38809 base:", k38809[b38[j]].tolist())
        print("  k38809 other:", k38809[o38[j]].tolist())
    # pattern counts
    pat = Counter()
    for j in range(nb):
        pat[(bool(id25[j]), bool(sw25[j]), bool(id38[j]), bool(sw38[j]))] += 1
    print("patterns (id25, sw25, id38, sw38): count")
    for k, v in sorted(pat.items()):
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
