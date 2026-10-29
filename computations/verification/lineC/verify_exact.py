"""V1: brute-force E_theta|Tr(D_theta M_N)^m|^2 with the literal repository M_N  vs
   (a) Prop.2 evaluated with mod-p Gauss sums (primes), (b) Prop.2 with direct z-sums (any odd N).
V2: large-p symbolic expansion (symbolic.py) vs per-prime exact evaluation, at large primes."""
import os, sys, itertools, numpy as np, math
from fractions import Fraction
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from model import MN
from brute import exact_E
from gauss_exact import eval_p, rho_classes, w_coeffs, form_matrix
from symbolic import expansion

def prop2_direct(N, m):
    c = pow(4, -1, N); w = w_coeffs(m); tot = 0j
    for rho, mult in rho_classes(m).items():
        n = max(rho)+1
        W = Fraction(mult)
        for b in range(n): W *= w[rho.count(b)]
        Z = np.array(list(itertools.product(range(N), repeat=n)), dtype=np.int64)
        for perm in itertools.permutations(range(m)):
            word = tuple(rho[perm[j]] for j in range(m))
            B = np.array(form_matrix(rho, word, n), dtype=np.int64)
            Q = (np.einsum('ij,jk,ik->i', Z, B, Z)//2) % N   # z^T G z with 2G = B (integer since B has even diagonal)
            tot += float(W)*np.exp(2j*np.pi*(c*Q % N)/N).sum()
    return (tot/N**m).real, abs((tot/N**m).imag)

if __name__ == '__main__':
    print('V1: brute force (literal M_N) vs Prop.2')
    cases = [(5, 3), (5, 5), (5, 7), (7, 3), (7, 4), (7, 6), (9, 3), (9, 4), (11, 3), (11, 5), (13, 4), (13, 5), (15, 3), (15, 4), (17, 4), (19, 4), (21, 3), (23, 4), (29, 4)]
    for N, m in cases:
        b = exact_E(MN(N), m)
        d, im = prop2_direct(N, m) if (m <= 5 and N**m <= 10**6) else (float('nan'), 0)
        isprime = all(N % q for q in range(2, int(N**.5)+1))
        g = eval_p(m, N).real if isprime else float('nan')
        print(f'N={N:3d} m={m}  brute={b:.12f}  prop2_direct={d:.12f} (|Im|={im:.1e})  prop2_modp={g:.12f}  max|diff|={max(abs(b-d), abs(b-g) if isprime else 0):.2e}')
        sys.stdout.flush()
    print('V2: symbolic large-p expansion vs per-prime exact evaluation')
    for m in range(3, 8):
        E, badp = expansion(m)
        for p in (101, 103, 1009, 1013, 10007, 10009):
            eps = 1 if p % 4 == 1 else 1j
            def leg(D):
                if D == 1: return 1
                # Jacobi via Euler criterion on D mod p
                return 1 if pow(D % p, (p-1)//2, p) == 1 else -1
            val = sum(float(co)*p**float(e)*(eps if odd else 1)*leg(D) for (e, odd, D), co in E.items())
            ex = eval_p(m, p)
            print(f'm={m} p={p:5d} symbolic={complex(val).real:.15f} exact={ex.real:.15f} diff={abs(val-ex):.1e}')
        sys.stdout.flush()
