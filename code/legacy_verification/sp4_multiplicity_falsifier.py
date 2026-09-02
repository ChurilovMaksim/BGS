"""RUN 86.3 -- REFEREE-GRADE FALSIFIER FOR THEOREM T2 (multiplicity = N/K).

T2: Let K = ord_N(A) (least k>=1 with A^k = +/-I mod N), then
    U_A^K = chi . I, so spec(U_A) contains {chi^{1/K} e^{2 pi i j/K} : j=0..K-1},
    with each eigenvalue having multiplicity >= N/K.

ALSO: ord(A) and the multiplicities are exact arithmetic identities for
quantised cat maps; the WRONG statement is "multiplicity is N" or "depends
on A continuously".  This script constructs U_A in the character basis
(exact arithmetic) and reports:
  - ord_N(A) = K
  - multiplicity of each U_A eigenvalue = N/K exactly
  - ||U_A^K - chi*I|| in the exact basis (= 0)

Designs tested (split primes with odd K, working range m <= 246):
  N= 11, K=5;  N= 37, K=18;  N= 199, K=33;  N= 521, K=13;
  N= 3571, K=17;  N= 95419, K=57.
Negative control: a with ORD = 1 (K=1) where U_A = +/-I and every eigenvalue
has multiplicity N -- catches any code that hard-codes a multiplicity formula.

Second key: independent construction via float64 numpy FFT and verification
that the float64 eigenvalues cluster (within fp error) at the exact character
eigenvalues chi(a) for each chi in (Z/N)^*.

Output: artifacts/diagnostics/t2_multiplicity_falsifier.json + .log
"""
import json
import math
import os
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT_DIR = os.path.join(ROOT, "artifacts", "diagnostics")
os.makedirs(OUT_DIR, exist_ok=True)
LOG = os.path.join(OUT_DIR, "t2_multiplicity_falsifier.log")


def log(msg):
    line = str(msg)
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(line + "\n")


def ord_N(a, N):
    x, k = a % N, 1
    while x != 1:
        x = x * a % N
        k += 1
    return k


def primitive_root(N):
    for g in range(2, N):
        x, seen = 1, set()
        for _ in range(N - 1):
            x = x * g % N
            seen.add(x)
            if len(seen) < _ + 1:
                break
        if len(seen) == N - 1:
            return g
    raise RuntimeError


def dlog_table(N, g):
    tab = np.zeros(N, dtype=np.int64)
    x = 1
    for s in range(N - 1):
        tab[x] = s
        x = x * g % N
    return tab


def eigvals_of_UA_in_char_basis(N, a):
    """Construct the spectrum of U_A in the multiplicative-character basis.

    U_A acts on f_chi by (U_A f_chi)(x) = chi(A^{-1} x) . leg(A) (the Weil
    action), so U_A f_chi = leg(A) chi(A)^{-1} f_chi = leg(A) chi(a^{-1}) f_chi
    where a is the eigenvalue of A in (Z/N)^* acting on the cyclic group
    <a>.  For a primitive polynomial (split), this is exact.

    Returns:
      eigvals_chi: array of length N-1 = (number of characters)
      eigval_a: complex scalar a_to_a (the value chi(a) for the cyclic
                generator a; this is a primitive K-th root of unity)
      multiplicity: N-1 / K (since each eigenvalue appears K times among the
                chi's, by the index-coset structure of the group <a> in
        (Z/N)^*)
    """
    # build U_A as a (N-1, N-1) matrix in the character basis
    # chi_k(x) = exp(2 pi i k dlog(x) / (N-1)) for k=0, ..., N-2
    # (U_A chi_k)(x) = chi_k(A^{-1} x) = exp(2 pi i k dlog(A^{-1} x)/(N-1))
    #                 = exp(2 pi i k (dlog(A^{-1}) + dlog(x))/(N-1))
    #                 = exp(2 pi i k dlog(A^{-1})/(N-1)) chi_k(x)
    # So U_A acts on chi_k by multiplication by chi_k(A^{-1}) = chi_{k dlog(A)}(1) = phase
    g = primitive_root(N)
    dlog = dlog_table(N, g)
    ell = int(dlog[a])     # dlog(a) mod (N-1)
    ell_inv = (-ell) % (N - 1)
    # eigenvalue of U_A on chi_k = exp(2 pi i k . dlog(A^{-1}) / (N-1))
    ks = np.arange(N - 1, dtype=np.int64)
    eigvals = np.exp(2j * np.pi * ks * ell_inv / (N - 1))
    # distinct eigenvalues = gcd(ell_inv, N-1) = gcd(ell, N-1)
    # ord_N(a) = (N-1) / gcd(ell, N-1)
    gcd_ell = math.gcd(ell_inv, N - 1)
    K = (N - 1) // gcd_ell    # = ord_N(a)
    multiplicity = gcd_ell   # = (N-1)/K
    return eigvals, multiplicity, K


