"""Wave 7 task 3: does omega distinguish w-classes?

Question: for xi, xi' in ONE fiber (same sorted multiset y, hence same
mode values) but with different sorted(w), w = (H*y)/D, does the
omega factor in the orbit-pair formula differ?

Main definitions used (fetched via GitHub connector at pinned HEAD
d87dce0d9277579568edfee6cffecbc96ea61024, NOT from local copies):
  band_limited_kick_bridge.md D3:
    Psi_m(s/D) = sum_{xi,xi'} phihat_s(xi) conj(phihat_s(xi'))
                 prod_k omega_k(eta * (S_k(xi) - S_k(xi'))),
    S_k(xi) = sum_j e(k * xi_j),  omega = J0(a|z|) or exp(-a^2|z|^2/4).
  LineDStrongKick.lean pairTerm:
    pairTerm = phi s xi * star(phi s xi') * prod_k omega k (eta*(S xi k - S xi' k)).
  LineDStrongKickConc.lean gaussOmega:
    gaussOmega a k z = exp(-(a k * z)^2 / 4)  (real z; complex form
    exp(-a^2|z|^2/4) in the source doc).

Test vectors (prior-wave data, workspace only; definitions above are
from main, vectors are just inputs):
  m=8: first example of M08_BAD_M8.json (y, y_prime, same sorted key,
       different Gamma-orbits: fiber 32 = 16 + 16).
  m=12: counterexample pair of sep_m12_pair_result.json (y, y').
Control: a vector from a different fiber (different sorted multiset).

Mode sums are computed independently for each vector as
  S_k(y) = sum_j exp(2*pi*i*k*y_j/D),  k = 1..m,
NOT by assuming multiset equality: the test is that the independently
computed sums come out equal (up to float rounding), hence Delta = 0,
hence omega = 1 at every eta, for both the Gaussian and J0 forms.
"""
import cmath
import json
import math

BASE = "/home/hatch/workspace/bgs-breakthrough/methods/"

def H_times(y):
    m = len(y)
    return [6 * y[i] - y[(i - 1) % m] - y[(i + 1) % m] for i in range(m)]

def w_of(y, D):
    Hy = H_times(y)
    assert all(v % D == 0 for v in Hy), "y not in Fix (Hy not divisible by D)"
    return [v // D for v in Hy]

def mode_sums(y, D, ks):
    m = len(y)
    out = {}
    for k in ks:
        s = 0j
        for v in y:
            s += cmath.exp(2j * math.pi * k * v / D)
        out[k] = s
    return out

def gauss_factor(delta, eta, a=1.0):
    # source complex form exp(-a^2 |z|^2 / 4), z = eta * delta
    return math.exp(-(a * eta * abs(delta)) ** 2 / 4.0)

def report_pair(name, m, D, y, yp):
    print(f"--- {name} (m={m}, D={D}) ---")
    print("sorted(y) == sorted(y'):", sorted(y) == sorted(yp))
    wy, wyp = sorted(w_of(y, D)), sorted(w_of(yp, D))
    print("w(y)      =", w_of(y, D))
    print("w(y')     =", w_of(yp, D))
    print("sorted(w) equal:", wy == wyp, "| sorted(w) y =", wy, "| y' =", wyp)
    ks = list(range(1, m + 1))
    Sy, Syp = mode_sums(y, D, ks), mode_sums(yp, D, ks)
    max_delta = 0.0
    for k in ks:
        d = abs(Sy[k] - Syp[k])
        max_delta = max(max_delta, d)
    print(f"max |Delta S_k| over k=1..{m}: {max_delta:.3e}")
    for eta in (0.0, 1.0, 5.0, 20.0, 100.0):
        # omega factor = prod_k omega_k(eta * Delta_k); with Delta=0 it is 1
        # (Gaussian: exp(0)=1; J0: J0(0)=1 by definition of the Bessel function)
        fac = 1.0
        for k in ks:
            fac *= gauss_factor(Sy[k] - Syp[k], eta)
        print(f"  eta={eta:6.1f}: Gaussian omega-factor = {fac:.12f}  (J0 factor = 1 exactly at Delta=0)")
    print()
    return max_delta, wy == wyp

# m = 8 bad fiber
m8 = json.load(open(BASE + "M08_BAD_M8.json"))
ex = m8["examples"][0]
assert m8["m"] == 8 and m8["D"] == 1331712
d8, w_eq8 = report_pair("m=8 first bad fiber", 8, 1331712, ex["y"], ex["y_prime"])

# m = 12 counterexample pair (vectors from the wave-4 gluing note,
# gluing_m12_counterexample.py, re-verified there: Hy = Hy' = 0 mod D,
# sorted multisets equal, affine canons distinct). Cross-checked here:
# their w vectors must match sep_m12_pair_result.json exactly.
m12 = json.load(open(BASE + "sep_m12_pair_result.json"))
y12 = (1366041600, 1366041600, 683020800, 1195286400, 341510400, 853776000,
       170755200, 170755200, 853776000, 341510400, 1195286400, 683020800)
yp12 = (1366041600, 1195286400, 1195286400, 1366041600, 853776000, 683020800,
        170755200, 341510400, 341510400, 170755200, 683020800, 853776000)
assert w_of(list(y12), 1536796800) == m12["y"]["w"]
assert w_of(list(yp12), 1536796800) == m12["y_prime"]["w"]
d12, w_eq12 = report_pair("m=12 counterexample pair", 12, 1536796800,
                          list(y12), list(yp12))

# Control: different fiber -> Delta != 0, Gaussian factor decays with eta
print("--- control: different fibers (m=8, y vs rotated-by-1 vector) ---")
y_ctrl = ex["y"]
yp_ctrl = [(v + 55488) % 1331712 for v in ex["y"]]  # shift breaks the multiset
print("sorted equal:", sorted(y_ctrl) == sorted(yp_ctrl))
Sy = mode_sums(y_ctrl, 1331712, range(1, 9))
Syp = mode_sums(yp_ctrl, 1331712, range(1, 9))
deltas = {k: abs(Sy[k] - Syp[k]) for k in range(1, 9)}
print("Delta_k:", {k: round(v, 4) for k, v in deltas.items()})
for eta in (1.0, 5.0, 20.0):
    fac = 1.0
    for k in range(1, 9):
        fac *= gauss_factor(Sy[k] - Syp[k], eta)
    print(f"  eta={eta:5.1f}: Gaussian omega-factor = {fac:.6e}")

print()
print("SUMMARY")
print(f"  m=8 : max|Delta| = {d8:.3e}, sorted(w) equal = {w_eq8}")
print(f"  m=12: max|Delta| = {d12:.3e}, sorted(w) equal = {w_eq12}")
print("  Verdict: omega factor is 1 at every eta within a fiber, for both")
print("  the Gaussian and J0 forms, even when sorted(w) differs.")
print("  Hence omega does NOT distinguish w-classes; route (a) for P_w fails.")
