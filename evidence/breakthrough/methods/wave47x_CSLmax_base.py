"""Wave 47x, task C (CSL-max): base-case census + drift structure.

1. For each level m: all on-support fibers with p in {1,2,4}:
   p=1: c and t = c/(Q/4); p=2: (a,b) residues mod Q/16 and u;
   p=4: bits (tau0,k) and whether the fiber is the reduction of a
   split fiber at level 2m (tower membership).
2. For pred1/pred2 lifts (from Table B logic): print delta mod 2
   patterns to expose the drift rule.
3. Full Table A counts (all OTHER bits values, not just first 20).
Usage: python3 wave47x_CSLmax_base.py [m ...]  (default 32 64 128)
"""
import sys
sys.path.insert(0, ".")
import numpy as np
from collections import defaultdict, Counter
from wave16_d1a_targeted import Dm, torsion_data, group_ids
from wave36_2part import snf_kernel_i32, orbit_canon
from wave38_helpers import period_of
from wave47x_CSLmax_all import level_data, bits_of


def main():
    levels = [int(a) for a in sys.argv[1:]] or [32, 64, 128]
    datas = {}
    for m in levels:
        datas[m] = level_data(m)
    for m in levels:
        L = datas[m]
        q, pts = L["q"], L["pts"]
        print(f"===== level m={m} Q={q} =====")
        # full Table A distribution
        dist = Counter()
        tower01 = []
        for f, idxs in L["onsup_by_fib"].items():
            y = pts[idxs[0]].astype(np.int64)
            p = period_of(y)
            if p % 4 != 0:
                continue
            b = bits_of(y, p, q)
            o = len(L["fib_orbits"][f])
            dist[(o > 1, b[0], b[1])] += 1
        print("  Table A full dist (split?, tau0, k) -> count:")
        for key in sorted(dist):
            print(f"    {key}: {dist[key]}")
        # period 1, 2 census
        for p_want in (1, 2):
            rows = []
            for f, idxs in L["onsup_by_fib"].items():
                y = pts[idxs[0]].astype(np.int64)
                p = period_of(y)
                if p != p_want:
                    continue
                if p_want == 1:
                    c = int(y[0]) % q
                    rows.append((f, c, c // (q // 4)))
                else:
                    a = int(y[0]) % q
                    b = int(y[1]) % q
                    u = ((b - 3 * a) % q) // (q // 2) % 2
                    rows.append((f, a % (q // 16), b % (q // 16), u))
            print(f"  period-{p_want} on-support fibers: {len(rows)}")
            for r in rows[:40]:
                print("   ", r)
        # tower period-4 fibers: reductions of split fibers at 2m
        if 2 * m in datas:
            up = datas[2 * m]
            ql = q
            low_by_seq = {}
            for i in range(len(pts)):
                low_by_seq[pts[i].astype(np.int64).tobytes()] = i
            tower4 = {}
            for f, idxs in up["onsup_by_fib"].items():
                if len(up["fib_orbits"][f]) <= 1:
                    continue
                y = up["pts"][idxs[0]].astype(np.int64)
                yred = (y % ql).astype(np.int64)
                li = low_by_seq.get(yred[:m].tobytes())
                if li is None:
                    continue
                ylo = pts[li].astype(np.int64)
                pred = period_of(ylo)
                if pred == 4:
                    tower4[int(L["fib"][li])] = ylo
            print(f"  tower period-4 fibers at m={m} (reductions of split "
                  f"fibers at {2*m}): {len(tower4)}")
            for f, ylo in sorted(tower4.items()):
                b = bits_of(ylo, 4, q)
                # reduction of ylo at m/2 if available
                print(f"    fid={f} y0..3={ylo[:4].tolist()} bits={b[:2]} "
                      f"S0/(Q/32)={b[2][0]//(q//32)} S1={b[2][1]}")
    # drift patterns for pred1/pred2 lifts at the largest level pair
    if len(levels) >= 2:
        ml, mu = levels[-2], levels[-1]
        lo, up = datas[ml], datas[mu]
        ql, qu = lo["q"], up["q"]
        low_by_seq = {}
        for i in range(len(lo["pts"])):
            low_by_seq[lo["pts"][i].astype(np.int64).tobytes()] = i
        print(f"===== drift patterns: upper m={mu} over m={ml} =====")
        for f, idxs in up["onsup_by_fib"].items():
            if len(up["fib_orbits"][f]) <= 1:
                continue
            y = up["pts"][idxs[0]].astype(np.int64)
            pp = period_of(y)
            yred = (y % ql).astype(np.int64)
            li = low_by_seq.get(yred[:ml].tobytes())
            if li is None:
                continue
            ylo = lo["pts"][li].astype(np.int64)
            pred = period_of(ylo)
            if pred not in (1, 2):
                continue
            yext = np.array([ylo[i % pred] for i in range(mu)], dtype=np.int64)
            delta = ((y - yext) // ql).astype(np.int64)
            dmod = (delta % 2).tolist()
            if pred == 2:
                step_ok = all((delta[i + 2] - delta[i]) % 2 == 1
                              for i in range(mu - 2))
                print(f"  pred2 up fid={f} p={pp}: delta%2 first16={dmod[:16]} "
                      f"step2-odd={step_ok}")
            else:
                half_ok = all((delta[i + 4] - delta[i]) % 2 == 1
                              for i in range(mu - 4))
                print(f"  pred1 up fid={f} p={pp}: delta%2 first16={dmod[:16]} "
                      f"half4-odd={half_ok} sum%2={int(np.sum(delta)) % 2}")


if __name__ == "__main__":
    main()
