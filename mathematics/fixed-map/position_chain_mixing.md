# Position-chain mixing, cyclic ramp and a marked three-link estimate

**Stable claim ID:** BGS-FM-021.
**Base:** `0ffb20cc152d0ddd2620887e46d21d1120b95fd8`.
Project proof with independent internal review; no priority or external referee claim.

## 1. Exact model, theorem and proof ownership

Use the unchanged odd-dimensional U_N, fixed tau=10^-80 and ordinary symbol
in `fixed_map_path_model.md`. Set P_N(x,y)=|U_N(x,y)|² and J_N(x,y)=1/N. The canonical
position-chain theorem is

limsup_(odd N ->infinity) ||P_N−J_N||op <=10^-64.

Consequently there is N_0 (not made effective here) such that for every
odd N>=N_0 and every integer L>=0,

||P_N^L−J_N||op <=2^-L.

For a cyclic word x of length m, put A(x)=product_j U_(x_j,x_(j+1)) and let
d(x) be its least cyclic period. Then D_m=sum_x d(x)|A(x)|² counts exactly
the ordered pairs related by cyclic rotation. For every fixed 0<a<b,

sup_(aN<=m<=bN)|Tr P_N^m−1|->0,
sup_(aN<=m<=bN)|D_m/m−1|->0.

In fact the errors are exponentially small up to polynomial prefactors.
Section3 gives a separate exact MARKED expression and its bound; no
once-counted trace-pair identification is asserted for that expression.

The common self-contained dependency is `four_branch_parametrix.md`.
Sections2–3 below retain the accepted proof of the hash-stable source
156808b1febd7b61a8aff4e4756314934e5cb6b471c7e5a2f15a6f5f64f216af,
with its independent audit at `../record/marked_path_independent_review_20261006.md`. The stronger
constant-gap statement subsumes the earlier seven-cut cyclic-ramp argument,
which is now provenance only, not a second canonical theorem source.
The proof requires neither FM-007 nor FM-018, classical mixing, a noisy
comparison, or any later uniqueness/reconnection continuation.

## 2. Proof of the constant gap

The reviewed construction gives, with h=1/N,

U_jk = e(3N/8) sqrt(h)/2 sum_(r=0)^3 e(S_r(t,x,y)/h) a_r(t,x,y) + O(h^1.5),

where a_r is the leading smooth transport amplitude (higher h terms can be included in the O(h^1.5)), a_r(0)=1, S_rt=g(x,S_rx)/(2pi), and all bounds are uniform in grid indices for fixed t. Thus P has entrywise remainder O(h²), operator remainder O(h), and sixteen leading kernels h a_r conjugate(a_s)e((S_r-S_s)/h)/4.

For r=s, their sum is h d(x,y), d=(1/4)sum_r |a_r|². The transport equation has real zeroth-order coefficient (g_xp+g_pp S_xx)/(4pi). The reviewed bounds |derivatives of g through order4|<10^9 and |S_xx|<=10^4 imply its absolute value is <10^14 on |t|<=10^-20. Along a characteristic the amplitude therefore satisfies |a_r-1|<=exp(10^14|t|)-1. At t=10^-80 this is <2*10^-66, hence |d-1|<10^-64. The operator norm of the difference of this sampled kernel and J is bounded by its maximum absolute row and column sums, hence <10^-64.

For r≠s, let phi_rs=S_r-S_s. Its initial phase difference is separable (a linear function of x,y plus a constant), so phi_rs,xy(0)=0. On the four-periodic phase correction, the Fourier coefficient of partial_t phi_rs,xy(0) at frequency (25/4,1/4) is

-(pi/128) e(-alpha/(2pi)) [e(r/4)-e(s/4)].

Indeed the symbol term B_7=1/200 times the positive momentum exponential supplies e(r/4-alpha/(2pi))/(800pi) in S_rt, and the mixed derivative multiplies by -(2pi)^2(25/4)(1/4). The bracket has modulus sqrt(2) or 2. The C² time-Taylor bound therefore leaves a remainder <=10^50 t² in this coefficient. At the specified tau this is 10^-110, strictly below sqrt(2)(pi/128)10^-80. Consequently phi_rs,xy is nonidentically zero for all twelve pairs.

The phases are real analytic. Also after factoring their initial separable phases, their mixed derivatives are uniformly O(tau), with magnitude <1/4 by the same derivative bounds. The local discrete TT* argument in Section6 of `four_branch_parametrix.md` applies unchanged: remove an arbitrarily small neighborhood of the analytic zero set, split the complement into finitely many rectangles with c<=|phi_xy|<=C<1/4 of fixed sign, and obtain local operator norm O(sqrt(log N/N)). Row-difference phase increments stay between c|x-x'| and C|x-x'|, so no nonzero sampling alias occurs. The removed kernel has limiting unnormalized HS norm bounded by its bounded amplitude times the square root of the removed area. Taking N→infinity and then the removed area→0 gives operator norm o(1) for each offdiagonal branch kernel.

Combining the four diagonal and twelve offdiagonal terms proves limsup ||P-J||<=10^-64, as stated. Since P is doubly stochastic, J is its reducing constant projection; (P-J)^L=P^L-J for L>=1. Contractivity and the eventual bound 1/2 give the stated powers (L=0 means I-J).

