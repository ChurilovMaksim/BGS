"""Wave 36, task 5: sigma-structure test at m=18 (exact slice) and m=30
(exact fiber-closed slice).

Setup (waves 20/34/35 conventions). Fix_m vectors are m-periodic
recurrence sequences y_{i+2} = 6 y_{i+1} - y_i mod q per prime-power
component q || D_m. Two vectors share the joint global multiset iff
sorted(y) = sorted(y'), iff some permutation sigma of Z/m has
y'_i = y_{sigma(i)} for all i (a "matching").
t = gcd(m,4) = 2 here; classes are even/odd positions.

Definitions tested (stated exactly, since the task wording admits
several readings):
- sigma is EXACTLY AFFINE if sigma(i) = u*i + c (mod m), gcd(u,m)=1.
- sigma is CLASS-AFFINE ("affine up to class permutation") if for
  some affine a and class-preserving rho, sigma = a o rho. This
  holds iff sigma maps each class O_r onto a single class
  O_{u*r+c} (class-preserving with affine class map); for t=2
  affine class maps are exactly D_2 = {id, swap}. Class-affine
  matching existence for a pair is equivalent to per-class
  multiset equality under id or swap, i.e. to JBL existence.
Tests per slice:
 (a) exact all-pairs count of pairs with NO class-affine matching
     (JBL failures) via per-point even/odd signature groups.
 (b) pairs with an EXACTLY AFFINE matching: base-vs-others, plus
     exact all-pairs count via affine-orbit incidences (PA/PB maps).
 (c) literal per-sigma question on base-vs-other pairs: is EVERY
     matching class-affine? For t=2, with x = #{i even: sigma(i)
     even}, achievable x range is [sum lo_v, sum hi_v] over values
     v (contingency intervals); all matchings class-affine iff
     that interval is exactly {0} or {|E|}. Non-class-affine
     matchings are exhibited explicitly where they exist.
Slices (fiber-closed: mates preserve component multisets, hence
preserve the fixed zero/constant components):
- m=18: mod-32 constant 0, mod-49 = 0, mod-39601 = 0, varying
  ker(25) x ker(38809) (wave-35 constructions) = 970,225 points.
- m=30: all components 0 except ker(625) x ker(841) = 525,625
  points (kernels by brute force, asserted size = q).
Within a slice, global values are injective in the varying pair
values, so fibers = groups by sorted pair multiset, and matching
is componentwise pair matching. Repository untouched, no Lean.
"""
import numpy as np
from collections import Counter


def kernel_mod_np(m, mod):
    a, b = np.meshgrid(np.arange(mod), np.arange(mod), indexing="ij")
    a = a.ravel().astype(np.int64)
    b = b.ravel().astype(np.int64)
    seqs = [a, b]
    for _ in range(m):
        seqs.append((6 * seqs[-1] - seqs[-2]) % mod)
    ok = (seqs[m] == a) & (seqs[m + 1] == b)
    out = np.stack([s[ok] for s in seqs[:m]], axis=1)
    assert len(out) == mod, (m, mod, len(out))
    return out.astype(np.int32)


def alpha_powers(m, mod):
    X = [1 % mod, 3 % mod]
    Y = [0, 2 % mod]
    for _ in range(2, m):
        x0, y0 = X[-1], Y[-1]
        X.append((3 * x0 + 4 * y0) % mod)
        Y.append((2 * x0 + 3 * y0) % mod)
    return np.array(X[:m], dtype=np.int64), np.array(Y[:m], dtype=np.int64)


def kernel_mod_38809(m):
    p = 197
    q = p * p
    X, Y = alpha_powers(m, q)
    x, y = np.meshgrid(np.arange(p, dtype=np.int64),
                       np.arange(p, dtype=np.int64), indexing="ij")
    x = x.ravel()
    y = y.ravel()
    seqs = (2 * (x[:, None] * (X % p)[None, :] +
                 2 * y[:, None] * (Y % p)[None, :])) % p
    seqs = (seqs * p).astype(np.int32)
    assert len(seqs) == q
    assert len(np.unique(seqs, axis=0)) == q
    return seqs


def row_index_map(K):
    """dict row-bytes -> row index for kernel K (n, m)."""
    d = {}
    for i, row in enumerate(K):
        d[row.tobytes()] = i
    return d


