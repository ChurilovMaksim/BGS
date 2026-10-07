# Independent audit: macroscopic coordinate-translation path pairs

## Normalized claim and primary verdict

**Proved as written.** For the unchanged odd-dimensional raw operator
U_N=exp(i tau N A_N) M_N at the literal, fixed tau=10^-80, and every fixed
0<delta<1/2,

sup_{delta <= c/N <= 1-delta} ||B_(N,c)|| -> 0,
B_(N,c)(j,k)=U_N(j,k) conjugate(U_N(j+c,k+c)).

The norm is the ordinary induced l2 norm; all matrix indices are modulo N.
For bounded w supported in a fixed [a,b] contained in (0,infinity), the
N^-2-normalized sum over any chosen macroscopic translation sets is eventually
O_{a,b,w}(N 2^(-aN)). If every chosen shift has order not dividing m, it is
an exact, once-counted off-charge subset. In particular unit shifts work on
any fixed positive band with b<1.

Candidate reviewed: `translation_family_proof.md`, SHA256
`49a24af2ca9e9628681ce08fcd023528f9b3bc5fbc578c7ec8cdfa11918b4f23`.
The verdict is an independent internal mathematical audit, not external
referee acceptance, an analytic formalization, or a theorem about the full
signed defect. The candidate's boundary-layer handoff was excluded from the
review and is not accepted by this verdict.

## 1. Source and dependency closure

The read-only canonical repository was `CANONICAL_ROOT`, with Git HEAD
`157277eeca8d8318976ea26bdbb1d3b1aa0d438a`. Applicable AGENTS, source-of-truth
hierarchy, conventions, research brief, claim ledger, registry, results and
open-obligation board were inspected. The ledger still treats FM-021/FM-022
as project analytic proofs and TRACE-005/BGS as open. No `.mathbox/` ledger
was found. The worktree was already being modified by other work; this audit
did not write in it. The receipt distinguishes the exact candidate pins,
unchanged load-bearing proof pins, and concurrent status/index drift.

Dependency graph:

1. Raw A_N and M_N definitions and odd-N Weyl convention.
2. Exact ordinary finite-shift dictionary and four-branch initial Gauss identity.
3. Global short-time analytic HJ graph, exact phase/amplitude lattice gluing.
4. Two-amplitude finite-difference residual and unitary Duhamel estimate.
5. Uniform derivative bounds and the C2 time-Taylor certificate at literal tau.
6. Exact branch/y translation of the entire phase correction.
7. Two independently reconstructed actual-symbol Fourier witnesses.
8. All-parameter character separation and a distinct alias-safe upper bound.
9. Local discrete TT*, analytic-zero-set cutoff, compactness in u=c/N.
10. Exact compression/trace identity, occupation order, and aggregate count.

Items 1-5 and the local TT* method in item 9 are inherited from
`fixed_map_path_model.md` and `four_branch_parametrix.md`, the common support
of FM-021/FM-022. They were read and reconstructed below rather than accepted
from prior verdicts alone. Neither FM-021's stochastic mixing conclusion nor
FM-022's reversed-path multiplicity theorem is a premise. FM-023, the Weyl
arithmetic translation theorem, is a different statement and is not needed.
The stationary-label WKB character formulas are also not needed.

The candidate's contribution is the coordinate-translation specialization,
its exact nonlinear translation factors, the two-mode exclusion of every
interior translation parameter, the compact-family upgrade, and its explicit
off-charge/once-counting interpretation. The original local WKB and TT*
arguments remain credited to the prior sources. Searching the maintained
mathematics and records did not reveal an existing identical translation-family
theorem; this is a bounded repository comparison, not a world-priority claim.

All leaves needed here are elementary algebra, internally reconstructed
analytic arguments, or the expressly stated raw-model convention. No unverified
specialized external theorem or continuous FIO theorem is imported. Finite
controls below support exact algebra only.

## 2. Raw quantizer, all branches, and wraparound

For odd N, inv2=(N+1)/2. The exponent difference between
(-1)^(kl) e_N(k(j+inv2*l)) and e(k(j/N+l/(2N))) is the integer kl.
Consequently the prescribed raw operator acts exactly by
sum c_(kl) e(k(x+h*l/2)) f(x+h*l), with l in {-1,0,1}.
This verifies the necessary half-shift and the sign convention.

