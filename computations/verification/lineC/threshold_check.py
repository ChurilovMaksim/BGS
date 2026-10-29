"""Exactness thresholds of the large-p expansion (Theorem 6 / Theorem 7) [COMPUTATIONAL].
For each m and each prime p in a range, compares EXACTLY (in Q + Q*s, s = eps_p*sqrt(p))
  (a) the per-prime value of Proposition 2 (mod-p congruence diagonalisation, valid for every odd prime), and
  (b) the symbolic large-p expansion (rank and square class over Q), valid by the Hadamard bound for p > 4^m.
m <= 7: symbolic side from symbolic.expansion (Python); m = 8: parsed from logs/engine_m8.log (C++ engine).
Usage: python3 threshold_check.py m pmin pmax [nproc]"""
import sys, re, os
from fractions import Fraction
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gauss_exact import terms
from symbolic import expansion

HERE = os.path.dirname(os.path.abspath(__file__))
# expansion logs (engine_m*.log, symbolic_m1_7.log): $LINEC_DATA, else ./data (packet layout), else ../logs (bgs-lineC layout)
DATA = os.environ.get('LINEC_DATA') or (os.path.join(HERE, 'data') if os.path.isdir(os.path.join(HERE, 'data')) else os.path.join(HERE, '..', 'logs'))

def primes(a, b):
    return [q for q in range(max(a, 3), b+1) if all(q % d for d in range(2, int(q**.5)+1))]

def leg(D, p):
    D %= p
    if D == 0: return 0
    return 1 if pow(D, (p-1)//2, p) == 1 else -1

def eps2(p):  # eps_p^2
    return 1 if p % 4 == 1 else -1

def exact_per_prime(m, p):
    """E = A + B*s, s = eps_p sqrt(p); returns (A, B) as Fractions."""
    T, _ = terms(m, 'p', p)
    A = Fraction(0); B = Fraction(0)
    for (n, r, chi), co in T.items():
        if r % 2 == 0:
            A += co*Fraction(p)**(n - r//2 - m)*eps2(p)**(r//2)*chi
        else:  # p^{n-r/2-m} eps^r = p^{n-(r+1)/2-m} * eps^{r-1} * (eps sqrt p)
            B += co*Fraction(p)**(n - (r+1)//2 - m)*eps2(p)**((r-1)//2)*chi
    return A, B

def symbolic_terms(m):
    if m <= 7:
        E, _ = expansion(m)
        return [(e, odd, D, co) for (e, odd, D), co in E.items()]
    out = []
    with open(os.path.join(DATA, f'engine_m{m}.log')) as f:
        for line in f:
            if line.startswith('decomposition'): break
            mm = re.match(r'\s*p\^\s*(\S+)\s+(eps\*)?\(\s*(-?\d+)/p\)\s*:\s*(\S+)', line)
            if mm:
                out.append((Fraction(mm.group(1)), 1 if mm.group(2) else 0, int(mm.group(3)), Fraction(mm.group(4))))
    return out

def symbolic_at(S, p):
    A = Fraction(0); B = Fraction(0)
    for e, odd, D, co in S:
        if odd:  # p^e eps (D/p) = p^{e-1/2} * s
            B += co*Fraction(p)**int(e - Fraction(1, 2))*leg(D, p)
        else:
            A += co*Fraction(p)**int(e)*leg(D, p)
    return A, B

def job(args):
    m, p, S = args
    ex = exact_per_prime(m, p); sy = symbolic_at(S, p)
    return p, ex, sy

if __name__ == '__main__':
    m, a, b = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    nproc = int(sys.argv[4]) if len(sys.argv) > 4 else 1
    S = symbolic_terms(m)
    ps = primes(a, b)
    with Pool(nproc) as pool:
        res = sorted(pool.map(job, [(m, p, S) for p in ps]))
    ok, bad = [], []
    for p, ex, sy in res:
        eq = (ex == sy)
        (ok if eq else bad).append(p)
        print(f'm={m} p={p:4d} exact=({ex[0]}) + ({ex[1]})*eps*sqrt(p)  symbolic_equal={eq}' + ('' if eq else f'  symbolic=({sy[0]}) + ({sy[1]})*eps*sqrt(p)'))
        sys.stdout.flush()
    print(f'SUMMARY m={m} primes in [{a},{b}]: expansion exact at {len(ok)} primes; differs at {bad}')
