"""Wave 39 task 4: exact census of E_alt over 2-part kernel points.

For a kernel sequence y (mod Q, minimal period p, 4|p) with
representatives in [0,Q):
  e_i = (y_{i+1} - 6 y_i + y_{i-1})/Q   (indices mod p, exact integer)
  A   = sum_{i<p} (-1)^i y_i
  E_alt = -sum_{i<p} (-1)^i e_i
Identity to verify: A = (Q/8) * E_alt. Question: |E_alt| < 8 ?
"""
import sys
import numpy as np
from collections import Counter, defaultdict


def kernel_seqs(m, q):
    """All kernel points mod q: seeds (a,b) with (M^m - I)s = 0 mod q,
    via brute force over a grid is too slow; use the SNF-free approach:
    enumerate seeds from the known structure: kernel has exactly q
    points; generate by iterating over the 2-dim seed space reduced by
    the kernel equations. Here we do it directly: M^m - I over Z/q has
    kernel of size q; we find it by solving via Smith-like brute force
    on one coordinate: for each a in [0,q), solve for b.
    Simpler: reuse wave36 snf_kernel_i32."""
    sys.path.insert(0, ".")
    from wave36_2part import snf_kernel_i32
    return snf_kernel_i32(m, q)


def min_period(seq):
    m = len(seq)
    for p in range(1, m + 1):
        if m % p == 0 and np.array_equal(seq, np.tile(seq[:p], m // p)):
            return p
    return m


def ealt_of_period_block(block, Q):
    p = len(block)
    y = block.astype(np.int64)
    yp = np.roll(y, -1)
    ym = np.roll(y, 1)
    num = yp - 6 * y + ym
    assert np.all(num % Q == 0), "recurrence defect not divisible by Q"
    e = num // Q
    sgn = np.where(np.arange(p) % 2 == 0, 1, -1)
    A = int(np.sum(sgn * y))
    E = -int(np.sum(sgn * e))
    return A, E, e


def main():
    for m in (32, 64):
        k = m.bit_length() - 1
        Q = 2 ** (2 * k + 3)
        pts = kernel_seqs(m, Q)
        assert len(pts) == Q, (len(pts), Q)
        bad_id = 0
        dist_all = Counter()
        dist_p8 = Counter()
        worst = []
        e_range = Counter()
        for row in pts:
            p = min_period(row)
            block = row[:p]
            A, E, e = ealt_of_period_block(block, Q)
            if 8 * A != Q * E:
                bad_id += 1
            dist_all[E] += 1
            for v in e:
                e_range[int(v)] += 1
            if p >= 8:
                dist_p8[E] += 1
                if abs(E) >= 8:
                    worst.append((E, p, block[:8].tolist()))
        print(f"m={m} Q={Q} points={len(pts)} identity_failures={bad_id}")
        print(f"  E_alt distribution (all periods): {dict(sorted(dist_all.items()))}")
        print(f"  E_alt distribution (p>=8): {dict(sorted(dist_p8.items()))}")
        print(f"  e_i value range: {dict(sorted(e_range.items()))}")
        print(f"  |E|>=8 cases with p>=8: {len(worst)}; first few: {worst[:5]}")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
