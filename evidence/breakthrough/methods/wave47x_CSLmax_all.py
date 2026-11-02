"""Wave 47x, task C (CSL-max): bits for ALL on-support fibers + lift classification.

Table A: for each level m, every on-support fiber with 4|p: bits (tau0,k);
  count how many have (0,1) vs anything else.
Table B: for each on-support SPLIT fiber at upper level 2m: reduction
  classification (pred, red onsup, red split, red o), lift identity and
  Delta parity when 4|pred, and the parity data for pred in {1,2}.
Usage: python3 wave47x_CSLmax_all.py [m ...]  (default 64 128; each m is
  an UPPER level, table A is printed for the lower level too on first use)
"""
import sys
sys.path.insert(0, ".")
import numpy as np
from collections import defaultdict
from wave16_d1a_targeted import Dm, torsion_data, group_ids
from wave36_2part import snf_kernel_i32, orbit_canon
from wave38_helpers import period_of


def level_data(m):
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
    # group on-support point indices by fiber id in one pass
    onsup_by_fib = defaultdict(list)
    for i in range(len(pts)):
        if sup[i]:
            onsup_by_fib[int(fib[i])].append(i)
    return dict(m=m, q=q, pts=pts, fib=fib, fib_orbits=fib_orbits,
                onsup_by_fib=onsup_by_fib)


def bits_of(y, p, q):
    if p % 4 != 0:
        return None
    yper = y[:p]
    S = [int(np.sum(yper[r::4])) % q for r in range(4)]
    tau0 = (S[0] // (q // 32)) % 2
    k = ((S[1] - 3 * S[0]) // (q // 4)) % 2
    return tau0, k, S


def table_A(L):
    m, q, pts = L["m"], L["q"], L["pts"]
    n = n_ok = 0
    others = []
    for f, idxs in L["onsup_by_fib"].items():
        y = pts[idxs[0]].astype(np.int64)
        p = period_of(y)
        if p % 4 != 0:
            continue
        n += 1
        b = bits_of(y, p, q)
        o = len(L["fib_orbits"][f])
        if b[0] == 0 and b[1] == 1:
            n_ok += 1
        else:
            others.append((f, o, p, b[:2]))
    print(f"Table A m={m}: on-support fibers with 4|p: {n}, bits (0,1): {n_ok}, "
          f"other: {len(others)}")
    for o_ in others[:20]:
        print("   OTHER:", o_)


def table_B(lo, up):
    ml, ql, mu, qu = lo["m"], lo["q"], up["m"], up["q"]
    assert qu == 4 * ql
    low_by_seq = {}
    for i in range(len(lo["pts"])):
        low_by_seq[lo["pts"][i].astype(np.int64).tobytes()] = i
    print(f"Table B upper m={mu} over lower m={ml}:")
    n_split = 0
    for f, idxs in up["onsup_by_fib"].items():
        o_up = len(up["fib_orbits"][f])
        if o_up <= 1:
            continue
        n_split += 1
        y = up["pts"][idxs[0]].astype(np.int64)
        pp = period_of(y)
        yred_full = (y % ql).astype(np.int64)
        li = low_by_seq.get(yred_full[:ml].tobytes())
        if li is None:
            print(f"  up fid={f} o={o_up} p={pp}: reduction NOT a lower point!")
            continue
        ylo = lo["pts"][li].astype(np.int64)
        pred = period_of(ylo)
        fred = int(lo["fib"][li])
        red_split = len(lo["fib_orbits"][fred]) > 1
        red_onsup = fred in lo["onsup_by_fib"]
        yext = np.array([ylo[i % pred] for i in range(mu)], dtype=np.int64)
        lift_ok = bool(np.array_equal(yred_full, yext))
        line = (f"  up fid={f} o={o_up} p={pp} -> red fid={fred} "
                f"o={len(lo['fib_orbits'][fred])} p={pred} "
                f"split={red_split} onsup={red_onsup} lift={lift_ok}")
        if lift_ok and pp == 4 * pred and pred % 4 == 0:
            delta = ((y - yext) // ql).astype(np.int64)
            Delta = [int(np.sum(delta[:pp][r::4])) for r in range(4)]
            S_up = [int(np.sum(y[:pp][r::4])) % qu for r in range(4)]
            S_lo = [int(np.sum(ylo[:pred][r::4])) % ql for r in range(4)]
            ident = all((S_up[r] - (4 * S_lo[r] + ql * Delta[r])) % qu == 0
                        for r in range(4))
            deven = all(d % 2 == 0 for d in Delta)
            b_up = bits_of(y, pp, qu)
            b_lo = bits_of(ylo, pred, ql)
            line += (f" ident={ident} Delta_even={deven} Delta={Delta} "
                     f"bits_up={b_up[:2]} bits_lo={b_lo[:2]}")
        elif lift_ok and pred == 2:
            delta = ((y - yext) // ql).astype(np.int64)
            # period-2 base: ylo = (a,b) repeating; a,b mod Q/16; u from b=3a+(Q/2)u
            a = int(ylo[0]) % ql
            b = int(ylo[1]) % ql
            u = ((b - 3 * a) % ql) // (ql // 2) % 2
            ssum = int(np.sum(delta[:pp])) % 2
            b_up = bits_of(y, pp, qu)
            line += (f" pred2: a%(Q/16)={a % (ql//16)} b%(Q/16)={b % (ql//16)} "
                     f"u={u} sumDelta%2={ssum} u+sum={ (u + ssum) % 2 } "
                     f"bits_up={b_up[:2]}")
        elif lift_ok and pred == 1:
            delta = ((y - yext) // ql).astype(np.int64)
            c = int(ylo[0]) % ql
            b_up = bits_of(y, pp, qu)
            line += (f" pred1: c={c} c/(Q/4)={c // (ql//4)} "
                     f"sumDelta%2={int(np.sum(delta[:pp])) % 2} "
                     f"factor={pp // pred} bits_up={b_up[:2]}")
        else:
            line += f" (no 4x-lift analysis: pp={pp} pred={pred})"
        print(line)
    print(f"  Table B done: {n_split} on-support split fibers at m={mu}")


def main():
    uppers = [int(a) for a in sys.argv[1:]] or [64, 128]
    cache = {}
    printed_A = set()
    for mu in uppers:
        ml = mu // 2
        if ml not in cache:
            cache[ml] = level_data(ml)
        if mu not in cache:
            cache[mu] = level_data(mu)
        for lv in (ml, mu):
            if lv not in printed_A:
                table_A(cache[lv])
                printed_A.add(lv)
        table_B(cache[ml], cache[mu])
        # free the upper level before the next (keeps peak memory down)
        if mu in cache and mu != uppers[-1]:
            del cache[mu]
        import gc; gc.collect()


if __name__ == "__main__":
    main()
