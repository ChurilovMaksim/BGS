"""
RUN 16 / r=6 EXTENSION: Count solutions to the sixth-order resonance
system on H^6:
    h1-h2+h3-h4+h5-h6     = 0 mod p
    1/h1-1/h2+1/h3-1/h4+1/h5-1/h6 = 0 mod p
and compare against Wick-pairing predictions.

Wick reference points:
* Number of perfect matchings on 6 labelled slots: (6-1)!! = 15.
* Non-crossing matchings (Catalan C_3): 5.
We test whether sol_6 matches a closed form analogous to r=4.
"""
import os, sys, json, math
import numpy as np
from sympy import primitive_root

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from master_formula_strong import find_orbit_H

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")


def sol6_count(p, H):
    """
    Brute force via meet-in-the-middle on triples.
    Signs: (+,-,+,-,+,-). Slots 1,3,5 positive; slots 2,4,6 negative.
    Left side: slots (1,3,5); Right side: slots (2,4,6).
    Condition: left_sum == right_sum for both components.
    """
    inv = {h: pow(h, p-2, p) for h in H}
    Hlist = sorted(H)
    # Enumerate all triples (x,y,z) of H for LEFT slots
    L = {}
    for h1 in Hlist:
        s1 = h1 % p; t1 = inv[h1]
        for h3 in Hlist:
            s13 = (s1 + h3) % p
            t13 = (t1 + inv[h3]) % p
            for h5 in Hlist:
                kk = ((s13+h5)%p, (t13+inv[h5])%p)
                L[kk] = L.get(kk,0)+1
    total = 0
    for h2 in Hlist:
        s2 = (-h2)%p; t2 = (-inv[h2])%p
        for h4 in Hlist:
            s24 = (s2 - h4)%p
            t24 = (t2 - inv[h4])%p
            for h6 in Hlist:
                kk = ((s24-h6)%p, (t24-inv[h6])%p)
                if kk in L:
                    total += L[kk]
    return total


def main():
    print("=== RUN 16: r=6 resonance ===")
    results = []
    test_cases = []
    for p in (101, 211, 401):
        g = int(primitive_root(p))
        ks = [d for d in range(3, min(30,p)) if (p-1)%d==0][:5]
        for k in ks:
            alpha=pow(g,(p-1)//k,p)
            H=set(); x=1
            for _ in range(k): H.add(x); x=x*alpha%p
            s6=sol6_count(p,H)

            # Wick references for r=6
            n_matchings_total = math.factorial(6)//(2**3 * math.factorial(3))  # 15
            n_catalan_C3 = 5
            # naive scaling guesses
            guess_A = 15 * k**3   # if each pairing contributes ~k choices per pair-slot triple
            guess_B = 15 * k**2   # alternative normalisation

            results.append(dict(p=p,k=k,sol6=s6,
                                guessA=guess_A, guessB=guess_B))
            ratio_A = s6/guess_A if guess_A>0 else 0
            print(f"p={p} k={k}: sol_6={s6}, "
                  f"15k^3={guess_A} (ratio {ratio_A:.3f}), "
                  f"15k^2={guess_B}")

    json.dump(results, open(os.path.join(ART,"run16_r6.json"),"w"), indent=1)
    print("saved artifacts/run16_r6.json")


if __name__=="__main__":
    main()
