"""Independent finite certificate for a nonunit endpoint Fourier minor.

No numerical roots or eigenvalues are used.  This checks a single example;
the general p-adic valuation theorem is proved separately in prose.
"""
from itertools import permutations

MOD = 5


def trim(a):
    a = [int(x) % MOD for x in a]
    while a and not a[-1]:
        a.pop()
    return tuple(a)


def subtract(a, b):
    return trim([(a[i] if i < len(a) else 0)
                 - (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def multiply(a, b):
    if not a or not b:
        return ()
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)


def remainder(a, b):
    a = list(trim(a))
    b = trim(b)
    inverse = pow(b[-1], -1, MOD)
    while len(a) >= len(b):
        shift = len(a)-len(b)
        coefficient = a[-1]*inverse % MOD
        for j, x in enumerate(b):
            a[shift+j] = (a[shift+j]-coefficient*x) % MOD
        a = list(trim(a))
    return tuple(a)


def gcd(a, b):
    while b:
        a, b = b, remainder(a, b)
    inverse = pow(a[-1], -1, MOD)
    return trim([inverse*x for x in a])


def power(a, exponent, modulus):
    out = (1,)
    while exponent:
        if exponent & 1:
            out = remainder(multiply(out, a), modulus)
        a = remainder(multiply(a, a), modulus)
        exponent //= 2
    return out


def evaluate(coefficients, value, modulus):
    out = ()
    for coefficient in reversed(coefficients):
        out = remainder(multiply(out, value), modulus)
        out = subtract(out, (-coefficient,))
    return out


def main():
    # Ascending coefficients: f(W)=W^6+W+2.
    f = (2, 1, 0, 0, 0, 0, 1)
    w = (0, 1)
    assert power(w, 5**6, f) == w
    assert gcd(f, subtract(power(w, 5**3, f), w)) == (1,)
    assert gcd(f, subtract(power(w, 5**2, f), w)) == (1,)
    # Hence f is irreducible: its irreducible factors have degree dividing 6,
    # whereas factors of degrees dividing 2 or 3 have been excluded.

    z = (2, 2, 4, 1, 2, 4)
    assert power(z, 63, f) == (1,)
    assert power(z, 21, f) != (1,)
    assert power(z, 9, f) != (1,)

    rows, columns = [43, 44, 61, 62], [36, 37, 54, 55]
    coefficients = [0] * 63
    for permutation in permutations(range(4)):
        parity = sum(permutation[i] > permutation[j]
                     for i in range(4) for j in range(i+1, 4))
        exponent = sum(rows[i]*columns[permutation[i]] for i in range(4)) % 63
        coefficients[exponent] += (-1)**parity
    assert evaluate(coefficients, z, f) == ()

    # Independently evaluate Phi_63: X^36-X^33+X^27-X^24+X^18
    #                              -X^12+X^9-X^3+1.
    phi = [0] * 37
    for exponent, coefficient in [(36, 1), (33, -1), (27, 1), (24, -1),
                                  (18, 1), (12, -1), (9, 1), (3, -1), (0, 1)]:
        phi[exponent] = coefficient
    assert evaluate(phi, z, f) == ()
    derivative = [i*phi[i] for i in range(1, len(phi))]
    assert evaluate(derivative, z, f) != ()

    print("Exact certificate passed: irreducible F5 degree 6, primitive order 63,")
    print("and vanishing endpoint minor for counts (0,0,0,0,2,0,2).")
    print("D(X) modulo X^63-1, as (exponent, integer coefficient):")
    print([(i, x) for i, x in enumerate(coefficients) if x])
    print("modulus =", f, "root =", z)
    print("root^21 =", power(z, 21, f), "root^9 =", power(z, 9, f))


if __name__ == "__main__":
    main()
