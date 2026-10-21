"""Finite structural sign check only; no asymptotic claim or original-family evidence."""
import cmath
import itertools
import math

N = 3
m = 3
half = pow(2, -1, N)
quarter = pow(4, -1, N)
roots = [cmath.exp(2j * math.pi * k / N) for k in range(N)]
e = lambda k: roots[k % N]
labels = list(itertools.product(range(N), repeat=2))
index = {v: j for j, v in enumerate(labels)}

def add(a, b): return ((a[0] + b[0]) % N, (a[1] + b[1]) % N)
def omega(a, b): return a[1] * b[0] - a[0] * b[1]
def mv(A, v): return ((A[0][0]*v[0]+A[0][1]*v[1]) % N,
                      (A[1][0]*v[0]+A[1][1]*v[1]) % N)
def mm(A, B): return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def adj(A): return [[A[j][i].conjugate() for j in range(len(A))] for i in range(len(A))]
def tr(A): return sum(A[j][j] for j in range(len(A)))
def ident(n): return [[int(i==j) for j in range(n)] for i in range(n)]
def mpow(A, n):
    out = ident(len(A))
    for _ in range(n): out = mm(out, A)
    return out
def imod(A): return [[v % N for v in row] for row in A]
def inv2(A):
    d = pow((A[0][0]*A[1][1]-A[0][1]*A[1][0]) % N, -1, N)
    return imod([[d*A[1][1], -d*A[0][1]], [-d*A[1][0], d*A[0][0]]])

S = [[3,2],[4,3]]
Sp = [imod(mpow(S,j)) for j in range(m+1)]
Si = [inv2(A) for A in Sp]
T = Sp[m]
K = imod([[T[i][j]-int(i==j) for j in range(2)] for i in range(2)])
Ki = inv2(K)
C = imod(mm([[T[i][j]+int(i==j) for j in range(2)] for i in range(2)], Ki))
W = []
for k,l in labels:
    W.append([[e(k*(x+half*l)) if y==(x+l)%N else 0j for y in range(N)] for x in range(N)])

# A dense, exactly orthogonal rational Householder matrix before floating conversion.
v = [1/3,2/3,2/3]
E = [[int(i==j)-2*v[i]*v[j] for j in range(N)] for i in range(N)]
M = [[e(-pow(8,-1,N)*(3*x*x-2*x*y+3*y*y))/math.sqrt(N) for y in range(N)] for x in range(N)]
Mm = mpow(M,m)
U = mm(E,M)
d = [tr(mm(adj(w),E))/N for w in W]
g = [tr(mm(w,Mm)) for w in W]
CE = [[tr(mm(adj(w),mm(E,mm(u,adj(E)))))/N for u in W] for w in W]

paths = list(itertools.product(range(N*N),repeat=m))
pindex = {p:j for j,p in enumerate(paths)}
amps = []
endpoints = []
for p in paths:
    xs = [mv(Sp[j],labels[p[j]]) for j in range(m)]
    area = sum(omega(xs[i],xs[j]) for i in range(m) for j in range(i+1,m))
    lam = (0,0)
    amp = e(half*area)
    for j in range(m):
        amp *= d[p[j]]
        lam = add(lam,xs[j])
    amps.append(amp)
    endpoints.append(lam)

max_closed = 0.0
max_sector = 0.0
all_sectors = 0j
for delta in paths:
    b = [mv(Sp[j],labels[delta[j]]) for j in range(m)]
    B = (0,0)
    for bj in b: B = add(B,bj)
    sector = 0j
    closed = 0j
    for n,p in enumerate(paths):
        shifted = tuple(index[add(labels[p[j]],labels[delta[j]])] for j in range(m))
        q = pindex[shifted]
        weight = amps[n]*amps[q].conjugate()
        sector += weight*g[index[endpoints[n]]]*g[index[endpoints[q]]].conjugate()
        if B==(0,0): closed += weight
    if B==(0,0):
        target = int(all(j==index[(0,0)] for j in delta))
        max_closed = max(max_closed,abs(closed-target))
    before = (0,0)
    claim = 1+0j
    for j in range(m):
        w = mv(Si[j],add(mv(Ki,B),before))
        u = add(w,labels[delta[j]])
        claim *= CE[index[w]][index[u]]
        before = add(before,b[j])
    max_sector = max(max_sector,abs(sector-claim))
    all_sectors += sector

phase_error = max(abs(g[index[lam]] - g[index[(0,0)]]*e(-quarter*omega(lam,mv(C,lam)))) for lam in labels)
direct = abs(tr(mpow(U,m)))**2
print({"N":N,"m":m,"paths":len(paths),"closed_offset_error":max_closed,
       "sector_to_adjoint_cycle_error":max_sector,"cayley_trace_phase_error":phase_error,
       "full_squared_trace_error":abs(all_sectors-direct)})
assert max_closed < 1e-11
assert max_sector < 1e-11
assert phase_error < 1e-11
assert abs(all_sectors-direct) < 1e-11
