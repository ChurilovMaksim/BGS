import math, sys
sys.setrecursionlimit(10000)

def beta_uv(m):
    # beta^m = u + v*sqrt(2), via u_{n+1} = 6u_n - u_{n-1}
    if m == 0: return (1, 0)
    u_prev, u = 1, 3  # u_0, u_1
    v_prev, v = 0, 2
    for _ in range(1, m):
        u_prev, u = u, 6*u - u_prev
        v_prev, v = v, 6*v - v_prev
    return (u, v)

def Dm(m):
    u, _ = beta_uv(m)
    return abs(2 - 2*u)

def vp(n, p):
    c = 0
    while n % p == 0:
        n //= p; c += 1
    return c

def beta_mod(r, p):
    u, v = 1 % p, 0
    for _ in range(r):
        u, v = (3*u + 4*v) % p, (2*u + 3*v) % p
    return (u, v)

def order_beta(p, rmax=200):
    # exact order of beta mod p (beta^r == 1 iff u==1, v==0)
    u, v = 1 % p, 0
    for r in range(1, rmax+1):
        u, v = (3*u + 4*v) % p, (2*u + 3*v) % p
        if u == 1 and v == 0:
            return r
    return None

def mat_pow_mod(M, e, q):
    def mul(A, B):
        return [(A[0]*B[0]+A[1]*B[2])%q, (A[0]*B[1]+A[1]*B[3])%q,
                (A[2]*B[0]+A[3]*B[2])%q, (A[2]*B[1]+A[3]*B[3])%q]
    R = [1,0,0,1]; B = M[:]
    while e:
        if e & 1: R = mul(R, B)
        B = mul(B, B); e >>= 1
    return R

def N_det(m, p):
    # M^m mod p^2, N = (M^m - I)/p mod p, return det(N) mod p
    Mm = mat_pow_mod([6, -1 % (p*p), 1, 0], m, p*p)
    a = (Mm[0]-1) % (p*p); b = Mm[1] % (p*p); c = Mm[2] % (p*p); d = (Mm[3]-1) % (p*p)
    assert a % p == 0 and b % p == 0 and c % p == 0 and d % p == 0, (m, p, Mm)
    N = [(a//p) % p, (b//p) % p, (c//p) % p, (d//p) % p]
    return (N[0]*N[3] - N[1]*N[2]) % p

# --- D values and valuations ---
for m in (35, 360, 1260):
    print(f"D_{m} digits: {len(str(Dm(m)))}")
print("v41(D360) =", vp(Dm(360), 41), " v41(D1260) =", vp(Dm(1260), 41))
print("v239(D1260) =", vp(Dm(1260), 239))
# D_35 factorization
from sympy import factorint
d35 = Dm(35)
print("D_35 =", d35)
f35 = factorint(d35)
print("D_35 factors:", f35)
d5, d7, d1 = Dm(5), Dm(7), Dm(1)
print("D_1 =", d1, "D_5 =", d5, "D_7 =", d7)
prim35 = d35 * d1 // (d5 * d7 // d1)  # primitive part P_35 = D35*D1/(D5*D7)?? check integrality
print("D35*D1 =", d35*d1, " D5*D7 =", d5*d7, " ratio:", (d35*d1)//(d5*d7), " exact:", (d35*d1) % (d5*d7) == 0)
P35 = (d35*d1)//(d5*d7) if (d35*d1) % (d5*d7) == 0 else None
if P35: print("P_35 =", P35, " factors:", factorint(P35))
# orders of primitive prime candidates
for p in ([41, 239] + (list(factorint(P35).keys()) if P35 else [])):
    print(f"ord_{p}(beta) =", order_beta(p), " v_p(D1260) =", vp(Dm(1260), p))
# reduction hypotheses for each (m,p,r)
for (m, p, r) in [(360, 41, 5), (1260, 41, 5), (1260, 239, 7)] + ([(1260, p, 35) for p in (list(factorint(P35).keys()) if P35 else [])]):
    print(f"(m={m}, p={p}, r={r}): r|m={m % r == 0}, p|(m/r)={ (m//r) % p == 0 }, detN mod p = {N_det(m, p)} (nonzero={N_det(m,p) != 0})")
