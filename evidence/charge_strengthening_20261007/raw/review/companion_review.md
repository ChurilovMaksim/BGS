# Separate independent audit: global switch transfer

## Claim and primary verdict

**Proved as written**, with the newly accepted one-step gap in `review.md`
and the explicitly inherited fractional-Hamming input used only for the
residual interpretation in T5. The primary conclusions are distinct:

1. The complete occupation-offcharge sum, with arbitrary Hamming masks,
   is exponentially controlled with its explicit switch factor z^s retained.
2. The undamped growing low-switch offcharge family is exponentially small
   without any checksum restriction, including partial checksum-zero fibers.
3. The high-Hamming/high-switch residual has a negligible damped endpoint,
   and its undamped target is equivalent to the stated signed boundary integral.

The final boundary integral is not estimated. No undamped global offcharge,
full CUE pair comparison, plateau, higher factorial or BGS conclusion follows.

Pinned candidate: `global_switch_transfer.md`, SHA256
`4a333b1847eb466ef66326e26562ee63770f6e09ed7f47d7b517e5fbf5e6d0be`.
This is a separate internal audit and does not retroactively enlarge the core
or earlier all-translation reviews. Inputs are frozen in
`companion_source_manifest.json`; canonical and author files were read only.

## 1. Dependency graph and exact generating object

The chain is: exact charge block dictionary and unitary adjoint → scalar/traceless
reduction → accepted one-step bound for the pinched adjoint → uniform arbitrary
torus/Hamming twists → exact occupation projection and Hamming coefficient
extraction → complete switch-damped estimate. A separate chain uses exact
zero-run deletion and the same one-step gap → a uniform twisted full-fiber
bound → an occupation-offcharge partial-fiber bound → switch counting.
Combining those two chains yields the weighted dense residual and the boundary
identity. The old finite-power theorem alone would not justify arbitrary row
twists. Its mixing/Egorov inputs are not needed here.

In the ordinary-HS basis E_(c,j)=|j><j+c|, the block of Ad(U) from d to c has
entry U_(j,k) conjugate(U_(j+c,k+d)), exactly as stated. The c=d entries of
zT+(1-z)D have weight one and the c!=d entries have weight z. Multiplication
on the left by Q_q V_theta places the Hamming and occupation marks at the
row vertex. Expanding one ordinary trace cyclically gives T3 with exactly
m rooted vertices and m directed transitions. Repeated coordinates are retained;
there is no factor m, rotation quotient, or hidden tensor-space dimension.

The theta integral is normalized over one torus variable per coordinate
label. It keeps precisely occupation-balanced terms. Thus zero twist minus
the integral equals the stated actual deterministic offcharge polynomial.
These auxiliary phases are a projector identity, not a changed random model.

## 2. Identity reduction and global norm estimate

Both T and D, and both adjoints, fix e0=I/sqrt(N). Thus e0 is reducing and
H0 invariant. Q_q and V_theta are unitary for |q|=1 and fix e0. Consequently
M fixes precisely the scalar direction used in the proof and preserves H0;
no assertion that this is its entire invariant space at all parameters is needed.

On H0, convexity gives

    ||M(z,q,theta)|| <= z+(1-z)rho = 1-kappa(1-z).

The bound is uniform in all N independently chosen theta variables. Subtracting
the scalar trace 1 leaves dimension N^2-1. It cancels exactly between the two
terms of the offcharge projector, producing the factor 2(N^2-1) in T7.
This scalar is not the Haar ramp min(m,N), and the candidate correctly says so.

As a polynomial in q, G has degree at most m. Fourier extraction at m+1 roots
has no alias among its possible exponents. Each coefficient has absolute value
at most the uniform |q|=1 bound; summing an arbitrary Hamming set costs at most
its cardinality. The Hamming-filtered per-m estimate is O(mN^2 exp(-kappa m(1-z))).
There are O(N) powers in a fixed positive Heisenberg band and normalization N^-2,
so the aggregate factor is O(N^2), exactly as in T9.

