"""Exact evaluation of E_theta|Tr(D_theta M_N)^m|^2 (i.i.d. uniform position phases) via
partition-lattice Moebius inversion + quadratic Gauss sums (REPORT Line C, Prop. 2).
  E = N^{-m} sum_rho W(rho) sum_{sigma in S_m} Gs(rho, sigma)
  W(rho) = prod_{blocks} w(|B|),  sum_n w(n) t^n/n! = log(sum_{n>=0} t^n/(n!)^2)
  Gs(rho,sigma) = sum_{z in F^{|rho|}} e_N(c (P_x(z) - P_y(z))),  c = 4^{-1} mod N.
Per-prime exact mode (mod p diagonalisation) and symbolic large-p mode (rank + square class over Q)."""
import itertools, math, sys
from fractions import Fraction
from functools import lru_cache

def set_partitions(m):
    """restricted growth strings"""
    def rec(i, cur, mx):
        if i == m:
            yield tuple(cur); return
        for b in range(mx+2):
            cur.append(b); yield from rec(i+1, cur, max(mx, b)); cur.pop()
    yield from rec(0, [], -1)

def w_coeffs(nmax):
    # power series log(1 + sum_{n>=1} t^n/(n!)^2), coefficient a_n ; w(n) = n! a_n
    A = [Fraction(0)] + [Fraction(1, math.factorial(n)**2) for n in range(1, nmax+1)]
    # log(1+A) = sum_k (-1)^{k-1} A^k / k
    res = [Fraction(0)]*(nmax+1)
    P = [Fraction(1)] + [Fraction(0)]*nmax
    for k in range(1, nmax+1):
        Q = [Fraction(0)]*(nmax+1)
        for i in range(nmax+1):
            if P[i]:
                for j in range(1, nmax+1-i):
                    Q[i+j] += P[i]*A[j]
        P = Q
        for i in range(nmax+1): res[i] += Fraction((-1)**(k-1), k)*P[i]
    return [res[n]*math.factorial(n) for n in range(nmax+1)]

def form_matrix(labels, word, n):
    """integer matrix 2G with z^T G z = sum_j z_{l_j} z_{l_{j+1}} - sum_j z_{w_j} z_{w_{j+1}}"""
    m = len(labels)
    B = [[0]*n for _ in range(n)]
    for seq, s in ((labels, 1), (word, -1)):
        for j in range(m):
            a, b = seq[j], seq[(j+1) % m]
            B[a][b] += s; B[b][a] += s
    return tuple(tuple(r) for r in B)

def diag_modp(B, p):
    """congruence-diagonalise symmetric B mod p: return (rank, product of pivots mod p)"""
    A = [[x % p for x in r] for r in B]; n = len(A); r = 0; prod = 1
    idx = list(range(n))
    while True:
        # find nonzero diagonal among remaining
        rem = [i for i in idx]
        if not rem: break
        piv = next((i for i in rem if A[i][i] % p), None)
        if piv is None:
            # find off-diagonal nonzero, make diagonal nonzero: e_i <- e_i + e_j
            pr = next(((i, j) for i in rem for j in rem if i != j and A[i][j] % p), None)
            if pr is None: break
            i, j = pr
            for k in range(n): A[i][k] = (A[i][k] + A[j][k]) % p
            for k in range(n): A[k][i] = (A[k][i] + A[k][j]) % p
            piv = i
        a = A[piv][piv] % p; ai = pow(a, -1, p)
        for i in rem:
            if i != piv and A[i][piv] % p:
                f = A[i][piv]*ai % p
                for k in range(n): A[i][k] = (A[i][k] - f*A[piv][k]) % p
                for k in range(n): A[k][i] = (A[k][i] - f*A[k][piv]) % p
        r += 1; prod = prod*a % p; idx.remove(piv)
    return r, prod