For P=3j^2-2jk+3k^2 and t=j-3k, direct expansion gives
P-3t^2=16jk-24k^2. The four-branch sum is the finite Gauss sum
sum_{r mod 4} e((-3Nr^2+2tr)/8)=2e((-3N+3Nt^2)/8).
Its entire modular core has 32 cases: odd N modulo 8 and t modulo 8. An
independent exact calculation in Q[z]/(z^4+1) verifies all 32. If
8 inv8=1+mN, then m=-N modulo 8. The preceding divisibility converts the
sum, with its e(3N/8) prefactor, to precisely e_N(-inv8 P)/sqrt(N).
Thus this is the actual raw M_N in every odd dimension, including composites.

The initial polynomial identities are, for every integer r,

S_(r+4)-S_r = x-3y-3r-6,
S_r(x+1,y)-S_(r-3)(x,y) = -2r-2y+3,
S_r(x,y+1)=S_(r+1)(x,y),
S_r(x+4,y)-S_r(x,y) = -3x+y+r-6.

Each is preserved at evolved times by HJ uniqueness. The x-gradients change
by integers or not at all, and g is periodic in x and p. Their affine
additions are time-independent. On x=j/N,y=k/N each required gluing phase,
multiplied by N, is an integer. Reducing branch labels modulo 4 therefore
leaves the summed sampled kernel unchanged under x or y translation by 1.
Individual branches are not falsely assumed to be 1-periodic.

All finite transport operators inherit the same gluing: integer momentum
shifts leave symbol derivatives unchanged, and the affine phase additions
cancel from the finite-shift Taylor remainder after the linear gradient
has been removed. Uniqueness then gives amplitude gluing without an extra
factor. This proves that the summed parametrix can be evaluated directly at
(x+u,y+u) in [0,2]^2, even across either or both lattice wraps. Its error is
still the corresponding actual periodic U_N error. There is no discontinuous
branch-selection operation to differentiate.

## 3. Inherited parametrix and literal-time constants

The Hamilton-Jacobi sign is S_t=g(x,S_x)/(2pi): differentiating e(S/h)
produces 2pi i S_t/h, matching iA_N/h. With p=S_x the characteristic field
is (-g_p,g_x)/(2pi). The symbol is real analytic and periodic.

Direct finite-shift expansion gives
D1 a=(g_p/(2pi))a_x+(g_xp+g_pp S_xx)a/(4pi).
The prescribed a0 and a1 equations cancel residual orders h^0 and h^1 after
the h^-1 HJ term. The remaining factored residual is O(h^2). Multiplying by
the sqrt(h) kernel prefactor gives entry residual O(h^(5/2)), hence operator
residual O(h^(3/2)). Exact matching at t=0 and unitary Duhamel give operator,
and therefore entrywise, error O(h^(3/2)). Fixed higher derivative bounds
needed for the two transports exist on the fixed compact enlarged charts.
Only a fixed finite number is used; no all-orders convergence is assumed.

The coarse constants withstand reconstruction. Sparse Fourier convolution
of the raw symbol gives weighted coefficient sum 51451/1000<52 and support
|(k,l)|<10. Thus 52*63^4<10^9 bounds coordinate derivatives through order 4;
10^12 safely bounds multilinear derivatives through order 3 of the
characteristic field in maximum norm, including the finite-dimensional
conversion factors.

At T=10^-20, BT=10^-8. The first three flow derivative bounds in the source
follow from the differentiated ODE and its integral variational equations.
The initial map (a,y)->(a,(y+r-3a)/4) has maximum-norm derivative 1 and zero
higher derivatives. In particular X_a>=1-2BT>0 and X-a is bounded, so the
projection is globally strictly monotone and onto, for every y and r.
It has a global analytic inverse. One can conservatively bound the inverse
map's first derivative by 4 and its second and third derivatives by 1 on
this interval using the ordinary implicit differentiation formulas; the
source's bounds 100 and resulting p-derivative bound 10^4 are therefore
more than sufficient. All of this is uniform on real charts and branch
shifts, despite the unbounded value of the initial momentum on the full plane.

