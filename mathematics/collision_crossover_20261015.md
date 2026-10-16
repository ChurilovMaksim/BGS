# A square-root-time crossover for the complete equal-directed-edge sector

**Stable claim:** `BGS-TRACE-089`. **Integration review:** 16 October 2026, author self-review.

**Exact scope:** m tends to infinity with m/sqrt(N) tending to a fixed finite c; not m of order N. Harer-Zagier is a classical external input.

Canonical status is [the claim ledger](../record/claim_ledger.md); source `S13` is preserved verbatim in [the imported record](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md#s13). Original execution counts are historical; fresh execution is recorded in [the integration receipt](../evidence/executions/20261016/chat-integration/receipt.json).


Date: 15 October 2026.

**Status and scope.** This note proves a limit for one exactly specified positive
subfamily of pairs in a quantum trace expansion. The abstract result assumes
only a uniformly dense, uniformly mixing doubly stochastic intensity matrix.
Its application to the prescribed BGS matrices inherits the project's FM-021
and four-branch parametrix inputs. It does not prove the full trace statistic,
phase-ensemble universality, deterministic Sine_2, or general BGS. No external
referee acceptance, formal verification, or world-priority claim is made.
The original note predates this canonical integration.

The previous packet gave an exponential lower bound for this subfamily at
m comparable with N. Here the entire subfamily, not just a finite number of
reconnection types, is evaluated asymptotically at m comparable with sqrt(N).
The probability measure used below is an exact normalization of deterministic
positive path weights, not an added random quantum operator.

## 1. Definition and theorem

Let U_N be unitary, P_ab=|U_ab|^2, and J_ab=1/N. Assume constants C>=1 and
0<=rho<1, independent of N, such that eventually

    max_ab P_ab <= C/N,       ||P-J||_(2->2) <= rho.             (1)

For a rooted closed word x=(x_0,...,x_(m-1)), x_m=x_0, put

    A(x)=product_(j=0)^(m-1) U_(x_j,x_(j+1)),
    nu_ab(x)=#{j:x_j=a,x_(j+1)=b}.

Define the COMPLETE equal-directed-edge contribution

    B_(N,m)=sum_(x,y:nu(x)=nu(y)) A(x) conjugate(A(y)).          (2)

If c(nu) is the number of rooted words of type nu, then exactly

    B_(N,m)=sum_nu c(nu)^2 product_ab P_ab^nu_ab.                (3)

**Theorem.** Suppose m=m_N tends to infinity and m/sqrt(N) tends to
c in [0,infinity), with c fixed and finite. Then

    B_(N,m)/m -> F(c) := sinh(c^2/2)/(c^2/2),   F(0)=1.         (4)

Let D_(N,m) be the exactly counted cyclic-rotation pair family. Under (1),

    D_(N,m)/m -> 1,
    [B_(N,m)-D_(N,m)]/m -> F(c)-1.                             (5)

No independence or genericity of the complex phases of U_N is assumed. Those
phases cancel exactly inside (2). Consequently (4) cannot, by itself, identify
the full spectrum of U_N. A flat Fourier unitary and a matrix with CUE-like
statistics have the same intensity hypotheses but need not have the same
full traces.

The endpoint c=0 is a regime statement with m->infinity, not a theorem for
fixed m or for arbitrary N-dependent c tending to infinity. In particular
one must NOT insert c=sqrt(N) in (4) to claim the Heisenberg limit.

## 2. Exact multiplicity and the closed-loop measure

For an edge table realized by a closed word, let R_a=sum_b nu_ab, with
sum R_a=m. On active vertices let t(nu) be a directed matrix-tree cofactor
of diag(R)-nu. For a one-vertex graph its value is the empty determinant 1.
The rooted BEST normalization, established independently in the prior note, is

    c(nu)=m t(nu) product_(a:R_a>0)(R_a-1)! / product_ab nu_ab!. (6)

This can also be proved directly by assigning labels to parallel edges,
choosing last-exit trees and then dividing out those labels. The factor m is
for a distinguished initial position. It must not be removed for periodic
words.

A useful bound, INCLUDING words with high multiplicities, is

    c(nu(x))/m <= F_m(x) := product_a R_a(x)!.                 (7)

Indeed a rooted arborescence chooses at most one of R_a outgoing edges at
each non-root vertex. Hence t(nu)<=product_(a != root) R_a;
insert this in (6), and discard the denominator >=1.

Write

    Z=Tr P^m,    Pr_loop(x)=product_j P_(x_j,x_(j+1))/Z.

For all sufficiently large N, Z>0, and (3) gives exactly

    B_(N,m)/m = Z E_loop[c(nu(X))/m].                         (8)

In fact Z->1 for EVERY m->infinity under (1). To check this without a
logarithmic lower restriction on m, put E=P-J. Since

    ||E||_HS^2=sum_ab P_ab^2-1 <= C-1,

Schatten Holder gives, for m>=2,

    |Z-1|=|Tr E^m| <= (C-1) rho^(m-2).                      (9)

The simpler N rho^m estimate suffices when m is comparable with sqrt(N).

## 3. A weighted bound that controls rare high-multiplicity words

This section is necessary. Showing that triple visits have small probability
would NOT alone justify discarding them from the expectation in (8).
Their multiplicities can be large.

Let pi be an equality partition on the m time slots, with v blocks, and
write I_pi for the event that all slots in each block have the same label.
Compared with a stationary open Markov word of length m, the closed-loop
law has density

    N P_(X_(m-1),X_0)/Z <= C/Z.

Reveal the word in time order. Each occurrence after the first in its
pi-block forces one already recorded label; its transition probability is
at most C/N. Fresh labels need not be required to differ, so their sums
cost at most one. Thus, with x=C/N,

    Pr_loop(I_pi) <= (C/Z) x^(m-v).                           (10)

Let a constraint pi_0 be supported on k specified slots and have b blocks
there. Its rank is r=k-b. The following strengthened inequality holds when
N>=C:

    E_loop[F_m I_(pi_0)]
       <= (C/Z) A_m(x) k! x^r,
    A_m(x)=product_(j=0)^(m-1)(1+jx).                        (11)

### Proof of (11)

For any word,

    F_m=product_a R_a! = sum_(sigma in S_m) I_(cycles(sigma)).

Apply (10) to the join of the cycle partition and pi_0. This gives

    E[F_m I_(pi_0)]
      <= (C/Z) sum_sigma x^(m-#blocks(cycles(sigma) join pi_0)).

The sum without pi_0 is A_m(x), by inserting one element at a time into a
permutation. Normalize the weights x^(m-#cycles) to a probability on S_m.
They are the permutation weights proportional to theta^(#cycles), theta=1/x.
Deletion of elements preserves this law: when a new element is inserted it
has m-1 non-singleton insertion positions, of weight one each, or a singleton
position of weight theta. This proves consistency directly.

The number of cycles merged by pi_0 depends only on the restricted permutation
on its k supported slots. Therefore the ratio of the joined sum to A_m(x) is

    [sum_(sigma in S_k) theta^(#blocks(cycles(sigma) join pi_0))]
                          / [theta(theta+1)...(theta+k-1)].

There are at most b blocks in the numerator join. Since theta>=1, the ratio
is at most k! theta^b/theta^k=k! x^(k-b), proving (11).

For m=O(sqrt(N)), A_m(C/N)<=exp[C m(m-1)/(2N)] is uniformly bounded.

Let Bad be the event that some vertex is visited at least three times or
some directed edge is used at least twice. A triple-vertex witness has three
slots and rank two. A pair of equal directed edges gives two equalities
on at most four slots; its rank is two for m>=3, including adjacent edge
times, where all three relevant labels must coincide. A union bound in (11)
yields

    E_loop[F_m 1_Bad]
      <= (C/Z) A_m(C/N)
          [6 binom(m,3)+24 binom(m,2)] (C/N)^2
      =O_(C,c)(N^(-1/2)) ->0.                                (12)

Equation (7) now shows that Bad has negligible contribution to B/m, not
merely negligible probability.

## 4. The collision diagram tends to a Poisson chord diagram

Associate an unordered pair of time slots with each repeated visit:

    eta_N = sum_(0<=i<j<m) 1_(X_i=X_j) delta_(i/m,j/m).

For c>0 this converges to a Poisson point process on
T={(s,t):0<s<t<1}, of intensity c^2 ds dt. Its total number K of chords is
Poisson with mean lambda=c^2/2. Conditional on K, the chord endpoints are
independent uniform pairs, equivalently a uniform matching of their cyclic
ordering. This assertion is about positive Markov-loop weights only.

Here are the moment details, including the mixing boundary.

For k pair constraints with 2k distinct selected slots, sort those slots
around the cycle. If their cyclic gaps g_j are at least
L_N=ceil(3 log N/|log rho|), then summing over the k paired site labels gives

    Pr_loop(all k equalities)
       = (1/Z) sum_(a_1,...,a_k)
                     product_(j=1)^(2k) (P^(g_j))_(label_j,label_(j+1))
       = N^(-k)(1+o(1)),                                    (13)

uniformly in the matching and selected slots. Here P^g=J+O(rho^g)
entrywise. If rho=0, take L_N=1 and the same calculation is exact.

The number of selections with a short cyclic gap is O_k(L_N m^(2k-1));
(10) bounds their total contribution by O_(k,C,c)(L_N/m)=o(1).
Riemann sums of (13) give the product factorial moment measures of the
claimed Poisson process.

Tuples of distinct collision edges sharing endpoints also have negligible
contribution. An equality graph on v slots with b connected components has
rank v-b and O_k(m^v) placements. Its bound from (10) is
O_k(m^v N^(-(v-b)))=O_k(N^(b-v/2)). Each component has at least two slots;
if a component has more than two, the exponent is negative. There are only
finitely many graphs at each fixed moment order. This handles overlapping
constraints, not just mutually disjoint pairs.

Thus all fixed marked factorial moments converge and are bounded. They
identify the Poisson law (its local exponential moment makes it moment
 determinate); alternatively apply finite inclusion-exclusion to disjoint
sets of chord positions and then truncate using the following bound.

On the event of no triple visits, K counts disjoint paired slots. For z>=1,
(10) and the number (m)_(2k)/(2^k k!) of k disjoint pairs give

    E_loop[z^K 1_no_triples]
       <= (C/Z) exp[(z-1) C m^2/(2N)].                      (14)

In particular

    E_loop[2^K 1_(K>L) 1_no_triples]
       <= 2^(-L) (C/Z) exp[3 C m^2/(2N)].                  (15)

This supplies the uniform integrability needed for counting ALL admissible
reconnections rather than truncating at a fixed number.

For c=0, (10) bounds the chance of a repeated pair by O(m^2/N)->0; (14)
and (12) give the expectation statement directly. Together with (9) this
gives B/m->1 without assuming m exceeds a multiple of log N.

## 5. Exact resummation of double-visit reconnections

On the complement of Bad, each vertex occurs once or twice, and each directed
edge occurs once. At a double vertex there are exactly two ways to match its
incoming edge occurrences to its outgoing occurrences. Choose either the
original matching or the switched one.

Let gamma=(0 1 ... m-1) be the original successor cycle, and let tau_A be the
product of transpositions joining the two occurrence slots of each switched
vertex in a subset A of the K chords. The reconnection forms a single Euler
circuit precisely when gamma tau_A is a single cycle.

Consequently

    c(nu(X))/m = T(eta_N),
    T(eta)=#{A subset chords: gamma tau_A is one cycle},       (16)

on the good event. With repeated edges but no triple vertices, the exact
formula has an additional denominator product_ab nu_ab!, which is explicitly
retained in the finite verifier. It is only one on the good event.

The functional T is at most 2^K and depends only on the circular order of
endpoints. Coincident endpoints have zero probability in the limiting Poisson
diagram. Equations (12), (15), (16) therefore justify convergence of its
expectation in (8).

For j selected uniform chords, contract the unselected time positions. The
question becomes whether a fixed 2j-cycle times a uniform perfect matching
has one cycle. The classical Harer-Zagier formula gives

    a_j = Pr(one cycle) = 1/(j+1) if j is even, and 0 if j is odd,
    a_0=1.                                                   (17)

For explicit verification of the specialization, its generating identity is

    1+2 sum_(j>=0) z^(j+1) E[y^(#cycles(gamma tau))]
            = ((1+z)/(1-z))^y.

Take the coefficient of y. The right side is
log((1+z)/(1-z))=2 sum_(g>=0) z^(2g+1)/(2g+1), proving (17).
This is an imported established combinatorial identity, not a new discovery.
A primary proof read in this continuation is Pittel, arXiv:1503.05598v1,
Eq. (1.1) and Section 2.

Conditional on K=k, each j-chord subdiagram is uniform. Hence

    E[T | K=k] = sum_(j even<=k) binom(k,j)/(j+1)
               = integral_0^1 [(1+x)^k+(1-x)^k]/2 dx
               = 2^k/(k+1).                                (18)

Averaging a Poisson K of mean lambda gives

    E T = exp(-lambda) sum_(k>=0) (2lambda)^k/[k!(k+1)]
        = (exp(lambda)-exp(-lambda))/(2lambda)
        = sinh(lambda)/lambda.                             (19)

Combining (8), (9), (12), (15)-(19) proves (4).

## 6. Cyclic pairs and the first noncyclic scale

Let d(x) be the least cyclic period and define

    D_(N,m)=sum_x d(x) product_j P_(x_j,x_(j+1)).

Exactly,

    0 <= m Tr P^m-D_(N,m)
       <= C m^2 (C/N)^(m/2).                               (20)

Indeed every proper period l dividing m has l<=m/2; repeating an l-word
costs at most (C/N)^(m-l) times its single weight, and Tr P^l<=C.
There are at most m periods, and the multiplicity loss is at most m.
Equations (9), (20) prove (5).

The sum over all numbers of switched vertices can be written

    F(c)=sum_(g>=0) lambda^(2g)/(2g+1)!,  lambda=c^2/2.        (21)

In particular F(c)=1+c^4/24+O(c^8) as c->0. One switched double visit
splits a circuit rather than giving a second single circuit; the first
nontrivial contribution involves two interlacing double visits. This is why
the first correction is fourth order in c, not second order.

For fixed c values:

| c | lambda=c^2/2 | F(c) |
|---:|---:|---:|
| 0.5 | 0.125 | 1.002606201929 |
| 1 | 0.5 | 1.042190610987 |
| 2 | 2 | 1.813430203924 |
| 3 | 4.5 | 10.000669144887 |

These are evaluations of the proved limiting function, not extrapolations of
the fixed-tau model from small matrix dimensions.

## 7. A finite exact enclosure in the flat-intensity class

If P=J exactly, word labels are iid uniform even under the loop measure.
Conditional on having k double vertices and m-2k singleton vertices, the chord
matching is uniform, and

    Pr(K=k,no triples)=(N)_(m-k) m! /
                           [N^m (m-2k)! k! 2^k].            (22)

Here (N)_j is a falling factorial; a term vanishes when j>N. Define

    G_(N,m)=sum_(k=0)^floor(m/2)
              (N)_(m-k) m! / [N^m (m-2k)! k! (k+1)].         (23)

This is the expectation of T on the no-triple event, before removing the
duplicate-edge factorial. It need not equal B/m at finite N.
With A_m=product_(j=0)^(m-1)(1+j/N), (11)-(12) give, for m>=3,

    max(0, G_(N,m)-24 binom(m,2) A_m/N^2)
       <= B_(N,m)/m
       <= G_(N,m)+6 binom(m,3) A_m/N^2.                     (24)

Both endpoints can be computed with exact rational arithmetic; no random
sampling and no floating spectral calculation is needed. The verifier
compares (23)-(24) against direct word enumeration for small N,m and computes
four larger rigorous enclosures. At N=100003, m=316 it gives, rounded outward,

    1.04023 < B_(N,m)/m < 1.04558.

The limiting c=1 value is 1.042190610987. This numerical example is for the
exact flat-intensity class, not a practical estimate of the startup of FM-021.

## 8. Original BGS application and the unclosed signed remainder

The actual family is unchanged:

    U_N=exp(i tau N Op_N(g)) M_N, tau=10^-80, N odd,
    M_xy=N^-1/2 e_N[-8^-1(3x^2-2xy+3y^2)],
    g(q,p)=cos(14pi q)+r(q)/10+r(q)sin(2pi q)/100-1/10
             +r(q+1/2)cos(2pi p-alpha)/100,
    r(q)=(1-cos14pi q)(1+cos2pi q),
    cos(alpha)=-3/5, sin(alpha)=4/5.

The maintained FM-021 theorem and its four-branch parametrix state eventual
max P_ab<=C/N and ||P-J||<=1/2 at exactly this fixed parameter, on all odd N.
Using those analytic project inputs, (4)-(5) therefore apply to this physical
family. No parameter average, prime restriction, altered kick, independent
quantum phases, or Egorov extension to sqrt(N) is introduced in the theorem.
Those inherited proofs have NOT been independently re-certified in this pass.

Nevertheless the full square trace is

    |Tr U_N^m|^2=B_(N,m)+R_(N,m),                            (25)

where R includes unequal-edge path pairs with all their complex signs.
The theorem does not evaluate R. Nor does local CUE statistics require the
pointwise quantity |Tr U_N^m|^2/m to approach one: the target is the full
appropriately weighted comparison, not pointwise equality with a Haar mean.

At m of order N, triple and higher visits have extensive weight; the rare-event
bound (12) no longer tends to zero, and the Poisson chord limit cannot be
substituted there. This is a specific obstruction to extrapolating (4), not
a claim that an extension is mathematically impossible.

The desired target still is

    N^-2 sum_m w(m/N) [|Tr U_N^m|^2-min(m,N)] ->0,             (26)

followed by the all-fixed-order signed factorial hierarchy. No estimate
proving (26) has been obtained in this note. The scale sqrt(N) remains o(N);
computing this positive subfamily is not closing the Heisenberg signed problem.

The determinant organization of the prior note remains exact:

    H_r(U)=m [z^r] {-log det(I-diag(z)U)}, |r|=m.

It handles counting, but a bound on the needed full coefficients (or their
signed products) is still absent. The result here is a nontrivial evaluation
of a specific polynomial-time sector, not a rebranding of that missing bound.

## 9. Evidence, provenance, and limitations

Executed command:

    python -O verify_collision_crossover.py

The standard-library verifier completed:

- 7,867 rooted words grouped into 951 edge tables, checked against exact BEST
  determinants and factorial domination;
- 1,710 no-triple word checks of the switched-cycle formula, including the
  parallel-edge factorial denominator;
- all 11,465 perfect matchings through six chords, checking both (17) and
  the all-subset average (18) by explicit permutations;
- 5,910 permutations used to check the weighted equality lemma for several
  constraint partitions, with rational weights;
- exact non-flat rational Markov-loop tests at N=3,m=5,6,7;
- four exact-rational flat-intensity enclosures via (23)-(24).

No ordinary assert is used: checks remain active under python -O. Numbers
shown as decimals are presentations of exact rational bounds or limiting
constants. Finite tests do not prove the Poisson limit or the asymptotic theorem;
the proof is Sections 2-6.

Primary sources and explicit credit:

1. B. Pittel, Another proof of Harer-Zagier formula,
   https://arxiv.org/html/1503.05598v1 , Eq. (1.1) and Section 2;
   published as Electron. J. Combin. 23(1) (2016), P1.21.
   Only the established chord-count identity is imported.
2. G. Tanner, Spectral statistics for unitary transfer matrices of binary graphs,
   https://arxiv.org/abs/nlin/0001025 . Exponentially large degeneracy families
   and compensating unitarity correlations are not claimed as discoveries here.
3. The prior attached edge-occupation THEOREM.md, 15 October 2026, for the rooted
   BEST counting setup; all needed formulas are restated and checked above.
4. ChurilovMaksim/BGS, mathematics/position_chain_mixing.md,
   blob 362ecbfe57040a99fb160bf757bc74259658dc63, and its stated
   mathematics/four_branch_parametrix.md dependency.

The quantitative combination in this note has not received an external referee
review or a complete literature-priority investigation. The Harer-Zagier
formula, BEST counting, and permutation insertion mechanism are standard prior
mathematics. No Fields-level or BGS-solution claim is made.

## 10. The exact determinant cancellation was also checked

The promised determinant-side resummation has a very short exact form.
For a fixed chord diagram with K>=1 double vertices, include ALL reconnections,
not just the ones producing one circuit. Write c_A for the number of cycles
of gamma tau_A. The sign of a permutation gives

    (-1)^c_A = (-1)^m sign(gamma tau_A) = -(-1)^|A|.

Consequently

    sum_(A subset {1,...,K}) (-1)^c_A = -(1-1)^K = 0.         (27)

Thus the repeated-vertex family cancels exactly in the signed cycle-cover
expansion, whereas restricting to ONE circuit gives the positive quantity T.
This is the local permutation version of the multiaffine identity

    det(I-diag(z)U)=sum_(I subset {1,...,N})
                      (-1)^|I| det(U_(I,I)) product_(i in I) z_i.

No coordinate occurs twice in a monomial of this determinant. Such finite
pseudo-orbit resummations and their relation to unitary subdeterminants are
established in Band--Harrison--Joyner, arXiv:1205.4214, and
Waltner--Gnutzmann--Tanner--Richter, arXiv:1209.3131. They are explicitly
credited rather than advertised as a new BGS argument.

The verifier now checks (27) by actual cycle counting for every perfect
matching with 1 through 6 chords, in addition to the positive one-cycle tests.

Crucially, the spectral statistic uses the logarithmic derivative, not the
polynomial alone. With p_U(z)=det(I-zU), r=exp(-s/N),

    N^-2 sum_(m>=1) r^(2m) |Tr U^m|^2
      = (1/(2pi N^2)) integral_0^(2pi)
           |r exp(i theta) p_U'(r exp(i theta))/p_U(r exp(i theta))|^2 d theta.
                                                                    (28)

This follows from the convergent logarithmic-derivative series in |z|<1 and
Parseval. Identity (27) does NOT estimate the denominator in (28) at distance
of order 1/N from the spectrum. In particular, exact determinant cancellation
and the square-root positive-sector law do not establish the required CUE
limit (1-exp(-2s))/(4s^2) for (28) at the prescribed U_N. The attempt reached
this explicit remaining obstruction; it did not remove it.
