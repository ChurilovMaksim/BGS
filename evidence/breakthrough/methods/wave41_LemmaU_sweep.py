"""Wave 41, task 2: exact Lemma U test + collision-mechanism classifier.

For a pair of distinct-prime constraining components (pa,fa), (pb,fb)
at m = 2u, group all points (C^a, C^b) by the pair multiset
P = block0 U block1 and classify each P-group:

  (i)   single dihedral orbit  D = <rot, conj, neg>
  (ii)  D-orbits connected by partial conjugations J_a, J_b only
  (iii) D-orbits connected using integer scalings lam == +-1 mod p
        (scaling edges; J edges allowed too -> (ii+iii))
  UNKNOWN otherwise (candidate fourth kind / Lemma U conflict)

Conflicts (two distinct unordered block pairs in one P-group) are
reported separately: any conflict is an exact counterexample to
Lemma U itself.

Byte keys: trace values are mod p^f < 65536, so 2 bytes each.
"""

import sys
import math
from collections import deque


def rmul(x, y, mod):
    a, b = x
    c, d = y
    return ((a * c + 2 * b * d) % mod, (a * d + b * c) % mod)


def rpow(x, n, mod):
    r = (1 % mod, 0)
    while n:
        if n & 1:
            r = rmul(r, x, mod)
        x = rmul(x, x, mod)
        n >>= 1
    return r


def tr(x, mod):
    return (2 * x[0]) % mod


def build_component(p, f, m):
    mod = p ** f
    assert mod < 65536, "mod too large for 2-byte encoding"
    u = m // 2
    alpha = (3 % mod, 2 % mod)
    au = rpow(alpha, u, mod)
    assert au == (mod - 1, 0), ("not constraining", p, f, au)
    assert rpow(alpha, m, mod) == (1 % mod, 0)
    beta = rmul(alpha, alpha, mod)
    bpow = [(1 % mod, 0)]
    for _ in range(1, u):
        bpow.append(rmul(bpow[-1], beta, mod))
    assert rmul(bpow[-1], beta, mod) == (1 % mod, 0)
    Cs = [(a, b) for a in range(mod) for b in range(mod)]
    idx = {C: i for i, C in enumerate(Cs)}
    seqs = []
    for C in Cs:
        seqs.append(tuple(tr(rmul(C, bpow[k], mod), mod) for k in range(u)))
    rot = [idx[rmul(beta, C, mod)] for C in Cs]
    conj = [idx[(C[0], (-C[1]) % mod)] for C in Cs]
    neg = [idx[((-C[0]) % mod, (-C[1]) % mod)] for C in Cs]
    tau = [idx[rmul(au, C, mod)] for C in Cs]
    assert tau == neg, "tau != neg: not constraining?"
    sigs = set()
    for C in Cs:
        sigs.add((tr(C, mod), tr(rmul(alpha, C, mod), mod)))
    assert len(sigs) == len(Cs), "trace signature not injective"
    return mod, Cs, idx, seqs, rot, conj, neg


def enc_pair(x, y):
    return x.to_bytes(2, "big") + y.to_bytes(2, "big")


def period_of(seq, u):
    divs = sorted(d for d in range(1, u + 1) if u % d == 0)
    for d in divs:
        if all(seq[k] == seq[k % d] for k in range(u)):
            return d
    return u


def comp_flags(mod, seqs, u, p):
    """Per-sequence: period T, distinct-values?, negation-free? (H1-H3)."""
    out = []
    for s in seqs:
        T = period_of(s, u)
        vals = s[:T]
        distinct = len(set(vals)) == T
        vset = set(vals)
        negfree = all(((-v) % mod) not in vset for v in vset)
        out.append((T, distinct, negfree))
    return out


def h4_check(vals, T, mod):
    """Branch-free? vals = one period of trace values, distinct & negfree.

    Equation 34*t_j - sigma*t_j' = tau*t_j'' (sigma,tau in {+-1})
    must have only standard solutions sigma=tau=+1,
    {j',j''} = {j-1, j+1} mod T. Returns True iff branch-free.
    """
    vset = set(vals)
    idx = {v: j for j, v in enumerate(vals)}
    for j in range(T):
        tj = vals[j]
        for sigma in (1, -1):
            for jp in range(T):
                v = (34 * tj - sigma * vals[jp]) % mod
                if v in idx:
                    jpp = idx[v]
                    if not (sigma == 1 and {jp, jpp} == {(j - 1) % T, (j + 1) % T}):
                        return False
                if ((-v) % mod) in vset:
                    return False
    return True


