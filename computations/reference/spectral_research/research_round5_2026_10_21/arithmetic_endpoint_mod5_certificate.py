"""Small exact certificate for the N=63 endpoint Fourier minor.

Only Python integer arithmetic is used. The finite-field portion proves
that one primitive-root embedding makes this minor zero modulo 5.
The resultant computation certifies its nonzero cyclotomic norm and
identifies that exactly one of the six primes over 5 divides it.
This is a coordinate-minor certificate, not a spectral-simplicity test.
"""
from itertools import permutations


def trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a


def add(a, b, prime):
    return trim([((a[j] if j < len(a) else 0)
                  + (b[j] if j < len(b) else 0)) % prime
                 for j in range(max(len(a), len(b)))])


def multiply(a, b, prime):
    if not a or not b:
        return []
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] = (c[i + j] + x * y) % prime
    return trim(c)


def remainder(a, b, prime):
    a = trim([x % prime for x in a])
    b = trim([x % prime for x in b])
    inverse = pow(b[-1], -1, prime)
    while len(a) >= len(b):
        offset = len(a) - len(b)
        factor = a[-1] * inverse % prime
        for j, x in enumerate(b):
            a[offset + j] = (a[offset + j] - factor * x) % prime
        a = trim(a)
    return a


def power(a, exponent, modulus, prime):
    out = [1]
    while exponent:
        if exponent & 1:
            out = remainder(multiply(out, a, prime), modulus, prime)
        a = remainder(multiply(a, a, prime), modulus, prime)
        exponent //= 2
    return out


def gcd(a, b, prime):
    while b:
        a, b = b, remainder(a, b, prime)
    inverse = pow(a[-1], -1, prime)
    return [(x * inverse) % prime for x in a]


def integer_division(a, b):
    """Exact long division by a monic integer polynomial."""
    a, b = trim(a), trim(b)
    assert b[-1] == 1
    quotient = [0] * max(0, len(a) - len(b) + 1)
    while len(a) >= len(b):
        offset, factor = len(a) - len(b), a[-1]
        quotient[offset] = factor
        for j, x in enumerate(b):
            a[offset + j] -= factor * x
        a = trim(a)
    return trim(quotient), a


def bareiss(matrix):
    """Fraction-free determinant; every asserted division is exact."""
    matrix = [row[:] for row in matrix]
    size, previous, sign = len(matrix), 1, 1
    for k in range(size - 1):
        pivot_row = next((r for r in range(k, size) if matrix[r][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            matrix[k], matrix[pivot_row] = matrix[pivot_row], matrix[k]
            sign = -sign
        pivot = matrix[k][k]
        for i in range(k + 1, size):
            for j in range(k + 1, size):
                numerator = pivot * matrix[i][j] - matrix[i][k] * matrix[k][j]
                assert numerator % previous == 0
                matrix[i][j] = numerator // previous
            matrix[i][k] = 0
        previous = pivot
    return sign * matrix[-1][-1]


def resultant(f, g):
    m, n = len(f) - 1, len(g) - 1
    matrix = [[0] * i + f + [0] * (n - 1 - i) for i in range(n)]
    matrix += [[0] * i + g + [0] * (m - 1 - i) for i in range(m)]
    return bareiss(matrix)


def main():
    prime = 5
    field_polynomial = [1, 3, 3, 3, 3, 3, 1]
    x = [0, 1]
    # The degree-six irreducibility criterion: squarefree factors have
    # degrees dividing six, and none has degree dividing two or three.
    assert power(x, 5**6, field_polynomial, prime) == x
    for degree in (2, 3):
        r = add(power(x, 5**degree, field_polynomial, prime), [0, -1], prime)
        assert gcd(r, field_polynomial, prime) == [1]
    assert power(x, 63, field_polynomial, prime) == [1]
    assert power(x, 21, field_polynomial, prime) != [1]
    assert power(x, 9, field_polynomial, prime) != [1]

    # I=J+7; row translation changes the determinant by a root of unity.
    columns = [0, 1, 18, 19]
    determinant_polynomial = [0] * 63
    for permutation in permutations(range(4)):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(4) for j in range(i + 1, 4))
        exponent = sum(columns[i] * columns[permutation[i]] for i in range(4))
        determinant_polynomial[exponent % 63] += (-1)**inversions
    determinant_polynomial = trim(determinant_polynomial)
    expected = {1: 4, 10: -1, 19: -1, 28: 4, 36: 1, 37: -2, 38: 1,
                45: -2, 46: -2, 47: -2, 54: 1, 55: -2, 56: 1}
    assert {j: c for j, c in enumerate(determinant_polynomial) if c} == expected
    assert remainder(determinant_polynomial, field_polynomial, prime) == []

    numerator = [0] * 43
    for j in (0, 21, 42):
        numerator[j] = 1
    phi63, residue = integer_division(numerator, [1, 0, 0, 1, 0, 0, 1])
    assert residue == []
    # Phi_63=(X^42+X^21+1)/(X^6+X^3+1).
    _, reduced_determinant = integer_division(determinant_polynomial, phi63)
    norm = abs(resultant(phi63, reduced_determinant))
    expected_norm = 5**6 * 7**12 * 127**2 * 881**2
    assert norm == expected_norm

    # ord_63(5)=6, so the six prime factors of Phi_63 mod 5 all have
    # degree six. Exactly one is shared by the determinant polynomial.
    assert all(pow(5, d, 63) != 1 for d in (1, 2, 3))
    assert pow(5, 6, 63) == 1
    shared = gcd([c % 5 for c in phi63],
                 [c % 5 for c in determinant_polynomial], 5)
    assert shared == field_polynomial

    print("PASS: P(X)=X^6+3X^5+3X^4+3X^3+3X^2+3X+1 is irreducible over F5.")
    print("PASS: X modulo P has exact order 63.")
    print("PASS: the endpoint minor I={7,8,25,26}, J={0,1,18,19} vanishes modulo P.")
    print("PASS: gcd(Phi_63, determinant polynomial) modulo 5 equals P.")
    print("PASS: exact cyclotomic norm =", norm)
    print("      = 5^6 * 7^12 * 127^2 * 881^2.")
    print("No assertion is made about the full Jacobi-eigenbasis overlap or H_diag.")


if __name__ == "__main__":
    main()
