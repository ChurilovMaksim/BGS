# Earlier foundations that survived the reconstruction audit

The original workspace contained many broad `[PROVEN]` labels. They were not copied wholesale into the current claim set. This file records the earlier material that remains genuinely useful, with a deliberately narrower status.

## Finite torus level sets at p=199 — FINITE-CERTIFICATE

`formalization/Bgs/TorusLevelSets.lean` machine-checks the finite combinatorial statements for `Q(a,b)=a^2-ab-b^2 mod 199` and the action of `A^T=[[2,1],[1,1]]`:

- `ord(A^T)=11`;
- every nonzero level set has `198=p-1` nonzero points;
- the zero cone minus the origin has `396=2p-2` points;
- every nonzero level set has `18=(p-1)/11` cyclic orbits;
- the cyclic action is free on every nonzero level set;
- the resulting global count identity holds.

The large finite evaluations use Lean `native_decide`; this is a fixed-prime certificate, not a uniform theorem about all split primes. The analytic Weil intertwining statement that motivated the count is not proved by this file.

## Branch scale at p=199 — FINITE-CERTIFICATE

`formalization/Bgs/TorusScaleLaw.lean` checks that `a=139` has order 11, its recorded inverse is 63, and the half-index trace `s=123` satisfies `s^2=5 mod 199`. The two recorded branch scales `123` and `76=-123` both square to `5=t^2-4` and have product `-5` modulo 199.

This is the concrete design certificate; the general scale law is not promoted merely from this finite instance.

## Twisted-Jacobi implementation identities — FINITE REGRESSION

The preserved certificates `evidence/certificates/twisted_jacobi_scalar_formula.json` and `evidence/certificates/twisted_jacobi_moments.json` record finite cross-checks of the twisted-Jacobi implementation. They include scalar-vs-vectorized checks at the recorded designs and reproduction of preserved q-curve moment data at `p=199` and `p=3571`. They are implementation/finite-moment evidence, not an asymptotic spectral theorem.

A historical domain bug is explicitly excluded: the old closed form requires the relevant `n1 != 0`; on the nonzero q-curves used by the audited calculation this condition is automatic. The unrestricted old statement is not retained.

## Antiunitary symmetry — SCOPED HISTORICAL RESULT

The historical kernel-chart calculation has the correct anti-linear eigenspace logic. If `Theta U Theta^-1=U^-1`, `Uv=lambda v` and `|lambda|=1`, then anti-linearity gives

`U Theta v = conjugate(lambda)^-1 Theta v = lambda Theta v`.

Thus the relevant eigenspace is preserved; the earlier objection that `Theta` necessarily sends it to the `lambda^-1` sector was itself incorrect.

What is not promoted is the stronger blanket statement that every relevant block has already been globally certified to be in GOE class. The historical script proves the standard nonzero-kernel chart and finite checks; a fresh global treatment of complementary charts and block conventions is required before using the symmetry classification as a load-bearing theorem.

## Shape/Catalan and full-group arcsine material — USEFUL BUT NOT PROMOTED

The archive contains exact finite relation counts, shape decompositions and moment data that motivated Catalan/arcsine conjectures. These remain valuable for regression and discovery.

They are not current all-orders theorems. In particular, the historical word-trace algebra used to justify the full-group arcsine package contains an unresolved higher rewrite case. Agreement of finitely many moments therefore does not license an all-orders claim.

The finite relation automaton and old manuscript sections remain recoverable from `record/corpus/` and Git history; their universal conclusions stay outside the active theorem list until re-proved.
