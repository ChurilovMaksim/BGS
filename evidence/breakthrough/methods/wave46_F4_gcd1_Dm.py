# D_m = |det(M^m - I)|, M = [[6,-1],[1,0]]; beta^m = u + v*sqrt(2), D_m = |2 - 2u|
def beta_pow(m):
    u, v = 1, 0
    for _ in range(m):
        u, v = 3*u + 4*v, 2*u + 3*v
    return u, v
def Dm(m):
    u, _ = beta_pow(m)
    return abs(2 - 2*u)
# verify known values
known = {3:196, 4:1152, 5:6724, 6:39200, 7:228484}
for m, val in known.items():
    d = Dm(m)
    print(f"D_{m} = {d} match={d==val}")
# D_36 factorization check (wave44: 128*729*25*49*121*5329*32041*38809*39601)
import math
d36 = Dm(36)
prod = 128*729*25*49*121*5329*32041*38809*39601
print("D_36 match wave44:", d36 == prod, "digits:", len(str(d36)))
# D_84 factorization check (wave42)
d84 = Dm(84)
prod84 = 2**7*3**4*5**2*7**4*11**2*13**4*83**2*113**2*239**2*251**2*337**2*4663**2*75937**2*45697**2
print("D_84 match wave42:", d84 == prod84)
# sizes
for m in (72, 108, 144, 180, 252):
    print(f"D_{m} digits:", len(str(Dm(m))))
# valuations v_41(D_180), v_239(D_252) by exact division
def vp(n, p):
    c = 0
    while n % p == 0:
        n //= p; c += 1
    return c
d180 = Dm(180); d252 = Dm(252)
print("v41(D180) =", vp(d180, 41), " v239(D252) =", vp(d239, 239) if False else vp(d252, 239))
print("v5(D180) =", vp(d180, 5), " v7(D252) =", vp(d252, 7), " v3(D108) =", vp(Dm(108), 3))
# beta orders mod p: beta^r == 1 in Z[sqrt2]/(p) iff u_r % p == 1 and v_r % p == 0
def beta_mod(m, p):
    u, v = 1 % p, 0
    for _ in range(m):
        u, v = (3*u + 4*v) % p, (2*u + 3*v) % p
    return u, v
print("beta^5 mod 41:", beta_mod(5, 41), " beta^7 mod 239:", beta_mod(7, 239), " beta^4 mod 3:", beta_mod(4, 3))
# divisors of m coprime to 36
def divs(m):
    return [d for d in range(1, m+1) if m % d == 0]
for m in (36, 72, 108, 144, 180, 252):
    cop = [d for d in divs(m) if math.gcd(d, 36) == 1]
    print(f"m={m}: divisors coprime to 36: {cop}")
