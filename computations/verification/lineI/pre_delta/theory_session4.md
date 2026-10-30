# Line I, Session 4, item 3: structural attempts at R'_A (honest record)

Notation as in theory_E2.md: Z_m(theta) = sum_n Phihat(n) e(-theta P(n)) for real theta (so Z_nu = Z_m(nu/2h)),
C_Z(k) = sum_{n,n'} Phihat(n) conj Phihat(n') 1[P(n)-P(n') = k]  (difference counts in Z, no reduction),
W'^A = (1/phi) sum_{nu unit, nu not in Res^A-set} (|Z_nu|^2 - RMT)  (exact rewriting of S3.5 definition).

## S4.1 Poisson/aliasing identity with the unit restriction  [P, elementary]
For q | 2h:  (1/q) sum_{nu' mod q} |Z_m(nu'/q)|^2 = sum_{j in Z} C_Z(j q).
Moebius over e | 2h (nu unit mod 2h  <=>  no prime of 2h divides nu):
   F = (1/phi(2h)) sum_{e | 2h} mu(e) (2h/e) sum_j C_Z(j 2h/e).
Proof: expand |Z|^2, sum the geometric series in nu' (orthogonality mod q); sum_{e | gcd(nu,2h)} mu(e) = 1[unit]. QED.
Consequence: F - RMT is an *additive* statement about the weighted difference set {P(n)-P(n')} in the progressions 0 mod q,
q = 2h/e.  The j=0 term (continuous integral int_0^1 |Z_m|^2 = C_Z(0)) is m-local; the dilation/resonance terms of TRACE-206 are
exactly the large-e (small q) aliasing sums; the "bulk" of W'^A is the e=1,2 aliasing sum_{j != 0} C_Z(2hj) minus what RMT predicts.
All three suggested viewpoints reduce to this identity (below); none gives new information about sum_{j!=0} C_Z(2hj).

## S4.2 No fixed S-arithmetic space: the prime support of h_m is unbounded  [P, modulo a cited theorem]
h_m = ((1+sqrt2)^m + (1-sqrt2)^m)/2 = V_m/2 for the Lucas companion sequence of (P,Q) = (2,-1).  V_m = U_{2m}/U_m, and a
primitive prime divisor of U_{2m} (exists for all 2m > 30 by Bilu–Hanrot–Voutier 2001; (2,-1) is not in their exceptional list
for large indices) divides V_m and no earlier U_k.  Hence {p : p | h_m for some m} is infinite and every finite S misses residues of
h_m for infinitely many m.  So a transfer operator on a FIXED adelic/S-arithmetic space (e.g. L^2 of Z_S-points with the finite
factors C^{b^2} for b | prod_{p in S} p^inf) can only see the residues nu/2h whose reduced denominator is S-smooth; for m with a
primitive prime p ~ h^{c} the bulk residues are invisible.  The full-adelic version (all b) is the regular representation of
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
* S4.1 identity (exact), S4.2 (with BHV), the Session-4 symmetry reduction (sym/), the counting certificates (dom/, if certified).
* Prop I8 (one-sided) stands; S4.1 rewrites its lower half as: sum_{j!=0} C_Z(2hj) is not much below RMT - C_Z(0) + dilation terms.
* No rigorous weakening of R'_A (O(m) bound, average-in-m bound, or positive-density version) was obtained.  The common
  bottleneck in every route is the same quantity: aliasing collisions sum_{j!=0} C_Z(2hj) of the weighted difference set at
  modulus 2h (fourth-moment / l^1 obstructions of theory_E2 Routes A–B are two faces of it).
