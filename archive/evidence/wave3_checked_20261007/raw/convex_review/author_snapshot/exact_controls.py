#!/usr/bin/env python3
"""Exact auxiliary controls; no actual-map or asymptotic verification."""
import hashlib
import itertools
import json
from pathlib import Path

import sympy as s

HERE = Path(__file__).resolve().parent
checks = 0


def check(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1


def equal_matrix(A, B):
    return all(s.simplify(x) == 0 for x in A - B)


def ad(U):
    # Ordering is immaterial for traces; this convention acts on X^transpose.
    return s.kronecker_product(U, U.conjugate())


def slices(U):
    N = U.rows
    return [s.Matrix(N, N, lambda x, y: U[x, y] if (x-y) % N == c else 0)
            for c in range(N)]


def compositions(total, count):
    if count == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for tail in compositions(total - first, count - 1):
                yield (first,) + tail


def word_product(word, T, D):
    result = s.eye(T.rows)
    for digit in word:
        result *= D if digit else T
    return result


U2 = s.Matrix([[s.Rational(3, 5), s.Rational(4, 5)],
               [-s.Rational(4, 5), s.Rational(3, 5)]])
v = s.Matrix([1, 2, 3])
w = s.Matrix([2, -1, 1])
U3 = (s.eye(3)-2*v*v.T/(v.T*v)[0]) * (s.eye(3)-2*w*w.T/(w.T*w)[0])
z = s.Rational(2, 3)
d = 1-z
report = {"arithmetic": "exact SymPy rationals and sqrt(3) Gaussian algebraic numbers",
          "dimensions": [2, 3], "max_degree": 6, "warnings": {}}

for U in [U2, U3]:
    N = U.rows
    check(equal_matrix(U.H*U, s.eye(N)), f"N={N} unitary")
    A = slices(U)
    T = ad(U)
    D = sum((ad(a) for a in A), s.zeros(N*N))
    omega = -1 if N == 2 else (-1+s.I*s.sqrt(3))/2
    Vs = []
    for b in range(N):
        Z = s.diag(*[s.simplify(omega**(b*j)) for j in range(N)])
        Vs.append(s.simplify(Z*U*Z.H))
    Db = sum((ad(V) for V in Vs), s.zeros(N*N))/N
    check(equal_matrix(D, Db), f"N={N} charge average equals slices")
    Tz = z*T+d*D
    powersT = [T**j for j in range(7)]
    powersD = [D**j for j in range(7)]
    powersZ = [Tz**j for j in range(7)]
    for m in range(1, 7):
        by_k = [s.Rational(0) for _ in range(m+1)]
        for word in itertools.product([0, 1], repeat=m):
            tr = s.trace(word_product(word, T, D))
            check(tr >= 0, f"N={N} m={m} word positivity {word}")
            by_k[sum(word)] += tr
        check(s.simplify(sum(z**(m-k)*d**k*by_k[k] for k in range(m+1))
                          - s.trace(powersZ[m])) == 0,
              f"N={N} m={m} complete binomial resummation")
        F = s.trace(powersZ[m])-z**m*s.trace(powersT[m])
        first = d*sum(z**n*s.trace(powersT[n]*D*powersZ[m-1-n]) for n in range(m))
        check(s.simplify(F-first) == 0, f"N={N} m={m} first pinch")
        check(s.simplify(s.trace(powersT[m])-abs(s.trace(U**m))**2) == 0,
              f"N={N} m={m} ordinary squared trace")
        for k in range(1, m+1):
            comp_sum = 0
            for comp in compositions(m-k, k):
                prod = s.eye(N*N)
                for run in comp:
                    prod *= powersT[run]*D
                comp_sum += s.trace(prod)
            check(s.simplify(by_k[k]-s.Rational(m, k)*comp_sum) == 0,
                  f"N={N} m={m} k={k} cyclic compositions")
            cut_sum = 0
            for n in range(m):
                p = m-1-n
                if p < k-1:
                    continue
                tail = sum((word_product(word, T, D)
                            for word in itertools.product([0, 1], repeat=p)
                            if sum(word) == k-1), s.zeros(N*N))
                cut_sum += s.trace(powersT[n]*D*tail)
            check(s.simplify(by_k[k]-cut_sum) == 0,
                  f"N={N} m={m} k={k} fixed count first pinch")
    # Full Kraus-word nonnegative trace at N=2 through degree 4,
    # independently expanded in unitary charge conjugations.
    if N == 2:
        for m in range(1, 5):
            for word in itertools.product([0, 1], repeat=m):
                k = sum(word)
                squared = 0
                for charges in itertools.product(range(N), repeat=k):
                    it = iter(charges)
                    product = s.eye(N)
                    for digit in word:
                        product *= Vs[next(it)] if digit else U
                    squared += abs(s.trace(product))**2
                squared /= N**k
                check(s.simplify(s.trace(word_product(word, T, D))-squared) == 0,
                      f"N={N} explicit Kraus word {word}")
    # The B_n counterexample identity, regardless of asymptotic hypotheses.
    fourth = sum(s.trace(a.H*a)**2 for a in A)
    check(fourth >= N, f"N={N} varying B lower bound")
    for n in range(5):
        Bn = (U.H)**(n+1)
        f = sum(abs(s.trace(U**n*a*Bn))**2 for a in A)
        check(s.simplify(f-fourth) == 0, f"N={N} varying B identity n={n}")

# Scalar count and remainder identities, including all boundary cases.
for A0 in range(1, 9):
    for M in range(A0, 9):
        starts = [max(0, A0-1-p) for p in range(M)]
        mass = d*sum(sum(z**n for n in range(starts[p], M-p)) for p in range(M))
        target = sum(1-z**m for m in range(A0, M+1))
        check(s.simplify(mass-target) == 0, "convex triangular mass")
        check(s.simplify(sum(z**n for n in starts)
                        -(M-A0+1+sum(z**r for r in range(1, A0)))) == 0,
              "convex endpoint mass")
        mass_dec = d*sum(z**(-p-1)*(M-p-starts[p]) for p in range(M))
        check(s.simplify(mass_dec-sum(z**(-m)-1 for m in range(A0, M+1))) == 0,
              "deconvolved triangular mass")
        check(s.simplify(d*sum(z**(-p-1) for p in range(M))-(z**(-M)-1)) == 0,
              "deconvolved endpoint mass")

# Weighted prefix inequality: exact extremal sparse sequence.
for L in range(1, 6):
    C0 = s.Rational(1)
    delta = 1/s.Integer(L)
    R0 = (C0-delta)*(L-1)
    R_opt = max(min((C0-delta)*r, delta*(L-r)) for r in range(L))
    f = [s.Rational(int(n % L == 0)) for n in range(20)]
    for start in range(8):
        for end in range(start, 15):
            lhs = sum(z**n*f[n] for n in range(start, end+1))
            rhs = delta*sum(z**n for n in range(start, end+1))+R0*z**start
            check(lhs <= rhs, "weighted prefix remainder")
            rhs_opt = delta*sum(z**n for n in range(start, end+1))+R_opt*z**start
            check(lhs <= rhs_opt, "sharper positive prefix remainder")

# Negative Hamming coefficient in a complete pinched difference.
m = 4
zh = s.Rational(1, 2)
hamming = {h: s.Rational(0) for h in range(m+1)}
for x in itertools.product(range(2), repeat=m):
    ax = s.prod(U2[x[j], x[(j+1) % m]] for j in range(m))
    for y in itertools.product(range(2), repeat=m):
        ay = s.prod(U2[y[j], y[(j+1) % m]] for j in range(m))
        c = [(y[j]-x[j]) % 2 for j in range(m)]
        h = sum(t != 0 for t in c)
        switch = sum(c[j] != c[(j+1) % m] for j in range(m))
        hamming[h] += ax*ay*(zh**switch-zh**m)
check(hamming[1] == -s.Rational(21168, 390625), "negative h=1 coefficient")
check(sum(hamming.values()) >= 0, "positive complete pinched trace")
report["warnings"]["hamming"] = {str(h): str(v) for h, v in hamming.items()}

# Occupation projection cannot be dominated by theta=0 correction.
Ud = s.diag(1, -1)
check(abs(s.trace(Ud))**2 == 0, "occupation theta=0 zero")
occupation_annealed = (1-zh)*sum(abs(Ud[j,j])**2 for j in range(2))
check(occupation_annealed == 1, "occupation annealed positive")
report["warnings"]["occupation"] = {"theta0_pinched_m1": "0", "annealed_pinched_m1": "1",
                                     "signed_difference": "-1", "z": "1/2"}
report["checks_passed"] = checks
report["nonclaims"] = ["No actual U_N computation", "No right-frame asymptotic proof",
                       "No occupation-uniform or Hamming-mask theorem",
                       "No proof of BGS or the prescribed logarithmic boundary closure"]
output = HERE / "exact_controls_result.json"
output.write_text(json.dumps(report, indent=2)+"\n")
print(json.dumps(report, indent=2))
