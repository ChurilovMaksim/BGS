# Constant position-chain gap and marked three-link cancellation

Checkpoint RECONNECT-20261006-A; base main 0ffb20cc152d0ddd2620887e46d21d1120b95fd8. Disjoint research artifact, not repository promotion. Author proof; independent review requested. Actual U_N=exp(i tau N A_N)M_N, tau=10^-80, odd N. No noise or phase averaging.

## 1. Dependencies and exact scope

The previously independently reviewed four-branch discrete WKB construction is ../bgs_fio_route/four_branch_wkb.md; its raw-model and quantitative derivative audit is ../bgs_reversal_review/independent_audit.md. We use its finite transport construction, initial phases, C² time-Taylor bound 10^50, and the alias-safe local discrete oscillatory lemma. The previous diagonal proof ../bgs_signed_route/diagonal_path_ramp.md gives only a diverging N-scaled gap; the following strengthens that subsidiary result, not the deterministic spectral target.

Write P_N(x,y)=|U_N(x,y)|², J_N(x,y)=1/N. Then

limsup_N ||P_N-J_N||op <= 10^-60.

In particular, for all sufficiently large odd N, ||P_N^L-J_N||op <= 2^-L for every integer L>=0. The threshold is not effective here and may be immense at this fixed tau.

## 2. Proof of the constant gap

The reviewed construction gives, with h=1/N,

U_jk = e(3N/8) sqrt(h)/2 sum_(r=0)^3 e(S_r(t,x,y)/h) a_r(t,x,y) + O(h^1.5),

where a_r is the leading smooth transport amplitude (higher h terms can be included in the O(h^1.5)), a_r(0)=1, S_rt=g(x,S_rx)/(2pi), and all bounds are uniform in grid indices for fixed t. Thus P has entrywise remainder O(h²), operator remainder O(h), and sixteen leading kernels h a_r conjugate(a_s)e((S_r-S_s)/h)/4.

For r=s, their sum is h d(x,y), d=(1/4)sum_r |a_r|². The transport equation has real zeroth-order coefficient (g_xp+g_pp S_xx)/(4pi). The reviewed bounds |derivatives of g through order4|<10^9 and |S_xx|<=10^4 imply its absolute value is <10^14 on |t|<=10^-20. Along a characteristic the amplitude therefore satisfies |a_r-1|<=exp(10^14|t|)-1. At t=10^-80 this is <2*10^-66, hence |d-1|<10^-64. The operator norm of the difference of this sampled kernel and J is bounded by its maximum absolute row and column sums, hence <10^-64.

For r≠s, let phi_rs=S_r-S_s. Its initial phase difference is separable (a linear function of x,y plus a constant), so phi_rs,xy(0)=0. On the four-periodic phase correction, the Fourier coefficient of partial_t phi_rs,xy(0) at frequency (25/4,1/4) is

-(pi/128) e(-alpha/(2pi)) [e(r/4)-e(s/4)].

Indeed the symbol term B_7=1/200 times the positive momentum exponential supplies e(r/4-alpha/(2pi))/(800pi) in S_rt, and the mixed derivative multiplies by -(2pi)^2(25/4)(1/4). The bracket has modulus sqrt(2) or 2. The C² time-Taylor bound therefore leaves a remainder <=10^50 t² in this coefficient. At the specified tau this is 10^-110, strictly below sqrt(2)(pi/128)10^-80. Consequently phi_rs,xy is nonidentically zero for all twelve pairs.

The phases are real analytic. Also after factoring their initial separable phases, their mixed derivatives are uniformly O(tau), with magnitude <1/4 by the same derivative bounds. The local discrete TT* argument from the reviewed reversal proof applies unchanged: remove an arbitrarily small neighborhood of the analytic zero set, split the complement into finitely many rectangles with c<=|phi_xy|<=C<1/4 of fixed sign, and obtain local operator norm O(sqrt(log N/N)). Row-difference phase increments stay between c|x-x'| and C|x-x'|, so no nonzero sampling alias occurs. The removed kernel has limiting HS norm bounded by its bounded amplitude times the square root of the removed area. Taking N→infinity and then the removed area→0 gives operator norm o(1) for each offdiagonal branch kernel.

Combining the four diagonal and twelve offdiagonal terms proves limsup ||P-J||<=10^-64, in particular the looser displayed 10^-60. Since P is doubly stochastic, J is its reducing constant projection; (P-J)^L=P^L-J for L>=1. Contractivity and the eventual bound 1/2 give the stated powers (L=0 means I-J).

## 3. Exact marked contraction: one uniform link kills it

For L_i>=0 define

E_dist(L)=sum_(a1,a2,a3 pairwise distinct; b1,b2,b3) product_i (P^Li)_(ai,bi) product_i U_(bi,a_(i+1)) conjugate(U_(bi,a_(i-1))),

with indices mod3. If ANY one P^Li is replaced by J, this expression is exactly zero: sum over its bi is N^-1 times inner product of the two distinct columns indexed by the other two ports. This argument requires no mixing of the other two links, and includes L_j=0.

Choose k with Lk=max Li and replace only this link by Delta=P^Lk-J. Its entries obey |Delta_ab|<=2^-Lk. The WKB kernel bound gives q=max|U_ab|²<=C/N. Taking absolute values after this exact cancellation, the six U factors cost q³; summing each of the other two b indices against its stochastic P power costs 1. There remain N³ choices of a and N choices of bk. Thus

|E_dist(L)| <= C³ N 2^-max(Li).

