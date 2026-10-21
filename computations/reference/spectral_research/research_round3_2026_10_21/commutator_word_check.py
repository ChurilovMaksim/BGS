"""Exact finite Lie-word check only; does not prove the operator remainder."""
from fractions import Fraction
from math import factorial
import json

ORDER = 5

def multiply(left, right):
    out = {}
    for u, a in left.items():
        for v, b in right.items():
            if len(u) + len(v) <= ORDER:
                out[u + v] = out.get(u + v, Fraction(0)) + a * b
    return {w: c for w, c in out.items() if c}

def inverse_word(word):
    return [(name, -coefficient) for name, coefficient in reversed(word)]

def series(word):
    out = {(): Fraction(1)}
    for name, coefficient in word:
        factor = {(name,) * k: Fraction(coefficient**k, factorial(k))
                  for k in range(ORDER + 1)}
        out = multiply(out, factor)
    return out

word = [('Y', 1)]
for _ in range(3):
    word = [('X', 1)] + word + [('X', -1)] + inverse_word(word)

result = series(word)
leading = {w: c for w, c in result.items() if len(w) == 4}
expected = {tuple('XXXY'): Fraction(1), tuple('XXYX'): Fraction(-3),
            tuple('XYXX'): Fraction(3), tuple('YXXX'): Fraction(-1)}
assert result.get((), 0) == 1
assert not any(1 <= len(w) <= 3 for w in result)
assert leading == expected

expanded = {}
for word_letters, coefficient in result.items():
    if len(word_letters) != 5:
        continue
    terms = {(): coefficient}
    for letter in word_letters:
        choices = {('X',): Fraction(1)}
        if letter == 'Y':
            choices[('Z',)] = Fraction(1)
        terms = multiply(terms, choices)
    for term, value in terms.items():
        expanded[term] = expanded.get(term, 0) + value
expanded = {term: value for term, value in expanded.items() if value}
assert all('Z' in term for term in expanded)

print(json.dumps({
    'word_factor_count': len(word),
    'Y_factor_count': sum(name == 'Y' for name, _ in word),
    'degrees_one_to_three_vanish': True,
    'degree_four': {''.join(w): str(c) for w, c in sorted(leading.items())},
    'degree_five_after_Y_equals_X_plus_Z':
        {''.join(w): str(c) for w, c in sorted(expanded.items())},
    'scope': 'Exact formal coefficients through degree five; no claim about '
             'uniform semiclassical or tau remainder.'
}, indent=2))
