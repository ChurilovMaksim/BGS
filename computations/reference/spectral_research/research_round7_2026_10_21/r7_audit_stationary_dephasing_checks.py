#!/usr/bin/env python3
"""Exact finite algebra checks; all asymptotic claims have separate proofs."""
from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
from pathlib import Path
from collections import Counter
import json

ROOT = Path(__file__).resolve().parents[1]
counts = Counter()


def check(ok, group):
    counts[group] += 1
    assert ok, (group, counts[group])


@dataclass(frozen=True)
class G:
    a: F = F(0)
    b: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "a", F(self.a))
        object.__setattr__(self, "b", F(self.b))

    def __add__(self, other):
        other = other if isinstance(other, G) else G(other)
        return G(self.a+other.a, self.b+other.b)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-other if isinstance(other, G) else -G(other))

    def __mul__(self, other):
        other = other if isinstance(other, G) else G(other)
        return G(self.a*other.a-self.b*other.b, self.a*other.b+self.b*other.a)

    __rmul__ = __mul__

    def conj(self):
        return G(self.a, -self.b)

    def norm2(self):
        return self.a*self.a + self.b*self.b

    def __truediv__(self, other):
        other = other if isinstance(other, G) else G(other)
        return self * other.conj() * (1/other.norm2())

    def __bool__(self):
        return bool(self.a or self.b)


Z, ONE = G(), G(1)
roots = (G(1), G(0,1), G(-1), G(0,-1))


def eye(n):
    return [[G(int(i == j)) for j in range(n)] for i in range(n)]


def zeros(n, m):
    return [[Z for _ in range(m)] for _ in range(n)]


def adj(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def mul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def add(A, B, c=1):
    return [[a+c*b for a,b in zip(ar,br)] for ar,br in zip(A,B)]


def scale(A, c):
    return [[c*x for x in row] for row in A]


def submatrix(A, rows, cols):
    return [[A[i][j] for j in cols] for i in rows]


def det(A):
    A = [row[:] for row in A]
    n, result = len(A), ONE
    for j in range(n):
        pivot = next((i for i in range(j,n) if A[i][j]), None)
        if pivot is None:
            return Z
        if pivot != j:
            A[j], A[pivot] = A[pivot], A[j]
            result = -result
        value = A[j][j]
        result = result*value
        for i in range(j+1,n):
            c = A[i][j]/value
            for k in range(j+1,n):
                A[i][k] = A[i][k]-c*A[j][k]
    return result


def inv(A):
    n = len(A)
    E = eye(n)
    B = [A[i][:]+E[i] for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j,n) if B[i][j])
        B[j], B[pivot] = B[pivot], B[j]
        value = B[j][j]
        B[j] = [x/value for x in B[j]]
        for i in range(n):
            if i != j:
                c = B[i][j]
                B[i] = [x-c*y for x,y in zip(B[i],B[j])]
    return [row[n:] for row in B]


def psd(A, group):
    check(A == adj(A), group)
    for k in range(1,len(A)+1):
        for ids in combinations(range(len(A)),k):
            d = det(submatrix(A,ids,ids))
            check(d.b == 0 and d.a >= 0, group)


def reflector(v):
    den = sum(x*x for x in v)
    return [[G(int(i == j)-F(2*v[i]*v[j],den))
             for j in range(len(v))] for i in range(len(v))]


