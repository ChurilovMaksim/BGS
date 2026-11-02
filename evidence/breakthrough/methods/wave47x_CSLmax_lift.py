"""Wave 47x, task C (CSL-max): lift-bits lemma + reduction ladder.

For each on-support split fiber at level 2m (upper), reduce its rep
mod Q_m, find the exact lower kernel point, and check:
 (a) y'_i == y[i mod p_red] (mod Q_m) for all i  [lift property];
 (b) p' == 4*p_red and drift-odd: delta_{i+p_red} - delta_i odd;
 (c) S'_r == 4*S_r + Q_m*Delta_r (mod Q') with Delta_r = sum_k delta_{4k+r};
 (d) Delta_r even for all r;
 (e) tau0'/k' vs tau0/k of the reduction;
 (f) reduction fiber is on-support split (or not).
Also prints the bits table for all on-support split fibers at each level.
Usage: python3 wave47x_CSLmax_lift.py [m_upper ...]  (default 64 128)
"""
import sys
sys.path.insert(0, ".")
import numpy as np
from collections import defaultdict
from wave16_d1a_targeted import Dm, torsion_data, group_ids
from wave36_2part import snf_kernel_i32, orbit_canon
from wave38_helpers import period_of


def fibers_at(m):
    j = m.bit_length() - 1
    q = 2 ** (2 * j + 3)
    D = Dm(m)
    Z, Qmod = torsion_data(m, D)
    pts = snf_kernel_i32(m, q)
    Qm = np.array([qq % q for qq in Qmod], dtype=np.int64)
    sup = ((2 * Qm[None, :] - pts.astype(np.int64) @ Z.astype(np.int64).T) % q == 0).all(axis=1)
    fib = group_ids(np.sort(pts, axis=1))
    ba, bb = orbit_canon(pts[:, :2].astype(np.int64), m, q)
    gam = group_ids(np.stack([ba, bb], axis=1))
    fib_orbits = defaultdict(set)
    for i in range(len(pts)):
        fib_orbits[int(fib[i])].add(int(gam[i]))
    split_ids = {f for f in fib_orbits if len(fib_orbits[f]) > 1}
    onsup = {int(fib[i]) for i in range(len(pts)) if sup[i]}
    out = []
    for f in sorted(split_ids & onsup):
        idx = [i for i in range(len(pts)) if int(fib[i]) == f]
        y = pts[idx[0]].astype(np.int64)
        p = period_of(y)
        o = len(fib_orbits[f])
        out.append(dict(fid=f, y=y, o=o, p=p))
    return dict(m=m, q=q, pts=pts, fib=fib, fib_orbits=fib_orbits,
                split_ids=split_ids, onsup=onsup, fibers=out)