For trace length m=L1+L2+L3+3, max Li>=(m-3)/3. Hence the complete marked contribution, even multiplied by m² and summed over all nonnegative triples, satisfies

|m² sum_(L1+L2+L3=m-3) E_dist(L)| <= C³ m² binom(m-1,2) N 2^(-(m-3)/3).

Every N^-2 smooth positive compact Heisenberg-band sum of this marked expression tends to zero exponentially, up to a polynomial prefactor. This closes the previous possible extra-N normalization loss for the MARKED expression and includes every short-link boundary. It does not bound an unmarked trace-pair family unless its exact multiplicities are separately controlled.

## 4. Exact finite checks and the surviving obstruction

check_exact.py uses Fraction arithmetic for rational Householder unitaries in dimensions3,4, links(1,2,3). It verifies the all-J, one-Delta, two-Delta formulas, equality contraction, triple equality, and distinct-port inclusion-exclusion recorded in the old handoff. exact_results.json records the outputs. This is finite algebra evidence only.

It also exhausts all N=3,m=6 words and all ordered three nonempty blocks, with distinct first vertices. Concatenation in block order1,2,3 is the first trace word and order1,3,2 the second. Both have six independently enumerated cyclic starts. Pairs related by cyclic rotation are discarded. Among the resulting ordered pairs, 17,568 have representation multiplicity3 and 936 have multiplicity6.

Examples in the same exact enumeration:

- ((0,0,0,0,1,2),(0,0,0,0,2,1)) has multiplicity3.
- ((0,0,1,2,1,2),(0,0,2,1,2,1)) has multiplicity6.

Both examples have primitive length6, so this is not merely periodic-start degeneracy. Therefore dividing the marked answer by a universal3 does not recover the actual ordered-pair subset. The required exact reweighting by inverse representation count depends on interior link histories, and its insertion destroys the simple Markov contraction. Exponential marked cancellation alone gives no bound for this reweighted signed sum.

## 5. Next genuine bottleneck

Find a canonical decomposition of actual path pairs, or a signed combinatorial inversion of the representation multiplicity, retaining a long freely summable link. Alternatively prove that the nonconstant-multiplicity portion is negligible with actual signed weights. The exact small counterexample rules out an unqualified universal prefactor; it does not rule out these mechanisms. Other noncyclic histories and all higher joint-trace orders remain outside this lemma. The full signed deterministic BGS target remains OPEN.

## 6. Executed canonical-encounter test and exact residual

A natural canonical rule does fail to preserve the free endpoint sum. For each fixed rooted ordered pair (x,y), enumerate all sorted triples of cut positions with pairwise distinct port values whose three blocks, rearranged as1,3,2, produce a rotation of y. Select the lexicographically first cut triple. This removes the cyclic labeling redundancy before choosing a unique encounter.

The exhaustive check in check_canonical.py finds the following N=3,m=7 example. Fix target cuts (0,1,4), ports (0,1,2), and vary only the last endpoint b:

x_b=(0,1,2,1,2,1,b), y_b=(0,2,1,b,1,2,1).

For b=0 or1, the sole cut triple is (0,1,4). For b=2, the admissible triples are (0,1,2), (0,1,4), (0,1,6), so the target triple is rejected. None of these pairs is cyclic-identical. Thus the canonical mask in the free endpoint is exactly (1,1,0), not a constant.

In general the uniform-link endpoint sum becomes

N^-1 sum_b I_b U_(b,a1) conjugate(U_(b,a2)) = N^-1 (U* D_I U)_(a2,a1),

rather than delta_(a1,a2)/N. For the real Householder U=I-vv^T/7, v=(1,2,3), a1=0,a2=1 and the exact mask above, this equals -6/49, since the omitted b=2 term is18/49. This residual is a local algebra obstruction to using the free-endpoint cancellation after canonical selection. It is not a claim that the complete canonically selected diagram has a nonzero asymptotic limit. A history-dependent mask also obstructs collapsing its link to P^L in the first place.

## 7. Executed combinatorial-inversion reduction

Let r(x,y) be the number of cyclic-label-quotiented admissible cut triples of a fixed primitive ordered pair; r<=binom(m,3). Exact union counting is

1_(r>0)=sum_(j=1)^r (-1)^(j-1) binom(r,j).

Equivalently each representation can receive weight1/r=integral_0^1 t^(r-1)dt. These formulas are valid but do not turn the first marked estimate into an unmarked bound. The jth term requires intersections of j different decomposition events. Their port/edge constraints couple previously free endpoints, exactly as in section6; the number of possible intersection orders grows with m. A fixed-complexity expansion cannot be truncated merely because each isolated marked three-link sum is exponentially small. One needs either a uniform summable estimate for the entire intersection hierarchy, or a structural cancellation preserving one free endpoint within every required intersection. Neither follows from the present constant-gap proof. This locates the next missing implication more precisely than generic “overcounting.”

Current disposition: constant-gap/marked theorem is an author proof awaiting independent review; universal unmarking prefactor is refuted by exact finite examples; the simplest lexicographic repair is refuted as a free-endpoint-preserving mechanism; inclusion–exclusion is an exact open reduction to growing-complexity coupled encounters. Full deterministic signed comparison remains open.

Additional arithmetic check: check_complex.py uses exact Gaussian-integer numerators for U=H diag(1,i,-1)H, H=I-vv^T/7 with v=(1,2,3), N=3. It verifies the distinct-port contraction vanishes exactly when each of the three links in turn is uniform. No floating arithmetic is used; common positive rational denominators are cleared. complex_results.json records three exact zeros.