signed_dimensions = []
cases = ((3,(0,1,2)), (4,(0,1,2,3)), (5,(0,1,2,3,0)), (3,(0,0,1)))
for n, exponents in cases:
    lam = [roots[e] for e in exponents]
    A = reflector(list(range(1,n+1)))
    v = list(range(1,n+1))
    v[0],v[1] = v[1],v[0]
    B = reflector(v)
    D = [[roots[i % 4] if i == j else Z for j in range(n)] for i in range(n)]
    H = mul(mul(A,D),B)
    check(mul(adj(H),H) == eye(n), "exact complex eigenbases")
    Lambda = [[lam[i] if i == j else Z for j in range(n)] for i in range(n)]
    U = mul(mul(H,Lambda),adj(H))
    check(mul(adj(U),U) == eye(n), "exact complex eigenbases")
    intensity = [[G(H[x][j].norm2()) for j in range(n)] for x in range(n)]
    J = [[G(F(1,n)) for _ in range(n)] for _ in range(n)]
    L = zeros(n,n)
    pairs = {}
    for j in range(n):
        for k in range(n):
            column = [[H[x][j]*H[x][k].conj()] for x in range(n)]
            outer = mul(column,adj(column))
            pairs[j,k] = outer
            if lam[j] == lam[k]:
                L = add(L,outer)
    BB = mul(intensity,adj(intensity))
    Q = add(L,J,-1)
    psd(Q, "stationary and eigenbasis positivity")
    psd(add(BB,J,-1), "stationary and eigenbasis positivity")
    psd(add(L,BB,-1), "stationary and eigenbasis positivity")
    powers = [eye(n)]
    returns = [eye(n)]
    for t in range(1,10):
        powers.append(mul(powers[-1],U))
        returns.append([[G(z.norm2()) for z in row] for row in powers[-1]])
    for T in range(1,10):
        finite = scale(eye(n),F(1,T))
        for t in range(1,T):
            finite = add(finite,add(returns[t],adj(returns[t])),F(T-t,T*T))
        spectral = zeros(n,n)
        for j in range(n):
            for k in range(n):
                ratio = lam[j]*lam[k].conj()
                val, total = ONE, Z
                for t in range(T):
                    total = total+val
                    val = val*ratio
                weight = (total/T).norm2()
                spectral = add(spectral,pairs[j,k],weight)
        check(finite == spectral, "exact Fejer compression")
        psd(add(finite,L,-1), "exact Fejer domination")
    if len(set(lam)) == n:
        check(bool(det(intensity)), "signed first-return identities")
        # Full Ad(U) in the (x,y) matrix-unit coordinates.
        W = [[U[x][a]*U[y][b].conj() for a in range(n) for b in range(n)]
             for x in range(n) for y in range(n)]
        diag = [x*n+x for x in range(n)]
        off = [i for i in range(n*n) if i not in diag]
        P = submatrix(W,diag,diag)
        Bout = submatrix(W,diag,off)
        Cin = submatrix(W,off,diag)
        S = submatrix(W,off,off)
        R = inv(add(eye(len(off)),S,-1))
        RC = mul(R,Cin)
        check(add(P,mul(Bout,RC)) == eye(n), "signed first-return identities")
        derivative = add(add(P,mul(Bout,RC),2),mul(mul(mul(Bout,R),S),RC))
        graphgram = add(eye(n),mul(adj(RC),RC))
        check(derivative == graphgram, "signed first-return identities")
        check(derivative == inv(BB), "signed first-return identities")
        signed_dimensions.append(n)

# No aliases occur in a polynomial kernel under the centered odd-N Fourier map.
for N in range(3,66,2):
    m = (N-1)//2
    for M in range(min(m,5)+1):
        for v in range(-M,M+1):
            for j in range(-m,m+1):
                check(((v+j) % N == 0) == (v+j == 0), "Fourier embedding without aliases")
                check(((v-j) % N == 0) == (v == j), "Fourier embedding without aliases")

tau = F(1,10**80)
check(84000*tau < F(1,1000), "Anosov cone constants")
for error in (F(1,1000),F(2,1000)):
    lower, upper = F(29,5)-error, F(1,5)+error
    check(lower > 5, "Anosov cone constants")
    check(4*upper < lower, "Anosov cone constants")
    check(1/(lower*lower) < F(1,25), "Anosov cone constants")
check(F(7,5)**2 < 2 < F(3,2)**2, "Anosov cone constants")
for T in range(1,201):
    check(F(1,T)+sum(F(2*(T-r),T*T) for r in range(1,T)) == 1,
          "exact Fejer normalization")

sources = (
    "research_round7_2026_10_21/r7_return_uniform_stationary_dephasing.md",
    "research_round7_2026_10_21/r7_return_all_fixed_powers_phase_separation.md",
    "research_round7_2026_10_21/root_original_intensity_at_prescribed_phase.md",
)
hashes = {name:sha256((ROOT/name).read_bytes()).hexdigest() for name in sources}
check(hashes[sources[0]] == "c2bf50a33a642b984afa7bfa83fdc0d28b8019c79d4f47121ab52adee5e53075",
      "source pin")
script_hash = sha256(Path(__file__).read_bytes()).hexdigest()
out = Path(__file__).with_suffix(".md")
lines = [
    "# Exact checks accompanying the stationary-dephasing audit", "",
    "21 October 2026. Integer and Gaussian-rational arithmetic only.", "",
    f"**Result: {sum(counts.values()):,} assertions passed.**", "",
    "| Group | Assertions |", "| --- | ---: |",
]
lines += [f"| {name} | {number:,} |" for name,number in counts.items()]
lines += [
    "", "The abstract finite identities were checked on complex rational unitary examples in dimensions 3, 4, and 5, including degenerate spectra. These are algebra checks and are not computations of the original tiny-kick family.",
    "Signed first-return derivatives were checked directly using the compressed Ad(U) blocks in dimensions " + ", ".join(map(str,signed_dimensions)) + ".",
    "Centered Fourier embedding was checked for every odd N from 3 through 65, polynomial coordinate degree up to five, and every retained input and output mode.",
    "Ergodicity, compactness, all limit operations, and the original-family asymptotic conclusions have separate analytic proofs in the audit; the script does not claim to verify them by finite tests.",
    "", "## Provenance", "", "| Source | SHA-256 |", "| --- | --- |",
]
lines += [f"| {name} | {digest} |" for name,digest in hashes.items()]
lines += ["", "Checker SHA-256: "+script_hash, ""]
out.write_text("\n".join(lines))
print(json.dumps({"status":"passed","assertions":sum(counts.values()),
                  "output":str(out),"script_sha256":script_hash},indent=2))
