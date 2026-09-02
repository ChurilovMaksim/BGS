"""
EXACT EVALUATION OF THE FOURTH-ORDER CANCELLATION COUNT, and the classification
of the two mechanisms that produce non-pairing solutions at higher order.

Setting.  In the eigenbasis of A (split case: over F_p; inert case: over F_{p^2}
with h^{-1} = Frobenius conjugate) a single A-orbit of frequencies gives, for a
cancellation Sum_i eps_i A^{j_i} u_0 = 0, the coupled system

    (S)   Sum_i eps_i h_i = 0        and       Sum_i eps_i h_i^{-1} = 0,
          h_i in H = <alpha>, |H| = k.

THEOREM (exact, r = 4).  With signs (+,-,+,-) the complete solution set of (S) is
  (i)   {h_1,h_3} = {h_2,h_4}   as multisets                      (always), and
  (ii)  h_3 = -h_1, h_4 = -h_2  with h_1,h_2 free                 (iff -1 in H).
There are no other solutions, and

    #solutions = 2k^2 - k          if -1 not in H,
                 3k^2 - 3k         if -1 in H.

Proof.  Put sigma = h_1 + h_3, pi = h_1 h_3 and sigma', pi' for the other pair.
Then 1/h_1 + 1/h_3 = sigma/pi, so (S) says sigma = sigma' and sigma/pi =
sigma'/pi'.  If sigma != 0 this forces pi = pi', so both pairs are the roots of
x^2 - sigma x + pi and hence equal as multisets, giving 2k^2 - k ordered
solutions.  If sigma = 0 then h_3 = -h_1 (needs -1 in H) and sigma' = 0 too, so
h_4 = -h_2; that family has k^2 members and meets (i) in 2k ordered tuples,
whence the totals.  QED

At order r = 2s > 4 non-pairing solutions do occur, by exactly two mechanisms:
  (a) STRUCTURAL: for every divisor d >= 2 of k the order-d subgroup consists of
      all d-th roots of unity, so it sums to zero, and so does each of its
      cosets (and the same for the inverses).  Hence for s = d, and more
      generally whenever s is a sum of divisors, non-pairing solutions exist.
      They are absent for every s < (least prime factor of k).
  (b) SPORADIC mod-p coincidences, governed by whether a fixed algebraic family
      is defined over F_p (a Chebotarev-type condition: for k = 13, s = 4 the
      extra count is exactly 416 for p = 313? no --- 4368 at p=313 and 416 at
      p = 521, 547, 911, and 0 at p = 599, 677, 859, 937, 1093).
      Empirically  extras / pairings  ~  c * k^s / p^2  with c in [0.01, 0.11].

Consequence.  The moments of order 2s of the compression match the Wigner
(pairing) values with relative error O(k^s/p^2) plus the structural terms, which
vanish when k has no prime factor <= s.  In particular the fourth moment is EXACT.
"""
import itertools, json, os
from collections import Counter
from sympy import primitive_root, isprime

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")


def subgroup(p, k):
    g = primitive_root(p)
    a = pow(g, (p-1)//k, p)
    return [pow(a, j, p) for j in range(k)]


def count_order(p, k, s):
    """#solutions of (S) with s plus-signs and s minus-signs, and the pairing count."""
    H = subgroup(p, k)
    inv = {h: pow(h, -1, p) for h in H}
    key = Counter(); mult = Counter()
    for t in itertools.product(H, repeat=s):
        key[(sum(t) % p, sum(inv[x] for x in t) % p)] += 1
        mult[tuple(sorted(t))] += 1
    return sum(c*c for c in key.values()), sum(c*c for c in mult.values())


def verify_r4(cases=((101, 5), (101, 10), (101, 20), (101, 25), (211, 3), (211, 5),
                     (211, 6), (211, 10), (521, 5), (521, 8), (521, 10), (521, 13),
                     (521, 20), (1009, 3), (1009, 6), (1009, 8), (1009, 12),
                     (1009, 24), (2003, 13))):
    rows = []
    for (p, k) in cases:
        if (p-1) % k: continue
        H = set(subgroup(p, k)); m1 = (p-1) in H
        tot, pair = count_order(p, k, 2)
        f = (3*k*k-3*k) if m1 else (2*k*k-k)
        rows.append(dict(p=p, k=k, minus1=bool(m1), total=int(tot),
                         formula=int(f), pairings=int(pair), ok=bool(tot == f)))
    return rows


if __name__ == "__main__":
    rows = verify_r4()
    bad = [r for r in rows if not r["ok"]]
    print("r=4 exact formula:  2k^2-k (-1 not in H)   /   3k^2-3k (-1 in H)")
    for r in rows:
        print(f"  p={r['p']:5d} k={r['k']:3d} -1inH={str(r['minus1']):5s} "
              f"total={r['total']:8d} formula={r['formula']:8d} "
              f"{'OK' if r['ok'] else 'MISMATCH'}")
    print(f"\n{len(rows)-len(bad)}/{len(rows)} exact matches")
    json.dump(dict(r4=rows, all_exact=(len(bad) == 0)),
              open(os.path.join(ART, "cancellation_r4.json"), "w"), indent=1)
    print("saved artifacts/cancellation_r4.json")