def classify_group(pts, na, nb, A, B, lam_a, lam_b, ker_a, ker_b):
    """pts: set of combined ints ia*nb+ib. A/B: component tuples
    (mod, Cs, idx, seqs, rot, conj, neg). ker_a/ker_b: kernel elements
    (parameter tuples with all-zero trace sequence; {0} unless p=3).
    Returns (type, detail). Edge types between D-orbits:
      J = partial conjugation, S = genuine scaling (lam == +-1 mod p
          but not +-1 mod p^f on some coordinate),
      N = partial negation (lam == -1 exactly on one coordinate),
      K = kernel translation (p=3 beta-artifact).
    Type = first connecting edge-type subset in increasing size order
    (J, S, N, K, then pairs, triples, all)."""
    (moda, Csa, idxa, _sa, rota, conja, nega) = A
    (modb, Csb, idxb, _sb, rotb, conjb, negb) = B

    def moves(pt):
        ia, ib = divmod(pt, nb)
        yield rota[ia] * nb + rotb[ib]
        yield conja[ia] * nb + conjb[ib]
        yield nega[ia] * nb + negb[ib]

    # D-orbit partition
    orbit_id = {}
    orbits = []
    for pt in pts:
        if pt in orbit_id:
            continue
        oid = len(orbits)
        orb = []
        dq = deque([pt])
        orbit_id[pt] = oid
        while dq:
            q = dq.popleft()
            orb.append(q)
            for r in moves(q):
                if r not in orbit_id:
                    if r not in pts:
                        return ("BUG", "D-orbit escapes group")
                    orbit_id[r] = oid
                    dq.append(r)
        orbits.append(orb)
    if len(orbits) == 1:
        return ("i", {"n_orbits": 1, "size": len(pts)})

    edges = {"J": set(), "S": set(), "N": set(), "K": set()}
    for pt in pts:
        ia, ib = divmod(pt, nb)
        o = orbit_id[pt]
        ja = conja[ia] * nb + ib
        if ja in pts and orbit_id[ja] != o:
            edges["J"].add((o, orbit_id[ja]))
        jb = ia * nb + conjb[ib]
        if jb in pts and orbit_id[jb] != o:
            edges["J"].add((o, orbit_id[jb]))
        # kernel translations (per point: kernel need not commute with D)
        ca, cb = Csa[ia], Csb[ib]
        for ka in ker_a:
            if ka == (0, 0):
                continue
            t = ((ca[0] + ka[0]) % moda, (ca[1] + ka[1]) % moda)
            if t in idxa:
                q2 = idxa[t] * nb + ib
                if q2 in pts and orbit_id[q2] != o:
                    edges["K"].add((o, orbit_id[q2]))
        for kb in ker_b:
            if kb == (0, 0):
                continue
            t = ((cb[0] + kb[0]) % modb, (cb[1] + kb[1]) % modb)
            if t in idxb:
                q2 = ia * nb + idxb[t]
                if q2 in pts and orbit_id[q2] != o:
                    edges["K"].add((o, orbit_id[q2]))
    # scaling edges: one representative per D-orbit suffices (integer
    # scaling commutes with D-moves)
    for orb in orbits:
        rep = orb[0]
        ia, ib = divmod(rep, nb)
        ca, cb = Csa[ia], Csb[ib]
        for la in lam_a:
            for lb in lam_b:
                if la == 1 and lb == 1:
                    continue
                na_pt = (la * ca[0] % moda, la * ca[1] % moda)
                nb_pt = (lb * cb[0] % modb, lb * cb[1] % modb)
                if na_pt not in idxa or nb_pt not in idxb:
                    continue
                r2 = idxa[na_pt] * nb + idxb[nb_pt]
                if r2 in pts and orbit_id[r2] != orbit_id[rep]:
                    ga = (la == 1 or la == moda - 1)
                    gb = (lb == 1 or lb == modb - 1)
                    if not ga or not gb:
                        edges["S"].add((orbit_id[rep], orbit_id[r2]))
                    else:
                        edges["N"].add((orbit_id[rep], orbit_id[r2]))

    def connected(subset):
        parent = list(range(len(orbits)))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for t in subset:
            for (x, y) in edges[t]:
                rx, ry = find(x), find(y)
                if rx != ry:
                    parent[rx] = ry
        return len({find(i) for i in range(len(orbits))}) == 1

    order = [("J",), ("S",), ("N",), ("K",),
             ("J", "S"), ("J", "N"), ("J", "K"),
             ("S", "N"), ("S", "K"), ("N", "K"),
             ("J", "S", "N"), ("J", "S", "K"), ("J", "N", "K"),
             ("S", "N", "K"), ("J", "S", "N", "K")]
    names = {"J": "ii", "S": "iii", "N": "neg", "K": "ker"}
    for subset in order:
        if connected(subset):
            return ("+".join(names[t] for t in subset),
                    {"n_orbits": len(orbits), "size": len(pts)})
    return ("UNKNOWN", {"n_orbits": len(orbits), "size": len(pts)})


