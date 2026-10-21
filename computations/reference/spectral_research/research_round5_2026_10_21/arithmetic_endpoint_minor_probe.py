"""Bounded discriminator for seven-chain endpoint Fourier minors.

This script screens the *specific* extreme-coordinate minors in the previous
p-adic proof. Floating-point output is discovery evidence only. It does not
certify simplicity of the original U_N or nonvanishing of overlap minors.
All row/column chirps and the invertible Fourier exponent c are omitted:
they do not change exact zero/nonzero over characteristic zero.
"""
import argparse
import numpy as np


def endpoint_sets(n, counts):
    rows = [s*n+j for s,k in enumerate(counts) for j in range(n-k,n)]
    cols = [s*n+j for s,k in enumerate(counts) for j in range(k)]
    return rows, cols


def bounded_compositions(total,parts,bound,prefix=()):
    if parts == 0:
        if total == 0:
            yield prefix
        return
    lo = max(0,total-(parts-1)*bound)
    hi = min(total,bound)
    for value in range(lo,hi+1):
        yield from bounded_compositions(total-value,parts-1,bound,prefix+(value,))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--n", type=int, default=3)
    p.add_argument("--max-total", type=int, default=10)
    p.add_argument("--limit", type=int, default=20)
    args = p.parse_args()
    n, N = args.n, 7*args.n
    zz = np.arange(N)
    F = np.exp(2j*np.pi*(zz[:,None]*zz[None,:] % N)/N)
    tested, candidates = 0, []
    for k in range(1,args.max_total+1):
        for counts in bounded_compositions(k,7,n):
            rows, cols = endpoint_sets(n,counts)
            B = F[np.ix_(rows,cols)]
            sv = np.linalg.svd(B,compute_uv=False)
            ratio = sv[-1]/sv[0]
            tested += 1
            if ratio < 1.e-12:
                candidates.append((k,counts,ratio,rows,cols))
    candidates.sort(key=lambda z:(z[0],z[1]))
    print(f"N={N}, n={n}, tested={tested}, zero_candidates={len(candidates)}")
    for row in candidates[:args.limit]:
        print(row)


if __name__ == "__main__":
    main()
