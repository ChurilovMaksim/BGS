# Independent audit: uniform finite-power contraction for all translations

## Claim and primary verdict

**Proved as written**, with the candidate's explicitly inherited actual-map
Egorov and normalized-area mixing inputs and their existing review boundaries.
At fixed tau=10^-80, there are one integer L>=1 and N0 such that for every
odd N>=N0 and every nonzero residue c,

||B_(N,c)^L|| <= 3/4,
B_(N,c)(j,k)=U_N(j,k) conjugate(U_N(j+c,k+c)).

Consequently |Tr B_(N,c)^m|<=C N exp(-gamma m) uniformly for m>=1 and
nonzero c. This establishes the stated N^-2-normalized exponentially small
translated-family aggregate. Its off-charge interpretation requires the
explicit mask ord(c) not dividing m; it does not allow an occupation mask
inside an otherwise unmasked contraction.

Reviewed candidate SHA256:
`c0059f000b4642de174097b3e971d22ba0eac09cdff684289f72ae11db00a7c7`.
This review is independent internal mathematical review. It is not an
external referee certificate or an analytic formalization. The completed
macroscopic review remains unchanged and separately pinned. No canonical
files, claim statuses, publication files, commits or remote branches were
written by this audit.

## 1. Dependency graph and exact inherited scope

The new logical chain is:

- actual raw four-branch parametrix and the already reviewed two-mode phase
  certificate;
- a scaled discrete TT* estimate for effective frequency c, retaining the
  near-row-diagonal minimum;
- small one-step norm for every sequence c->infinity, including c/N->0;
- operator-norm convergence for each fixed c to a compact integral kernel;
- exact midpoint-sector pairing plus actual one-step Egorov and normalized
  trace convergence, identifying that kernel with a Koopman compression;
- actual normalized-area mixing, excluding peripheral eigenvalues of each
  fixed-c compact limit;
- finitely many low offsets plus a simultaneous large-offset cutoff,
  producing one common finite power;
- exact negative-offset conjugation, trace-power bound and once-counted
  occupation-admissible family.

The macro candidate at SHA256
`49a24af2ca9e9628681ce08fcd023528f9b3bc5fbc578c7ec8cdfa11918b4f23`
was separately reviewed as proved as written. That review pins all raw
branch/gluing, literal-time C2, nonlinear translation-factor and ordinary-HS
obligations. This extension uses precisely those ingredients, not the
unproved boundary sketch previously excluded from the macro audit.

The additional inherited input is FM-018,
`frozen_operator_transfer_coercivity.md`, O8 with j=1, O9 and O11.
O8/O9 concern the same raw odd-N quantizer and Ad(U), and O11 concerns the
same nonlinear G=S composed with Phi_g^(tau/(2pi)), under its actual invariant
normalized area. Only fixed smooth observables are used here. There is no
growing-c Egorov estimate, noisy operator, annealed trace, or operator-norm
convergence of a full unregularized Koopman quantization being borrowed.

The prior FM-018 review explicitly retains FM-001 and FM-006 prerequisites.
The relevant portions were read here:

- FM-001 Sections 1, 2 and 3.1 give the corrected ordinary symbol and an
  analytic area-preserving Anosov map conjugate to S for
  0<|kappa|<=10^-12. The actual kappa=tau/(2pi) lies strictly in this range.
  Topological mixing follows from the hyperbolic cat map and this conjugacy.
- FM-006 Section 2 identifies actual normalized area as the equilibrium/Gibbs
  state for the negative unstable potential: Ruelle's inequality bounds
  pressure above by zero, Pesin's formula gives equality for smooth invariant
  area, and Hölder equilibrium-state uniqueness identifies the measure.
- The durable source check `frozen_operator_transfer_sources_20261006.md`
  and EXT-PP-1990 record Parry--Pollicott Proposition 2.4 and its proof,
  printed pp. 29-31 / PDF pp. 33-35, Theorem 2.2(ii), and Appendix III.3.
  Its product-Hölder-norm correlation estimate passes through the Hölder
  Markov coding and Sobolev embedding to O11 for this same area measure.
  The relevant underlying registry leaves remain EXT-RUELLE-1978, Theorem 2,
  and EXT-PESIN-1977, Theorem 5.1.

No new external-source leaf was needed. This audit checks the exact mapping
and the new uses of these accepted inputs; it does not claim a new full
independent audit of FM-001, all of FM-006, or the Ruelle/Pesin/Markov-coding
source proofs. Their recorded self-review/independent-review distinctions
remain intact. Topological conjugacy alone is not used to transport Lebesgue
measure or to claim measure mixing. The nonlinear pressure-growth theorem,
centralizer classification, and the noisy-channel conclusions of FM-018 are
not dependencies of this result.