In particular z_N=1-A log(N)/N with A>2/(kappa a) is eventually in (0,1) and
makes the bound vanish. The more general exact sufficient condition is
kappa a N(1-z_N)-2 log N→+infinity. Constants and startup remain non-effective.

## 3. The checksum-free partial-fiber argument

For a fixed difference word c, inserting arbitrary occupation phases changes
each block only by the unitary row multiplier V_(theta,c). Its norm is unchanged.
For c=0 that multiplier is exactly the identity. The endpoint identities are

    B_(c,0)^theta 1=0 (c!=0),
    1* B_(0,d)^theta=0 (d!=0).

The first is the inner product of two distinct rows, times a row phase; the
second is the inner product of two distinct columns with no surviving row phase.
They hold for every theta, with no smoothness or derivative bound on theta.

Take a nonconstant cyclic charge word. Every zero-charge run is bounded by
nonzero switch endpoints. If its length is at least two, the intervening factor
P^ell may therefore be replaced exactly by (P-J)^ell, since the endpoint
annihilates J. Length-one runs have no diagonal transition and require no such
replacement. Cyclicity lets the seam be chosen outside a zero run. All r switch
blocks contract by at most one and all m-r diagonal transitions contract by rho.
The trace has dimension N, giving |F_theta(c)|<=N rho^(m-r).

A nonzero constant word has m diagonal factors and satisfies N rho^m. The
constant-zero word is wholly balanced and its offcharge contribution is exactly
zero; it must not be treated as a centered run. Thus for every nonzero word,

    |F_off(c)|=|F_0(c)-integral F_theta(c)| <=2N rho^(m-s(c)).

This genuinely controls the occupation-mismatched part of a checksum-zero
fiber. It does not identify that part with the original full fiber. Its proof
uses the exact mask's uniform torus representation, not a claim that arbitrary
subsets of a small signed sum remain small.

For r>=1, choose the r switch edges and the r cyclic run colors. This counts at
most binom(m,r)N^r words; invalid equal-neighbor choices only overcount. The
r=1 class is empty for a cyclic word but harmlessly overcounted. Constant words
are handled separately. T12 follows with the displayed 2N^2 rho^m first term.

With gamma=-log rho and R_N=floor(gamma a N/(8 log N)), the crude estimate
log(bN^2/rho)<=3 log N eventually makes the truncated sum at most a polynomial
factor times exp(-5gamma aN/8), hence O(exp(-gamma aN/2)). This holds uniformly
on the band. Taking absolute values only after each exact partial-fiber
contraction permits any restrictions on c and any scalar weights depending
on c with modulus at most one.

## 4. Weighted dense-mask subtraction is valid

The high-Hamming filtered global polynomial is an exact sum over all offcharge
pairs with h>floor(.49m). Its low-switch portion is a restriction on c alone,
after the occupation-offcharge projector has already been justified fiberwise.
The new absolute partial-fiber envelope controls this portion uniformly after
multiplication by z^s for every real 0<=z<=1. Consequently its subtraction from
the global high-Hamming polynomial is valid with the exponential error claimed.

This is not subtraction of an old unweighted signed small sum. No estimate for
an arbitrarily reweighted balanced projector or for a masked fragment of a
full signed fiber is imported. The accepted low-Hamming theorem is used only
at the undamped point to locate the remaining literal offcharge set. The
damped dense estimate itself comes from exact Hamming extraction and the new
weighted partial-fiber bound.

## 5. Derivative, boundary and normalization

For the finite polynomial with the fixed residual mask, differentiation marks
each switch by s u^(s-1). The mask is independent of z, so the fundamental theorem
of calculus gives T15 without additional terms. Before mask extraction,

    d/dz Tr M^m = m Tr(M^(m-1) Q_q V_theta(T-D))

