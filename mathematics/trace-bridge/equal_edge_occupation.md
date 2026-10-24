# Exponentially large equal-edge contributions at Heisenberg times

**Subsequent flat-class continuation:** [BGS-TRACE-093](gaussian_equal_edge.md)
proves Gaussian comparison for every m=o(N), the exact exponential rate at
m/N->alpha>0 and the Wick collision mean. The present proof and its non-flat
hypotheses retain their original scope. The classical Gaussian crossover is
credited to Kristjansen--Plefka--Semenoff--Staudacher (2002).


**Stable claim:** `BGS-TRACE-088`. **Integration review:** 16 October 2026, author self-review.

**Exact scope:** Dense-mixing intensities with a fixed C and rho<1; cancellation is established only to an O(N^2) remainder. Equal-edge is smaller than the vertex-balanced sector.

Canonical status is [the claim ledger](../../record/claim_ledger.md); source `S12` is preserved verbatim in [the imported record](../../archive/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md#s12). Original execution counts are historical; fresh execution is recorded in [the integration receipt](../../archive/evidence/executions/20261016/chat-integration/receipt.json).


Date: 15 October 2026.

**Status:** a self-contained exact counting formula and an asymptotic theorem
for dense, uniformly mixing unistochastic matrices. Application to the frozen
BGS family uses the explicitly stated project input FM-021 and its four-branch
parametrix. This is NOT a proof of the pair CUE limit, the signed all-order
hierarchy, or BGS. The original note predates this canonical integration. No independent external
refereeing, formal verification, or world-priority claim is made.

The qualitative phenomenon of exponentially large periodic-orbit degeneracy
contributions and the need for compensating unitarity correlations was already
identified by Gregor Tanner (2000). The contribution of this note is the exact
rooted multiplicity normalization, a dense-mixing quantitative bound, and its
precise application boundary. The BEST theorem and directed matrix-tree theorem
are established mathematics, not discoveries of this project.

## 1. The complete, exactly counted family

Let U be an N by N unitary matrix and P_ab=|U_ab|^2. For a rooted closed word
x=(x_0,...,x_(m-1)), with x_m=x_0, set

    A(x)=product_(j=0)^(m-1) U_(x_j,x_(j+1)),
    nu_ab(x)=#{j: x_j=a, x_(j+1)=b}.

Then Tr U^m=sum_x A(x). Let c(nu) be the number of rooted words with edge
multiplicity matrix nu. Define

    B_(N,m)=sum_(x,y:nu(x)=nu(y)) A(x) conjugate(A(y)).

Identical edge multiplicities imply exactly identical complex amplitudes,
not just approximately equal actions. Therefore

    B_(N,m)=sum_nu c(nu)^2 product_ab P_ab^(nu_ab) >=0.       (1)

All rooted words, repetitions, loops, and nonprimitive cycles are included,
exactly once. This does not define the whole phase-balanced/vertex-occupation
sector; equal edges is a smaller, explicitly defined family.

## 2. Exact rooted BEST formula

An edge type of a nonempty closed word is a connected Eulerian directed
multigraph on its active vertices. Write

    r_a=sum_b nu_ab=sum_b nu_ba,  m=sum_a r_a.

Let t(nu) denote the common directed spanning-tree cofactor of
L=diag(r)-nu, restricted to the active vertices, with one row and column
deleted. The trees point toward the deleted root. Loops do not contribute to
L's diagonal. If there is only one active vertex, use the empty determinant 1.
Then

    c(nu)= m t(nu) product_(a:r_a>0)(r_a-1)!
                      / product_ab nu_ab!.                 (2)

For a disconnected support with edges in more than one component there is no
single closed word visiting all those edges, so c(nu)=0.

Proof of normalization: temporarily distinguish parallel directed edges.
With a specified initial vertex a and unrestricted initial edge, the last-exit
construction counts

    r_a t_a(nu) product_b(r_b-1)!

rooted labelled Euler tours. The final outgoing edges from all vertices other
than a form an arborescence toward a. Conversely, choose that arborescence and
orders of the other outgoing edges and follow unused edges in order. The last
exits prevent termination away from the root or stranding unused edges. In an
Eulerian graph all tree cofactors t_a agree (equivalently, the adjugate of the
balanced Laplacian has equal entries). Sum r_a over roots to obtain m.
Each rooted vertex word has exactly product nu_ab! assignments of parallel-edge
labels. Dividing by this number proves (2), including periodic rooted words.

Two elementary factorial inequalities give a useful bound:

    (r-1)! >= 2^((r-2)_+)  for r>=1,
    n! <= 2^(n(n-1)/2)     for n>=0.

Every graph realized by a closed word has t(nu)>=1. Put

    C_edge(x)=sum_ab binom(nu_ab(x),2),
    V_j(x)=#{a:r_a(x)=j}.

Since sum_a(r_a-2)_+=m-2N+2V_0+V_1, (2) yields

    c(nu(x)) >= m 2^(m-2N+2V_0(x)+V_1(x)-C_edge(x)).       (3)

## 3. An exact change of measure, not a new random quantum model

Let

    Z_(N,m)=Tr P^m=sum_x product_j P_(x_j,x_(j+1)).

When Z>0, define the probability of a closed word by

    Prob_loop(x)=product_j P_(x_j,x_(j+1))/Z.

This is only a convenient normalization of positive deterministic path weights.
It does not replace U with a random matrix. Equation (1) gives exactly

    B_(N,m)=Z E_loop[c(nu(X))].                             (4)

Jensen's inequality applied to (3) now proves the finite bound

    log(B_(N,m)/(m Z)) >= log(2) [m-2N
                      +2 sum_a Prob(R_a=0)
                      +  sum_a Prob(R_a=1)
                      -E C_edge],                         (5)

where R_a is the number of visits to a in the rooted m-word. Formula (5)
requires no mixing assumption.

## 4. Dense mixing forces an extensive multiplicity contribution

Assume, along N tending to infinity,

    max_ab P_ab <= C/N,
    ||P-J_N||_(2->2) <= rho <1,    (J_N)_ab=1/N,             (6)

with C and 0<rho<1 independent of N. P is doubly stochastic because U is unitary.
Let m=m_N satisfy m/N -> alpha in (0,infinity).

### 4.1. Normalization of the closed path law

Doubly stochasticity gives P^m-J_N=(P-J_N)^m. Hence

    |Z_(N,m)-1| <= N rho^m ->0.                             (7)

For every l>=1,

    (P^l)_ab <= C/N,                                       (8)

because multiplying a column bounded by C/N by a row-stochastic matrix
preserves that bound. Also |(P^l)_ab-1/N|<=rho^l.

### 4.2. Uniform Poisson limit for one vertex's visit count

For fixed k>=1 and fixed vertex a,

    E(R_a)_k = k!/Z sum_(0<=t_1<...<t_k<m)
                   product_(j=1)^k (P^(g_j))_aa,            (9)

where g_j=t_(j+1)-t_j, and the final cyclic gap is m-t_k+t_1.
For k=1 this means g_1=m.

Choose L_N=ceil(3 log N/|log rho|). The number of selected k-tuples having
any cyclic gap below L_N is O_k(L_N m^(k-1)). Their contribution, using (8),
is O_(k,C,alpha)(log N/N). On every remaining tuple,

    product_j(P^(g_j))_aa=N^(-k)(1+o(1)),

uniformly in a. Thus

    E(R_a)_k -> alpha^k uniformly in a.                     (10)

The same exact formula gives the bound

    E(R_a)_k <= (C m/N)^k/Z.

It allows dominated convergence in the falling-factorial expansion of
E z^(R_a), uniformly on compact subsets of the complex z-plane. Consequently

    Prob(R_a=0) -> exp(-alpha),
    Prob(R_a=1) -> alpha exp(-alpha),                       (11)

uniformly over a. These limits use ordinary dense Markov-loop mixing, not
spectral universality of U.

### 4.3. Directed edge repetitions have bounded mean

For two nonadjacent edge times separated by k, 2<=k<=m-2, their probability
of having identical ordered endpoints is

    (1/Z) sum_ab P_ab^2 (P^(k-1))_ba (P^(m-k-1))_ba
       <= C^3/(Z N^2).                                    (12)

Indeed sum_ab P_ab^2<=C. For adjacent times, equality of edges forces a
self-loop repeated twice; its probability is

    (1/Z) sum_a P_aa^2 (P^(m-2))_aa <= C^3/(Z N^2).

The same applies across the cyclic boundary. These formulas hold for m>=3.
Summing over pairs of times yields

    E C_edge <= C^3 m(m-1)/(2 Z N^2)=O(1).                  (13)

### 4.4. Exponential lower bound

Insert (7), (11), (13) into (5). Define

    h(alpha)=alpha-2+(alpha+2) exp(-alpha).

It is positive for every alpha>0: h(0)=0 and
h'(alpha)=1-(alpha+1)exp(-alpha)>0. We obtain

    liminf_(N->infinity) (1/N) log B_(N,m_N)
         >= h(alpha) log 2 >0.                             (14)

Equivalently, for every eta<h(alpha)log2, B_(N,m_N)>=exp(eta N)
eventually. The argument is uniform for m/N in a fixed compact subset of
(0,infinity), with the smallest h on that subset.

At alpha=1 the explicit lower exponential rate is

    (3/e-1) log 2 = 0.07183661174191525...

The use of 2^((r-2)_+) is not optimal. Keeping the full factorial in (2)
and using the uniformly bounded exponential moments of R_a improves the
rate to E[log((Poisson(alpha)-1)!)] with the value interpreted as zero at
0 and 1. No optimal exponential rate is asserted.

## 5. What unitarity already cancels, exactly

Let R_(N,m) be the sum over all remaining ordered path pairs, those with
unequal directed edge counts. Exactly,

    |Tr U^m|^2=B_(N,m)+R_(N,m).

Unitarity gives 0<=|Tr U^m|^2<=N^2, so

    -B_(N,m) <= R_(N,m) <= -B_(N,m)+N^2.                    (15)

Combining (14) and (15), R/B -> -1 exponentially fast in N (up to a
polynomial factor). This demonstrates a real collective cancellation at
Heisenberg times, but controls the final answer only to O(N^2), NOT to the
O(N) scale or the specific CUE reference needed by BGS.

There is an even more precise localization of this cancellation. Group by
vertex visits r=(r_1,...,r_N), and let

    H_r(U)=sum_(x:visits(x)=r) A(x).

If D=diag(exp(i theta_a)) with independent uniform phases, exact torus
orthogonality gives

    V_(N,m):=E_D |Tr(DU)^m|^2=sum_r |H_r(U)|^2 <= N^2.      (16)

The inequality is pointwise unitarity of DU before averaging. Thus the
cross-terms between different edge types WITHIN THE SAME vertex type already
satisfy

    V_(N,m)-B_(N,m)=-B_(N,m)+O(N^2).                        (17)

This identity is a diagnostic, not an assertion that phase averaging preserves
the original local law. Equal edges must not be confused with the entire
phase-balanced vertex sector. Independent phases on individual matrix entries
would instead produce B_(N,m), but that randomization generally destroys
unitarity and is not the diagonal-phase ensemble in (16).

All H_r have a finite formal generating function:

    H_r(U)=m [z^r] {-log det(I-D(z)U)},  |r|=m.              (18)

This follows from -log det(I-X)=sum_(m>=1)Tr(X^m)/m. Alternatively substitute
(2) and sum over edge counts with fixed row sums. Equation (18) resums the
multiplicities; it does not by itself bound the physical coefficients.

## 6. Explicit finite inequality for flat intensities

If |U_ab|^2=1/N exactly, then Z=1 and the m vertex labels are independent
uniform variables in the exact closed-word measure. For m>=3,

    Prob(R_a=0)=(1-1/N)^m,
    Prob(R_a=1)=(m/N)(1-1/N)^(m-1),
    E C_edge=m(m-1)/(2N^2).

Therefore, at every finite N and m>=3,

    B_(N,m) >= m * 2^F_(N,m),                              (19)

    F_(N,m)=m-2N+2N(1-1/N)^m
                     +m(1-1/N)^(m-1)-m(m-1)/(2N^2).

For N=m=1009 this lower bound exceeds 10^34, whereas unitarity bounds the
complete |Tr U^m|^2 by 1009^2. This is an exact-class illustration, not a
numerical threshold for the physical tau=10^-80 family.

## 7. Application to the exact frozen BGS matrices and its limits

Keep

    U_N=exp(i*10^-80*N*A_N) M_N

with the maintained full physical symbol, midpoint/raw dictionary, and all odd
dimensions. FM-021 in mathematics/position_chain_mixing.md gives the eventual
constant singular gap ||P_N-J_N||<=1/2, and the four-branch parametrix supplies
max|U_xy|^2<=C/N at the same fixed coupling. With these stated project inputs,
(14)-(17) apply to the actual family at every sequence m_N/N->alpha>0, including
composite dimensions. No artificial noise, weak-kick limit, parameter average,
prime-density condition or classical-to-quantum extension to time N is inserted
in the new theorem.

Those inherited analytic statements were read in this pass; they are not
re-certified by the finite checks. The core theorem (2), (5), (14) has a
self-contained proof from its displayed hypotheses. The source project
statements still have their original internal-review status, not independent
external certification.

The cyclic-rotation subfamily D_m studied in FM-021 has D_m~m. By contrast,
the COMPLETE equal-edge family B_(N,m) is exponentially larger and contains
non-cyclic reorderings. This is not a contradiction of D_m~m: D_m and B_(N,m)
are different subsets of the exact double sum. Fixed reconnection types or
marked endpoint cancellations cannot be extrapolated to the entire equal-edge
family without handling the multiplicities and compensating cross-types.

## 8. Remaining problem: the polynomial residual, not an exponential-sector estimate

The target remains, for each smooth compact w,

    N^-2 sum_(m>=1) w(m/N)
           [|Tr U_N^m|^2-min(m,N)] ->0,

and then the complete fixed-order factorial hierarchy. Neither (14) nor the
unitarity identity (15) estimates that residual at its required scale.

The quantitative lesson is not 'all different actions may be discarded':
doing so after retaining equal-edge degeneracies would leave an exponentially
incorrect answer. One must first keep/resum the phase relations imposed by
unitarity, including compensating terms inside each vertex-occupation class,
and then control the polynomial remainder using the physical phase structure.
The count formula (18) provides an exact, non-overcounting organization for
that attempt, but no signed CUE asymptotic is asserted for its coefficients.

An O(N) upper bound alone would still not determine the value min(m,N).
The current derivation establishes neither that bound for the specified
matrix nor the full required signed comparison. This is not closure of BGS.

## 9. Verification and sources

The autonomous Python verifier uses exact integer Bareiss determinants and
word enumeration to check (2), including loops and periodic words; it also
checks the exact multiplicity lower bound, complex trace regrouping, row-phase
Parseval via alias-free finite integration, and the explicit flat Jensen bound.
An independent rational Markov-loop calculation checks every factorial order
1 through 6 for N=3,m=6 and the repeated-edge probability bound.

Execution:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -O verify_edge_occupation.py

The completed run checked 16,284 words in 1,569 edge types, 18 exact rational
factorial-moment identities, and all displayed finite matrix controls.
Maximum complex trace-regrouping error: 3.31e-15.
Maximum row-phase Parseval error: 6.67e-15.
Proxy BGS matrices at tau=0.03 are used only in finite algebra checks; no
physical asymptotic result is inferred from them.

External primary sources consulted:

* G. Tanner, Spectral statistics for unitary transfer matrices of binary graphs,
  J. Phys. A 33 (2000), 3567-3585, DOI 10.1088/0305-4470/33/18/304;
  arXiv:nlin/0001025. Its qualitative exponentially large degeneracy contribution
  and unitarity-cancellation mechanism are explicitly acknowledged.
* M. Farrell and L. Levine, Multi-Eulerian tours of directed graphs,
  Electron. J. Combin. 23(2) (2016), P2.21, DOI 10.37236/5588;
  arXiv:1509.06237. Context for the classical BEST/last-exit counting mechanism.

Project inputs read:

* ChurilovMaksim/BGS, mathematics/position_chain_mixing.md, blob
  362ecbfe57040a99fb160bf757bc74259658dc63.
* ChurilovMaksim/BGS, mathematics/four_branch_parametrix.md, blob
  587cb2741921571bd327f93a443e3b2d2e92a690.

No whole-literature novelty audit or independent external referee acceptance
is claimed. These finite tests do not establish any N->infinity assertion;
the asymptotic proof is Sections 3-4 above.
