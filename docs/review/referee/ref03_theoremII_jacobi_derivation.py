"""
REFEREE CHECK R83.3 --- Theorem II (twisted Jacobi sums): closing the derivation
gap flagged as REVIEW_ERRORS #4, and locating the TRUE missing hypothesis.

=============================================================================
1.  WHAT THE PAPER CLAIMS  (thm:jacobi)
=============================================================================
    <f_chi | T(n) | f_psi>  =  e_N(-q/2) * conj(chi)(n1) * psi(n1)
                               * J(chi,psi;q) / (N-1),
    J(chi,psi;q) = sum_{x != 0,1} conj(chi)(x) psi(x-1) e_N(q x),   q = n1 n2.

=============================================================================
2.  WHAT REVIEW_ERRORS #4 CLAIMS
=============================================================================
"Direct calculation, after the substitution x -> x + n1, gives
     conj(chi)(n1) e(2^{-1} n1 n2) sum_x conj(chi)(x) psi(x) e(n2 x / N),
 i.e. the exponential involves n2 alone and the sum has psi(x), not psi(x-1).
 This does not match."

=============================================================================
3.  WHY REVIEW_ERRORS #4 IS ITSELF WRONG
=============================================================================
The reviewer applied an ADDITIVE shift x -> x + n1 and then factored
conj(chi)(x + n1) = conj(chi)(n1) conj(chi)(x).  That step is invalid: chi is
a MULTIPLICATIVE character on F_N^*, so chi(x+n1) does NOT factor.  Only
chi(x * n1) = chi(x) chi(n1) holds.

=============================================================================
4.  THE CORRECT DERIVATION (three lines; supplied here for the paper)
=============================================================================
Conventions (as implemented in src/core/catmap_core.weyl):
    (X^{n1} f)(x) = f(x - n1),      (Z^{n2} f)(x) = e_N(n2 x) f(x),
    T(n1,n2)      = e_N(2^{-1} n1 n2) X^{n1} Z^{n2}.
Then
    (T(n) f)(x) = e_N(2^{-1} n1 n2) * e_N(n2 (x - n1)) * f(x - n1).

With f_chi(x) = chi(x)/sqrt(N-1) for x != 0 and f_chi(0) = 0:

  <f_chi|T(n)|f_psi>
    = (N-1)^{-1} e_N(2^{-1} n1 n2 - n1 n2)
        * sum_x conj(chi)(x) psi(x - n1) e_N(n2 x)
    = (N-1)^{-1} e_N(-2^{-1} q)
        * sum_{x != 0, x != n1} conj(chi)(x) psi(x - n1) e_N(n2 x).      (*)

Now assume n1 != 0 and substitute the MULTIPLICATIVE change of variable
x = n1 y  (a bijection of F_N^*, y ranges over F_N minus {0,1}):

    conj(chi)(n1 y) = conj(chi)(n1) conj(chi)(y),
    psi(n1 y - n1)  = psi(n1) psi(y - 1),
    e_N(n2 * n1 y)  = e_N(q y),         q := n1 n2.

Substituting into (*):

  <f_chi|T(n)|f_psi>
    = e_N(-q/2) conj(chi)(n1) psi(n1) (N-1)^{-1}
        sum_{y != 0,1} conj(chi)(y) psi(y-1) e_N(q y)
    = e_N(-q/2) conj(chi)(n1) psi(n1) J(chi,psi;q) / (N-1).      QED

=============================================================================
5.  THE REAL GAP:  the hypothesis n1 != 0 is MISSING from the paper
=============================================================================
The multiplicative substitution requires n1 invertible.  At n1 = 0 the printed
right-hand side contains conj(chi)(0) psi(0) = 0, whereas the true value from
(*) is
    (N-1)^{-1} sum_{x != 0} conj(chi)(x) psi(x) e_N(n2 x),
which is a Gauss sum for chi = psi and generally NONZERO.  So the printed
identity FAILS on the n1 = 0 line (N of the N^2 frequencies).

This is a genuine (if narrow) defect and must be repaired in the statement.
It does NOT touch the numerical certification, because that certification runs
over LEVEL SETS of q = n1 n2 built from invertible n1.

=============================================================================
6.  WHAT THIS SCRIPT VERIFIES  (two mechanistically independent keys)
=============================================================================
KEY 1 -- brute-force operator matrix element: build T(n) as an explicit N x N
         matrix from X, Z, form <f_chi|T(n)|f_psi> by dense linear algebra.
KEY 2 -- the closed-form right-hand side, evaluated as an independent finite
         character sum with no matrix ever formed.

We compare over ALL (chi, psi, n) in a design, separately for n1 != 0 and
n1 == 0, to (a) confirm the formula where the derivation applies, and
(b) exhibit explicit failure on the n1 = 0 line.

Run: py -3 review/referee/ref03_theoremII_jacobi_derivation.py
"""
import cmath
import json
import math
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(ROOT, "artifacts", "referee_r83")
os.makedirs(OUT, exist_ok=True)


