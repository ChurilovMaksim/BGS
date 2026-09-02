"""
RUN 13 / CRITICAL EXPERIMENT: Does the QUANTUM fourth moment Tr(W^4)
see Theta when arithmetic says GUE?

For each (A,p) in the DISAGREEMENT set (A reversible over Z, k=ord_p(alpha)
odd so -1 NOT in H):
  * Arithmetic prediction from resonance count: GUE-type pairing mass.
  * Symmetry intuition: Theta exists -> maybe GOE-type.
Compute the ACTUAL quantum quantity
    Tr[(P_lam W P_lam)^4],   W = V_lam - mu I,
for several eigenspaces and compare against both Wick values.

If Tr(W^4) follows GUE-Wick: "arithmetic beats symmetry" extends to the
quantum observable; title stands.
If it follows GOE-Wick: symmetry wins at the quantum level even though
the resonance counter is blind to Theta; title must change.
"""
import math, os, sys, json
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_core import U_cat
from master_formula_r4 import weyl_matrix, build_V, projector_eigenspace
from master_formula_strong import find_orbit_H

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")


def wick_values(c_abs_sq_list, has_third_pairing):
    """
    Wick predictions for Tr[W^4] given list |c_n|^2 per frequency n.
    GUE (2 pairings): 2*(sum |c|^2)^2
    GOE (3 pairings): 3*(sum |c|^2)^2 - extra term involving sum c_n^2 conj
    We use the simple leading form; boundary corrections are lower order.
    """
    M2 = sum(c_abs_sq_list)
    gue = 2.0 * M2 * M2
    goe = 3.0 * M2 * M2
    return gue, goe


def main():
    print("=== RUN 13 critical experiment ===")
    RES = {"cases": []}

    Fd = {(1, 0): 1.0 + 0j, (0, 1): 0.7 + 0.3j}
    cases = [
        ([2, 1, 1, 1], 101),
        ([2, 1, 1, 1], 199),
        ([2, 1, 1, 1], 211),
        ([5, 2, 2, 1], 199),
    ]
    all_gue, all_goe, undecided = 0, 0, 0
    for (A, p) in cases:
        H = find_orbit_H(p, A)
        if H is None: continue
        k = len(H)
        U = U_cat(A, p)
        V = build_V(Fd, p)
        spaces = projector_eigenspace(U)

        gue_pred, goe_pred = wick_values(
            [abs(complex(c))**2 for c in Fd.values()],
            has_third_pairing=(k % 2 == 0))

        for idx, (lam, Pl, m) in enumerate(spaces[:3]):
            Vl = Pl @ V @ Pl
            mu = complex(np.trace(Vl)) / m
            W = Vl - mu * np.eye(p, dtype=complex)
            tw4 = float(np.real(np.trace(np.linalg.matrix_power(W, 4))))
            d_gue = abs(tw4 - gue_pred)
            d_goe = abs(tw4 - goe_pred)
            closer = "GUE" if d_gue < d_goe else "GOE"
            if closer == "GUE": all_gue += 1
            else: all_goe += 1
            RES["cases"].append(dict(A=A, p=p, m=m, k=k,
                                     trW4=tw4,
                                     gue=gue_pred, goe=goe_pred,
                                     d_gue=d_gue, d_goe=d_goe,
                                     closer=closer))
            print(f"A={A} p={p} mult={m}: Tr[W^4]={tw8:.4f}".format(tw8=tw4)
                  if False else
                  f"A={A} p={p} mult={m}: Tr[W^4]={tw4:9.4f}  "
                  f"GUE={gue_pred:7.3f}(d={d_gue:7.3f})  "
                  f"GOE={goe_pred:7.3f}(d={d_goe:7.3f})  -> {closer}")

    print(f"\nSummary: closer-to-GUE {all_gue}, closer-to-GOE {all_goe}")
    verdict = ("ARITHMETIC/GUE dominates" if all_gue > all_goe else
               "SYMMETRY/GOE dominates" if all_goe > all_goe else
               "MIXED")
    print(verdict)
    json.dump(RES, open(os.path.join(ART, "run13_quantum_w4.json"), "w"),
              indent=1, default=str)
    print("saved artifacts/run13_quantum_w4.json")


if __name__ == "__main__":
    main()
