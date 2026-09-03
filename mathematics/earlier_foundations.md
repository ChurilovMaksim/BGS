# Earlier foundations that survived the reconstruction audit

The original workspace contained many broad `[PROVEN]` labels. They were not
copied wholesale into the current claim set. This file records earlier
material that remains genuinely useful, with deliberately narrower status.

## Finite torus level sets at p=199 — FINITE-CERTIFICATE

`formalization/Bgs/TorusLevelSets.lean` machine-checks finite combinatorial
statements for `Q(a,b)=a^2-ab-b^2 mod 199` and the action of
`A^T=[[2,1],[1,1]]`:

- `ord(A^T)=11`;
- every nonzero level set has `198=p-1` nonzero points;
- the zero cone minus the origin has `396=2p-2` points;
- every nonzero level set has `18=(p-1)/11` cyclic orbits;
- the cyclic action is free on every nonzero level set;
- the resulting global count identity holds.

Large finite evaluations use Lean `native_decide`; this is a fixed-prime
certificate, not a uniform theorem about all split primes.

## Branch scale at p=199 — FINITE-CERTIFICATE

`formalization/Bgs/TorusScaleLaw.lean` checks that `a=139` has order 11, its
recorded inverse is 63, and the half-index trace `s=123` satisfies
`s^2=5 mod 199`. The two recorded branch scales `123` and `76=-123` both
square to `5=t^2-4` and have product `-5` modulo 199.

This is a concrete design certificate; the general scale law is not promoted
from one finite instance.

## Twisted-Jacobi implementation identities — FINITE REGRESSION

`evidence/certificates/twisted_jacobi_scalar_formula.json` and
`evidence/certificates/twisted_jacobi_moments.json` are now validated by the
maintained producer `computations/verification/twisted_jacobi_regression.py`.
The regression performs scalar-vs-BLAS character-sum checks at explicit
designs and reproduces the preserved q-curve fourth moments.

A historical domain bug is excluded: the old closed form requires the relevant
`n1 != 0`; on the nonzero q-curves used by the audited calculation this
condition is automatic. The unrestricted historical statement is not retained.

## Antiunitary symmetry — SCOPED HISTORICAL RESULT

The audited anti-linear eigenspace logic is correct. If
`Theta U Theta^-1=U^-1`, `Uv=lambda v` and `|lambda|=1`, anti-linearity gives

`U Theta v = conjugate(lambda)^-1 Theta v = lambda Theta v`.

Thus the relevant eigenspace is preserved. What is not promoted is a blanket
global GOE-class theorem for every block/chart; that stronger classification
still needs a fresh load-bearing treatment if it is used later.

## Shape/Catalan and full-group arcsine material — USEFUL BUT NOT PROMOTED

Historical exact finite relation counts and moment data motivated useful
Catalan/arcsine conjectures, but the old word-trace algebra had an unresolved
higher rewrite case. Agreement of finitely many moments therefore does not
license an all-orders theorem.

The original relation/shape code and manuscript states remain recoverable from
Git history, in particular the last pre-cleanup archive commit
`d0e414ec26ff7e43ad59e80f77c9d8c679e87c4b`. They are intentionally not
duplicated in the current working tree.
