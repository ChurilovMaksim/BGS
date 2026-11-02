# Wave 47x task B: reproduce mod-49 twin, sigma profiles, admissibility.
p, f = 7, 2
mod = p**f  # 49
# sqrt(2) mod 49: r=10 (10^2=100=2 mod 49)
r = 10
assert (r*r - 2) % mod == 0
b = (17 + 12*r) % mod          # beta first component
bi = (17 - 12*r) % mod         # beta second component = b^{-1}
assert (b*bi) % mod == 1
print("b =", b, "ord(b) =", end=" ")
o = 1; x = b
while x != 1:
    x = x*b % mod; o += 1
print(o)
def cycle(c1, c2):
    # t_k = c1*b^k + c2*b^{-k}, k=0..ord-1; return period + values
    bp = [1]*o; bm = [1]*o
    for k in range(1, o):
        bp[k] = bp[k-1]*b % mod; bm[k] = bm[k-1]*bi % mod
    t = [(c1*bp[k] + c2*bm[k]) % mod for k in range(o)]
    # minimal period (divides o)
    import math
    per = o
    for d in range(1, o+1):
        if o % d == 0 and all(t[k] == t[k % d] for k in range(o)):
            per = d; break
    return per, t[:per]
# C = 1+2sqrt2 -> (1+2r, 1-2r) = (21, 30); D = 1+5sqrt2 -> (2, 0); D' mirror = (0, 2)
C = (21, 30); D = (2, 0); Dp = (0, 2)
for name, (c1, c2) in [("C", C), ("D", D), ("D'", Dp)]:
    per, t = cycle(c1, c2)
    print(name, "comp", (c1, c2), "period", per, "distinct", len(set(t)), "multiset==C?", end=" ")
    print()
perC, tC = cycle(*C)
perD, tD = cycle(*D)
perDp, tDp = cycle(*Dp)
print("M(C)==M(D):", sorted(tC) == sorted(tD), " M(C)==M(D'):", sorted(tC) == sorted(tDp))
print("C values:", tC)
print("D values:", tD)
print("D' values:", tDp)
# sigma: t'_k = t_{sigma(k)} (t distinct -> well-defined)
idx = {v: k for k, v in enumerate(tC)}
def sigma(tprime):
    return [idx[v] for v in tprime]
sD = sigma(tD); sDp = sigma(tDp)
print("sigma_D :", sD)
print("sigma_D':", sDp)
for name, s in [("D", sD), ("D'", sDp)]:
    for g in (3, 7, 21):
        ok = all(s[k] % g == k % g for k in range(21))
        print(f"  {name}: sigma(k)==k mod {g} for all k? {ok}")
    # anti-diagonal mod 3?
    okm = all((s[k] + k) % 3 == 0 for k in range(21))
    print(f"  {name}: sigma(k)==-k mod 3 for all k? {okm}")
# alpha admissibility: alpha = 3+2sqrt2 -> (3+2r, 3-2r)
a1 = (3 + 2*r) % mod; a2 = (3 - 2*r) % mod
def order(x):
    o = 1; y = x
    while y != 1:
        y = y*x % mod; o += 1
    return o
print("alpha comps:", a1, a2, "orders:", order(a1), order(a2))
oal = order(a1)*order(a2)//__import__('math').gcd(order(a1), order(a2))
print("ord(alpha) mod 49 =", oal, "even?", oal % 2 == 0)
# check alpha^u == -1 solvable: need u with (a1^u, a2^u) == (48, 48)
sol = [u for u in range(1, 200) if pow(a1, u, mod) == 48 and pow(a2, u, mod) == 48]
print("u with alpha^u == -1 mod 49:", sol[:5], "count<200:", len(sol))
