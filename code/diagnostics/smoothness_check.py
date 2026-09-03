"""
RUN 10 / smoothness spot-check of V on actual solutions.
At each sampled solution verify Jacobian rows (lam) and (-mu_i/x_i^2)
are NOT proportional over F_p (rank 2 = smooth point).
Artifact: artifacts/smoothness_check.json
"""
import json, os
import numpy as np

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")
rng = np.random.default_rng(1717)


def count_and_check(p, lam, mu, max_check=300):
    xs = np.arange(1, p, dtype=np.int64)
    inv = np.array([pow(int(x), p - 2, p) for x in xs], dtype=np.int64)

    K12a = (lam[0] * xs[:, None] + lam[1] * xs[None, :]) % p
    K12b = (mu[0] * inv[:, None] + mu[1] * inv[None, :]) % p
    key12 = (K12a * p + K12b).ravel()
    del K12a, K12b
    K34a = ((p - lam[2]) * xs[:, None] + (p - lam[3]) * xs[None, :]) % p
    K34b = ((p - mu[2]) * inv[:, None] + (p - mu[3]) * inv[None, :]) % p
    key34 = (K34a * p + K34b).ravel()
    del K34a, K34b

    order12 = np.argsort(key12)
    key12s = key12[order12]
    d12 = {}
    for idx in order12:
        k = int(key12[idx])
        d12.setdefault(k, [])
        if len(d12[k]) < max_check:
            d12[k].append(int(idx))

    checked = singular = 0
    key34set = set(int(x) for x in key34)
    for kk, lst in list(d12.items()):
        if kk not in key34set:
            continue
        matches = np.where(key34 == kk)[0]
        step = max(1, len(matches))
        for pos, i1x in enumerate(lst):
            jpair = int(matches[(pos * step) % len(matches)])
            i1 = i1x // p          # x1 index
            i3 = i1x % p           # x3 index
            j3 = jpair // p        # x2 index
            j4 = jpair % p         # x4 index
            if checked >= max_check:
                break
            checked += 1
            x1, x2, x3, x4 = (int(xs[i1]), int(xs[j3]),
                              int(xs[i3]), int(xs[j4]))
            J1 = [lam[t] for t in range(4)]
            J2 = [(-mu[t] * pow(x, p - 2, p) ** 2) % p
                  for t, x in enumerate((x1, x2, x3, x4))]
            nz = [t for t in range(4) if J1[t] % p]
            prop = True
            if not nz:
                prop = False
            else:
                t0 = nz[0]
                invJ = pow(J1[t0], p - 2, p)
                tt = (J2[t0] * invJ) % p
                for q in range(4):
                    if (J2[q] - tt * J1[q]) % p != 0:
                        prop = False
                        break
            if prop:
                singular += 1
        if checked >= max_check:
            break
    return {"checked": checked, "singular": singular}


def main():
    out = []
    for p in (2053, 4099):
        lam = [int(v) for v in rng.integers(1, p, size=4)]
        mu = [int(v) for v in rng.integers(1, p, size=4)]
        r = count_and_check(p, lam, mu)
        ok = r["singular"] == 0 and r["checked"] > 0
        r.update({"p": p, "pass": bool(ok)})
        out.append(r)
        print(f"p={p}: checked={r['checked']} singular={r['singular']} "
              f"[{'PASS' if ok else 'FAIL'}]")
    json.dump(out, open(os.path.join(ART, "smoothness_check.json"), "w"),
              indent=1)
    print("saved artifacts/smoothness_check.json")


main()
