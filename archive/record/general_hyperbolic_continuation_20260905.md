# General hyperbolic continuation, 2026-09-05

## Mathematical results and dependencies

The finite spectral theorem is now derived directly from Weyl covariance and
integer cyclic-character multiplicities. It requires an odd recurrence order,
identity at that order and invertibility of A^j-I at every nontrivial power.
It does not require a split residue ring, prime dimension, squarefree dimension,
or the previous Gaussian/Floquet analysis. The full and parity trace characters
also determine which parity sector has exactly equal root multiplicities.

For every hyperbolic A in SL(2,Z), both trace signs are covered by
N_K=u_((K+1)/2)+sign(Tr A)*u_((K-1)/2), with the u recurrence at |Tr A|.
The admissible primes are K>3 not dividing |Tr A|-2 sign(Tr A).
The Legendre symbol of that last integer selects the uniform parity sector.
The positive-trace argument and the signed extension have distinct files to
preserve their explicit hypotheses. The invariant odd quadratic refinement
on F2^2 is part of the general quantization, not silently identified with the
previous characteristic.

The support-separated smooth construction then works at fixed nonzero classical
strength for every such A. A finite sine Taylor remainder at each desired order
and an all-real-exponent unitary product bound give all inverse-power operator
norm errors, all polynomial time windows, exact cluster ranks and all fixed
factorial local correlation asymptotics. The actual random-origin point process
converges to the empty measure despite exact unit intensity at each finite N;
its moments are not uniformly integrable. The construction remains smoothly
conjugate to an arithmetic map and is not positive generic BGS.

A separate analytic rigidity proof excludes {g,g composed with S}=0 for a
nonconstant C1 generator whose critical set has measure zero. It applies to
nonconstant real analytic generators. It does not exclude a nonzero bracket
from being a coboundary. The arbitrary finite-multiple-orbit zero-variance
problem has not been solved by this argument.

Quantitative one-mode transversality is proved by projecting the quadratic
Hilbert-space orbit-sum map onto the nonzero single-mode vector. The resulting
real polynomial is monic quadratic. This yields a background-independent
sublevel estimate and a deterministic three-point variance certificate.
These are classical-functional statements, not spectral universality.

## Further exact consequence: sharp inverse-moment threshold

Let b be a nonzero mode, gamma_b=Gamma_A(b)>0, and T a scalar random variable
whose density is bounded by M. Set Z=Gamma_A(g+T b)/gamma_b. The sublevel theorem
gives P(Z<=u)<=min(1,C*u^(1/4)), where C=2*sqrt(2)*M.
In particular Z>0 almost surely. For every 0<p<1/4, the layer-cake identity
and the splitting point u0=C^(-4) give

    E Z^(-p)
      =p integral_0^infinity u^(-p-1) P(Z<u) du
      <=C^(4p)/(1-4p).

Indeed, integrate C*u^(1/4) below u0 and one above u0. The same inequality
holds conditionally on a smooth background when the selected coefficient has
a conditional density bounded by M, and then unconditionally by integration.

The exponent 1/4 cannot be improved uniformly over backgrounds. At g=0,
quadratic homogeneity gives Z=T^4. If the density of T is bounded below by
a positive number near zero, E Z^(-p) diverges for p>=1/4. Thus the exact
threshold for a uniform inverse-moment conclusion is p<1/4. This sharpness
claim concerns the exponent, not the constant in the sublevel estimate.

## Intended verification layers

The Python verifier independently constructs finite metaplectic matrices and
checks both parity spectra in small examples, including a negative control
which fails under the old noninvariant characteristic. Its exact component
checks integer matrix identities and unit determinants.

The C++ verifier computes signed recurrence moduli instead from integer matrix
trace sums and uses multiprecision integers. Its intended sweep contains
131 signed-trace/prime pairs. The Lean source proves finite Boolean
characteristic invariance and particular integer identities at moduli 169
and 989. None of these finite checks formalizes the smooth or asymptotic proof.

## Execution and publication boundary in this continuation

Source-write and read-back requests were made, and a local independent verifier
was submitted to the runtime. No readable successful execution report or new
commit SHA was available to the authoring assistant in this continuation.
Accordingly this record does not assert that those requests completed, that
all tests passed, that the current main is synchronized, or that a new Lean
or PDF build succeeded. The source files deliberately emit a PASS report only
after their checks actually complete.

Do not turn the intended sweep size into a measured test count. Do not copy
successful build claims from the earlier coboundary branch onto these sources.
The integration script defaults to dry-run and records no scientific status;
it requires --apply to add the article input, README/result/claim entries,
CMake targets and the finite Lean import while preserving existing content.

A future audit should match every claimed execution to the exact source hash,
read the complete output, and independently verify the resulting repository
head. No world-priority or prize-level assertion is warranted by a source write.