def primitive_root(N):
    from sympy import primitive_root as pr
    return int(pr(N))


def characters(N):
    """All N-1 multiplicative characters of F_N^*, as arrays chi[x], x=0..N-1,
    with chi[0] = 0.  Indexed by j: chi_j(g^t) = e((j t)/(N-1))."""
    g = primitive_root(N)
    dlog = np.zeros(N, dtype=np.int64)
    cur = 1
    for t in range(N - 1):
        dlog[cur] = t
        cur = (cur * g) % N
    chis = np.zeros((N - 1, N), dtype=complex)
    for j in range(N - 1):
        for x in range(1, N):
            chis[j, x] = cmath.exp(2j * math.pi * (j * dlog[x] % (N - 1)) / (N - 1))
    return chis, g


def weyl_matrices(N):
    w = cmath.exp(2j * math.pi / N)
    Xm = np.zeros((N, N), dtype=complex)
    for x in range(N):
        Xm[x, (x - 1) % N] = 1.0
    Zm = np.diag([w ** x for x in range(N)])
    return Xm, Zm, w


def run(N, max_pairs=6, max_freqs=40, seed=20260831):
    chis, g = characters(N)
    Xm, Zm, w = weyl_matrices(N)
    b2 = pow(2, -1, N)
    rng = np.random.default_rng(seed)

    Xp = [np.eye(N, dtype=complex)]
    for _ in range(N - 1):
        Xp.append(Xp[-1] @ Xm)
    Zp = [np.eye(N, dtype=complex)]
    for _ in range(N - 1):
        Zp.append(Zp[-1] @ Zm)

    def T(n1, n2):
        n1 %= N
        n2 %= N
        return (w ** ((b2 * n1 * n2) % N)) * (Xp[n1] @ Zp[n2])

    def f(j):
        v = chis[j].copy() / math.sqrt(N - 1)
        return v

    def Jsum(jc, jp, q):
        s = 0.0 + 0.0j
        cc = chis[jc].conj()
        pp = chis[jp]
        for x in range(2, N):          # x != 0, x != 1
            s += cc[x] * pp[(x - 1) % N] * (w ** ((q * x) % N))
        return s

    pairs = [(int(rng.integers(0, N - 1)), int(rng.integers(0, N - 1)))
             for _ in range(max_pairs)]
    freqs_nz = []
    while len(freqs_nz) < max_freqs:
        n1 = int(rng.integers(1, N))       # n1 != 0
        n2 = int(rng.integers(0, N))
        freqs_nz.append((n1, n2))
    freqs_z = [(0, int(rng.integers(1, N))) for _ in range(min(8, N - 1))]

    err_nz, err_z = [], []
    detail_z = []
    for (jc, jp) in pairs:
        fc, fp = f(jc), f(jp)
        for (n1, n2) in freqs_nz:
            lhs = np.vdot(fc, T(n1, n2) @ fp)
            q = (n1 * n2) % N
            rhs = (w ** ((-b2 * q) % N)) * chis[jc].conj()[n1] * chis[jp][n1] \
                * Jsum(jc, jp, q) / (N - 1)
            err_nz.append(abs(lhs - rhs))
        for (n1, n2) in freqs_z:
            lhs = np.vdot(fc, T(n1, n2) @ fp)
            q = (n1 * n2) % N
            rhs = (w ** ((-b2 * q) % N)) * chis[jc].conj()[n1] * chis[jp][n1] \
                * Jsum(jc, jp, q) / (N - 1)
            err_z.append(abs(lhs - rhs))
            detail_z.append(dict(chi=jc, psi=jp, n1=n1, n2=n2,
                                 lhs_abs=float(abs(lhs)), rhs_abs=float(abs(rhs)),
                                 err=float(abs(lhs - rhs))))

    return dict(
        N=int(N), primitive_root=int(g),
        n_pairs=len(pairs), n_freq_nonzero_n1=len(freqs_nz), n_freq_zero_n1=len(freqs_z),
        MAX_ERR_n1_nonzero=float(max(err_nz)),
        MEAN_ERR_n1_nonzero=float(np.mean(err_nz)),
        MAX_ERR_n1_zero=float(max(err_z)),
        MAX_LHS_abs_on_n1_zero=float(max(d["lhs_abs"] for d in detail_z)),
        MAX_RHS_abs_on_n1_zero=float(max(d["rhs_abs"] for d in detail_z)),
        sample_n1_zero=detail_z[:6],
    )


