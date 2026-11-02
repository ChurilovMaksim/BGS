# Pell analysis: beta=(1+sqrt2), beta^n = a_n + b_n*sqrt2.
# beta^64 = 1 mod q  <=>  q | gcd(a64-1, b64) = 2*b32 (proved in note).
# Among prime divisors of b32: beta^32 = 1 iff q | (a32-1); =-1 iff q | (a32+1).
a, b = 1, 0
for _ in range(32):
    a, b = a + 2*b, a + b
a32, b32 = a, b
print("a32 =", a32, " b32 =", b32)
print("check a32^2-2*b32^2 =", a32*a32 - 2*b32*b32)
print("a32-1 =", a32-1, " a32+1 =", a32+1)
print("gcd(a32-1, b32) =", __import__('math').gcd(a32-1, b32))
print("gcd(a32+1, b32) =", __import__('math').gcd(a32+1, b32))
try:
    from sympy import factorint
    f = factorint(b32)
    print("factor b32:", f)
    for p in sorted(f):
        print(f"  p={p}: divides a32-1? {(a32-1)%p==0}  divides a32+1? {(a32+1)%p==0}")
except ImportError:
    print("no sympy; b32 =", b32)