Differentiation of HJ yields exactly
S_tt=(g_p g_x+g_p^2 p_x)/(4pi^2).
For H=g_p or g_x, chain differentiation through order 2 bounds every
H(x,p(x,y)) derivative by 5*10^17. The factorial-weighted C2 derivative norm
is below 10^19 and is submultiplicative. The corresponding norm of p_x is
below 10^5. Thus the numerator is bounded by 10^38+10^43, comfortably below
10^50 even before division by 4pi^2. Therefore

||S(t)-S(0)-t g(x,S_x(0))/(2pi)||_(C2) <= (10^50/2)t^2

is a valid literal-time certificate. This audit does not replace a specified
physical time with a merely unspecified sufficiently small time.

Products of two four-branch expansions give 16 N^-1 kernels with uniformly
smooth amplitudes, plus entrywise O(N^-2), hence operator O(N^-1), error.
The constants are uniform in u in [0,1]. For every r,s the initial translated
phase is explicitly a sum of a function of x, a function of y, and a constant:

S_r^0(x,y)-S_s^0(x+u,y+u)
= ((r-s)/4+u/2)x + (3(s-r)/4+u/2)y
  + u^2/2+su/2+3(s^2-r^2)/8.

Its removal is by finite-dimensional unitary diagonal multipliers and has
no norm cost, regardless of the u-dependence of those multipliers.

## 4. Exact nonlinear translation and every interior parameter

For every r, S_r(t,x,y)=S_0(t,x,y+r) follows from equality of their initial
data and the same HJ equation, with y a parameter. Hence exactly
R_r(t,x,y)=R_0(t,x,y+r), where R=S-S^0. The x+4 and y+4 phase identities
above show that R_0 is separately 4-periodic in x and y. Its normalized
Fourier coefficients on [0,4]^2 are therefore well defined.

Independent convolution of r(q), r(q+1/2) and the positive momentum cosine
term gives

ghat(0,1)=(-3-4i)/1000,
ghat(1,1)=(3+4i)/2000.

At t=0, a symbol mode (k,1) becomes the unique mode
(k-3/4,1/4) in S_(0,t). No negative-momentum or momentum-free term can supply
these frequencies. Mixed differentiation multiplies its coefficient by
-2pi(k-3/4)(1/4). The two coefficients, divided by pi, are

at (-3/4,1/4): -9/8000 - (3/2000)i, modulus 3/1600;
at ( 1/4,1/4): -3/16000 - (1/4000)i, modulus 1/3200.

The coefficient remainder is at most (10^50/2)tau^2=5*10^-111. At tau=10^-80,
each exact Fourier coefficient A_i of R_(0,xy)(tau) therefore has modulus
at least pi*tau/6400. A normalized Fourier coefficient is bounded by the
supremum norm, so there is no missing area or Fourier normalization factor.

For the full nonlinear correction, not only its first Taylor term,
translation gives the coefficients of Phi_(r,s,u),xy exactly as

A_i [e(r/4)-e(s/4+(i-1/2)u)], i=0,1.

Putting z=e((s-r)/4-u/2), the brackets have moduli |1-z| and |1-ze(u)|.
Triangle inequality and sin(pi d)>=2d for 0<=d<=1/2 give

max(|1-z|,|1-ze(u)|) >= |1-e(u)|/2 >= 2 dist(u,Z).

Both brackets can vanish only if e(u)=1. Thus every one of the 16 branch
pairs has a nonzero mixed-derivative Fourier coefficient at every interior
u, including all rational alias parameters. For u in [delta,1-delta], its
modulus is at least pi*tau*delta/3200. There is no additive u-independent
nonlinear error that could spoil the small character separation.

The nonzero Fourier coefficient certifies that the mixed derivative is
nonidentically zero on the plane. Real-analytic continuation then forbids
it from vanishing identically on the open unit square or any open rectangle.
This local consequence is essential to the zero-set argument.

Separately, the first-time mixed derivative of a single correction is
(g_xp/4-3g_pp/16)/(2pi), whose absolute value is below 10^9. Consequently
sup|Phi_xy| <= 2*10^9*tau+10^50*tau^2 < 1/4.
This independent small upper bound is what rules out nonzero sampling aliases.
The nonvanishing certificate alone would not do so.

