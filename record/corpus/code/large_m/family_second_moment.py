"""
Run 82w: THE TRUE MECHANISM OF THE SIXTH MOMENT -- a family second moment.
=========================================================================
op:pairing, attempt 2.  Attempt 1 (R82.21) showed the "matching" picture is
not well-defined; this run replaces it with an EXACT identity and verifies it.

DERIVATION (full character group first, for clarity).  With
J(chi,psi;q) = sum_{x in X} conj(chi)(x) psi(x-1) e_N(qx),  X = F_N \\ {0,1},

  (1/(N-1)^2) sum_{chi,psi in Ghat} |J|^6
    = sum_{x,y in X^3} e_N(q(Sx-Sy)) [sum_chi chi(Py/Px)] [sum_psi psi(Pcy/Pcy')]
    = sum_{(x,y): e3(x)=e3(y), e3(x-1)=e3(y-1)} e_N(q(Sx-Sy))

where e3 = triple product, Sc = sum of coordinates.  Introducing the COMMON
values (P,Q) = (e3(x), e3(x-1)) = (e3(y), e3(y-1)) and

    W(P,Q) := sum_{y in X^3: e3(y)=P, e3(y-1)=Q} e_N(q*Sy),

this becomes the EXACT identity

    M6(q) := (1/(N-1)^2) sum_{chi,psi} |J|^6  =  sum_{(P,Q)} |W(P,Q)|^2.

So the sixth moment is the SECOND MOMENT OF A FAMILY of exponential sums
W(P,Q) -- traces over the curves C_{P,Q} = {y: e3(y)=P, e3(y-1)=Q} of the
linear phase e_N(q*Sy).  There are NO matchings and NO diagonal N^3: the N^3
scale comes from summing ~N^2 curves, each contributing |W| ~ sqrt(N) by
Weil--Deligne (the phase Sy is non-degenerate on the curve), i.e. the family
second moment ~ N^2 * N = N^3.  The Catalan constant 5 is then

    5 = lim (1/N^3) sum_{(P,Q)} |W(P,Q)|^2,

a FAMILY SECOND MOMENT -- i.e. a monodromy/cohomological quantity of the
S_3-covering family (the curve C_{P,Q} is the fibre of the S_3-cover), exactly
the kind of input Katz's equidistribution theorems supply.  The "factorial 6"
would correspond to six pointwise contributions; the truth is that the main
term counts cohomology, not matchings.

THIS SCRIPT verifies, by exact computation at small primes:
  V1  the identity M6(q) = sum_{(P,Q)} |W(P,Q)|^2  (both sides computed
      independently: left from the J-matrix over all character pairs, right
      from the (P,Q)-bucketed phase sums);
  V2  the constant: (1/N^3) sum |W|^2 -> ~5;
  V3  the per-curve Weil bound: |W(P,Q)| <= C sqrt(N) with C reported.

Output: artifacts/r82/family_second_moment.json
"""

import json
import os
import sys
import time

import numpy as np


def run(N, q, chi_full=True):
    t0 = time.time()
    X = np.array([x for x in range(2, N)], dtype=np.int64)      # x != 0, 1
    g_table = np.zeros(N, dtype=np.int64)                       # discrete log
    # multiplicative characters via a primitive root
    def prim_root(p):
        from sympy import factorint
        fac = list(factorint(p - 1))
        g = 2
        while any(pow(g, (p - 1) // f, p) == 1 for f in fac):
            g += 1
        return g
    g = prim_root(N)
    dlog = np.zeros(N, dtype=np.int64)
    x = 1
    for s in range(N - 1):
        dlog[x] = s
        x = x * g % N
    dl_X = dlog[X]

    # ---- right side: bucket y in X^3 by (P,Q) = (e3(y), e3(y-1)) ----------
    W = {}
    for y1 in X:
        for y2 in X:
            p12 = int(y1 * y2 % N)
            s12 = int(y1 + y2)
            for y3 in X:
                P = p12 * int(y3) % N
                Q = ((y1 - 1) * (y2 - 1) % N) * ((y3 - 1) % N) % N
                S = s12 + int(y3)
                key = (P, Q)
                W[key] = W.get(key, 0j) + complex(np.cos(2 * np.pi * q * S / N),
                                                  np.sin(2 * np.pi * q * S / N))
    tR = time.time() - t0
    rhs = float(sum(abs(w) ** 2 for w in W.values()))
    wmax = max(abs(w) for w in W.values())

    # ---- left side: the J-matrix over all character pairs -----------------
    t1 = time.time()
    ph = np.exp(2j * np.pi * (q * X % N) / N)
    # J(chi,psi) = sum_x conj(chi)(x) psi(x-1) e_N(qx);
    # rows indexed by chi exponent k over dlog(x) for x in X (|X| = N-2),
    # cols by psi exponent j over dlog(x-1).
    K = np.exp(-2j * np.pi * np.outer(np.arange(N - 1), dl_X) / (N - 1)) * ph
    Vm = np.exp(2j * np.pi * np.outer(np.arange(N - 1), dlog[(X - 1) % N]) / (N - 1))
    Jm = K @ Vm.T                                 # (N-1, N-1)
    M6 = float((np.abs(Jm) ** 6).sum()) / (N - 1) ** 2
    tL = time.time() - t1

    ident_err = abs(M6 - rhs) / max(rhs, 1e-30)
    const = rhs / N ** 3
    print(f"N={N} q={q}: M6 = {M6:.6e};  sum|W|^2 = {rhs:.6e};  "
          f"rel err = {ident_err:.2e}   [{len(W)} curves, "
          f"L {tL:.0f}s / R {tR:.0f}s]", flush=True)
    print(f"   constant (1/N^3)sum|W|^2 = {const:.4f}   (Catalan target 5);  "
          f"max|W|/sqrt(N) = {wmax/np.sqrt(N):.3f}", flush=True)
    return {"N": N, "q": q, "M6": M6, "sum_W2": rhs, "rel_err": ident_err,
            "n_curves": len(W), "const_over_N3": const,
            "max_W_over_sqrtN": wmax / np.sqrt(N)}


def main():
    out = {"script": "src/r82w_family_second_moment.py",
           "generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "tests": []}
    for (N, q) in ((37, 3), (37, 5), (53, 5), (53, 11), (73, 7)):
        out["tests"].append(run(N, q))
    dest = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "artifacts", "r82", "family_second_moment.json")
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("artifact ->", dest, flush=True)


if __name__ == "__main__":
    main()
