> Historical route checkpoint. The maintained stronger theorem is
> [BGS-TRACE-093](../../mathematics/gaussian_equal_edge_20261016.md).
> The safe 3/4 window below is not a critical threshold.

# Flat equal-directed-edge sector: a uniform Ginibre comparison

16 October 2026. New derivation from the definitions; coordinator reconstruction and finite checks; superseded range.
The finite Gaussian benchmark is established prior mathematics. No priority
claim is made for the comparison. This result concerns a positive equal-edge
sector in the flat-intensity class, not a signed trace statistic of a fixed
unitary matrix and not the BGS conjecture.

## Claim and dependency boundary

For rooted cyclic words of length m on N labels let c(nu) count words with
directed edge table nu. Set d(nu)=prod_ab nu_ab!, and

    B = N^(-m) sum_nu c(nu)^2,
    G = N^(-m) sum_nu c(nu)^2 d(nu).

G is E|Tr X^m|^2 for complex Ginibre X with entry variance 1/N.
Define

    A_m = prod_(j=0)^(m-1) (1+j/N),
    Q_m = prod_(j=0)^m (N-j)/(N+j)    if m<N,
          0                             if m>=N.

For m>=4 put

    q3 = 6/[(N+1)(N+2)],
    q22 = 4(N+5)/[(N+1)(N+2)(N+3)],
    R_(N,m) = m q3 + [binom(m,2)-m] q22.

For m=3 set R_(N,3)=3q3. Then the finite comparison is

    0 <= G-B <= (m/4) A_m R_(N,m),                         (1)

    0 <= 1-B/G <= min(1,
       m(m+1) R_(N,m) / [4(N+m)(1-Q_m)]).                 (2)

All quantities in (1)-(2) are exact rational numbers. For m=1, B=G=1;
for m=2, G=2 and B=2-1/N.

Consequently, along every sequence of positive integers m=m_N satisfying

    m=o(N^(3/4)),

one has B/G -> 1. No lower growth restriction on m is required.
The proof uses only rooted BEST counting, permutation insertion, and the
classical finite Ginibre eigenvalue kernel. It does not use a Poisson
approximation, a no-triple-visit assumption, or the fixed-crossover theorem.

## 1. Exact Gaussian benchmark, with all normalizations

Independent entry moments give E X_ab^r conjugate(X_ab)^s=0 for r!=s and
r!/N^r for r=s. Expanding both traces gives exactly the displayed definition
of G. In particular, G is not B: the parallel-edge factorial cannot be
discarded at finite N.

For an unscaled complex Ginibre Y=sqrt(N)X the established eigenvalue kernel is

    K_N(z,w) = pi^(-1) exp[-(|z|^2+|w|^2)/2]
                    sum_(j=0)^(N-1) (z conjugate(w))^j/j!.

This follows from the Gaussian Schur Jacobian and Vandermonde determinant;
the usual determinantal covariance identity then gives

    N^m G = integral |z|^(2m) K_N(z,z) d^2z
          - double_integral z^m conjugate(w)^m |K_N(z,w)|^2 d^2z d^2w
          = sum_(j=max(0,N-m))^(N-1) (j+m)!/j!.

The one-point integral is sum_(j=0)^(N-1)(j+m)!/j!; the second integral
subtracts the same terms for 0<=j<N-m. There is no subtraction when m>=N.
The hockey-stick binomial identity now proves

    G = (m!/N^m)[binom(N+m,m+1)-binom(N,m+1)]
      = [N(N+1)...(N+m)-N(N-1)...(N-m)]/[(m+1)N^m]
      = [(N+m)/(m+1)] A_m (1-Q_m).                        (3)

The falling product is interpreted as zero when m>=N. The exact benchmark
in (3), and the double-scaling sinh limit derived from it, are classical.
Primary reference: C. Kristjansen, J. Plefka, G. W. Semenoff and
M. Staudacher, *A New Double-Scaling Limit of N=4 Super Yang-Mills Theory
and PP-Wave Strings*, Nucl. Phys. B 643 (2002), 3-30,
arXiv:hep-th/0205033v2, equations (2.4), (2.8), Appendix A.
Their displayed finite formula assumes m<N; the kernel derivation above
also handles m>=N. A detailed explicit
kernel derivation is also given by S.-S. Byun and P. J. Forrester,
arXiv:2211.16223v3, Propositions 2.1-2.2, equations (2.3), (2.9)-(2.10).
The displayed integration supplies the exact specialization used here.

Source audit: equation (6.2) of Akemann--Vernizzi,
arXiv:hep-th/0212051v2, omits the factor 1/(m+1) present in its cited
Kristjansen--Plefka--Semenoff--Staudacher source. This omission is visible
in the PDF, not just in extracted text. Already m=1 would give 2N
instead of N. We therefore do not import that displayed normalization.

## 2. A sharper factorial domination on repeated-edge words

Take an iid uniformly labelled word x and write r_a for its visit counts,
F(x)=prod_a r_a!, and C_edge(x)=sum_ab binom(nu_ab(x),2). The exact rooted
BEST formula is

    c(nu)d(nu)/m = t(nu) prod_(a:r_a>0)(r_a-1)!.

For any chosen active root a, an in-arborescence chooses one of r_b
outgoing edge occurrences at every b!=a. Therefore

    t(nu) <= prod_(b!=a) r_b,
    c(nu)d(nu)/m <= F(x)/r_a.                             (4)

If C_edge>0, some directed edge is used at least twice, so its initial
vertex a has r_a>=2. Thus c(nu)d(nu)<=mF/2 on this event.
Furthermore, for any edge table,

    1-1/d(nu) <= C_edge(nu)/2.                            (5)