## 2. Scaled TT*: the potentially dangerous logarithm is controlled

Take a good rectangle in the unit coordinate chart, row separation
h=|i-i'|/N=k/N, and f(y)=psi(i/N,y)-psi(i'/N,y). Fixed-sign mixed derivative
bounds give d0*h<=|f'(y)|<=d1*h. For entries e(ell psi), the lattice increments
are of size (ell/N)h. Their distance from the integers is at least
(ell/N)d0*h, since the local upper bound (ell/N)d1<1/4 excludes every
nonzero integer alias. The total increment variation is O((ell/N)h).

Summation by parts therefore bounds the unnormalized column sum by
O(N/(ell*h)); the reciprocal-denominator variation has the same order.
The product of the two row amplitudes has uniformly bounded variation.
After the N^-2 factor from TT*,

|(TT*)_(i,i')| <= C/(ell*k), i!=i'.

It is essential also to retain the trivial bound C/N, valid for every row
pair. With K=floor(N/ell), the first K offsets cost O(1/ell). The remaining
harmonic sum starts at K, not at 1. Since ell<=N/2 implies
K>=N/(2ell), it is at most log(2ell). Thus

||T||^2 <= C[N^-1+(1+log(2ell))/ell].

This is an alias-safe discrete estimate. The factors ell/N and the cutoff
at N/ell have not been dropped. In particular a slowly growing c cannot
be defeated by a spurious log N/c remainder. As in the macro review, the
rectangles actually used have horizontal width at most the unit chart;
an arbitrary wide-rectangle formulation would require the corresponding
width in its alias condition.

For a smoothly converging family psi_v, a fixed small neighborhood of the
limiting analytic zero set is removed first. Its ordinary, unnormalized HS
norm is bounded by a uniform amplitude bound times the square root of its
area, in the limit N->infinity. On finitely many complementary rectangles,
continuity preserves a positive lower mixed-derivative bound, and the scaled
estimate tends to zero as ell->infinity. The sequence limit precedes the
small-area limit. No uniform finite-type bound or count of zeros is assumed.

## 3. Growing offsets and the simultaneous two-cutoff statement

For 1<=c_N<N/2, c_N->infinity, pass to a subsequence on which u_N=c_N/N
converges. If the limit is positive, the separately reviewed macro theorem
applies. If u_N->0, the off-diagonal branch pairs r!=s retain at u=0 the
nonzero exact Fourier factors A_i[e(r/4)-e(s/4)]. They are o(1) at frequency N
by the parameter-uniform version of the inherited TT* argument.

For a diagonal branch, divide the phase difference by u using the exact
identity

Psi_(r,u)=-integral_0^1 (partial_x+partial_y)S_r(x+t u,y+t u) dt.

This defines a uniformly smooth, indeed real-analytic, phase family down to
u=0. Its cat part is separable. The Fourier coefficients of its limiting
mixed derivative are
-2pi i (nu_(i,x)+nu_(i,y)) A_i e(r/4).
The two frequency sums are -1/2 and 1/2, so both coefficients are nonzero.
This uses the exact nonlinear coefficients from the macro proof, not a
new Taylor error divided by a potentially tiny u.

The effective frequency is exactly ell=N*u=c_N. On good rectangles the
needed lower and upper derivative bounds are uniform, while u_N*d1<1/4
holds eventually. Applying the scaled cutoff argument gives o(1) for all
four diagonal branch terms. The 16-term sum and O(N^-1) error prove A8 for
every growing-offset sequence.

The passage to A11 has the correct quantifiers. If for some epsilon no
simultaneous pair (C_epsilon,N_epsilon) existed, one could choose a failing
odd N_n>=n and c_n>=n with c_n<N_n/2. This contradicts A8. Thus one cutoff
controls every N large enough and every offset above that cutoff at once.
A threshold chosen separately along each sequence would not suffice; the
candidate does not make that mistake.

## 4. Fixed-c norm convergence really removes escaping aliases

Fix an integer c>0. For every r!=s, the limiting phase at u=0 has a
nonidentically-zero analytic mixed derivative. The corresponding matrix
norm tends to zero, including its action on arbitrary N-dependent vectors.
This is an operator-norm assertion from discrete TT*, not weak convergence
of finitely many observable pairings.

For r=s, uniform smooth Taylor expansion at u=c/N gives

N[S_r(x,y)-S_r(x+c/N,y+c/N)] = -c( S_(r,x)+S_(r,y) )+O_c(N^-1),
a_(r,N)(x,y) conjugate(a_(r,N)(x+c/N,y+c/N))
=|a_(r,0)(x,y)|^2+O_c(N^-1).

Thus the surviving matrix is N^-1 times the sampled kernel k_c of A13,
with O_c(N^-2) entry error and O_c(N^-1) operator error. The common raw
factor e(3N/8) cancels in the product. No odd-N residue-class phase remains
in these diagonal terms.

For the isometry J_N from normalized l2_N to step functions,
(J_N* f)_j=N integral_[j/N,(j+1)/N) f.
Hence the integral kernel of J_N B J_N* is N B_(ij) on each cell pair.
For B_(ij)=N^-1 k_c(i/N,j/N), this is exactly the piecewise constant sampled
kernel, which converges uniformly, hence in ordinary HS and operator norm,
to k_c. The scale factor N is indispensable and is correctly present.
Adding the already small off-diagonal branches and parametrix remainder
proves the full operator-norm convergence A12.

A bounded smooth square kernel is Hilbert-Schmidt, so K_c is compact.
Circle gluing is also correct: y->y+1 shifts the branch label; reducing
r modulo 4 changes (partial_x+partial_y)S by -2 times an integer. The x+1
identity adds -2 to the same derivative before branch reduction. The
resulting factors e(2c) equal 1, with matching amplitude and derivative
gluing. Compactness itself does not require this stronger periodicity.

A decisive adversarial negative control is worth retaining. At tau=0,
K_c^cat=0 for odd c. Nevertheless every quantum B_(N,c)^cat has norm 1.
For fixed odd c and N>c its rank-one Fourier mode has label
(inv2*c) mod N=(N+c)/2, which escapes to infinite centered frequency.
For even c, the classical compression has rank one, norm 1 and square zero.
Thus neither weak Egorov nor the cat classical compression alone proves
A12 or a strict one-step contraction. The actual nonzero-tau off-diagonal
branch estimate is exactly the additional ingredient needed to eliminate
this obstruction. The candidate includes it.

## 5. Correct ordinary/raw midpoint signs and Koopman identification

For an integer c and q-Fourier mode b,

(-1)^(bc)e_N(b(j+inv2*c))=e(b(j/N+c/(2N))).

The exponent difference is the integer bc, so there is no extra odd-c sign.
Therefore ordinary quantization of f(q)e(cp) is supported exactly on the
coordinate offset k=j+c, with coefficient F_N(j)=f((j+c/2)/N). Reducing k
modulo N does not change this identity. Its normalized HS norm is exactly
N^-1 sum_j |F_N(j)|^2.

For arbitrary such coefficient vectors, direct matrix multiplication proves

<F_N,B_(N,c)G_N>_(l2_N)
=<Op_N(i_cf),Ad(U_N)Op_N(i_cg)>_(normalized HS).

The candidate's complex conjugations and the order of f and g are correct.
There is no missing N or sqrt(N), and no commutation of compression with
the full superoperator is presumed.

The orientation of the classical map was separately checked. Direct
substitution of the raw M kernel gives
M W(a,b)=W(3a+4b,2a+3b) M.
This is pullback by S in (q,p) coordinates. The Weyl commutator gives
-2N sin(pi omega/N), and its classical limit is X_g/(2pi), with
X_g=(g_p,-g_q). Since U=E M, the complete forward adjoint therefore gives
pullback by G=S composed with Phi_g^(tau/(2pi)). Using G inverse here would
be a convention error; the candidate uses the correct G.

For fixed trigonometric polynomials f,g and fixed c, O8 applies with a fixed
H5 norm. The first argument in O9 has fixed finite frequency support, so
its low-band hypothesis is satisfied for every sufficiently large N; the
second is the smooth pullback by G. These results pass the right-hand pairing
to <i_cf,C_G i_cg>. On the left, the midpoint step functions converge in L2
to f,g and A12 gives the norm limit. Density and boundedness prove
K_c=i_c* C_G i_c on all of L2(T).

One can also check the phase sign at zero time from the generating function:
S_x is the output momentum and -S_y the input momentum. Thus
-c(S_x+S_y)=c(p_input-p_output), exactly the phase left by the i_c projection
of the Koopman pullback. This agrees with the raw midpoint derivation.

## 6. Actual mixing, compact spectrum and one common finite power

The actual G preserves normalized area, making C_G unitary. For c!=0,
every h=i_c f has zero area mean. O11 extends from smooth to zero-mean L2
observables by smooth approximation and Cauchy-Schwarz; unitarity makes the
approximation errors uniform in the iteration number.

If K_c f=lambda f and |lambda|=1, then with P_c=i_c i_c*,
P_c C_G(i_c f)=lambda i_c f. The projected vector has the same norm as the
unprojected unitary image. Pythagoras therefore forces the perpendicular
component to vanish, so C_G(i_c f)=lambda i_c f. Its self-correlation has
constant modulus ||f||^2 and cannot tend to zero, contradicting actual-area
mixing. This excludes all unit-circle eigenvalues of K_c.

Compactness is critical: any nonzero spectral point is an eigenvalue, and
nonzero spectral values cannot accumulate away from zero. Since K_c is a
contraction, it follows that r(K_c)<1. The spectral-radius formula then
gives a finite L_c with ||K_c^(L_c)||<1/2. A strict bound on ||K_c|| itself
is not required. No dimension-dependent eigenvector or diagonalization
estimate appears in this argument.

Take epsilon=1/2 in the simultaneous two-cutoff statement. Only finitely
many positive c<C0 remain. Fixed-c operator-norm convergence implies
convergence of each fixed L_c power. Indeed
(J_N B J_N*)^ell=J_N B^ell J_N* because J_N*J_N=I, and its norm is the matrix
power norm. Increase one N0 so all these finitely many powers have norm
at most 3/4. Set L=max(1,L_c for c<C0). Exact contractivity of B makes all
higher powers no larger, so this single L works for every small offset.
For c>=C0 the one-step bound 1/2 gives ||B^L||<=2^-L<=1/2.

The negative-offset identity is exactly
B_(-c)=T_(-c) conjugate(B_c) T_c,
where (T_c f)(j)=f(j+c). It is a permutation-unitary conjugation and complex
conjugation, not an assumed reflection symmetry of U. It applies to every
power. Every nonzero residue at odd N has a representative +/-c with
1<=c<N/2, so the same L,N0 and rho=3/4 cover all offsets.

Writing m=qL+r with 0<=r<L gives
||B^m||<=rho^q<=rho^-1 exp[-(-log rho)m/L].
Thus A2 follows with C=rho^-1 and gamma=(-log rho)/L, uniformly in c,m,N
past the single startup threshold.

## 7. Exact family, all-band mask and scope

The rooted trace identity, injective union over c, and occupation-order
argument were already independently checked in the macro review and were
reconstructed in this extension's controls as well. A18 has at most N
offsets, O_b(N) powers, the trace prefactor N, and the original N^-2
normalization. This gives O_(a,b,w)(N exp(-gamma aN)). The modulus is taken
after each signed path contraction, never before on individual path weights.

The condition ord(c) not dividing m makes every word at that offset genuinely
off-charge in any positive band, including bands above the plateau. When
ord(c) divides m, both balanced and off-charge words can occur, and the
unmasked trace cannot separate them. At N|m the proposed admissible-offset
set is indeed empty, since every shift order divides N. These cases are
retained rather than silently reclassified.

A1 controls powers of each individual offset compression. It does not on
its own give contraction of arbitrary products with changing offsets. A
separate word-family corollary would require its own exact block identity,
run structure, counting, masks and overlap proof. None is included in this
verdict.

## 8. Independent bounded evidence and remaining gap

`independent_checks.py` imports no candidate or repository verifier. It uses
exact Gaussian rationals, integer exponents and rational polynomial
integration. Its bounded tests include:

- 106,743 ordinary/raw midpoint exponent checks at odd N<=43;
- direct raw-kernel metaplectic intertwining, including wrapped/negative
  indices and labels, to check the forward-G orientation;
- normalized-HS sector pairings for independently built complex rational
  unitaries in dimensions 3,5,7;
- all negative-offset power conjugacies through power 4 in those dimensions;
- 1,721 scaled TT* Schur row sums with their near-diagonal cutoff;
- fixed-c cat compression and escaping-alias controls through c=99;
- exact integration of piecewise-constant kernel HS discretization errors,
  checking the J_N normalization and factor N;
- quotient/remainder arithmetic for the uniform finite-power conclusion;
- 397,394 occupation-vector/offset cases, preserving both balanced and
  unbalanced examples at divisible times.

These are finite algebraic controls. They do not simulate fixed-tau quantum
norms, establish classical mixing numerically, or replace any analytic limit.
Normal and optimized runs, an injected-failure check, source snapshots,
checksums and exact commands are recorded in the separate manifest.

No gap remains in the new extension implications, relative to the expressly
identified inherited inputs. No shrinking-coupling or varying-map theorem,
effective threshold, quantitative gamma, full signed defect, arbitrary
occupation mask, plateau correction, stationary-label identification, or
higher factorial comparison has been proved. The macro report is not
retrospectively enlarged by this separate result. TRACE-005 and BGS remain
open.