def diag_Q(B):
    """rank and squarefree class of product of pivots over Q, plus 'bad' primes (pivot num/den primes)"""
    A = [[Fraction(x) for x in r] for r in B]; n = len(A); r = 0; prod = Fraction(1); idx = list(range(n)); bad = 1
    while idx:
        piv = next((i for i in idx if A[i][i] != 0), None)
        if piv is None:
            pr = next(((i, j) for i in idx for j in idx if i != j and A[i][j] != 0), None)
            if pr is None: break
            i, j = pr
            for k in range(n): A[i][k] += A[j][k]
            for k in range(n): A[k][i] += A[k][j]
            piv = i
        a = A[piv][piv]
        for i in idx:
            if i != piv and A[i][piv] != 0:
                f = A[i][piv]/a
                for k in range(n): A[i][k] -= f*A[piv][k]
                for k in range(n): A[k][i] -= f*A[k][piv]
        r += 1; prod *= a; bad *= abs(a.numerator)*a.denominator; idx.remove(piv)
    num = prod.numerator*prod.denominator  # same square class
    sgn = -1 if num < 0 else 1; num = abs(num); sf = 1; d = 2
    while d*d <= num:
        while num % (d*d) == 0: num //= d*d
        if num % d == 0: sf *= d; num //= d
        d += 1
    sf *= num
    return r, sgn*sf, bad

def legendre(a, p):
    a %= p
    if a == 0: return 0
    return 1 if pow(a, (p-1)//2, p) == 1 else -1

def dihedral_canon(lab):
    m = len(lab); best = None
    for s in range(m):
        for rev in (False, True):
            seq = [lab[(s + (-j if rev else j)) % m] for j in range(m)]
            # relabel to restricted growth
            mp = {}; out = []
            for v in seq:
                if v not in mp: mp[v] = len(mp)
                out.append(mp[v])
            t = tuple(out)
            if best is None or t < best: best = t
    return best

def set_partitions_maxdef(m, maxdef):
    """restricted growth strings with deficit m - #blocks <= maxdef (pruned)"""
    def rec(i, cur, mx):
        if i == m:
            yield tuple(cur); return
        for b in range(mx+2):
            nb = max(mx, b) + 1
            if (i + 1) - nb > maxdef: continue
            cur.append(b); yield from rec(i+1, cur, max(mx, b)); cur.pop()
    yield from rec(0, [], -1)

def rho_classes(m, maxdef=None):
    cl = {}
    gen = set_partitions(m) if maxdef is None else set_partitions_maxdef(m, maxdef)
    for rho in gen:
        c = dihedral_canon(rho); cl[c] = cl.get(c, 0) + 1
    return cl

def terms(m, mode='Q', p=None):
    """returns dict key->Fraction coefficient.
    mode 'Q': key (k, r, D) meaning p^{-m} * p^{(2n-r)/2} eps^r ((c/2)^r D / p); with c=1/4, (c/2)~2.
    mode 'p': key (n, r, chi) exact for given prime p."""
    w = w_coeffs(m)
    out = {}
    cache = {}
    for rho, mult in rho_classes(m).items():
        n = max(rho)+1
        sizes = [rho.count(b) for b in range(n)]
        W = Fraction(mult)
        for s in sizes: W *= w[s]
        for perm in itertools.permutations(range(m)):
            word = tuple(rho[perm[j]] for j in range(m))
            B = form_matrix(rho, word, n)
            if B not in cache:
                if mode == 'Q':
                    r, D, bad = diag_Q(B); cache[B] = (r, D, bad)
                else:
                    r, d = diag_modp(B, p); cache[B] = (r, d)
            if mode == 'Q':
                r, D, bad = cache[B]; key = (2*n - r, r, D)
            else:
                r, d = cache[B]
                c2 = pow(8, -1, p)  # c/2 with c = 4^{-1}
                chi = legendre(pow(c2, r, p)*d, p) if r > 0 else 1
                key = (n, r, chi)
            out[key] = out.get(key, Fraction(0)) + W
    return out, cache

def eval_p(m, p):
    """exact float value at prime p (mod p diagonalisation; valid for every odd prime p)"""
    T, _ = terms(m, 'p', p)
    eps = 1 if p % 4 == 1 else 1j
    val = 0
    for (n, r, chi), co in T.items():
        val += float(co)*p**(n - r/2 - m)*(eps**r)*chi
    return val

if __name__ == '__main__':
    for m, p in [(3, 7), (4, 7), (3, 11), (4, 11), (5, 13), (6, 11)]:
        print(m, p, eval_p(m, p))
