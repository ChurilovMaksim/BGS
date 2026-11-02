# Debug inert p=11 f=2 "twin" groups: are they mod-11 dihedral lifts?
mod = 121; p = 11
bp = [(1, 0)]
for _ in range(200):
    x, y = bp[-1]
    bp.append(((17*x + 24*y) % mod, (12*x + 17*y) % mod))
    if bp[-1] == (1, 0): break
T = len(bp) - 1
print("ord(beta) mod 121 =", T)
def mul(C, D):
    a, b = C; x, y = D
    return ((a*x + 2*b*y) % mod, (a*y + b*x) % mod)
def cyc(C, n=T):
    return [(2*mul(C, bp[k])[0]) % mod for k in range(n)]
rep = (11, 11); bad = (11, 110)
print("M(rep)==M(bad)?", sorted(cyc(rep)[:6]) == sorted(cyc(bad)[:6]))
# orbit of rep mod 121
orbit = set()
for r in range(T):
    orbit.add(mul(rep, bp[r]))
    orbit.add(mul((rep[0], (-rep[1]) % mod), bp[r]))
print("bad in orbit?", bad in orbit)
# mod-11 relation between (1,1) and (1,10)
bp11 = [(x % p, y % p) for (x, y) in bp]
def mul11(C, D):
    a, b = C; x, y = D
    return ((a*x + 2*b*y) % p, (a*y + b*x) % p)
found = None
for r in range(T):
    if mul11((1, 1), bp11[r]) == (1, 10): found = ("rot", r); break
    if mul11((1, p-1), bp11[r]) == (1, 10): found = ("conj-rot", r); break
print("mod-11 relation (1,10) vs (1,1):", found)
if found:
    kind, r = found
    base = (1, 1) if kind == "rot" else (1, p-1)
    lifted = mul(rep, bp[r])
    print("lifted beta^r * rep mod 121 =", lifted, "vs bad", bad, " diff:", ((lifted[0]-bad[0]) % mod, (lifted[1]-bad[1]) % mod))
    # check: is bad = lam * orbit-element for unit lam?
    for o in orbit:
        if o[0] == 0 and o[1] == 0: continue
        # try lam from first nonzero coord
        for (oi, xi) in ((o[0], bad[0]), (o[1], bad[1])):
            pass
    # brute lam over units mod 121 (110 units) x orbit (<=132): check bad == lam*o
    units = [lam for lam in range(mod) if lam % p != 0]
    hit = [(lam, o) for o in orbit for lam in units if ((lam*o[0]) % mod, (lam*o[1]) % mod) == bad]
    print("bad = lam * orbit-element?", len(hit) > 0, hit[:3])