def bits_of(y, p, q):
    """(tau0, k, S) for a sequence with 4|p; None if 4 does not divide p."""
    if p % 4 != 0:
        return None
    yper = y[:p]
    S = [int(np.sum(yper[r::4])) % q for r in range(4)]
    tau0 = (S[0] // (q // 32)) % 2
    k = ((S[1] - 3 * S[0]) // (q // 4)) % 2
    return tau0, k, S


def main():
    uppers = [int(a) for a in sys.argv[1:]] or [64, 128]
    for mu in uppers:
        ml = mu // 2
        lo = fibers_at(ml)
        up = fibers_at(mu)
        ql, qu = lo["q"], up["q"]
        assert qu == 4 * ql, (qu, ql)
        # exact-sequence lookup at lower level: bytes -> index
        low_by_seq = {}
        for i in range(len(lo["pts"])):
            low_by_seq[lo["pts"][i].astype(np.int64).tobytes()] = i
        print(f"===== upper m={mu} (Q'={qu}) over lower m={ml} (Q={ql}) =====")
        print(f"upper on-support split fibers: {len(up['fibers'])}")
        n_lift = n_drift = n_ident = n_deven = n_bitseq = 0
        n_red_split_onsup = 0
        bad = []
        for F in up["fibers"]:
            yp = F["y"]
            pp = F["p"]
            yred_full = (yp % ql).astype(np.int64)
            # lower rep: first ml entries must be a kernel point at lower level
            key = yred_full[:ml].tobytes()
            if key not in low_by_seq:
                bad.append((F["o"], pp, "reduction prefix not a lower point"))
                continue
            li = low_by_seq[key]
            y = lo["pts"][li].astype(np.int64)
            pred = period_of(y)
            fred = int(lo["fib"][li])
            red_split = fred in lo["split_ids"]
            red_onsup = fred in lo["onsup"]
            if red_split and red_onsup:
                n_red_split_onsup += 1
            # (a) lift property on the full length-2m vector
            yext = np.array([y[i % pred] for i in range(mu)], dtype=np.int64)
            if not np.array_equal(yred_full, yext):
                bad.append((F["o"], pp, f"lift property fails (pred={pred})"))
                continue
            n_lift += 1
            if pp != 4 * pred:
                bad.append((F["o"], pp, f"period not 4x: pred={pred}"))
                continue
            delta = ((yp - yext) // ql).astype(np.int64)
            if not np.all((yp - yext) % ql == 0):
                bad.append((F["o"], pp, "non-integer delta"))
                continue
            # (b) drift-odd
            if np.all(((delta[pred:] - delta[:-pred]) % 2) == 1):
                n_drift += 1
            else:
                bad.append((F["o"], pp, "drift not odd"))
            # (c),(d) lift identity + Delta parity (needs 4|pred for grouping,
            # but identity itself needs only the sum split)
            S_up = [int(np.sum(yp[:pp][r::4])) % qu for r in range(4)]
            yper = y[:pred]
            S_lo = [int(np.sum(yper[r::4])) % ql for r in range(4)] if pred % 4 == 0 else None
            Delta = [int(np.sum(delta[r::4])) for r in range(4)]
            # note: delta has length mu; class-sum index range is k < pp/4 = pred
            Delta = [int(np.sum(delta[:pp][r::4])) for r in range(4)]
            if S_lo is not None:
                ok_ident = all((S_up[r] - (4 * S_lo[r] + ql * Delta[r])) % qu == 0
                               for r in range(4))
            else:
                ok_ident = None
            if ok_ident:
                n_ident += 1
            elif ok_ident is False:
                bad.append((F["o"], pp, f"lift identity fails S_up={S_up} S_lo={S_lo} D={Delta}"))
            if all(d % 2 == 0 for d in Delta):
                n_deven += 1
            else:
                bad.append((F["o"], pp, f"Delta not even: {Delta}"))
            # (e) bits comparison (needs 4|pred)
            b_up = bits_of(yp, pp, qu)
            b_lo = bits_of(y, pred, ql)
            if b_up is not None and b_lo is not None:
                if b_up[0] == b_lo[0] and b_up[1] == b_lo[1]:
                    n_bitseq += 1
                else:
                    bad.append((F["o"], pp, f"bits differ up={b_up[:2]} lo={b_lo[:2]}"))
            print(f"  up o={F['o']} p={pp} -> red fid={fred} o={len(lo['fib_orbits'][fred])} "
                  f"p={pred} split={red_split} onsup={red_onsup} "
                  f"bits_up={b_up[:2] if b_up else None} bits_lo={b_lo[:2] if b_lo else None} "
                  f"Delta={Delta}")
        print(f"  SUMMARY m={mu}: lift={n_lift} drift_odd={n_drift} ident={n_ident} "
              f"Delta_even={n_deven} bits_equal={n_bitseq} "
              f"red_split_onsup={n_red_split_onsup}/{len(up['fibers'])} bad={len(bad)}")
        for b in bad[:20]:
            print("   BAD:", b)
        del lo, up
        import gc; gc.collect()


if __name__ == "__main__":
    main()