def main():
    results = [run(N) for N in (23, 31, 41, 61)]
    print(f"{'N':>5}{'max err (n1!=0)':>20}{'max err (n1==0)':>20}"
          f"{'max |LHS| n1=0':>18}{'max |RHS| n1=0':>18}")
    print("-" * 82)
    for r in results:
        print(f"{r['N']:>5}{r['MAX_ERR_n1_nonzero']:>20.3e}{r['MAX_ERR_n1_zero']:>20.3e}"
              f"{r['MAX_LHS_abs_on_n1_zero']:>18.6f}{r['MAX_RHS_abs_on_n1_zero']:>18.6f}")

    worst_ok = max(r["MAX_ERR_n1_nonzero"] for r in results)
    worst_bad = max(r["MAX_ERR_n1_zero"] for r in results)
    rhs_zero = max(r["MAX_RHS_abs_on_n1_zero"] for r in results)

    formula_holds = worst_ok < 1e-11
    n1zero_fails = worst_bad > 1e-3 and rhs_zero < 1e-14

    verdict = dict(
        derivation_supplied="multiplicative substitution x = n1*y (see module docstring)",
        review_errors_4_diagnosis="WRONG: used additive shift x -> x+n1 and factored "
                                  "a multiplicative character across a sum",
        max_error_where_derivation_applies=float(worst_ok),
        max_error_on_n1_equals_0_line=float(worst_bad),
        rhs_identically_zero_on_n1_equals_0=bool(rhs_zero < 1e-14),
        FORMULA_CONFIRMED_for_n1_nonzero=bool(formula_holds),
        GENUINE_DEFECT_missing_hypothesis_n1_nonzero=bool(n1zero_fails),
        VERDICT=("PASS: identity proven and certified for n1 != 0; REVIEW_ERRORS #4's "
                 "diagnosis refuted; NEW genuine defect found: the paper omits the "
                 "hypothesis n1 != 0, and the printed RHS vanishes identically on the "
                 "n1 = 0 line where the true matrix element does not")
                if (formula_holds and n1zero_fails) else "INCONCLUSIVE",
    )
    print()
    print("=" * 82)
    print(f"formula holds for n1 != 0        : {formula_holds}  (max err {worst_ok:.2e})")
    print(f"formula FAILS on the n1 = 0 line : {n1zero_fails}  (max err {worst_bad:.2e}, "
          f"printed RHS == 0 there)")
    print(f"VERDICT: {verdict['VERDICT']}")
    print("=" * 82)

    path = os.path.join(OUT, "ref03_theoremII_jacobi_derivation.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(dict(verdict=verdict, designs=results), fh, indent=2)
    print(f"artifact: {path}")
    return 0 if (formula_holds and n1zero_fails) else 1


if __name__ == "__main__":
    raise SystemExit(main())
