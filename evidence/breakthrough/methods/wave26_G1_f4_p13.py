"""Wave 26, task 1 (part 2): (2,2) mechanism at p=13, mod 13^4.
- L0, k, Tr(u) mod 13 (decides whether v=2 singletons can exist for unit C).
- Lemma 5 shapes for k=2 (linear regime): expect 0 violations on samples.
- v=1 coset invariance under Tr(eta)=0 mod 13 twist.
- v=2 singleton shift formula S_C = c*w0 + Tr(eta0*C1) + c*Tr(eta1) (mod 13),
  shift = 2197*S_C; w0 = Tr(eta0)/13 mod 13.
- At most one singleton per trace value t across all classes (sampled A).
"""
import random
from collections import Counter

def add(x, y, P): return ((x[0]+y[0]) % P, (x[1]+y[1]) % P)
def mul(x, y, P): return ((x[0]*y[0]+2*x[1]*y[1]) % P, (x[0]*y[1]+x[1]*y[0]) % P)
def tr(x, P): return (2*x[0]) % P
def pw(x, n, P):
    r = (1, 0)
    while n:
        if n & 1: r = mul(r, x, P)
        x = mul(x, x, P); n >>= 1
    return r
def vp_int(n, p):
    if n == 0: return 99
    v = 0
    while n % p == 0:
        n //= p; v += 1
    return v

ALPHA = (3, 2); p = 13; P = p**4; L0 = 14; k = 2; s = 2
Pbig = P * (p**k)
gb = pw(ALPHA, L0, Pbig)
u_big = (((gb[0]-1) % Pbig)//(p**k), (gb[1] % Pbig)//(p**k))
u = (u_big[0] % P, u_big[1] % P)
g = pw(ALPHA, L0, P)
print("gamma mod P:", g, "order 169:", pw(g, 169, P) == (1, 0), "gamma^13 != 1:", pw(g, 13, P) != (1, 0))
print("u mod P:", u, "Tr(u) mod 13:", tr(u, P) % p, "Tr(u) mod 169:", tr(u, P) % (p**2))
print("169*u mod P == gamma-1:", ((169*u[0]) % P, (169*u[1]) % P) == ((g[0]-1) % P, g[1] % P))
print("gamma-1 coeffs mod P:", ((g[0]-1) % P, g[1] % P),
      "vp:", vp_int((g[0]-1) % P, p), vp_int(g[1] % P, p))

gps = [pw(g, j, P) for j in range(p**s)]
random.seed(1)
viol = 0; cnt = Counter()
for trial in range(400):
    if trial % 2 == 0:
        C = (random.randrange(P), random.randrange(P))
    else:
        c = random.randrange(1, p)
        C = ((c + p*random.randrange(p**3)) % P, (p*random.randrange(p**3)) % P)
    F = Counter(tr(mul(C, gj, P), P) for gj in gps)
    T1 = tr(mul(C, u, P), P); v = vp_int(T1, p)
    if v >= s: ok = (len(F) == 1)
    else:
        step = p**(k+v); size = p**(s-v)
        ok = (len(F) == size and all(c_ == p**v for c_ in F.values())
              and all((x - tr(C, P)) % step == 0 for x in F))
    cnt[(v, len(F))] += 1
    if not ok:
        viol += 1
        if viol <= 3: print("  SHAPE VIOLATION C,v,F:", C, v, dict(F))
print(f"Lemma5 shapes p=13 (400 samples): violations={viol}, (v,|F|)={dict(cnt)}")

# Twist checks, general eta0 with Tr(eta0) = 0 mod 13 (eta0 = (13*a0, b))
bad1 = 0; n1 = 0; bad2 = 0; n2 = 0
for trial in range(300):
    c = random.randrange(1, p)
    C = ((c + p*random.randrange(p**3)) % P, (p*random.randrange(p**3)) % P)
    eta0 = ((p*random.randrange(p), random.randrange(p**2)))
    eta1 = (random.randrange(p), random.randrange(p))
    eta = add(eta0, mul((p, 0), eta1, P), P)
    Cp = mul(C, add((1, 0), mul((p**k, 0), eta, P), P), P)
    F = Counter(tr(mul(C, gj, P), P) for gj in gps)
    Fp = Counter(tr(mul(Cp, gj, P), P) for gj in gps)
    T1 = tr(mul(C, u, P), P); v = vp_int(T1, p)
    if v == 1:
        n1 += 1
        if F != Fp: bad1 += 1
    if v >= 2:
        n2 += 1
        C1 = (((C[0]-c)//p) % p, (C[1]//p) % p)
        w0 = (tr(eta0, P)//p) % p
        S = (c*w0 + tr(mul(eta0, C1, p), p) + c*tr(eta1, p)) % p
        pred = (2197 * S) % P
        actual = (tr(Cp, P) - tr(C, P)) % P
        if actual != pred: bad2 += 1
print(f"twist: v=1 invariance tested={n1} bad={bad1}; v=2 shift formula tested={n2} bad={bad2}")

# At most one singleton per trace value t across classes, sampled A.
# Classes r mod 2; H0 = <alpha^(2*169)> mod P, order 7; class r = disjoint union
# over z in H0 of F(A*alpha^r*z) (rho=1 since m = t*|H|).
H0 = [pw(mul(pw(ALPHA, 2, P), pw(ALPHA, 0, P), P), 0, P)]  # placeholder replaced below
H0 = [pw(ALPHA, 338*j, P) for j in range(7)]
print("H0 order check:", len(set(H0)), "alpha^2 order:", )
random.seed(3)
viol_t = 0; sing_tot = 0; As_with_sing = 0
for trial in range(200):
    A = (random.randrange(P), random.randrange(P))
    per_t = Counter()
    for r in range(2):
        for z in H0:
            C = mul(mul(A, pw(ALPHA, r, P), P), z, P)
            T1 = tr(mul(C, u, P), P); v = vp_int(T1, p)
            if v >= 2:
                sing_tot += 1
                per_t[tr(C, P) % p] += 1
    if sing_tot > 0 and trial < 200: pass
    if per_t and max(per_t.values()) > 1:
        viol_t += 1
    if per_t: As_with_sing += 1
print(f"singleton per-t: sampled A=200, A with >=1 singleton={As_with_sing}, "
      f"total singletons={sing_tot}, violations(>1 per t)={viol_t}")
