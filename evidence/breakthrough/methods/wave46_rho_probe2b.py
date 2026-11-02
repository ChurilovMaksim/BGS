ALPHA = (3, 2)
def mul(a, b, M): return ((a[0]*b[0]+2*a[1]*b[1]) % M, (a[0]*b[1]+a[1]*b[0]) % M)
def pw(a, n, M):
    r = (1, 0)
    while n:
        if n & 1: r = mul(r, a, M)
        a = mul(a, a, M); n >>= 1
    return r
print("alpha^16 mod 8192:", pw(ALPHA, 16, 8192), "alpha^32 mod 8192:", pw(ALPHA, 32, 8192))
def primes(n):
    s = bytearray(b'\x01')*(n+1); s[0:2] = b'\x00\x00'
    for i in range(2, int(n**0.5)+1):
        if s[i]:
            s[i*i:n+1:i] = b'\x00'*(((n - i*i)//i)+1)
    return [i for i in range(n+1) if s[i]]
found = []
for q in primes(50000):
    if pw(ALPHA, 32, q) == (1,0) and pw(ALPHA, 16, q) != (1,0):
        found.append((q, pw(ALPHA, 16, q)))
print("order-32-alpha primes <=50000:", found, "count:", len(found))