follows by summing all m noncommuting product-rule terms and using trace cyclicity.
It does not require M to commute with its derivative. Applying the same theta
projection, Hamming extraction and low-switch subtraction gives exactly the
marked residual derivative. There is no missing m or N factor.

The damped endpoint has already been proved negligible. Therefore the original
N^-2 compact-weight residual target is equivalent to the stated signed integral
over [z_N,1]. This is a reduction with a known interior endpoint, not an estimate
of that integral.

The counterexample z^m has the stated interior exponential bound and equals one
at the boundary. Multiplying by N or N^2 yields the corresponding normalized
band obstruction. It is explicitly not claimed to arise from the actual map.
The elementary telescoping estimate gives 4(N^2-1)m(1-z) before Hamming extraction,
and at most another m+1 after it. Thus aggregate sufficient continuity regimes
are respectively N^2(1-z)→0 and N^3(1-z)→0. They cannot overlap the sufficient
damping regime above. No inference to the endpoint is justified.

One harmless wording refinement: T6 uses 'N(1-z)>>log N'. The exact proved
condition also permits A log N with a sufficiently large fixed A. It is better
to repeat kappa a N(1-z)-2 log N→+infinity. This does not alter the incompatibility
or any theorem, and no source edit was made.

Haar left-diagonal invariance kills each occupation-mismatched monomial before
any deterministic z/Hamming mask is applied, so the offcharge Haar comparator
is zero for every mask. The undamped total comparator remains min(m,N). The
regularized trace is never substituted for this total comparator.

## 6. Independent bounded controls

`switch_checks.py` independently builds a dense, non-Hermitian complex rational
unitary of dimension three as a product of two exact Householder reflections.
It uses the coordinate-pair basis |j><l|, separate literal rooted-word tables,
and a finite torus quadrature rather than the author's symbolic implementation.
The fourth-root average is exact because every occupation exponent lies in
[-m,m] with 1<=m<=3; the four-root q extraction is also alias-free.

Normal and optimized runs agree exactly. The tested range contains:

- All 819 rooted ordered word pairs at N=3, m=1,2,3 and 3,177 literal mask partitions.
- 3,072 complete transfer trace identities and 3,072 marked derivative identities,
  at z=0,1/3,2/3,1, every fourth-root q, and every fourth-root coordinate phase.
- 96 exact torus projections, 72 Hamming coefficient/derivative extractions,
  and 64 explicitly weighted dense-mask subtractions.
- 768 twisted zero-run endpoint identities; 2,304 exact centered zero-run
  replacements; 192 constant-zero exclusions retaining exactly the scalar 1.
- 3,072 two-sided identity reductions for M and its adjoint.

A nonvacuous checksum-zero witness has m=2, c=(1,2), full-fiber value
404113/614656 and offcharge partial-fiber value 175752/614656. They are distinct
and the latter is nonzero. This directly rejects the invalid full-fiber equality
while exercising the new exact projector.

The version-2 manifests include exact code hashes, outputs, resource caps and
actual commands, and validate. The controls prove only these bounded identities.
No literal-tau matrix norm, asymptotic gap, full endpoint law or BGS conclusion
is obtained numerically.

## 7. Obligation summary and remaining gap

Passed: exact N^2 transfer, rooted multiplicities, both identity reductions,
arbitrary torus/Hamming phases, coefficient extraction, uniform twisted
zero-run removal, checksum-zero occupation projection, all-switch word count,
weighted high-Hamming subtraction, derivative ordering, original normalization,
and the interior/boundary distinction.

Inherited rather than re-proved here: the accepted one-step actual gap and the
accepted undamped .49 Hamming estimate. Out of scope: an estimate of T16, the
balanced complement, deterministic full pair law, plateau and higher orders.
The strongest safe new residual is high-Hamming and high-switch, with no
checksum escape clause. Its undamped signed boundary integral remains open.