For C_edge=0 both sides vanish; for C_edge=1 exactly one factorial is 2
and equality holds; for C_edge>=2 the right side is at least 1.
The exact iid-word change of measure consequently gives

    G-B = E_iid[c(nu)(d(nu)-1)]
        = E_iid[c(nu)d(nu)(1-1/d(nu))]
        <= (m/4) E_iid[F C_edge].                        (6)

These are statements about exact positive counting measures. They are not
approximations of Gaussian entries or of physical quantum phases.

## 3. Exact Ewens-weighted repeated-edge expectation

For a permutation sigma on the m time slots, let I_sigma(x) mean that x is
constant on every cycle of sigma. Then

    F(x)=sum_(sigma in S_m) I_sigma(x),
    E_iid F = N^(-m) sum_sigma N^(#cycles(sigma))=A_m.       (7)

For any equality constraint pi_0 on k selected slots, the joined-cycle
partition counts distinct freely chosen labels. Hence

    E_iid[F I_(pi_0)]/A_m
       = [sum_(sigma in S_k) N^(#blocks(cycles(sigma) join pi_0))]
          /[N(N+1)...(N+k-1)].                            (8)

For completeness, deletion consistency follows by inserting a new slot
into a permutation: N units of weight form a singleton cycle, while each
existing slot gives one insertion position of weight one. After deleting
unmarked slots, the restricted permutation therefore has the same
cycle-weight law proportional to N^(#cycles). The number of cycles merged
by pi_0 depends only on this restriction, proving (8).

Two directed edge occurrences coincide when their initial slots have equal
labels and their successor slots have equal labels. For m>=3 this imposes
rank two constraints. Adjacent edge occurrences use three slots all equal,
so the numerator in (8) is 6N; this gives q3. Nonadjacent edge occurrences
use four distinct slots with two specified pairs. Exactly four permutations
preserve both pairs as separate joined blocks; the other twenty join them.
Thus the numerator is 4N^2+20N, giving q22.

There are m unordered adjacent pairs among the edges of an m-cycle for
m>=4, and binom(m,2)-m other pairs. At m=3 all three pairs are adjacent.
Summing (8) over pairs proves exactly

    E_iid[F C_edge] = A_m R_(N,m).                         (9)

Equations (3), (6), (9) prove the finite bounds (1)-(2).

## 4. Uniform range and asymptotic content

For 0<=j<N, (1-j/N)/(1+j/N)<=exp(-2j/N). Consequently

    0<=Q_m<=exp[-m(m+1)/N]

when m<N, and the same inequality is automatic when Q_m=0.
For m>=3, q3<=6/N^2 and q22<=20/N^2, so R<=10m^2/N^2.
Since 1-exp(-x)>=x/(1+x), the explicit bound implies the convenient
uniform estimate

    0 <= 1-B/G <= min(1,
       (5/2) (m^2/N^2) [1+m(m+1)/N]).                    (10)

For m=o(N^(3/4)), both terms tend to zero. At m>>sqrt(N), m=o(N),
the sharper bound (2) has leading value

    m^4/(2N^3) (1+o(1)).                                 (11)

Thus at m=cN^(3/4) it gives only limsup(1-B/G)<=min(1,c^4/2).
This is an upper bound, not a proof of a critical correction or a sharp
transition. The proof deliberately dominates the one-circuit reconnection
count by all within-vertex permutations and may lose a factor of order
m^2/N. There is no proved failure mechanism at N^(3/4) here.

The Gaussian exact formula implies, uniformly when sqrt(N)<<m=o(N),

    log G = log[N/(m+1)]
            + (N+m+1/2)log(1+m/N)-m + O(1/N).

One may instead retain the exact finite product in (3), avoiding any
truncation of this logarithm. For sqrt(N)<<m=o(N^(3/4)), expansion gives

    G = [N/(m+1)] exp[
         m(m+1)/(2N)
         -m(m+1)(2m+1)/(12N^2)
         +O(m^4/N^3)] (1+o(1)).                          (12)

Together with (10), the same holds for B. The cubic correction generally
cannot be omitted throughout the window m=o(N^(3/4)); omitting it requires
m=o(N^(2/3)). More generally, log A_(m+1) has its exact Taylor sum with a
uniform alternating-series remainder when m<N.

## 5. Open continuation and scientific disposition

The unavailable chat claim m=o(N^(3/4)) has now been reconstructed and
proved from the supplied definitions. The proof does not certify that it
is the exact proof formerly intended. The initial exponent 3/4 is superseded by BGS-TRACE-093, which proves every m=o(N). No signed physical extension to m of order N,
non-flat intensities, the physical fixed U_N trace, or BGS is established.

An exact organization of the sharper question is useful. Under the law

    Pr(sigma) proportional to N^(#cycles(sigma)),

assign independent uniform N-colours to its cycles. For the fixed successor
cycle gamma, additionally condition on gamma sigma being one cycle. The
resulting word marginal is proportional to c(nu)d(nu), and

    B/G = E_conditioned[1/d(nu)],
    Pr_Ewens(gamma sigma one cycle)=G/(m A_m).              (13)

At sqrt(N)<<m=o(N), the conditioning probability is asymptotic to N/m^2.
The domination used in (6) omits that conditioning, explaining precisely
the loss that creates the safe exponent 3/4. Controlling repeated directed
edges under (13), or an invariant Gaussian Hessian calculation, could
extend the comparison. Neither route has been closed in this note.

The verifier uses exact rational/integer word and permutation enumeration.
It separately checks (3), (4)-(5), (8)-(9), (1)-(2), (10), and the
one-circuit identity (13). It never samples Gaussian spectra and does not
assert that finite agreement proves any asymptotic statement.
