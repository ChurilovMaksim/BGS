"""
RUN 9 / END-TO-END CERTIFICATION of the character-expansion reduction:

    #sol(S_F) = p^-2 [ k^4 + (k/(p-1))^4 * sum_{chi_vec in X^4} C(chi_vec) ]

    C(chi_vec) = sum_(u,v)!=0 prod_i Ktilde_{chi_i}(lambda_i u, mu_i v)
    lambda_i = a_i/a_1, mu_i = b_i/b_1,
    Ktilde_chi(t,s) = sum_x chi(x) e_p(t x + s/x),
    chi in X = chars of F_p^x trivial on H = <alpha> (|X| = (p-1)/k).

Compared against direct brute-force counting over H^4. Exact arithmetic.
Artifact: artifacts/char_expansion_cert.json
"""
import json, math, os, sys
from collections import Counter
import numpy as np
from sympy import isprime, primitive_root

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")


def char_tables(p, g, m):
    tabs = []
    for j in range(m):
        tab = np.zeros(p - 1, dtype=np.complex128)
        x = 1
        for t in range(p - 1):
            tab[x - 1] = np.exp(2j * math.pi * (j * t % m) / m)
            x = x * g % p
        tabs.append(tab)
    return tabs


def kloosterman_char_table(p, chi_tab):
    xs = np.arange(1, p, dtype=np.int64)
    inv = np.array([pow(int(x), p - 2, p) for x in xs], dtype=np.int64)
    T = np.zeros((p, p), dtype=np.complex128)
    for s in range(p):
        vec = np.zeros(p, dtype=np.complex128)
        if s == 0:
            vec[1:] = chi_tab
        else:
            vec[1:] = chi_tab * np.exp(2j * np.pi * (s * inv % p) / p)
        T[s, :] = np.conj(np.fft.fft(np.conj(vec)))
    return T


def brute_solutions(p, A, B, H):
    inv = {h: pow(h, p - 2, p) for h in H}
    a1, a2, a3, a4 = A
    b1, b2, b3, b4 = B
    L = Counter()
    for h1 in H:
        s1 = a1 * h1 % p
        t1 = b1 * inv[h1] % p
        for h3 in H:
            L[(s1 + a3 * h3) % p, (t1 + b3 * inv[h3]) % p] += 1
    tot = 0
    for h2 in H:
        s2 = a2 * h2 % p
        t2 = b2 * inv[h2] % p
        for h4 in H:
            key = ((s2 + a4 * h4) % p, (t2 + b4 * inv[h4]) % p)
            if key in L:
                tot += L[key]
    return tot


def run_case(p, k, labels):
    A, B = labels
    g = int(primitive_root(p))
    alpha = pow(g, (p - 1) // k, p)
    H = []
    x = 1
    for _ in range(k):
        H.append(x)
        x = x * alpha % p
    assert len(set(H)) == k
    m = (p - 1) // k

    tabs = char_tables(p, g, m)
    KT = [kloosterman_char_table(p, tb) for tb in tabs]

    ipA0 = pow(A[0], p - 2, p)
    ipB0 = pow(B[0], p - 2, p)
    eps = [1, -1, 1, -1]                      # sign pattern (+,-,+,-)
    # lambda_i = eps_i*a_i/a_1 : signs do NOT cancel (only eps_1 = +1)
    lams = [(eps[i] * A[i]) * ipA0 % p for i in range(4)]
    mus = [(eps[i] * B[i]) * ipB0 % p for i in range(4)]

    us = np.arange(p)
    cols = [(lam * us) % p for lam in lams]

    total_C = 0.0 + 0.0j
    # precompute per-char per-row selections lazily via fancy indexing:
    # for each char j and each v: row vector R_j[v][t] = KT[j][(mu_j v)%p, t]
    # sel[slot][char][v] : row vector over t of Ktilde_{chi_j}(lam_slot u, mu_slot v)
    # AXES INCLUDED: v and u run over ALL of F_p; the (0,0) term is
    # subtracted afterwards (only the all-trivial char-quadruple survives
    # there, giving (p-1)^4).
    sel = [[[KT[j][(mus[sl] * v) % p, :] for v in range(p)]
            for j in range(m)] for sl in range(4)]

    c0, c1, c2, c3 = cols
    for j1 in range(m):
        S1 = sel[0][j1]
        for j2 in range(m):
            S2 = sel[1][j2]
            P12 = [S1[v][c0] * S2[v][c1] for v in range(p)]
            for j3 in range(m):
                S3 = sel[2][j3]
                P123 = [P12[v] * S3[v][c2] for v in range(p)]
                for j4 in range(m):
                    S4 = sel[3][j4]
                    acc = 0.0 + 0.0j
                    for vv in range(p):
                        acc += complex(np.sum(P123[vv] * S4[vv][c3]))
                    total_C += acc

    # remove the (u,v)=(0,0) term: only all-trivial chi_vec contributes (p-1)^4
    total_C -= (p - 1) ** 4
    bf = brute_solutions(p, A, B, H)
    lhs = p ** 2 * bf - k ** 4
    prefac = (k / (p - 1)) ** 4
    rhs = prefac * total_C
    err = abs(lhs - float(np.real(rhs))) / max(abs(lhs), 1e-300)
    print(f"p={p} k={k}: brute={bf} lhs={lhs:.6e} "
          f"Re(rhs)={float(np.real(rhs)):.6e} rel_err={err:.2e}", flush=True)
    return {"p": p, "k": k, "labels": [list(A), list(B)], "brute": int(bf),
            "rel_err": float(err), "passed": bool(err < 1e-9)}


def main():
    out = {"cases": []}
    allpass = True
    cases = [
        (41, 8, ((1, 1, 1, 1), (1, 1, 1, 1))),
        (41, 8, ((1, 2, 3, 4), (5, 6, 7, 8))),
        (73, 9, ((1, 1, 2, 3), (1, 4, 5, 6))),
    ]
    for (p, k, labels) in cases:
        if not isprime(p) or (p - 1) % k != 0:
            print(f"[SKIP] p={p}, k={k}")
            continue
        rec = run_case(p, k, labels)
        out["cases"].append(rec)
        allpass &= rec["passed"]
    out["all_pass"] = bool(allpass and len(out["cases"]) >= 2)
    json.dump(out, open(os.path.join(ART, "char_expansion_cert.json"), "w"),
              indent=1)
    print("ALL PASS" if out["all_pass"] else "SOME FAIL")
    print("saved artifacts/char_expansion_cert.json")


if __name__ == "__main__":
    main()