def allowed_lambdas(mod, p):
    return [lam for lam in range(mod)
            if lam % p in (1, p - 1) and _gcd(lam, mod) == 1]


def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def point_key(ia, ib, seqsa, seqsb, nega, negb):
    sa = seqsa[ia]
    sb = seqsb[ib]
    b0 = sorted(enc_pair(x, y) for x, y in zip(sa, sb))
    b1 = sorted(enc_pair(x, y) for x, y in
                zip(seqsa[nega[ia]], seqsb[negb[ib]]))
    key = b"".join(sorted(b0 + b1))
    b0b = b"".join(b0)
    b1b = b"".join(b1)
    bp = (b0b, b1b) if b0b <= b1b else (b1b, b0b)
    return key, bp


def d_orbit_size(pt, nb, rota, rotb, conja, conjb, nega, negb):
    seen = {pt}
    dq = deque([pt])
    while dq:
        q = dq.popleft()
        ia, ib = divmod(q, nb)
        for r in (rota[ia] * nb + rotb[ib],
                  conja[ia] * nb + conjb[ib],
                  nega[ia] * nb + negb[ib]):
            if r not in seen:
                seen.add(r)
                dq.append(r)
    return len(seen)


def run_case(m, pa, fa, pb, fb, rigid=False, rigid_sample=300):
    import random
    A = build_component(pa, fa, m)
    B = build_component(pb, fb, m)
    (moda, Csa, idxa, seqsa, rota, conja, nega) = A
    (modb, Csb, idxb, seqsb, rotb, conjb, negb) = B
    na, nb = len(Csa), len(Csb)
    u = m // 2
    lam_a = allowed_lambdas(moda, pa)
    lam_b = allowed_lambdas(modb, pb)
    ker_a = [Csa[i] for i, s in enumerate(seqsa) if all(v == 0 for v in s)]
    ker_b = [Csb[i] for i, s in enumerate(seqsb) if all(v == 0 for v in s)]
    print(f"  kernels: |ker_a|={len(ker_a)} |ker_b|={len(ker_b)}", flush=True)
    flags_a = flags_b = None
    if rigid:
        flags_a = comp_flags(moda, seqsa, u, pa)
        flags_b = comp_flags(modb, seqsb, u, pb)
    # Phase 1: group by key, store (blockpair, count, first point) only.
    groups = {}
    conflicts = []
    npts = 0
    h123_res = []
    h123_n = 0
    rng = random.Random(12345)
    for ia, sa in enumerate(seqsa):
        for ib in range(nb):
            key, bp = point_key(ia, ib, seqsa, seqsb, nega, negb)
            pt = ia * nb + ib
            npts += 1
            g = groups.get(key)
            if g is None:
                groups[key] = [bp, 1, pt]
            else:
                g[1] += 1
                if g[0] != bp and len(conflicts) < 5:
                    conflicts.append({"first_pt": g[2], "pt": pt})
            if rigid:
                Ta, da, na_ = flags_a[ia]
                Tb, db, nb_ = flags_b[ib]
                if Ta > 1 and Tb > 1 and da and db and na_ and nb_:
                    h123_n += 1
                    if len(h123_res) < 5000:
                        h123_res.append(pt)
                    elif rng.random() < 5000 / h123_n:
                        h123_res[rng.randrange(5000)] = pt
            if npts % 1000000 == 0:
                print(f"  ... phase1 {npts} points, {len(groups)} groups",
                      flush=True)
    print(f"CASE m={m} ({pa}^{2 * fa},{pb}^{2 * fb}) points={npts} "
          f"groups={len(groups)} conflicts={len(conflicts)}", flush=True)
    for c in conflicts:
        print("  CONFLICT:", c, flush=True)
    # Non-(i) groups: count != D-orbit size of first point.
    nontrivial = {}
    for key, (bp, cnt, first) in groups.items():
        osz = d_orbit_size(first, nb, rota, rotb, conja, conjb, nega, negb)
        if osz != cnt:
            nontrivial[key] = []
    print(f"  nontrivial groups: {len(nontrivial)}", flush=True)
    # Phase 2: collect points of nontrivial groups only.
    if nontrivial:
        for ia in range(na):
            for ib in range(nb):
                key, _bp = point_key(ia, ib, seqsa, seqsb, nega, negb)
                lst = nontrivial.get(key)
                if lst is not None:
                    lst.append(ia * nb + ib)
    hist = {}
    hist_pts = {}
    unknowns = []
    keytype = {}
    for key, (bp, cnt, first) in groups.items():
        if key in nontrivial:
            plist = nontrivial[key]
            t, det = classify_group(set(plist), na, nb, A, B, lam_a, lam_b,
                                    ker_a, ker_b)
            keytype[key] = t
            if t == "UNKNOWN":
                unknowns.append((plist, det))
        else:
            t = "i"
            keytype[key] = t
        hist[t] = hist.get(t, 0) + 1
        hist_pts[t] = hist_pts.get(t, 0) + cnt
    print(f"  group types: {hist}", flush=True)
    print(f"  points by type: {hist_pts}", flush=True)
    for plist, det in unknowns[:5]:
        pts = [(divmod(q, nb)) for q in plist]
        print(f"  UNKNOWN group size={len(plist)} det={det}", flush=True)
        print(f"    points(C^a,C^b)={[(Csa[a], Csb[b]) for a, b in pts[:20]]}",
              flush=True)
    # rigid verification on reservoir sample of H1-H3 points
    if rigid:
        print(f"  H1-H3 points: {h123_n} (reservoir {len(h123_res)})",
              flush=True)
        sample = rng.sample(h123_res, min(rigid_sample, len(h123_res))) \
            if h123_res else []
        h4cache_a = {}
        h4cache_b = {}

        def h4_a(ia):
            if ia not in h4cache_a:
                T, _, _ = flags_a[ia]
                h4cache_a[ia] = h4_check(seqsa[ia][:T], T, moda)
            return h4cache_a[ia]

        def h4_b(ib):
            if ib not in h4cache_b:
                T, _, _ = flags_b[ib]
                h4cache_b[ib] = h4_check(seqsb[ib][:T], T, modb)
            return h4cache_b[ib]

        n_rigid = 0
        viol = []
        g_hist = {}
        for pt in sample:
            ia, ib = divmod(pt, nb)
            if not (h4_a(ia) and h4_b(ib)):
                continue
            n_rigid += 1
            key, _bp = point_key(ia, ib, seqsa, seqsb, nega, negb)
            t = keytype.get(key, "?")
            Ta = flags_a[ia][0]
            Tb = flags_b[ib][0]
            g = math.gcd(Ta, Tb)
            g_hist[(t, g in (1, 2))] = g_hist.get((t, g in (1, 2)), 0) + 1
            # theorem predicts: (i), or (ii) only if g | 2
            ok = (t == "i") or (t == "ii" and g in (1, 2))
            if not ok:
                viol.append((pt, t, Ta, Tb, g))
        print(f"  rigid sample: {len(sample)} sampled, {n_rigid} pass H4",
              flush=True)
        print(f"  rigid group types (type, g|2): {g_hist}", flush=True)
        for v in viol[:10]:
            print(f"  RIGID VIOLATION: point={v}", flush=True)
    return groups


if __name__ == "__main__":
    # args: m pa fa pb fb [rigid]
    m = int(sys.argv[1])
    pa, fa, pb, fb = int(sys.argv[2]), int(sys.argv[3]), \
        int(sys.argv[4]), int(sys.argv[5])
    rigid = len(sys.argv) > 6 and sys.argv[6] == "rigid"
    run_case(m, pa, fa, pb, fb, rigid=rigid)
