"""Independent exact checks for the frozen ramified higher-seven candidate.

No author program is imported. Arithmetic is polynomial long division over F5;
the kernel and gauges are rebuilt from the stated formulas. Bounded checks do
not replace the separate uniform proof audit.
"""
from pathlib import Path
from fractions import Fraction
import argparse, hashlib, json, math, platform, time
import numpy as np

if not __debug__:
    raise RuntimeError("Assertions must be enabled")
ROOT = Path(__file__).resolve().parent
D = 42
ZERO = np.zeros(D, dtype=np.int64)
ONE = ZERO.copy(); ONE[0] = 1
# Phi49 = sum_{j=0}^6 x^(7j). Build monomial remainders by multiplying x,
# then applying its monic degree42 relation; not a reshape/cyclic shortcut.
TABLE = np.zeros((2*D-1, D), dtype=np.int64); TABLE[0, 0] = 1
for k in range(1, len(TABLE)):
    TABLE[k, 1:] = TABLE[k-1, :-1]
    for j in range(6): TABLE[k, 7*j] -= TABLE[k-1, -1]
    TABLE[k] %= 5
X = TABLE[1].copy()

def mul(a, b):
    return np.convolve(a, b) @ TABLE % 5

def power(a, k):
    ans = ONE.copy()
    while k:
        if k & 1: ans = mul(ans, a)
        a = mul(a, a); k >>= 1
    return ans

def trim(a):
    a = list(a)
    while a and a[-1] == 0: a.pop()
    return a

def divrem(a, b):
    a, b = trim(a), trim(b)
    q = [0]*max(0, len(a)-len(b)+1)
    while len(a) >= len(b):
        j = len(a)-len(b); c = a[-1]*pow(int(b[-1]), -1, 5)%5
        q[j] = c
        for k, x in enumerate(b): a[j+k] = (a[j+k]-c*x)%5
        a = trim(a)
    return trim(q), a

def polysub(a, b):
    return trim([((a[k] if k < len(a) else 0)-(b[k] if k < len(b) else 0))%5
                 for k in range(max(len(a), len(b)))])

def polymul(a, b):
    if not a or not b: return []
    return trim((np.convolve(a, b)%5).tolist())

MOD = [int(k%7 == 0) for k in range(43)]

def inv(a):
    r0, r1, s0, s1 = MOD, trim(a.tolist()), [], [1]
    assert r1
    while r1:
        q, r = divrem(r0, r1)
        r0, r1, s0, s1 = r1, r, s1, polysub(s0, polymul(q, s1))
    assert len(r0) == 1
    s0 = [(x*pow(int(r0[0]), -1, 5))%5 for x in s0]
    _, s0 = divrem(s0, MOD)
    out = ZERO.copy(); out[:len(s0)] = s0
    assert np.array_equal(mul(out, a), ONE)
    return out

def rank(A):
    A = A.copy()%5; row = 0; pivots = []
    for col in range(A.shape[1]):
        hit = next((k for k in range(row, A.shape[0]) if np.any(A[k, col])), None)
        if hit is None: continue
        A[[row, hit]] = A[[hit, row]]
        v = inv(A[row, col])
        for j in range(col, A.shape[1]): A[row, j] = mul(A[row, j], v)
        for i in range(row+1, A.shape[0]):
            a = A[i, col].copy()
            if np.any(a):
                for j in range(col, A.shape[1]): A[i, j] = (A[i, j]-mul(a, A[row, j]))%5
        pivots.append(col); row += 1
        if row == A.shape[0]: break
    return row, pivots

def inverse(A):
    n = len(A); M = np.zeros((n, 2*n, D), dtype=np.int64); M[:, :n] = A
    for j in range(n): M[j, n+j] = ONE
    for col in range(n):
        hit = next(k for k in range(col, n) if np.any(M[k, col]))
        M[[col, hit]] = M[[hit, col]]; v = inv(M[col, col])
        for j in range(2*n): M[col, j] = mul(v, M[col, j])
        for i in range(n):
            if i == col: continue
            a = M[i, col].copy()
            for j in range(2*n): M[i, j] = (M[i, j]-mul(a, M[col, j]))%5
    return M[:, n:]

def dot(a, b):
    out = ZERO.copy()
    for x, y in zip(a, b): out = (out+mul(x, y))%5
    return out

