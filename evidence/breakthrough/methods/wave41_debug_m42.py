"""Debug one 'ii+iii' group at m=42 (25,169): what connects its orbits?
Distinguishes: J-edges, partial negations, genuine scalings; and for
each connecting map, whether block0 is preserved or swapped, and
whether parameters are pure-sqrt2.
"""
import sys
sys.path.insert(0, ".")
from wave41_LemmaU_sweep import (build_component, enc_pair,
                                 classify_group, allowed_lambdas)
from collections import deque

m, pa, fa, pb, fb = 42, 5, 1, 13, 1
A = build_component(pa, fa, m)
B = build_component(pb, fb, m)
(moda, Csa, idxa, seqsa, rota, conja, nega) = A
(modb, Csb, idxb, seqsb, rotb, conjb, negb) = B
na, nb = len(Csa), len(Csb)
u = m // 2
lam_a = allowed_lambdas(moda, pa)
lam_b = allowed_lambdas(modb, pb)
print("lam_a:", lam_a, "lam_b:", lam_b)

groups = {}
for ia, sa in enumerate(seqsa):
    sa_t = seqsa[nega[ia]]
    for ib, sb in enumerate(seqsb):
        sb_t = seqsb[negb[ib]]
        b0 = sorted(enc_pair(x, y) for x, y in zip(sa, sb))
        b1 = sorted(enc_pair(x, y) for x, y in zip(sa_t, sb_t))
        key = b"".join(sorted(b0 + b1))
        b0b = b"".join(b0)
        b1b = b"".join(b1)
        bp = (b0b, b1b) if b0b <= b1b else (b1b, b0b)
        pt = ia * nb + ib
        g = groups.get(key)
        if g is None:
            groups[key] = [bp, [pt]]
        else:
            g[1].append(pt)
            assert g[0] == bp, "conflict!"

# find first ii+iii group and dissect it
for key, (bp, plist) in groups.items():
    t, det = classify_group(set(plist), na, nb, A, B, lam_a, lam_b)
    if t != "ii+iii":
        continue
    print(f"=== ii+iii group size={len(plist)} det={det}")
    pts = [(divmod(q, nb)) for q in plist]
    print("points (C^a, C^b):")
    for (ia, ib) in pts:
        print("  ", Csa[ia], Csb[ib],
              "pure_a:", Csa[ia][0] == 0, "pure_b:", Csb[ib][0] == 0)
    # block0 of first point, as pairs
    ia0, ib0 = pts[0]
    b0_0 = sorted(zip(seqsa[ia0], seqsb[ib0]))
    print("block0(first):", b0_0)
    # D-orbits
    S = set(plist)

    def moves(pt):
        ia, ib = divmod(pt, nb)
        yield rota[ia] * nb + rotb[ib]
        yield conja[ia] * nb + conjb[ib]
        yield nega[ia] * nb + negb[ib]

    orbit_id = {}
    orbits = []
    for pt in plist:
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
                    orbit_id[r] = oid
                    dq.append(r)
        orbits.append(orb)
    print(f"D-orbits: {len(orbits)}")
    for i, orb in enumerate(orbits):
        print(f"  orbit {i} size {len(orb)}:",
              [(Csa[divmod(q, nb)[0]], Csb[divmod(q, nb)[1]]) for q in orb])
    # edges: for each point, J images and scaling images in group
    for pt in plist:
        ia, ib = divmod(pt, nb)
        o = orbit_id[pt]
        for name, q2 in (("J_a", conja[ia] * nb + ib),
                         ("J_b", ia * nb + conjb[ib])):
            if q2 in S and orbit_id[q2] != o:
                ja, jb = divmod(q2, nb)
                # block0 of q2 vs block0 of pt
                b0_q = sorted(zip(seqsa[ja], seqsb[jb]))
                b0_p = sorted(zip(seqsa[ia], seqsb[ib]))
                rel = "preserved" if b0_q == b0_p else (
                    "swapped" if b0_q == sorted([(-x % moda, -y % modb)
                                                 for x, y in b0_p])
                    else "OTHER")
                print(f"  edge {name}: {Csa[ia], Csb[ib]} -> "
                      f"{Csa[ja], Csb[jb]} orbit {o}->{orbit_id[q2]} "
                      f"block0 {rel}")
        for la in lam_a:
            for lb in lam_b:
                if la == 1 and lb == 1:
                    continue
                ca, cb = Csa[ia], Csb[ib]
                na_pt = (la * ca[0] % moda, la * ca[1] % moda)
                nb_pt = (lb * cb[0] % modb, lb * cb[1] % modb)
                if na_pt not in idxa or nb_pt not in idxb:
                    continue
                q2 = idxa[na_pt] * nb + idxb[nb_pt]
                if q2 in S and orbit_id[q2] != o:
                    ja, jb = divmod(q2, nb)
                    b0_q = sorted(zip(seqsa[ja], seqsb[jb]))
                    b0_p = sorted(zip(seqsa[ia], seqsb[ib]))
                    rel = "preserved" if b0_q == b0_p else (
                        "swapped" if b0_q == sorted([(-x % moda, -y % modb)
                                                     for x, y in b0_p])
                        else "OTHER")
                    print(f"  edge scaling({la},{lb}): "
                          f"{Csa[ia], Csb[ib]} -> {Csa[ja], Csb[jb]} "
                          f"orbit {o}->{orbit_id[q2]} block0 {rel} "
                          f"pure_a={ca[0] == 0} pure_b={cb[0] == 0}")
    break