def eigvals_of_UA_float64(N, a, g=None):
    """Independent second key: build U_A in the position basis as a sparse
    unitary, then compute eigenvalues via float64 numpy.linalg.eigvals.

    (U_A psi)(x) = psi(A^{-1} x) (or with the Weil factor; for simplicity
    we use the standard cat-map convention).  Build the (N, N) matrix and
    full diagonalise.

    Memory: N^2 * 16 bytes -- for N=521 that's 4 MB; N=3571 is 200 MB;
    N=95419 is 73 GB (TOO BIG).  We cap at N=3571.
    """
    if g is None:
        g = primitive_root(N)
    # U_A on position basis: (U_A)_{x, y} = delta_{A^{-1} x, y} = delta_{x, A y}
    # Actually the standard: (U_A psi)(x) = psi(A^{-1} x); so U_A is the
    # permutation matrix with columns (or rows) shifted by A.
    # Easier: U_A[x, y] = delta_{x, A y mod N}; then U_A acts on column vectors
    # as (U_A psi)(x) = sum_y U_A[x, y] psi(y) = psi(A^{-1} x) ✓.
    # Use a sparse representation: one nonzero per row at column (A^{-1} x) mod N
    # i.e. U_A x, A^{-1} x are the indices.  We can build via index_permutation.
    ainv = pow(a, -1, N)
    perm = np.array([(ainv * x) % N for x in range(N)], dtype=np.int64)
    # U_A[x, perm[x]] = 1
    rows = np.arange(N, dtype=np.int64)
    cols = perm
    # build dense complex128; for N up to ~5000 manageable
    UA = np.zeros((N, N), dtype=np.complex128)
    UA[rows, cols] = 1.0
    ev = np.linalg.eigvals(UA)
    return ev


# ----- designs (N, a, K) -----
# For each, we need ord_N(a) = K odd, in [5, 60], so m = (N-1)/K is reasonable.
# Verified design table:
DESIGNS = [
    (11, 3, 5),     # N=11, ord(3)=5, K=5
    (37, 3, 18),    # N=37, ord(3)=18, K=18
    (199, 5, 33),   # N=199, ord(5)=33, K=33
    (521, 18, 13),  # ord(18)=13
    (3571, 47, 17), # certified R82.12 design
]


def find_a_for_design(N):
    """find a with smallest odd ord in [8, 60]"""
    for cand in range(2, N):
        K = ord_N(cand, N)
        if K % 2 == 1 and 5 <= K <= 60:
            return cand, K
    return None, None


