#!/usr/bin/env python3
"""Independent finite HS/block controls over exact Gaussian rationals.

No finite computation proves universal M2 or the asymptotic M3 claim.
"""
from fractions import Fraction as F
from hashlib import sha1, sha256
from pathlib import Path
import json
import platform


class G:
    def __init__(self, a=0, b=0):
        if isinstance(a, G):
            self.a, self.b = a.a, a.b
        else:
            self.a, self.b = F(a), F(b)

    def __add__(self, other):
        y = G(other)
        return G(self.a+y.a, self.b+y.b)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.a,-self.b)

    def __sub__(self, other):
        return self+-G(other)

    def __rsub__(self, other):
        return G(other)+-self

    def __mul__(self, other):
        y = G(other)
        return G(self.a*y.a-self.b*y.b, self.a*y.b+self.b*y.a)

    __rmul__ = __mul__

    def __truediv__(self, other):
        y = G(other)
        norm = y.a*y.a+y.b*y.b
        assert norm
        return G((self.a*y.a+self.b*y.b)/norm,
                 (self.b*y.a-self.a*y.b)/norm)

    def __eq__(self, other):
        y = G(other)
        return self.a == y.a and self.b == y.b

    def __bool__(self):
        return bool(self.a or self.b)

    def conjugate(self):
        return G(self.a,-self.b)

    def norm2(self):
        return self.a*self.a+self.b*self.b

    def __str__(self):
        return str(self.a) if not self.b else f'({self.a})+({self.b})i'


def mat(a):
    return [[G(x) for x in row] for row in a]


def eye(n):
    return [[G(i == j) for j in range(n)] for i in range(n)]


def dagger(a):
    return [[a[j][i].conjugate() for j in range(len(a))]
            for i in range(len(a[0]))]


def product(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), G())
             for j in range(len(b[0]))] for i in range(len(a))]


def plus(a,b):
    return [[x+y for x,y in zip(ar,br)] for ar,br in zip(a,b)]


def scale(a,c):
    return [[x*c for x in row] for row in a]


def power(a,r):
    result = eye(len(a))
    for _ in range(r):
        result = product(result,a)
    return result


def rref(a):
    result = [[G(x) for x in row] for row in a]
    pivots = []
    lead = 0
    for col in range(len(result[0])):
        pivot = next((j for j in range(lead,len(result)) if result[j][col]), None)
        if pivot is None:
            continue
        result[lead],result[pivot] = result[pivot],result[lead]
        pivot_value = result[lead][col]
        result[lead] = [x/pivot_value for x in result[lead]]
        for j in range(len(result)):
            if j != lead and result[j][col]:
                value = result[j][col]
                result[j] = [x-value*y for x,y in zip(result[j],result[lead])]
        pivots.append(col)
        lead += 1
        if lead == len(result):
            break
    return result,pivots


def inverse(a):
    n = len(a)
    rr,pivots = rref([ar+ir for ar,ir in zip(a,eye(n))])
    assert pivots[:n] == list(range(n))
    assert [row[:n] for row in rr] == eye(n)
    return [row[n:] for row in rr]


def submatrix(a,rows,cols):
    return [[a[i][j] for j in cols] for i in rows]


def vector_product(a,x):
    return [sum((v*w for v,w in zip(row,x)),G()) for row in a]


def vector_norm2(x):
    return sum((v.norm2() for v in x), F(0))


def serialize(a):
    return [[str(x) for x in row] for row in a]


def hs_operator(U):
    n = len(U)
    return [[U[i][a]*U[j][b].conjugate() for a in range(n) for b in range(n)]
            for i in range(n) for j in range(n)]


imag = G(0,1)
sx = mat([[0,1],[1,0]])
sy = [[G(),-imag],[imag,G()]]
sz = mat([[1,0],[0,-1]])
sharp_U = scale(plus(eye(2),scale(plus(plus(sx,sy),sz),-imag)),F(1,2))
assert product(product(sharp_U,sx),dagger(sharp_U)) == sy
assert product(product(sharp_U,sy),dagger(sharp_U)) == sz
assert product(product(sharp_U,sz),dagger(sharp_U)) == sx

# A separate non-real, nonnormal-offdiagonal exact N=3 input via Cayley transform.
hermitian = [[G(),G(1),G(0,2)], [G(1),G(2),G(3)],
             [G(0,-2),G(3),G(-1)]]
assert dagger(hermitian) == hermitian
cayley_U = product(plus(eye(3),scale(hermitian,-imag)),
                   inverse(plus(eye(3),scale(hermitian,imag))))
inputs = [('N2_identity',eye(2)), ('N2_Pauli_cycle',sharp_U),
          ('N3_Cayley',cayley_U)]