def field_setup(n):
    if n == 49: q = X
    elif n == 147:
        for c in range(1, 5):
            z = power((X+c*ONE)%5, (5**42-1)//3)
            if not np.array_equal(z, ONE): break
        assert np.array_equal(power(z, 3), ONE)
        q = mul(X, z)
    else: raise ValueError(n)
    powers = [ONE]
    for k in range(1, n): powers.append(mul(powers[-1], q))
    assert np.array_equal(mul(powers[-1], q), ONE)
    for p in (7, 3):
        if n%p == 0: assert not np.array_equal(powers[n//p], ONE)
    return lambda k: powers[k%n]

def data(n, last_depth=None):
    m = n//7; qp = field_setup(n)
    if last_depth is None: last_depth = m-1
    prod = np.zeros((last_depth+1, 7, D), dtype=np.int64); prod[0, :] = ONE
    for t in range(1, last_depth+1):
        for j in range(7):
            z = (ONE+qp(t+m*j))%5
            prod[t, j] = mul(prod[t-1, j], mul(z, z))
    low = [ONE]
    for s in range(1, m):
        z = (ONE-qp(7*s))%5
        low.append(mul(low[-1], mul(z, z)))
    def gauge(t, j):
        h = t//m; f = low[t%m].copy()
        while h:
            f = f*pow(math.factorial(h%5), 2, 5)%5; h //= 5
        return mul(qp(m*j*t+4*t*t), inv(mul(prod[t, j], f)))
    def raw(x, y):
        return qp(-pow(8, -1, n)*(3*x*x-2*x*y+3*y*y))
    def block(rt, ct):
        out = np.zeros((7, 7, D), dtype=np.int64); a = (n+1)//2
        for j in range(7):
            ri = inv(gauge(rt, j))
            for k in range(7):
                out[j, k] = mul(ri, mul(raw(a+rt+m*j, a+ct+m*k), gauge(ct, k)))
        return out
    return qp, prod, low, gauge, raw, block

def base_checks(unit=False):
    n = 49; m = 7; qp, prod, low, gauge, raw, block = data(n, 35)
    g = np.array([gauge(t, j) for t in range(m) for j in range(7)])
    if unit:
        ci = inv(4*qp(-4)%5)
        for t in range(m):
            for j in range(7): g[7*t+j] = mul(g[7*t+j], power(ci, t))
    gi = np.array([inv(v) for v in g])
    # Independently construct the multiplication-by-raw-Fourier linear map.
    pos = [(n+1)//2+t+m*j for t in range(m) for j in range(7)]
    T = np.zeros((49, 49, D, D), dtype=np.int64)
    for i, a in enumerate(pos):
        for j, b in enumerate(pos):
            e = -pow(8, -1, n)*(3*a*a-2*a*b+3*b*b)%n
            for k in range(D): T[i, j, :, k] = qp(e+k)
    def J(v):
        out = np.zeros_like(v); out[:-7] = v[7:]; return out
    def K(v):
        z = np.array([mul(g[j], v[j]) for j in range(n)])
        z = np.einsum('abij,bj->ai', T, z)%5
        return np.array([mul(gi[j], z[j]) for j in range(n)])
    # Actual reduced upper bond from the Laurent r, not cosine builder.
    c = 4*qp(-4)%5
    for t in range(1, 7):
        for j in range(7):
            z7 = (qp(7*t)-ONE)%5; z1 = (qp(t+7*j)+ONE)%5
            bond = -mul(mul(z7, z7), mul(z1, z1))%5
            bond = mul(bond, qp(-8*(t+7*j)))
            assert np.array_equal(mul(inv(gauge(t-1, j)), mul(bond, gauge(t, j))), c)
    result = []
    for shift in range(6):
        h = prod[m*shift]
        def E(v):
            z = K(v); out = np.zeros_like(z)
            for t in range(m):
                for j in range(7): out[7*t+j] = mul(h[j], z[7*t+(j+shift)%7])
            return out
        # Literal effective-gauge witness T=J+H_r K_n, distinct from author's
        # unit-upper-gauge script. This checks precisely the candidate's T.
        def step(v): return (J(v)+E(v))%5
        v = np.zeros((n, D), dtype=np.int64); v[24] = ONE
        w = J(v); krylov = []; comm = []
        for t in range(n):
            krylov.append(v.copy()); comm.append((w-J(v))%5)
            v, w = step(v), step(w)
        rk, kp = rank(np.array(krylov).transpose(1, 0, 2))
        rc, cp = rank(np.array(comm).transpose(1, 0, 2))
        rec = {'shift':shift, 'cyclic_rank':rk, 'commutator_rank':rc,
               'cyclic_columns':kp, 'commutator_columns':cp}
        print(json.dumps(rec), flush=True); result.append(rec)
        assert rk == 49 and rc == 48
    return {'n':49, 'gauge':'D_unit=D_eff*(4q^(-4))^(-t)' if unit else 'D_eff exactly as (6)', 'vector':24,
            'T':'J+H_r K_49^unit' if unit else 'J+H_r K_49',
            'actual_upper_scalar':'1' if unit else '4q^(-4)', 'variants':result}

def lucas_endpoint(n, e):
    m = n//7; P = 5**e; L = m*P; high = m*(P-1)
    qp, prod, low, gauge, raw, block = data(n, high+m-1)
    facts = []; ifacts = []
    for t in range(L):
        v = t//m; f = low[t%m].copy()
        while v: f = f*pow(math.factorial(v%5), 2, 5)%5; v //= 5
        facts.append(f); ifacts.append(inv(f))
    prev = []; count = 0; carried = 0; phase_count = 0
    for s in range(L):
        # Alternative q-Pascal recurrence to author: [s,r]=[s-1,r]+Q^(s-r)[s-1,r-1].
        row = []
        for r in range(s+1):
            value = ZERO.copy()
            if r < s: value += prev[r]
            if r: value += mul(qp(7*(s-r)), prev[r-1])
            if s == 0: value = ONE.copy()
            value %= 5; row.append(value)
            rr, ss = r//m, s//m; no_carry = r%m <= s%m
            while rr or ss:
                no_carry &= rr%5 <= ss%5; rr //= 5; ss //= 5
            want = mul(facts[s], mul(ifacts[r], ifacts[s-r])) if no_carry else ZERO
            sq = mul(value, value)
            assert np.array_equal(sq, want); count += 1
            carried += not no_carry
            if no_carry and (n, e) == (49, 1):
                # Explicitly check BOTH depth conjugations from leading Shat.
                old = mul(qp(-8*r*(s-r)), sq)
                new = mul(mul(facts[r], qp(-4*r*r)),
                          mul(old, mul(qp(4*s*s), ifacts[s])))
                expect = mul(qp(4*(s-r)**2), ifacts[s-r])
                assert np.array_equal(new, expect); phase_count += 1
        prev = row
    shift = (P-1)%7; scalar = pow(4, (P-1)//7, 5); entries = 0
    for r in range(m):
        for s in range(m):
            end, base = block(high+r, s), block(r, s)
            for j in range(7):
                h = prod[m*shift, j]*scalar%5
                for k in range(7):
                    assert np.array_equal(end[j, k], mul(h, base[(j+shift)%7, k])); entries += 1
    rec = {'n':n, 'e':e, 'N':n*P, 'lucas_entries':count,
           'carry_zeros':carried, 'simultaneous_gauge_checks':phase_count,
           'endpoint_entries':entries, 'shift':shift}
    print(json.dumps(rec), flush=True); return rec

def shifted_poles():
    # Use long-chain n147, independently build endpoint and penultimate blocks.
    n = 147; m = 21; qp, prod, low, gauge, raw, block = data(n, 5*m)
    E0 = block(m-1, 0); F0 = block(m-2, 0); cases = []
    for shift in range(6):
        hh = prod[m*shift]; EE = np.zeros_like(E0); FF = np.zeros_like(F0)
        for j in range(7):
            for k in range(7):
                EE[j,k] = mul(hh[j], E0[(j+shift)%7,k])
                FF[j,k] = mul(hh[j], F0[(j+shift)%7,k])
        alpha = None
        for j in range(7):
            v = (ONE+qp(m*(shift+1+j)-1))%5; pole = inv(mul(v,v))
            for k in range(7):
                want = mul(pole, mul(EE[j,k], qp(-2*m*k)))
                ratio = mul(FF[j,k], inv(want))
                if alpha is None: alpha = ratio
                assert np.array_equal(alpha, ratio)
        cases.append({'shift':shift, 'pole_power':shift+1, 'block_entries':49})
    # Separate grid and pole roots in the accepted B2 polynomial dictionary.
    import sympy as s
    q = s.symbols('q')
    source = ROOT/'source'
    kd = json.loads((source/'bounded_boundary_norm_input.json').read_text())
    qp = field_setup(49)
    def evaluate(expr):
        ans = ZERO.copy()
        for (k,),c in s.Poly(s.sympify(expr),q,modulus=5).terms(): ans=(ans+int(c)*qp(k))%5
        return ans
    coeff = [evaluate(a) for a in kd['coefficients_w']]
    den = mul(evaluate(kd['denominator']), mul((ONE+qp(7))%5,(ONE+qp(7))%5))
    for grid in range(1,7):
        V = np.zeros((7,7,D),dtype=np.int64)
        for t in range(7):
            for j in range(7):
                p = ONE.copy()
                for u in range(1,t+1):
                    z=(ONE+qp(u+7*grid*j))%5; p=mul(p,mul(z,z))
                V[t,j]=mul(qp(7*grid*j*(2*t+3)), inv(p))
        VI=inverse(V)
        for pole in range(1,7):
            left=[]
            for j in range(7):
                z=(ONE+qp(7*pole-1+7*grid*j))%5
                left.append(mul(V[0,j],inv(mul(z,z))))
            contraction=dot(left,VI[:,0]); numer=dot(coeff,[qp(7*pole*k)for k in range(6)])
            assert np.any(contraction)
            assert np.array_equal(mul(contraction,den),numer)
    return {'n147_shifted_penultimate':cases, 'independent_grid_pole_pairs':36,
            'accepted_polynomial_dictionary_identity':True}

def grade_checks():
    # Exact path grades in the row-recursion, retaining all branches (including
    # paths whose symbolic coefficients can cancel); boundaries remove terms.
    cases=[]
    for L in (1,2,3,7,35):
        memo={}
        def support(r,s):
            if r<0 or s<0 or s>=L:return set()
            if (r,s) in memo:return memo[r,s]
            if r==0:return {(s,0,0)}
            z=set(support(r-1,s-1))
            z|={(d,a+1,b)for d,a,b in support(r-1,s)}
            z|={(d,a,b+1)for d,a,b in support(r-1,s+1)}
            z|={(d,a,b+1)for d,a,b in support(r-2,s)}
            for d,a,b in z:assert d-s+r==a+2*b
            leading={(d,a,b)for d,a,b in z if a+2*b==0}
            assert leading==({(s-r,0,0)} if s>=r else set())
            memo[r,s]=z;return z
        count=sum(len(support(r,s)) for r in range(L)for s in range(L))
        cases.append({'L':L,'branch_grades':count})
    # Exact cyclotomic valuation increments and inequality (4).
    valuations=[]
    for m,e in ((7,1),(7,2),(7,3),(21,1),(21,2)):
        P=5**e;L=m*P;F=[Fraction(0)]
        for u in range(1,L):
            if u%m: delta=Fraction(0)
            else:
                v=u//m;a=0
                while v%5==0:a+=1;v//=5
                delta=Fraction(1,2*5**(e-a-1))
            F.append(F[-1]+delta)
        assert all(F[t+1]-F[t]<=Fraction(1,2)for t in range(L-1))
        pairs=0
        for r in range(L):
            for d in range(L-r):
                assert F[r+d]>=F[r]+F[d];pairs+=1
        # Exhaustive correction bounds at first two ramification levels;
        # each grade tests r,d,s with h=d-s+r>0, all integral first-row indices.
        triples=0
        if L<=175:
            for r in range(L):
                for s in range(L):
                    for d in range(max(0,s-r+1),L):
                        h=d-s+r
                        assert h-F[d]+F[s]-F[r]>=Fraction(h,2);triples+=1
        valuations.append({'m':m,'e':e,'superadditive_pairs':pairs,'correction_triples':triples})
    return {'recurrence':cases,'valuations':valuations}

if __name__=='__main__':
    arg=argparse.ArgumentParser();arg.add_argument('mode',choices=['bases','unit_bases','dictionary','poles','grades']);args=arg.parse_args()
    start=time.time()
    assert pow(5,42,49)==1 and all(pow(5,d,49)!=1 for d in (21,14,6))
    if args.mode=='bases':result=base_checks()
    elif args.mode=='unit_bases':result=base_checks(unit=True)
    elif args.mode=='dictionary':result=[lucas_endpoint(n,e)for n,e in [(49,1),(49,2),(49,3),(147,1)]]
    elif args.mode=='poles':result=shifted_poles()
    else:result=grade_checks()
    out={'mode':args.mode,'arithmetic':'F5[x]/Phi49; exact int64 polynomial operations',
         'result':result,'seconds':time.time()-start,'python':platform.python_version(),
         'numpy':np.__version__,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/(args.mode+'_results.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)
