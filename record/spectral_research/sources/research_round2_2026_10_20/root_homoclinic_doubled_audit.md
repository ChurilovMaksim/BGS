> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/root_homoclinic_doubled_audit.md`. Embedded SHA256: `7a69112ae859e4469ca1ca87225c41b7d80175c97f2fee3d7d64db1c656c25a6`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit of the exact coherent pairs and doubled transfer

20 October 2026. Input:

- fermionic_homoclinic_and_doubled_transfer.md
- SHA-256: 85e74eda0116dbbda1e3ba7a1028fbeb36da97072b7a92b3addc5d3004024168

**Verdict: PASS for the statements in this input.** This is an audit of the
specified proof, not a claim that the target spectral-statistics theorem
has been established. The exponentially small pair construction in the
input is not the later, still separate large-mass encounter proposal.

## 1. Exact phase and the odd-dimensional convention

The two winding factors cancel exactly because
(-1)^(n_q n_p) exp(-i*pi*N*n_q*n_p)=1 for odd N.
Thus the reduction from input (2.1) to (2.2) retains the full original
lattice phase. No real-half versus modular-half substitution is made.

The Landau deck maps compose: their extra phase is exp(2*pi*i*N*n_p*k_q)=1.
The stated deck law for the generating function has (a,c)=L(b,d).
Since L=I modulo 2, ca-db is even, so its constant term in the
prequantum lift is also exactly trivial. The input and output q-linear
terms cancel with the input and output deck factors respectively.
This verifies the local scalar (2.6) and its product around a closed
orbit. The inverse map convention is consistent throughout.

## 2. Uniform regularity of the actual scalar

The centered phase, rather than the uncentered action, is differentiated.
Its base derivative has a quadratic zero in the displacement Z, by the
Taylor integral remainder. On the saturated contour |Z|<=C sqrt(h)|y|,
this cancels the h denominator. Mixed kernel derivatives up to the two
oscillator derivatives in each variable have the same property after
differentiating the remainder. Fixed-strip Cauchy bounds provide the
needed higher spatial derivatives.

The contour's coercivity gives an h-independent exponential majorant
with all polynomial moments. This justifies the dominated derivative
and its L2 bounds even outside the straight part of the contour. The
trace-norm criterion has the correct constant: for
A_osc=1-partial_y^2+y^2, ||A_osc^(-1)||_HS^2=pi^2/24, and sandwiching
the differentiated kernel between its two inverses gives (3.7).

The denominator bound in the normalized graph keeps its base Lipschitz
constant finite uniformly in h. Its fiber contraction is <0.172.
Pullback by Psi^(-1), whose Lipschitz constant is <=8, therefore gives
the Holder-seminorm multiplier 0.172 sqrt(8)<1. Uniform convergence of
the graph iteration preserves the resulting Holder bound.
The disk |gamma_h-1|<0.0002 provides a single logarithm. This verifies
uniform C^(1/2) regularity of log gamma_h and makes no unsupported
claim of C1 regularity of the invariant graph.

## 3. The concrete symbolic pair

In the frozen Berg construction both spines pass through the origin
in the stable and unstable directions. A periodic point on either
corresponding leaf is the origin, since its forward or backward
iterates converge to the origin. Thus the nonzero fixed point
(1/2,0) has a unique loop itinerary.

The connectivity matrix has three loops at each vertex and nonzero
edges in both directions between vertices. The words in (4.2) are
therefore admissible. The unique visit to the other vertex makes each
word primitive. A cyclic rotation cannot reverse the order of its
two distinct single-loop excursions while preserving the unique
two-edge excursion as anchor.

The fiber bound of four excludes the origin for words of primitive
period greater than four. All other periodic points avoid every
iterated boundary and hence have unique codes. The two words therefore
give different primitive geometric orbits of the asserted period,
rather than two codes of one orbit.

## 4. Cell matching, amplitudes, and sizes

Matching equal cells 0^R a 0^R, 0^R b 0^R, and 0^R c 0^R position by
position yields a bijection of all positions. Even at cell endpoints,
a centered radius-R window reaches only the zero padding of the
adjacent cell, so the two windows agree. This checks the matching
argument at its boundary cases.

The exact conjugacy converts symbolic agreement into the stated
spatial decay for chosen common lifts. Composition of log gamma_h
with a spatial C^(1/2) conjugacy gives decay lambda^(-R/4), which is
indeed bounded by (2/3)^R. The local phase's derivative supplies the
factor N. Unit-modulus phase products and the sum of the local
logarithms give (4.8)--(4.10) with constants independent of N and R.

For R=floor(N/6) and odd N, the period is N-1, N+1, or N+3.
The estimate |gamma_h-1|<0.0002 implies 6^(-m)<=|a_p|^2<=5^(-m).
When the relative error is at most 1/2, the ordered cross-term pair
has lower bound m^2 6^(-m); its upper bound is 2m^2 5^(-m).
These weights are exponentially small. Their positivity is positivity
of an identified sub-sum only, not a lower bound on the complete
signed off-diagonal sum.

## 5. Doubled transfer and all tail factors

The stated Weyl commutator is obtained by subtracting the two exact
Weyl multiplication laws, so ad(A_N) is correctly self-adjoint on
Hilbert--Schmidt space. Direct modular Egorov gives the permutation
v -> Sv and the exact identity
Ad(U_N)=exp(i*tau*N*ad(A_N)) P_S. Its trace is |Tr U_N^m|^2.

The double resolvent series is absolutely convergent for 0<r<1.
Equal powers give N^2/(1-r^2), and both off-diagonal orders give
2 sum_(m>=1) r^m |p_m|^2/(1-r^2). The CUE scaling constant in
(6.3) is correct after using 1-r^2~4s/N. Boundedness of the normalized
Abel pair statistic is equivalent to the stated O_s(N^3) squared
Hilbert--Schmidt norm, not to an operator-norm improvement.

The invariant vector I/sqrt(N) makes the operator norm exactly
(1-r)^(-1). Removing the full commutant leaves a unitary operator,
so this alone cannot yield a strictly decaying all-time norm bound.
The assertion is restricted to this actual finite quantum space.

Finally |E_m|<=2q_*^m and |p_m|<=N give
||p_m|^2-|P_m|^2|<=4Nq_*^m+4q_*^(2m).
For q_*=.421, the complete geometric sum is <3N+1.
Thus the normalized infinite Abel tail replacement has error
at most 3/N+1/N^2; there is no discarded tail assumption.

## 6. Scope

Every audited estimate in this input is consistent with H_diag being
true or false. The first missing actual-family bound remains the
squared Hilbert--Schmidt resolvent O_s(N^3), or the fixed compact-band
k=2 weighted trace sum described in the main research state. The
higher-order H_diag assertions require further estimates even if this
pair bound were obtained.

