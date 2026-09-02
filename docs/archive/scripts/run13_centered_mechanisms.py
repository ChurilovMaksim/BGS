"""
RUN 13 / Phase 2 + 3: CENTERED MOMENTS and TWO-MECHANISM INVESTIGATION.

Phase 2: Work with W = V_lam - mu*I where mu = Tr[V_lam]/m.
         Compute Tr[W^r] for r=2,3,4 and compare with raw Tr[V^r].
         Verify that WD comparison makes sense only after centering.

Phase 3: For each A in a family, check:
         (a) is k = ord_p(alpha) even?  (arithmetic switch)
         (b) does there exist R in GL(2,Z) with RAR^{-1}=A^{-1}?
             (classical reversing -> Theta exists)
         Test correlation / possible disagreement.
"""
import math, os, sys, json
import numpy as np
from sympy import primerange, factorint

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_core import U_cat
from master_formula_r4 import weyl_matrix, build_V, projector_eigenspace
from master_formula_strong import find_orbit_H, brute_resonance_solutions

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")


def is_reversible(A):
    """Check if exists R in GL(2,Z) with R A R^{-1} = A^{-1}.
    For SL(2,Z): A=[a,b;c,d] is reversible iff exists R with certain form.
    Standard criterion: A reversible iff trace(A) has specific property."""
    a,b,c,d = A
    tr = a+d
    det = a*d-b*c
    # In SL(2,Z), reversible iff tr is even or ... (Baake-Roberts criterion)
    # Simplified check: try small R matrices
    candidates_R = [
        [[0,1],[1,0]],          # swap coordinates
        [[0,-1],[1,0]],         # rotation by pi/2
        [[1,0],[0,-1]],         # reflection y
        [[-1,0],[0,1]],         # reflection x
        [[1,1],[0,-1]],
        [[1,0],[1,-1]],
    ]
    Amat = np.array(A).reshape(2, 2)
    Ainv = np.array([[d,-b],[-c,a]])  # since det=1
    for R in candidates_R:
        Rm = np.array(R)
        detR = int(round(np.linalg.det(Rm)))
        if abs(detR) != 1: continue
        Rinv = np.array([[Rm[1,1],-Rm[0,1]],[-Rm[1,0],Rm[0,0]]]) / detR
        if np.allclose(Rm@Amat@Rinv, Ainv) or np.allclose(Rm@Amat@Rinv, -Ainv):
            return True
    return False


def phase2_centered(p, A, Fd):
    """Compute centered moments for each eigenspace."""
    U = U_cat(A, p)
    V = build_V(Fd, p)
    spaces = projector_eigenspace(U)
    out = []
    for (lam, Pl, m) in spaces[:2]:
        Vl = Pl @ V @ Pl
        mu = complex(np.trace(Vl)) / m
        W = Vl - mu * np.eye(p, dtype=complex)
        moments_raw = [float(np.real(np.trace(np.linalg.matrix_power(Vl, r))))
                       for r in (2, 4)]
        moments_ctr = [float(np.real(np.trace(np.linalg.matrix_power(W, r))))
                       for r in (2, 4)]
        out.append(dict(m=m, mu_re=float(mu.real), mu_im=float(mu.imag),
                        tr2_raw=moments_raw[0], tr4_raw=moments_raw[1],
                        tr2_ctr=moments_ctr[0], tr4_ctr=moments_ctr[1]))
    return out


def phase3_two_mechanisms(primes=(101, 199, 211, 307, 401)):
    """For each hyperbolic A and prime p: record parity of k=ord_p(alpha),
    reversibility of A. Look for disagreement patterns."""
    results = []
    hyperbolic_As = [
        [2,1,1,1],   # classic cat map
        [3,1,2,1],
        [2,1,3,2],
        [5,2,2,1],
        [1,1,3,4],
    ]
    for A in hyperbolic_As:
        rev = is_reversible(A)
        for p in primes:
            H = find_orbit_H(p, A)
            if H is None: continue
            k = len(H)
            has_m1 = (p-1) in set(H)
            results.append(dict(A=A, p=p, k=k,
                                k_even=(k%2==0), minus1_in_H=bool(has_m1),
                                A_reversible=bool(rev)))
    return results


def main():
    print("=== RUN 13 Phases 2+3 ===")
    RES = {"phase2": [], "phase3": []}

    print("--- Phase 2: centering ---")
    Fd = {(1,0): 1.0+0j, (0,1): 0.7+0.3j}
    for p in (101, 211):
        rows = phase2_centered(p, [2,1,1,1], Fd)
        for r in rows:
            RES["phase2"].append(dict(p=p, **r))
            print(f"p={p} m={r['m']}: mu={r['mu_re']:.4f}"
                  f"{r['mu_im']:+.4f}j  "
                  f"Tr2 raw={r['tr2_raw']:.3f} ctr={r['tr2_ctr']:.3f}  "
                  f"Tr4 raw={r['tr4_raw']:.3f} ctr={r['tr4_ctr']:.3f}")

    print("--- Phase 3: two mechanisms ---")
    mech = phase3_two_mechanisms()
    RES["phase3"] = mech
    # Summary table
    disagree = [r for r in mech if r["k_even"] != r["A_reversible"]]
    agree_GUE_GOE_consistent = [
        r for r in mech
        if (r["k_even"] and r["A_reversible"]) or
           (not r["k_even"] and not r["A_reversible"])
    ]
    print(f"total cases: {len(mech)}")
    print(f"k_even == A_reversible cases: "
          f"{sum(1 for r in mech if r['k_even']==r['A_reversible'])}")
    print(f"k_even != A_reversible (DISAGREE): {len(disagree)}")
    for r in disagree[:5]:
        print(f"  DISAGREE: A={r['A']} p={r['p']} k={r['k']} "
              f"k_even={r['k_even']} rev={r['A_reversible']}")

    json.dump(RES, open(os.path.join(ART,"run13_phase23.json"),"w"),
              indent=1, default=str)
    print("saved artifacts/run13_phase23.json")


if __name__ == "__main__":
    main()