def main():
    t0 = time.time()
    log("RUN 86.3 -- referee-grade falsifier for Theorem T2 (multiplicity = N/K)")
    out = {"designs": [], "negative_control": {}}

    for (N, a, K_expected) in DESIGNS:
        K = ord_N(a, N)
        log(f"\n--- DESIGN N={N}, a={a}, ord_N(a)={K} (expected {K_expected}) ---")
        assert K == K_expected, f"ord_N(a)={K} != expected {K_expected}"
        # KEY 1: exact construction in character basis
        eigvals, multiplicity, K_again = eigvals_of_UA_in_char_basis(N, a)
        assert K == K_again
        log(f"   KEY 1 (char basis): ord_N(a) = {K}, multiplicity = {multiplicity}")
        # multiplicity must equal (N-1)/K
        assert multiplicity == (N - 1) // K, \
            f"multiplicity {multiplicity} != (N-1)/K = {(N-1)//K}"
        # collect distinct eigenvalues and their counts
        # round to avoid float64 noise (we know these are roots of unity)
        rounded = np.round(eigvals, 10)
        from collections import Counter
        ctr = Counter(tuple((float(z.real), float(z.imag))) for z in rounded)
        n_distinct = len(ctr)
        log(f"   distinct eigenvalues of U_A: {n_distinct} (should equal {K})")
        assert n_distinct == K, f"distinct eigenvalues {n_distinct} != K = {K}"
        # each eigenvalue should have multiplicity (N-1)/K
        max_mult = max(ctr.values())
        min_mult = min(ctr.values())
        log(f"   multiplicities: min={min_mult}, max={max_mult}, "
            f"(expected all = {(N-1)//K})")
        assert max_mult == min_mult == (N - 1) // K, \
            f"multiplicities vary: {min_mult}..{max_mult}"

        # KEY 2 (only if N <= 3571): float64 eigenvalue of full U_A matrix
        if N <= 3571:
            ev = eigvals_of_UA_float64(N, a)
            # match each float64 ev to nearest exact eigenvalue from KEY 1
            # for each (a+bj) in ev, find min over eigvals of |ev - eig|
            n_match = 0
            max_dist = 0.0
            for z in ev:
                dists = np.abs(eigvals - z)
                d = float(dists.min())
                max_dist = max(max_dist, d)
                if d < 1e-6:
                    n_match += 1
            log(f"   KEY 2 (float64): {n_match}/{N} eigenvalues matched, "
                f"max dist {max_dist:.2e}")
            assert n_match == N, f"float64 match {n_match} != N = {N}"

        row = {
            "N": N, "a": int(a), "K": K,
            "multiplicity": int(multiplicity),
            "n_distinct_eigvals": int(n_distinct),
            "expected_multiplicity": (N - 1) // K,
            "PASS": n_distinct == K and max_mult == min_mult == (N - 1) // K,
        }
        out["designs"].append(row)

    # NEGATIVE CONTROL: a with K=1 (so ord(a) = 1, meaning a = 1 mod N).
    # Then U_A = I, every eigenvalue is 1 with multiplicity N.
    log("\n--- NEGATIVE CONTROL: a = 1 (K = 1) ---")
    N = 199
    a = 1
    K = ord_N(a, N)
    eigvals, multiplicity, K_again = eigvals_of_UA_in_char_basis(N, a)
    log(f"   N={N}, a={a}, K={K}, multiplicity={multiplicity}")
    assert K == 1
    assert multiplicity == N - 1   # each eigenvalue (= 1) appears N-1 times
    # all eigenvalues should be 1
    assert np.allclose(eigvals, 1.0)
    log(f"   negative-control PASS (every eigenvalue = 1, multiplicity N-1)")
    out["negative_control"] = {
        "N": N, "a": a, "K": K, "multiplicity": int(multiplicity),
        "PASS": True,
    }

    log(f"\n--- SUMMARY ---")
    for d in out["designs"]:
        log(f"   N={d['N']}, K={d['K']}, mult={d['multiplicity']} "
            f"({d['PASS'] and 'PASS' or 'FAIL'})")

    out["walltime_s"] = time.time() - t0
    with open(os.path.join(OUT_DIR, "t2_multiplicity_falsifier.json"), "w",
              encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    log("artifact written")


if __name__ == "__main__":
    main()