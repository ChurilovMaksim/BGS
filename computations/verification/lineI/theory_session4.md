# Line I, Session 4, item 3: structural attempts at R'_A (honest record)

Notation as in theory_E2.md: Z_m(theta) = sum_n Phihat(n) e(-theta P(n)) for real theta (so Z_nu = Z_m(nu/2h)),
C_Z(k) = sum_{n,n'} Phihat(n) conj Phihat(n') 1[P(n)-P(n') = k]  (difference counts in Z, no reduction),
W'^A = (1/phi) sum_{nu unit, nu not in Res^A-set} (|Z_nu|^2 - RMT)  (exact rewriting of S3.5 definition).

## S4.1 Poisson/aliasing identity with the unit restriction  [P, elementary; the interpretation paragraph is heuristic, DF6]
For q | 2h:  (1/q) sum_{nu' mod q} |Z_m(nu'/q)|^2 = sum_{j in Z} C_Z(j q).
Moebius over e | 2h (nu unit mod 2h  <=>  no prime of 2h divides nu):
   F = (1/phi(2h)) sum_{e | 2h} mu(e) (2h/e) sum_j C_Z(j 2h/e).
Proof: expand |Z|^2, sum the geometric series in nu' (orthogonality mod q); sum_{e | gcd(nu,2h)} mu(e) = 1[unit]. QED.
Consequence [P]: F - RMT is an *additive* statement about the weighted difference set {P(n)-P(n')} in the progressions 0 mod q,
q = 2h/e.  The j=0 term (continuous integral int_0^1 |Z_m|^2 = C_Z(0)) is m-local.
Interpretation [heuristic / assessment, DF6 — NOT part of the proved statement]: the e > 2 Moebius terms are sums of |Z_m|^2 at EXACT
rationals nu'/q of denominator dividing q = 2h/e, i.e. at NON-unit residues, which the Moebius inversion subtracts out; the resonant
residues of TRACE-206 are UNITS nu with b nu == a (mod 2h), i.e. nu/2h = k/b + a/(2hb): NEAR, not at, small-denominator rationals.  The two
are related through the G2 law (TRACE-203), not identical.  Reading the "bulk" of W'^A as the e = 1, 2 aliasing sum
sum_{j != 0} C_Z(2hj) minus its RMT prediction is a heuristic.  All three suggested viewpoints reduce to this identity (below); none
gives new information about sum_{j!=0} C_Z(2hj) [assessment].

## S4.2 No fixed S-arithmetic space: the prime support of h_m is unbounded  [P, modulo a cited theorem; the obstruction is an assessment]
(DF7, corrected.)  h_m = V_m/2 for the Lucas pair alpha, beta = 1 +- sqrt2 ((P,Q) = (2,-1): alpha+beta = 2 and alpha*beta = -1 coprime,
alpha/beta not a root of unity), U_n = (alpha^n - beta^n)/(alpha - beta), V_n = alpha^n + beta^n, and U_{2m} = U_m V_m = 2 h_m U_m
(Lean `Bgs.LineIArith.lucasU_two_mul`).  Bilu–Hanrot–Voutier 2001 (J. reine angew. Math. 539, 75–122, Theorem 1.4: for n > 30 every
n-th Lucas number has a primitive divisor; Carmichael 1913 already covers real Lucas pairs) gives, for every m >= 16, a prime p with
p | U_{2m} and p not dividing (alpha-beta)^2 U_1 ... U_{2m-1}.  Then p is odd (p does not divide U_2 = 2), p does not divide U_m, so
p | h_m; and p does not divide h_{m'} for 0 < m' < m, because h_{m'} | U_{2m'} with 2m' < 2m (Lean `primitive_dvd_nsw`).  Hence every
m >= 16 gives a NEW odd prime of h_m, and for every finite set S of primes, h_m has a prime factor outside S for all sufficiently
large m (Lean `finite_set_fails`, with the primitive-divisor theorem as an explicit hypothesis).  (Numerically every m = 2..60 has a new
prime in h_m.)  No size statement about these primes is claimed (the earlier "p ~ h^c" is withdrawn: it is unproved and unneeded).
[assessment] Consequence for operators: a transfer operator on a FIXED adelic/S-arithmetic space (e.g. L^2 of Z_S-points with the finite
factors C^{b^2} for b | prod_{p in S} p^inf) can only see the residues nu/2h whose reduced denominator is S-smooth; once h_m has a prime
outside S, EVERY unit residue nu has reduced denominator 2h_m, which is not S-smooth, so all unit residues are invisible to it.
The full-adelic version (all b) is the regular representation of
Q/Z with factor dim b^2 -> infinity: there is no trace-class structure and its "trace" of the m-th power over denominators b | 2h
is literally the Parseval sum S4.1.  Obstruction recorded: the residue sum is a single trace only on a non-compact (non-nuclear)
space; no spectral gap/resonance expansion is available uniformly in b.  [assessment]

## S4.3 Hecke-equivariance  [P for the identity, assessment for the use]
The unit group (Z/2h)^x acts on residues; for each Dirichlet character chi mod 2h,
   sum_{nu unit} chi(nu) |Z_nu|^2 = sum_k C(k) * (Gauss-type sum of chi against e(nu k /2h)),
and the trivial character gives back S4.1.  Invariance of |Z_nu|^2 under a subgroup U0 (we have it for the twisted sums,
Zhat(lambda beta) = Zhat(beta), Zhat(-beta) = Zhat(beta)) only reduces the sum to U0-orbits; it adds no cancellation: the
"Hecke trace" is the same trace on orbit space.  To be useful one would need the Hecke operators to act on a space where
|Z_nu|^2 - RMT is (close to) an eigenvector with small eigenvalue; nothing like that is visible (numerically the bulk deviations
are not character-structured: see zpred logs, no dominant chi).  [assessment, not quantified this session]

## S4.4 L^2-in-m averaging  [assessment]
The modulus 2h_m changes with m (and by S4.2 its prime support is unbounded), so W'^A_m for different m involve unrelated
progressions; there is no orthogonality in m.  The only m-uniform object is the transfer law Z_m(a/b) = (1 - lambda^-m) Tr(...L_{a/b}^m...)
for FIXED a/b with b | 2h_m; it controls finitely many residues per b, i.e. exactly the resonant part, not the bulk.
Averaging over m therefore reduces to averaging sum_{j != 0} C_Z(2 h_m j) over m: an additive problem about whether the weighted
difference set of P hits multiples of 2h_m at the RMT rate, on average over m.  No unconditional bound obtained.

## S4.5 What is rigorous after Session 4
* S4.1 identity (exact), S4.2 arithmetic statement (with BHV; the operator obstruction is an assessment), the Session-4 symmetry
  reduction (sym/), the counting certificates (dom/, Theorem I9: certified for classes 1:3 and 2:1; DF4 rerun dom_v3/).
* Prop I8 (one-sided) stands; S4.1 rewrites its lower half as: sum_{j!=0} C_Z(2hj) is not much below RMT - C_Z(0) + dilation terms.
* No rigorous weakening of R'_A (O(m) bound, average-in-m bound, or positive-density version) was obtained.  The common
  bottleneck in every route is the same quantity: aliasing collisions sum_{j!=0} C_Z(2hj) of the weighted difference set at
  modulus 2h (fourth-moment / l^1 obstructions of theory_E2 Routes A–B are two faces of it).