## 3. Exact marked contraction: one uniform link kills it

For L_i>=0 define

E_dist(L)=sum_(a1,a2,a3 pairwise distinct; b1,b2,b3) product_i (P^Li)_(ai,bi) product_i U_(bi,a_(i+1)) conjugate(U_(bi,a_(i-1))),

with indices mod3. If ANY one P^Li is replaced by J, this expression is exactly zero: sum over its bi is N^-1 times inner product of the two distinct columns indexed by the other two ports. This argument requires no mixing of the other two links, and includes L_j=0.

Choose k with Lk=max Li and replace only this link by Delta=P^Lk-J. Its entries obey |Delta_ab|<=2^-Lk. The WKB kernel bound gives q=max|U_ab|²<=C/N. Taking absolute values after this exact cancellation, the six U factors cost q³; summing each of the other two b indices against its stochastic P power costs 1. There remain N³ choices of a and N choices of bk. Thus

|E_dist(L)| <= C³ N 2^-max(Li).

For trace length m=L1+L2+L3+3, max Li>=(m-3)/3. Hence the complete marked contribution, even multiplied by m² and summed over all nonnegative triples, satisfies

|m² sum_(L1+L2+L3=m-3) E_dist(L)| <= C³ m² binom(m-1,2) N 2^(-(m-3)/3).

Every N^-2 smooth positive compact Heisenberg-band sum of this marked expression tends to zero exponentially, up to a polynomial prefactor. This closes the previous possible extra-N normalization loss for the MARKED expression and includes every short-link boundary. It does not bound an unmarked trace-pair family unless its exact multiplicities are separately controlled.

## 4. Cyclic-ramp corollary and exact signed residual

P is doubly stochastic and constants reduce it. For every m>=1,

|Tr P^m−1| <=(N−1)||P−J||^m <=N 2^-m

once N>=N_0. This uses the trace bound by dimension times operator norm;
normality is not assumed. WKB gives q_N=max|U_xy|²=O(N^-1), so q_N<=1/5
eventually. The exact cyclic multiplicity formula is

m Tr P^m−D_m =sum_x (m−d(x))|A(x)|² >=0.

Only proper-period words occur. For each proper divisor d|m, d<=m/2;
repeating a d-word has weight at most q_N^(m−d) times its single d-word
weight. Summing gives q_N^(m−d)Tr P^d<=N q_N^(m/2). At most m choices of
d and a multiplicity at most m give

0<=m Tr P^m−D_m<=m²N q_N^(m/2).

Thus |D_m/m−1|<=N2^-m+mN(1/5)^(m/2), uniformly for m in any positive
compact Heisenberg band. For smooth compactly supported w in (0,infinity),

N^-2 sum_m w(m/N)D_m -> integral xi w(xi) dxi.

Writing the exact signed remainder R_m=|Tr U_N^m|²−D_m, the pair CUE target
on that band is still exactly

N^-2 sum_m w(m/N)R_m -> integral [min(xi,1)−xi]w(xi) dxi.

In particular the required correction above xi=1 is negative. Exponential
mixing of P does not estimate this signed interference. The separate
reversal theorem removes only the explicitly defined reverse-cyclic family.

## 5. Why the marked estimate is not an unmarked theorem

There is no universal multiplicity factor converting Section3 into a
once-counted ordered trace-pair subset. Exhaustive N=3,m=6 block enumeration
in the accepted source gives 17,568 pairs of multiplicity3 and 936 of
multiplicity6. The primitive examples

((0,0,0,0,1,2),(0,0,0,0,2,1)),
((0,0,1,2,1,2),(0,0,2,1,2,1))

have these respective multiplicities; periodic roots do not explain the
difference. A proposed lexicographically first cut triple also need not
preserve a free endpoint. For target cuts (0,1,4), the m=7 pairs

x_b=(0,1,2,1,2,1,b), y_b=(0,2,1,b,1,2,1)

give canonical-selection mask (1,1,0) for b=0,1,2. The uniform endpoint
contraction then becomes N^-1(U* D_I U)_(a2,a1), not zero in general. For
U=I−vv^T/7, v=(1,2,3), a1=0,a2=1 it equals −6/49 exactly.

These finite counterexamples rule out the stated shortcuts; they do not
rule out every unmarking scheme, prove a nonzero actual-model residual, or
settle any asymptotic once-counted sum. General noncyclic interference and
all higher factorial orders remain open. No once-counted unmarking theorem is asserted.

## 6. Verification boundary

`../../computations/verification/actual_path_theorems.py` checks exact coefficients for all twelve
same-coordinate differences, exact rational amplitude/remainder comparisons,
and exact distinct-port uniform-link cancellation for a complex rational
unitary and boundary link lengths. The source and independent marked
verifiers are replayed with their hashes in `../../evidence/executions/20261006/path-theorems/receipt.json`.
Finite tests support the identified algebra only; the analytic N-limit rests
on the proof above and the shared parametrix. No finite-N experiment at
rescaled coupling is offered as evidence for the actual fixed-tau limit.