def analyze(m, K1, MOD2, K2, label):
    n1, n2 = len(K1), len(K2)
    N = n1 * n2
    E = m // 2
    print(f"== {label}: m={m} slice {n1}x{n2} = {N} points", flush=True)
    P = (K1[:, None, :].astype(np.int64) * MOD2 +
         K2[None, :, :].astype(np.int64)).astype(np.int32)
    flat = P.reshape(N, m)
    srt = np.sort(flat, axis=1)
    _, inv, counts = np.unique(srt, axis=0, return_inverse=True,
                               return_counts=True)
    order = np.argsort(inv, kind="stable")
    bounds = np.concatenate([[0], np.cumsum(counts)])
    nfib = len(counts)
    print(f"   fibers: {nfib}, multi-member: {int((counts >= 2).sum())}, "
          f"max fiber size: {int(counts.max())}", flush=True)

    # base-vs-other pairs
    base_list, other_list = [], []
    for fi in range(nfib):
        if counts[fi] < 2:
            continue
        idx = order[bounds[fi]:bounds[fi + 1]]
        base_list.append(np.full(len(idx) - 1, idx[0]))
        other_list.append(idx[1:])
    base_idx = np.concatenate(base_list)
    other_idx = np.concatenate(other_list)
    nb = len(base_idx)
    print(f"   base-vs-other pairs: {nb}", flush=True)
    b1, o1 = base_idx // n2, other_idx // n2
    b2, o2 = base_idx % n2, other_idx % n2

    # ---- (a) class-affine existence, exact all-pairs ----
    # NOTE: even/odd multisets must share ONE id space, else the swap
    # lookup mixes two unrelated id assignments (bug in first run).
    ev = np.sort(flat[:, 0::2], axis=1)
    od = np.sort(flat[:, 1::2], axis=1)
    evod = np.concatenate([ev, od], axis=0)
    _, uids = np.unique(evod, axis=0, return_inverse=True)
    ev_id, od_id = uids[:N], uids[N:]
    sig = ev_id.astype(np.int64) * N + od_id.astype(np.int64)
    fib_of_pt = np.empty(N, dtype=np.int64)
    for fi in range(nfib):
        fib_of_pt[order[bounds[fi]:bounds[fi + 1]]] = fi
    comp = fib_of_pt.astype(np.int64) * (N * N) + sig
    sidx = np.argsort(comp, kind="stable")
    scomp = comp[sidx]
    uniq_c, first = np.unique(scomp, return_index=True)
    cnts = np.diff(np.append(first, len(scomp)))
    # recover (fiber, sig) per group: sig = comp mod N^2
    NN = N * N
    gsig = uniq_c % NN
    gfib = uniq_c // NN
    d = {}
    for f_, s_, c_ in zip(gfib.tolist(), gsig.tolist(), cnts.tolist()):
        d[(f_, s_)] = c_
    # swap signature lookup needs (even, odd) ids: sig = e*N + o
    pairs_with = 0
    for (f_, s_), c_ in d.items():
        e_, o_ = divmod(s_, N)
        s2 = o_ * N + e_
        if s2 == s_:
            pairs_with += c_ * (c_ - 1) // 2
        elif s2 > s_:
            pairs_with += c_ * d.get((f_, s2), 0)
    total_pairs = int((counts * (counts - 1) // 2).sum())
    print(f"   (a) all pairs: {total_pairs}, with class-affine matching: "
          f"{pairs_with}, WITHOUT: {total_pairs - pairs_with}", flush=True)

    # ---- (b) exactly-affine matching ----
    units = [u for u in range(m) if np.gcd(u, m) == 1]
    d1, d2 = row_index_map(K1), row_index_map(K2)
    PA, PB = [], []
    for u in units:
        for c in range(m):
            perm = [(u * j + c) % m for j in range(m)]
            pa = np.array([d1.get(K1[i, perm].tobytes(), -1)
                           for i in range(n1)], dtype=np.int64)
            pb = np.array([d2.get(K2[i, perm].tobytes(), -1)
                           for i in range(n2)], dtype=np.int64)
            PA.append(pa)
            PB.append(pb)
    print(f"   affine maps: {len(PA)}", flush=True)
    aff_bo = np.zeros(nb, dtype=bool)
    for pa, pb in zip(PA, PB):
        aff_bo |= (pa[b1] == o1) & (pb[b2] == o2)
    print(f"   (b) base-vs-other pairs with exactly-affine matching: "
          f"{int(aff_bo.sum())} / {nb} "
          f"(without: {int((~aff_bo).sum())})", flush=True)
    # direct verification of a few claimed affine pairs
    _units = [u for u in range(m) if np.gcd(u, m) == 1]
    _checked = 0
    for _k in range(nb):
        if not aff_bo[_k]:
            continue
        _bi, _oi = int(base_idx[_k]), int(other_idx[_k])
        _found = False
        for _u in _units:
            for _c in range(m):
                _perm = [(_u * j + _c) % m for j in range(m)]
                if (flat[_oi] == flat[_bi][_perm]).all():
                    _found = True
                    break
            if _found:
                break
        assert _found, f"affine claim failed direct check, pair {_k}"
        _checked += 1
        if _checked >= 5:
            break
    print(f"   (b) direct verification passed for {_checked} pairs",
          flush=True)
    # exact all-pairs affine count via incidences
    i1_all = np.repeat(np.arange(n1), n2)
    i2_all = np.tile(np.arange(n2), n1)
    pt_idx = np.arange(N, dtype=np.int64)
    keys = []
    for pa, pb in zip(PA, PB):
        p1 = pa[i1_all]
        p2 = pb[i2_all]
        valid = (p1 >= 0) & (p2 >= 0)
        pidx = np.where(valid, p1 * n2 + p2, -1)
        good = valid & (pidx != pt_idx)
        if good.any():
            lo = np.minimum(pt_idx[good], pidx[good])
            hi = np.maximum(pt_idx[good], pidx[good])
            keys.append(lo * N + hi)
    if keys:
        allk = np.concatenate(keys)
        print(f"   (b) affine incidences: {len(allk)}", flush=True)
        if len(allk) <= 150_000_000:
            aff_pairs = len(np.unique(allk))
            print(f"   (b) exact all-pairs with affine matching: {aff_pairs} "
                  f"/ {total_pairs}", flush=True)
        else:
            print("   (b) exact all-pairs skipped: too many incidences",
                  flush=True)
    # first base-other pair without affine matching (explicit example)
    ex = None
    if (~aff_bo).any():
        j = int(np.where(~aff_bo)[0][0])
        ex = (int(base_idx[j]), int(other_idx[j]),
              flat[int(base_idx[j])].tolist(),
              flat[int(other_idx[j])].tolist())
        print(f"   (b) EXAMPLE pair without affine matching: base pt "
              f"{ex[0]} other pt {ex[1]}", flush=True)
        print(f"       base = {ex[2]}", flush=True)
        print(f"       other= {ex[3]}", flush=True)
    return dict(N=N, nfib=nfib, nb=nb, total_pairs=total_pairs,
                pairs_with=pairs_with, aff_bo=int(aff_bo.sum()),
                example=ex, flat=flat, base_idx=base_idx,
                other_idx=other_idx, b1=b1, o1=o1, b2=b2, o2=o2)


def test_c(m, res, label):
    """(c) literal per-sigma question on base-vs-other pairs."""
    flat, base_idx, other_idx = res["flat"], res["base_idx"], res["other_idx"]
    E = m // 2
    nb = len(base_idx)
    all_aff = 0
    some_nonaff = 0
    no_class_aff = 0
    first_nonaff = None
    for k in range(nb):
        o = flat[other_idx[k]]
        b = flat[base_idx[k]]
        do = {}
        for idx, v in enumerate(o.tolist()):
            kk = (v, idx & 1)
            do[kk] = do.get(kk, 0) + 1
        db = {}
        for idx, v in enumerate(b.tolist()):
            kk = (v, idx & 1)
            db[kk] = db.get(kk, 0) + 1
        lo = hi = 0
        for v in set(o.tolist()):
            a0 = do.get((v, 0), 0)
            a1 = do.get((v, 1), 0)
            b0 = db.get((v, 0), 0)
            n = a0 + a1
            lo += max(0, a0 + b0 - n)
            hi += min(a0, b0)
        if lo == hi and lo in (0, E):
            all_aff += 1
        else:
            some_nonaff += 1
            if lo == hi:
                no_class_aff += 1
            if first_nonaff is None:
                first_nonaff = (int(base_idx[k]), int(other_idx[k]),
                                b.tolist(), o.tolist(), lo, hi)
    print(f"   (c) base-vs-other pairs: all matchings class-affine: "
          f"{all_aff}, some non-class-affine matching: {some_nonaff}, "
          f"no class-affine matching at all: {no_class_aff}", flush=True)
    if first_nonaff is not None:
        bi, oi, bseq, oseq, lo, hi = first_nonaff
        print(f"   (c) EXAMPLE pair with non-class-affine matching: base pt "
              f"{bi} other pt {oi}, achievable x-range [{lo}, {hi}] "
              f"(E={E})", flush=True)
        print(f"       base = {bseq}", flush=True)
        print(f"       other= {oseq}", flush=True)
        # construct explicit non-class-affine matching: start from an
        # id-type class-affine matching if one exists, else swap-type,
        # then swap images of two same-value positions of opposite parity
        res["c_example"] = first_nonaff
    return first_nonaff


def construct_sigma(m, bseq, oseq):
    """Given base/other sequences with a class-affine matching, build
    an explicit non-class-affine matching by swapping images of two
    same-value positions of opposite parity. Returns sigma list or None.
    Assumes an id-type class-affine matching exists (checked by caller
    via per-class multisets); falls back to swap-type."""
    E = m // 2
    # candidate class-affine matchings: id (E->E, O->O) or swap (E->O, O->E)
    for pi in ("id", "swap"):
        # greedy per-value assignment respecting pi
        from collections import defaultdict
        pool = defaultdict(list)
        for j, v in enumerate(bseq):
            pool[v].append(j)
        sigma = [None] * m
        ok = True
        # positions of other grouped by value; assign within pi-classes
        used = set()
        for i, v in enumerate(oseq):
            want_par = (i & 1) if pi == "id" else (1 - (i & 1))
            cand = [j for j in pool[v] if (j & 1) == want_par
                    and j not in used]
            if not cand:
                ok = False
                break
            sigma[i] = cand[0]
            used.add(cand[0])
        if not ok:
            continue
        # find same value at both parities in other
        pos_by_val = defaultdict(list)
        for i, v in enumerate(oseq):
            pos_by_val[v].append(i)
        for v, ps in pos_by_val.items():
            ev = [i for i in ps if i % 2 == 0]
            od = [i for i in ps if i % 2 == 1]
            if ev and od:
                i1, i2 = ev[0], od[0]
                # swap images; check it breaks class-affineness:
                s2 = list(sigma)
                s2[i1], s2[i2] = s2[i2], s2[i1]
                # class-affine iff all even -> one parity and all odd -> other
                ev_imgs = {s2[i] & 1 for i in range(m) if i % 2 == 0}
                od_imgs = {s2[i] & 1 for i in range(m) if i % 2 == 1}
                if len(ev_imgs) == 2 or len(od_imgs) == 2:
                    # verify matching property
                    assert all(oseq[i] == bseq[s2[i]] for i in range(m))
                    assert sorted(s2) == list(range(m))
                    return s2, pi
        return None
    return None


if __name__ == "__main__":
    m = 18
    k25 = kernel_mod_np(m, 25)
    k38809 = kernel_mod_38809(m)
    print(f"kernel 25: {len(k25)}, kernel 38809: {len(k38809)}", flush=True)
    r18 = analyze(m, k25, 38809, k38809, "m=18 slice")
    ex18 = test_c(m, r18, "m=18")
    if ex18 is not None:
        bi, oi, bseq, oseq, lo, hi = ex18
        got = construct_sigma(m, bseq, oseq)
        print(f"   (c) explicit non-class-affine sigma: {got[0] if got else None}"
              f" (from {got[1] if got else '-'} -type base matching)",
              flush=True)
    m = 30
    k625 = kernel_mod_np(m, 625)
    k841 = kernel_mod_np(m, 841)
    print(f"kernel 625: {len(k625)}, kernel 841: {len(k841)}", flush=True)
    r30 = analyze(m, k625, 841, k841, "m=30 slice")
    ex30 = test_c(m, r30, "m=30")
    if ex30 is not None:
        bi, oi, bseq, oseq, lo, hi = ex30
        got = construct_sigma(m, bseq, oseq)
        print(f"   (c) explicit non-class-affine sigma: {got[0] if got else None}"
              f" (from {got[1] if got else '-'} -type base matching)",
              flush=True)
    print("DONE", flush=True)