resolvent_controls = []
observability_controls = []
recurrence_controls = []
for name,U in inputs:
    n = len(U)
    assert product(dagger(U),U) == eye(n)
    T = hs_operator(U)
    assert product(dagger(T),T) == eye(n*n)
    diagonal = [i*n+i for i in range(n)]
    off = [i for i in range(n*n) if i not in diagonal]
    P = submatrix(T,diagonal,diagonal)
    assert P == [[G(U[i][j].norm2()) for j in range(n)] for i in range(n)]
    L = submatrix(T,diagonal,off)
    C = submatrix(T,off,diagonal)
    E = submatrix(T,off,off)
    for z in [G(F(1,3)),G(F(-1,2)),G(0,F(1,4))]:
        full_inverse = inverse(plus(eye(n*n),scale(T,-z)))
        lower_inverse = inverse(plus(eye(len(off)),scale(E,-z)))
        schur = plus(plus(eye(n),scale(P,-z)),
                     scale(product(product(L,lower_inverse),C),-z*z))
        assert submatrix(full_inverse,diagonal,diagonal) == inverse(schur)
        resolvent_controls.append({'input':name,'z':str(z),'status':'passed'})

    returns = [submatrix(power(T,j),diagonal,diagonal) for j in range(7)]
    assert returns[0] == eye(n)
    for j in range(6):
        rhs = product(P,returns[j])
        for s in range(j):
            kernel = product(product(L,power(E,j-1-s)),C)
            rhs = plus(rhs,product(kernel,returns[s]))
        assert returns[j+1] == rhs
    recurrence_controls.append({'input':name,'n_range':'0..5', 'status':'passed'})

    for r in range(n+1):
        if r == 0:
            rank = 0
            nullity = len(off)
            witness = [G(i == 0) for i in range(len(off))]
        else:
            obs = []
            for j in range(1,r+1):
                obs += submatrix(power(T,j),diagonal,off)
            rr,pivots = rref(obs)
            rank = len(pivots)
            nullity = len(off)-rank
            free = next((j for j in range(len(off)) if j not in pivots),None)
            witness = None if free is None else [G(j == free) for j in range(len(off))]
            if witness is not None:
                for row,pivot in zip(rr,pivots):
                    witness[pivot] = -row[free]
                assert all(not x for x in vector_product(obs,witness))
        if r < n:
            assert nullity >= (n-1)*(n-r) > 0
            assert witness is not None
            transported = vector_product(power(E,r),witness)
            assert vector_norm2(witness) > 0
            assert vector_norm2(transported) == vector_norm2(witness)
            full_witness = [G() for _ in range(n*n)]
            for index,value in zip(off,witness):
                full_witness[index] = value
            full_output = vector_product(power(T,r),full_witness)
            assert all(not full_output[index] for index in diagonal)
            assert [full_output[index] for index in off] == transported
        observability_controls.append({'input':name,'N':n,'r':r,'rank':rank,
                                       'nullity':nullity,
                                       'norm_preserving_witness_checked':r<n})

sharp_T = hs_operator(sharp_U)
sharp_diag,sharp_off = [0,3],[1,2]
sharp_P = submatrix(sharp_T,sharp_diag,sharp_diag)
sharp_E = submatrix(sharp_T,sharp_off,sharp_off)
sharp_L = submatrix(sharp_T,sharp_diag,sharp_off)
sharp_C = submatrix(sharp_T,sharp_off,sharp_diag)
J2 = [[G(F(1,2)) for _ in range(2)] for _ in range(2)]
IminusJ = plus(eye(2),scale(J2,-1))
assert sharp_P == J2
assert power(sharp_E,2) == [[G(),G()],[G(),G()]]
assert product(sharp_L,sharp_C) == [[G(),G()],[G(),G()]]
assert product(product(sharp_L,sharp_E),sharp_C) == IminusJ
assert submatrix(power(sharp_T,3),sharp_diag,sharp_diag) == eye(2)
assert power(sharp_U,3) == scale(eye(2),-1)

base = Path(__file__).resolve().parent
source = base/'coherence_memory_candidate_20261014.md'
raw = source.read_bytes()
assert sha256(raw).hexdigest() == 'b7b90c31b51f5cca32c1ef189d064f6896fcb38a232a740e8dccc05b995afb09'
output = base/'coherence_memory_independent_checks_20261014.json'
result = {
    'status':'passed', 'python':platform.python_version(),
    'arithmetic':'Exact Gaussian rationals: ordered pairs of fractions.Fraction',
    'source':{'path':str(source),'bytes':len(raw),'sha256':sha256(raw).hexdigest(),
              'git_blob':sha1(f'blob {len(raw)}\0'.encode()+raw).hexdigest()},
    'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
    'unitary_inputs':[{'name':name,'U':serialize(U)} for name,U in inputs],
    'resolvent_controls':resolvent_controls,
    'recurrence_controls':recurrence_controls,
    'observability_controls':observability_controls,
    'sharp_N2':{'U':serialize(sharp_U), 'P':'J_2', 'Ad_U_Pauli_action':'x -> y -> z -> x',
                'E_sigma_x':'sigma_y', 'E_sigma_y':'0', 'E2':'0',
                'LC':'0', 'LEC':'I_2-J_2', 'D_T3_D':'I_2', 'U3':'-I_2'},
    'prose_boundary_counterexample':'U=I_N gives D T^n D=P^n=I_N for every n',
    'coverage':'Three exact unitary inputs at N=2,3; nine resolvents with |z|<1; '
               'recurrences through n=5; exact observability ranks for 0<=r<=N '
               'and norm-preserving witnesses for 0<=r<N; explicit sharp N=2 case.',
    'non_claims':['Finite controls do not prove universal M2',
                  'No asymptotic M3 or actual U_k phase perturbation computed',
                  'No claim that every source has nondecaying observed memory',
                  'No spectral-radius inference from the norm plateau'],
    'command':'python3 coherence_memory_independent_checks_20261014.py',
}
output.write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+'\n')
print(json.dumps({'status':'passed','output':str(output),
                  'script_sha256':result['script_sha256'],
                  'observability':observability_controls},ensure_ascii=False))
