from math import gcd
from sympy import factorint

def rad(n):
    r = 1
    for p in factorint(n):
        r *= p
    return r

def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c

x, y = 1, 0
for m in range(1, 31):
    x, y = 3 * x + 8 * y, x + 3 * y
    A = x - 1
    D = 2 * A
    g = A // gcd(A, y)
    assert x * x - 8 * y * y == 1, m
    assert rad(D) == rad(g), (m, D, g)
    va, vy = v2(A), v2(y)
    assert va == (1 if m % 2 == 1 else 2 + 2 * vy), (m, va, vy)
    assert v2(g) == (1 if m % 2 == 1 else 2 + vy), (m, v2(g))
print("rad + v2 checks PASS m=1..30")
