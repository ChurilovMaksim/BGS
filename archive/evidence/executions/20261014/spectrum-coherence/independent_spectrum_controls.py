#!/usr/bin/env python3
"""Exact finite controls reconstructed from definitions, without author code.

These controls do not prove the generic diagonal-phase lemma, any limit,
or BGS. Only stdlib integers/Fraction arithmetic is used.
"""
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
from itertools import permutations
from pathlib import Path
import json
import platform
import sys

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / 'flat_spectrum_obstruction_20261013.md'
OUTPUT = ROOT / 'flat_spectrum_obstruction_independent_checks_20261014.json'


def transpose(a):
    return list(map(list, zip(*a)))


def multiply(a, b):
    bt = transpose(b)
    return [[sum((x*y for x, y in zip(row, col)), Q(0))
             for col in bt] for row in a]


def eye(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def kron(a, b):
    return [[a[i][j]*b[r][s] for j in range(len(a[0]))
             for s in range(len(b[0]))]
            for i in range(len(a)) for r in range(len(b))]


def qmatrix(a):
    return [[str(v) for v in row] for row in a]


def add(*polys):
    result = {}
    for poly in polys:
        for exponent, coefficient in poly.items():
            result[exponent] = result.get(exponent, Q(0)) + coefficient
    return {e: c for e, c in result.items() if c}


def scale(poly, scalar):
    return {e: c*scalar for e, c in poly.items() if c*scalar}


def times(a, b):
    result = {}
    for ea, ca in a.items():
        for eb, cb in b.items():
            exponent = tuple(x+y for x, y in zip(ea, eb))
            result[exponent] = result.get(exponent, Q(0)) + ca*cb
    return {e: c for e, c in result.items() if c}


def power(poly, n):
    if n > 0 and not poly:
        return {}
    dim = len(next(iter(poly)))
    result = {(0,)*dim: Q(1)}
    for _ in range(n):
        result = times(result, poly)
    return result


def determinant(a, dim):
    result = {}
    for perm in permutations(range(len(a))):
        inversions = sum(perm[i] > perm[j]
                         for i in range(len(a)) for j in range(i+1, len(a)))
        term = {(0,)*dim: Q((-1)**inversions)}
        for i, j in enumerate(perm):
            term = times(term, a[i][j])
        result = add(result, term)
    return result


def charpoly(a, column_variables=False):
    n = len(a)
    dim = n+1 if column_variables else 1
    lam = {(1,)+(0,)*(dim-1): Q(1)}
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            exponent = [0]*dim
            if column_variables:
                exponent[j+1] = 1
            row.append(add(lam if i == j else {},
                           {tuple(exponent): -Q(a[i][j])}))
        matrix.append(row)
    return determinant(matrix, dim)


def lam_coefficient(poly, degree):
    return {(0,)+e[1:]: c for e, c in poly.items() if e[0] == degree}


def discriminant(poly, n):
    dim = len(next(iter(poly)))
    if n == 1:
        return {(0,)*dim: Q(1)}
    b = lam_coefficient(poly, n-1)
    c = lam_coefficient(poly, n-2)
    if n == 2:
        return add(power(b, 2), scale(c, -4))
    assert n == 3
    d = lam_coefficient(poly, 0)
    return add(times(power(b, 2), power(c, 2)), scale(power(c, 3), -4),
               scale(times(power(b, 3), d), -4), scale(power(d, 2), -27),
               scale(times(times(b, c), d), 18))


def format_poly(poly, names):
    terms = []
    for exponent, coefficient in sorted(poly.items(), reverse=True):
        monomial = '*'.join(name if degree == 1 else f'{name}^{degree}'
                            for name, degree in zip(names, exponent) if degree)
        terms.append(f'{coefficient}' + (f'*{monomial}' if monomial else ''))
    return ' + '.join(terms) if terms else '0'


W = [[1,1,1,1], [1,-1,-1,1], [1,1,-1,-1], [1,-1,1,-1]]
H = [[Q(v, 2) for v in row] for row in W]
assert multiply(W, transpose(W)) == [[4*x for x in row] for row in eye(4)]
assert multiply(H, transpose(H)) == eye(4)
powers = [eye(4)]
for _ in range(6):
    powers.append(multiply(powers[-1], H))
assert powers[2] == [[Q(v) for v in row]
                     for row in [[1,0,0,0],[0,0,1,0],[0,0,0,1],[0,1,0,0]]]
assert powers[6] == eye(4)
hc = charpoly(H)
assert hc == {(4,):Q(1), (3,):Q(1), (1,):Q(-1), (0,):Q(-1)}
B = [[H[i][j]*H[j][i] for j in range(4)] for i in range(4)]
assert multiply(B, transpose(B)) == [[x/4 for x in row] for row in eye(4)]
traces = [sum(p[i][i] for i in range(4)) for p in powers[:6]]
assert traces == [4,-1,1,2,1,-1]

base_labels = Counter({0:1, 2:1, 3:1, 4:1})
mult = Counter({0:1})
tensor_multiplicities = {}
for k in range(1, 17):
    mult = Counter({r:sum(mult[s]*base_labels[(r-s)%6] for s in range(6))
                    for r in range(6)})
    nums = [4**k+2*(-1)**k+2+2**k,
            4**k+(-1)**k-1-2**k,
            4**k-(-1)**k-1+2**k,
            4**k-2*(-1)**k+2-2**k,
            4**k-(-1)**k-1+2**k,
            4**k+(-1)**k-1-2**k]
    assert all(n % 6 == 0 for n in nums)
    assert [mult[r] for r in range(6)] == [n//6 for n in nums]
    assert sum(mult.values()) == 4**k
    tensor_multiplicities[str(k)] = [mult[r] for r in range(6)]

BH2 = kron(B, B)
J3 = [[Q(1,3) for _ in range(3)] for _ in range(3)]
BT = kron(BH2, J3)
gram = multiply(BT, transpose(BT))
assert gram == [[x/16 for x in row] for row in kron(eye(16), J3)]

primes = [3,5,7,11,13,17,19,23,29,31]
chirp_results = []
pair_total = 0
for p in primes:
    parameter_pairs = [(1,d) for d in range(p)] + [(q,0) for q in range(2,p)]
    expected_modulus_coefficients = [2*p-1] + [p-1]*(p-1)
    for q, d in parameter_pairs:
        image = set()
        coefficients = [0]*p
        for b in range(p):
            for c in range(p):
                a, h = (b-c)%p, (q*(b+c)+d)%p
                exponent = (q*(b*b-c*c)+d*(b-c))%p
                assert exponent == a*h % p
                image.add((a,h))
                coefficients[exponent] += 1
        assert len(image) == p*p
        assert coefficients == expected_modulus_coefficients
        pair_total += p*p
    for d in range(p):
        sd = Counter((b*b+d*b)%p for b in range(p))
        sminus = Counter((b*b-d*b)%p for b in range(p))
        assert sd == sminus
    residue_multiplicities = Counter(b*b%p for b in range(p))
    assert residue_multiplicities[0] == 1
    assert all(residue_multiplicities[x] in (0,2) for x in range(1,p))
    chirp_results.append({'p':p, 'q_d_pairs':parameter_pairs,
                          'ordered_bc_pairs':len(parameter_pairs)*p*p,
                          'modulus_squared_coefficients':expected_modulus_coefficients,
                          'square_eigenvalue_multiplicities':
                              [residue_multiplicities[x] for x in range(p)]})

tensor_center_results = []
for k in [2,3]:
    for p in [3,5,7]:
        counts = Counter()
        for r, multiplicity in enumerate(tensor_multiplicities[str(k)]):
            for b in range(p):
                counts[(p*r+6*(b*b%p))%(6*p)] += multiplicity
        N = 4**k*p
        assert sum(counts.values()) == N
        assert len(counts) <= 6*p
        assert 4**k % 6 == 4
        t = 6*p*(4**k//6)
        assert t == N-4*p and t > 0
        assert all(t*center % (6*p) == 0 for center in counts)
        tensor_center_results.append({'k':k, 'p':p, 'N':N,
                                     'occupied_6p_grid_centers':len(counts),
                                     't':t, 'counts':dict(sorted(counts.items()))})

examples = [
    ('N1', [[7]], True),
    ('N2_swap_zero_diagonal', [[0,1],[1,0]], True),
    ('N2_defective_Jordan', [[1,1],[0,1]], True),
    ('N2_dense', [[1,2],[3,4]], True),
    ('N3_cycle_zero_diagonal', [[0,1,0],[0,0,1],[1,0,0]], True),
    ('N2_singular_boundary_zero_matrix', [[0,0],[0,0]], False),
]
lemma_examples = []
for name, a, invertible in examples:
    n = len(a)
    f = charpoly(a, column_variables=True)
    disc = discriminant(f, n)
    assert bool(disc) == invertible
    names = ['lambda'] + [f'z{j+1}' for j in range(n)]
    lemma_examples.append({'name':name, 'A':a, 'f':format_poly(f,names),
                           'discriminant':format_poly(disc,names),
                           'invertible':invertible})

raw = INPUT.read_bytes()
blob_header = f'blob {len(raw)}\0'.encode()
from hashlib import sha1
input_blob = sha1(blob_header+raw).hexdigest()
assert input_blob == '666e8a9ab551e945936198638ebb4d4286a67454'
result = {
    'status':'passed',
    'arithmetic':'Exact Python integers and fractions.Fraction; no floating arithmetic',
    'runtime':{'python':platform.python_version(), 'executable':sys.executable},
    'source':{'path':str(INPUT), 'bytes':len(raw), 'git_blob':input_blob,
              'sha256':sha256(raw).hexdigest()},
    'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
    'core':{'H2':qmatrix(powers[2]), 'H6':qmatrix(powers[6]),
            'charpoly_H':format_poly(hc,['lambda']), 'traces_H_q_0_to_5':list(map(str,traces)),
            'B_H':qmatrix(B), 'B_gram':'I_4 / 4',
            'k2_p3_tensor_B_gram':'I_16 tensor J_3 / 16'},
    'tensor_root_multiplicities_k_1_to_16':tensor_multiplicities,
    'chirp':chirp_results,
    'total_ordered_bc_pairs':pair_total,
    'tensor_center_controls':tensor_center_results,
    'column_phase_discriminant_examples':lemma_examples,
    'coverage':'Core N=4 exact; tensor multiplicities k=1..16; explicit k=2,p=3 Gram; '
               'chirps at ten listed primes for q=1,all d and all nonzero q,d=0; '
               'tensor centers for k in {2,3}, p in {3,5,7}; five invertible symbolic '
               'discriminant examples and one singular boundary example.',
    'non_claims':['Not a universal proof of the generic column-phase lemma',
                  'No perturbed-family eigenvalue computation',
                  'No asymptotic limit, uniform integrability, or BGS certified by this run'],
    'command':'python3 flat_spectrum_obstruction_independent_checks_20261014.py',
}
OUTPUT.write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+'\n')
print(json.dumps({'status':result['status'], 'output':str(OUTPUT),
                  'total_ordered_bc_pairs':pair_total,
                  'input_git_blob':input_blob,
                  'script_sha256':result['script_sha256']},ensure_ascii=False))