Endpoint negative controls were retained: at u=0 the r=s brackets vanish;
at u=1 they vanish for s-r=2 modulo 4. At c=0 modulo N the actual matrix
is P=|U|^2, whose norm is 1. Neither the compactness proof nor this review
extends to shrinking boundary layers.

## 5. Uniform discrete TT* and ordinary HS normalization

All needed rectangles can be chosen inside a slight enlargement of the
unit coordinate square, with horizontal width below 2. In the actual
unit-square rows, d=|x-x'|<=1. If c<=|phi_xy|<=C<1/4 has fixed sign, then
psi_y=phi_y(x,y)-phi_y(x',y) has magnitude between cd and Cd and fixed sign.
The increments Delta_j=N[psi((j+1)/N)-psi(j/N)] have the same bounds and
stay strictly below 1/2 in modulus. Their distance from the integers is
therefore bounded below by cd. Since psi_yy=O(d), the total variation of
Delta_j is O(d). Discrete summation by parts with reciprocal
(e(Delta_j)-1)^-1 gives the unnormalized oscillatory sum O(1/d), including
endpoint and amplitude-variation terms. The reciprocal's total variation
is O(d)/d^2=O(1/d).

It follows that TT* has diagonal entries O(1/N) and off-diagonal entries
O(1/(N|i-i'|)); Schur gives ||T||^2=O(log(2N)/N). Smooth supported amplitude
families with uniform finite derivatives give uniform constants on a fixed
good rectangle. No normality is needed.

A technical convention worth making explicit: an abstract version of this
local lemma on arbitrarily wide rectangles would need a width-dependent
alias condition. The source's proof and this candidate use unit coordinate
charts and can choose smaller rectangles, so that issue does not restrict
or invalidate the stated theorem.

For uniformity, let an arbitrary sequence of admissible u_N converge along
a subsequence to u_* in the same compact interval. For each fixed branch
pair, Phi_xy(u_*) is real analytic and nonidentically zero, so its zero set
has area zero. This follows by one-variable analytic slicing and Fubini;
identically zero slices lie in the zero set of a nonzero transverse analytic
coefficient. Connected analytic continuation supplies the needed nonidentity
on all chart pieces.

Choose a fixed smooth cutoff covering that zero set and the chart boundary,
with support area as small as desired. The omitted kernel has ordinary HS
norm squared at most M^2 N^-2 sum chi(i/N,j/N)^2, which tends to at most
M^2 times that small area. This bound is uniform in the varying amplitudes
and u_N; their convergence is unnecessary. It is the unnormalized matrix HS
norm and directly dominates operator norm. Normalized channel HS would lose
a factor sqrt(N) here and is not used.

The remaining compact support has a finite rectangular partition with mixed
derivative of fixed sign and bounded away from zero at u_*. Smooth dependence
on u preserves half each lower bound along the subsequence. All higher
phase and amplitude derivatives needed in TT* are uniformly bounded there.
The finite sum of good kernels tends to zero. Taking N to infinity first,
then shrinking the fixed bad region, proves norm o(1) on this subsequence.
A contradiction/compactness argument establishes the supremum over u.
Apply it to the finite set of 16 pairs and add the O(N^-1) remainder.

No finite-type exponent, bound on the number of zeros, or quantitative
startup dimension has been presumed. All small-lower-bound constants may
depend on fixed tau, delta and the cutoff.

## 6. Compression, exact family, and counting

Let E_j^c=|j><j+c|. Under the ordinary HS inner product these are orthonormal,
and the (i,j) compression coefficient of Ad(U) is
Tr((E_i^c)^* U E_j^c U*)=U_(ij) conjugate(U_(i+c,j+c)).
Ad(U) is unitary, so the compression has norm at most 1 exactly. Invariance
of the compressed subspace is neither claimed nor needed. Changing all
coordinate-vector inner products by the same 1/N factor does not change
these induced operator norms.

Multiplication and ordinary trace give exactly
Tr B_c^m=sum_{x in (Z/N)^m} A_U(x) conjugate(A_U(x+c)).
Every repeated coordinate remains in this rooted tuple expansion. At zero
coupling the matrix is N^-1 e_N(inv2*c*(j+k+c)); it has rank one and norm 1.
For every nonzero c, including nonunits, its square is zero because the
intermediate character is e_N(c*k) and its full geometric sum vanishes.
This distinguishes the actual nonlinear fixed-tau norm mechanism from an
invalid claim of a small cat one-step norm.

For independent uniform coordinate phases, D_theta multiplies A_U(x) by
the character of its occupation vector. Averaging a paired character is 1
exactly when the occupation vectors agree and 0 otherwise. This derives T16
without modifying U's deterministic entries or presuming random dynamics.
The phase distribution is specified in the candidate's target contract.

For any fixed nonempty first word x, its translated second word x+c determines
c uniquely from coordinate zero. Thus (x,c)->(x,x+c) is injective. The ordinary
trace already uses rooted tuples; adding a cyclic-rotation or marked-cut
multiplicity would be wrong and is not done in the candidate.

A shift c has d=N/gcd(c,N) elements in every coordinate-label orbit. An
invariant integer occupation vector is constant on each such orbit, so its
total mass is a multiple of d. Therefore d not dividing m is sufficient
for off-charge membership; d>m is a useful stronger condition. The converse
is not asserted. Unit c has d=N, so every positive m<N is off-charge. Such
pairs are consequently disjoint from all equal-occupation cyclic/reversal
pairs. When d divides m, balanced examples must be retained rather than
silently removed by a mask. Independent controls include composite N=9 and
nonunit shifts, as well as the m=0 boundary for the occupation implication.

Finally, choose the common eventual threshold with sup ||B_c||<=1/2. Then
|Tr B_c^m|<=N||B_c||^m<=N2^-m even for nonnormal B_c. There are at most N
shifts and at most (b+2)N relevant positive powers, giving

N^-2 sum_m |w(m/N)| sum_c |Tr B_c^m|
<= (b+2)||w||_infinity N 2^(-aN).

The absolute value is taken only after each exact signed contraction, not
on individual path weights. This proves T4 with its original N^-2
normalization. Arbitrary bounded weights need no smoothness for this bound.

## 7. Independent finite evidence and exact scope

`independent_checks.py` was written without importing the candidate checker,
its results, or repository modules. It reconstructs the symbol by sparse
convolution and uses exact Gaussian rational arithmetic for independent
complex rational unitaries. Its coverage includes:

- all 32 residue cases in the modulo-8 Gauss reduction;
- all 16 initial translated branch pairs and exact polynomial gluing checks;
- raw/ordinary half-shift and lifted cat controls at odd N=3,...,41;
- the two Fourier coefficients and rational literal-time inequalities;
- all branch pairs for rational interior parameters of denominator at most 80;
- retained endpoint common-zero cases;
- exact compression and rooted trace identities for N=3,m<=5; N=5,m<=4;
  N=7,m<=3, including c=0;
- independent occupation-grouped phase averaging for these N with m<=3;
- 751,608 occupation-vector/shift cases at N in {3,5,9}, total mass 0..10,
  including 72 balanced cases rather than filtering them away;
- 8,280 rooted-word once-counting cases through length 4 at N in {3,5,9}.

The rational-parameter checks are bounded tests only. The continuous
all-parameter claim rests on the exact ratio-character argument in Section 4.
The occupation enumeration is over all weak compositions in its declared
range, not a sample of selected words. Finite rational unitaries test universal
algebra and are not surrogates for the actual fixed-tau asymptotic theorem.
No rescaled-coupling numerical norm computation is offered as evidence.

Exact commands, completion statuses, source SHA256 values, optimized-mode
comparison and injected-failure check are recorded in `manifest.json`.
`obligations.json` provides a machine-readable obligation matrix.

## 8. Remaining gap and strongest safe use

No missing implication was found inside the scoped macroscopic theorem.
It can safely be used as a selected signed off-charge-family deletion with
its exact admissibility condition and N^-2 normalization. It supplies neither
a bound for the complementary off-charge sum nor a bound after imposing an
arbitrary additional path mask. Shrinking translations, the unreviewed
boundary-layer sketch, other path pairs, plateau correction, stationary-label
dictionaries, and every higher factorial comparison remain outside this
verdict. TRACE-005 and deterministic BGS remain open.

The cheapest next check before any promotion is to verify that the candidate
and load-bearing source hashes still match this receipt, reconcile the
concurrently modified status files, and preserve these boundaries verbatim.
This audit itself performs no canonical integration, publication, commit,
or push.
