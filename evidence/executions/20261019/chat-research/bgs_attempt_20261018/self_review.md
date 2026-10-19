# Adversarial self-review, 18 October 2026

This is author self-review, not an independent referee report.

1. **Actual hypotheses.** The matrix is deterministic symplectic Fourier;
   only D is random. The proof gives P=J and B^2=I/N exactly. No reciprocal
   or iid nonunitary ensemble replaces the original admissible family.
2. **Covariance convention.** Standard circular Gaussian has E|Z|^2=1.
   The exceptional coordinate is Z^2, whose fourth absolute moment is 24.
   All higher fixed trace coordinates are independent sqrt(m)Z_m.
3. **Index collisions.** Replacing balanced tuples by bijections is not exact.
   The proof explicitly bounds its overcount by L! binom(L,2)/N. This is
   the reason the joint trace theorem has an error term rather than a false
   exact moment formula. Direct phase-polynomial checks retain these terms.
4. **Finite-field characteristic.** p is odd. Each difference entry belongs
   to {-2,-1,0,1,2}, so rank zero modulo p has no extra solutions. Nonzero
   skew ranks are even. Characteristic two would break both arguments.
5. **Character average.** Integrating a^T K b first over a gives the exact
   indicator Kb=0; the average is p^(-rank K), with no omitted Gauss phase.
6. **Multiplicity.** The map pi->pi sigma_s pi^(-1) has fiber size
   product m^(s_m)s_m!. Combining this with the involution count gives the
   a! factor, including unequal counts of short cycles on the two sides.
7. **Moment determinacy.** Any real projection of the candidate vector is a
   quadratic Gaussian polynomial plus an independent Gaussian. Its moment
   generating function exists near zero. The method of moments applies.
8. **Exact secular formula.** Repeated sampled vertices make determinant
   rows identical. Thus c_N,k=E|det A|^2/k! is exact, unlike the trace-tuple
   bijection approximation. Formula (6) is exact for every finite N.
9. **Growing regimes.** The L! error allows weighted degree
   (1-epsilon)log N/log log N. The longer coefficient window in (9) needs
   p fixed and the separate Gram coupling. Neither is Heisenberg scale.
10. **Analytic limits.** The physical characteristic-polynomial convergence
    is proved only in |z|<exp(-1/2). Formula (11) describes the coefficient
    limits on |t|<1; it does not silently extend the physical N-limit to
    that whole disk. The coefficient series is justified by positive
    Parseval/Tonelli, not an unjustified expectation interchange.
11. **CUE comparison.** Haar E|e_k|^2=1 is proved by phase orthogonality,
    Cauchy--Binet, and row-permutation invariance. No external universality
    result is imported. Existing global trace-two anomaly is credited as
    prior project work; the current addition is its full joint law and
    complete secular generating function. Literature priority is unverified.
12. **Checks.** Both exact bounded runs pass. They use different physical
    constructions: principal-minor sums, phase signatures, finite-field
    ranks, and full phase Fourier polynomials. All executed inputs are
    retained unchanged. Passing manifests are provenance, not proof badges.
13. **Scope.** No inference from global traces to T_N or local spacings is
    made. G/TC and their inherited proof obligations are not promoted or
    modified. The generic target remains open even at E T_N->1/2.
14. **Closed attempts.** Commutators cannot yield the proposed extra group
    invariance. Full strong-absorption asymptotics do not identify T by
    themselves. These are scoped method obstructions, not a refutation of
    the original target or an exhaustion claim for every possible route.
15. **Bilinear extension.** For fixed seed size b, a generic seed means
    A^T is neither A nor -A. Then A,A^T are linearly independent over every
    odd F_p, so the zero quadratic signature forces sigma=tau. Symmetric
    seeds allow reversed long cycles and are excluded by B=J. Skew seeds
    reproduce the earlier exceptional short-cycle law.
16. **Quadratic phases.** Nonzero quadratic Gauss sums need not be positive
    or real. The proof uses their modulus only. The first seed checker
    wrongly required rational real mixed moments; this implementation
    failure is retained in seed_run/. Its original inputs are unchanged.
    The corrected v2 checker uses exact cyclotomic complex coefficients;
    it passes 630 partition-pair checks and four physical seed examples.
17. **No duplicate promotion.** The two later code versions are not silently
    substituted in old manifests. The original successful runs, failed
    seed run, and corrected seed run have distinct output scopes. The
    broader seed theorem is self-reviewed, with no repository claim update.
